#exemplo de autenticacao de formulario
import requests
url = 'https://pentest-ground.com'
response = request.get(url) # metodo GET

data = {'user':'tim','passwd':'1337'}
response = request.post(url,data=data) #metodo POST
print(response.text)
#response.text -> string
#response.content -> bytestring

