from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetail(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	user_type = models.CharField(max_length = 20)
	created_date_time = models.DateTimeField(auto_now_add = True)
	
class NotesHandling(models.Model):
	uploaded_by = models.ForeignKey(UserDetail,on_delete=models.CASCADE)
	title = models.TextField()
	description = models.TextField()
	uploaded_date_time = models.DateTimeField(auto_now_add = True)
	file_url = models.URLField(null = True,blank = True)

	