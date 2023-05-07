






function firstRC(arr){
    temp_arr = []
    for (let i = 0; i < arr.length; i++){
        if(temp_arr.includes(arr[i])){
            return arr[i];
        }else{
            temp_arr.push(arr[i])
        }
    }
}