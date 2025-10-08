use std::env;

use crate::behaviour_tweaker;

pub(crate) fn get_os() {
    println!("Current OS detected {}", env::consts::OS);
}