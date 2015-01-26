## Bellman-Ford Algorithm for single source shortest paths

Calculates the length of the shortest path between a source vertex and all other vertices in weighted, directed graphs. Graphs can have arbitrary edge weights. Exits with an error if a negative cost cycle is detected.

* Time complexity: O(|V||E|)


Uses the dynamic programming algorithmic design strategy.
* Optimal substructure: If P is the shortest path from s to v with at most i edges, then either
  * P has less than i edges, in which case it is the shortest path with at most i-1 edges
  * P has exactly i edges and contains as its last hop the edge (w,v) and P' is the shortest path from s to w with at most i-1 edges.
* Recurrence: For every 1 ≤ i ≤ |V|-1, for every edge (u,v) Cost<sub>(v,i)</sub> = min{Cost<sub>(v,i-1)</sub>, Cost<sub>(u,i-1)</sub> + c<sub>(u,v)</sub> }

See http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm