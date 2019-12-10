import matplotlib.pyplot as plt
import csv

x=[]
y=[]
z=[]
a=[]
with open('HIMU-2019-12-10_13-37-45.csv') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    
    for i in plots:
        a.append(i)

    for j in range(4,741):
        x.append(float(a[j][0]))
    for j in range(4,741):
        y.append(float(a[j][1]))
    for j in range(4,741):
        z.append(float(a[j][2]))




plt.plot(x,label='x-axis')
plt.plot(y,label='y-axis')
plt.plot(z,label='z-axis')

plt.xlabel('x')
plt.ylabel('y')

plt.title('kalman filter')
plt.legend()
plt.show()
#HIMU-2019-12-09_22-25-18
