import requests
import sys



print sys.argv[1:]
lenargv = len(sys.argv[1:])
if lenargv != 3:
	print('3 arguments needed')

userLogin = ''
userKey = ''
message = ''

baseUrl = 'https://smsapi.free-mobile.fr/sendmsg?'

payload = 'user=' + userLogin + '&pass=' + userKey + '&msg=' + message

finalUrl = baseUrl + payload


r = requests.post(finalUrl)

if r.status_code == 200:
	print("Message sent successfully")
elif r.status_code == 400:
	print("One argument is missing")
elif r.status_code == 402:
	print("Too many sms sent, please wait and retry")
elif r.status_code == 403:
	print("The service is not activated on the line holder's account, or incorrect login/userkey")
elif r.status_code == 500:
	print("Server side error. Please try again later")

print("Stopping execution")

