# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:14:23 2019

@author: smorandv
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rm_ext_and_nan(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A dictionary of clean CTG called c_ctg
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    # CTG_features = CTG_dataset[['LB', 'AC', 'FM', 'UC', 'DL', 'DS', 'DR', 'DP', 'ASTV', 'MSTV', 'ALTV', 'MLTV',
    # 'Width', 'Min', 'Max', 'Nmax', 'Nzeros', 'Mode', 'Mean', 'Median', 'Variance', 'Tendency']]
    # c_ctg = [feature for feature in CTG_features.columns.values.tolist() if feature != extra_feature]
    # print(xx)
    # print("hulli")
    # print(CTG_features)
    # print("hallo")
    # print(
    # features = CTG_features.drop(columns=[extra_feature])
    # {k:v for (k,v) in dict1.items() if v>2}
    
    c_ctg = { key : pd.to_numeric(value, errors='coerce') for (key, value) in CTG_features.drop(columns = [extra_feature]).items() if key != extra_feature}
   
    # print(c_ctg)
    # --------------------------------------------------------------------------
    return c_ctg


def nan2num_samp(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A pandas dataframe of the dictionary c_cdf containing the "clean" features
    """
    c_cdf = {}
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    for i in CTG_features:
        if i == extra_feature:
            continue;
        c_cdf[i] = pd.to_numeric(CTG_features[i], errors='coerce').fillna(np.random.choice(CTG_features[i].astype(float, errors='ignore')))
    # { key : pd.to_numeric(value, errors='coerce') for (key, value) in CTG_features[i].fillna(np.random.choice(CTG_features[i].astype(float, errors='ignore')))  if key != extra_feature} # that was too complicated for me this time:( 
    # print(c_cdf)
    # -------------------------------------------------------------------------
    return pd.DataFrame(c_cdf)


def sum_stat(c_feat):
    """

    :param c_feat: Output of nan2num_cdf
    :return: Summary statistics as a dicionary of dictionaries (called d_summary) as explained in the notebook
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    d_summary = {value: {'min':c_feat[value].min(), 'q1': np.percentile(c_feat[value], 25), 'median': np.percentile(c_feat[value], 50), 'q3': np.percentile(c_feat[value], 75), 'max': c_feat[value].max()} for value in c_feat}
    # -------------------------------------------------------------------------
    return d_summary


def rm_outlier(c_feat, d_summary):
    """

    :param c_feat: Output of nan2num_cdf
    :param d_summary: Output of sum_stat
    :return: Dataframe of the dictionary c_no_outlier containing the feature with the outliers removed
    """
    c_no_outlier = {}
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return pd.DataFrame(c_no_outlier)


def phys_prior(c_cdf, feature, thresh):
    """

    :param c_cdf: Output of nan2num_cdf
    :param feature: A string of your selected feature
    :param thresh: A numeric value of threshold
    :return: An array of the "filtered" feature called filt_feature
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:-----------------------------

    # -------------------------------------------------------------------------
    return filt_feature


def norm_standard(CTG_features, selected_feat=('LB', 'ASTV'), mode='none', flag=False):
    """

    :param CTG_features: Pandas series of CTG features
    :param selected_feat: A two elements tuple of strings of the features for comparison
    :param mode: A string determining the mode according to the notebook
    :param flag: A boolean determining whether or not plot a histogram
    :return: Dataframe of the normalized/standardazied features called nsd_res
    """
    x, y = selected_feat
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return pd.DataFrame(nsd_res)
