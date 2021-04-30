#mendefinisikan objek array dengan nilai awal tertentu
import array
A = array.array('i', [100,200,300,400,500])
print(A)

#jika ingin mengubah nilai dari elemen tertentu
A[1] = -700 #mengubah elemen kedua
A[4] = 800  #mengubah elemen kelima
print(A)