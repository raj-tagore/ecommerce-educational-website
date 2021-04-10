from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Buyer
from django.shortcuts import HttpResponse
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
import random
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 

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
	SelectedProduct = Product.objects.get(id = int(ProductId))
	SelectedBuyer = Buyer.objects.get(id = int(BuyerId))

	RecipientEmail = str(SelectedBuyer.Email)

	Subject = "Your Purchase has been confirmed"

	Text = """
			Thank You, Mr.""" +str(SelectedBuyer.Name)+ """
			Your order has been successfully placed
			Details:
			""" +str(SelectedProduct.Name)+ """
			Price: Rs. """+str(SelectedProduct.Price)+ """
			Your order will be delivered in """+str(SelectedProduct.DaysForDelivery)+ """
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
			    <img src="C:/Users/Raj Tagore/Pictures/Screenshots/onlineCourse.png" alt="" width= 100%> 
			    </div>
			    <div class="ProductInfo">
			    <p><h3 class="left">"""+str(SelectedProduct.Name)+ """</h3></p>
			    <p>Your order will be delivered in """+str(SelectedProduct.DaysForDelivery)+ """ days.</p>
			    <p>Price: Rs. """+str(SelectedProduct.Price)+ """</p>
			    </div>
			</div>
			<br><br>
			</body>
			</html> """
	
	SendMail(Subject, Text, HTML, RecipientEmail)

# Create your views here.
def ProductsPg(request):
	RelevantProducts = []
	AllProductsObj = Product.objects.all()
	for i in AllProductsObj:
		if i.Display == True:
			RelevantProducts.append(i)
	RelevantProducts = sorted(RelevantProducts, key=lambda Product: Product.Position)
	return render(request, 'Products/products.html', {'Product' : RelevantProducts, 'Media' : MEDIA_URL})

def ViewProduct(request, ProductId):
	SelectedProduct = Product.objects.get(id = int(ProductId))
	return render(request, 'Products/PBuy.html', {'Product': SelectedProduct, 'Media' : MEDIA_URL})

def Pay1(request):
	ProductId = request.POST["PId"]
	SelectedProduct = Product.objects.get(id = int(ProductId))
	return render(request, 'Products/PForm.html', {'Product': SelectedProduct, 'Media': MEDIA_URL})

def Pay2(request):
	Name = request.POST["Name"]
	Email = request.POST["Email"]
	Phone = request.POST["Phone"] 
	PId = request.POST["PId"]
	Address = request.POST["Address1"]+", "+request.POST["Address2"]+", "+request.POST["Address3"]+", "+request.POST["PinCode"]
	SelectedProduct = Product.objects.get(id = PId)
	Namo = Name.split(' ')[0].lower()
	random.seed(time.clock())
	hash_object = hashlib.sha256(b'random.randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	Price = round(float(SelectedProduct.Price), 2)
	if (SelectedProduct.ActivateDiscount==True):
		Price = round(float(SelectedProduct.DiscountedPrice), 2)
	hashSequence = "FEG7f40y|"+str(txnid)+"|"+str(Price)+"|"+str(PId)+"|"+Namo+"|"+Email+"||"+Name+'|'+str(Phone)+'|'+Email+"|"+Address+"|||||"
	hash_string=hashSequence
	hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
	VarDict = {
		'Product' : SelectedProduct,
		'Price' : Price,
		'PAYU_MERCHANT_KEY' : PAYU_MERCHANT_KEY,
		'PAYU_MERCHANT_SALT' : PAYU_MERCHANT_SALT,
		'TxnId' :txnid,
		'Namo' : Namo,
		'Name' : Name,
		'Address' : Address,
		'Phone' : Phone, 
		'Email' : Email,
		"hashh":hashh,
		"hash_string":hash_string,
	}
	return render(request, 'Products/PPayUForm.html', VarDict)
	'''VarDict = {'Product' : Product, 'Media' : MEDIA_URL, 
				'Name': Name,
				'Email': Email,
				'Phone': Phone,
				'Address': Address}
	return render(request, 'Tbuy.html', VarDict)'''

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
	Name=request.POST['udf2']
	Phone=request.POST['udf3']
	Email=request.POST['udf4']
	Address=request.POST['udf5']
	salt=SALT
	SelectedProduct = Product.objects.get(id = int(productinfo))
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'||||||'+Address+'|'+Email+'|'+str(Phone)+'|'+Name+'||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'||||||'+Address+'|'+Email+'|'+str(Phone)+'|'+Name+'||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
	if(hashh !=posted_hash):
		s=False
		vardict = {"txnid":txnid,"status":status,"amount":amount,"s":s, 'Product':SelectedProduct,'user':Buyer,'Media' : MEDIA_URL}
		return render(request, 'Products/PSuccessPg.html', vardict)

	else:
		'''print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."'''
		s=True
		NewBuyer = Buyer()
		NewBuyer.Name = Name
		NewBuyer.Email = Email
		NewBuyer.Phone = Phone
		NewBuyer.Address = Address
		NewBuyer.ProductId = SelectedProduct.id
		NewBuyer.ProductName = SelectedProduct.Name
		NewBuyer.save()
		#PrepMail(NewBuyer.id, NewBuyer.ProductId)
		#user.Courses.add(Product)
		vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':SelectedProduct, 'user':NewBuyer,'Media' : MEDIA_URL}
	return render(request, 'Products/PSuccessPg.html', vardict)

@csrf_protect
@csrf_exempt
def PaymentFailure(request):
	return HttpResponse("Your transaction failed, Return to the homepage and try again")

def SearchProducts(request):
	namo = request.GET.get('keyword')
	FilteredProductsObj = Product.objects.filter(Name = namo)
	return render(request, 'Products/products.html', {'Product' : FilteredProductsObj, 'Media' : MEDIA_URL})


