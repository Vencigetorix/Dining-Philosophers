import threading 
from filosofo import Filosofo
lock = threading.RLock()
Filosofos = [Filosofo(lock) for i in range(5)]
i=0
thrds=[]
states = []


def showStates():
    j = 0
    for fil in Filosofos:
        states[j] = fil.status
    print(states)


for fil in Filosofos:
    if (i == 4):
        fil.setRight(Filosofos[0])
    else:
        fil.setRight(Filosofos[i+1])
    fil.setLeft(Filosofos[i-1])
    i += 1
i = 0

for fil in Filosofos:
    thrds[i] = threading.Thread(fil.run())
    thrds[i].start()
    i+=1
    showStates()