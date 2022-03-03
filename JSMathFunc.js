function trunkate(full,trunk) {
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