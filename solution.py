class Solution:
    def twoCitySchedCost(self, costs) -> int:
        
        for i in costs:
            i.append(i[1]-i[0])
        costsort=sorted(costs,key=lambda x:x[2],reverse=True)  
        n=int(len(costsort)/2)
        res=costsort[:n]
        res1=costsort[n:]
        result1=[sum(i) for i in zip(*res)]
        result2=[sum(i) for i in zip(*res1)]
        result=result1[0]+result2[1]
        return result

b=[[10,20],[30,200],[400,50],[30,20]] 
s=Solution()
print(s.twoCitySchedCost(b))