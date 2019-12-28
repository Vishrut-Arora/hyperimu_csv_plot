import matplotlib.pyplot as plt
import csv

x=[]
y=[]
z=[]
b=[]
c=[]
d=[]
t=[]
a=[]

vx=0
ux=0
vy=0
uy=0
vz=0
uz=0
delta_s_x=0
delta_s_y=0
delta_s_z=0
with open('Task2.csv') as csvfile:
    plots = csv.reader(csvfile)

    for i in plots:
        a.append(i)
    for j in range(4,291):
        t.append(float(a[j][0])*(10**-3))



    for j in range(4,291):
        x.append(float(a[j][0]))
    for j in range(4,291):
        y.append(float(a[j][1]))
    for j in range(4,291):
        z.append(float(a[j][2]))
    for j in range(4,291):
        b.append(float(a[j][3]))
    for j in range(4,291):
        c.append(float(a[j][4]))
    for j in range(4,291):
        d.append(float(a[j][5]))

    for j in range(0,287):
        ax=(x[j]-b[j])
        vx=ux+ax*0.1
        delta_s_x+=(ux*0.1+ax*0.5*0.01)
        ux=vx
        ay=(y[j]-c[j])
        vy=uy+ay*0.1
        delta_s_y+=(uy*0.1+ay*0.5*0.01)
        uy=vy
        az=(z[j]-d[j])
        vz=uz+az*0.1
        delta_s_z+=(uz*0.1+az*0.5*0.01)
        uz=vz

    print(delta_s_x," ",delta_s_y," ",delta_s_z)
