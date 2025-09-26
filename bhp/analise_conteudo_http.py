'''
Os pacotes lxml e BeautifulSoap podem auxiliar na analise do conteudo de uma resposta HTTP(XML e HTML)
'''
#suponha que voce tenha o conteudo HTML de uma request armazenado na variavel `content`
#com o lxml,voce pode recuperar o conteudo e analisar os links:

#XML -> armazenar e transferir  dados (descrever dados) 
#HTML -> exibir os dados para o usuario final

from io import BytesIO #modulo `io` facilita para lidar com tipos de entrada/saida(principais: text I/O, binary I/O e raw I/O)
from lxml import etree
import requests


url = 'http://testhtml5.vulnweb.com/#/popular' #site intencionalmente vulneravel para testes
r = requests.get(url) # GET request
content = r.content # content -> bytes

parser = etree.HTMLParser() # etree -> ElementTree(forma estruturada e hierarquica do XML)
content = etree.parse(BytesIO(content),parser=parser) # analisar o conteudo em formato de arvore


# encontrar todos os elementos com a tag ancora "a"
for link in content.findall('.//a'):
    print(f"{link.get('href')} -> {link.text}")


'''
->com a classe BytesIO podemos utilizar uma string de bytes como um objeto de arquivo quando analisarmos a
resposta HTTP.

->Em seguida, realizamos a solicitacao GET e utilizamos o parser HTML lxml para analisar a resposta.O parser
espera um objeto semelhante a um arquivo ou um nome de arquivo.A classe BytesIO nos permite utilizar o conteudo da string de bytes
retornada como um objeto semelhante a um arquivo para ser passado para o parser lxml

-> utilizamos uma consulta simples para encontrar todas as tags a(ancora) que contem links no conteudo retornado e
imprimimos os resultados.Cada tag de ancora define um link.Seu atributo href especifica a URL do link

-> a chamada da funcao e o retorno de um valor sao feitas na f-string (format)

'''
