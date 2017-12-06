import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import pylab
from sklearn.metrics.cluster import \
	mutual_info_score, normalized_mutual_info_score, adjusted_mutual_info_score


ising_slice = np.loadtxt("slice_Tc", delimiter = ",")
adpNN_r = np.load("r1_64.npy")

def plot_MI_distance(data, ax, marker, dmax = 25, method = 'NMI'):
	if len(data.shape) == 1:
		assert(len(data)%dmax == 0)
		data = data.reshape(len(data)//dmax,dmax)
	N,dmax = data.shape
	print(dmax)
	if method == 'NMI':
		NMIs = np.zeros(dmax)
		for d in range(1,dmax):
			NMIs[d] = normalized_mutual_info_score(data[:,0], data[:,d])
		MIs = NMIs

	if method == 'AMI':
		AMIs = np.zeros(dmax)
		for d in range(1,dmax):
			AMIs[d] = adjusted_mutual_info_score(data[:,0], data[:,d])
		MIs = AMIs

	if method == 'self_NMI':
		self_NMIs = np.zeros(dmax)
		for d in range(1,dmax):
			self_NMIs[d] = MI(data[:,0], data[:,d])
		MIs = self_NMIs
	# return ax.plot(range(1,dmax), MIs[1:dmax],'o')	
	return ax.plot(np.log10(range(1,dmax)), np.log10(MIs[1:dmax]),marker)[0]

def plot_all():
	plt.close('all')
	axes = [0]
	fig,axes[0] = plt.subplots(1)
	fig.set_size_inches(10, 5)

	ising_NMIs = plot_MI_distance(data=ising_slice[:,:25], ax=axes[0], marker='ro')
	ising_AMIs = plot_MI_distance(data=ising_slice[:,:25], ax=axes[0], method='AMI', marker='r-')
	ising_self_NMIs = plot_MI_distance(data=ising_slice[:,:25], ax=axes[0], method='self_NMI', marker='r--')
	adpNN_NMIs = plot_MI_distance(data=adpNN_r, ax=axes[0], marker='bo')
	adpNN_AMIs = plot_MI_distance(data=adpNN_r, ax=axes[0], method='AMI', marker='b-')
	adpNN_self_NMIs = plot_MI_distance(data=adpNN_r, ax=axes[0], method='self_NMI', marker='b--')

	plt.xlabel('log(d(X,Y))')
	plt.ylabel('log(I(X;Y))')
	plt.legend((ising_NMIs, ising_AMIs, ising_self_NMIs, adpNN_NMIs, adpNN_AMIs, adpNN_self_NMIs),\
		('Ising_NMI', 'Ising_AMI', 'Ising_self_NMI', 'AdpNN_r_NMI', 'AdpNN_r_AMI', 'AdpNN_self_NMI'))
	# plt.savefig('MI_sklearn.png')
	plt.show() 

def H(Px):
	return np.sum(-Px * np.log2(Px))

def MI(x, y, bins = [[-1.5, 0.5, 1.5],[-1.5, 0.5, 1.5]], normalized = True):
	Nxy = np.histogram2d(x, y, bins = bins)[0]
	Nx = np.sum(Nxy, axis=0)
	Ny = np.sum(Nxy, axis=1)
	Pxy = Nxy/np.sum(Nxy)
	Px = Nx/np.sum(Nx)
	Py = Ny/np.sum(Ny)
	mi = H(Px) + H(Py) - H(Pxy)
	if normalized:
		mi = mi/np.sqrt(H(Px)*H(Py))
	return mi
 
# mutual_info(ising_slice[:,0], ising_slice[:,1])

plot_all()