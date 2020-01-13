import numpy as np
import re

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
      
    def keep_numeric_only(self,col_list=[]):
        for col in col_list:
            self.df[col]=self.df[col].astype(str).str.strip().str.replace(r'[^\d.]+','')
            self.df[col]=self.df[col].replace('',np.nan)
            try:
                self.df[col]=self.df[col].astype(float)
            except ValueError as ve:
                print(f'WARNING: conversion to float Failed ({col})')
                print(ve)
        return self.df
        