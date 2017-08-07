#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from portal.models import Lesson, Register_student, Financial, Teacher, Setting




class teacherform(forms.ModelForm):
    imgfile = forms.FileField(required=False)
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'14'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'15'}))
    national_code = forms.CharField(widget=forms.TextInput(attrs={'size':'16'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'size': '17'}))
    mail = forms.EmailField(required=False,widget=forms.TextInput(attrs={'size': '24'}))
    class Meta:
        model = Teacher
        fields = ('imgfile','first_name', 'last_name', 'national_code', 'address', 'mobile','mail')

class Lessonform(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'14'}))
    number = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'15'}))
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    time = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'size':'16'}))
    date = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    class Meta:
        model=Lesson
        fields='__all__'

class studentfrom(forms.ModelForm):
    CHOICES_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','یازدهم'),('7','دهم'),
                      ('8', 'هشتم'),('9','هفتم'),('10','ششم'),('11','پنجم'),('12','چهارم'),('13','سوم'),('14','دوم'),('15','یکم'),
                      ('16', 'پیش دبستانی'),('17','عدم آغاز تحصیل'),)
    CHOICES_father_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),)
    CHOICES_mother_ejuction=(('1','دکتری'),('2','فوق لیسانس'),('3','لیسانس'),('4','فوق دیپلم'),('5','دیپلم'),('6','زیر دیپلم'))

    CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
    code = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'style':'background-color:#91bae8','size': '12'}))
    imgfile = forms.FileField(required=False,)#widget=forms.FileInput(attrs={'class':'img-thumbnail'})
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'16'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'17'}))
    father_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'15'}))
    national_code = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'15'}))
    mail = forms.EmailField(required=False,widget=forms.TextInput(attrs={'size': '24'}))
    born = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'16'}))
    #end_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_ejuction)
    end_ejuction = forms.ChoiceField(choices=CHOICES) #choices=CHOICES_ejuction
    address = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'rows':'3'}))
    phone = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    mobile = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    school = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'17'}))
    school_time = forms.CharField(max_length=25,required=False,widget=forms.TextInput(attrs={'size':'16'}))

    father_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_father_ejuction)
    father_work = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'16'}))
    father_phone = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'17'}))

    mother_ejuction = forms.ChoiceField(widget=forms.Select,choices=CHOICES_mother_ejuction)
    mother_work = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    mother_phone = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'size':'17'}))


    physical_illness = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'16'}))
    physical_illness_medicine = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    mental_illness_medicine = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'16'}))
    mental_illness = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'size':'15'}))
    detail = forms.CharField(max_length=1000,required=False,widget=forms.Textarea(attrs={'rows': '3'}))

    #teahcer = forms.ModelChoiceField(queryset=Teacher.objects.all())
    #lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())

    class Meta:
        model=Register_student
        fields =('code','imgfile','first_name','last_name','father_name','national_code','mail','born','address','phone','mobile','school','school_time',
                 'father_work','father_phone','mother_work','mother_phone','physical_illness','physical_illness_medicine','mental_illness',
                 'mental_illness_medicine','detail')

class financialform(forms.ModelForm):
    class Meta:
        model = Financial
        fields='__all__'

class settingform(forms.ModelForm):
    class Meta:
        model=Setting
        fields='__all__'
