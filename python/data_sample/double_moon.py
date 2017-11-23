from math import pi, cos, sin, sqrt
from random import random, randint
import numpy as np
import matplotlib.pyplot as plt
import sys

class half_moon:

    def __init__(self, centre = (0, 0), out_rad = 10, in_rad = 7, angle = pi, rotation = 0):
        self.centre = centre
        self.out_rad = out_rad
        self.in_rad = in_rad
        self.angle = angle
        self.rotation = rotation

    def generate_radius(self):
        # the distribution of points on an array is not uniform, but
        # linearly proportional to radius, so we need to do some computation to
        # find a random point.
        r2 = self.in_rad ** 2
        R2 = self.out_rad ** 2
        radius_ = (R2 - r2) * random() + r2
        # radius ** 2 = radius_
        return sqrt(radius_)

    def generate_sample(self):
        angle = self.angle * random() + self.rotation
        radius = self.generate_radius()
        sample = np.array([radius * cos(angle), radius * sin(angle)])
        sample += self.centre
        return sample

    def generate_samples(self, num = 1000):
        samples = []
        for _ in range(num):
            angle = self.angle * random() + self.rotation
            radius = self.generate_radius()
            x = np.array([radius * cos(angle), radius * sin(angle)])
            x += self.centre
            samples.append(x)
            self.samples =  np.array(samples)
        return self.samples

    def plot_samples(self):
        samples = self.generate_samples()
        plt.scatter(samples[:, 0], samples[:, 1])
        #plt.show()

    def plot_radius(self):
        samples = self.generate_samples()
        radium = ((samples.T - np.array([self.centre]).T)**2).sum(0)
        n = 50
        plt.scatter(radium[:n], [1]*n)
        #plt.show()
