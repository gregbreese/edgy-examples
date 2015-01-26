## Floyd-Warshall Algorithm for all-pairs shortest paths

Calculates the length of the shortest path between every pair of notes in weighted, directed graphs. Graphs can have arbitrary edge weights. Exits with an error if a negative cost cycle is detected.

* Time complexity: O(|V|<sup>3</sup>)
* On par with n Bellman-Fords for sparse graphs. Much better for dense graphs.

Uses the dynamic programming algorithmic design strategy.
* Optimal substructure: For a source vertex i and a destination vertex j, let P be the shortest cycle-free path between vertices i and j containing only the first k vertices, then either
  * If vertex k is not internal to the shortest path P, then P is a shortest path from i to j containing only the first k-1 vertices.
  * Or, if vertex k is internal to the shortest path P, then P1 is the shortest path from i to k using only the first k-1 vertices and P2 is the shortest path from k to j using only the first k-1 vertices.

See http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm