from django.shortcuts import render
from D_App.models import User

# Create your views here.

def index(request):
	return render(request,'myapp/index.html')

def main(request):
	user_list = User.objects.order_by('First_Name')
	user_record = {'User_details':user_list}
	return render(request,'myapp/index.html',context = user_record)