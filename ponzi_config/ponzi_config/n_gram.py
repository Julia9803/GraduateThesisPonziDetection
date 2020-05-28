#!/usr/bin/env python
# coding=utf-8

# @file N-Gram.py
# @brief N-Gram
# @author Julia9803,julia925583000@gmail.com
# @version 1.0
# @date 2019-01-11 20:15:27

import re
from collections import *
import os
import pandas as pd
from math import isnan

# N = 2
V = 0
F = 5

basepath = "./subtxn3"
generatepath = "feature/feature3/"
generatelabel = "subtrainLabels3.csv"
contracts = []


def getPaymentAttribute(filename):
    df = pd.read_csv(filename)
    if len(df[df['direction'] == 'IN']) != 0:
        value_investment = df[df['direction'] == 'IN']['value'].str.split(' ', expand=True)[0].str.replace(',', '')
        tmp = pd.DataFrame(value_investment, dtype=float)
        value_investment = tmp.apply(sum).values[0]
        avg_investment = tmp.mean().values[0]
        std_investment = tmp.std().values[0]
        if isnan(std_investment):
            std_investment = 0
    else:
        value_investment = 0.0
        avg_investment = 0.0
        std_investment = 0.0

    if len(df[df['direction'] == 'OUT']) != 0:
        value_payment = df[df['direction'] == 'OUT']['value'].str.split(' ', expand=True)[0].str.replace(',', '')
        tmp = pd.DataFrame(value_payment, dtype=float)
        value_payment = tmp.apply(sum).values[0]
        avg_payment = tmp.mean().values[0]
        std_payment = tmp.std().values[0]
        if isnan(std_payment):
            std_payment = 0
    else:
        value_payment = 0.0
        avg_payment = 0.0
        std_payment = 0.0

    investment_times = len(df[df['direction'] == 'IN'])
    payment_times = len(df[df['direction'] == 'OUT'])

    if payment_times != 0:
        investment_payment_rate = investment_times / payment_times
    else:
        investment_payment_rate = investment_times + 1  #

    txn_period = df['age'].max() - df['age'].min()

    return value_investment, value_payment, len(
        df), avg_investment, std_investment, avg_payment, std_payment, investment_times, payment_times, investment_payment_rate, txn_period


## get internal txns' times for directions owner creator other
## if not internal txn value = 0
def getInternalDirections(filename):
    df = pd.read_csv(filename)
    to_add = filename.split("&")[0]
    from_add = filename.split("&")[1]
    owner = len(df[df['inter_direction'] == 0])
    investor = len(df[df['inter_direction'] == 1])
    other = len(df[df['inter_direction'] == 2])
    return owner, investor, other


def getOpcodeSequence(filename):
    global contracts
    df = pd.read_csv(filename)
    #     direction = df['direction'].tolist()
    #     txn_type = df['txn_type'].tolist()
    #     _type = df['type'].tolist()
    combine_attribute = df['direction'].str.strip() + '&' + df['txn_type'] + '&' + df['type'].apply(str)
    combine_attribute = combine_attribute.tolist()
    contracts.append({"Id": filename[16:-4], "Class": df['Class'][0]})
    return filename[16:-4], combine_attribute


def getOpcodeNgram(ops, n):
    opngramlist = [tuple(ops[i:i + n]) for i in range(len(ops) - n)]
    opngram = Counter(opngramlist)
    return opngram


def n_gram(_N):
    N = _N
    map3gram = defaultdict(Counter)
    N_investments = []
    N_payments = []
    D_index = []  # investment-payment
    Txn_len = []  # length of 1to1 txns
    Avg_investment = []
    Std_investment = []
    Avg_payment = []
    Std_payment = []
    Investment_times = []
    Payment_times = []
    Investment_payment_rate = []
    Txn_period = []
    N_owner = []
    N_creator = []
    N_other = []
    I_direction = []

    count = 1
    for each_file in os.listdir(basepath):
        # print("counting the 3-gram of the {0} file...".format(each_file))
        # print(count)
        count += 1

        investment, payment, txn_len, avg_investment, std_investment, avg_payment, std_payment, investment_times, payment_times, investment_payment_rate, txn_period = getPaymentAttribute(
            os.path.join(basepath, each_file))
        N_investments.append(investment)
        N_payments.append(payment)
        D_index.append(investment - payment)
        Txn_len.append(txn_len)
        Avg_investment.append(avg_investment)
        Std_investment.append(std_investment)
        Avg_payment.append(avg_payment)
        Std_payment.append(std_payment)
        Investment_times.append(investment_times)
        Payment_times.append(payment_times)
        Investment_payment_rate.append(investment_payment_rate)
        Txn_period.append(txn_period)

        owner, investor, other = getInternalDirections(os.path.join(basepath, each_file))
        N_owner.append(owner)
        N_creator.append(investor)
        N_other.append(other)

        ops = getOpcodeSequence(os.path.join(basepath, each_file))
        op3gram = getOpcodeNgram(ops[1], N)
        map3gram[ops[0]] = op3gram

    cc = Counter([])
    for d in map3gram.values():
        cc += d
    selectedfeatures = {}
    tc = 0
    for k, v in cc.items():
        if v >= V:
            selectedfeatures[k] = v
            #  print k,v
            tc += 1
    dataframelist = []
    for fid, op3gram in map3gram.items():
        standard = {}
        standard["Id"] = fid
        for feature in selectedfeatures:
            if feature in op3gram:
                standard[feature] = op3gram[feature]
            else:
                standard[feature] = 0
        dataframelist.append(standard)

    df = pd.DataFrame(dataframelist)
    df['Txn_len'] = Txn_len
    df['N_investments'] = N_investments
    df['N_payments'] = N_payments
    df['D_index'] = D_index
    df['Avg_investment'] = Avg_investment
    df['Std_investment'] = Std_investment
    df['Avg_payment'] = Avg_payment
    df['Std_payment'] = Std_payment
    df['Investment_times'] = Investment_times
    df['Payment_times'] = Payment_times
    df['Investment_payment_rate'] = Investment_payment_rate
    df['Txn_period'] = Txn_period
    df['N_owner'] = N_owner
    df['N_creator'] = N_creator
    df['N_other'] = N_other

    df.to_csv(generatepath + str(N) + "gramfeature_short.csv", index=False)


#     df = pd.DataFrame(contracts)
#     df.to_csv(generatelabel,index=False)

if __name__ == '__main__':
    n_gram()
