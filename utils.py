import numpy as np
import re

team_match_dict={
    'BYU':'Brigham Young',"Hawai'i":'Hawaii', 'UConn':'Connecticut',
    'Miami (Florida)':'Miami (Fla.)', 'SMU':'Southern Methodist', 
    'TCU':'Texas Christian', 'UAB':'Alabama at Birmingham', 
    'UCF':'Central Florida','USF':'South Florida','UNLV':'Nevada-Las Vegas',
    'USC':'Southern California','UTEP':'Texas-El Paso', 
    'UTSA':'Texas-San Antonio','Appalachian St.':'Appalachian State',
    'Fla. Atlantic':'Florida Atlantic',"Florida Int'l":'Florida International',
    'Western Ky.':'Western Kentucky','Middle Tenn. St.':'Middle Tennessee',
    'FIU':'Florida International','NC State':'North Carolina State','UMass':'Massachusetts',
    'Southern Miss':'Southern Mississippi','NIU':'Northern Illinois',
    'U.S. Air Force Academy':'Air Force','U.S. Military Academy':'Army','U.S. Navel Academy':'Navy',
    'Louisiana State':'LSU','Alabama-Birmingham':'Alabama at Birmingham','California, Los Angeles':'UCLA',
    'Arkansas State':'Arkansas','at Buffalo, the State  New York':'Buffalo'
} 

class DataFrameCleaner:
    def __init__(self,df):
        self.df = df
    
    def remove_chars(self,col_list=[],char_list=[],na_val=np.nan,type_coerce=str):
        for col in col_list:
            self.df[col]=self.df[col].astype(str).str.strip()
            for char in char_list:
                self.df[col]=self.df[col].str.replace(char,'')
            self.df[col]=self.df[col].replace('',np.nan)
            try:
                self.df[col]=self.df[col].astype(type_coerce)
            except ValueError as ve:
                print(f'WARNING: Type Coercsion Failed ({col})')
                print(ve)
        return self.df
      
    def keep_numeric_only(self,col_list=[],type_coerce=float):
        for col in col_list:
            self.df[col]=self.df[col].astype(str).str.strip().str.replace(r'[^\d.]+','')
            self.df[col]=self.df[col].replace('',np.nan)
            try:
                self.df[col]=self.df[col].astype(type_coerce)
            except ValueError as ve:
                print(f'WARNING: conversion to float Failed ({col})')
                print(ve)
        return self.df
        
    def remove_wiki_citation(self,col_list=None):
        if col_list == None:
            col_list = self.df.columns
        for col in col_list:
            try:
                self.df[col]=self.df[col].str.replace(r"\[([A-Za-z0-9_]+)\]",'')    
            except:
                pass