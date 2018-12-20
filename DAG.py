# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:06:35 2018

@author: Pioneer
"""
from pathlib import Path

class DAG:
    def __init__(self):
        self.v = None
        self.e = list()
        self.visited = None
        self.isDAG = True
        self.ts = list()
        self.clock = 1
        self.pre = list()
        self.post = list()
#----------------------------------------------------------------------------------
        
        
    def Main(self):
        corf = input("Do you want to provide the input from the command line or a .txt file? Type c for command line else type f for .txt file: ")
        "".upper()
        if(corf.strip().upper() == "C"):
            self.v = int(input("Enter the number of vetrices: "))
            while True:
                inp = input("Enter the edges (u,v) or press enter if finished: ")
                if(inp.strip() != ""):
                    inpEdge = inp.split(',')
                    self.e.append( [ int(inpEdge[0]), int(inpEdge[1]) ] )
                else:
                    break
        elif(corf.strip().upper() == "F"):
            f = input("Enter the full file path including .txt: ")
            file = open(Path(f))
            self.v = int(file.readline())
            for edges in file:
                inpEdge = edges.strip().split(',')
                self.e.append( [ int(inpEdge[0]), int(inpEdge[1]) ] )
        else:
            print("Incorrect Option Choosen!")
            return
            
        self.visited = [False]*(self.v+1)
        self.pre = [None]*(self.v+1)
        self.post = [None]*(self.v+1)
        self.visited[0] = None
        self.DFS()
        
        # check for back-edge with pre and post number       
        for edge in self.e:
            ver, u = edge[1], edge[0]
            if self.pre[ver] < self.pre[u] and self.post[ver] > self.post[u]:
                self.isDAG = False
                break
            
        if(self.isDAG):
            print("YES")
            print(*reversed(self.ts), sep = ', ')
            print(max(self.LongestPath()[:]))
        else:
            print("NO")
#----------------------------------------------------------------------------------
                
            
    def DFS(self):
        for u in range(1, self.v+1):
            if self.visited[u] == False:
                self.Explore(u)
#----------------------------------------------------------------------------------
            
            
    def Explore(self, u):
        self.visited[u] = True
        edges = [edge for edge in self.e if edge[0] == u]        
        self.PreVisit(u)
        
        for edge in edges:
            if self.visited[edge[1]] == False:
                self.Explore(edge[1])
                
        self.PostVisit(u)        
        self.ts.append(u)
#----------------------------------------------------------------------------------

        
    def PreVisit(self, u):
        self.pre[u] = self.clock
        self.clock += 1
#----------------------------------------------------------------------------------

        
    def PostVisit(self, u):
        self.post[u] = self.clock
        self.clock += 1
#----------------------------------------------------------------------------------
        
        
    def LongestPath(self):
        dist = [-1]*(self.v+1)
        dist[1] = 0
        for u in reversed(self.ts):
            edges = [edge for edge in self.e if edge[0] == u]
            for edge in edges:
                if dist[edge[1]] < dist[u] + 1 and dist[u] + 1 > 0:
                    dist[edge[1]] = dist[u] + 1
        return dist
#----------------------------------------------------------------------------------    
###################################################################################
        
DAG().Main()


