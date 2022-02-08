# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:28:50 2022

@author: Netanel Iyov
"""
import math


# defining a class node, when right and left sons are optional and defaulted to None.
class Node:
    def __init__(self,letter, freq,right=None, left=None):
        self.letter = letter
        self.freq = freq
        self.right = right
        self.left = left
       
def CreateNode(freq, right=None, left=None):
    return Node(None,freq,right,left)

def Swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return

def left(i):
    return i*2 + 1

def right(i):
    return (i+1)*2

def parent(i):
    if (i==0):
        return None
    if(i%2 == 0):
        return int(i/2 -1) 
    else:
        return int((i-1)/2)

# Min Heap implementation 
# Functions : Min-Heapify-Down, Min-Heapify-Up, Build-Min-Heap, Heap-Extract-Min, Heap-Insert

def MinHeapifyDown(A,i):
    n = len(A)
    r = right(i)
    l = left(i)
    smallest = i
    
    if(l<n and A[l].freq < A[i].freq):
        smallest = l
    if (r<n and A[r].freq < A[smallest].freq ):
        smallest = r
    if (smallest != i):
        Swap(A,i,smallest)
        MinHeapifyDown(A, smallest)
    return
    
def MinHeapifyUp(A,i):
    p = parent(i)
    if (i==0):
        return
    if( A[i].freq < A[p].freq ):
        Swap(A,i,p)
        MinHeapifyUp(A, p)
    return

def BuildMinHeap(A):
    n = len(A)
    for i in range((math.floor(n/2))-1,-1,-1):
        MinHeapifyDown(A,i)
    
    return
    
def HeapExtractMin(A):
    Min = A[0]
    Swap(A,0,len(A)-1)
    A.pop()
    MinHeapifyDown(A, 0)
    
    return Min

def MinHeapInsert(A,x):         # when x is a node structure in our implementation
    A.append(x)
    MinHeapifyUp(A, len(A)-1)
    return    


def Assigncode(node,code,CodeDict):           # Make a Code dictionary where the keys are the letters and the values are the code 
    if (node.left == None):
        CodeDict[node.letter] = code
        return
    else:
        Assigncode(node.left, code+"0", CodeDict)    # if the path to the node goes through left son of an ancestor then add '0'
        Assigncode(node.right, code+"1", CodeDict)   # same as above, but to the right add '1'

def Encode(s,CodeDict):                       # code given string with given Dictionary code
    code=""
    for char in s:
        code += CodeDict[char]
        
    return code
    
inp = input("Please enter a sting you want to encode : ")
arr = {i : inp.count(i) for i in set(inp)}
Table = []
for key in arr:
    Table.append(Node(key, arr[key]))

# set our table to be a min heap
BuildMinHeap(Table)

# Build the Huffman tree according to Huffman's algorithm
while (len(Table) > 1):                    
    Min1 = HeapExtractMin(Table)
    Min2 = HeapExtractMin(Table)
    MinHeapInsert(Table, CreateNode(Min1.freq+Min2.freq,Min1, Min2))
    
HuffmanTree = Table[0]
CodeDict = {}
Assigncode(HuffmanTree, "", CodeDict)
Encoded = Encode(inp,CodeDict)
print("The huffman code for the givent input is : " + Encoded)





































   
