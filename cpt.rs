fn scalar(vector: Vec<i32>,factor: i32) -> Vec<i32>{
    let mut final_vec = Vec::new();
    for number in vector{
        final_vec.push(number * factor);
    }
    return final_vec;
}

fn main() {
    let new_vector : Vec<i32> = scalar([2,2,5,1,9,38].to_vec(),10);
    for number in new_vector{
        println!("{}", number);
    }

}