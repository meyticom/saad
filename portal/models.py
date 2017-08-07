#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
    imgfile = models.FileField(upload_to='img_teacher/',default='profile-icon.png',null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    mobile = models.CharField(null=True,blank=True,max_length=12)
    mail = models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.first_name +" " + self.last_name  # ehtemal eshtebah vojod dare



class Lesson(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50,null=True,blank=True)
    teacher = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Register_student(models.Model):
    CHOICES_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','یازدهم'),('7','دهم'),
                      ('8', 'هشتم'),('9','هفتم'),('10','ششم'),('11','پنجم'),('12','چهارم'),('13','سوم'),('14','دوم'),('15','یکم'),
                      ('16', 'پیش دبستانی'),('17','عدم آغاز تحصیل'),)
    CHOICES_father_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),)
    CHOICES_mother_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','زیر دیپلم'))
    code = models.CharField(max_length=50,null=True)
    imgfile = models.FileField(upload_to='img_profile/',default='profile-icon.png',null=True,blank=True)
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,null=True,blank=True)
    national_code = models.CharField(max_length=50,null=True,blank=True)
    mail = models.EmailField(null=True)
    born = models.CharField(max_length=50)
    end_ejuction = models.CharField(max_length=50, choices=CHOICES_ejuction)
    address = models.TextField()
    phone = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=50,null=True,blank=True)
    school = models.CharField(max_length=50,null=True)
    school_time = models.CharField(max_length=25,null=True)

    father_ejuction = models.CharField(max_length=50,null=True,choices=CHOICES_father_ejuction)
    father_work = models.CharField(max_length=50,null=True)
    father_phone = models.CharField(max_length=50,null=True)

    mother_ejuction = models.CharField(max_length=50,null=True,choices=CHOICES_mother_ejuction)
    mother_work = models.CharField(max_length=50,null=True)
    mother_phone = models.CharField(max_length=50,null=True,blank=True)


    physical_illness = models.CharField(max_length=50,null=True)
    physical_illness_medicine = models.CharField(max_length=50,null=True)
    mental_illness_medicine = models.CharField(max_length=50,null=True)
    mental_illness = models.CharField(max_length=50,null=True)
    detail = models.CharField(max_length=1000,null=True)

    teacher = models.ForeignKey(Teacher,null=True)
    lesson = models.ForeignKey(Lesson,null=True)

    def __str__(self):
        return self.code

class Financial(models.Model):
    code = models.OneToOneField(Register_student,null=True,blank=True)
    kole_shahrie = models.CharField(max_length=50)
    daryafti = models.CharField(max_length=50)
    noe_takhfif = models.CharField(max_length=60,null=True,blank=True)
    shahrie_bt = models.CharField(max_length=50,null=True) #shahrie ba Ehtesabe takhfif
    baghimande = models.CharField(max_length=50)
    def __str__(self):
        return self.kole_shahrie



class Setting(models.Model):
    sms_number = models.IntegerField(blank=True,null=True,default=0)
    sms_username = models.CharField(max_length=20,blank=True)
    sms_password = models.CharField(max_length=20,blank=True)
    father_message_sms = models.CharField(max_length=200,blank=True)
    mother_message_sms = models.CharField(max_length=200,blank=True)
    student_message_sms = models.CharField(max_length=200,blank=True)
    student_first_code = models.CharField(max_length=20)
