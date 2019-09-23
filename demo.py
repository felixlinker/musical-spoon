from core import *

print("Willkommen! Dies stellt eine Demo der Hauptfunktionen des musical-spoon-packages dar.\n Zunaechst wird aus drei Knoten und drei Kanten ein einfaches Graph-Objekt erstellt und anschliessend graphisch dargestellt.")
v1 = Vertex(1, 'A')
v2 = Vertex(2, 'B')
v3 = Vertex(3, 'C')

e1 = Edge(v1, v2)
e2 = Edge(v2, v3)
e3 = Edge(v3, v1)

g1 = Graph([v1,v2,v3], [e1,e2,e3])
show_graph(g1)

print("Nun werden zwei Graphen aus Dateien eingelesen und anschliessend angezeigt.\n Der erste Graph wird aus einer .graph-Datei eingelesen, welche dem in der Seminargruppe beschlossenen Format entspricht.\n Der zweite Graph wird aus einer JSON-Datei eingelesen, welche die Struktur von Aspirin aus der PubChem-DB gespeichert hat.")
g2 = parse("./Graphen/graph1.graph")
show_graph(g2)

g3 = parse_chem("./Graphen/test.json")
show_graph(g3)

print("Nun werden die beiden Graphen g1 und g2 mittels dem Bron-Kerbush-Algorithmus verglichen und die maximale Clique angegeben und als Graph-Objekt in g4 gespeichert.")
g4 = find_mcis(g1, g2)
show_graph(g4)

print("Jetzt werden mehrere zufaellige Graphen erstellt. Fuer genaue Parameterbeschreibung siehe Ausarbeitung Abschnitt 3.6\n g5 ist ein zufaelliger Graph mit 8 Knoten\n g6 ist ein triangulaerer Graph\n g7 ist ein vollständiger Graph" )
g5 = random_graph(8,8)
g6 = random_triangular_graph(10,0)
g7 = complete_graph(7)
show_graph_comparable(g5, g6, g7)

print("als naechstes wird die Funktion cut_edges auf den Graph g7 angewendet und in g8 gespeichert(Loeschwahrscheinlichkeit der Kanten: 0.5)")
g8 = cut_edges(g7, 0.5)
show_graph(g8)

print("Nun werden zwei Graphen aus Dateien eingelesen und vergleichbar dargestellt. \nDarauf folgend wird der Cordella-Algorithmus auf diese Graphen-Objekte angewendet. \n Die Ausgabe ist eine Liste von gepaarten Knoten")
g9 = parse("./Graphen/scriptG1.graph")
g10 = parse("./Graphen/cordellaTest1.graph")
show_two_graphs(g9,g10)
Cordella(g9, g10)

print("Als nächstes wird die Funktion zum multiplen Alignment mittels eines simultan erstellten Guide-Trees gezeigt. \nDie fuenf Graphen g1,g2,g4,g11 und g12 dienen als Input.\n Der erstellte Guide-Tree wird im Newick-Format in der Konsole angegeben, sowie als Graph visualisiert")
g11 = random_chess_graph(4, 0)
g12 = random_triangular_graph(6)
show_graph_comparable(g1, g2, g4)
show_two_graphs(g11,g12)

g1.name = "g1"
g2.name = "g2"
g4.name = "g4"
g11.name = "g11"
g12.name = "g12"
t = create_tree([g1, g2, g4, g11, g12])
show_graph(t.result)
show_graph(t.tree_structure)

print("Nachfolgend wird an einem Beispiel die Regulationsmöglichkeit gezeigt, bei der Suche nach Most-Common-Induced-Subgraphes die Labels der Knoten mit einzubeziehe.\n Die erste Variante zeigt die Suche ohne Labelvergleich. \n Die zweite Variante ist mit dem Labelvergleich.")
g15 = parse("./Graphen/label1.graph")
g16 = parse("./Graphen/label2.graph")
g17 = find_mcis_without_prompt(g15,  g16, checklabels = False)
show_graph_comparable(g15, g16, g17)
g18 = find_mcis_without_prompt(g15,  g16, checklabels = True)
show_graph_comparable(g15, g16, g18)

print("Abschließend wird demonstriert, dass im BK-Algorithmus eine Anker-Struktur eingebaut werden kann.\n Die erste Variante zeigt die Ausgabe ohne einen Anker, die zweite die Ausgabe mit einer Ankerstruktur.\n Dieser Teil des Programms dauert ein wenig.")
# Diese MCIS Suche kann ein paar Minuten dauern, ist jedoch ein gute Beispiel für einen sinnvollen Ankereinsatz
# ------------------------------------------------
g13 = parse("./Graphen/scriptG1.graph")
g14 = parse("./Graphen/scriptG2.graph")
mcis = find_mcis_without_prompt(g13, g14)
show_graph_comparable(g13, g14, mcis)
anker = ["5;9", "7;3", "9;6", "10;7", "6;2", "8;4"]
mcis_ankered = find_ankered_mcis(g13, g14, anker)
show_graph_comparable(g13, g14, mcis_ankered)
# -----------------------------------------------