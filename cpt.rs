fn scalar(vector: Vec<i32>,factor: i32){
    let mut final_vec :Vec<i32>;
    for number in vector{
        final_vec.append(number * factor);
    }
    return final_vec;
}

fn main() {
    println!("{}", scalar([2,2],5));
}