
import matplotlib.pyplot as plt
from networkx import nx
import random
import time

def havelHakimi(sequence):

    if all(isinstance(degrees, int) for degrees in sequence):
       degree_sequence = list(sequence)


    else:
        return False
    if len(degree_sequence) == 0:
        print("The sequence is empty")
        return True

    if sum(degree_sequence) % 2:
        print("No graph exists with this degree sequence.The sum of all the elements in the degree sequence is not even.")
        return False
    if min(degree_sequence) < 0:
        print("No graph exists with this degree sequence.Degree sequence should not have negative numbers!")
        return False  # negative degree

    while degree_sequence:
        degree_sequence.sort()
        degree_sequence.reverse()
        print("Intermediate Sequence " + str(degree_sequence))
        for item in degree_sequence:
            if item < 0:
                print("No graph exists with this degree sequence.")
                return False
        d = degree_sequence.pop(0)
        if d == 0:
            print("There exists a graph G with this degree sequence")
            return True
        if d > len(degree_sequence):
            print(str(d) + " dgree is too large for sequence!")
            return False
        for i in range(0, d):
            degree_sequence[i] -= 1
        print("Popped: " + str(d))
    return False




random_sequence=[]
n=random.randint(0,100)

print("the length of the degree sequence is {0}".format(n))
for x in range(n):
  random_sequence.append(random.randint(0,n-1 ))
print("the degree sequence is {0}".format(random_sequence))

start_time = time.time()

x=havelHakimi(random_sequence)
print("--- %s seconds ---" % (time.time() - start_time))


if x==True:
    G = nx.configuration_model(random_sequence)
    nx.draw(G)
    plt.show()