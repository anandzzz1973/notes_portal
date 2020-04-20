from django.urls import path
from firstapp import views

urlpatterns = [
	path('login', views.loginpage),
	path('signup',views.signup),
	path('register/',views.register),
	path('students',views.students),
	path('teachers',views.teachers),
	path('login/',views.login_P),
	path('post_something/',views.post),
	path('logout/',views.logout_view),
]
