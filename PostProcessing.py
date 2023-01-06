# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:17:18 2021

@author: Rahul Ramaraju
"""
from __future__ import division
def Index(pN,Velocity):
    index = Velocity + 3*pN
    if (Velocity) == 1:
        label = "Vx"
    if (Velocity) == 2:
        label = "Vy"
    if (Velocity) == 3:
        label = "Vz"
    return label, index
def ArrayCreate(number,tstart,tend,location= None):
    import numpy as np
    import io
    if location == None:
        loc = "0/U"
    file = open(loc).read().replace('(',' ').replace(')',' ')
    data = np.loadtxt(io.StringIO(file),skiprows=0,dtype=str)
    array2 = []
    timestep = float(data[len(data)-1,0])/float(len(data))
    for x in range(int((tstart/timestep)),int((tend/timestep)),1):
        array2.append(data[x,number])
    array1 = np.array(array2)
    aray1 = array1.astype(float)
    return aray1
class Graphs():
    def Tser(pN,Velocity,tstart,tend):
        """
        Parameters
        pN : Integer
            The probe number starting from 0
        Velocity : Integer
            1 = Vx; 2 = Vy; 3 = Vz
        tstart : Integer
            time start
        tend : Integer
            time end
        """
        import matplotlib.pyplot as plt
        import numpy as np
        time = ArrayCreate(0,tstart,tend)
        label, index = Index(pN,Velocity)
        y = ArrayCreate(index,tstart,tend)
        plt.plot(time, y)
        plt.xlim(tstart,tend)
        plt.xlabel("Time")
        plt.ylabel(label)
        plt.title("Time vs Particle Number " + str(pN) + " " + str(label) + " : ")
        plt.savefig('TimeSer {}-{}.png'.format(pN,label),format= "png")
        plt.close()
        return()
    def CrossCorrelation(pN1,Velocity1,pN2,Velocity2,tstart,tend):
        """
        Parameters
        pN1 / pN2 : Integer
            The probe number starting from 0
        Velocity1 / Velocity2 : Integer
            1 = Vx; 2 = Vy; 3 = Vz
        tstart : Integer
            time start
        tend : Integer
            time end
        """
        import matplotlib.pyplot as plt
        from scipy.signal import correlate
        import numpy
        label1, index1 = Index(pN1,Velocity1)
        label2, index2 = Index(pN2,Velocity2)
        compare1 = ArrayCreate(index1,tstart,tend)
        compare2 = ArrayCreate(index2,tstart,tend)
        time = ArrayCreate(0,tstart,tend)
        Cross = correlate(compare1,compare2)
        length = len(Cross)
        Cross = 2*Cross/length
        len_1 = len(compare1)
        duration = time[len_1-1]- time[0];
        dt=duration/float(len_1-1)
        duration=length*dt/2;
        d= numpy.linspace( -duration, duration, length )
        idx = numpy.argmax(Cross)
        print (" Maximum:  Delay=%8.4g sec   Amp=%8.4g " %(d[idx],Cross[idx]))
        plt.plot(d, Cross)
        plt.xlabel('Time')
        plt.ylabel("Cross Correlation Value")
        plt.legend(" Maximum:  Delay=%8.4g sec   Amp=%8.4g " %(d[idx],Cross[idx]))
        plt.title('Cross Correlation - ' + str(pN1)  + str(label1) + " x " + str(pN2)  + str(label2) +':')
        plt.savefig('Cross {}-{} x {}-{}.png'.format(pN1,label1,pN2,label2),format= "png")
        plt.close()
        return()
    def Pspec():
        import numpy as np
        import matplotlib.pyplot as plt
        import math
        #label1, index = Index(pN1,Velocity)
        #y = ArrayCreate(index,tstart,tend)
        y = np.array([0])
        for x in range(0,100,2):
            x = 10*(math.cos(math.pi*math.radians(x)))
            print(x)
            print(y)
            y = np.append(y,[x])
        ps = np.abs(np.fft.fft(y))**2
        time_step = 1 
        freqs = np.fft.fftfreq(y.size, time_step)
        idx = np.argsort(freqs)
        plt.plot(freqs[idx], ps[idx])
        return()
    
Graphs.Pspec()
        
        
        
#Graphs.CrossCorrelation(1,16,0,50)
#Graphs.Tser(1,1,0,2.5)


