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
    'U.S. Air Force Academy':'Air Force','U.S. Military Academy':'Army','U.S. Naval Academy':'Navy',
    'Alabama-Birmingham':'Alabama at Birmingham','California, Los Angeles':'UCLA',
    'Arkansas State':'Arkansas','at Buffalo, the State  New York':'Buffalo','University of Arkansas, Fayetteville':'Arkansas',
    'Bowling Green State':'Bowling Green','Pennsylvania State':'Penn State','Arkansas State University':'Arkansas State',
    'University of Akron': 'Akron',
    'University of Alabama at Birmingham': 'Alabama at Birmingham','Appalachian State University': 'Appalachian State',
    'Arizona State University': 'Arizona State','Auburn University': 'Auburn',
    'Ball State University': 'Ball State','Baylor University': 'Baylor',
    'Boise State University': 'Boise State','Bowling Green State University': 'Bowling Green',
    'Brigham Young University': 'Brigham Young','University at Buffalo, the State University of New York': 'Buffalo',
    'University of Central Florida': 'Central Florida','Central Michigan University': 'Central Michigan',
    'The University of North Carolina at Charlotte': 'Charlotte','University of Cincinnati': 'Cincinnati',
    'Clemson University': 'Clemson','Coastal Carolina University': 'Coastal Carolina',
    'Colorado State University': 'Colorado State','Duke University': 'Duke',
    'East Carolina University': 'East Carolina','Eastern Michigan University': 'Eastern Michigan',
    'Florida Atlantic University': 'Florida Atlantic','Florida International University': 'Florida International',
    'Florida State University': 'Florida State','Georgia Southern University': 'Georgia Southern',
    'Georgia State University': 'Georgia State','University of Hawaii, Manoa': 'Hawaii',
    'Iowa State University': 'Iowa State','Kansas State University': 'Kansas State',
    'Kent State University': 'Kent State','Liberty University': 'Liberty',
    'Louisiana Tech University': 'Louisiana Tech','University of Louisville': 'Louisville',
    'Marshall University': 'Marshall','University of Maryland, College Park': 'Maryland',
    'University of Massachusetts, Amherst': 'Massachusetts','University of Memphis': 'Memphis',
    'Michigan State University': 'Michigan State','Middle Tennessee State University': 'Middle Tennessee',
    'University of Minnesota, Twin Cities': 'Minnesota','Mississippi State University': 'Mississippi State',
    'University of Nebraska, Lincoln': 'Nebraska','New Mexico State University': 'New Mexico State',
    'North Carolina State University': 'North Carolina State','University of North Texas': 'North Texas',
    'Northern Illinois University': 'Northern Illinois','University of Notre Dame': 'Notre Dame',
    'The Ohio State University': 'Ohio State','Oklahoma State University': 'Oklahoma State',
    'Old Dominion University': 'Old Dominion','Oregon State University': 'Oregon State',
    'University of Pittsburgh': 'Pittsburgh','Purdue University': 'Purdue',
    'Rice University': 'Rice','Rutgers, The State University of New Jersey, New Brunswick': 'Rutgers',
    'San Diego State University': 'San Diego State','San Jose State University': 'San Jose State',
    'University of South Alabama': 'South Alabama','University of South Florida': 'South Florida',
    'University of Southern California': 'Southern California','Southern Methodist University': 'Southern Methodist',
    'The University of Southern Mississippi': 'Southern Mississippi','Stanford University': 'Stanford',
    'Syracuse University': 'Syracuse','Temple University': 'Temple',
    'Texas A&M University, College Station': 'Texas A&M','Texas Christian University': 'Texas Christian',
    'Texas State University': 'Texas State','Texas Tech University': 'Texas Tech',
    'University of Toledo': 'Toledo','Troy University': 'Troy',
    'Tulane University': 'Tulane','The University of Tulsa': 'Tulsa','Utah State University': 'Utah State',
    'Vanderbilt University': 'Vanderbilt','Wake Forest University': 'Wake Forest',
    'Washington State University': 'Washington State','West Virginia University': 'West Virginia',
    'Western Kentucky University': 'Western Kentucky','Western Michigan University': 'Western Michigan',
    'University of Wisconsin-Madison': 'Wisconsin','University of Wyoming': 'Wyoming',
    'University of Alabama':'Alabama','University of Arizona':'Arizona','University of Colorado, Boulder':'Colorado',
    'University of California, Los Angeles':'UCLA','University of California, Berkeley':'California',
    'University of Connecticut':'Connecticut','University of Florida':'Florida',
    'University of Tennessee at Chattanooga':'Tennessee','University of Texas at Austin':'Texas',
    'University of Georgia':'Georgia','California State University, Fresno':'Fresno State',
    'Georgia Institute of Technology':'Georgia Tech','University of Illinois Urbana-Champaign':'Illinois',
    'University of Louisiana at Lafayette':'Louisiana-Lafayette','University of Louisiana Monroe':'Louisiana-Monroe',
    'University of Missouri, Columbia':'Missouri','Louisiana State University':'LSU','Pennsylvania State University':'Penn State',
    'Indiana University, Bloomington':'Indiana','Miami University (Ohio)':'Miami (Ohio)','University of Miami (Florida)':'Miami (Fla.)',
    'University of North Carolina, Chapel Hill':'North Carolina','University of Nevada, Las Vegas':'Nevada-Las Vegas','University of Nevada, Reno':'Nevada',
    'Virginia Polytechnic Institute and State University':'Virginia Tech',
    'University of Texas at El Paso':'Texas-El Paso','University of Texas at San Antonio':'Texas-San Antonio',
    'Ohio University':'Ohio','Northwestern University':'Northwestern','University of South Carolina, Columbia':'South Carolina'
    
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