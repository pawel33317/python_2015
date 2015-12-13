f = open('matrix.txt', 'r')
matrixy = f.read().split("\n")

n = 2
matrix = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(2)]
matrixMul = [[0 for k in xrange(n)] for j in xrange(n)]
for i in range(len(matrixy)):
    tmp1=matrixy[i].split(";")
    for j in range(len(tmp1)):
        tmp2=tmp1[j].split(" ")
        for k in range(len(tmp2)):
            #print str(i)+' '+str(j)+' '+str(k)
            matrix[i][j][k]=tmp2[k]

            
for i in range(len(matrix[0])):
    for j in range(len(matrix[0][0])):
        matrixMul[i][j] = 0

        
for i in range(len(matrix[0])):
    for j in range(len(matrix[1][0])):
        for k in range(len(matrix[1][0])):
            matrixMul[i][j] += int(matrix[0][i][k]) * int(matrix[1][k][j]);

for i in range(len(matrix[0])):
    for j in range(len(matrix[0][0])):
        print matrixMul[i][j],
        print ' ',
    print '\n' 
f.close()
