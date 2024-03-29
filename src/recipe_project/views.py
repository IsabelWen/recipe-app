from django.shortcuts import render, redirect  
#Django authentication libraries           
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm    

#define a function view called login_view that takes a request from user
def login_view(request):
    #error_message to None                                 
    error_message = None   
    #form object with username and password fields                             
    form = AuthenticationForm()                            
   
    #when user hits "login" button, then POST request is generated
    if request.method == 'POST':       
        #read the data sent by the form via POST request                   
        form =AuthenticationForm(data=request.POST)
       
        #check if form is valid
        if form.is_valid():                                
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            #authenticate function to validate the user
            user=authenticate(username=username, password=password)
            if user is not None:
            #then login
                login(request, user)                
                return redirect('users:profile')
        else: 
            error_message ='Something went wrong.'

    #prepare data to send from view to template
    context ={                                             
       'form': form,
       'error_message': error_message
    }
    #load the login page using "context" information
    return render(request, 'auth/login.html', context) 

#define a function view called logout_view that takes a request from user
def logout_view(request):                                  
    logout(request)
    return render(request, 'auth/success.html') 