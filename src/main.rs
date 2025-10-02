// Main file of vSettingsExporter
const PNAME:&str = "vSetEx"; // Program name printed in terminal

fn main() {
    // We do everything we need to before starting the program
    println!("{PNAME}] Starting !");

    // We then start the program and its event loop
    main_event_loop();

    safely_closing();
}

fn main_event_loop() {
    let mut running:bool = true;

    let mut count:u32 = 5;

    // Main even loop
    while running {
        println!("{PNAME}] {count}...");


        if count > 0 {
            count = count - 1;
        }
        else {
            running = false;
        }
    }
}

fn safely_closing() {
    println!("{PNAME}] Closed safely !");
}