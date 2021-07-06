PMS_MOTOR_SUBCODES = {
    0: "No errors in the motor module",
    1: "The motor module could not be initialized",
    2: "An overcurrent is detected",
    3: "Internal error refer to DMC",
    4: "Wrong current: rated motor current is greater than max",
    5: "Wrong poles number (is odd)",
    6: "Wrong settings: rated motor voltage is too high in relation with the battery "
    "voltage capability. Check battery voltage set in autotuning menu. Load defaults "
    "and reparmetrize",
    7: "Internal error refer to DMC",
    8: "Internal error refer to DMC",
    9: "Sine signal is out of range: check connection and sensor",
    10: "Cosine signal is out of range: check connection and sensor",
    11: "No Hall sensor signals; check connection and sensor",
    12: "Unable to perform recalculation: motor calculated maximum speed exceeds "
    "500 Hz. Check motor parameters.",
    13: "Unable to perform recalculation: limit curves; check motor parameters "
    "(Ls, Ke, Fmax, Idemag) in auto tune menu.",
    14: "Unable to calculate controller gains: check motor parameters "
    "(Ls, Ke, Fmax, Idemag) and perform recalculation or do autotuning again.",
    15: "Internal error refer to DMC",
}

ERROR_CODES = {
    0: {"description": "No error", "subcodes": None},
    1: {"description": "N/A", "subcodes": None},
    2: {
        "description": "Voltage getting low",
        "subcodes": {
            1: "Battery voltage below absolute minimum",
            2: "Capacitor voltage below absolute minimum",
            3: "Battery voltage below LV cut back adjustment (drive cut back active)",
            4: "Capacitor voltage below LV cut back adjustment (drive cut back active)",
        },
    },
    3: {
        "description": "Inhibit drive/ BDI Cut / BLC via can",
        "subcodes": {
            1: "BDI Cut out (Battery below BDI cut Level)",
            2: "Pump inhibit input active (Only Pump Software)",
            3: "BCL via CAN message time out",
            4: "BCL via CAN message toggle security bit fail",
        },
    },
    4: {
        "description": "Voltage getting high",
        "subcodes": {
            1: "Battery voltage above absolute minimum",
            2: "Capacitor voltage above absolute minimum",
            3: "Battery voltage above minimum adjustment",
            4: "Capacitor voltage above minimum adjustment",
        },
    },
    5: {"description": "Motor temperature high", "subcodes": None},
    6: {"description": "Controller temperature high", "subcodes": None},
    7: {
        "description": "Adjustment out of range",
        "subcodes": {
            1: "Master does not share the line contactor but any one of the slave does",
            2: "Master shares the line contactor but one of the requested slave "
            "doesn’t",
            3: "A slave node number larger than last sharing node also share the line "
            "contactor",
            4: "WigWag is enabled but walkie is not",
            5: "inching and walkie are both enabled",
            6: "dual motor with speed control mode",
            7: "shared LC and Control Via CAN HMI both active",
            8: "Inching and Control Via CAN HMI both active",
            9: "Walkie and Control Via CAN HMI both active",
            10: "Control Via CAN HMI enabled and CAN node number set as master",
            11: "Hill hold Enabled and Torque control enabled",
            12: "---",
            13: "CAN control type options are active but Control Via CAN HMI is not "
            "enabled.",
            14: "Can Node ID via digital input enabled but control but Control Via CAN "
            "HMI is not enabled.",
            15: "means Shared Line Contactor HMI option is activated (“ShareLC”>=2) on "
            "but not control via CAN HMI active (CANMsgs>=4). Solution set "
            "CANMsgs < 4.",
            16: "Shared Line contactor HMI “master node” (“CAN node”) is higher/equal "
            "than last node (“LstNode”). This happens in the controller with the "
            "setting “ShareLC”=2 if “CAN node”>= “LstNode”, that is a non-sense. "
            "Solution: check node assignment, and make sure “CAN node” < “LstNode",
            17: "Shared Line contactor HMI “slave node” “CAN node”) is lower/equal "
            "than Shared Line contactor HMI “master” node (defined in “LstNode”). "
            "This happens in the controller with the setting “ShareLC”=3 if “CAN "
            "node”<= “LstNode”, that is a non- sense. Solution: check node "
            "assignment, and make sure “CAN node” > “LstNode”",
            "<999": "First digit: menu number, Last 2 digits: adjustment number within "
            "menu",
            999: "Power PCB doesn't match firmware",
        },
    },
    8: {"description": "Default adjustments used", "subcodes": None},
    9: {"description": "Memory chip fault", "subcodes": {">0": "Contact DMC"}},
    10: {"description": "Both forward and reverse inputs active", "subcodes": None},
    11: {"description": "Seat switch not closed or timed", "subcodes": None},
    12: {
        "description": "Power up sequence fault",
        "subcodes": {
            1: "Traction: FS1 switch active at power up",
            2: "Traction: Forward switch active at power up",
            3: "Traction: Reverse switch active at power up",
            4: "Pump: speed 1 or pump pot active at power up",
            5: "Pump: speed 2 active at power up",
            6: "Pump: speed 3 active at power up",
            7: "Pump: speed 4 active at power up",
            8: "Pump: speed 5 active at power up",
            9: "Inching: Forward switch active at power up",
            10: "Inching: Reverse switch active at power up",
            11: "Inhibit direction change fault",
            12: "CAN HMI Safety Stop 1 switch inactive fault",
        },
    },
    13: {
        "description": r"Accelerator more than 50% at power up",
        "subcodes": {
            1: "Normal accelerator type high at power up",
            2: "Wig-wag high at power up",
        },
    },
    14: {
        "description": "Inching sequence faults or belly switch active",
        "subcodes": {
            1: "Forward switch active when inching",
            2: "Reverse switch active when inching",
            3: "FS1 switch active when inching",
            4: "Seat switch active when inching",
            5: "Foot Brake switch active when inching",
            6: "Hand Brake active when inching",
            7: "Both inching buttons active when inching",
            8: "Inching buttons active when normal drive",
        },
    },
    15: {
        "description": "Supply voltage fault",
        "subcodes": {
            1: "+5 V supply voltage too low",
            2: "+5 V supply voltage too high",
            3: "+14 V supply voltage too low",
            4: "+14 V supply voltage too high",
        },
    },
    16: {"description": "N/A", "subcodes": None},
    17: {
        "description": "Battery voltage too low",
        "subcodes": {
            1: "Battery voltage below absolute minimum",
            2: "Capacitor voltage below absolute minimum",
            3: "Battery voltage below minimum adjustment",
            4: "Capacitor voltage below minimum adjustment",
        },
    },
    18: {
        "description": "High sided mosfets short circuit",
        "subcodes": {1: "M1 mosfets", 2: "M2 mosfets", 3: "M3 mosfets"},
    },
    19: {"description": "Motor stall protection", "subcodes": None},
    20: {
        "description": "Hardware over current detected",
        "subcodes": {
            1: "Positive overcurrent detected during initialization",
            2: "Negative overcurrent detected during initialization",
            3: "Positive overcurrent detected",
            4: "Negative overcurrent detected",
            ">4": "Contact DMC",
        },
    },
    21: {
        "description": "Contactor coil driver fault (e.g. short circuit)",
        "subcodes": {
            1: "Digital contactor output 1 short circuit during initialization",
            2: "Digital contactor output 1 short circuit at closing",
            3: "Digital contactor output 1 short circuit when closed",
            4: "Digital contactor output 2 short circuit during initialization",
            5: "Digital contactor output 2 short circuit at closing",
            6: "Digital contactor output 2 short circuit when closed",
            7: "Digital contactor output 3 short circuit during initialization",
            8: "Digital contactor output 3 short circuit at closing",
            9: "Digital contactor output 3 short circuit when closed",
            10: "Digital output 4 short circuit during initialization",
            11: "Digital output 4 short circuit at closing",
            12: "Digital output 4 short circuit when closed",
            13: "Unknow fault",
        },
    },
    22: {
        "description": "Voltage is too high",
        "subcodes": {
            1: "Battery voltage above absolute maximum",
            2: "Capacitor voltage above absolute maximum",
            3: "Battery voltage above maximum adjustment",
            4: "Capacitor voltage above maximum adjustment",
        },
    },
    23: {
        "description": "Low sided mosfets short circuit in neutral",
        "subcodes": {1: "M1 mosfets", 2: "M2 mosfets", 3: "M3 mosfets"},
    },
    24: {
        "description": "Hardware fail safe fault",
        "subcodes": {
            1: "Cannot finish checking the hardware fail safe",
            2: "Hardware fail safe feedback is low at startup",
            3: "Hardware fail safe feedback is high during toggling",
            4: "Hardware fail safe feedback is low after toggling stops",
            5: "Hardware fail safe encountered an unknown error",
            6: "Hardware fail safe is not alive during normal run",
            7: "Main loop is stuck",
            8: "Software watchdog caused a reset. Recalculation is disabled now!",
        },
    },
    25: {
        "description": "Line contactor fault (e.g. short circuit)",
        "subcodes": {
            1: "Could not discharge the capacitor bank",
            2: (
                "Capacitor bank dit not charge sufficiently to safely close the line "
                "contactor"
            ),
            3: "Line contactor opened inadvertently",
        },
    },
    26: {
        "description": "Thermal shutdown fault (only for minimum pump speed fault)",
        "subcodes": {1: "Pump thermal shutdown", 2: "Pump low voltage shotdown"},
    },
    27: {
        "description": "Low sided mosfets short circuit during power up and before "
        "line contactor is closed",
        "subcodes": {1: "M1 mosfets", 2: "M2 mosfets", 3: "M3 mosfets"},
    },
    28: {
        "description": "Wire off detected",
        "subcodes": {
            1: "Quadrature encoder sensor wire off or noise detected (AC only)",
            2: "5 V supply wire off detected",
            3: "0 V supply wire off detected",
            4: "Wig-wag out of safety range",
            5: "Motor Temperature Sensor wire off",
        },
    },
    29: {
        "description": "CAN node fault",
        "subcodes": {
            1: "shared Line Contactor slave time out fault",
            2: "shared Line Contactor Master fails to broadcast to slaves",
            3: "shared Line Contactor requested slave is not found by master",
            4: "shared Line Contactor master time out fault",
            5: "Control Via CAN HMI timeout (not receive CAN Drive Command Message "
            "from VCU)",
            6: "Control Via CAN HMI security bit error (VCU fails to toggle security "
            "bit)",
            7: "Control Via CAN HMI enable switch/wire is not connected",
            13: "Can Node ID via digital inputs is detected to 0, check input status",
        },
    },
    30: {
        "description": "Motor overspeeding",
        "subcodes": {
            1: r"Motor speed is too high to commence safe pulsing (speed is > 80 % of "
            "maximum motor speed)",
            2: "Motor speed is higher than absolute maximum speed (Check Absolute "
            "Maximum Speed)",
        },
    },
    31: {"description": "Motor fault", "subcodes": PMS_MOTOR_SUBCODES},
    32: {
        "description": "Motor Module initialization error",
        "subcodes": PMS_MOTOR_SUBCODES,
    },
    33: {
        "description": "Motor Module configuration inconsistency",
        "subcodes": PMS_MOTOR_SUBCODES,
    },
    34: {
        "description": "Motor Module parameter inconsistency",
        "subcodes": PMS_MOTOR_SUBCODES,
    },
    35: {
        "description": "Current sensor calibration fault",
        "subcodes": {
            1: "Could not initialize the calibration",
            2: "Time out during calibration",
        },
    },
    36: {"description": "Controller temperature over 100 degree", "subcodes": None},
    39: {
        "description": "Generic time out",
        "subcodes": {
            1: "Time out on configuration upload",
            2: "Time out on getting stable inputs",
            3: "Time out on motor ready",
        },
    },
    40: {
        "description": "System Fault",
        "subcodes": {">0": 'Contact DMC (see also table "System Codes")'},
    },
}
