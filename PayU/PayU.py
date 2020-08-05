from payu import get_hash
from uuid import uuid4
data = {
    'txnid':uuid4().hex, 'amount':10.00, 'productinfo': 'Sample Product',
    'firstname': 'test', 'email': 'test@example.com', 'udf1': 'Userdefined field',
}
hash_value = get_hash(data)


PAYU_MERCHANT_KEY = "FEG7f40y"
PAYU_MERCHANT_SALT = "lHX69YxP0p"
PAYU_MODE = "TEST"