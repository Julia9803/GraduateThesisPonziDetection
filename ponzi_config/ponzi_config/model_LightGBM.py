#!/usr/bin/env python
# coding=utf-8

import lightgbm as lgb
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def LightGBM(_method, _N):
    basepath = "feature/feature3/"
    generatepath = "res/res3/"
    label = 3
    # method = "ALL"  # or TBF or ALL(APF+TBF)
    # N = 1  # 11 means 1~10 0 means APF, don't need N-Gram
    method = _method
    N = int(_N)

    sf1 = pd.read_csv(basepath + "1gramfeature_short.csv")
    sf2 = pd.read_csv(basepath + "2gramfeature_short.csv")
    sf3 = pd.read_csv(basepath + "3gramfeature_short.csv")
    sf4 = pd.read_csv(basepath + "4gramfeature_short.csv")
    sf5 = pd.read_csv(basepath + "5gramfeature_short.csv")
    sf6 = pd.read_csv(basepath + "6gramfeature_short.csv")
    sf7 = pd.read_csv(basepath + "7gramfeature_short.csv")
    sf8 = pd.read_csv(basepath + "8gramfeature_short.csv")
    sf9 = pd.read_csv(basepath + "9gramfeature_short.csv")
    sf10 = pd.read_csv(basepath + "10gramfeature_short.csv")

    subtrainLabel = pd.read_csv('subtrainLabels' + str(label) + '.csv')
    if (method == "APF"):
        sf = sf1.drop(sf1.columns[1:-15], axis=1)
    elif (method == "TBF"):
        if (N < 11):
            sf = pd.read_csv(basepath + str(N) + "gramfeature_short.csv")
            sf = sf[sf.columns[0:-15]]
        elif (N == 11):
            sf = pd.concat(
                [sf1[sf1.columns[0:-15]], sf2[sf2.columns[1:-15]], sf3[sf3.columns[1:-15]], sf4[sf4.columns[1:-15]],
                 sf5[sf5.columns[1:-15]], sf6[sf6.columns[1:-15]], sf7[sf7.columns[1:-15]], sf8[sf8.columns[1:-15]],
                 sf9[sf9.columns[1:-15]], sf10[sf10.columns[1:-15]]], axis=1)
    elif (method == "ALL"):
        if (N < 11):
            sf = pd.read_csv(basepath + str(N) + "gramfeature_short.csv")
        elif (N == 11):
            sf = pd.concat([sf1, sf2[sf2.columns[1:-15]], sf3[sf3.columns[1:-15]], sf4[sf4.columns[1:-15]],
                            sf5[sf5.columns[1:-15]], sf6[sf6.columns[1:-15]], sf7[sf7.columns[1:-15]],
                            sf8[sf8.columns[1:-15]], sf9[sf9.columns[1:-15]], sf10[sf10.columns[1:-15]]], axis=1)

    subtrain = pd.merge(subtrainLabel, sf, on='Id')
    labels = subtrain.Class
    subtrain.drop(["Class", "Id"], axis=1, inplace=True)
    feature = subtrain.columns
    # subtrain = subtrain.values

    k = 1
    n_splits = 5
    _sum = 0
    _sum_recall = 0
    _sum_precision = 0
    _sum_f1 = 0

    X_train, X_test, y_train, y_test = train_test_split(subtrain, labels, test_size=1.0 / 3)

    lgb_train = lgb.Dataset(X_train, y_train)  # 将数据保存到LightGBM二进制文件将使加载更快
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)  # 创建验证数据

    param = {'num_leaves': 31, 'num_trees': 500, 'boosting_type': 'gbdt', 'objective': 'binary'}
    param['metric'] = ['auc', 'binary_logloss']
    num_round = 100
    # model = lgb.train(param, lgb_train, num_round, valid_sets=lgb_eval,early_stopping_rounds=10)
    bst = lgb.cv(param, lgb_train, num_round, nfold=5, early_stopping_rounds=30)
    model = lgb.train(param, lgb_train, num_boost_round=len(bst['auc-mean']))

    model.save_model(generatepath + 'lightGBM_model.txt')
    y_pred1 = model.predict(X_test, num_iteration=model.best_iteration)  # 如果在训练期间启用了早期停止，可以通过best_iteration方式从最佳迭代中获得预测
    # y_pred = model.predict(X_test)
    y_pred = (y_pred1 >= 0.5) * 1
    _matrix = confusion_matrix(y_test, y_pred)
    print(_matrix)
    acc = accuracy_score(y_test, y_pred)
    precision, recall, F1, _ = precision_recall_fscore_support(y_test, y_pred, average="binary")
    print("accuracy: {0:.4f}, precision: {1:.4f}, recall: {2:.4f}, F1: {3:.4f}".format(acc, precision, recall, F1))
    print('roc:', roc_auc_score(y_test, y_pred))
    print('Feature names:', list(feature))
    print('Feature importances:', list(model.feature_importance()))
    res = {'acc': [acc], 'precision': [precision], 'recall': [recall], 'f1-score': [F1]}
    df = pd.DataFrame(res)
    df.to_csv(generatepath + method + str(N) + "LightGBM.csv", index=False)
    df.to_json(generatepath + method + str(N) + "LightGBM.json")

    return df


if __name__ == '__main__':
    # for i in range(1, 12):
    LightGBM("APF", 1)
