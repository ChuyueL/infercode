import argparse
from os.path import exists
import re
from os import path
from tree_sitter import Language, Parser
from pathlib import Path

# def print_tree_line(id, data, root_node, reports, excluded_node_types):
#     node_id = id
#     node_type = root_node.type.lower()
#     node_label = data[root_node.start_byte:root_node.end_byte].lower()
#     has_child = len(root_node.children) > 0
#     depth = 1
#     s = "{}-{},".format(node_id, node_type)
#     if not has_child:
#         s = "{}-{}-{},".format(node_id, node_type, node_label.decode("utf-8"))
#     for child in root_node.children:
#         (id, child_depth, child_str) = print_tree_line(id + 1, data, child, reports, excluded_node_types)
#         depth = max(depth, child_depth+1)
#         s = "{}{}".format(s, child_str)
#     if str(node_type) not in excluded_node_types and len(str(node_type))>0:
#         reports[node_id] = "{}{}".format(s, depth)
#     # reports[node_id] = "{}{}".format(s, depth)

#     return (id, depth, s)

def print_tree_line(id, data, root_node, reports, excluded_node_types):
    node_id = id
    node_type = root_node.type
    has_child = len(root_node.children) > 0
    if not has_child:
        node_label = data[root_node.start_byte:root_node.end_byte]
    else:
        first_child = root_node.children[0]
        # first_child could be the same as last_child
        node_label = data[root_node.start_byte:first_child.start_byte] 
        next_sibbling = root_node.next_sibling
        if next_sibbling:
            node_label = node_label + data[root_node.end_byte:next_sibbling.start_byte] 
        node_label = node_label.strip()
    depth = 1
    if not node_label:
        s = "{}-{},".format(node_id, node_type)
    else:
        s = "{}-{}-{},".format(node_id, node_type, node_label.decode("utf-8"))
    for child in root_node.children:
        (id, child_depth, child_str) = print_tree_line(id + 1, data, child, reports, excluded_node_types)
        depth = max(depth, child_depth+1)
        s = "{}{}".format(s, child_str)
    if str(node_type) not in excluded_node_types and len(str(node_type))>0:
        reports[node_id] = "{}{}".format(s, depth)
    return (id, depth, s)


def print_subtree(data, root_node, reports, excluded_node_types):
    (id, depth, s) = print_tree_line(1, data, root_node, reports, excluded_node_types)

    return "{}{}".format(s, depth)

