class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        
        def DFS(node):
            # Cycle detected.
            if visited[node] == 1:
                return False
            
            # Visit this node, explore neighbors.
            visited[node] = 1
            for nbr in G[node]:
                if visited[nbr] != 2 and not DFS(nbr):
                    return False
            
            # Done visiting node.
            visited[node] = 2
            return True
        
        # Build the graph.
        G = collections.defaultdict(list)
        for postreq, course in prerequisites:
            G[course].append(postreq)
            G[postreq]  # Make sure nodes are made for courses with no postreqs.
        
        visited = [0] * numCourses
        for node in G:
            if not visited[node]:
                if not DFS(node):
                    return False
        return True