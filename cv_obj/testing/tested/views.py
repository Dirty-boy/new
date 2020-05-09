from django.shortcuts import render

# Create your views here.
from django.views import View

class Tested(View):
    def get(self,request):
        print('yunxxxxxxxxxxxxxxxxxx')
        return render(request,'dd.html')

    def post(self,request):
        pass




def CC(request):
    return render(request,'dd.html')
