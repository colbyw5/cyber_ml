#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:32:24 2020

@author: colbywilkinson
"""

import pandas as pd


def process_pcap(url):
    
    '''reads raw UNSW-NB15 data, converts feature types'''
    
    ### Read in feature names
    
    feature_desc = pd.read_csv("https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/NUSW-NB15_features.csv",
                          encoding= 'unicode_escape',
                          index_col = False)
    
    pcap_data = pd.read_csv(url,  # read data file from source
                       names = feature_desc['Name']) 
    
    # converting feature types
    
    cat_features = ['srcip','sport','dstip', 'dsport','proto',\
                    'state','service', 'stcpb', 'dtcpb',\
                    'is_sm_ips_ports', 'attack_cat','Label']
    
    pcap_data[cat_features] = \
        pcap_data[cat_features].astype('category') 
    
    pcap_data.dropna(inplace = True)
    
    pcap_data.drop_duplicates(inplace=True)
    
    return pcap_data

