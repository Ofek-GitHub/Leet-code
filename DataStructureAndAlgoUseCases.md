# Leet-code
there are several algorithms and data structures We will use to solve leet-code problems.
1) binary search
2) linked list 
3) bubble sort 
4) heap sort
5) insertion sort
6) merge sort
7) quick sort
8) hash table
9) recursion
10) memoization
11)dynamic programming
12) graph manipulation(BFS,DFS,DAG,shortest paths,Dikstra ETC)

I will explain the use case of each data structure and algorithms and how should we approach problems.


1)
 Binary search is an efficient algorithm for finding an element within a sorted array or list. It works by repeatedly dividing the list in half until the element is found or it is clear that the element is not in the list.

There are a few key conditions that must be met in order for binary search to be applicable:

The element you are searching for must be contained within the list or array.
The list or array must be sorted.
The list or array must be relatively small. Binary search has a time complexity of O(log n), so it is more efficient for smaller lists.
You would use binary search when you need to find an element within a sorted list or array and the list is not too large. It is a good choice when you need to perform many searches on the same list, as the list only needs to be sorted once.



2)
A linked list is a linear data structure in which each element is a separate object, called a node, that stores a reference (link) to the next node in the list. Linked lists are used to implement many other data structures, such as stacks, queues, and graphs.

There are a few key advantages to using linked lists over other data structures, such as arrays:

Dynamic size: Linked lists can grow or shrink as needed, since each node is stored separately in memory. This is in contrast to arrays, which have a fixed size once they are created.

Efficient insertion and deletion: It is easy to add or remove elements from a linked list, since you only need to update the links of the adjacent nodes. With an array, you may need to shift elements around to make room for new elements or fill the gap left by deleted elements.

No wasted space: In a linked list, each element uses only as much space as it needs to store the data and the link. In an array, the entire array must be created with a fixed size, even if you don't end up using all the elements.

Overall, you would use a linked list when you need a dynamic data structure that allows efficient insertion and deletion of elements, and when you don't need to access elements randomly (since linked lists do not support random access).



3)
Bubble sort is a simple sorting algorithm that repeatedly iterates through the list, compares adjacent elements, and swaps them if they are in the wrong order. It is called "bubble sort" because the smaller elements tend to "bubble" up to the top of the list, like bubbles rising to the surface of a liquid.

Bubble sort has a time complexity of O(n^2), which makes it inefficient for sorting large lists. It is not a good choice for most real-world sorting tasks. However, it can be a useful learning tool for understanding how sorting algorithms work, and it may be appropriate in some very limited situations where the list is small and performance is not a concern.

In general, you would not use bubble sort for sorting tasks in production environments. There are many other sorting algorithms that are more efficient, such as quicksort, mergesort, and heapsort. These algorithms have time complexities of O(n log n) or better, which makes them much faster for sorting large lists.




4)
Heapsort is a comparison-based sorting algorithm that uses a data structure called a heap to sort a list of elements. A heap is a complete binary tree that satisfies the heap property, which states that the value of each node is greater than or equal to the values of its children.

Heapsort has a time complexity of O(n log n), which makes it efficient for sorting large lists. It is a good choice when you need to sort a list in-place (without using additional memory) and when you need stable sorting (meaning that the order of equal elements is preserved).

In general, you would use heapsort when you need to sort a large list and you want a sorting algorithm that is efficient and stable. It is a good choice for many real-world sorting tasks. However, it is not the fastest sorting algorithm in all cases, and there are other algorithms that may be more suitable for certain types of data or specific use cases.



5)
Insertion sort is a simple sorting algorithm that builds the final sorted list one element at a time, by repeatedly inserting the next element into the correct position in the already-sorted portion of the list. It has a time complexity of O(n^2), which makes it inefficient for sorting large lists.

Insertion sort is a good choice when the list is small, or when the elements are already partially sorted. It is also a good choice when the list is almost sorted, since it can sort the list in linear time in this case.

In general, you would use insertion sort when you need to sort a small list and you don't need the fastest possible sorting algorithm. It is also a good choice when the list is partially sorted or almost sorted, since it can take advantage of this to sort the list efficiently. However, for most real-world sorting tasks, there are more efficient algorithms available, such as quicksort or mergesort.





6)
Merge sort is a divide-and-conquer sorting algorithm that works by recursively dividing the list into smaller pieces, sorting the pieces, and then merging the sorted pieces back together. It has a time complexity of O(n log n), which makes it efficient for sorting large lists.

Merge sort is a good choice when you need a stable sort (meaning that the order of equal elements is preserved) and when you need to sort a list in-place (without using additional memory). It is also a good choice when you need to sort a list that is very large or when you don't know the size of the list in advance, since it can handle lists of any size.

In general, you would use merge sort when you need to sort a large list and you want a stable, in-place sorting algorithm that can handle lists of any size. It is a good choice for many real-world sorting tasks, but there may be faster algorithms available for certain types of data or specific use cases.



7)

Quick sort is a divide-and-conquer sorting algorithm that works by partitioning the list around a pivot element, and then recursively sorting the sublists on either side of the pivot. It has a time complexity of O(n log n) on average, which makes it efficient for sorting large lists.

Quick sort is a good choice when you need a fast sorting algorithm and when you don't need a stable sort (meaning that the order of equal elements is not preserved). It is also a good choice when you have a list that is partially sorted or almost sorted, since it can take advantage of this to sort the list efficiently.

In general, you would use quick sort when you need to sort a large list and you want a fast, in-place sorting algorithm. It is a good choice for many real-world sorting tasks, but there may be other algorithms that are more suitable for certain types of data or specific use cases. It is important to note that the performance of quick sort can degrade to O(n^2) in the worst case, so it is important to choose a good pivot element to ensure good performance.

8)

A hash table is a data structure that stores a collection of keys and values, and allows for efficient insertion, deletion, and lookup of values based on their keys. It works by using a hash function to map the keys to indices in an array, and then storing the values at those indices.

There are a few key advantages to using a hash table over other data structures:

Fast lookup: Hash tables support constant-time lookup of values based on their keys, as long as the hash function is well-behaved and the hash table is not too full.

Efficient insertion and deletion: Hash tables also support constant-time insertion and deletion of key-value pairs, as long as the hash function is well-behaved and the hash table is not too full.

No wasted space: A hash table uses only as much space as is needed to store the keys and values, making it a space-efficient data structure.

You would use a hash table when you need to store a large collection of key-value pairs and you need to be able to efficiently look up, insert, and delete values based on their keys. Hash tables are a good choice for many real-world tasks, such as storing dictionaries, implementing caches, and implementing sets.


9)
Recursion is a programming technique in which a function calls itself to solve a problem. It can be a useful tool for solving problems that can be broken down into smaller, similar subproblems, or for implementing algorithms that have a recursive structure.

There are a few key situations in which recursion can be useful:

When the problem can be naturally divided into smaller subproblems: Recursion can be a good choice for problems that can be divided into smaller subproblems that are similar to the original problem. For example, the problem of finding the nth term in the Fibonacci sequence can be solved recursively by defining a function that calculates the nth term as the sum of the (n-1)th and (n-2)th terms.

When the problem involves processing a tree or graph data structure: Recursion is a natural choice for traversing tree and graph data structures, since these data structures have a recursive structure. For example, you could use recursion to implement a depth-first search or a breadth-first search on a graph.

When the problem can be expressed in terms of a recursive function: Some problems are naturally expressed in terms of a recursive function, and recursion can be a good choice for implementing these problems. For example, the problem of calculating the factorial of a number can be expressed as a recursive function that calculates the factorial of (n-1) and then multiplies it by n.

Overall, you would use recursion when you are solving a problem that can be naturally divided into smaller subproblems, or when the problem involves processing a tree or graph data structure, or when the problem can be expressed in terms of a recursive function. It is important to ensure that the recursive function has a base case to avoid infinite recursion.


10)

Memoization is a technique used to optimize the performance of recursive algorithms by storing the results of expensive function calls and returning the stored result when the same inputs occur again. This can help to avoid recomputing the same result multiple times, which can improve the performance of the algorithm by reducing the number of function calls and the amount of work that needs to be done.

For example, consider the problem of calculating the nth term in the Fibonacci sequence, which is defined as the sum of the (n-1)th and (n-2)th terms. A recursive function to calculate the nth term might look like this:
Overall, you would use memoization to optimize the performance of recursive algorithms that compute the same result multiple times, in order to reduce the number of function calls and the amount of work that needs to be done. It can be especially useful for algorithms that have a time complexity of O(2^n) or higher.

11)
Dynamic programming is a technique for solving problems by breaking them down into smaller subproblems, solving the subproblems, and storing the results in a table or array. The results can then be used to solve larger subproblems and ultimately the original problem. This technique can be used to improve the performance of recursive algorithms by avoiding the need to recalculate the same result multiple times.

Dynamic programming is a good choice for solving problems that have a recursive structure and that exhibit overlapping subproblems, meaning that the same subproblems are solved multiple times in the course of solving the original problem. It is typically used to solve optimization problems, where the goal is to find the optimal solution among a set of possible solutions.

Some common examples of problems that can be solved using dynamic programming include the Fibonacci sequence, the Knapsack problem, and the Longest Common Subsequence problem.

To use dynamic programming to solve a problem, you need to identify the subproblems and the optimal solution for each subproblem. You can then store the results in a table or array and use them to solve larger subproblems and ultimately the original problem. It is important to ensure that the subproblems are solved in the correct order, so that the results of the smaller subproblems are available when solving the larger subproblems.

In general, you would use dynamic programming to solve optimization problems that have a recursive structure and that exhibit overlapping subproblems, in order to improve the performance of the algorithm by avoiding the need to recalculate the same result multiple times. It is a powerful technique that can be used to solve a wide range of problems, but it can be challenging to implement and requires careful thought and planning.



12)

Graph manipulation refers to the process of modifying a graph data structure by adding or deleting nodes or edges, or by modifying the properties of the nodes or edges. Graph manipulation is a common task in computer science, and is used in a wide range of applications, including social networks, routing algorithms, and machine learning.

There are a few key situations in which you might use graph manipulation:

When you need to store and manipulate a network of interconnected nodes: Graphs are a natural choice for storing and manipulating networks of interconnected nodes, such as social networks, transportation networks, and communication networks. You might use graph manipulation to add or delete nodes or edges, or to update the properties of the nodes or edges.

When you need to perform graph traversal or search: Graph manipulation can be used to perform graph traversal or search algorithms, such as depth-first search or breadth-first search. These algorithms involve visiting the nodes of the graph in a specific order, and may require adding or deleting nodes from a queue or stack as they are visited.

When you need to implement machine learning algorithms: Some machine learning algorithms, such as decision trees and neural networks, can be represented as graphs. You might use graph manipulation to create or modify these graphs in order to implement the algorithms.

Overall, you would use graph manipulation when you need to store and manipulate a network of interconnected nodes, when you need to perform graph traversal or search, or when you need to implement machine learning algorithms that are represented as graphs. Graph manipulation can be a powerful tool for solving a wide range of problems, but it requires careful planning and a thorough understanding of the algorithms and data structures involved.


BFS :

Breadth-first search (BFS) is an algorithm for traversing or searching a graph or tree data structure. It works by starting at the root node and exploring all of the neighboring nodes at the current depth level before moving on to the nodes at the next depth level.

There are a few key situations in which you might use BFS:

When you need to find the shortest path between two nodes: BFS is often used to find the shortest path between two nodes in a graph, since it always explores the nodes at the current depth level before moving on to the next depth level. This ensures that the path found by BFS is always the shortest path, as measured by the number of edges.

When you need to visit all of the nodes in a graph: BFS is also often used to visit all of the nodes in a graph, since it explores the nodes level by level, starting at the root node. This can be useful for tasks such as graph traversal or topological sort.

When you need to find all nodes that are a certain distance from the root node: BFS can be used to find all of the nodes that are a certain distance from the root node, by stopping the search when the desired depth level is reached.

Overall, you would use BFS when you need to find the shortest path between two nodes, when you need to visit all of the nodes in a graph, or when you need to find all nodes that are a certain distance from the root node. It is a useful algorithm for many real-world tasks, but it has a time complexity of O(n + m), where n is the number of nodes and m is the number of edges, which can make it inefficient for very large graphs.


DFS :


Depth-first search (DFS) is an algorithm for traversing or searching a graph or tree data structure. It works by starting at the root node and exploring as far as possible along each branch before backtracking.

There are a few key situations in which you might use DFS:

When you need to visit all of the nodes in a graph: DFS is often used to visit all of the nodes in a graph, since it explores each branch as far as possible before backtracking. This can be useful for tasks such as graph traversal or topological sort.

When you need to find all nodes that are a certain distance from the root node: DFS can be used to find all of the nodes that are a certain distance from the root node, by stopping the search when the desired depth level is reached.

When you need to find a path between two nodes: DFS can be used to find a path between two nodes in a graph, by starting at the root node and searching for the destination node as it explores the graph. However, DFS does not always find the shortest path between two nodes, since it does not always explore the nodes at the current depth level before moving on to the next depth level.

Overall, you would use DFS when you need to visit all of the nodes in a graph, when you need


SHORTEST PATHS  : 

There are several algorithms that can be used to find the shortest path between two nodes in a graph. Some common algorithms include:

Dijkstra's algorithm: This algorithm is used to find the shortest path between two nodes in a graph with non-negative edge weights. It works by repeatedly selecting the node with the smallest distance from the source node and updating the distances of its neighbors.

A* search: This algorithm is used to find the shortest path between two nodes in a graph with both positive and negative edge weights. It uses a heuristic function to guide the search and can be used to find the shortest path in real-time, such as in a video game.

Bellman-Ford algorithm: This algorithm is used to find the shortest path between two nodes in a graph with both positive and negative edge weights. It works by repeatedly relaxing the edges of the graph and can handle graphs with negative-weight cycles.

Floyd-Warshall algorithm: This algorithm is used to find the shortest path between all pairs of nodes in a graph. It works by using dynamic programming to compute the shortest path between each pair of nodes.

Overall, the choice of shortest path algorithm will depend on the characteristics of the graph and the requirements of the application.


Dijkstra's algorithm: Dijkstra's algorithm is a good choice for finding the shortest path between two nodes in a graph with non-negative edge weights. It is often used in applications such as routing and navigation, where the goal is to find the shortest path between two locations.

A* search: A* search is a good choice for finding the shortest path between two nodes in a graph with both positive and negative edge weights. It is often used in real-time applications, such as video games, where the goal is to find the shortest path in real-time.

Bellman-Ford algorithm: Bellman-Ford algorithm is a good choice for finding the shortest path between two nodes in a graph with both positive and negative edge weights. It is often used in applications such as network routing, where the goal is to find the shortest path between two nodes while taking into account the cost of the edges.

Floyd-Warshall algorithm: Floyd-Warshall algorithm is a good choice for finding the shortest path between all pairs of nodes in a graph. It is often used in applications such as transportation networks, where the goal is to find the shortest path between all pairs of locations.

Overall, the choice of shortest path algorithm will depend on the characteristics of the graph and the requirements of the application. It is important to carefully consider these factors in order to choose the algorithm that is most

