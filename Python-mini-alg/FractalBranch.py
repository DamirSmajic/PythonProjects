import turtle
t = turtle.Turtle()
t.left(90)

def fraktalno_drvo(duz_grane, t):
    if duz_grane > 1:
        t.forward(duz_grane)
        t.right(45)
        fraktalno_drvo (0.6 * duz_grane, t)
        t.left(90)
        fraktalno_drvo(0.6 * duz_grane, t)
        t.right(45)
        t.backward(duz_grane)

fraktalno_drvo(100, t)
