from multiprocessing import context
from django.shortcuts import render, HttpResponse
from ap19.forms import BlogForm
from ap19.forms import ReadersForm
from ap19.models import Blog
from ap19.models import Readers

def index(request):
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES)
        form2=ReadersForm(request.POST, request.FILES)
        if form.is_valid() or form2.is_valid():            
            form.save()
            form2.save()
            return HttpResponse('File saved')
    else:
        form=BlogForm()
        form2=ReadersForm()
        context={'form':form, 'form2':form2}
    return render(request, 'index.html', context)

def second(request):
    myblog=Blog.objects.all().values()
    myblog2=Readers.objects.all().values()
    context={'myblog':myblog, 'myblog2':myblog2}
    return render(request, 'second.html', context)


