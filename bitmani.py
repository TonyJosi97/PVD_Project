val = 111
data = '100'
bival = bin(val)
bival = bival[2:]
newbival = bival[:(len(bival)-len(data))] + data
print(bival,newbival,int(bival,2),int(newbival,2)) 