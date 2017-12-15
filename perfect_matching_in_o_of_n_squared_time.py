#-----------------
#-----------------
# libraries:
import numpy as np
import scipy.linalg
import random
import itertools
import time
#-----------------
#-----------------
# parameters:
iterations=500 #number of iterations
nlowerbound=1400 # starting (minimal) size of the adjacency matrix
nupperbound=1450# maximal size of the adjacency matrix
d=3 # mumber of edges from each node
#-----------------
#-----------------
# non-important variables:
flag=0
zerodetnotmodtwo=0
nonzerodetnotmodtwo=0
numofdetzero=0
numofdetnonzero=0
possibledets=[]
dashes="------------------------------------------"
#fh = open("neq100.txt","w")
#-----------------
#-----------------
# iterate over an interval for n
for n in range(nlowerbound,nupperbound):
	times=iterations
	while times>0:
#-----------------
#-----------------
# create random matrix as a sum of non-clashing permutation matrices
		start_time=time.time()
		flag=0
		a=np.zeros((n,n))
		a1=np.random.permutation(n)
		a2=np.random.permutation(n)
		for i in range(0,n):
			if a1[i]==a2[i]:
				flag=1					
				break
		while flag:
			flag=0
			a2=np.random.permutation(n)
			for i in range(0,n):
				if a1[i]==a2[i]:
					flag=1					
					break
		a3=np.random.permutation(n)
		for i in range(0,n):
			if (a1[i]==a3[i]) or (a2[i]==a3[i]):
				flag=1					
				break
		while flag:
			flag=0
			a3=np.random.permutation(n)
			for i in range(0,n):
				if (a1[i]==a3[i]) or (a2[i]==a3[i]):
					flag=1			
					break
		for i in range(0,n):
			a[i,a1[i]]=1
			a[i,a2[i]]=1
			a[i,a3[i]]=1
		end_time=time.time()-start_time
		print("Time for generating matrix: %.5f" %end_time)
		start_time=time.time()
#-----------------
#-----------------
# calculate determinant		
		if int(round(scipy.linalg.det(a)))%2==0:
			numofdetzero+=1
		else:
			numofdetnonzero+=1
		if int(round(scipy.linalg.det(a)))==0:
			zerodetnotmodtwo+=1
		else:
			nonzerodetnotmodtwo+=1
		end_time=time.time()-start_time
		print("Time for computing determinant: %.5f" %end_time)
		
		# print matrices with zero determinant
		#if (int(round(scipy.linalg.det(a)))==0):
		#	print(a)
		#	print("Determinant",int(round(scipy.linalg.det(a))))
		# print matrices with non-zero even determinant
		#if (int(round(scipy.linalg.det(a)))!=0) and (int(round(scipy.linalg.det(a)))%2==0):
		#	print(a)
		#	print("Determinant",int(round(scipy.linalg.det(a))))
#-----------------
#-----------------
# output to file:
#		if (int(round(scipy.linalg.det(a)))!=0) and (int(round(scipy.linalg.det(a)))%2!=0):
#			print(a)
#				fh.write(np.array_str(a))
#				fh.write("\n")
#				det="Determinant "+str(int(round(scipy.linalg.det(a))))+"\n"
#			print("Determinant ",int(round(scipy.linalg.det(a))))
#				fh.write(det)
#				fh.write("\n")
#				fh.write("\n")
#-----------------
#-----------------			
#		if int(round(scipy.linalg.det(a))) not in possibledets:
#			possibledets.append(int(round(scipy.linalg.det(a))))
		
		times-=1
#-----------------
#-----------------
# output:
	print("n: ",n)
	print("Number of zero determinants mod 2: ",numofdetzero)
	print("Number of nonzero determinants mod 2: ",numofdetnonzero)
	print(dashes)
	print("Number of zero determinants: ",zerodetnotmodtwo)
	print("Number of nonzero determinants: ",nonzerodetnotmodtwo)
	#print("Possible determinants: ", sorted(possibledets))
	print(dashes)
	print(dashes)
	print(dashes)
#-----------------
#-----------------
	zerodetnotmodtwo=0
	nonzerodetnotmodtwo=0
	numofdetzero=0
	numofdetnonzero=0
	possibledets=[]
#fh.close()

