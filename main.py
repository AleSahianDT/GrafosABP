import networkx as nx
import matplotlib.pyplot as plt

# Definir nombres de las ciudades
cities = ["Tulcán", "Ibarra", "Quito", "Latacunga", "Ambato", "Guaranda", "Riobamba", "Azogues", "Cuenca", "Esmeraldas",
          "Portoviejo", "Manta", "S. Domingo", "Guayaquil", "Salinas", "Machala"]

# Matriz de distancias
distances = [
    [0, 1263, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1263, 0, 1133, 0, 0, 0, 0, 0, 0, 296, 0, 0, 0, 0, 0, 0],
    [0, 1133, 0, 1081, 0, 0, 0, 0, 0, 255, 0, 0, 1529, 0, 0, 0],
    [0, 0, 1081, 0, 425, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 425, 0, 999, 622, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 999, 0, 599, 0, 0, 0, 0, 0, 0, 1728, 0, 0],
    [0, 0, 0, 0, 622, 599, 0, 2421, 0, 0, 0, 0, 0, 285, 0, 0],
    [0, 0, 0, 0, 0, 0, 2421, 0, 316, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 316, 0, 0, 0, 0, 0, 196, 0, 2309],
    [0, 296, 255, 0, 0, 0, 0, 0, 0, 0, 0, 3577, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3757, 38, 0, 2443, 1981, 3245, 0],
    [0, 0, 1529, 0, 0, 0, 0, 0, 0, 0, 0, 2443, 0, 2823, 0, 0],
    [0, 0, 0, 0, 0, 1728, 285, 0, 196, 0, 0, 1987, 2823, 0, 1294, 1818],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3245, 0, 1294, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2309, 0, 0, 0, 0, 1818, 0, 0]
]

# Crear el grafo de distancias
distance_graph = nx.Graph()

# Añadir nodos y aristas al grafo
for i, city in enumerate(cities):
    distance_graph.add_node(city)
    for j, distance in enumerate(distances[i]):
        if distance != 0:
            distance_graph.add_edge(city, cities[j], weight=distance)

# Matriz de dificultad del terreno
difficulties = [
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
    [0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 3, 2, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 3, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 3, 3, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0]
]

# Crear el grafo de dificultad del terreno
difficulty_graph = nx.Graph()

# Añadir nodos y aristas al grafo
for i, city in enumerate(cities):
    difficulty_graph.add_node(city)
    for j, difficulty in enumerate(difficulties[i]):
        if difficulty != 0:
            difficulty_graph.add_edge(city, cities[j], weight=difficulty)

# Posiciones de los nodos
pos = nx.spring_layout(distance_graph, seed=42)

# Graficar el grafo de distancias
plt.figure(figsize=(14, 10))
nx.draw(distance_graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
distance_weights = nx.get_edge_attributes(distance_graph, 'weight')
nx.draw_networkx_edge_labels(distance_graph, pos, edge_labels=distance_weights, font_color='red')
plt.title("Grafo de Distancias entre Ciudades")
plt.show()

# Graficar el grafo de dificultad del terreno
plt.figure(figsize=(14, 10))
nx.draw(difficulty_graph, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
difficulty_weights = nx.get_edge_attributes(difficulty_graph, 'weight')
nx.draw_networkx_edge_labels(difficulty_graph, pos, edge_labels=difficulty_weights, font_color='blue')
plt.title("Grafo de Dificultad del Terreno entre Ciudades")
plt.show()
