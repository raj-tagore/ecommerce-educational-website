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
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

PAYU_MERCHANT_KEY = "FEG7f40y"
PAYU_MERCHANT_SALT = SALT = "lHX69YxP0p"
PAYU_MODE = "TEST"

# Create your views here.
def ProductsPg(request):
	AllProductsObj = Product.objects.all()
	return render(request, 'products.html', {'Product' : AllProductsObj, 'Media' : MEDIA_URL})

def ViewProduct(request, ProductId):
	SelectedProduct = Product.objects.get(id = int(ProductId))
	return render(request, 'PBuy.html', {'Product': SelectedProduct, 'Media' : MEDIA_URL})

def Pay1(request):
	ProductId = request.POST["PId"]
	SelectedProduct = Product.objects.get(id = int(ProductId))
	return render(request, 'PForm.html', {'Product': SelectedProduct, 'Media': MEDIA_URL})

def Pay2(request):
	Name = request.POST["Name"]
	Email = request.POST["Email"]
	Phone = request.POST["Phone"]
	PId = request.POST["PId"]
	Address = request.POST["Address1"]+", "+request.POST["Address2"]+", "+request.POST["Address3"]+", "+request.POST["PinCode"]
	SelectedProduct = Product.objects.get(id = PId)
	Namo = Name.split(' ')[0].lower()
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	Price = round(float(SelectedProduct.Price), 2)
	hashSequence = "FEG7f40y|"+str(txnid)+"|"+str(Price)+"|"+str(PId)+"|"+Namo+"|"+Email+"||"+Name+'|'+str(Phone)+'|'+Email+"|"+Address+"|||||"
	hash_string=hashSequence
	hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
	print(hash_string)
	print(Price)
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
	return render(request, 'PPayUForm.html', VarDict)
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
		return render(request, 'PSuccessPg.html', vardict)

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
		#user.Courses.add(Product)
		vardict = {"txnid":txnid,"status":status,"amount":amount, "s":s, 'Product':SelectedProduct, 'user':NewBuyer,'Media' : MEDIA_URL}
	return render(request, 'PSuccessPg.html', vardict)

@csrf_protect
@csrf_exempt
def PaymentFailure(request):
	return HttpResponse("Your transaction failed, Return to the homepage and try again")

def SearchProducts(request):
	namo = request.GET.get('keyword')
	FilteredProductsObj = Product.objects.filter(Name = namo)
	return render(request, 'products.html', {'Product' : FilteredProductsObj, 'Media' : MEDIA_URL})


