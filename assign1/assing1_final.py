#Assignment 1 - 2D Line Segment Clipping program
c_zone = 0 #clipping zone 0000
bound_left = 1 #left 0001
bound_right = 2 #right 0010
bound_bottom = 4 #under 0100
bound_top = 8 #top 1000

#Find region what the line is 
def findRegion(x, y, xmin, xmax, ymin, ymax):

    line = c_zone  #set zero for the line 
    if x <xmin : 
        line |= bound_left
    elif x > xmax :
        line |= bound_right
    if y < ymin :
        line |= bound_bottom
    elif y > ymax :
        line |= bound_top
    return line 

def clipping(x1,y1,x2,y2 , xmin, xmax, ymin, ymax):
    start =  findRegion(x1,y1, xmin, xmax, ymin, ymax)
    final = findRegion(x2,y2, xmin, xmax, ymin, ymax)
    accept = False
    print( " ----------------------------- ")
    print("input is : (%d, %d) to (%d, %d)" % (x1,y1,x2,y2))
    
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
            print(out)
 
            m = (y2 - y1) / (x2 - x1) # find  slope 

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
                start =  findRegion(x1,y1, xmin, xmax, ymin, ymax)
            
            else :
                x2 = x
                y2 = y 
                final = findRegion(x2, y2, xmin, xmax, ymin, ymax)

    if accept :
        print ("Line is in window and position is  (%d, %d) to (%d, %d)" % (x1, y1, x2, y2))

    else :
        print ("Line is not in the window  Line is in " + bin(start) + " and " + bin (final) +  " region")       




#In the window x_min =  0 , y_min = 0 and x_max = 10, y_max = 10 
#insert (-1,6) and (5,12) กรณีที่มีบางส่วนอยู่ใน window
clipping(-1,6,5,12,0,10,0,10)
#insert (-2,-5) and (-10,-4) ในกรณีที่ไม่มีส่ววนไหนอยู่ใน window เลย
clipping(-2,-5,-10,-4,0,10,0,10) 
#insert (1,1) , (3,3) ในกรณีที่ทุกส่วนอยู่ใน window
clipping(1,1,3,3,0,10,0,10) 
