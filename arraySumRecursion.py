def _findSum(arr): 
     if len(arr)== 1: 
        return arr[0] 
     else: 
        return arr[0]+_findSum(arr[1:])