from PIL import Image
import sys

im = Image.open("test.png")
input = open("enc", "r")
outp = open("retrieved", "w")
lg = open("embedlog", "w")

pix = im.load()
hi, wi = im.size

completed = 0
retrieved = ""
count = 0
paddbits = "0000000"

binval = input.read(1)
if len(binval) == 0:
    print("\nEmpty i/p File!")
b = ord(binval)
# print(eightbit)
bitstring = bin(b)
bits = bitstring[2:]

capacity = 0
lix = hi // 3
liy = wi // 3


def classify(pvd):
    nbits = 0
    if pvd < 16:
        nbits = 2
    elif 16 < pvd < 32:
        nbits = 3
    else:
        nbits = 4
    return nbits


def calcCapacity():
    global capacity
    for i in range(0, lix * 3, 3):
        for j in range(0, liy * 3, 3):
            rref, gref, bref = pix[i + 1, j + 1]
            for k in range(i, (i + 3)):
                if k >= hi:
                    break
                for l in range(j, (j + 3)):
                    if k == i + 1 and l == j + 1:
                        continue
                    if l >= wi:
                        break
                    r, g, b = pix[k, l]
                    rdif = r - rref
                    gdif = g - gref
                    bdif = b - bref
                    rdif = abs(rdif)
                    gdif = abs(gdif)
                    bdif = abs(bdif)
                    capacity = (
                        capacity + classify(rdif) + classify(gdif) + classify(bdif)
                    )
    return capacity


def embedbits(i, j, pixel, diff, colorpixel):
    nb = diff
    global bits
    global count
    global bitstring
    global retrieved
    global paddbits
    global binval
    global completed
    pad = 0
    if nb < len(bits):
        # print(bits,end=" ")
        newbits = bits[:nb]
        bits = bits[nb:]
        # print(newbits)
        retrieved += newbits
        val = colorpixel
        data = newbits
        bival = bin(val)
        bival = bival[2:]
        newbival = bival[: (len(bival) - len(data))] + data
        # print(bival,newbival)
        # print("location:",i,j,"pixel:",pixel,"no of bits:",diff,"pad:",pad)
        lg.write("%s %s %s %s %s %s" % (i, j, pixel, diff, pad, "\n"))
        return int(newbival, 2)
    else:
        newbits = bits + paddbits[: (nb - len(bits))]
        pad = nb - len(bits)
        retrieved += newbits
        # print("pad",newbits)
        # print("stats",newbits,retrieved)
        val = colorpixel
        data = newbits
        bival = bin(val)
        bival = bival[2:]
        newbival = bival[: (len(bival) - len(data))] + data
        count += 1
        retrieved = retrieved[: (len(retrieved) - pad)]
        # print("Info for",count,"data:","retrieved -",int(retrieved,2),"orginal - ",int(bitstring,2))
        binval = input.read(1)
        if len(binval) == 0:
            # print("location:",i,j,"pixel:",pixel,"no of bits:",diff,"pad:",pad)
            lg.write("%s %s %s %s %s %s" % (i, j, pixel, diff, pad, "\n"))
            print("Embedding Completed")
            completed = 1
            # print(bival,newbival)
            return int(newbival, 2)
        outp.write(chr(int(retrieved, 2)))
        b = ord(binval)
        # print(eightbit)
        bitstring = bin(b)
        bits = bitstring[2:]
        retrieved = ""
        # print(bival,newbival)
        # print("location:",i,j,"pixel:",pixel,"no of bits:",diff,"pad:",pad)
        lg.write("%s %s %s %s %s %s" % (i, j, pixel, diff, pad, "\n"))
        return int(newbival, 2)


print("Total Embd. Capacity: ", calcCapacity())
for i in range(0, lix * 3, 3):
    for j in range(0, liy * 3, 3):
        # print("--------------")
        rref, gref, bref = pix[i + 1, j + 1]
        for k in range(i, (i + 3)):
            if k >= hi:
                break
            for l in range(j, (j + 3)):
                if k == i + 1 and l == j + 1:
                    continue
                if l >= wi:
                    break
                r, g, b = pix[k, l]
                rdif = r - rref
                gdif = g - gref
                bdif = b - bref
                rdif = abs(rdif)
                gdif = abs(gdif)
                bdif = abs(bdif)
                if completed == 0:
                    newr = embedbits(k, l, "r", classify(rdif), r)
                if completed == 0:
                    newg = embedbits(k, l, "g", classify(gdif), g)
                if completed == 0:
                    newb = embedbits(k, l, "b", classify(bdif), b)
                if completed == 1:
                    im.save("protest.png")
                    lg.close()
                    sys.exit("Done..Exiting main prog.")
                capacity = capacity + classify(rdif) + classify(gdif) + classify(bdif)
                # print("\n__",k,l,": ",pix[k,l],"bits: ",classify(rdif),classify(gdif),classify(bdif),"binary: ",'{0:08b}'.format(r))
                pix[k, l] = (newr, newg, newb)

