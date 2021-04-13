from django.shortcuts import render
from django.shortcuts import redirect
from .models import OnlineTrainingProgram, OnlineTrainingApplicant, OnlineClient
from django.shortcuts import HttpResponse
import os
from payu.gateway import get_hash
from uuid import uuid4
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import time
import hashlib
import random
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

PAYU_MERCHANT_KEY = "FEG7f40y"
PAYU_MERCHANT_SALT = SALT = "lHX69YxP0p"
PAYU_MODE = "TEST"


# Create your views here.
def TrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	SelectedCategory = 'Null'
	RelevantObj = [] 
	for i in Programs:
		if i.Display == True:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def InsuranceTrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	DisplayedPrograms = []
	for i in Programs:
		if i.Display == True:
			DisplayedPrograms.append(i)
	SelectedCategory = 'Insurance'
	RelevantObj = []
	for i in DisplayedPrograms:
		ObjCategories = []
		for j in i.Category.all():
			ObjCategories.append(j.Name)
		if SelectedCategory in ObjCategories:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def SalesTrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	DisplayedPrograms = []
	for i in Programs:
		if i.Display == True:
			DisplayedPrograms.append(i)
	SelectedCategory = 'Sales'
	RelevantObj = []
	for i in DisplayedPrograms:
		ObjCategories = []
		for j in i.Category.all():
			ObjCategories.append(j.Name)
		if SelectedCategory in ObjCategories:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def NetworkMarketingTrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	DisplayedPrograms = []
	for i in Programs:
		if i.Display == True:
			DisplayedPrograms.append(i)
	SelectedCategory = 'Network Marketing'
	RelevantObj = []
	for i in DisplayedPrograms:
		ObjCategories = []
		for j in i.Category.all():
			ObjCategories.append(j.Name)
		if SelectedCategory in ObjCategories:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}	
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def BusinessTrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	DisplayedPrograms = []
	for i in Programs:
		if i.Display == True:
			DisplayedPrograms.append(i)
	SelectedCategory = 'Business'
	RelevantObj = []
	for i in DisplayedPrograms:
		ObjCategories = []
		for j in i.Category.all():
			ObjCategories.append(j.Name)
		if SelectedCategory in ObjCategories:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def SelfDevelopmentTrainingPg(request):
	Programs = OnlineTrainingProgram.objects.all()
	DisplayedPrograms = []
	for i in Programs:
		if i.Display == True: 
			DisplayedPrograms.append(i) 
	SelectedCategory = 'Self Development'
	RelevantObj = []
	for i in DisplayedPrograms:
		ObjCategories = []
		for j in i.Category.all():
			ObjCategories.append(j.Name)
		if SelectedCategory in ObjCategories:
			RelevantObj.append(i)
	RelevantObj = sorted(RelevantObj, key=lambda OnlineTrainingProgram: OnlineTrainingProgram.Position)
	VarDict = {'programs' : RelevantObj, 'Media' : MEDIA_URL, 'SelectedCategory': SelectedCategory}
	return render(request, "Training/OnlineTrainingPrograms.html", VarDict)

def HostTrainingPg(request):
	return render(request, "HostTrainingPrograms.html")


#display the form to apply for a training program
def ApplyForTraining(request, CourseName):
	Course = OnlineTrainingProgram.objects.get(Name = CourseName)
	return render(request, "Training/ApplyForTrainingForm.html", {'Course' : Course, 'Media' : MEDIA_URL})

def MoreAboutTraining(request, CourseName):
	Course = OnlineTrainingProgram.objects.get(Name = CourseName)
	return render(request, "Training/OnlineMoreAboutTraining.html", {'SelectedTraining' : Course, 'Media' : MEDIA_URL})

def Pay2(request):
	Name = request.POST["Name"] 
	Email = request.POST["Email"]
	Phone = request.POST["Phone"]
	CourseId = request.POST["CourseId"]
	Address = request.POST["Address1"]+", "+request.POST["Address2"]+", "+request.POST["Address3"]+", "+request.POST["PinCode"]
	Applicants = OnlineTrainingApplicant.objects.all()
	TrainingObj = OnlineTrainingProgram.objects.get(id = CourseId)
	exists = False
	for i in Applicants:
		if(int(i.Phone) == int(Phone)):
			if(i.CourseId == CourseId):
				s = "This Phone number is already registered to this program"
				exists = True
			else:
				continue	
		else:
			continue
	if(exists):
		return render(request, 'Training/ApplyForTrainingForm.html', {'s': s, 'Course' : TrainingObj, 'Media' : MEDIA_URL})
	else:
		VarDict = {'Product' : TrainingObj, 'Media' : MEDIA_URL, 
					'Name': Name,
					'Email': Email,
					'Phone': Phone,
					'CourseId': TrainingObj.id,
					'Address': Address}
		return render(request, 'Training/Tbuy.html', VarDict)

def Pay3(request):
	Name = request.POST["Name"]
	Email = request.POST["Email"]
	Phone = request.POST["Phone"]
	CourseId = request.POST["CourseId"]
	Address = request.POST["Address"]
	Product = OnlineTrainingProgram.objects.get(id = int(CourseId))
	Namo = Name.split(' ')[0].lower()
	
	randomize = randint(0,20)
	hash_object = hashlib.sha256(bytes(randomize+int(time.time())))
	txnid=hash_object.hexdigest()[0:20]

	hashh = ''
	price = round(float(Product.Price), 2)
	hashSequence = "FEG7f40y|"+str(txnid)+"|"+str(price)+"|"+str(CourseId)+"|"+Namo+"|"+Email+"||"+Name+"|"+str(Phone)+"||"+Address+"|||||"
	hash_string=hashSequence
	hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
	VarDict = {
		'Name' : Name,
		'Phone' : Phone,
		'Email' : Email,
		'Product' : Product,
		'Address' : Address,
		'price' : price,
		'PAYU_MERCHANT_KEY' : PAYU_MERCHANT_KEY,
		'PAYU_MERCHANT_SALT' : PAYU_MERCHANT_SALT,
		'TxnId' :txnid,
		'Namo' : Namo,
		"hashh":hashh,
		"hash_string":hash_string,
	}
	return render(request, 'Training/OPayUForm.html', VarDict)

@csrf_protect
@csrf_exempt
def OTPaymentSuccess(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	udf1=request.POST['udf1']
	Name=request.POST['udf2']
	Phone=request.POST['udf3']
	Address=request.POST['udf5']
	salt=SALT
	print("ok this runs")
	Product = OnlineTrainingProgram.objects.get(id = int(productinfo))
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'||||||'+Address+'||'+Phone+'|'+Name+'||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'||||||'+Address+'||'+Phone+'|'+Name+'||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
	if(hashh !=posted_hash):
		s=False
		vardict = {"txnid":txnid,"status":status,"amount":amount,"s":s, 'Product':Product, 'user':NewApplicant,'Media' : MEDIA_URL}
		return render(request, 'SuccessPg.html', vardict)

	else:
		'''print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."'''
		exists = False
		Applicants = OnlineTrainingApplicant.objects.all()
		for i in Applicants:
			if(int(i.Phone) == int(Phone)):
				if(i.CourseId == Product.id):
					user = i
					exists = True
				else:
					continue	
			else:
				continue
		if(exists):
			s=True
			vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':Product, 'user':user,'Media' : MEDIA_URL}
			return render(request, 'Training/TSuccessPg.html', vardict)
		else:
			s=True
			NewApplicant = OnlineTrainingApplicant()
			NewApplicant.Name = Name
			NewApplicant.Email = email
			NewApplicant.CourseId = Product.id
			NewApplicant.CourseName = Product.Name
			NewApplicant.Phone = Phone
			NewApplicant.Address = Address
			NewApplicant.save()
			vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':Product, 'user':NewApplicant,'Media' : MEDIA_URL}
			return render(request, 'Training/TSuccessPg.html', vardict)

@csrf_protect
@csrf_exempt
def OTPaymentFailure(request):
	return HttpResponse("Your transaction failed, Return to the homepage and try again")


def VerifyParticipantForm(request, CourseName):
	Course = OnlineTrainingProgram.objects.get(Name = CourseName)
	VarDict = {'Course': Course}
	return render(request, 'Training/OTVerifyYourself.html', VarDict)
	

def ActuallyJoinTraining(request):
	CourseId = request.POST['CourseId']
	RollNo = request.POST['RollNo']
	Phone = request.POST['Phone']
	Email = request.POST['Email']
	Course = OnlineTrainingProgram.objects.get(id = CourseId)
	AllApplicants = OnlineTrainingApplicant.objects.all()
	JoinedApplicants = [i for i in AllApplicants if int(i.CourseId) == int(Course.id)]
	Verified = False
	MeetingLink = ''
	for i in JoinedApplicants:
		if int(i.id) == int(RollNo): 
			if int(i.Phone) == int(Phone):
				Verified = True
				MeetingLink = Course.MeetingLink
				VarDict = {'Verified' : Verified, 'MeetingLink' : MeetingLink, 'Course' : Course}
				return render(request, "Training/OTParticipantConfirmed.html", VarDict)
			else:
				continue
		else:
			continue
	VarDict = {'Verified' : Verified, 'MeetingLink' : MeetingLink, 'Course' : Course}
	return render(request, "Training/OTParticipantConfirmed.html", VarDict)
