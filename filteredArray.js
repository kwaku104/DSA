function filteredArray(arr, elem) {
    let newArr = [];
    // Only change code below this line
    for(var i = 0; i < arr.length; i++){
      if(arr[i].indexOf(elem) == -1){
        console.log(arr[i].indexOf(elem));
        newArr.push(arr[i]);
        console.log()
      }
    }
    // Only change code above this line
    return newArr;
  }
  
  console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 1));