
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
from .serializers import *
import json
from django.core.mail import send_mail
from django.conf import settings


# @api_view(['GET'])
# def slips(request):
#     if request.method == 'GET':
#         data = slip.objects.all()
#         serializer = slipserializer(data,many = True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def packages(request):
#     if request.method == 'GET':
#         data = package.objects.all()
#         serializer = packageserializer(data,many = True)
#         return Response(serializer.data)
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        ref_data = json.loads(data)
        usr = User.objects.create_user(ref_data['firstname'],ref_data['email'],ref_data['password'])
        usr.last_name = ref_data['lastname']
        usr.save()
        login(request,usr)
        return Response({'message':'registered successfully'})

@api_view(['POST'])
def logIn(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        ref_data = json.loads(data)
        uname = User.objects.get(email = ref_data['ID'])
        usr = authenticate(username = uname,password = ref_data['password'])
        login(request,usr)
        return Response({'message': 'successfully logged in'})
        
@api_view(['GET'])
def user(request):
    print(request.user)
    return Response({'none':None})

@api_view(['GET'])
def projects(request):
    if request.method == 'GET':
        proj = project.objects.all()
        serializer = projectserializer(proj,many = True)
        return Response(serializer.data)

@api_view(['GET'])
def skills(request):
    if request.method == 'GET':
        sk = skill.objects.all()      
        serializer = skillserializer(sk,many = True)
        return Response(serializer.data)
    
@api_view(['GET'])
def tech(request):
    if request.method == 'GET':
        tech = technology.objects.all()
        serializer = technologyserializer(tech,many = True)
        return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def placeorder(request):
    if request.method == 'POST':
        usr = request.user
        print(usr)
        data = request.body.decode('utf-8')
        ref_data = json.loads(data)
        # order.objects.create(timeframe = ref_data['time'],goals = ref_data['goals'],questions = ref_data['questions'],audience = ref_data['audience'],status = 'initiated')
        return Response('package oredered succesfully')

@api_view(['POST'])
def mail(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        ref_data = json.loads(data)
        send_mail(ref_data['subject'], "", 'kundan.personalweb@outlook.com', ['kundanbhardwaj145@gmail.com'], fail_silently=False,html_message=ref_data['body'])
        return Response('Message sent sucessfully')
@api_view(['GET'])
def socials(request):
    if request.method == 'GET':
        apps = social.objects.all()
        serializer = socialserializer(apps,many = True)
        return Response(serializer.data) 
 
@api_view(['GET']) 
def docs(request):
    if request.method == 'GET':
        data = doc.objects.get(doc_name = 'resume')
        serializer = docserializer(data)
        return Response(serializer.data)
    
@api_view(['GET'])
def getservice(request):
    if request.method == 'GET':
        data = service.objects.all()
        d = serviceserializer(data,many = True)
        ser = []
        for i in data:
            ser.append(serviceattributeserializer(serviceattribute.objects.filter(att_of = i),many = True).data)
        return Response({'services':d.data,'attrs': ser})
    
@api_view(['GET'])
def edu(request):
    if request.method == 'GET':
        data = education.objects.all()
        serializer = edserializer(data,many=True)
        return Response(serializer.data)