#!/usr/bin/env python
# coding=utf-8

from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#  from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import KFold
import sys

def RandomForest():
    basepath = "feature/feature2/"
    generatepath = "res/res2/"
    label = 2
#     method = "ALL" # or TBF or ALL(APF+TBF)
#     N = 1 # 11 means 1~10 0 means APF, don't need N-Gram
    method = sys.argv[1]
    N = int(sys.argv[2])
    
    sf1 = pd.read_csv(basepath + "1gramfeature_short.csv")
    # sf2 = pd.read_csv(basepath + "2gramfeature_short.csv")
    # sf3 = pd.read_csv(basepath + "3gramfeature_short.csv")
    # sf4 = pd.read_csv(basepath + "4gramfeature_short.csv")
    # sf5 = pd.read_csv(basepath + "5gramfeature_short.csv")
    # sf6 = pd.read_csv(basepath + "6gramfeature_short.csv")
    # sf7 = pd.read_csv(basepath + "7gramfeature_short.csv")
    # sf8 = pd.read_csv(basepath + "8gramfeature_short.csv")
    # sf9 = pd.read_csv(basepath + "9gramfeature_short.csv")
    # sf10 = pd.read_csv(basepath + "10gramfeature_short.csv")
    sf2 = pd.DataFrame()
    sf3 = pd.DataFrame()
    sf4 = pd.DataFrame()
    sf5 = pd.DataFrame()
    sf6 = pd.DataFrame()
    sf7 = pd.DataFrame()
    sf8 = pd.DataFrame()
    sf9 = pd.DataFrame()
    sf10 = pd.DataFrame()    
    
    subtrainLabel = pd.read_csv('subtrainLabels' + str(label) + '.csv')
    if(method == "APF"):
        sf = pd.read_csv("1gramfeature_short.csv")
        sf = sf[sf.columns[-15:]]
    elif(method == "TBF"):
        if(N < 11):
            sf = pd.read_csv(basepath + str(N) + "gramfeature_short.csv")
            sf = sf[sf.columns[0:-15]]
        elif(N == 11):
            sf = pd.concat([sf1[sf1.columns[0:-15]],sf2[sf2.columns[1:-15]],sf3[sf3.columns[1:-15]],sf4[sf4.columns[1:-15]],sf5[sf5.columns[1:-15]],sf6[sf6.columns[1:-15]],sf7[sf7.columns[1:-12]],sf8[sf8.columns[1:-15]],sf9[sf9.columns[1:-15]],sf10[sf10.columns[1:-15]]],axis=1)
    elif(method == "ALL"):
        if(N < 11):
            sf = pd.read_csv(basepath + str(N) + "gramfeature_short.csv")
        elif(N == 11):
            sf = pd.concat([sf1,sf2[sf2.columns[1:-15]],sf3[sf3.columns[1:-15]],sf4[sf4.columns[1:-15]],sf5[sf5.columns[1:-15]],sf6[sf6.columns[1:-15]],sf7[sf7.columns[1:-15]],sf8[sf8.columns[1:-15]],sf9[sf9.columns[1:-15]],sf10[sf10.columns[1:-15]]],axis=1)

    subtrain = pd.merge(subtrainLabel, sf1, on='Id')
    labels = subtrain.Class
    subtrain.drop(["Class","Id"], axis=1, inplace=True)
    feature = subtrain.columns
    subtrain = subtrain.values

    k = 1
    n_splits = 5
    _sum = 0
    _sum_recall = 0
    _sum_precision = 0
    _sum_f1 = 0

    kf = KFold(n_splits,shuffle=True)
    for i in range(k):
        for train_index, test_index in kf.split(subtrain):
            X_train, X_test = subtrain[train_index], subtrain[test_index]
            y_train, y_test = labels[train_index], labels[test_index]
    #     X_train, X_test, y_train, y_test = train_test_split(
    #         subtrain, labels, test_size=1.0 / 3)

    #         model = GaussianNB()    # 朴素贝叶斯
    #         model=svm.SVC(C=0.5, kernel='rbf',gamma=5 ) #SVC
    #         model = RF(n_estimators=500, n_jobs=-1)
            model = RF(criterion="entropy",n_estimators=500)
            model.fit(X_train,y_train)
            score = model.score(X_test, y_test)
            pre = model
            _sum += score
            y_pred = model.predict(X_test)
            _matrix = confusion_matrix(y_test, y_pred)
            print(_matrix)
            precision, recall, F1, _ = precision_recall_fscore_support(y_test, y_pred, average="binary")
            print ("accuracy: {0:.4f}, precision: {1:.4f}, recall: {2:.4f}, F1: {3:.4f}".format(score, precision, recall, F1))
            _sum_recall += recall
            _sum_precision += precision
            _sum_f1 += F1

        print(i)

    res = _sum /(n_splits*k)
    res_precision = _sum_precision /(n_splits*k)
    res_recall =  _sum_recall /(n_splits*k)
    f1_score = _sum_f1 /(n_splits*k)
    print("average_accuracy: {0:.4f}".format(res))
    print("average_precision: {0:.4f}".format(res_precision))
    print("average_recall: {0:.4f}".format(res_recall))
    print("average_f1-score: {0:.4f}".format(f1_score))
    res = {'acc':[res], 'precision':[res_precision], 'recall':[res_recall],'f1-score':[f1_score]}
    df = pd.DataFrame(res)
    df.to_csv(generatepath + method + str(N) + "RF.csv",index=False)

if __name__ == '__main__':
    RandomForest()