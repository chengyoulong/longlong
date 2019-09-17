import matplotlib.pyplot as plt 
import numpy as np 

def fitting(x_n,y_n):
    x = np.array(x_n)
    y = np.array(y_n)
    A = np.vstack([x,np.ones(len(x))]).T
    m,c= np.linalg.lstsq(A, y)[0]
    end = 'y = '+str(m)+'x'+str(c)
    plt.plot(x,y,'o',label='Orginal date',markersize=10)
    plt.plot(x,m*x + c,'r',label='Fitted line')
    plt.legend()
    plt.show()
    print(end)

if __name__ == "__main__":
    fitting([0,1,2,3],[-1,0.2,0.9,2.1])
