import pickle

pk_file=open("banner.p","rb")

data=pickle.load(pk_file)
str=""

for list in data:
    print(list)
    for i in list:
        str += i[0]*i[1]
    str += '\n'
print(str)    
