# -*- coding: utf-8 -*-

ASSIGNMENT 9


import networkx as nx
import matplotlib.pyplot as plt

simple_graph = nx.DiGraph()
reified_graph = nx.DiGraph()


1. Jerry is a cat.
2. Jerry was sitting on the sofa.
3. Jerry is owned by Tom.
4. Tom called Jerry.
5. Jerry walked from the sofa to Tom.
6. Tom gave some milk to Jerry.
7. Jerry drank the milk. 

simple_relationships = [
    ("Jerry", "cat", "is a"),
    ("Jerry", "sofa", "was sitting on"),
    ("Jerry", "Tom", "is owned by"),
    ("Tom", "Jerry", "called"),
    ("Jerry", "sofa", "walked from"),
    ("Jerry", "Tom", "walked to"),
    ("Tom", "milk", "gave some to"),
    ("Jerry", "milk", "drank")
]

for source, target, relation in simple_relationships:
    simple_graph.add_edge(source, target, label=relation)

reified_relationships = [
    ("Jerry", "cat", "is a"),
    ("Jerry", "sofa", "was sitting on"),
    ("Jerry", "Tom", "is owned by"),
    ("Tom", "called_Jerry", "called"),  # Reified: "called_Jerry" as an event node
    ("called_Jerry", "Jerry", "affected"),
    ("Jerry", "walked_to_Tom", "initiated"),  # Reified: "walked_to_Tom" as an event node
    ("walked_to_Tom", "sofa", "from"),
    ("walked_to_Tom", "Tom", "to"),
    ("Tom", "gave_milk", "gave"),  # Reified: "gave_milk" as an event node
    ("gave_milk", "milk", "object"),
    ("gave_milk", "Jerry", "recipient"),
    ("Jerry", "drank_milk", "initiated"),  # Reified: "drank_milk" as an event node
    ("drank_milk", "milk", "object")
]

for source, target, relation in reified_relationships:
    reified_graph.add_edge(source, target, label=relation)

def draw_graph(graph, title):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, font_weight="bold", arrows=True)
    edge_labels = {(source, target): label for source, target, label in graph.edges(data="label")}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red", font_size=8)
    plt.title(title)
    plt.show()

draw_graph(simple_graph, "Simple Semantic Net")

draw_graph(reified_graph, "Reified Semantic Net")
'''
import networkx as nx
import matplotlib.pyplot as plt
G1 = nx.DiGraph()
G2 = nx.DiGraph() 
G1.add_edge("Jerry", "Cat", relation="is a")
G1.add_edge("Jerry", "Sofa", relation="is on")
G1.add_edge("Jerry", "Tom", relation="owned by")
G1.add_edge("Tom", "Jerry", relation="related to")
G1.add_edge("Milk", "Jerry", relation="related to")
G2.add_edge("Jerry", "Cat", relation="is a")
G2.add_node("sitting")
G2.add_edge("Jerry", "sitting", relation="actor")
G2.add_edge("sitting", "Sofa", relation="on")
G2.add_node("owned")
G2.add_edge("Tom", "owned", relation="owner")
G2.add_edge("owned", "Jerry", relation="entity owned")
G2.add_node("called")
G2.add_edge("Tom", "called", relation="caller")
G2.add_edge("called", "Jerry", relation="callee")
G2.add_node("walked")
G2.add_edge("Jerry", "walked", relation="mover")
G2.add_edge("walked", "Sofa", relation="from")
G2.add_edge("walked", "Tom", relation="to")
G2.add_node("gave")
G2.add_edge("Tom", "gave", relation="giver")
G2.add_edge("gave", "Milk", relation="item given")
G2.add_edge("gave", "Jerry", relation="receiver")
G2.add_node("drank")
G2.add_edge("Jerry", "drank", relation="drinker")
G2.add_edge("drank", "Milk", relation="thing consumed")
def draw_graph(G, title):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    plt.title(title)
    plt.show()
draw_graph(G1, "Graph 1: Simple Semantic Net (Ignoring Verbs)")
draw_graph(G2, "Graph 2: Reified Semantic Net (With Verbs)")