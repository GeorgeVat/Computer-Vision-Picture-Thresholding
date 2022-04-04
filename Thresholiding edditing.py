import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image
import sys

#1. Read the picture 
A = np.array(Image.open(sys.argv[1])) 
grammes = A.shape[0]
stiles = A.shape[1]
print(grammes, stiles)
#print(len(A.shape))

plt.imshow(A,cmap="gray")
plt.show()

#2. if the picture has colors, i transform it in 2 dimensions
E= np.zeros([grammes,stiles])

if(len(A.shape)==3):  # if has colors
    print('OPA')
    for m in range (1, grammes):
        for n in range (1, stiles):
            E[m][n]=(A[m][n][0]+A[m][n][1]+A[m][n][2])/3
else: # grayscale
    for m in range (1, grammes):
        for n in range (1, stiles):
            E[m][n]=A[m][n]

#3. Second argument, threshold
threshold=int(sys.argv[2])



#4. Vriskw tin katwfliomeni eikona (estw Ak)
Ak= np.zeros([grammes,stiles])
for m in range (1,grammes):
    for n in range (1,stiles):
        if(E[m,n]<=threshold):
            Ak[m,n]=0  # 0 = mayro hroma sta grammata tis eikonas
        else:
            Ak[m,n]=255 # 255 = aspro hroma sto fonto

#5. Emfanizw tin katwfliomeni eikona kai meta tin apothikeyw
plt.imshow(Ak,cmap="gray")
plt.show()
#Image.fromarray(Ak.astype(np.uint8)).save(sys.argv[2])





