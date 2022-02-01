# write a program to calculate the valume of a cuboid using default arguments
def volume(l,w=3,h=4):
    print(" length:",l,"\t width:",w,"\t hight:",h)
    return l*w*h
print(" valume1",volume(4,6,6))
print(" volume2", volume(3,7,5))
print(" volume",volume(4))
