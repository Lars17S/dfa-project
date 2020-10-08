f = open("test1.txt", "r")
lines=f.readlines()
states=[]
symbols=[]
initialState=""
finalStates=[]
evaluations=[]
index=0

states=lines[0].split(",")
states[len(states)-1]=states[len(states)-1].strip()
symbols=lines[1].split(",")
symbols[len(symbols)-1]=symbols[len(symbols)-1].strip()
initialState=lines[2]
finalStates=lines[3].split(",")
finalStates[len(finalStates)-1]=finalStates[len(finalStates)-1].strip()


dicc={}

for x in range(4,len(lines)):
    evaluations.append(lines[x].split("=>"))
    evaluations[-1][1]=evaluations[-1][1].strip()
    evaluations[-1][0]=evaluations[-1][0].replace(",","")


dicc=dict(evaluations)


#print(dicc)
print(evaluations)
print(dicc)
#print(states,symbols,initialState,finalStates)
#print(f.read())

