#Assignment 1 - 2D Line Segment Clipping program
c_zone = 0 #clipping zone 0000
bound_left = 1 #left 0001
bound_right = 2 #right 0010
bound_bottom = 4 #under 0100
bound_top = 8 #top 1000

#Define (x,y)max and (x,y)min 
xmin = 0
xmax = 10
ymin = 0
ymax = 10

#Find region what the line is 
def findRegion(x, y):

    line = c_zone #set zero for the line 
    if x <xmin :
        line |= bound_left
    elif x > xmax :
        line |= bound_right
    if y < ymin :
        line |= bound_bottom
    elif y > ymax :
        line |= bound_top
    # print ("the line is in this ", bin(line))
    return line 

def clipping(x1,y1,x2,y2):
    start =  findRegion(x1,y1)
    final = findRegion(x2,y2)
    accept = False

    print("input is : (%d, %d) to (%d, %d)" % (x1,y1,x2,y2))
    # x1 = int(x1)
    # x2 = int(x2)
    # y1 = int(y1)
    # y2 = int(y2)
    while True :

        if  start == 0 and final == 0:
            accept = True
            break
        
        elif (start & final) != 0 :
            break
        
        else :
            
            x = 1
            y = 1
            if start != 0 :
                out = start
            else :
                out =  final 
            
            # if out == bound_top :
            m = (y2 - y1) / (x2 - x1)

            if out & bound_top :
                x = x1 + (ymax - y1) / m
                y = ymax
                
            
            elif out &  bound_bottom :
                x = x1 + (ymin - y1) / m
                y = ymin

            elif out & bound_left :
                y = y1 + (xmin - x1) * m
                x = xmin
            
            elif out & bound_right :
                y = y1 + (xmax - x1) * m 
                x = xmax

            if out == start :
                x1 = x
                y1 = y
                start =  findRegion(x1,y1)
            
            else :
                x2 = x
                y2 = y 
                final = findRegion(x2, y2)

    if accept :
        
        print ("Line is in window and position is  (%d, %d) to (%d, %d)" % (x1, y1, x2, y2))

    else :
        print ("Lines eject")       


    

clipping(-1,6,5,12)
clipping(-2,-5,-1,-3) 