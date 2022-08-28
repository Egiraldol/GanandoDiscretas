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
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertar(head: Node, valor, posI):
    return posicionAux(head,valor,posI,1)
def posicionAux(head:Node,valor:int,i:int,j:int,aux=0)->Node:
    if head==None:
        newHead = Node(valor)
        newHead.next= None
        return newHead
    else:
        if j == i - 1:
            aux = head.next
            head.next = valor
        if j == i:
            head.val = valor
            head.next = aux
        else:
            return posicionAux(head.next,valor,i,j+1)
        return head

'''
