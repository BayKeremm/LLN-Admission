import unittest
def mat_to_list(adj_mat):
    if len(adj_mat)==0 or len(adj_mat[0]) == 0:
        return []
    n = len(adj_mat)
    adj_list = []
    curr_list = []
    for i in range(n):
        for j in range(n):
            if adj_mat[i][j]:
                curr_list.append(j)
        adj_list.append(curr_list) 
        curr_list = []
    return adj_list

class TestMatToList(unittest.TestCase):
    def test_empty(self):
        adj_mat = [[]]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(adj_list,[])
    def test_task(self):
        adj_mat = [[0,1,0,1,0,0],
                [0,0,1,0,0,0],
                [1,0,0,0,0,0],
                [0,0,0,0,1,0],
                [0,0,0,1,0,0],
                [0,0,0,0,0,0]]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(adj_list,[[1, 3], [2], [0], [4], [3], []])
    def test_cyclic(self):
        adj_mat = [ [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,1],
                    [1,0,0,0,0],
                    [0,0,0,0,0]
                   ]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(adj_list,[[1], [2], [3,4], [0], []])

if __name__ == "__main__":
    unittest.main()