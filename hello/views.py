
from django.shortcuts import render

def index(request):
    return render(request, "index.html",)
    
def count(request):
  fulltext = request.GET['fulltext']
  
  word = fulltext.split()
  
  return render(request, 'count.html',{'fulltext': fulltext,'count':len(word)})