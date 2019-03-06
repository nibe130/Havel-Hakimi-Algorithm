
import matplotlib.pyplot as plt
from networkx import nx

z = [98, 95, 95, 94, 92, 89, 89, 89, 87, 87, 86, 85, 85, 84, 83, 81, 80, 79, 77, 75, 71, 70, 70, 70, 69, 68, 68, 67, 65, 64, 63, 62, 61, 59, 58, 55, 54, 54, 53, 53, 53, 53, 51, 49, 47, 46, 45, 45, 45, 43, 42, 42, 41, 39, 38, 38, 37, 36, 35, 35, 35, 35, 35, 34, 33, 30, 30, 29, 28, 28, 27, 25, 23, 22, 22, 21, 19, 19, 19, 18, 17, 15, 15, 15, 13, 13, 12, 12, 12, 11, 11, 10, 10, 5, 5, 4, 4, 2, 1, 1]

print(nx.is_graphical(z))

print("Configuration model")
G = nx.configuration_model(z)  # configuration model
print(G)
degree_sequence = [d for n, d in G.degree()]  # degree sequence
print("Degree sequence %s" % degree_sequence)
print("Degree histogram")
hist = {}
for d in degree_sequence:
    if d in hist:
        hist[d] += 1
    else:
        hist[d] = 1
print("degree #nodes")
for d in hist:
    print('%d %d' % (d, hist[d]))

nx.draw(G)
plt.show()