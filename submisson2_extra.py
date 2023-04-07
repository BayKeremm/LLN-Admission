import unittest

def reachableBFS(adj_list,start_node,visited):
    if len(adj_list)==0:
        return set()
    if start_node not in visited:
        visited.add(start_node)
        for neighbor in adj_list[start_node]:
            visited = reachableBFS(adj_list, neighbor, visited)
    return visited
class TestReachable(unittest.TestCase):
    def test_empty(self):
        adj_list = []
        res = reachableBFS(adj_list,0,set())
        self.assertEqual(res,set())
    def test_no_edges(self):
        adj_list = [[], [], [], [], []]
        res = reachableBFS(adj_list,2,set())
        self.assertEqual(res,{2})
    def test_task_source_0(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        res = reachableBFS(adj_list,0,set())
        self.assertEqual(res,{0,1,2,3,4})
    def test_task_source_4(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        res = reachableBFS(adj_list,4,set())
        self.assertEqual(res,{3,4})
    def test_cycle_source_0(self):
        adj_list = [[1], [2], [3,4], [0], []]
        res = reachableBFS(adj_list,0,set())
        self.assertEqual(res,{0,1,2,3,4})
    def test_cycle_source_2(self):
        adj_list = [[1], [2], [3,4], [0], []]
        res = reachableBFS(adj_list,2,set())
        self.assertEqual(res,{0,1,2,3,4})

if __name__ == "__main__":
    unittest.main()

