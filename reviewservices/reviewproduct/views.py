from django.shortcuts import render
from .models import Review
from .models import Product
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
       'reviews': Review.objects.all(),
       'products': Product.objects.all()  
       }
      
       return render(request, 'reviewproduct/product.html', review_info)
def ipad(request) :
       review_info= {
       'reviews': Review.objects.all(),
       'products': Product.objects.all()  
       }
      
       return render(request, 'reviewproduct/Ipad.html', review_info)

def sonytv(request) :
       review_info= {
       'reviews': Review.objects.all(),
       'products': Product.objects.all()  
       }
      
       return render(request, 'reviewproduct/sonytv.html', review_info)
