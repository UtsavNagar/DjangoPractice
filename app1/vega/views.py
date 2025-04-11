from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *
# Create your views here.

def receipe(request):
    if request.method == "POST":
        data = request.POST
        
        name = data.get('name')
        description = data.get('description')
        imageFile = request.FILES.get('image')
        
        Receipe.objects.create(
            name = name,
            description = description,
            image = imageFile,
            )

    allReceipe = Receipe.objects.all()
        
    if request.GET.get("search"):
        allReceipe = allReceipe.filter(name__icontains = request.GET.get("search"))
        
    context = {"page" : "receipe","allReceipe" : allReceipe}
    return render(request, "receipe.html", context) 

def delete_receipe(request, id):
    Receipe.objects.get(id=id).delete()
    return redirect('receipe')

def update_receipe(request, id):
    querySet = Receipe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        
        querySet.name = data.get('name')
        querySet.description = data.get('description')
        image = request.FILES.get('image')
        
        if image:
            querySet.image = image
            
        querySet.save()

        return redirect('receipe')


    context = {"updateId":id,"receipe" : querySet}
    return render(request,'updateReceipe.html',context)
    
