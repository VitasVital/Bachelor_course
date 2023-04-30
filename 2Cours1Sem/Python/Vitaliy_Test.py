import math
import copy
import numpy as np

class First_Task:
    def function(self,x,eps):
        res=1
        member=1
        k=1
        while(member>=eps):
            member=x**k

            factorial=1
            for i in range(k):
                factorial*=(i+1)
            member/=factorial
            res+=member
            k+=1
        res//=eps
        res*=eps
        return res

# v=First_Task()
# print(v.function(2.0,0.001))

class Second_Task:
    def a_function(self,text):
        l=[]
        help=[]
        for i in range(len(text)):
            if text[i]==" ":
                help.reverse()
                l+=help
                l+=" "
                help=[]
            elif i==(len(text)-1):
                help += text[i]
                help.reverse()
                l += help
            else:
                help+=text[i]
        text=""
        for i in l:
            text+=i
        return text

    def b_function(self,text):
        l=[]
        k1=0
        for i in text:
            l+=i
        l.append(" ")
        l.insert(0," ")
        for i in range(len(l)):
            if l[i]==" " or i==len(l)-1:
                k2=i
                for j in range(len(l[k1:k2])//2+1):
                    l[k1+j],l[k2-j]=l[k2-j],l[k1+j]
                k1=i
        l.pop(0)
        l.pop()
        text=""
        for i in l:
            text+=i
        return text

# f=open("file1.txt",encoding="utf-8")
# f2=open("file2.txt","w",encoding="utf-8")
# text=f.read()
# c=Second_Task()
# solution=c.a_function(text)
# print(solution)
# f2.write(solution)
# f.close()
# f2.close()



matrix=np.array([[6,7,9,8,4,2,5,3,1],
                [8,3,5,1,6,7,4,2,9],
                [2,1,4,9,3,5,7,6,8],
                [7,6,8,5,1,3,9,4,2],
                [3,4,2,6,8,9,1,5,7],
                [5,9,1,7,2,4,3,8,6],
                [9,8,6,3,5,1,2,7,4],
                [1,2,3,4,7,8,6,9,5],
                [4,5,7,2,9,6,8,1,3]], int)


class Third_Task:
    def function(self,matrix):
        matr=copy.copy(matrix)

        for x in range(len(matrix)):
            count1 = set()
            count2 = set()
            for y in range(len(matrix)):
                count1.add(matrix[x][y])
                count2.add(matrix[y][x])
            if (len(count1)!=len(matrix)):
                return False
            if (len(count2)!=len(matrix)):
                return False
        helpx=3
        helpy=3
        for x in range(3):
            for y in range(3):
                count1 = set()
                for i in range(3):
                    for j in range(3):
                        count1.add(matrix[helpx*x+i][helpy*y+j])
                if (len(count1) != len(matrix)):
                    return False

        return True

# m=Third_Task()
# print(m.function(matrix))