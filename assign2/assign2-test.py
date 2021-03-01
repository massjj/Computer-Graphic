def clip(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

   def computeIntersection():
      print("s : ", s)
      print("e : ", e)
      print("cp1 : ", cp1)
      print("cp2 : ", cp2)
      print("=========================")
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0]
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

   outputList = subjectPolygon
   
   cp1 = clipPolygon[-1]
   print("cp1 : ", cp1)

   for clipVertex in clipPolygon:
      cp2 = clipVertex
      print("clipolygonn : ",cp2)
      print("CP1 --- ",cp1)
      inputList = outputList
      #print("output",outputList)
      outputList = []
      s = inputList[-1]
      print("s : ", s)
      for subjectVertex in inputList:
         e = subjectVertex
         # print("Print ----- ", e)
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
         #print("s is : ", s)
      cp1 = cp2
   return(outputList)


polygon = [(50,150),(200,50),(350,150),(350,300),(250,300),(200,250),(150,350),(100,250),(100,200)]
rectangular = [(100,100),(300,100),(300,300),(100,300)]
clip = clip(polygon,rectangular)
print(clip)