'''
 This script converts the UTCS-feed-id-graph.json file to igraph 
'''

'''
    Command needed for graph
    g.add_vertex('id_number')
    id_number in g.vs["name"]    
    g["id1","id2"] = 1
    g.vs[0]     
    list(zip(g.vs['name'],g.pagerank()))
'''

from igraph import *
from pprint import pprint as pp
import json
g = Graph(directed=True)

with open('graph.json','r') as input:
    utcs_graph = json.load(input)

def convert(utcs_graph):
    # First, add a bunch of vertex from the keyset of utcs_graph
    g.add_vertices(list(utcs_graph.keys()))
    for key in utcs_graph:
        tagged_list = utcs_graph[key]
        for eachTag in tagged_list:
            tagged_user_id = eachTag[0]
            # If the tagged person isn't a vertex, then add it as a new vertex
            if eachTag not in g.vs['name']:
                g.add_vertex(tagged_user_id)
            # Connect the edge between them
            g[key,tagged_user_id] = 1
    
    result = sorted(list(zip(g.vs['name'],g.pagerank())),key=lambda node: node[1],reverse=True)

    for user_id, rank_score in result:
        # Only display purpose of the user id for privacy purpose
        pp(str(user_id) + " " + str(round(rank_score,6)))
    
convert(utcs_graph)