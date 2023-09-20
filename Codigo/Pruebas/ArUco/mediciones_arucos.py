#Prueba valores de pixeles
import numpy as np

cantidad = 40
disxpix = np.zeros((2,cantidad))
for i in range (cantidad -1):
  disxpix[0][i] = input("distancia")
  disxpix[1][i] = input("pixeles")
for i in range(cantidad -1):
  print("distancia", i, disxpix[0][i])
  print("pixeles", i, disxpix[1][i])
