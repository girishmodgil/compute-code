#Monte Carlo Simulation Example
#Estimate Pi
def estimate_pi(nsamples):
    xval = []
    yval = []
    sqx = []
    sqy = []   
    inc = 0 #inside the circle
    for i in range(nsamples):
        #Assume a unit circle
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (x**2 + y**2) <= 1:
            inc = inc + 1
            xval.append(x)
            yval.append(y)
        else:
            sqx.append(x)
            sqy.append(y)
            
    pi_estimate = 4 * (float(inc)/nsamples)
    
    return pi_estimate, xval, yval, sqx, sqy


if __name__ == "__main__":

    import math
    import random
    
    ans, xvals, yvals, sqxs, sqys = estimate_pi(1000)
    print(ans)

    import matplotlib.pyplot as plt 

    plt.plot(xvals, yvals, 'rx')
    plt.plot(sqxs, sqys, 'bo')
    plt.title('Estimate is ' + str(ans))
    plt.show()

