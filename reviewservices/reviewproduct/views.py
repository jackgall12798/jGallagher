from django.shortcuts import render
from .models import Review
def home(request) :
     return render(request, 'reviewproduct/home.html', {'title':'Home Page '})
def about(request) :
    return render(request, 'reviewproduct/about.html', {'title':'About Us'})
def contact(request) :
    return render(request, 'reviewproduct/contact.html', {'title':'Contact Us'})
#def product(request) :
 #   return render(request, 'reviewproduct/product.html', {'title':'Product Page'})

def product(request) :
       review_info= {
       'reviews': Review.objects.all()
       }
       return render(request, 'reviewproduct/product.html', review_info)


