import json 

#read from the input file 
k= "input.json"

#function to convert binary representations to set form 
def convbin(n):
    fostr="{:0"+str(n)+"b}"
    binstr=fostr.format(n)
    li=[]
    c=0
    for i in range(n-1,-1,-1):
        if binstr[i] == '1' :
            li.append(c)
        c+=1
    return li
    print (li)


#function to convert set representations to binary form 
def tobin(lis):
    n=0
    for i in lis :
        n+=2**i
    return n


#reading the input file 
with open (k,"r") as inputjson:
    data = json.load(inputjson)

stateset=[]
finalstates = []
n=data["states"]
letters=data["letters"]
tomake=[]
tomake1=[]

fostr="{:0"+str(n)+"b}"

curr=0
#creating the power set and iterating through it
for i in range (2**n):
    l=fostr.format(i)
    # converting the integer to set from and building the set of DFA states
    li=convbin(i)
    stateset.append(li)
    #iterating through each symbol of the input alphabet  
    for alpha in letters: 
        c=0
        tomake.append([li,alpha,[]]);
        tomake1.append([i,alpha,0]);
        for j in range (n-1,-1,-1) :
            # checking if a state of DFA should be  included in the final state set
            if c in data["final"] and l[j]=='1' and alpha == letters[0]:
                finalstates.append(convbin(i))
            if l[j] == '1':
                for k in data["t_func"]:
                    if k[0]==c and k[1]== alpha :
                        # taking union of the output of state-symbol combination from the NFA for each element in the current state of DFA
                        tomake[curr][2] = list(set(tomake[curr][2]) | set(k[2]))
                        tomake1[curr][2] = tomake1[curr][2] | tobin(k[2])
            c+=1
        curr+=1

#constructing the final output dictionary 
outputjs = {}
outputjs["states"]=stateset
outputjs["letters"]=letters
outputjs["t_func"]=tomake 
outputjs["start"] = data["start"]
outputjs["final"]=finalstates


#writing to the output file 
with open("output.json",'w') as outputfile :
    json.dump(outputjs,outputfile,indent=1)

