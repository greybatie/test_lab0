import matplotlib.pyplot as plt
import numpy as np

f=open('/Users/margobatie/repos/NE204_lab0/lab0_spectral_data.txt', "r")
lines=f.readlines()[1:]


Am241=[] # 59.54 keV
Ba133=[] # 80.997 keV (34%) 302.853 keV (18%) 356.017 keV (62%)
Cs137=[] # 661.66 keV
Co60=[] # 1173.2 keV and 1332.51 keV
Eu152=[] # 344.28 keV (27%) 1112.1 keV (14%) 1408.1 keV (21%) 121.78 keV (26%)


for x in lines:
    x.split('\t')
    y=[int(s) for s in x.split() if s.isdigit()]
    Am241.append(y[0])
    Ba133.append(y[1])
    Cs137.append(y[2])
    Co60.append(y[3])
    Eu152.append(y[4])
# testing that input vectors have the same length
f.close()


len(Cs137)==len(Am241)==len(Cs137)==len(Co60)==len(Eu152)==8192

chan=list(range(1,len(Cs137)+1)) #number of channels:8192
#sources=[ for i in chan Am241[i]+Ba133[i]+Cs137[i]+Co60[i]+Eu152[i]]

centroid_Cs=np.argmax(Cs137) # 661.66 keV
centroid_Am=np.argmax(Am241) # 59.54 keV

x1=centroid_Am
x2=centroid_Cs

y1=59.5409
y2=661.657

energies=[]
m=float(y2-y1)/(x2-x1)
b=float(-m*x1+y1)
#print(m,b)
chan_array=np.array(chan)

for i in chan:
    energies.append(np.multiply(m, chan_array[i-1])+b)


#makes pretty of raw data
plt.semilogy(chan, Am241, label='Am-241')
plt.semilogy(chan, Ba133, label='Ba-133')
plt.semilogy(chan, Cs137, label='Cs-137')
plt.semilogy(chan,Co60, label='Co-60')
plt.semilogy(chan, Eu152, label='Eu-152')
plt.legend()
plt.xlabel('Channel Number')
plt.ylabel('Number of Counts')
plt.title('Imported Raw Data')
plt.savefig('/Users/margobatie/repos/NE204_lab0/images/rawdata.png')
plt.show()
