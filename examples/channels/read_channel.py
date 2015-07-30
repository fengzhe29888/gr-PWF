import numpy as np
nlinks=2
nt=2
f1=open('2x2channel_10dB_1.bin','rb')
content = np.fromfile(f1,dtype=np.complex64).reshape(nlinks*nt,nlinks*nt,order='F')
#content_reshape = content.reshape(4,4,order='F')
H = np.zeros((nlinks,nlinks,nt,nt), dtype = np.complex64)

for l in range(nlinks):
	for k in range(nlinks):
		for m in range(nt):
			H[l][k][m] = content[l*nt+m][k*nt:(k+1)*nt]


#H[0][0] = np.array([content[0][0],content[0][1],content[1][0],content[1][1]]).reshape(2,2)
#H[0][1] = np.array([content[0][2],content[0][3],content[1][2],content[1][3]]).reshape(2,2)
#H[1][0] = np.array([content[2][0],content[2][1],content[3][0],content[3][1]]).reshape(2,2)
#H[1][1] = np.array([content[2][2],content[2][3],content[3][2],content[3][3]]).reshape(2,2)

print content
print H





