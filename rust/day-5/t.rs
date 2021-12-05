fn main() {
    println!("hi");
    let r = (0..10).step_by(2);
    let s = (5..0).step_by(!1);
    for (x, y) in r.zip(s) {
        println!("{} {}", x, y);
    }
}