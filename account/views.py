from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponse


class IndexView(View):
    def get(self,request):
            return render(request,"post/index.html")
        
index = IndexView.as_view()