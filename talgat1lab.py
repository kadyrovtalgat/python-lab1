import requests 
import re 
gk=[]
g=[] 
response = requests.get('http://www.mosigra.ru/') 
a=re.findall(r'(\w*@\w*[.]\w*)',str(response.content)) 
a=set(a) 
i=1
for word in a:
	gk.insert(i,word)
	i=i+1 
p=1
b=re.findall(r'http:\/\/www\.mosigra\.ru\/[\w\d:#@%\/;$~_?\+-=\/\.&]*',str(response.content)) 
b=set(b)
for word in b:
	gk.insert(p,word)
	p=p+1 
k=1
while k<9:
	response = requests.get(gk[k]) 
	a=re.findall(r'(\w*@\w*[.]\w*)',str(response.content)) 
	a=set(a) 
	i=1
	for word in a:
		t=0
		for n in range(1,i):
			if word==gk[n]:
				t=1
		if t==0:
			g.insert(i,word)
			i=i+1 
	k=k+1
g=set(g)
print(g)