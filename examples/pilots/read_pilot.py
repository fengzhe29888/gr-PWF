import numpy as np
#fpilot1 = np.fromfile(open('fpilot1.bin','rb'),dtype=np.complex64).reshape(400,2)
f1=open('fpilot1.bin','rb')
content = np.fromfile(f1,dtype=np.complex64)
fpilot1 = content.reshape(400,2).transpose()

f2=open('fpilot2.bin','rb')
content = np.fromfile(f2,dtype=np.complex64)
fpilot2 = content.reshape(400,2).transpose()

r1=open('rpilot1.bin','rb')
content = np.fromfile(r1,dtype=np.complex64)
rpilot1 = content.reshape(400,2).transpose()

r2=open('rpilot2.bin','rb')
content = np.fromfile(r2,dtype=np.complex64)
rpilot2 = content.reshape(400,2).transpose() #2 x 400 pilot

z = np.array([[0,0,0,0],[0,0,0,0]])
shift1 = np.concatenate((fpilot1,z),axis=1)

#print fpilot1
#print np.dot(shift1[:,0:400],fpilot1.transpose().conj())/400
#print np.dot(shift1[:,1:401],fpilot1.transpose().conj())/400
#print np.dot(shift1[:,2:402],fpilot1.transpose().conj())/400
#print np.dot(shift1[:,3:403],fpilot1.transpose().conj())/400
#print np.dot(shift1[:,4:404],fpilot1.transpose().conj())/400

Nt=2
tlen=400
A=np.arange(Nt)[np.newaxis]
dft_coef=np.exp(-2*np.pi*1j/Nt)
dft_matrix=np.power(dft_coef, np.dot(A.transpose(),A))
dft_pilot_seq=np.tile(dft_matrix,(tlen/Nt,1))
scramble_1=2*np.random.random_integers(0,1,size=(tlen,Nt))-1
pilot_seq_1=np.multiply(dft_pilot_seq,scramble_1) #tlen x Nt
channel=np.array([[1,0.5],[0.01,1]])
receive=np.dot(pilot_seq_1,channel)
corr = np.dot(pilot_seq_1.transpose().conj(), receive)/tlen
detect = np.linalg.norm(corr)
#print np.dot(scramble_1.transpose(),scramble_1)/tlen
#print np.dot(pilot_seq_1.transpose().conj(),pilot_seq_1)/tlen
#print corr
#print detect

nt = 2
Pt=100
P=0
nlinks=2
V=np.zeros((nlinks,nt,nt), dtype = np.float32)
Sinit = np.zeros((nlinks,nt,nt), dtype = np.float32)
a0 = np.zeros((nt,nt))
a1 = np.zeros((nt,nt))
for l in range(nlinks):
	V[l]=np.random.standard_normal(size=(nt,nt))
	Sinit[l]=np.dot(V[l],V[l].transpose())
	P=P+Sinit[l].trace()
alpha = np.true_divide(Pt,P)
Sinit=np.dot(Sinit,alpha).astype(np.float32)
print Sinit
a0[:] = Sinit[0]
a1[:] = Sinit[1]
print a0
print a1
print len(a0)








