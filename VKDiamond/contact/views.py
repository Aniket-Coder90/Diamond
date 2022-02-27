# from django.http import HttpResponse
from sqlite3 import connect
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.views import View
# from contact.forms import ContactForm
from contact.models import *
# Create your views here.

def ContactForm(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        contactno = request.POST['phone']
        textmessage = request.POST['description']
        contact = Contact(Firstname=firstname, Lastname=lastname, Email=email, ContactNo=contactno, TextMessage=textmessage)
        
        contact.save()

        return render(request, 'plugins/success.html')
    return render(request, 'contact/index.html')

# class ContactUs(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, 'contact/index.html', {'form': form})

#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             return HttpResponse('Thank you for Contacting !!!')

#         form.save()
#         return HttpResponse('Thank you for Contacting !!!')