from django.shortcuts import render
from .models import Review
<<<<<<< HEAD
from .models import Product 
=======
from .models import Product
>>>>>>> 5c0a566db2634932637d369bc70b799a7e60c9be
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
<<<<<<< HEAD
       'products': Product.objects.all()
=======
       'products': Product.objects.all()  
>>>>>>> 5c0a566db2634932637d369bc70b799a7e60c9be
       }
      
       return render(request, 'reviewproduct/product.html', review_info)


