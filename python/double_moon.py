from data_sample.double_moon import *

if __name__ == '__main__':

    h1 = half_moon((0, 1))
    h2 = half_moon((0, -1), rotation = pi)
    h = [h1, h2]
    color = 'brr'
    #h1.plot_radius()
    #h2.plot_radius()
    y = []
    n = 2000
    samples = np.ones((3, n))
    for _ in range(n):
        label = randint(0, 1)
        if label:
            y.append(label)
        else:
            y.append(-1) # there is a significant difference between -1 and 0
                         # may also try other pairs like (2, -2), (1, -3), (1, 0)
        sample = h[label].generate_sample()
        samples[:2, _] = sample
    samples = np.array(samples)
    plt.scatter(samples[0], samples[1], color = [color[_+1] for _ in y])
    samples = np.matrix(samples)

    y = np.matrix([y])
    XXT = np.matmul(samples, samples.T)
    w = np.matmul(np.matmul(y, samples.T), np.linalg.inv(XXT))

    w = w.A1
    print(w)
    p = np.array([0, -w[2]/w[1]])
    d = np.array([1, (-w[0]-w[2])/w[1] + w[2]/w[1]])
    line = np.array([ p + 10 * d, p - 10 * d]).T
    plt.plot(line[0], line[1])
    plt.show()

