#!/usr/bin/env python

'''
Random experimental script to see if the inflection points
of moving averages have any advantage in predictive power.
'''

import sys
import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)
    return df

def add_moving_average(df, on='Close Price', window=20):
    '''
    WARNING: Mutates the dataframe.
    '''
    df['sma'+str(window)] = df[on].rolling(window=window).mean()

def add_slope(df, on='sma20'):
    '''
    WARNING: Mutates the dataframe
    '''
    df['slope'] = df[on] - df[on].shift(1)

def add_inflection_flags(df, slope='slope'):
    '''
    WARNING: Mutates the dataframe
    '''
    df['prev_slope'] = df[slope].shift(1)
    df['crest'] = df.apply(lambda x: x[slope] < 0 and x['prev_slope'] > 0)
    df['trough'] = df.apply(lambda x: x[slope] > 0 and x['prev_slope'] < 0)

def calculate_margins(df):
    buy_list = []
    sell_list = []
    for e in df.iterrows():
        if e[1]['crest']:
            sell_list.append(e[1]['Close Price'])
        if e[1]['trough']:
            buy_list.append(e[1]['Close Price'])
    margin = 0
    if len(buy_list) == len(sell_list):
        margin = sum(sell_list) - sum(buy_list)
    elif len(buy_list) == len(sell_list) + 1:
        # Bought one last that we didn't sell.
        margin = sum(sell_list) - sum(buy_list[:-1]) 
    elif len(buy_list) == len(sell_list) - 1:
        # Sold one before we bought anything
        margin = sum(sell_list[1:]) - sum(buy_list)
    else:
        print("Unresolvable Buy & Sell mismatch!")
        print("Bought: ", buy_list)
        print("Sold: ", sell_list)
        sys.exit(-1)
    return margin

def run(filename, window=20):
    df = load_data(filename)
    add_moving_average(df, window=window)
    add_slope(df, on='sma'+str(window))
    add_inflection_flags(df)
    margins = calculate_margins(df)
    print(margins)