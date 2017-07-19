#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
import urllib
from portal.models import Teacher,Lesson,Register_student
from portal.forms import teacherform,studentfrom,Lessonform
import time,datetime,jdate
###################################Register and edit teacher ###########################################################
def edit_teacher(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method=="POST":
        form = teacherform(request.POST,request.FILES,instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            return redirect('teacherview')
    else:
        teacher = teacherform(instance=teacher)
    return render(request,'portal _ new/edit teacher.html',{'teacher':teacher})


def teacherview(request):
    teacherforms = Teacher.objects.all()
    return render(request,'portal _ new/teacher table.html', {'teacherforms': teacherforms})


def add_teacher(request):
    if request.method =='POST':
        form = teacherform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('teacherview')
        else:
            print form.errors
    else:
        form = teacherform()
    return render(request,'portal _ new/teacher form.html', {'form':form })

###################################End of register and edit teacher ####################################################







###################################register and edit student ####################################################
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
    student_code = str(jdate.jd_to_persian(jd)[0])[2:4] + str(month)+"1"+str(int(code.code[3:7])+1)[1:]
    studentforms = Register_student.objects.all()
    if request.method =='POST':
        form = studentfrom(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save(commit=True)
            father = {'to':'{0}'.format(data['father_phone'].encode('utf8')),'msg': 'گرانمایه ارجمند:آقای {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(data['last_name'].encode('utf8')),'uname':'meyticom','pass':'mme2700230'}
            #urllib.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from=100020400&{0}".format(urllib.urlencode(father)))
            #time.sleep(2)
            mother = {'to':'{0}'.format(data['mother_phone']),'msg': 'گرانمایه ارجمند:خانواده {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(data['last_name'].encode('utf8')),'uname':'meyticom','pass':'mme2700230'}
            #urllib.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from=100020400&{0}".format(urllib.urlencode(mother)))
            end_student = Register_student.objects.all()[1:]
            all_student = Register_student.objects.all().reverse()
            return redirect('all_student')
        else:
            print form.errors
    else:
        form = studentfrom()
    return render(request,'portal _ new/student form.html', {'form':form , 'studentforms': studentforms,'student_code':student_code})


def edit_student(request, pk):
    student = get_object_or_404(Register_student, pk=pk)
    if request.method == "POST":
        form = studentfrom(request.POST,request.FILES,instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            student.save()
            return redirect('all_student')
        else:
            print form.errors
    else:
        student = studentfrom(instance=student)
    return render(request, 'portal _ new/edit student.html', {'student': student})
###################################End of register and edit student ####################################################








################################### register and edit lesson ####################################################
def lesson_list(request):
    lesson = Lesson.objects.all()
    return render(request,'portal _ new/lesson table.html',{'lesson':lesson})

def add_lesson(request):
    if request.method =='POST':
        form = Lessonform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('lesson_list')
        else:
            print form.errors
    else:
        form = Lessonform()
    return render(request,'portal _ new/lesson form.html', {'form':form })


def lesson_edit(request,pk):
    lesson = get_object_or_404(Lesson,pk=pk)
    if request.method=="POST":
        form = Lessonform(request.POST,instance=lesson)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect('lesson_list')
        else:
            print form.errors
    else:
        lesson = Lessonform(instance=lesson)
    return render(request,'portal _ new/edit lesson.html',{'lesson':lesson})
################################### End of register and edit lesson ####################################################



def all_student(request):
    all = Register_student.objects.all()
    return render(request,'portal _ new/student table.html',{'all':all})



def paa(request):
    render(request,'student/index.html',{})




