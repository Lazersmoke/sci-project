import time
from os import system as oscaller
from os import name as osname
myfile=open('outputfile.txt','w')
NUM_TRIALS=1
tests=int(input('How many tests? '))
integratedlag=bool(input('Compensate for lag?(0 or 1) '))
def timerify(commander,Numtrials,lag):
	lister=[]
	for n in range(int(Numtrials)):
		timestart=time.time()
		oscaller(commander)
		timeend=time.time()
		lister.append((timeend-timestart)-lag)
	total=0.0
	for n in lister:
		total+=n
	return total/Numtrials

def pyintegrated(NUM_TRIALS):
	Int=[]
	for n in range(int(NUM_TRIALS)):
		starttime=time.time()
		#begin integrated
		x=0
		y=1
		while y<1000001:
			y+=1
			x+=5
		print(str(x))
		#end integrated
		endtime=time.time()
		Int.append(endtime-starttime)
	total=0.0
	for n in Int:
		total+=n
	return total/NUM_TRIALS
if (osname=='posix'):
	blankcommand='false'
elif (osname=='nt'):
	blankcommand='rem'
if integratedlag:
	print('**CALCULATING LAG**')
	lag=timerify(blankcommand,NUM_TRIALS,0)
	print('**LAG CALCULATED**')
else:
	lag=0.0
for n in range(tests):
	myfile.write(str(timerify('python3 pytarget.py',NUM_TRIALS,lag))+'\n')
	myfile.write(str(pyintegrated(NUM_TRIALS))+'\n')
	myfile.write(str(timerify('java Jtarget',NUM_TRIALS,lag))+'\n')
	myfile.write(str(timerify('perl perltarget.perl',NUM_TRIALS,lag))+'\n')
myfile.close()

















	
	
	
	








