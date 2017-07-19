from __future__ import unicode_literals

from django.db import models







class Teacher(models.Model):
    imgfile = models.FileField(upload_to='img_teacher/',null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.IntegerField()
    address = models.TextField()
    mobile = models.IntegerField()
    mail = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50,null=True,blank=True)
    teacher = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Register_student(models.Model):
    code = models.CharField(max_length=50,null=True)
    imgfile = models.FileField(upload_to='img_profile/',null=True,blank=True)
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=50,null=True,blank=True)
    mail = models.EmailField(null=True)
    born = models.CharField(max_length=50)
    end_ejuction = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=50,null=True,blank=True)
    school = models.CharField(max_length=50,null=True)
    school_time = models.CharField(max_length=25,null=True)

    father_ejuction = models.CharField(max_length=50,null=True)
    father_work = models.CharField(max_length=50,null=True)
    father_phone = models.CharField(max_length=50,null=True)

    mother_ejuction = models.CharField(max_length=50,null=True)
    mother_work = models.CharField(max_length=50,null=True)
    mother_phone = models.CharField(max_length=50,null=True,blank=True)


    physical_illness = models.CharField(max_length=50,null=True)
    physical_illness_medicine = models.CharField(max_length=50,null=True)
    mental_illness_medicine = models.CharField(max_length=50,null=True)
    mental_illness = models.CharField(max_length=50,null=True)
    detail = models.CharField(max_length=1000,null=True)

    teacher = models.ForeignKey(Teacher,null=True)
    lesson = models.ForeignKey(Lesson,null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Financial(models.Model):
    last_name = models.ForeignKey(Register_student,null=True)
    mablaghe_kol = models.CharField(max_length=20,null=True)
    takhfif = models.CharField(max_length=20,null=True)
    pardakht_avaliye = models.IntegerField(null=True)
    def __unicode__(self):
        return self.mablaghe_kol



class Setting(models.Model):
    sms_number = models.IntegerField(blank=True,null=True)
    sms_username = models.CharField(max_length=20,blank=True)
    sms_password = models.CharField(max_length=20,blank=True)
    father_message_sms = models.CharField(max_length=200,blank=True)
    mother_message_sms = models.CharField(max_length=200,blank=True)
    student_message_sms = models.CharField(max_length=200,blank=True)


    student_first_code = models.CharField(max_length=20,blank=False)
