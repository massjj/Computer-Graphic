def test(c_edge1, c_edge2, b):
    return (c_edge2[0] - c_edge1[0]) * (b[1] - c_edge1[1]) > (c_edge2[1] - c_edge1[1]) * (b[0] - c_edge1[0])


def cohen(s, e, cp1, cp2):
    dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
    dp = [s[0] - e[0], s[1] - e[1]]
    n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
    n2 = s[0] * e[1] - s[1] * e[0]
    n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
    return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]


def clip(polygon, rectangular):

    outputList = polygon
    # เลือกเส้น edge ที่จะทำการ clipping โดยจะประกอบด้วยจุด  2 จุดคือ (c_edge1, c_edge2)
    c_edge1 = rectangular[-1]

    for clipEdge in rectangular:  # วน loop ไปที่จะ edge
        c_edge2 = clipEdge

        # print("clipE 1: ", c_edge1)
        # print("clipE 2: ", c_edge2)

        inputList = outputList
        outputlist = []
        #print("print inputList : ", inputList)
        #print("point2 : ", point2)

        prev_point = inputList[-1]
        # วน loop ที่รูป polygon
        for position in inputList:

            cur_point = position
            # print("Prev point : ", prev_point)
            # print("Cur_point : ",cur_point)
            #print("Prev : ",prev_point)

            # เช็คว่าจุดต้นและจุดปลายอยู่ภายใน หรือภายนอก window
            if test(c_edge1, c_edge2, cur_point):
                if not test(c_edge1, c_edge2, prev_point):
                    outputList.append(
                        cohen(prev_point, cur_point, c_edge1, c_edge2))
                else:
                    outputList.append(cur_point)

            elif test(c_edge1, c_edge2, prev_point):
                outputList.append(
                    cohen(prev_point, cur_point, c_edge1, c_edge2))

            else:
                prev_point = cur_point

        c_edge1 = c_edge2
    return outputList

# [[100.0, 116.66666666666667], [125.00000000000001, 100.0], [275.0, 100.0], [300.0, 116.66666666666667],
# [300.0, 299.99999999999994], [250.0, 300.0], (200, 250), [175.0, 300.0], [125.0, 300.0], [100.0, 250.0]]


polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300),
           (200, 250), (150, 350), (100, 250), (100, 200)]
rectangular = [(100, 100), (300, 100), (300, 300), (100, 300)]
print(clip(polygon, rectangular))


x1 = s[0]
y1 = s[1]
x2 = e[0]
y2 = e[1]
xmin = cp1[0]
xmax = cp2[0]
ymin = cp1[1]
ymax = cp2[1]
