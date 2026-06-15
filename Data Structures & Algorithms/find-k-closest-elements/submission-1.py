class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        w = arr[:k]
        l = 0

        for i in range(k, n):
            d1 = abs(arr[i]-x)
            lastd = abs(w[-1]-x)
            firstd= abs(w[0]- x)


            if lastd >= d1:
                w.remove(arr[l])
                w.append(arr[i])
                l+=1
            else:
                if firstd <= d1:
                    continue 
                else:
                    w.remove(arr[l])
                    w.append(arr[i])
                    l+=1
        return w 


                

        