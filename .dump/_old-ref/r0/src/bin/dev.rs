use std::fs::{self, File};
use std::io::{ErrorKind};
use std::process::exit;

fn mmain() -> std::io::Result<()> {
    fs::create_dir("/some/dir")?;
    Ok(())
}


pub fn create_logdir() {
    match fs::create_dir("./log") {
        Ok(_) => (),
        Err(e) => match e.kind() {
            ErrorKind::AlreadyExists => (),
            ErrorKind::PermissionDenied => {
                eprintln!("Error: {e}");
                exit(1);
            },
            ErrorKind::NotFound => {
                eprintln!("Error: {e}");
                exit(1);
            },
            _ => {
                eprintln!("Error: {e}");
                exit(1);
            },
        }
    }
}

pub fn create_logfile() {
    match File::create("./log/log.json") {
        Ok(_) => (),
        Err(e) => {
            eprintln!("Error: {e}");
            exit(1);
        }
    }
}

fn main() {
    create_logdir();
    create_logfile();
}
