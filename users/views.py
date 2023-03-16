from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.

def index_view(request):

    if request.method == "POST":

        user_id = request.POST['username']
        password = '1234'   #password 임의 통일

        user = auth.authenticate(
            request,
            user_id=user_id,
            password=password
        )

        if user is not None:
            auth.login(request, user)

            return redirect ('/polling')
        
        else:
            return render(request, 'users/index.html')
    
    else:
        return render(request, 'users/index.html')
    
def logout_view(request):
    auth.logout(request)

    return redirect('/')