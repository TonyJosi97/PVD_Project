from PIL import Image

im = Image.open('protest.png') # Can be many different formats.
pix = im.load()
hi,wi = im.size 

mi = 0
mj = 0
count = 0

print(hi,wi)

for i in range(hi//3):
    for j in range(wi//3):
        if(mi + 3 > hi and mj + 3 > wi):
                break
        print("\n************************\n")
        for k in range(mi, mi+3):
            for l in range(mj, mj+3):
                r, g, b = pix[l, k]
                print("\n--",l,k,end=" ")
                print("pix ", r, g, b, end=" ")
                print(pix[l,k], end=" ")
        print()
        mi = mi+3
        mj = mj+3
        count += 1

print("co : ", count)


'''
for i in range(hi):
    for j in range(wi):
            r,g,b = pix[i,j]
            print("__",i,j,"rgb - ",r,g,b,"pix = ",pix[i,j],end=" ")
            print()
'''