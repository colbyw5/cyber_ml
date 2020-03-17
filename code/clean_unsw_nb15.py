#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:32:24 2020

@author: colbywilkinson
"""

import pandas as pd

### Read in feature names

feature_desc = pd.read_csv("https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/NUSW-NB15_features.csv",
                            encoding= 'unicode_escape',
                            index_col = False)

categorical_features = feature_desc[feature_desc['Type '] == 'nominal']['Name']



### Read in observations, compiling across the 5 files

base_url = 'https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/UNSW-NB15_'

file_names = [base_url + str(x) + '.csv' for x in range(1, 6)]

def process_pcap(url):
    
    pcap_data = pd.read_csv(url,  # read data file from source
                       names = feature_desc['Name']) 
    
    # convert text features to categorical
    
    pcap_data[categorical_features] = \
        pcap_data[categorical_features].astype('category') 
        
    pcap_data['dsport'] = pd.to_numeric(pcap_data['dsport'])
    
    pcap_data.dropna(inplace = True)
    

    
    return pcap_data

process_pcap(url = file_names[0])