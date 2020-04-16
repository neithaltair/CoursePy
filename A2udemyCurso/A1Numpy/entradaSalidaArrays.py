import numpy as np

array0 = np.arange(6)
print(array0)

#se puede guardar el array
np.save('array1s',array0)
print(np.load('array1s.npy'))

array1= np.arange(6)
array2=  np.arange(8)
#Salvar dos array con la misma variable
np.savez('arraysDob',x=array1,y=array2)


arrayRecuperado = np.load('arraysDob.npz')
print(arrayRecuperado['y'])


#SALVAR EN FICHERO DE TEXTO EL ARRAY
arrayT = ([54,54,54,28,1,58,1,5,456,45,84,15,486,1])
np.savetxt('mifichero.txt',arrayT,delimiter=',')

np.loadtxt('mifichero.txt',delimiter=',')
print(arrayT)