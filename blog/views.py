from django.shortcuts import render
#appel aux articles
from .models import Article
# Create your views here.
def home(request):
    list_artcles=Article.objects.all()
    context={"list_artcles":list_artcles}
    return render(request, 'index.html',context)


