#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
import urllib
from portal.models import *
from portal.forms import *
import time,datetime,jdate




def teacher(request):
    teacherforms = Teacher.objects.all()
    if request.method =='POST':
        form = teacherform(request.POST,request.FILES)
        if form.is_valid():
            mm = Teacher(imgfile=request.FILES['imgfile'])
            mm.save()
            form.save(commit=True)
            return add_student()
        else:
            print form.errors
    else:
        form = teacherform()
    return render(request,'portal/add_teacher.html', {'form':form , 'teacherforms': teacherforms})


def add_student(request):
    code = Register_student.objects.all().last()
    time = str(datetime.datetime.now())
    year = time[0:4]
    month = time[5:7]
    day = time[8:10]
    jd = jdate.gregorian_to_jd(int(year), int(month), int(day))
    if (jdate.jd_to_persian(jd)[1]) == '01'or'02'or'03':
        month ='2'
    elif (jdate.jd_to_persian(jd)[1]) == '04'or'05'or'06' :
        month='3'
    elif (jdate.jd_to_persian(jd)[1]) == '09' or '08' or '07' :
        month='4'
    else:month='1'
    final = str(jdate.jd_to_persian(jd)[0])[2:4] + str(month)+"1"+str(int(code.code[3:7])+1)[1:]
    studentforms = Register_student.objects.all()
    if request.method =='POST':
        form = studentfrom(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            newdoc = Register_student(imgfile=request.FILES['imgfile'])
            newdoc.save()
            form.save(commit=True)
            father = {'to':'{0}'.format(data['father_phone'].encode('utf8')),'msg': 'گرانمایه ارجمند:آقای {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(data['last_name'].encode('utf8')),'uname':'meyticom','pass':'mme2700230'}
            #urllib.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from=100020400&{0}".format(urllib.urlencode(father)))
            #time.sleep(2)
            mother = {'to':'{0}'.format(data['mother_phone']),'msg': 'گرانمایه ارجمند:خانواده {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(data['last_name'].encode('utf8')),'uname':'meyticom','pass':'mme2700230'}
            #urllib.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from=100020400&{0}".format(urllib.urlencode(mother)))
            end_student = Register_student.objects.all()[1:]
            all_student = Register_student.objects.all().reverse()
            return render(request,'portal/end.html',{'end_student':end_student,'all_student':all_student})
        else:
            print form.errors
    else:
        form = studentfrom()
    return render(request,'portal/register.html', {'form':form , 'studentforms': studentforms,'final':final})

def all_student(request):
    all = Register_student.objects.all()
    return render(request,'portal/student.html',{'all':all})




def student_detail(request, pk):
    student = get_object_or_404(Register_student, pk=pk)
    if request.method == "POST":
        pass
    else:
        student = studentfrom(instance=student)
    return render(request, 'portal/student_detail.html', {'student': student})


#dont used this project
def financial(request):
#    studentforms = Register_student.objects.all()
    if request.method =='POST':
        form = financialform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return paa(request)
        else:
            print form.errors
    else:
        form = financialform()
    return render(request,'portal/financial.html',{})

def paa(request):
    render(request,'portal/hello.html',{})
