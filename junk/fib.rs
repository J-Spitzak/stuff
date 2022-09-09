fn fib(n: i32) -> i32{
    if n == 1 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    fib(n-1) + fib(n-2)
}
fn main(){
    let x = fib(45);
    println!("{}", x);
}    
