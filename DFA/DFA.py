import numpy as np

states=[]
symbols=[]
initialState=''
finalStates=[]
evaluations=[]
index=0
f=0
globalIndex=0
print("WHAT FILE DO YOU WANT TO OPEN? (1 FOR test1.txt) (2 FOR test2.txt) ")
opcion= int(input())

#We open the selected file
if opcion==1:
    f = open("test1.txt", "r")
elif opcion==2:
    f = open("test2.txt", "r")

#These are the variables we used to read the input
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
first=True
equivalent=True

#We get the evaluations with a split from the following lines
for x in range(4,len(lines)):
    evaluations.append(lines[x].split("=>"))
    evaluations[-1][1]=evaluations[-1][1].strip()
    evaluations[-1][0]=evaluations[-1][0].replace(",","")

#We add them yo a dictionary
dicc=dict(evaluations)

#Recursive function to traverse the graph of the states
def rec_path(state, str_rec):

    print("CURRENT STATE: ", state, " CURRENT STRING: ", str_rec)
    if len(str_rec) == 0:       #This is the base case of the recursive function
        return state in finalStates

    key = state + str_rec[len(str_rec) - 1]
    print("KEY: ", key)
    if key in dicc.keys():                  #If the current character is in the dictionary, then we call the recursive function again
        return rec_path(dicc[key], str_rec[:-1])
    return False

#Function to call the recursive functino rec_path
def check_dfa(str_val):
    return rec_path(initialState, str_val)

#Function to fill the table with values that are empty in the dictionary but exist in the states so we can compare each one
def fill_keys():
    global first
    if(first==True):        #We verify that it is just called one time with a bool
        for state in states:
            for lang in symbols:
                key = state + lang
                if key not in dicc.keys():
                    dicc[key] = 'X'
        first=False

#This is the function to find the equivalents between the states
def find_match(noEquivalents):
    global globalIndex,initialState

    table = []
    for state in states: # q0       #We build the transition table
        row_state = []
        row_state.append(state)
        row_state.append([])
        for lang in symbols:
            key = state + lang
            row_state[1].append(dicc[key])
        table.append(row_state)

    equivalents = []

    for line in table:              #We check which states are equivalent according to the table above
        transitions = line[1]
        list_eq = []
        for line_it in table:
            if line_it[1] == transitions:
                list_eq.append(line_it[0])
        if len(list_eq) > 1:
            if list_eq not in equivalents:
                equivalents.append(list_eq)

    print("EQUIVALENTS", equivalents)
    if not equivalents:             #We check if the equivalents table is empty, means that it can't be minimized
        noEquivalents=False

    print("------------------------------------------------------------------")

    temp_dict = {}
    if(globalIndex==0):             #We build the temporal dictionary with the equivalences so we can change the names
        for index in range(0, len(equivalents)):
            alias = "Q-" + str(index)

            for item in equivalents[index]:
                temp_dict[item] = alias
    elif globalIndex!=0:
        for index in range(0, len(equivalents)):
            alias = "Q-" + str(index+globalIndex+1)

            for item in equivalents[index]:
                temp_dict[item] = alias
    globalIndex=globalIndex+1

    new_dict = {}

    for key in dicc.keys():         #We replace the states with the equivalent ones in the temporal dictionary
        state = key[:-1]
        if state in temp_dict.keys():
            new_key = temp_dict[state] + key[len(key) - 1]
        else: new_key = key
        new_dict[new_key] = dicc[key]

    for key in new_dict.keys():
        if new_dict[key] in temp_dict.keys():
            new_dict[key] = temp_dict[new_dict[key]]


    for key in temp_dict.keys():        #We update the states, final states and initial states for further iterations
        if key in states:
            states.remove(key)
        if key in finalStates:
            finalStates.remove(key)
            if temp_dict[key] not in finalStates:
                finalStates.append(temp_dict[key])
        if key == initialState:
            initialState=temp_dict[key]
        if temp_dict[key] not in states:
            states.append(temp_dict[key])


    if noEquivalents==True:             #We print the new information
        print("NEW INITIAL STATE",initialState, "\n")
        print("NEW FINAL STATES: ", finalStates,"\n")
        print("STATES: ",states, "\n")
        print("TEMPORAL DICTIONARY: ",temp_dict, "\n")
        print("ORIGINAL DICTIONARY: ", dicc, "\n")
        print("MINIMIZED DICTIONARY: ", new_dict,"\n")
        print("EQUIVALENCE TABLE: ")
        table_f = []
        for state in states:
            row_state = []
            row_state.append(state)
            row_state.append([])
            for lang in symbols:
                key = state + lang
                row_state[1].append(new_dict[key])
            table_f.append(row_state)
        for item in table_f:
            print(item)
        print("-----------------------------------------------------------------------------------------------")
    return new_dict,noEquivalents


print("THIS ARE YOUR STATES: ",states)
opcion2=0

while(opcion2!=3):
    print("WHAT DO YOU WANT TO DO? (1 FOR VALIDATING A STRING) (2 FOR MINIMIZE) (3 TO END)")
    opcion2= int(input())
    if opcion2==1:
        print("GIVE THE STRING TO VALIDATE")
        print("THIS IS THE LANGUAGE: ",symbols)
        opcion3=str(input())
        if check_dfa(str(opcion3)):
            print("TRUE: The string is validated because ends in a final state")
        else:
            print("FALSE: The string is not validated because it does not end in final state")

    elif opcion2==2:
        print("---------------------------------------------------------")
        fill_keys()

        if equivalent:            #We loop the minized function until there are no equivalents
            dicc,equivalent=find_match(equivalent)
        else:
            print("THERE ARE NO EQUIVALENTS OR CANNOT BE MINIMIZED ANYMORE")
        print("---------------------------------------------------------")

