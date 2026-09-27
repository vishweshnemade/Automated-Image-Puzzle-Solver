from PIL import Image
#imporing the imade library from PIL


def f(g, d, a):
    """Split a square image into g x g equal-sized puzzle pieces."""
    #piece size = ps
    a= a.convert("RGB").resize((d, d))
    #finding out whole number
    ps = d // g
    #setting up empty so as to store data in it latter
    pieces = []

    for r in range(g):
       for c in range(g):
           #setting up condition within w.r.t c and r
           left = c * ps
           top = r * ps
           right = left + ps
           bottom = top + ps
           #setting up the piceses so that image can be seted
           #appending data in the empty set pieces
           pieces.append(a.crop((left, top, right, bottom)))

    return pieces
#giving result on return
#solving the the situation continuesly
#decreses time complecxity
#we can apply sigle code
#can use it multiple times


