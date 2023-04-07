import unittest

def reachableDFS(adj_list,start_node):
    if len(adj_list)==0:
        return set()
    to_visit = [start_node]
    visited = set()
    while len(to_visit) != 0:
        node = to_visit.pop() 
        if node not in visited:
            visited.add(node)
            for neighbor in adj_list[node]:
                to_visit.append(neighbor)
    return visited

class TestReachable(unittest.TestCase):
    def test_empty(self):
        adj_list = []
        res = reachableDFS(adj_list,0)
        self.assertEqual(res,set())
    def test_no_edges(self):
        adj_list = [[], [], [], [], []]
        res = reachableDFS(adj_list,2)
        self.assertEqual(res,{2})
    def test_task_source_0(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        res = reachableDFS(adj_list,0)
        self.assertEqual(res,{0,1,2,3,4})
    def test_task_source_4(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        res = reachableDFS(adj_list,4)
        self.assertEqual(res,{3,4})
    def test_cycle_source_0(self):
        adj_list = [[1], [2], [3,4], [0], []]
        res = reachableDFS(adj_list,0)
        self.assertEqual(res,{0,1,2,3,4})
    def test_cycle_source_2(self):
        adj_list = [[1], [2], [3,4], [0], []]
        res = reachableDFS(adj_list,2)
        self.assertEqual(res,{0,1,2,3,4})

if __name__ == "__main__":
    unittest.main()

