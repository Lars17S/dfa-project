states=[]
symbols=[]
initialState=''
finalStates=[]
evaluations=[]
index=0

f = open("test1.txt", "r")
lines=f.readlines()
states=lines[0].split(",")
states[len(states)-1]=states[len(states)-1].strip()
symbols=lines[1].split(",")
symbols[len(symbols)-1]=symbols[len(symbols)-1].strip()
initialState=lines[2]
initialState=initialState.rstrip()
finalStates=lines[3].split(",")
finalStates[len(finalStates)-1]=finalStates[len(finalStates)-1].strip()


dicc={}

for x in range(4,len(lines)):
    evaluations.append(lines[x].split("=>"))
    evaluations[-1][1]=evaluations[-1][1].strip()
    evaluations[-1][0]=evaluations[-1][0].replace(",","")


def rec_path(state, str_rec):
    print("current state: ", state, " currentr str: ", str_rec)
    if len(str_rec) == 0:
        return state in finalStates

    key = state + str_rec[len(str_rec) - 1]
    print("key: ", key)
    if key in dicc.keys():
        return rec_path(dicc[key], str_rec[:-1])
    return False
    
def check_dfa(str_val):
    return rec_path(initialState, str_val)

dicc=dict(evaluations)


#print(dicc)
print(evaluations)
print(dicc)
print(finalStates)
print(check_dfa('aba'))
#print(states,symbols,initialState,finalStates)
#print(f.read())

