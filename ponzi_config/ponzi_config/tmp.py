from model_RF import RandomForest
from model_XGBoost import XGBoost
from model_LightGBM import LightGBM
import pandas as pd
from n_gram import n_gram
import json

if __name__ == '__main__':
    # file = "res/res2/ALL2RF.json"
    # with open(file, 'r') as f:
    #     result = json.load(f)
    #     newres = {}
    #     for each in result:
    #         for item in result[each]:
    #             newres[each] = round(result[each]["0"], 4)
    #     print(newres)

    # for i in range(1, 11):
    #     n_gram(i)
    # for i in range(1, 2):
    #     RandomForest("APF", i)
    #     XGBoost("APF", i)
    #     LightGBM("APF", i)
    # for i in range(1, 12):
    #     RandomForest("TBF", i)
    #     XGBoost("TBF", i)
    #     LightGBM("TBF", i)
    for i in range(11, 12):
        RandomForest("ALL", i)

