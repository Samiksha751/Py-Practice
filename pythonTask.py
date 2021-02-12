mat1 = [[1,2,3],[4,5,6]]
mat2 = [[7,8,9],[6,7,3]]
result= [[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
             result[i][j]+= mat1[i][k]*mat2[j][k]
for r in result:
    print(r)
        