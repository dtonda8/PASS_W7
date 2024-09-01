from typing import List
from data_structures.linked_list import LinkedList
from data_structures.array_sorted_list import ArraySortedList
from data_structures.referential_array import ArrayR

def LLtoList(ll: LinkedList):
    out = []
    for i in range(len(ll)):
        out.append(ll[i])
    return out

def SLtoList(sl: ArraySortedList):
    out = []
    for i in range(len(sl)):
        out.append(sl[i].value)
    return out

def AR(lst: List):
    out = ArrayR(len(lst))
    for i in range(len(lst)):
        out[i] = lst[i]
    return out

def SL(lst: List):
    out = ArraySortedList(len(lst))
    for i in range(len(lst)):
        out.add(lst[i])
    return out
