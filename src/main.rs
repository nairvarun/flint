use sha2::{Digest, Sha256};
use std::{
    fs::File,
    io::{self, Write, BufRead, BufReader, Read, BufWriter},
    str::Bytes,
};

fn main() {
    let vals: Vec<_> = vec![00, 99, 21];

    println!("read/write/proof");

    let mut input = String::new();

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            let trimmed_input = input.trim();
            match trimmed_input {
                "read" => {
                    let file = File::open("store.bin").expect("failed to read");
                    let mut reader = BufReader::new(file);
                    let mut buffer = vec![];
                    reader
                        .read_to_end(&mut buffer)
                        .expect("failed to read");
                    // println!("{:?}", reader);
                    dbg!(reader);
                },
                "write" => {
                    let file = File::create("store.bin").expect("failed to write");
                    let mut writer = BufWriter::new(file);
                    writer
                        .write_all(vals.as_slice())
                        .expect("failed to write");
                },
                "proof" => println!("p"),
                _ => println!("999"),
            }
        },
        Err(error) => println!("error: {error}"),
    }

    // let hash = Sha256::digest(vals);

    // let mut file = File::create("hashfile").expect("failed to create file");
    // file.write_all(&hash).expect("failed to write file");
}
