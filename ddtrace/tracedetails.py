#!/usr/bin/env python

import sys, json

def pretty_print(filename, node_id):
    with open(filename) as f: 
        spans = json.load(f)
    print(json.dumps(spans[node_id], indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: X </api/v1/trace/ output file location> <node_id>")
        sys.exit(1)

    pretty_print(sys.argv[1], sys.argv[2])

