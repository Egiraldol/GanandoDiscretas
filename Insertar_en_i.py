class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertar(head: Node, valor, posI):
    if posI == 1:
        cambio = insertarAux(head, valor)
        return cambio
    else:
        return insertar(head.next, valor, posI-1)

def insertarAux(head: Node, valor: int) -> Node:
    NodoCabeza = Node(valor)
    NodoCabeza.next = head
    return NodoCabeza
