import pandas as pd
import matplotlib.pyplot as plt
import cmath

dataf = pd.read_csv("C:/Users/DELL/Desktop/data.csv")
x = dataf['x[n]']
y = dataf['y[n]']
n = [i for i in range(1, 194)]
'''

'''
def denoise(y):
    #y is the signal which would be denoise
    #n be the length of signal
    #list for storing all denoise value of each input
    l=[]
    n=len(y)
    for i in range(n):
        l.append(0)# string value 0 in the list
    l[-1]=(sum(y[n-3:])+sum(y[n-3:n-1]))/5   # for index -1 
    l[-2]=(sum(y[n-4:])+sum(y[n-3:n-2]))/5
    for i in range(n-2):
        if i==0:
            #for the zeroth element we take  average of first three element and element from index 1 to 3
            l[i]= (sum(y[:3])+sum(y[1:3])) / 5   
        elif i==1:
            #for the first element  we take average  of first four element and element from index 2 to 3
            l[i]=(sum(y[:4])+sum(y[2:3])) / 5
        else:
            #for the rest element we take average of first 5 elements
            l[i]=sum(y[i-2:i+3])/5
    return l
#x_t=denoise(y)
#steps to calculate fourier transform:
#1.calculate exponetial term 
#2. calculating product of signal with exponential term
#3.calculate integration of above part by summation
#4.return list contaning sum
def fourier_transform(X):
    L = []
    for w in range(0, 193):
        Y = 0
        for p in range(0, len(y)):
            Y = Y+((X[p]*(cmath.exp(complex(0, ((-1*2*cmath.pi*w*(p+1)/193)))))))
        L.append(Y)
    return L
#steps to calculate fourier transform:
#1.calculate exponetial term 
#2. calculating product of signal with exponential term
#3.calculate integration of above part by summation
#4.return list contaning sum
def fourier_transform_h(X,L):
    h=[0.0625,0.25,0.375, 0.25, 0.0625]
    L1 = []
    for w1 in range(0, 193):
        Y1 = 0
        for p1 in range(0, len(h)):
            Y1 = Y1+((h[p1]*(cmath.exp(complex(0, ((-1*2*cmath.pi*w1*(p1-2)/193)))))))
        if Y1.real <= 0.35:
            Y1 = 0.35
        L1.append(L[w1]/Y1)
    return L1
#step to calculate inverse fourier transform
#1.calculate exponential part 
#2. calculating product of signal with exponential term
#3.calculate integration of above part by summation
#4.divide this list by length of the list (here 193)
#5. return list contaning sum
def ift(L1):
    X1 = []
    for t in range(0, 193):
        F = 0
        for r in range(0, len(y)):
            F = F+((L1[r])*cmath.exp(complex(0, 2*r*cmath.pi*t/193)))
        X1.append(F/193)
    return X1
    
h=[0.0625,0.25,0.375, 0.25, 0.0625]
x_t=denoise(y)
x1_n=fourier_transform(x_t)
h_n=fourier_transform_h(h,x1_n)
#X2=denoise(X2)
X1=[]
X1=ift(h_n)
plt.plot(X1,label='x1[n]')
plt.plot(x,label='x[n]')
plt.title('Graph of x1[n] and x[n]')
plt.legend()
plt.show()
x2_n=fourier_transform(y)
h_n=fourier_transform_h(h,x2_n)
X_dbr=ift(h_n)
X2 = denoise(X_dbr)
plt.plot(X2,label='x2[n]')
plt.plot(x,label='x[n]')
plt.title('Graph of x2[n] and x[n]')
plt.legend()
plt.show()
MSE1 = 0
for i in range(193):
    MSE1 += (y[i] - x[i])**2
MSE1 = MSE1/193
print(abs(MSE1))
MSE2= 0
for i in range(193):
    MSE2 += (X1[i] - x[i])**2
MSE2 = MSE2/193
print(abs(MSE2))
MSE3 = 0
for i in range(193):
    MSE3 += (X2[i] - x[i])**2
MSE3 = MSE3/193
print(abs(MSE3))
    

