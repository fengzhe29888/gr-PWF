import numpy as np
nlinks = 2
nt = 2
f1=open('sigmagen_1.bin','rb')
content = np.fromfile(f1,dtype=np.complex64).reshape(nt,nlinks*nt,order='F')
Sinit = np.zeros((nlinks,nt,nt), dtype = np.complex64)

for l in range(nlinks):
	for k in range(nt):
		Sinit[l][k]= content[k][l*nt:(l+1)*nt]

#Sinit[0] = np.array([content[0][0],content[0][1],content[1][0],content[1][1]]).reshape(2,2)
#Sinit[1] = np.array([content[0][2],content[0][3],content[1][2],content[1][3]]).reshape(2,2)



print content
print Sinit
