import numpy as np
import math
import random

def phi(x):
    if x > 40:
        return 1
    elif x < -40:
        return 0
    else:
        x = 1.0 + math.exp(-x)
        return 1.0 / x

def d_phi(x):
    x = phi(x)
    return x * (1.0 -x)

class MultiPerceptron(object):
    def __init__(self, eta=1, n_iter=10, num_node0=20):
        self.eta = eta
        self.n_iter = n_iter
        self.num_node0 = num_node0

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target values.

        Returns
        -------
        self : object

        """
        x = [[],[]]
        for i in range(self.num_node0):
            x[0].append(random.random() * 1)
            x[1].append(random.random() * 1)
        self.w0_ = np.array(x)
        #self.y0_ = np.array([ 0 ] * self.num_node0) # y0_ = (X * w0_)
        x = []
        for i in range(self.num_node0):
            x.append(random.random() * (-1))
        self.shift0_ = np.array(x)
        #self.phi_y0_ = np.array([ 0 ] * self.num_node0) # phi_y0_ = phi(y0_+shift0_)
        x = []
        for i in range(self.num_node0):
            x.append(random.random() * 1)
        self.w1_ = np.array(x)
        #self.y1_ = 0 # y1_ = (phi_y0_ * w1_ )
        self.shift1_ = random.random() * (-1)
        self.errors_ = []

        for _ in range(self.n_iter):
            #print(self.shift1_)
            errors = 0
            eta = self.eta
            for xi, target in zip(X, y):
                y0_, y1_, phi_y0_, output = self.net_input_helper(xi)

                err = target - output

                if abs(err) >= 0.5:
                    errors += 1

                    delta_output = err * d_phi( y1_ + self.shift1_ )
                    delta_phi_y0_ = np.array([[0.0] * self.num_node0])
                    for i in range(self.num_node0):
                        delta_phi_y0_[0, i] = delta_output * (d_phi(y0_[i] + self.shift0_[i]) * self.w1_[i])

                        self.shift0_[i] += eta * delta_phi_y0_[0, i]

                    self.w0_ = np.add(self.w0_, eta * (np.dot( np.array([xi]).T, delta_phi_y0_)))
                    self.w1_ = np.add(self.w1_, eta * delta_output * phi_y0_)
                    self.shift1_ += eta * delta_output
                    eta -= self.eta / len(y)
            self.errors_.append(errors)
            if errors == 0:
                print('training terminated after', _, 'steps because no errors occurred.')
                break
        return self

    def net_input_helper(self, xi):
        """Calculate net input"""
        y0_ = np.dot(xi, self.w0_)
        x = []
        for i in range(self.num_node0):
            x.append(random.random() * 1)

        phi_y0_ = np.array(x)
        for i in range(self.num_node0):
            #print(y0_[i])
            phi_y0_[i] = phi( y0_[i] + self.shift0_[i] )
        y1_ = np.dot(phi_y0_, self.w1_)
        output = phi( y1_ + self.shift1_ )
        return y0_, y1_, phi_y0_, output

    def net_input(self, xi):
        return self.net_input_helper(xi)[3]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.5, 1, 0)

