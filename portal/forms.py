#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from portal.models import Lesson, Register_student, Financial, Teacher




class teacherform(forms.ModelForm):
    imgfile = forms.FileField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    national_code = forms.IntegerField()
    address = forms.CharField()
    mobile = forms.IntegerField()
    mail = forms.EmailField()
    class Meta:
        model = Teacher
        fields = ('imgfile','first_name', 'last_name', 'national_code', 'address', 'mobile','mail')

class Lessonform(forms.ModelForm):
    name = forms.CharField(max_length=50)
    number = forms.CharField(required=False)
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    time = forms.CharField(max_length=100,required=False)
    date = forms.CharField(max_length=50,required=False)
    class Meta:
        model=Lesson
        fields='__all__'

class studentfrom(forms.ModelForm):
    CHOICES_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','یازدهم'),('7','دهم'),
                      ('8', 'هشتم'),('9','هفتم'),('10','ششم'),('11','پنجم'),('12','چهارم'),('13','سوم'),('14','دوم'),('15','یکم'),
                      ('16', 'پیش دبستانی'),('17','عدم آغاز تحصیل'),)
    CHOICES_father_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),)
    CHOICES_mother_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','زیر دیپلم'))
    code = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'شماره صاد'}))
    imgfile = forms.FileField(required=False,)#widget=forms.FileInput(attrs={'class':'img-thumbnail'})
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'نام'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'نام خانوادگی'}))
    father_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'نام پدر'}))
    national_code = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'کد ملی'}))
    mail = forms.EmailField(required=False,widget=forms.TextInput(attrs={'placeholder' : 'ایمیل'}))
    born = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'تاریخ تولد'}))
    end_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_ejuction)
    address = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder' : 'آدرس'}))
    phone = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'منزل'}))
    mobile = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'همراه'}))
    school = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'مدرسه'}))
    school_time = forms.CharField(max_length=25,required=False,widget=forms.TextInput(attrs={'placeholder' : 'شیفت مدرسه'}))

    father_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_father_ejuction)
    father_work = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'شغل پدر'}))
    father_phone = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'همراه پدر'}))

    mother_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_mother_ejuction)
    mother_work = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'شغل مادر'}))
    mother_phone = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder' : 'همراه مادر'}))


    physical_illness = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'سابقه بیماری'}))
    physical_illness_medicine = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'داروی مصرفی'}))
    mental_illness_medicine = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'مقطع تحصیلی'}))
    mental_illness = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder' : 'مقطع تحصیلی'}))
    detail = forms.CharField(max_length=1000,required=False,widget=forms.TextInput(attrs={'placeholder' : 'مقطع تحصیلی'}))

    #teahcer = forms.ModelChoiceField(queryset=Teacher.objects.all())
    #lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())

    class Meta:
        model=Register_student
        fields =('code','imgfile','first_name','last_name','father_name','national_code','mail','born','address','phone','mobile','school','school_time',
                 'father_work','father_phone','mother_work','mother_phone','physical_illness','physical_illness_medicine','mental_illness',
                 'mental_illness_medicine','detail')

class financialform(forms.ModelForm):
    last_name = forms.CharField(max_length=50)
    mablaghe_kol = forms.CharField(max_length=50)
    takhfif = forms.CharField(max_length=50)
    pardakht_avaliye = forms.CharField(max_length=50)
    class Meta:
        model = Financial
        fields=('last_name','mablaghe_kol','takhfif','pardakht_avaliye')
