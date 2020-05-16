def solution(banana_list):
    def gcd(x, y):
       while(y):
           x, y = y, x % y
       return x
    def remove_guard(guards, min):
        for i in range(len(guards)):
            j = 0 
            while j < len(guards[i]):
                if(guards[i][j]==min):
                    guards[i].pop(j)
                j+=1 
        guards[min]=[-1]
    def will_loop(a,b):
        z = (a + b) / gcd(a, b)
        z=int(z)
        return bool((z - 1) & z)
        # if(a<b):
        #     x = Fraction(b,a)
        # else :
        #     x = Fraction(a,b)
        # a1=x.numerator
        # b1=x.denominator
        # ans = pow(2,b1,b1+a1)
        # return bool(ans)
    
    def get_match(p,loopable,visited):
        #print("start",p,loopable,visited)
        for i in range(len(banana_list)):
            if guards[i][p] and visited[i]==False :
                visited[i]=True
                if loopable[i]==-1 or get_match(loopable[i],loopable,visited):
                    loopable[i]=p
                    return True
        #print(loopable,visited)
        return False  


    ans=0
    # print(will_loop(7,21))
    leng= len(banana_list)
    guards=[[False] *leng for i in range(leng)]
    #print(leng,guards)
    for i in range(leng):
        for j in range(i+1):
            if(will_loop(banana_list[i], banana_list[j])):
                #print(i,j)
                guards[i][j]=True
                guards[j][i]=True
    # for i in range(leng):
    #          for j in range(leng):
    #              print(guards[i][j],end=" ")
    #          print("\n",end="")
    ans = 0
    loopable= [-1] * leng
    for i in range(leng):
        visited = [False] * leng
        a=get_match(i, loopable,visited)
        #print(a)
        if a:
            ans += 1
    return leng -2*( ans//2)
print(solution([1,1]))
