import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

hdulist = pyfits.open("/Users/User/Downloads/v523cas60s-001(1).fit")
hdulist.info()
scidata = hdulist[0].data # обращаемся к самому изображению

# середина звезды
yser = 1165
xser = 474
r = 10
valuex = []
valuey = []
x = []
y = []
for i in range(xser - r, xser + r):
    valuex.append(scidata[yser][i])
    x.append(i)

for j in range(yser - r, yser + r):
    valuey.append(scidata[j][xser])
    y.append(j)

plt.figure()
plt.subplot(2, 1, 1)

plt.plot(x, valuex)
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Зависимость Value от x при y = 1165')

plt.subplot(2, 1, 2)
plt.plot(y, valuey)
plt.xlabel('y')
plt.ylabel('Value')
plt.title('Зависимость Value от y при x = 474')
plt.subplots_adjust(wspace=1, hspace=1)
plt.show()

hdulist.close()


