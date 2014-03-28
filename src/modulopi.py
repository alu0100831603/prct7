#!/usr/bin/python
import sys
PI = 3.1415926535897931159979634685441852
def funcion(n):
   suma=0.0
   for i in range(1,n+1):
     x_i=float(i-1.0/2)/n
     
     fx_i= 4.0/(1+x_i**2)
     suma=suma+fx_i
   pi = (1.0/float(n))*suma
   return pi
   
if __name__ == "__main__":
  
if len(sys.argv)==3:
    n=sys.argv[1]
    m=sys.argv[2]
else:
     print 'El modo de uno es: modulopi.py numero numero' 
     n=5
     m=10
for repeticion in range(1,veces+1):
     zpi = funcion(n)
     z = z+[zpi]
     resta = funcion(n) - PI
     print'%d %1.35f | %1.35f | %1.35f' % (repeticion, PI, funcion(n), resta)
     n = n*2
   print z      