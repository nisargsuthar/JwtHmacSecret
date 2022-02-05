from jwt import decode
import hmac
import hashlib
import base64

header = 'ENTER YOUR JWT HEADER HERE'
payload = 'ENTER YOUR JWT PAYLOAD HERE'
signature = 'ENTER YOUR JWT SIGNATURE HERE'.translate(None, '/_+-=')

with open("/path/to/wordlist.txt") as f:
	for s in f:
		secret = s.strip()
		brutesig = hmac.new(secret, header+"."+payload, hashlib.sha256).hexdigest().decode("hex")
		brutesig = base64.b64encode(brutesig).translate(None, '/_+-=')
		print("Testing secret: " + secret)
		
		if(brutesig == signature):
			print("\nSecret found!: " + secret)
			break
			