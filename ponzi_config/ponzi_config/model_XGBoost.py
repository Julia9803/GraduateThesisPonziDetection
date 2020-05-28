import logging

import pandas as pd
import xgboost as xgb
from sklearn import metrics
from sklearn.model_selection import KFold


def XGBoost(_method, _N):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(message)s',
                        level=logging.ERROR)
    basepath = "feature/feature3/"
    generatepath = "res/res3/"
    label = 3
    # method = "ALL"  # or TBF or ALL(APF+TBF)
    # N = 1  # 11 means 1~10 0 means APF, don't need N-Gram
    method = _method
    N = _N

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
    label = subtrain.Class
    x = subtrain.drop(["Class", "Id"], axis=1)
    data = x.values

    k = 10
    n_splits = 5
    res = 0
    res_recall = 0.0
    res_precision = 0.0
    f1_score = 0.0

    # # 测试集和训练集
    kf = KFold(n_splits, shuffle=False)
    for train_index, test_index in kf.split(data):
        train_x, test_x = data[train_index], data[test_index]
        train_y, test_y = label[train_index], label[test_index]
        dtrain = xgb.DMatrix(train_x, label=train_y)
        dtest = xgb.DMatrix(test_x)

        #         params={'booster':'gbtree',
        #                 'objective': 'binary:logistic',
        #                 'eval_metric': 'auc',
        #                 'max_depth':10,
        #                 'lambda':300,
        #                 'gamma':0.2,
        #                 'subsample':1.0,
        #                 'colsample_bytree':0.2,
        #                 'scale_pos_weight':0.1,
        #                 'min_child_weight':5,
        #                 'eta': 0.025,
        #                 'seed':0,
        #                 'nthread':8,
        #                 'silent':1}
        #         watchlist = [(dtrain,'train')]
        #         bst=xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)
        #         ypred=bst.predict(dtest)
        other_params = {'learning_rate': 0.1, 'n_estimators': 490, 'max_depth': 5, 'min_child_weight': 1, 'seed': 0,
                        'subsample': 0.9, 'colsample_bytree': 0.7, 'gamma': 0.1, 'reg_alpha': 1, 'reg_lambda': 2}

        bst = xgb.XGBRegressor(**other_params)
        bst.fit(train_x, train_y)
        ypred = bst.predict(test_x)
        y_pred = (ypred >= 0.5) * 1

        print('AUC: %.4f' % metrics.roc_auc_score(test_y, ypred))
        print('ACC: %.4f' % metrics.accuracy_score(test_y, y_pred))
        print('Recall: %.4f' % metrics.recall_score(test_y, y_pred))
        print('F1-score: %.4f' % metrics.f1_score(test_y, y_pred))
        print('Precesion: %.4f' % metrics.precision_score(test_y, y_pred))
        print('Table: {}'.format(metrics.confusion_matrix(test_y, y_pred)))
        matrix = metrics.confusion_matrix(test_y, y_pred)
        res += metrics.accuracy_score(test_y, y_pred)
        res_recall += metrics.recall_score(test_y, y_pred)
        res_precision += metrics.precision_score(test_y, y_pred)
        f1_score += metrics.f1_score(test_y, y_pred)

    res /= 5
    res_recall /= 5
    res_precision /= 5
    f1_score /= 5
    print("avg acc: %.4f" % res)
    print("avg precision: %.4f" % res_precision)
    print("avg recall: %.4f" % res_recall)
    print("avg f1_score: %.4f" % f1_score)
    res = {'acc': [res], 'precision': [res_precision], 'recall': [res_recall], 'f1-score': [f1_score]}
    df = pd.DataFrame(res)
    df.to_csv(generatepath + method + str(N) + "XGBoost.csv", index=False)
    df.to_json(generatepath + method + str(N) + "XGBoost.json")
    return df


if __name__ == '__main__':
    for i in range(1, 12):
        XGBoost("ALL", i)
    for i in range(1, 12):
        XGBoost("TBF", i)
    XGBoost("APF", 1)
