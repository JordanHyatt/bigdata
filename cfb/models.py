from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    abrev = models.CharField(verbose_name='School Abbreviation',max_length=10)

class Coach(models.Model):
    ''' The Model Represents a college football coach '''
    lastName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)

    
class School(models.Model):
    ''' The Model Represents a college football School '''
    name = models.CharField(max_length=200)
    abrev = models.CharField(verbose_name='School Abbreviation',max_length=10)
    
class Conference(models.Model):   
    ''' The Model Represents a college football Conference '''
    name = models.CharField(max_length=200) 
    

class Season(models.Model):
    ''' The Model Represents a college football Season '''
    year = models.IntegerField() 