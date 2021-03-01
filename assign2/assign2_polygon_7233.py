""" 

Assignment 2 : Polygon Clipping
Name : Sasikarn Aungkanakorn 

"""
def clip(polygon, rectangular):
    def intersection(): # หาจุดตัดกันระหว่าง  edge of window 
        x1,y1 = edge1[0], edge1[1]
        x2,y2 = edge2[0], edge2[1]
        x3,y3 = line1[0], line1[1]
        x4,y4 = line2[0], line2[1]

        top = [(x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4), (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)] 
        under = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
        return (top[0]/under, top[1]/ under)




    result = []
    set_result = set()
    edge1 = rectangular[-1]
    for edge in rectangular : # ไล่ทำงานไปทีละ edge 
        edge2 = edge 
        print("########### Edge : ", edge1,edge2)
        line1 = polygon[-1]


        print(polygon)
        for line in polygon: #ไล่ที่ละเส้นโดยยึด edge ที่กำลังอยู่ตอนนี้เป็นหลัก
            line2 = line

            # check ว่าอยู่ใน window หรือไม่ 
            # chack point P(x-1,y-1)
            check1 = (edge2[0]-edge1[0])*(line1[1]-edge1[1]) - (edge2[1]-edge1[1])*(line1[0]-edge1[0])
            print("-check 1 : ", check1)

            #check point P(x,y)
            check2 = (edge2[0]-edge1[0])*(line2[1]-edge1[1]) - (edge2[1]-edge1[1])*(line2[0]-edge1[0])
            print("-check 2 : ", check2)

            if check1 > 0  :  #line1 is  in
                if check2 > 0 or check2 == 0  : #กรณีที่ in - in 
                    print("1 . THe line is in the window ", line1, line2)
                    # result.append(line1)

                else : # กรณีที่  check2 < 0  in - out
                    print("--Need to compute line2")
                    result.append(intersection())
                    
            elif check2 > 0 :  #line 2 is in 
                if check1 > 0 or check1 == 0 : #กรณีที่ in - in 
                    print("2. THe line is in the window ", line1, line2)
                    # result.append(line2)
                else : #กรณีที่ check 1 < 0 : line 1 is  out  กรณีที่ out - in 
                    print("--Need to compute line1")
                    result.append(intersection())
                    

            elif check1 == 0 and check2 == 0 : # กรณี in - in 
                print("3. the line is in the edge of the window", line1, line2)
                result.append(line1)
                result.append(line2)

            else : 
                print("all the line is out")
                

            line1 = line2
            
            print("=================================")

        edge1 = edge2
    print("input  : " , polygon)
    print("window : " , rectangular)
    for i in result :
        set_result.add(i)

    return set_result
        



# polygon = [(0,6),(0,0),(10,0),(10,6),(5,11)]
# rectangular = [(0,0),(10,0),(10,10),(0,10)]

# polygon = [(5,-1), (11,5), (8,11), (2,11), (-1,5)]
# rectangular = [(0,0),(10,0),(10,10),(0,10)]

polygon = [(50,150),(200,50),(350,150),(350,300),(250,300),(200,250),(150,350),(100,250),(100,200)]
rectangular = [(100,100),(300,100),(300,300),(100,300)]

print( "output : ",clip(polygon,rectangular))