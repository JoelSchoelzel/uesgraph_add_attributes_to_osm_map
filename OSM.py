import osmium as osm
import pandas as pd
#import json
import uesgraphs as ug
from shapely.geometry import Point

#class OSMHandler(osm.SimpleHandler):
#    def __init__(self):
#        osm.SimpleHandler.__init__(self)
#        self.osm_data = []
#
#    def node(self, n):
#        self.osm_data.append(["node",
#                                  n.id,
#                                  n.version,
#                                  n.visible,
#                                  pd.Timestamp(n.timestamp),
#                                  n.uid,
#                                  n.changeset,
#                                  n.user,
#                                  n.location,
#                                  len(n.tags)])
#
#    def way(self, w):
#        self.osm_data.append(["way",
#                              w.id,
#                              w.version,
#                              w.visible,
#                              pd.Timestamp(w.timestamp),
#                              w.uid,
#                              w.changeset,
#                              w.user,
#                              #w.location,
#                              len(w.tags)])
#
#    def relation(self, r):
#        self.osm_data.append(["relation",
#                              r.id,
#                              r.version,
#                              r.visible,
#                              pd.Timestamp(r.timestamp),
#                              r.uid,
#                              r.changeset,
#                              r.user,
#                             # r.location,
#                              len(r.tags)])
#
#if __name__ == '__main__':
#    h = OSMHandler()
#    h.apply_file("EON.osm")
#
#data_colnames = ['type', 'id', 'version', 'visible', 'ts', 'uid', 'chgset', 'user', 'location', 'ntags']
#elements = pd.DataFrame(h.osm_data, columns=data_colnames)
#elements = elements.sort_values(by=['type', 'id', 'ts'])
#elements.to_csv("nodes.csv", date_format='%Y-%m-%d %H:%M:%S', sep=';')
#
#elements['location'] = elements['location'].astype(str)
#elements['Längengrad'] = elements['location'].str[0:8]
#elements['Breitengrad'] = elements['location'].str[9:18]
#
#
#f_1 = elements.get('Breitengrad')
#f_1 = pd.Series(f_1).values
#g_1 = pd.to_numeric(f_1, errors='coerce')
#
#f_2 = elements.get('Längengrad')
#f_2 = pd.Series(f_2).values
#g_2 = pd.to_numeric(f_2, errors='coerce')
#
#demand = graph.add_building(
#    name='Building 1',
#    position=Point(g_2[0], g_1[0]),
#)
#graph.nodes[demand]['heat_load_kW'] = 200
#print(elements)

graph = ug.UESGraph()
ug.uesgraph.UESGraph.from_osm(graph, osm_file='EON.osm')   #einlesen der OSM-Datei als graph

vis = ug.Visuals(graph)
vis.show_network(
    show_plot=True,
    scaling_factor=30,
    )

#
x = ug.uesgraph.UESGraph.number_of_nodes(graph, node_type='building')

d = graph.nodelist_building
j = graph.nodelist_building[0]                 #
graph.nodes[j]['heat_load_kW'] = 200           #neues Attribut wird Knoten hinzugefügt
k = graph.nodes[graph.nodelist_building[0]]    #alle Attribute eines Knotens werden ausgegeben

e = graph.positions
i = graph.nodes_by_name
#graph.nodes[E.ON Energy Research Center]['heat_load_kW_1'] = 300
k = graph.nodes[graph.nodelist_building[0]]