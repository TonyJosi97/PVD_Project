import contextlib, sys
from random import randint
python3 = sys.version_info.major >= 3

paddbits = '0000000'

def rand():
    return randint(3, 5)

def main(args):
    ipfile = args
    outp = open("retrieved","w")
    count = 0
    with open(ipfile, "r") as input:
        while True:
            binval = input.read(1)
            if len(binval) == 0:
                break
            b = ord(binval)
            #print(eightbit)
            bitstring = bin(b)
            bits = bitstring[2:]
            retrieved = ''
            while True:
                nb = rand()
                count += 1
                if(nb < len(bits)):
                    #print(bits,end=" ")
                    newbits = bits[:nb]
                    bits = bits[nb:]
                    #print(newbits)
                    retrieved += newbits
                    #print("stats",newbits,retrieved,end=" ")
                else:
                    newbits = bits + paddbits[:(nb-len(bits))]
                    pad = nb-len(bits)
                    retrieved += newbits
                    #print("pad",newbits)
                    #print("stats",newbits,retrieved,end=" ")
                    break
            retrieved = retrieved[:(len(retrieved)-pad)]
            #print()
            print(chr(int(retrieved,2)),end="")
            outp.write(chr(int(retrieved,2)))
    outp.close()

if __name__ == "__main__":
	main(sys.argv[1])