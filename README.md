= Untied States

> And here’s a fun puzzle:
> Several states have suddenly decided to form empires by annexing all of their neighbors. The remaining free states are few and isolated.
> Try to classify the states as Capitals, Vassal States, or Free States. Each Vassal must be adjacent to exactly one Capital, a Capital can only be adjacent to its Vassals, and no two Free States can be adjacent to each other.
> Can this be done? (I have no idea. You need at least one free state, in New England; there are graphs for which this is unsolvable, like the 5-cycle.) Which sets of capitals are possible?

== Input
Store the undirected graph as a series of lines in a file, `state-connections.txt` by default. Each line should be space-separated tokens, where the first token is a vertex and the following tokens each are a vertex adjacent to the first.
Redundancies (multiple lines starting with the same vertex, or listing edges from both ends) are permissible and will be handled gracefully.

Example file format:
    CA OR NV AZ
    WA OR ID
    OR WA CA NV ID
    NV CA OR ID AZ
    ID WA OR NV
    AZ CA NV

Running this algorithm on large graphs is **not recommended**.

== Usage
`$ python empires.py foobar.txt` calls this using `foobar.txt` to store the graph.
`$ python empires.py` calls it using `state-connections.txt`.
