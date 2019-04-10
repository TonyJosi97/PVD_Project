from PIL import Image
import sys, os

im = Image.open(sys.argv[1])
# input = open(sys.argv[2], "w")
lg = open("embedlog.log", "r")

pix = im.load()
hi, wi = im.size
temp = 1
chrtr = ""

while True:
    st = lg.readline()
    if len(st) == 0:
        print(chr(int(chrtr, 2)))
        break
    i, j, pixel, diff, pad, charNum = st.split()
    i = int(i)
    j = int(j)
    diff = int(diff)
    pad = int(pad)
    charNum = int(charNum)
    # print(i, j, pixel, diff, pad, charNum)
    # print(pix[i,j])
    r, g, b = pix[i, j]
    if temp != charNum:
        print(chr(int(chrtr, 2)), end="")
        # print()
        chrtr = ""
    if pixel == "r":
        binr = bin(r)
        chrtr += binr[(len(binr) - diff) :]
        # print(i,j,pixel,binr,"before pad - ",chrtr,end=" ")
        if pad != 0:
            chrtr = chrtr[: (len(chrtr) - pad)]
            # print("after pad - ",chrtr,end=" ")
    if pixel == "g":
        binr = bin(g)
        chrtr += binr[(len(binr) - diff) :]
        # print("before pad - ",chrtr,end=" ")
        if pad != 0:
            chrtr = chrtr[: (len(chrtr) - pad)]
            # print("after pad - ",chrtr,end=" ")
    if pixel == "b":
        binr = bin(b)
        chrtr += binr[(len(binr) - diff) :]
        # print("before pad - ",chrtr,end=" ")
        if pad != 0:
            chrtr = chrtr[: (len(chrtr) - pad)]
            # print("after pad - ",chrtr,end=" ")
    temp = charNum
