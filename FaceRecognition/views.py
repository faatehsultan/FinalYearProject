# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import models
import cv2
import os
import shutil
import numpy as np
import pickle
from datetime import datetime


# from django.contrib.auth.decorators import permission_required


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # superuser = User.objects.create_superuser(username=username, email=email, password=password)
        # superuser.save()
        data = models.admindata(username=username, email=email, password=password)
        data.save()
        # print("user created")
        return redirect('/')
    return render(request, 'signup.html')


# @permission_required('auth.view_user')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        users = models.admindata.objects.all()
        for user in users:
            if user.username == username and user.password == password:
                return render(request, 'navbar.html')
    return render(request, 'login.html')


def navbar(request):
    return render(request, 'navbar.html')


def addstudent(request):
    if request.method == "POST":
        name = request.POST['name']
        fathername = request.POST['fathername']
        address = request.POST['address']
        gender = request.POST['gender']
        department = request.POST['department']
        section = request.POST['section']
        birthdate = request.POST['birthdate']
        id = request.POST['id']
        email = request.POST['email']
        studentdata = models.student(name=name, fathername=fathername, address=address, gender=gender,
                                     department=department, section=section, birthdate=birthdate, id=id, email=email)
        studentdata.save()
        return redirect('record')
    data = models.department.objects.all()
    return render(request, 'addstudent.html',{'record': data})


def record(request):
    data = models.student.objects.all()
    return render(request, 'record.html', {"record": data})


def delete(request, id, name):
    data = models.student.objects.get(id=id, name=name)
    data.delete()
    path = "F:\\4th semester\\AOA(SIR KASHIF)\\Project\\Images\\" + name
    if os.path.isdir(path):
        shutil.rmtree(path)
    return redirect('record')


def update(request, id):
    print(id)
    if request.method == "POST":
        name = request.POST['name']
        fathername = request.POST['fathername']
        address = request.POST['address']
        gender = request.POST['gender']
        department = request.POST['department']
        section = request.POST['section']
        birthdate = request.POST['birthdate']
        id = request.POST['id']
        email = request.POST['email']
        studentdata = models.student(name=name, fathername=fathername, address=address, gender=gender,
                                     department=department, section=section, birthdate=birthdate, id=id, email=email)
        studentdata.save()
        return redirect('record')
    data = models.student.objects.get(id=id)
    return render(request, 'update.html', {"record": data})


def captureimage(request, id, name):
    imgcounter = 1
    models.student.objects.get(id=id, name=name)
    path2 = "F:\\4th semester\\clonedProject\\FinalYearProject\\Project\\Images"
    os.chdir(path2)
    SubFolder = name
    path3 = path2 + "\\" + SubFolder
    if os.path.isdir(path3):
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("Face Recognition", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                print("Escape entered, closing the app")
                break
            elif k % 256 == 32:
                img_name = name + "_{}.png".format(imgcounter)
                cv2.imwrite(os.path.join(path3, img_name), frame)
                imgcounter += 1

        cv2.waitKey(1)
        cam.release()
        cv2.destroyAllWindows()
    else:
        os.mkdir(SubFolder)
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("Face Recognition", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                print("Escape entered, closing the app")
                break
            elif k % 256 == 32:
                img_name = name + "_{}.png".format(imgcounter)
                cv2.imwrite(os.path.join(path3, img_name), frame)
                imgcounter += 1
        cv2.waitKey(1)
        cam.release()
        cv2.destroyAllWindows()
    return redirect('record')


def train(request):
    return redirect('navbar')


def adddepartment(request):
    if request.method == "POST":
        dept = request.POST['dept']
        department = models.department(dept=dept)
        department.save()
        return redirect('departments')
    return render(request, 'adddepartment.html')


def addsection(request, dept):
    if request.method == "POST":
        dept = request.POST['dept']
        section = request.POST['section']
        sections = models.sec(dept=dept, section=section)
        sections.save()
        return redirect('departments')
    data = models.department.objects.get(dept=dept)
    return render(request, 'addsection.html', {'depts': data})


def departments(request):
    data = models.department.objects.all()
    return render(request, 'departments.html', {"depts": data})


def deletedept(request, dept):
    data = models.department.objects.get(dept=dept)
    data.delete()
    return redirect('departments')
