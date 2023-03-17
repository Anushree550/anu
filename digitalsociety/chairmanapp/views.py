from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from random import*
from django.core.mail import send_mail

# Create your views here.

""" 
get(): return object

models.object.get(fieldname = htmlname) : fetch data from database (model)

uid = models.object.get()
uid.fieldname = newvalue
uid.save()    : for update data

# To store the data in model (similar to the insert query)
uid = model.objects.create(fieldname=pythonname,fieldname=pythonname)


# Fetch all the data from model (without any condition)

var = models.objects.all()
e.g. Notice.objects.all()

#fetch all data from models but condition wise



filter(): queryset

var = models.objects.filter()(fieldname = value)
"""

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'cid' : cid,
                    }
            return render(request,"chairmanapp/index.html",context)
        else:
            sid = Societymember.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'sid' : sid,
                    }
            return render(request,"societymemberapp/index.html",context)
       
    else:
        return redirect("login")

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            pemail = request.POST['email']
            ppassword = request.POST['password']
            print("------>email",pemail)
            try:
                uid = User.objects.get(email = pemail)
                if uid.password ==ppassword:
                    if uid.role == "chairman":
                        cid = Chairman.objects.get(user_id = uid)

                        print("firstname",cid.firstname)
                        print("SIGN IN BUTTON PRESS---->",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email'] = uid.email #session store
                        return redirect("home")
                    else:
                        sid = Societymember.objects.get(user_id = uid)
                        print("firstname",sid.firstname)
                        print("SIGN IN BUTTON PRESS---->",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email'] = uid.email
                        # print("-----> putting data in session",request.session['email'])
                        # context = {
                        #      'uid' : uid,
                        #      'sid' : sid,
                        # }
                        # return render(request,"societymemberapp/index.html",context)
                        return redirect("home")
                        # print("SOCIETY MEMBER")
                else:
                    context = {
                        'emsg' : "invalid password"
                    }
                print("----->something went wrong")
                return render(request,"chairmanapp/login.html",context)
            except:
                context = {
                        'emsg' : "invalid email address"
                }
                print("----->something went wrong")
                return render(request,"chairmanapp/login.html",context)
        else:
            print("===>login page refresh")
            return render(request,"chairmanapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")


def chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            
            cid.firstname = firstname
            cid.lastname = lastname
            if "pictures" in request.FILES:
                cid.pic = request.FILES['picture']

            cid.save()
                                                   
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context) 
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)  
    else:
        return redirect("login") 

def chairman_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                return redirect("logout")
            else:
                pass
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context = {
            'uid' : uid,
            'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            blockno = request.POST['blockno']
            contactno = request.POST['contactno']
            l1 = ['asd782d','sd784','sd7342c','8dj43','s78sd432','9a8s12']
            password = email[4:7]+contactno[3:7]+choice(l1)

            uid = User.objects.create(email = email,password = password,role = "societymember")
            sid = Societymember.objects.create(user_id = uid,firstname = firstname,lastname = lastname,contact_no = contactno,block_no = blockno)

            if sid:
                send_mail("Digital Society Password","Your password is: "+str(password),"anushreemehta550@gmail.com",[email])
                msg = "successfully society member created !! plz check gmail account for password"
                context = {
                    'msg' : msg,
                    'uid' : uid,
                    'cid' : cid,
                }
                return render (request,'chairmanapp/add-member.html',context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render (request,"chairmanapp/add-member.html",context)
    else:
        return redirect("login")


def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            nid = Notice.objects.create(
                user_id = uid,
                title = request.POST['title'],
                description = request.POST['description'],
            )
            nall = Notice.objects.all()
            context = {
                'uid' : uid,
                'cid' : cid,
                'nall' : nall,
            }
            return render (request,"chairmanapp/notice-list.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render (request,"chairmanapp/add-notice.html",context)
    else:
        return redirect("login")
    
def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        nall = Notice.objects.all()
        context = {
                'uid' : uid,
                'cid' : cid,
                'nall' : nall,
        }
        return render (request,"chairmanapp/notice-list.html",context)

def view_notice_details(request,pk):
    if "email" in request.session:
        print("------>PK",pk)
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        notice = Notice.objects.filter(id = pk)
        context = {
                'uid' : uid,
                'cid' : cid,
                'notice' : notice,
        }
        return render (request,"chairmanapp/notice-details.html",context)
