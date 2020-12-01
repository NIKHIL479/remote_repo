from django.shortcuts import render
from testapp.models import Hydjobs



# Create your views here.
def index(request):

    return render(request,'testapp/index2.html')
def hydjobs(request):
    jobs_list=Hydjobs.objects.order_by('date');
    dict={'jobs_list':jobs_list}
    return render(request,'testapp/demo2.html',context=dict)
