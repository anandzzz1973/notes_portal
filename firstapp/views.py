from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from firstapp.models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import cloudinary,cloudinary.uploader,cloudinary.api
import mimetypes
# Create your views here.

def loginpage(request):
	return render(request,'first.html')

def signup(request):
	return render(request,'second.html')

@login_required(login_url='/firstapp/login')
def students(request):
	user = request.user
	
	all_posts = NotesHandling.objects.all()
	return render(request,'students.html',{'all_posts':all_posts})

@login_required(login_url='/firstapp/login')
def teachers(request):
	user = request.user
	
	all_posts = NotesHandling.objects.all()
	return render(request,'teachers.html',{'all_posts':all_posts})

def register(request):

	if request.method == 'POST':
		form = request.POST

		f_name = form['firstname']
		s_name = form['lastname']
		u_type = form['usertype']
		u_email = form['email']
		u_password = form['password']

		user = User.objects.create_user(
			username = u_email,
			first_name = f_name,
			last_name = s_name,
			email = u_email,
			password = u_password
			)

		userObject = UserDetail.objects.create(
			user = user,
			user_type = u_type
			)

		message = " You have registered successfully!!!"

		return render(request,'second.html',{'info':message})

	else:
		return redirect('/firstapp/signup')


def login_P(request):
	if request.method=='POST':
		form=request.POST

		u_email = form['email']
		u_password = form['password']

		user = authenticate(request,username=u_email, password=u_password)
		if user is not None:
			login(request,user)
			useris = User.objects.get(username = u_email)

			userDetailIs = UserDetail.objects.get(user = useris)

			if userDetailIs.user_type == "Student":
				return redirect('/firstapp/students')
			else:
				return redirect('/firstapp/teachers')

		else:
			print('haha')
	else:
		return redirect('/firstapp/login')


def post(request):
	user = request.user
	userDetailIs = UserDetail.objects.get(user = user)

	if request.method == "POST":
		info_dict = None		
		form = request.POST

		title = form['title']
		desc = form['desc']
		try:
			tup = mimetypes.guess_type(request.FILES['files'].name)
			info_dict = cloudinary.uploader.upload(request.FILES['files'])
			new_notes = NotesHandling.objects.create(
				title = title,
				description = desc,
				uploaded_by = userDetailIs,
				file_url = info_dict['secure_url']
				)
		except:
			new_notes = NotesHandling.objects.create(
				title = title,
				description = desc,
				uploaded_by = userDetailIs,
				)

		if userDetailIs.user_type =='Teacher':

			return redirect('/firstapp/teachers')
		else:
			return redirect('/firstapp/students')

	else:
		return HttpResponse('haha')

def logout_view(request):
    logout(request)
    return redirect('/firstapp/login')

