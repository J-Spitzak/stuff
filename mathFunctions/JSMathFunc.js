function trunkate(full,trunk) {
    if (trunk >= 0){
        full = full.toString();
        full = [...full]; 
        var value = 0;
    
        for (var i = 0; i < full.length; i++) {
        if(full[i] == ".") {
            value = i;
            }
        }
        value = value + trunk;
        var round = full[value + 1];
        var x = parseInt(full[value]) + 1;
        if(parseInt(round) >= 5) {
        full[value] = x.toString();  
        }
        
        full.splice(value + 1,full.length);  
        full = full.join("");
    
        return parseFloat(full);
    }
    else{
        return NaN
    }
  }

function absval(val, root = 0){
    if (val >= root){
        return val - root;
    }
    else{
      return root - val;
    }
}

function linear(val, low, high){
    val = val - low;
    high = high - low;
    return val / high;
}

function max(numbs){
    let max = numbs[0];
    for(var i = 0;i < numbs.length;i++){
        if (i > max){
            max = i;
        };
    }
    return max;
}

/*
function min(numbs){
    var min = null
    for (var i = 0;i < numbs.length;i++){
        if (min == null){
            min = i;
        };
        elif (i < min){
            min = i;
        };
    return min;
    };
}*/

function mean(numbs, int = False){
    sum = 0
    for (var i = 0;i < numbs.length; i++){
        sum += i;
    }
    if (int == False){
        return sum / len(numbs);
    }
    if (int == True){
        return Math.floor(sum / len(numbs));
    }
}

function mode(numbs){
    var dict = {};
    for (var i = 0; i < numbs.length; i++){
        if (dict.includes(numbs[i])){
            dict[i] += 1;
        }    
        else{
            dict[i] = 1;
        }
    }
    //dict is now a dictionary with all of the numbers provided and a corresponding
    //value saying how many times it appears 
    var values = []; //all of the numbers
    var number = []; // the numbers of each number (parrallel lists)
    for (var i = 0; i < dict.length;i++){//key in dict:
       values.append(dict[key]);
       number.append(key);
    }
}