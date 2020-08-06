from django.shortcuts import render, redirect
from .models import Course
from user.models import User
import os
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from payu.gateway import get_hash
from uuid import uuid4
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

PAYU_MERCHANT_KEY = "FEG7f40y"
PAYU_MERCHANT_SALT = SALT = "lHX69YxP0p"
PAYU_MODE = "TEST"

def MakeTagsList():
	CourseObjAll = Course.objects.all()
	CourseTags = []
	AllTags = []
	AllDiffTags = []
	#to make list of all tags
	for k in CourseObjAll:
		CourseTags = k.Tags.split(', ')
		for l in CourseTags:
			AllTags.append(l)
		AllTags.sort()
	AllDiffTags.append(AllTags[0])
	for m in range(len(AllTags)):
		if AllTags[m]==AllDiffTags[-1]:
			continue
		else:
			AllDiffTags.append(AllTags[m])
	return AllDiffTags

def HomeView(request):
	return render(request, 'index.html')

def CourseListView(request):
	CourseObjAll = Course.objects.all()

	#read tags from file
	'''TagsFileObj = open('tags.txt', 'r+')
	TagsArr = TagsFileObj.read().split()'''
	#make new tags list thru function
	AllDiffTags = MakeTagsList()

	RecentCourses = []
	NotSearched = True
	if (len(CourseObjAll)>5):
		for n in range(len(CourseObjAll)-5, len(CourseObjAll)):
			RecentCourses.append(CourseObjAll[n])
	else :
		for n in CourseObjAll:
			RecentCourses.append(n)
	VarDict = {'CourseObjAll' : CourseObjAll, 'media' : MEDIA_URL, 
				'Tags': AllDiffTags, 'RecentCourses' : RecentCourses, 'NotSearched' : NotSearched}
	return render(request, 'coursesList.html', VarDict) 

def SearchCourse(request):
	#the tag submitted by user
	TagInput = request.GET.get("tag")
	#all Course object
	CourseObjAll = Course.objects.all()
	#Course fulfilling search result
	RelevantCourses = []
	RecentCourses = []
	NotSearched = False

	#Add any course who has matching tag to relevent Course
	for i in CourseObjAll:
		TagsList = i.Tags.split(', ')
		for j in TagsList:
			if j == TagInput:
				RelevantCourses.append(i)
			else:
				continue

	#make new tags list thru function
	AllDiffTags = MakeTagsList()

	#to make list of 5 recent Course
	if (len(CourseObjAll)>5):
		for n in range(len(CourseObjAll)-5, len(CourseObjAll)):
			RecentCourses.append(CourseObjAll[n])
	else :
		for n in CourseObjAll:
			RecentCourses.append(n)

	varDict = {'CourseObjAll' : RelevantCourses, 'media' : MEDIA_URL, 'NotSearched' : NotSearched}

	return render(request, 'coursesList.html', varDict) 

def SearchCourseByName(request):
	#name submitted by user
	InputName = request.GET.get("tag")
	#all Course object
	CourseObjAll = Course.objects.all()
	#Course fulfilling search result
	RelevantCourses = []
	RecentCourses = []
	NotSearched = False
	
	#Add any course who has matching name to relevent Course
	for i in CourseObjAll:
		NameWords = i.Name.split(' ')
		for j in NameWords:
			if j == InputName:
				RelevantCourses.append(i)
			else:
				continue
	
	varDict = {'CourseObjAll' : RelevantCourses, 'media' : MEDIA_URL, 'NotSearched' : NotSearched}

	return render(request, 'CoursesList.html', varDict) 

def RedirectView(request):
	return redirect('/CourseList')
 
def SpecificCourseView(request, namo):
	UserId = request.POST["UId"]
	CourseId = int(request.POST["CId"])
	videos = Course.objects.get(Name = namo)
	User = User.objects.get(id = int(UserId))
	OwnedCourses = User.Courses.all()
	NotVerified = True
	for i in OwnedCourses:
		if(i.id == CourseId):
			NotVerified = False
			videos = Course.objects.get(Name = namo)
			return render(request, 'single-blog.html', {'namo' : namo, 'videos' : videos, 'media' : MEDIA_URL, 'NotVerified' : NotVerified})
		else:
			return render(request, 'single-blog.html', {'namo' : namo, 'NotVerified' : NotVerified})
	return render(request, 'single-blog.html', {'namo' : "No Courses bought", 'NotVerified' : NotVerified})

def Pay1(request, CourseId):
	Prompt = "Please login to continue with your purchase"
	return render(request, 'login2.html', {'Prompt' : Prompt, 'CourseId' : CourseId, 'Media' : MEDIA_URL})

def Pay2(request, CourseId2):
	Email = request.POST["Email"]
	Password = request.POST["Password"]
	CourseId = request.POST["CourseId"]
	if(CourseId == CourseId2):
		Persons = User.objects.all()
		for i in Persons:
			if (i.Email == Email):
				if (i.Password == Password):
					CourseObj = Course.objects.get(id = CourseId)
					return render(request, 'buy.html', {'Product' : CourseObj, 'Media' : MEDIA_URL, 'Person': i})
				else:
					Prompt = "Wrong Password"
					return render(request, 'login2.html', {'Prompt' : Prompt})
			else:
				Prompt = "User Doesnt Exist"
				continue
		return render(request, 'login2.html', {'Prompt' : Prompt})
	else:
		return HttpResponse("We encountered an error, return to the homepage and try again")

def Pay3PayU(request):
	CId = request.POST["CId"]
	PId = request.POST["PId"]
	Person = User.objects.get(id = CId)
	Product = Course.objects.get(id = PId)
	Namo = Person.Name.split(' ')[0].lower()
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	price = round(float(Product.Price), 2)
	hashSequence = "FEG7f40y|"+str(txnid)+"|"+str(price)+"|"+str(PId)+"|"+Namo+"|"+Person.Email+"|"+str(CId)+"|||||||||"
	hash_string=hashSequence
	hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
	print(hash_string)
	print(price)
	VarDict = {
		'Person' : Person,
		'Product' : Product,
		'price' : price,
		'PAYU_MERCHANT_KEY' : PAYU_MERCHANT_KEY,
		'PAYU_MERCHANT_SALT' : PAYU_MERCHANT_SALT,
		'TxnId' :txnid,
		'Namo' : Namo,
		"hashh":hashh,
		"hash_string":hash_string,
	}
	return render(request, 'PayUForm.html', VarDict)

@csrf_protect
@csrf_exempt
def PaymentSuccess(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	udf1=request.POST['udf1']
	salt=SALT
	Product = Course.objects.get(id = int(productinfo))
	user = User.objects.get(id = int(udf1))
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'||||||||||'+udf1+'|'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'||||||||||'+udf1+'|'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
	if(hashh !=posted_hash):
		s=False
		vardict = {"txnid":txnid,"status":status,"amount":amount,"s":s, 'Product':Product, 'user':user,'Media' : MEDIA_URL}
		return render(request, 'SuccessPg.html', vardict)

	else:
		'''print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."'''
		s=True
		user.Courses.add(Product)
		vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':Product, 'user':user,'Media' : MEDIA_URL}
	return render(request, 'SuccessPg.html', vardict)

@csrf_protect
@csrf_exempt
def PaymentFailure(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	udf1=request.POST['udf1']
	salt=SALT
	Product = Course.objects.get(id = int(productinfo))
	user = User.objects.get(id = int(udf1))
	s=False
	vardict = {"txnid":txnid,"status":status,"amount":amount,"s":s, 'Product':Product, 'user':user,'Media' : MEDIA_URL}
	return render(request, 'SuccessPg.html', vardict)
	
