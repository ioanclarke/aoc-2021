fn main() {
    let s = "Hello";
    let x: fn<T, T, F>(&T, &T, &F) -> &T = std::cmp::max_by_key;
    print_type_of(&x);
    print_type_of(&s);
}
    
fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}