def negative_one_side(arr):
    for i in arr:
        if i<0:
            print(i)
            arr.remove(i)
            
            arr.append(i)
        
                 
          
    print(arr)

            
            


arrry = [-9,1,3,6,7,-5,9,-9,-6,4,-3,4,3,-8]
negative_one_side(arrry)
