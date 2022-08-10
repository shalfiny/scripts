#!/usr/bin/env python

import sys, json

def rec_print(spans, node_id, l = 0):
    s = spans[node_id]
    print("{}{}sec {}: {} [{}]".format(' ' * l, s['duration'], s['name'], s['resource'][:30], node_id))
    for c in s['children_ids']:
        rec_print(spans, c, l + 1)


def parse(filename, root_id):
    with open(filename) as f: 
        spans = json.load(f)
    rec_print(spans, root_id)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: X </api/v1/trace/ output file location> <root_id>")
        sys.exit(1)

    parse(sys.argv[1], sys.argv[2])

