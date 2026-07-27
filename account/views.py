from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import UserAccountLoginForm,UserAccountCreateForm
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

class InfoView(LoginRequiredMixin,View):
    login_url = "account:login"
    
    def get(self,request):
        return render(request,"account/info.html",{ "account" : request.user})
        
class LoginView(View):
    def get(self,request):
        form = UserAccountLoginForm()
        return render(request,"account/login.html",{"form" : form})
    
    def post(self, request):
        form = UserAccountLoginForm(request,data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("post:index")
        else:
            return render(request,"account/login.html",{"form" : form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("post:index")
    
class CreateAccountView(View):
    def get(self, request):
        form = UserAccountCreateForm()
        return render(request,"account/create.html",{"form" : form})
    
    def post(self, request):
        form = UserAccountCreateForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post:index")
        else:
            return render(request,"account/create.html",{"form" : form})
        
info_account = InfoView.as_view()
login_account = LoginView.as_view()
logout_account = LogoutView.as_view()
create_account = CreateAccountView.as_view()