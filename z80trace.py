#!/usr/bin/python3

import sys

class Node:
    next_id = 0

    def __init__(self, pc):
        self.id = Node.next_id
        Node.next_id = Node.next_id + 1
        self.pc = pc
        self.next = []
        self.prev = []
        self.valid = True

nodes = {}
last_node = None
node_before_interrupt = None
in_interrupt = False
just_entered_interrupt = None
interrupt_call_level = None

with open(sys.argv[1]) as f:
    for line in f:
        pc = line.rstrip()

        if pc == "Interrupt":
            in_interrupt = True
            just_entered_interrupt = True
            interrupt_call_level = 1
        elif pc == "CALL":
            if in_interrupt:
                interrupt_call_level = interrupt_call_level + 1
        elif pc == "RET":
            if in_interrupt:
                interrupt_call_level = interrupt_call_level - 1
                if interrupt_call_level == 0:
                    last_node = node_before_interrupt
                    in_interrupt = False
        else:
            if pc in nodes:
                node = nodes[pc]
            else:
                node = Node(pc)
                nodes[pc] = node

            if just_entered_interrupt:
                node_before_interrupt = last_node
                just_entered_interrupt = False
            elif last_node is not None:
                if node not in last_node.next:
                    last_node.next.append(node)
                    node.prev.append(last_node)

            last_node = node

potential_merges = list(nodes.values())
while len(potential_merges) > 0:
    node = potential_merges[0]
    remain = False

    if node.valid:
        if len(node.next) == 1:
            next_node = node.next[0]
            if len(next_node.prev) == 1:
                node.pc = node.pc + " " + next_node.pc
                node.next = next_node.next
                next_node.valid = False
                remain = True

    if not remain:
        potential_merges.pop(0)

print("digraph z80 {")

for node in nodes.values():
    if node.valid:
        print("n" + str(node.id) + " [ label = \"" + node.pc + "\" ]")
        for next_node in node.next:
            print("n" + str(node.id) + " -> n" + str(next_node.id) + ";")

print("}")
