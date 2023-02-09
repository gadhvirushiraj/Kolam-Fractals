import turtle

axiom = ["F","-", "-", "F", "-", "-", "F"]
replace_F = ["F","+","F","-","-","F","+","F"]
theta = 60

def construct(axiom):
    final_axiom = []
    for i,x in enumerate(axiom):
        if x == "F":
            final_axiom.extend(replace_F)
        else:
            final_axiom.append(x)

    return final_axiom
        
def draw(final):
    kolam = turtle.Turtle()
    kolam.speed(10000)
    for i,x in enumerate(final):
        if x == "F":
            kolam.forward(10)
        elif x == "+":
            kolam.left(theta)
        elif x == "-":
            kolam.right(theta)
    turtle.done()

for _ in range(3):
    axiom = construct(axiom)

draw(axiom)