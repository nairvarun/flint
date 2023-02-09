use std::fs::{self, File};

pub fn setup() -> std::io::Result<()> {
    fs::create_dir("/some/dir").unwrap();
    File::create("./log/log.json").unwrap();
    Ok(())
}

// pub fn create_logdir() -> std::io::Result<()> {
//     fs::create_dir("./log")?;
//     Ok(())
// }

// pub fn create_logfile()  -> std::io::Result<()> {
//     File::create("./log/log.json")?;
//     Ok(())
// }


// fn _old_create_logdir() {
//     match fs::create_dir("./log") {
//         Ok(_) => (),
//         Err(e) => match e.kind() {
//             ErrorKind::AlreadyExists => (),
//             ErrorKind::PermissionDenied => {
//                 eprintln!("Error: {e}");
//                 exit(1);
//             },
//             ErrorKind::NotFound => {
//                 eprintln!("Error: {e}");
//                 exit(1);
//             },
//             _ => {
//                 eprintln!("Error: {e}");
//                 exit(1);
//             },
//         }
//     }
// }

// fn _old_create_logfile() {
//     match File::create("./log/log.json") {
//         Ok(_) => (),
//         Err(e) => {
//             eprintln!("Error: {e}");
//             exit(1);
//         }
//     }
// }
