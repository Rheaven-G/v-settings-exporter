// Main file of vSettingsExporter
// LIBRARIES

// MODULES
mod main_events;
mod file_manager;
mod behaviour_tweaker;

// CONSTANTS
pub(crate) const PNAME:&str = "vSetEx"; // Program name printed in terminal

fn main() {
    // run once
    main_events::start();

    // loop main events AKA: active program
    main_event_loop();

    // closing safely for smooth user experience
    safely_closing();
}


fn main_event_loop() { // Sync with user inputs

    let mut running:bool = true;

    // Main even loop
    while running {
        main_events::update();
        main_events::late_update();
    }
}

fn safely_closing() {
    println!("{PNAME}] Closed safely !");
}