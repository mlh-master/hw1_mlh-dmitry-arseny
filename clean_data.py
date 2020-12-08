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
    c_ctg = { key : pd.to_numeric(value, errors='coerce') for (key, value) in CTG_features.drop(columns = [extra_feature]).items()}
    # --------------------------------------------------------------------------

    return c_ctg


def nan2num_samp(CTG_features, extra_feature):
    """
    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A pandas dataframe of the dictionary c_cdf containing the "clean" features
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    c_cdf = {}
    c_ctg = CTG_features.drop(columns=[extra_feature])
    c_ctg = c_ctg.apply(lambda col: pd.to_numeric(col, errors='coerce'))
    
    for column in c_ctg.columns:
        hist = c_ctg.loc[:, column].dropna()

        def rand_sampling(x, var_hist):
            if np.isnan(x):
                rand_idx = np.random.choice(var_hist.index)
                x = var_hist[rand_idx]
            return x

        c_cdf[column] = c_ctg[[column]].applymap(lambda x: rand_sampling(x, hist))[column]
        
    # --------------------------------------------------------------------------
    
    return pd.DataFrame(c_cdf)


def sum_stat(c_feat):
    """
    :param c_feat: Output of nan2num_cdf
    :return: Summary statistics as a dicionary of dictionaries (called d_summary) as explained in the notebook
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    summary = c_feat.describe()
    summary = summary.rename({"25%": "Q1", "50%": "median", "75%": "Q3"})
    d_summary = summary.to_dict()
    for column in summary.columns:
        d_summary[column] = summary[column]
        del d_summary[column]['count']
        del d_summary[column]['mean']
        del d_summary[column]['std']
    # --------------------------------------------------------------------------
    
    return d_summary


def rm_outlier(c_feat, d_summary):
    """
    :param c_feat: Output of nan2num_cdf
    :param d_summary: Output of sum_stat
    :return: Dataframe of the dictionary c_no_outlier containing the feature with the outliers removed
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    c_no_outlier = {}
    for column in c_feat.columns:
        clean = []
        q1 = d_summary[column]['Q1']
        q3 = d_summary[column]['Q3']
        IQR = q3-q1
        outlier1 = q1-1.5*IQR
        outlier2 = q3+1.5*IQR
        for i in c_feat.index:
            x = c_feat.loc[i, column].astype(float)
            if not ((x <= outlier1) or (x >= outlier2)):
                clean.append(x)
            else:
                clean.append(np.nan)
        c_no_outlier[column] = clean
    # --------------------------------------------------------------------------
    return pd.DataFrame(c_no_outlier)


def phys_prior(c_cdf, feature, thresh):
    """
    :param c_cdf: Output of nan2num_cdf
    :param feature: A string of your selected feature
    :param thresh: A numeric value of threshold
    :return: An array of the "filtered" feature called filt_feature
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    filt_feature = [ind if ind <= thresh and ind >= 0 else np.nan for ind in c_cdf[feature]]
    # --------------------------------------------------------------------------
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
    summary = CTG_features.describe()
    summary_dict = summary.to_dict()
    ctg = CTG_features.copy()
    if mode == 'standard':
        for i in selected_feat:
            ctg[i] = (ctg[i] - summary_dict[i]['mean'])/summary_dict[i]['std']
    if mode == 'MinMax':
        for i in selected_feat:
            ctg[i] = (ctg[i] - summary_dict[i]['min'])/(summary_dict[i]['max']-summary_dict[i]['min'])
    if mode == 'mean':
        for i in selected_feat:
            ctg[i] = (ctg[i] - summary_dict[i]['mean'])/(summary_dict[i]['max']-summary_dict[i]['min'])
    modes = {'none','mean', 'MinMax', 'standard'}
    if flag == True:
        title = [x, y]
        axarr = ctg.hist(column=[x, y], bins=100, layout=(1, 2), figsize=(20, 10))
        for i, ax in enumerate(axarr.flatten()):
            ax.set_xlabel('Value')
            ax.set_ylabel('Count')
            ax.set_title(title[i])
    nsd_res = ctg
    # -------------------------------------------------------------------------
    return pd.DataFrame(nsd_res)