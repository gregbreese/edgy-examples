## Kruskal.xml

Contains two versions of Kruskal's Algorithm for MST.

MST Kruskal (Basic) is a simple version of Kruskal's algorithm that relies on the 'is cyclic' block to determine whether an edge is required. This version is easier to understand but not representative of how the algorithm would actually be implemented as testing for cyclicity is O(|E|).


MST Kruskal (Advanced) uses a union-find data structure to keep track of which vertices have been connected. This is more representative of an actual implementation of the algorithm but not very readable without first understanding the union-find data structure. This block makes use of two other blocks that are included; Find and Union.



## Prim.xml

Contains an implementation of Prim's Algorithm for MST.
