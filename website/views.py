from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	if request.method == "POST":
		 message_name = request.POST['message-name'] 
		 message_email = request.POST['message-email']
		 message = request.POST['message']

		 # send an email
		 send_mail(
		 	'JEDAR Website message from: ' + message_name,# subject
		 	'Message: ' + message + '\nFrom ' + message_email, # message
		 	message_email, # from email
		 	['pcharlesirvin@gmail.com', 'charlespenalosa18@gmail.com'], # to email
		 	)

		 return render(request, 'home.html', {'message_name': message_name})


	else:	 

		 return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

	