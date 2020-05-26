import numpy as np
import matplotlib.pyplot as plt

def generate_studies(p, sample_size=128, nb_studies=1000):
	studies = np.zeros(nb_studies)
	for study in range(nb_studies):
		for sample in range(sample_size):
			if np.random.rand() < p:
				studies[study] += 1
		studies[study] = studies[study]/sample_size
	return studies; 

def histo(pp):
	np_histo = len(pp) # number of histograms
	fig, ax = plt.subplots(1, np_histo) # create plot
	for histo in range(np_histo):
		n, bins, patches = ax[histo].hist(pp[histo], 10, density=True); 
		ax[histo].set_xlabel('Estimate')
		ax[histo].set_ylabel('PDF of the Estimator')
	ax[0].set_title('True p={}, {} studies {} samples per study'.format(0.35,100,128))
	ax[1].set_title('True p={}, {} studies {} samples per study'.format(0.65,100,128))
	plt.show()


def lecture1(sample_size=128, nb_studies=1000):
	p1 = generate_studies(0.35, sample_size, nb_studies)
	p2 = generate_studies(0.65, sample_size, nb_studies)
	histo((p1,p2))

lecture1(nb_studies=5000)


def lecture2_7(f, n_max = 100):
    # param f: a bounded function
    # X_n ~ B(1/n) Bernouilli r.v.
    E_f_x_n = np.zeros(n_max)
    for n in range(1, n_max):
        E_f_x_n[n] = f(1)/n + f(0)*(1-1/n)
    fig, ax = plt.subplots(1, 1)
    ax.plot(range(n_max), E_f_x_n, label='E(cos(Xn))')
    ax.legend()
    ax.set_xlabel('n')
    ax.set_ylabel('Expectation')
    ax.set_title('Lecture 2-7  X_i ~ B(1/n) Convergence in distribution of E[f(Xn)]')
    ax.plot(range(n_max), np.ones(n_max), linestyle=':')
    plt.show()
lecture2_7(np.cos)
