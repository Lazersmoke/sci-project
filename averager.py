newfile=open('outputfile.txt','r')
xfile=open('xfile.txt','w')
pyarr=[]
intpyarr=[]
jarr=[]
perlarr=[]
#KEY 0>python 1>int. python 2>java 3>perl
selector=0
numlines=0
for line in newfile:
	numlines+=1	
	if selector==0:
		pyarr.append(float(line))
	elif selector==1:
		intpyarr.append(float(line))
	elif selector==2:
		jarr.append(float(line))
	elif selector==3:
		perlarr.append(float(line))
	if selector!=3:
		selector+=1
	else:
		selector=0
pytot=0
intpytot=0
jtot=0
perltot=0
for n in pyarr:
	xfile.write(str(n)+'\n')
	pytot+=n
for n in intpyarr:
	xfile.write(str(n)+'\n')
	intpytot+=n
for n in jarr:
	xfile.write(str(n)+'\n')
	jtot+=n
for n in perlarr:
	xfile.write(str(n)+'\n')
	perltot+=n
pyfinal=pytot/(float(numlines)/4)
intpyfinal=intpytot/(float(numlines)/4)
jfinal=jtot/(float(numlines)/4)
perlfinal=perltot/(float(numlines)/4)

print('Python Average: '+str(pyfinal)+'\nIntegrated Python Average: '+str(intpyfinal)+'\nJava Average: '+str(jfinal)+'\nPerl Average: '+str(perlfinal))
