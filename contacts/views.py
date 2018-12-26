from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        email = request.POST['email']

        #Check if User has already made an enquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,phone=phone, message=message, user_id=user_id)

        contact.save()
        #Send Email
        send_mail('Property Listing Enquiry',
        'There has been an enquiry for '+ listing + '. Sign into admin panel for more info.',
        'edwindane553@gmail.com',
        [realtor_email, 'mittalbhishak@rediffmail.com'],
        fail_silently=False
        )

        messages.success(request,'Your Request has been Submitted, A realtor will get back to you soon')
        return redirect('/listings/'+listing_id)