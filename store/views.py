from django.shortcuts import render,HttpResponse,redirect
from .models import Subscribstion,Signup_model,Product
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def home ( request):
    return render (request,'index.html')


def electronic(request):
    return render (request,'electronic.html')

def fashion(request):
    fashion=Product.objects.all()
    return render (request,'fashion.html',{'fashion':fashion})

def jewellery(request):
    return render (request,'jewellery.html')

def cart(request):
    return render (request,'cart.html')

def login(request):
    return render (request,'login.html')

def handel_login(request):
    
  if request.method=='POST':
    email=request.POST['email']
    password=request.POST['password']

    customer=Signup_model.objects.get(email=email)
    if customer:
       flag=check_password(password,customer.password)
       if flag:
          request.session['customer']=customer.id
          return redirect('home')
       else:
          msg="email and password doesnot match"
          return render(request,'login.html',{'msg':msg})
    else:
          msg="email and password doesnot match"
          return render(request,'login.html',{'msg':msg})
 







def signup(request):
    return render (request,'signup.html')

def signupsucess(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        mobile_no=request.POST['mobile_number']
        city=request.POST['city']
        password=request.POST['password']
        cnfpassword=request.POST['cnfpassword']
        
        if password != cnfpassword:
            msg='password and cnf password doesnot match'
            return render (request,'signup.html',{'msg':msg})
        else:
            if Signup_model.objects.filter(email=email):
             msg='email already exist'
             return render (request,'signup.html',{'msg':msg})
            else:

             password=make_password(password)
             msg='signup sucess ...! Now you may login ...! '
            
            Signup_model(username=username,email=email,mobile_no=mobile_no,city=city,password=password).save()
            return render (request,'login.html',{'msg':msg})
        

def subscribstion(request):
 if request.method == 'POST':
    email=request.POST['Email']
    
    if Subscribstion.objects.filter(email=email):

        msg='you already SUBSCRIBEED...!'
        return render (request,'index.html',{'msg':msg})
    else:
        Subscribstion(email=email).save()
        msg='Thanks for SUBSCRIBE...!'
        return render (request,'index.html',{'msg':msg}) 