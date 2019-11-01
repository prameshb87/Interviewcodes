"""
Given a nXn matrix, consisting of non-negative numbers, where 0 represents an
obstacle, 1 represents grass or level 1 and every other value represents height
of a node in a tree, find a path from 1 to the top most node. If no path exists,
return -1
eg1. [[0,1,2],[0,0,3],[7,6,4]] returns [1,2,3,4,6,7]
eg2. [[0,1,2],[0,4,3],[7,6,5]] returns [1,2,3,4,5,6,7]
eg3. [[0,1,2],[0,0,0],[7,6,4]] returns -1 as there are 0s separating the top and bottom rows
and there is no path connecting them.
"""

def get_path(m, i, j, path):
    if i < len(m) or j < len(m[i]):
        return
    if a[i][j] == 'X':
        return
    if a[i][j] == 0:
        a[i][j] == 'X'
        return
    if a[i][j] != 1 and len(path) == 0:
        return
    if a[i][j] not in path:
        path.append(a[i][j])
        a[i][j] == 'X'
        if i-1 >= 0 :
            to_visit.append(a[i-1][j])
        if i+1 < len(m) :
            to_visit.append(a[i+1][j])
        if j-1 >= 0 :
            to_visit.append(a[i][j-1])
        if j+1 < len(m[i]) :
            to_visit.append(a[i-1][j])
