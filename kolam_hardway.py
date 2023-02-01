import matplotlib.pyplot as plt
import numpy as np
import math

class Node:
    def __init__(self, parent_dir, is_even, length, dock_parent, color, is_root = False, end = False) -> None:
        self.growth_dir = parent_dir
        self.is_even = is_even
        self.is_root = is_root
        self.length = length
        self.dock_parent = dock_parent
        self.endOdd = end
        self.mycords= (0,0)
        self.color = color
        self.draw()
    
    def draw(self):
        if self.is_even:
            self.mycords = draw_even(self.length, self.growth_dir, self.dock_parent, self.is_root, self.color)
        else:
            self.mycords = draw_odd(self.length, self.growth_dir, self.dock_parent, self.endOdd, self.color)

    def giveCenter(self):
        return self.mycords

def draw_even(l, dir, p_origin, is_root, color):

    mycords= (0,0)
    c2 = l/math.sqrt(2) + 0.5*l
    c1 = l/math.sqrt(2) + 1.5*l
    x = np.array([l/2, l/2, c1 - l, c1]) 
    y = np.array([c1, c1 - l, l/2, l/2])

    if is_root:
        plt.plot(x, y, color = color)
        plt.plot(-x, -y, color = color)
        plt.plot(x, -y, color = color)
        plt.plot(-x, y, color = color)
    else:
        if dir == 1:
            mycords = (c1 + c2 + p_origin[0], p_origin[1])
            plt.plot(x + c2 + c1 + p_origin[0], y + p_origin[1], color = color)
            plt.plot(x + c2 + c1 +  p_origin[0], -y + p_origin[1], color = color)
            plt.plot(-x[:-1] + c2 + c1 + p_origin[0], -y[:-1] + p_origin[1], color = color)
            plt.plot(-x[:-1] + c2 + c1 + p_origin[0], y[:-1] + p_origin[1], color = color)
        elif dir == -1:
            mycords = (- c1 - c2 + p_origin[0], p_origin[1])
            plt.plot(x[:-1] - c2 - c1 + p_origin[0], y[:-1] + p_origin[1], color = color)
            plt.plot(x[:-1] - c2 - c1 + p_origin[0], -y[:-1] + p_origin[1], color = color)
            plt.plot(-x - c2 - c1 + p_origin[0], -y + p_origin[1], color = color)
            plt.plot(-x - c2 - c1 + p_origin[0], y + p_origin[1], color = color)
        elif dir == 2:
            mycords = (p_origin[0], p_origin[1] + c1 + c2)
            plt.plot(x + p_origin[0], y + c2 + c1 + p_origin[1], color = color)
            plt.plot(-x + p_origin[0], y + c2 + c1 + p_origin[1], color = color)
            plt.plot(x[1:] + p_origin[0], -y[1:] + c2 + c1 + p_origin[1], color = color)
            plt.plot(-x[1:] + p_origin[0], -y[1:] + c2 + c1 + p_origin[1], color = color)
        elif dir == -2:
            mycords = (p_origin[0], p_origin[1] - c1 - c2)
            plt.plot(x[1:] + p_origin[0], y[1:] - c2 - c1 + p_origin[1], color = color)
            plt.plot(-x[1:] + p_origin[0], y[1:] - c2 - c1 + p_origin[1], color = color)
            plt.plot(-x + p_origin[0], -y - c2 - c1 + p_origin[1], color = color)
            plt.plot(x + p_origin[0], -y - c2 - c1 + p_origin[1], color = color)

    plt.axis('off')
    plt.gca().set_aspect('equal')

    return mycords
   
def draw_odd(l, dir, p_origin, end, color):

    mycords= (0,0)
    c2 = l/math.sqrt(2) + 0.5*l
    c1 = l/math.sqrt(2) + 1.5*l
    x = np.array([-c1, -(c1 - l), -l/2, -l/2] + [l/2, l/2, c1 - l, c1]) 
    y = np.array([l/2, l/2, c1 - l, c1] + [c1, c1 - l, l/2, l/2])

    if dir == 1:
        if end == True: plt.plot([x[-1] + c2 + c1 + p_origin[0], x[-1] + c2 + c1 + p_origin[0]], [y[-1] + p_origin[1], -y[-1] + p_origin[1]], color = color) 
        mycords = (c1 + c2 + p_origin[0], p_origin[1])
        plt.plot(x[1:] + c2 + c1 + p_origin[0], y[1:] + p_origin[1], color = color)
        plt.plot(x[1:] + c2 + c1 + p_origin[0], -y[1:] + p_origin[1], color = color)
    elif dir == -1:
        if end == True: plt.plot([x[0] - c2 - c1 + p_origin[0], x[0] - c2 - c1 + p_origin[0]], [y[0] + + p_origin[1], -y[0] + p_origin[1]], color = color) 
        mycords = (- c1 - c2 + p_origin[0], p_origin[1])
        plt.plot(x[:-1] - c2 - c1 + p_origin[0], y[:-1] + p_origin[1], color = color)
        plt.plot(x[:-1] - c2 - c1 + p_origin[0], -y[:-1] + p_origin[1], color = color)
    elif dir == 2:
        if end == True: plt.plot([y[-1] + p_origin[0], -y[-1] + p_origin[0]], [x[-1] + c2 + c1 + p_origin[1], x[-1] + c2 + c1 + p_origin[1]], color = color) 
        mycords = (p_origin[0], p_origin[1] + c1 + c2)
        plt.plot(y[1:] + p_origin[0], x[1:] + c2 + c1 + p_origin[1], color = color)
        plt.plot(-y[1:] + p_origin[0], x[1:] + c2 + c1 + p_origin[1], color = color)
    elif dir == -2:
        if end == True: plt.plot([y[0] + p_origin[0], -y[0] + p_origin[0]], [x[0] - c2 - c1 + p_origin[1], x[0] - c2 - c1 + p_origin[1]], color = color) 
        mycords = (p_origin[0], p_origin[1] - c1 - c2)
        plt.plot(y[:-1] + p_origin[0], x[:-1] - c2 - c1 + p_origin[1], color = color)
        plt.plot(-y[:-1] + p_origin[0], x[:-1] - c2 - c1 + p_origin[1], color = color)

    plt.axis('off')
    plt.gca().set_aspect('equal')

    return mycords

def driver(parent, iter, iter_done = 1):

    # if iter_done == iter - 1:
    #     color = 'r'
    # else:
    #     color = 'black'

    color = 'black'
    if iter_done < iter:
        cords = parent.giveCenter()
        dir = [1, -1, 2, -2]
        del dir[dir.index(-1 * parent.growth_dir)]
        if parent.is_even:
            if iter_done in odds:
                ch1 = Node(dir[0], False, 10, cords, color)
                ch2 = Node(dir[1], False, 10, cords, color)
                ch3 = Node(dir[2], False, 10, cords, color)

                if parent.is_root:
                    ch4 = Node((-1 * parent.growth_dir), False, 10, cords, color)
                    driver(ch4, iter, iter_done + 1)
                    del ch4

                driver(ch1, iter, iter_done + 1)
                del ch1
                driver(ch2, iter, iter_done + 1)
                del ch2
                driver(ch3, iter, iter_done + 1)
                del ch3
            else:
                lastCap = True if iter_done + 1 == iter else False
                ch1 = Node(parent.growth_dir, False, 10, cords, color,end = lastCap)
                del dir[dir.index(parent.growth_dir)]
                ch2 = Node(dir[0], False, 10, cords, color, end = True)
                ch3 = Node(dir[1], False, 10, cords, color, end = True)

                if iter_done in oddsodds:
                    if abs(int(ch1.giveCenter()[1])) in oddsoddsodds or abs(int(ch1.giveCenter()[0])) in oddsoddsodds:
                        driver(ch1, iter, iter_done + 1)
                else:
                    driver(ch1, iter, iter_done + 1)
                del ch1
        else:
            ch1 = Node(parent.growth_dir, True, 10, cords, color)
            driver(ch1, iter, iter_done + 1)
            del ch1
    else:
        return None

        

iter = 6
odds = list(range(1, 2**(iter -1), 2))[::2]
oddsodds = list(range(7, 2**(iter - 1), 8))
oddsoddsodds = [int(10*i*(2+math.sqrt(2))) for i in range(0,2**(iter-1),8)]
p = Node(-1, True, 10, (0,0), "black", is_root = True)
driver(p, 2**(iter-1))
plt.show()