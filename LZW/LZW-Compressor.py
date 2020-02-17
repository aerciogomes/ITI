# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:54:36 2020

@author: aerci
"""

###FAZER
    
def getKeysByValue(dictOfElements, valueToFind):    
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            return item[0]
    return  -1

#COMPRESSOR    
ascii_table = {}
asciis_table = {}

for i in range(256):
    asciis_table[i] = bytes([ord(chr(i))]) 
    

texto = []
K = 9
MAX = 2**K
table_size = len(asciis_table)


ascii_tables = teste

ascii_table = asciis_table.copy()

output = []
i = 0
byte = ascii_tables[i]
s = b''
while byte != b"":
    #verifica se o byte atual + anterior está no dicionário
    index = getKeysByValue(ascii_table,s+byte)
    
    #se sim, atualiza o anterior com o atual
    if index != -1:
        s += byte
    #caso não, coloca o index no output e acrescenta no dicionario os bytes concatenados se possivel
    else:
        #TODO:
        #encode s to output file;
        output.append(getKeysByValue(ascii_table,s))
        ##output.append(index.bit[9])
        if table_size < MAX:
            ascii_table[table_size] = s + byte
            table_size += 1
        s = byte;
        
    i += 1    
    byte = ascii_tables[i]
    
byte = b'EOF'
index = getKeysByValue(ascii_table,s+byte)

#se sim, atualiza o anterior com o atual
if index != -1:
    s += byte
#caso não, coloca o index no output e acrescenta no dicionario os bytes concatenados se possivel
else:
    #TODO:
    #encode s to output file;
    output.append(getKeysByValue(ascii_table,s))
    ##output.append(index.bit[9])
    if table_size < MAX:
        ascii_table[table_size] = s + byte
        table_size += 1
    s = byte;
    
    
#DESCOMPRESSOR

table_size = len(asciis_table)
ascii_table = asciis_table.copy()
palavra = []
word = []
s = b''
i = 0
byte = ascii_table[output[i]]

palavra.append(byte)
word.append(byte[0])
i += 1

while i < len(output):
    s = byte
    if output[i] >= len(ascii_table):
        teste = s+ascii_table[output[0]]
        palavra.append(teste)
        for j in range(len(teste)):
            word.append(teste[i])
        if table_size < MAX:
            ascii_table[table_size] = s + ascii_table[output[0]]
            table_size += 1
        byte = ascii_table[output[i]]
        i += 1
        continue
        
    byte = ascii_table[output[i]]
    
    if getKeysByValue(ascii_table,byte) != -1:
        palavra.append(byte)
        for j in range(len(byte)):
            word.append(byte[j])
        P = s
        C = byte[0:1]
        if table_size < MAX:
            ascii_table[table_size] = P+C
            table_size += 1
    else:
        P = s
        C = s[0:1]
        s = P + C
        if table_size < MAX:
            ascii_table[table_size] = P+C
            table_size += 1
    i += 1


index = 0  
    
        
    
    

teste = []

with open("corpus16MB.txt", "rb") as f:
    #ler byte
    byte = f.read(1)
    s = b''
    while byte != b"":
        teste.append(byte)
        #verifica se o byte atual + anterior está no dicionário
#        index = getKeysByValue(ascii_table,s+byte)
#        
#        #se sim, atualiza o anterior com o atual
#        if index != -1:
#            s += byte
#        #caso não, coloca o index no output e acrescenta no dicionario os bytes concatenados se possivel
#        else:
#            #TODO:
#            #encode s to output file;
#            output.append(getKeysByValue(ascii_table,s))
#            ##output.append(index.bit[9])
#            if table_size < MAX:
#                ascii_table[table_size] = s + byte
#                table_size += 1
#            s = byte;
            
            
        byte = f.read(1)
    
len(teste)

ufa2 = []
ufa2.append(bytes())
    
print(ascii_table[261])
    
print(b'' + b''+ufa[0]+'')
    

alou = []
for i in range(len(output)):
    alou.append(bin(output[i]))

testeoi = []
for i in range (55):
    testeoi.append(i)
    

    
arquivo = open('compressor.txt','w')
arquivo.write(str(output))
arquivo.close()

encoding = 'utf-8'
print(palavra[49])
print(i)
teste4 = []
for i in range(len(palavra)):
    teste4.append(str(palavra[i],"utf-8"))
    
arquivo = open('descompressor.txt','wb')
for j in range(len(palavra)):
    arquivo.write(palavra[j])
arquivo.close()

print(teste3[6])

print(j)

map(bin,bytearray(ufa))

    


