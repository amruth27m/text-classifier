import os
import json

file = open('offer_data.json')
data = json.load(file)

#print(len(data))
balaji = []
amruth  = []
adil = []

i = 0
for sms in data:
    if(i%3 == 0):
        balaji.append(sms)
    elif(i%3 == 1):
        amruth.append(sms)
    else:
        adil.append(sms)
    i += 1
    
#print(len(balaji))
#print(len(amruth))
#print(len(adil))

outa = open("balaji/data.json", "w")
outb = open("amruth/data.json", "w")
outc = open("adil/data.json", "w")

json.dump(balaji, outa)
json.dump(amruth, outb)
json.dump(adil, outc)