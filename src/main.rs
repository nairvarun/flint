pub struct BinaryTree<T> {
    pub velue: T,
    pub left: Option<Box<BinaryTree<T>>>,
    pub right: Option<Box<BinaryTree<T>>>,
}

fn main() {
    println!("Hello, world!");
}
