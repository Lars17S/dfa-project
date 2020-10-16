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
print(evaluations)
print(dicc)
print(finalStates)
print(check_dfa('aba'))
print(symbols)
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
print(dicc)

def find_match():
    table = []
    for state in states: # q0
        row_state = []
        row_state.append(state)
        for lang in symbols:
            key = state + lang 
            row_state.append(dicc[key])
        table.append(row_state)

    for line in table:
        print(line, '\n')
    
    

    
find_match()

# Extraer el estado 
# Buscar entradas "q0" + "a", "q0" + "b" ... hasta todos los caracteres en el lenguaje
# Si no existe la entrada, llenar el key con un string vacio ""

# Iterar para cada uno de los estados
    # Extraer los estados para cada valor en la transición
    # Buscar todos aquellos estados que tienen los mismos valores de transición 
    # Si son iguales, añadir en lista de equivalencia

# Remplazar todos los estados equivalentes por un nuevo key


