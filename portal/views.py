#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
import urllib
from portal.models import Teacher,Lesson,Register_student,Setting,Financial
from portal.forms import teacherform,studentfrom,Lessonform,settingform,financialform
import time,datetime
from portal import jdate

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout
from django.http import HttpResponse,HttpResponseRedirect

###################################Register and edit teacher ###########################################################
@login_required
def edit_teacher(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method=="POST":
        form = teacherform(request.POST,request.FILES,instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            return redirect(view_teacher)
    else:
        teacher = teacherform(instance=teacher)
    return render(request,'portal _ new/edit teacher.html', {'teacher': teacher})

@login_required
def del_teacher(request,pk):
    del_teach = Teacher.objects.get(pk=pk)
    del_teach.delete()

    return redirect(view_teacher)

@login_required
def view_teacher(request):
    teacherforms = Teacher.objects.all()
    return render(request,'portal _ new/teacher table.html', {'teacherforms': teacherforms})

@login_required
def add_teacher(request):
    if request.method =='POST':
        form = teacherform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(view_teacher)
        else:
            print (form.errors)
    else:
        form = teacherform()
    return render(request,'portal _ new/teacher form.html', {'form': form })

###################################End of register and edit teacher ####################################################



###################################register and edit student ####################################################
@login_required
def add_student(request):
    student = Register_student.objects.all().last()
    set = Setting.objects.all().last()
    time = str(datetime.datetime.now())
    year = time[0:4]
    month = time[5:7]
    day = time[8:10]
    jd = jdate.gregorian_to_jd(int(year), int(month), int(day))
    if (jdate.jd_to_persian(jd)[1]) == '01'or'02'or'03':
        month ='2'
    elif (jdate.jd_to_persian(jd)[1]) == '04'or'05'or'06':
        month='3'
    elif (jdate.jd_to_persian(jd)[1]) == '09' or '08' or '07':
        month='4'
    else:month='1'

    try:
        student_code = str(jdate.jd_to_persian(jd)[0])[2:4] + str(month)+"1"+str(int(student.code[3:7])+1)[1:]
    except:
        try:
            student_code = str(jdate.jd_to_persian(jd)[0])[2:4] + str(month)+"1"+str(int(set.student_first_code[3:7])+1)[1:]
        except:
            return redirect(setting)
    studentforms = Register_student.objects.all()
    if request.method =='POST':
        form = studentfrom(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save(commit=True)
            if set.sms_username or set.sms_password or set.sms_number :
                if set.father_message_sms and data['father_phone']:
                    father = {'to':'{0}'.format(data['father_phone']),'msg': 'گرانمایه ارجمند:آقای {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(
                        data['last_name']),'uname':'{0}'.format(set.sms_username),'pass':'{0}'.format(set.sms_password)}
                    urllib.request.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from={0}&{1}".format(set.sms_number, urllib.parse.urlencode(father)))
                if set.mother_message_sms and data['mother_phone']:
                    mother = {'to': '{0}'.format(data['mother_phone']),
                              'msg': 'گرانمایه ارجمند:خانواده {0} پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(
                                  data['last_name']), 'uname': 'meyticom', 'pass': 'mme2700230'}
                    urllib.request.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from={0}&{1}".format(set.sms_number, urllib.parse.urlencode(mother)))
                if set.student_message_sms and data['mobile']:
                    sms_m = {'to': '{0}'.format(data['mobile']),
                              'msg': 'گرانمایه ارجمند:{0} عزیز پیوستن شما را به خانواده بزرگ صاد تبریک می گوییم '.format(
                                  data['first_name']),'uname':'{0}'.format(set.sms_username),'pass':'{0}'.format(set.sms_password)}
                    urllib.request.urlopen("http://37.130.202.188/class/sms/webservice/send_url.php?from={0}&{1}".format(set.sms_number,urllib.parse.urlencode(sms_m)))
            return redirect(financial)
        else:
            print (form.errors)
    else:
        form = studentfrom()
    return render(request,'portal _ new/student form.html', {'form':form , 'studentforms': studentforms,'student_code':student_code,'setting':setting})

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Register_student, pk=pk)
    if request.method == "POST":
        form = studentfrom(request.POST,request.FILES,instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            student.save()
            return redirect(all_student)
        else:
            print (form.errors)
    else:
        student = studentfrom(instance=student)
    return render(request, 'portal _ new/edit student.html', {'student': student})

@login_required
def del_student(request,pk):
    del_student = Register_student.objects.get(pk=pk)
    del_student.delete()
    return redirect(all_student)


@login_required
def all_student(request):
    all = Register_student.objects.all()
    return render(request,'portal _ new/student table.html',{'all':all})


###################################End of register and edit student ####################################################








################################### register and edit lesson ####################################################
@login_required
def lesson_list(request):
    lesson = Lesson.objects.all()
    return render(request,'portal _ new/lesson table.html',{'lesson':lesson})
@login_required
def add_lesson(request):
    if request.method =='POST':
        form = Lessonform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(lesson_list)
        else:
            print (form.errors)
    else:
        form = Lessonform()
    return render(request,'portal _ new/lesson form.html', {'form':form })

@login_required
def lesson_edit(request,pk):
    lesson = get_object_or_404(Lesson,pk=pk)
    if request.method=="POST":
        form = Lessonform(request.POST,instance=lesson)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect(lesson_list)
        else:
            print (form.errors)
    else:
        lesson = Lessonform(instance=lesson)
    return render(request,'portal _ new/edit lesson.html',{'lesson':lesson})

@login_required
def del_lesson(request,pk):
    lesson_del = Lesson.objects.get(pk=pk)
    lesson_del.delete()
    return redirect(lesson_list)
################################### End of register and edit lesson ####################################################




def paa(request):
    render(request,'student/index.html',{})

@login_required
def setting(reqest):
    data = Setting.objects.all().first()
    if reqest.method == "POST":
        form = settingform(reqest.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(setting)
        else:
            print (form.errors)
    else:
        form = settingform(instance=data)
    return render(reqest,'portal _ new/setting.html',{'form':form})






##########################################################log####################
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')




def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/students')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("شناسه شما غیرفعال می باشد.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("اطلاعات وارد شده صحیح نمی باشد!")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.سایت
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        if not request.user.is_authenticated:
            return render(request, 'portal _ new/login.html', {})
        else:
            return HttpResponse("شما وارد سایت شده اید")
###########################################################################################


def financial(request):
    if request.method =='POST':
        form = financialform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.code=Register_student.objects.all().only('code').last()
            user.save()
            return redirect(all_student)
        else:
            print (form.errors)
    else:
        form = Lessonform()
    return render(request,"portal _ new/Financial.html",{'form':form})



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def operator(request):
    return render(request, "portal _ new/operator.html")


@login_required
def main(request):
    return render(request, "portal _ new/main.html")