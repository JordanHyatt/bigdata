from django.db import models

class Team(models.Model):
    school = models.ForeignKey('School',on_delete=models.CASCADE)
    type = models.CharField(verbose_name='Team Type',max_length=10)
    def __str__(self):
        return f'{self.type}, {self.school}'

class Coach(models.Model):
    ''' The Model Represents a college football coach '''
    lastName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    
class School(models.Model):
    ''' The Model Represents a college football School '''
    name = models.CharField(max_length=200)
    abrev = models.CharField(verbose_name='School Abbreviation',max_length=10,null=True)
    def __str__(self):
        return f'{self.name}'
    
class Conference(models.Model):   
    ''' The Model Represents a college football Conference '''
    name = models.CharField(max_length=200) 
    def __str__(self):
        return f'{self.name}'
    
class Season(models.Model):
    ''' The Model Represents a college football Season '''
    year = models.IntegerField() 
    def __str__(self):
        return f'{self.year}'
    
class TeamSeason(models.Model):
    class Meta:
        unique_together=[('team','season')]
    team = models.ForeignKey('Team',on_delete=models.CASCADE)
    season =  models.ForeignKey('Season',on_delete=models.CASCADE)
    conference = models.ForeignKey('Conference',on_delete=models.CASCADE,null=True)
    coach = models.ForeignKey('Coach',on_delete=models.CASCADE,null=True)
    win = models.IntegerField(null=True)
    loss = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.season}, {self.team}'

class CoachPay(models.Model):
    ''' This Model represents the coaches pay for a particular season'''
    teamseason = models.ForeignKey('TeamSeason',on_delete=models.CASCADE) 
    base = models.FloatField(verbose_name='Base Salary',null=True)
    total = models.FloatField(verbose_name='Total Salary',null=True)
    bonus = models.FloatField(verbose_name='Bonus',null=True)
    buyout = models.FloatField(verbose_name='Buyout',null=True)

class CfbstatsUrlId(models.Model):
    team = models.ForeignKey('Team',on_delete=models.CASCADE)
    urlId = models.CharField(max_length=10)



















