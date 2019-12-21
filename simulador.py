import requests
while(True):
   valor = (input("Informe um valor: "))
   r = requests.post("https://estacionamentao.herokuapp.com/upload", json={"LDR":valor})
   print(r.status_code)
