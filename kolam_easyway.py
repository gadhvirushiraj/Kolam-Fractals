import turtle
import collections

# struct = list("F-G-G")
# replace_F = list("F-G+F+G-F")
# replace_G = list("GG")
# theta = 120

struct = ["F","-","-","G","-","-","F","-","-","G","-","-"]
replace_F = ["F","+","G","+","F","-","-","G","-","-","F","+","G","+","F"]
replace_G = list("G")
theta = 45

def construct(struct):
    final_struct = []
    for i,x in enumerate(struct):
        if x == "F":
            final_struct.extend(replace_F)
        elif x == "G":
            final_struct.extend(replace_G)
        else:
            final_struct.append(x)

    return final_struct
        
def draw(final):
    kolam = turtle.Turtle()
    kolam.speed(100000)
    for i,x in enumerate(final):
        if x == "F" or x == "G":
            kolam.forward(3)
        elif x == "+":
            kolam.left(theta)
        elif x == "-":
            kolam.right(theta)
    turtle.done()

for _ in range(7):
    struct = construct(struct)

print(struct)
draw(struct)