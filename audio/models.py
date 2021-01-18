from django.db import models
from django.contrib.auth.models import User
 


# Create your models here.
class DictationCard():
    id : str
    name : str
    link : str
    standard : str
    subject: str
    levels : str
    isschool : bool


class ExamCardDetails(models.Model):
    level_id : models.CharField(max_length=10)
    level_number = models.CharField(max_length=100)
    level_image = models.ImageField(upload_to ='pics')
    level_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    level_desc = models.CharField(max_length=500)

class DictationAudio(models.Model):
    audio_number = models.IntegerField()
    audio_name = models.CharField(max_length=100)
    audio_level = models.CharField(max_length=500)
    audio_lang = models.CharField(max_length=100)
    audio_path = models.FileField(upload_to='audio')
    audio_show = models.BooleanField()

    def __str__(self):
        return self.audio_level + "  " + str(self.audio_number) + " "+self.audio_name

class StudentEnroll(models.Model):
    stuname = models.CharField(max_length=30)
    sk = models.CharField(max_length=10,default="dummmi")
    stusubject = models.CharField(max_length=30, default="Telugu")
    stuclass = models.CharField(max_length=10)
    stuschool = models.CharField(max_length=40)
    stutown = models.CharField(max_length=30)
    stucontact = models.CharField(max_length=12)
    stuemail= models.EmailField()
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.sk + '   '+ self.stuname

class SchoolEnroll(models.Model):
    sclname = models.CharField(max_length=30)
    scladdress = models.CharField(max_length=10)
    scltown = models.CharField(max_length=40)
    sclcontact = models.CharField(max_length=12)
    sclemail= models.EmailField()

    def __str__(self):
        return self.sclname + '>> '+ self.scltown

class TeluguLevels(models.Model):
    name = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=6, unique=True)
    shortname = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nickname         

class TestSchedule(models.Model):
    name = models.ForeignKey(StudentEnroll, on_delete=models.CASCADE)
    test_nickname = models.CharField(max_length=5, default="Al1")
    subject = models.CharField(max_length=20)
    test_type = models.CharField(max_length=10)
    test_level = models.ForeignKey(TeluguLevels, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name.sk + self.name.stuname + str(self.status)

class StudentTestStats(models.Model):
    testTypes= (
        ('PRE', 'PRE'),
        ('POT', 'POT'),
        ('POOT', 'POOT'),
        ('POST', 'POST'),

    )
    name = models.ForeignKey(StudentEnroll, on_delete=models.CASCADE) # need to remove
    # schedule = models.ForeignKey(TestSchedule, on_delete=models.CASCADE)
    subject = models.CharField(max_length= 20, default="Telugu")
    testtype = models.CharField(max_length=10, default="PRE")
    level = models.CharField(max_length=20, default="SUNN")
    status = models.IntegerField(default=1)
    action = models.CharField(max_length=40, default="---")
    datenow = models.DateTimeField(auto_now_add=True)
    conductedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    timegap = models.CharField(default='-', max_length=2)
    times = models.CharField(default='-', max_length=2)   

    def __str__(self):
        return self.name.stuname

class TestMarks(models.Model):
    student = models.OneToOneField(StudentEnroll, on_delete=models.CASCADE)

    PRE_l1 = models.CharField(default=' ', max_length=2)
    PRE_g1 = models.CharField(default=' ', max_length=2)

    PRE_l2 = models.CharField(default=' ', max_length=2)
    PRE_g2 = models.CharField(default=' ', max_length=2)

    PRE_l3 = models.CharField(default=' ', max_length=2)
    PRE_g3 = models.CharField(default=' ', max_length=2)

    PRE_l4 = models.CharField(default=' ', max_length=2)
    PRE_g4 = models.CharField(default=' ', max_length=2)

    PRE_l5 = models.CharField(default=' ', max_length=2)
    PRE_g5 = models.CharField(default=' ', max_length=2)

    PRE_l6 = models.CharField(default=' ', max_length=2)
    PRE_g6 = models.CharField(default=' ', max_length=2)

    POT_l1 = models.CharField(default=' ', max_length=2)
    POT_g1 = models.CharField(default=' ', max_length=2)
    
    POT_l2 = models.CharField(default=' ', max_length=2)
    POT_g2 = models.CharField(default=' ', max_length=2)    

    POT_l3 = models.CharField(default=' ', max_length=2)
    POT_g3 = models.CharField(default=' ', max_length=2)

    POT_l4 = models.CharField(default=' ', max_length=2)
    POT_g4 = models.CharField(default=' ', max_length=2)

    POT_l5 = models.CharField(default=' ', max_length=2)
    POT_g5 = models.CharField(default=' ', max_length=2)

    POT_l6 = models.CharField(default=' ', max_length=2)
    POT_g6 = models.CharField(default=' ', max_length=2)

    POOT_l1 = models.CharField(default=' ', max_length=2)
    POOT_g1 = models.CharField(default=' ', max_length=2)

    POOT_l2 = models.CharField(default=' ', max_length=2)
    POOT_g2 = models.CharField(default=' ', max_length=2)

    POOT_l3 = models.CharField(default=' ', max_length=2)
    POOT_g3 = models.CharField(default=' ', max_length=2)

    POOT_l4 = models.CharField(default=' ', max_length=2)
    POOT_g4 = models.CharField(default=' ', max_length=2)

    POOT_l5 = models.CharField(default=' ', max_length=2)
    POOT_g5 = models.CharField(default=' ', max_length=2)

    POOT_l6 = models.CharField(default=' ', max_length=2)
    POOT_g6 = models.CharField(default=' ', max_length=2)

    POST_l1 = models.CharField(default=' ', max_length=2)
    POST_g1 = models.CharField(default=' ', max_length=2)

    POST_l2 = models.CharField(default=' ', max_length=2)
    POST_g2 = models.CharField(default=' ', max_length=2)

    POST_l3 = models.CharField(default=' ', max_length=2)
    POST_g3 = models.CharField(default=' ', max_length=2)

    POST_l4 = models.CharField(default=' ', max_length=2)
    POST_g4 = models.CharField(default=' ', max_length=2)

    POST_l5 = models.CharField(default=' ', max_length=2)
    POST_g5 = models.CharField(default=' ', max_length=2)

    POST_l6 = models.CharField(default=' ', max_length=2)
    POST_g6 = models.CharField(default=' ', max_length=2)
    
    def __str__(self):
        return self.student.stuname
