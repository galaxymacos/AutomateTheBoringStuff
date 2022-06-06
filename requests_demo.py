import requests

# requests get demo


# requests auth demo
r = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(r.text)

