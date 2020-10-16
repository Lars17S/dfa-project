import numpy as np

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
# print(evaluations)
# print(dicc)
# print(finalStates)
# print(check_dfa('aba'))
# print(symbols)
#print(states,symbols,initialState,finalStates)
#print(f.read())

# Llenar el diccionario

def fill_keys():
    for state in states:
        for lang in symbols:
            key = state + lang
            if key not in dicc.keys():
                dicc[key] = 'X'
fill_keys()


def find_match():

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

    for line in table:
        transitions = line[1]
        list_eq = []
        for line_it in table:
            if line_it[1] == transitions:
                # print(line_it[0], " is equivalent to ", line[0])
                list_eq.append(line_it[0])
        if len(list_eq) > 1:
            if list_eq not in equivalents:
                equivalents.append(list_eq)

    print("EQUIVALENTS")
    print(equivalents)
    print()

    # q1: qA, q3: qA
    # q2: qB, q4: qB

    temp_dict = {}

    for index in range(0, len(equivalents)):
        alias = "Q-" + str(index)
        for item in equivalents[index]:
            temp_dict[item] = alias

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
    
    print("ORIGINAL: ", dicc)
    print("NEW: ", new_dict)
    # dict.get(key)
    # dict[key] 
    

    

    
find_match()

# Extraer el estado 
# Buscar entradas "q0" + "a", "q0" + "b" ... hasta todos los caracteres en el lenguaje
# Si no existe la entrada, llenar el key con un string vacio ""

# Iterar para cada uno de los estados
    # Extraer los estados para cada valor en la transición
    # Buscar todos aquellos estados que tienen los mismos valores de transición 
    # Si son iguales, añadir en lista de equivalencia

# Remplazar todos los estados equivalentes por un nuevo key


