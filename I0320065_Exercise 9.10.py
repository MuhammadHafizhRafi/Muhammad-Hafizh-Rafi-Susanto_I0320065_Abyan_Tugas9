#nilai awal (sebelum dibalik)
import array
A = array.array('i', [100,200,300,400,500])
print(A)

A[1] = -700
A[4] = 800
print(A)
A.reverse()
print(A)