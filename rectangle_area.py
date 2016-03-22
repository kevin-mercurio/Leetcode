"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.


------ (C,D)
|         |-|-----(G,H)
|         | |       |
(A,B) ------        |
          | |       |
        (E,F) ------|


>>> get_area(-2, -2, 2, 2, -2, -2, 2, 2)
16

"""


def get_area(A,B,C,D,E,F,G,H):
    """ find the total area of overlapping rectangles """
    #area of rectangles:
    a1 = (C-A)*(D-B)
    a2 = (G-E)*(H-F)
    overlap = max( min(C,G) - max(A,E),0)*max( min(D,H) - min(B,F),0)

    area = a1+a2-overlap
    return area

if __name__ == '__main__':
    import doctest
    doctest.testmod()
