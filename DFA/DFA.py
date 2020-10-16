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

if opcion==1:
    f = open("test1.txt", "r")
elif opcion==2:
    f = open("test2.txt", "r")


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


for x in range(4,len(lines)):
    evaluations.append(lines[x].split("=>"))
    evaluations[-1][1]=evaluations[-1][1].strip()
    evaluations[-1][0]=evaluations[-1][0].replace(",","")

dicc=dict(evaluations)
def rec_path(state, str_rec):

    print("CURRENT STATE: ", state, " CURRENT STRING: ", str_rec)
    if len(str_rec) == 0:
        return state in finalStates

    key = state + str_rec[len(str_rec) - 1]
    print("KEY: ", key)
    if key in dicc.keys():
        return rec_path(dicc[key], str_rec[:-1])
    return False
    
def check_dfa(str_val):
    return rec_path(initialState, str_val)
    print(str_val)





def fill_keys():
    global first
    if(first==True):
        for state in states:
            for lang in symbols:
                key = state + lang
                if key not in dicc.keys():
                    dicc[key] = 'X'
        first=False


def find_match(noEquivalents):
    global globalIndex,initialState



    table = []
    for state in states: # q0
        row_state = []
        row_state.append(state)
        row_state.append([])
        for lang in symbols:
            key = state + lang
            row_state[1].append(dicc[key])
        table.append(row_state)

    equivalents = []
    print(table)
    for line in table:
        transitions = line[1]
        list_eq = []
        for line_it in table:
            if line_it[1] == transitions:
                list_eq.append(line_it[0])
        if len(list_eq) > 1:
            if list_eq not in equivalents:
                equivalents.append(list_eq)

    print("EQUIVALENTS", equivalents)
    if not equivalents:
        print("THERE ARE NO EQUIVALENTS")
        noEquivalents=False

    print("------------------------------------------------------------------")

    # q1: qA, q3: qA
    # q2: qB, q4: qB

    temp_dict = {}
    if(globalIndex==0):
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

    for key in dicc.keys():
        state = key[:-1]
        if state in temp_dict.keys():
            new_key = temp_dict[state] + key[len(key) - 1]
        else: new_key = key
        new_dict[new_key] = dicc[key]

    for key in new_dict.keys():

        if new_dict[key] in temp_dict.keys():
            new_dict[key] = temp_dict[new_dict[key]]

    for key in temp_dict.keys():
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
    if noEquivalents==True:
        print("NEW INITIAL STATE",initialState, "\n")
        print("NEW FINAL STATES: ", finalStates,"\n")
        print("STATES: ",states, "\n")
        print("TEMPORAL DICTIONARY: ",temp_dict, "\n")
        print("ORIGINAL DICTIONARY: ", dicc, "\n")
        print("NEW DICTIONARY: ", new_dict,"\n")
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


        print(check_dfa(str(opcion3)))
    elif opcion2==2:
        print("---------------------------------------------------------")
        fill_keys()

        while(equivalent==True):
            dicc,equivalent=find_match(equivalent)
        print("---------------------------------------------------------")


# Extraer el estado 
# Buscar entradas "q0" + "a", "q0" + "b" ... hasta todos los caracteres en el lenguaje
# Si no existe la entrada, llenar el key con un string vacio ""

# Iterar para cada uno de los estados
    # Extraer los estados para cada valor en la transición
    # Buscar todos aquellos estados que tienen los mismos valores de transición 
    # Si son iguales, añadir en lista de equivalencia

# Remplazar todos los estados equivalentes por un nuevo key

# Llenar el diccionario
