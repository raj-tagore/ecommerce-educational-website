from django.shortcuts import render, redirect
from .models import Course, CourseApplicant
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
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

PAYU_MERCHANT_KEY = "FEG7f40y"
PAYU_MERCHANT_SALT = SALT = "lHX69YxP0p"
PAYU_MODE = "TEST"

def SendMail(Subject, TextContent, HtmlContent, Recipient):
	Email= MIMEMultipart("alternative")
	Email['Subject'] = Subject
	Email['From'] = 'noreply.leader.factory@gmail.com'
	Email['To'] = Recipient

	ConvertedText = MIMEText(TextContent, 'plain')
	ConvertedHTML = MIMEText(HtmlContent, 'html')
	Email.attach(ConvertedText)
	Email.attach(ConvertedHTML)

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.connect("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login('noreply.leader.factory@gmail.com', 'noreplyLF1234')
	s.sendmail('noreply.leader.factory@gmail.com', Recipient, Email.as_string())
	s.quit()

def PrepMail(BuyerId, ProductId):
	SelectedProduct = Course.objects.get(id = int(ProductId))
	SelectedBuyer = CourseApplicant.objects.get(id = int(BuyerId))

	RecipientEmail = str(SelectedBuyer.Email)

	Subject = "Your Purchase has been confirmed"

	Text = """
			Thank You, Mr.""" +str(SelectedBuyer.Name)+ """
			You have successfully bought the course!
			Details:
			""" +str(SelectedProduct.Name)+ """

			You will find the course after you follow these steps:
			1: Go to the Home Page
			2: Click on 'Login'
			3: Click on 'Items'
			4: Look for the course you have bought, and click on 'View Course Content'
			"""

	HTML = """
			<html>
			<head>
			<style>
			h1 {text-align: center;}
			h2 {text-align : center;}
			h4 {text-align: left;}
			body {text-align: center;}
			.left {text-align: left;}
			.row {background-color: lightyellow;}
			.ProductPic {float: left;
						width: 30%;
						padding: 10px;}
			.ProductInfo {float: right;
						width: 60%;
						padding: 10px;
						text-align: left;}
			.row::after {content: '';
						clear: both;
						display: table;}
			</style>
			</head>
			<body>
			<h1>Thank You</h1>
			<h3>Mr. """ +str(SelectedBuyer.Name)+ """</h3>
			<h3>Your order has been successfully placed</h3>
			<h4>Order Details:</h4>
			<div class="row">
				<div class="ProductPic">
				<img src=" """+str(SelectedProduct.FrontPic)+""" "  alt="" width= 100%> 
				</div>
				<div class="ProductInfo">
				<p><h3 class="left">"""+str(SelectedProduct.Name)+ """</h3></p>
				</div>
			</div>
			<br>
			You will find the course after you follow these steps:
			1: Go to the Home Page
			2: Click on 'Login'
			3: Click on 'Items'
			4: Look for the course you have bought, and click on 'View Course Content'
			<br><br>
			</body>
			</html> """
	
	SendMail(Subject, Text, HTML, RecipientEmail)

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
	DisplayCourses = [i for i in CourseObjAll if i.Display == True]

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
	VarDict = {'CourseObjAll' : DisplayCourses, 'media' : MEDIA_URL, 
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
	
	DisplayCourses = [i for i in RelevantCourses if i.Display == True]

	varDict = {'CourseObjAll' : DisplayCourses, 'media' : MEDIA_URL, 'NotSearched' : NotSearched}

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
	DisplayCourses = [i for i in RelevantCourses if i.Display == True]
	
	varDict = {'CourseObjAll' : DisplayCourses, 'media' : MEDIA_URL, 'NotSearched' : NotSearched}

	return render(request, 'coursesList.html', varDict) 

def RedirectView(request):
	return redirect('/CourseList')
 
def SpecificCourseView(request, namo):
	videos = Course.objects.get(Name = namo)
	NotVerified = False
	"""for i in OwnedCourses:
		if(i.id == CourseId):
			NotVerified = False
			videos = Course.objects.get(Name = namo)
			return render(request, 'single-blog.html', {'namo' : namo, 'videos' : videos, 'media' : MEDIA_URL, 'NotVerified' : NotVerified})
	return render(request, 'single-blog.html', {'namo' : "No Courses bought", 'NotVerified' : NotVerified})"""
	"""for i in OwnedCourses:
		videos = Course.objects.get(Name = namo)"""
	return render(request, 'single-blog.html', {'namo' : namo, 'videos' : videos, 'media' : MEDIA_URL, 'NotVerified' : NotVerified})

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
				Prompt = "User Doesnt Exist, please register first!"
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
		NewApplicant = CourseApplicant()
		NewApplicant.Name = user.Name
		NewApplicant.Email = email
		NewApplicant.CourseId = Product.id
		NewApplicant.CourseName = Product.Name
		NewApplicant.Phone = user.Phone
		NewApplicant.Address = user.Address
		NewApplicant.save()
		PrepMail(NewApplicant.id, Product.id)
		vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':Product, 'user':user,'Media' : MEDIA_URL}
	return render(request, 'SuccessPg.html', vardict)


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
	
