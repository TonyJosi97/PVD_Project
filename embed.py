from PIL import Image

im = Image.open('test.png')
pix = im.load()
hi,wi = im.size 

def classify(pvd):
    bits = 0
    if(pvd < 16):
        bits = 2
    elif(16 < pvd < 32):
        bits = 3
    else:
        bits = 4
    return bits

capacity = 0

lix = hi//3
liy = wi//3

for i in range(0,lix*3,3):
    for j in range(0,liy*3,3):
        print("--------------")
        rref,gref,bref = pix[i+1,j+1]
        for k in range(i,(i+3)):
            if(k >= hi):
                break
            for l in range(j,(j+3)):
                if(l >= wi):
                    break
                r,g,b = pix[k,l]
                rdif = r - rref
                gdif = g - gref
                bdif = b - bref
                rdif = abs(rdif)
                gdif = abs(gdif)
                bdif = abs(bdif)
                capacity = capacity + classify(rdif) + classify(gdif) + classify(bdif)
                print("__",k,l,": ",pix[k,l],"bits: ",classify(rdif),classify(gdif),classify(bdif),"binary: ",'{0:08b}'.format(r))
                pix[k,l] = (rdif,gdif,bdif)
im.save('protest.png')

print("\nCapacity: ",capacity)