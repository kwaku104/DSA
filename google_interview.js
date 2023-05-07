// Naive
function hasPairWithSum(arr, sum){
    var arrayElements = []
    var len = arr.length;
    for(var i =0; i<len-1; i++){
       for(var j = i+1;j<len; j++){
          if (arr[i] + arr[j] === sum)
          arrayElements.push(arr.indexOf(arr[i]))
          arrayElements.push(arr.indexOf(arr[j]))
          console.log(arrayElements)
          return true;
       }
    }
  
    return false;
  }
  
  // Better
  function hasPairWithSum2(arr, sum){
    const mySet = new Set();
    const len = arr.length;
    for (let i = 0; i < len; i++){
      if (mySet.has(arr[i])) {
        return true;
      }
      mySet.add(sum - arr[i]);
    }
    return false;
  }
  [1,2,4,4]
  hasPairWithSum2([6,4,3,2,1,7], 9)