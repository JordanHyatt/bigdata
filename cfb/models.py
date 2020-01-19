from django.db import models
from django.utils.translation import gettext_lazy as _

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

class Player(models.Model):
    ''' The Model Represents a college football Player '''
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

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    wiki_team_name = models.CharField(max_length=100)
    surface = models.CharField(max_length=200)
    capacity = models.IntegerField()
    year_built = models.IntegerField()
    year_expanded = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.name}, {self.city}, {self.state}'    
    
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
    stadium = models.ForeignKey('Stadium',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.season}, {self.team}'


class CoachPay(models.Model):
    ''' This Model represents the coaches pay for a particular season'''
    teamseason = models.ForeignKey('TeamSeason',on_delete=models.CASCADE) 
    base = models.FloatField(verbose_name='Base Salary',null=True)
    total = models.FloatField(verbose_name='Total Salary',null=True)
    bonus = models.FloatField(verbose_name='Bonus',null=True)
    bonusPaid = models.FloatField(verbose_name='Bonus Paid',null=True)
    buyout = models.FloatField(verbose_name='Buyout',null=True)
    def __str__(self):
        return f'{self.teamseason}, {self.total}'

class CfbstatsUrlId(models.Model):
    team = models.OneToOneField('Team',on_delete=models.CASCADE,related_name='cfbs')
    urlId = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.team}, {self.urlId}'


class TeamSeasonRecord(models.Model):
    class Meta:
        unique_together=[('desc','teamseason')]
    desc = models.CharField(verbose_name='Description',max_length=50)
    teamseason = models.ForeignKey('TeamSeason',on_delete=models.CASCADE) 
    win = models.IntegerField(null=True)
    loss = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.teamseason}, {self.desc}, {self.win}-{self.loss}'    

class GameResult(models.Model):
    class Meta:
        unique_together=[('teamseason','oname','date')]
    LOC_CHOICES=(('H','Home'),('A','Away'),('N','Neutral'))
    RESULT_CHOICES=(('W','Win'),('L','Loss'),('T','Tie'))
    teamseason = models.ForeignKey('TeamSeason',on_delete=models.CASCADE,related_name='game_set')
    opponent = models.ForeignKey('TeamSeason',on_delete=models.CASCADE,related_name='game_opponent_set',null=True)
    oname = models.CharField(verbose_name='Opponent Name',null=True,max_length=1)
    orank = models.IntegerField(verbose_name='Opponent Rank',null=True)
    score = models.IntegerField(verbose_name='Points Scored',null=True)
    oscore = models.IntegerField(verbose_name='Opponent Points Scored',null=True)
    date = models.DateTimeField(null=True)
    location = models.CharField(choices=LOC_CHOICES,verbose_name='Game Location',null=True,max_length=1)
    result = models.CharField(choices=RESULT_CHOICES,verbose_name='Game Result',null=True,max_length=1)
    length = models.FloatField(verbose_name='Game Length [hrs]',null=True)
    attendance = models.FloatField(verbose_name='Game Attendance',null=True)
    def __str__(self):
        return f'{self.teamseason} vs {self.oname}, {self.result} {self.score}-{self.oscore}'  


class TeamSeasonStat(models.Model):
    class Meta:
        unique_together=[('teamseason','category','desc')]
    teamseason = models.ForeignKey('TeamSeason',on_delete=models.CASCADE)
    category = models.CharField(verbose_name='Stat Category',null=True,max_length=1)
    desc = models.CharField(verbose_name='Stat Desc',null=True,max_length=1)
    value = models.FloatField(verbose_name='Team Value',null=True)
    ovalue = models.FloatField(verbose_name='Opponent Value',null=True)
    def __str__(self):
        return f'{self.teamseason}, {self.category}-|-{self.desc}, {self.value} [opp({self.ovalue})]'      





















