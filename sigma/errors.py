"""
Error codes taken from manual
SuperSigma2 PMS Manual V1.0 (SW V02.10.00).pdf
"""

PMS_MOTOR_SUBCODES = {
    0: "No errors in the motor module.",
    1: "The motor module could not be initialized. Load Default Parameter and key cycle",
    2: "An motor overcurrent is detected. Check if motor tuned properly, check motor wiring (lack of isolation)..",
    3: "Internal error refer to DMC",
    4: "Wrong current setup: current for Autotuning is set greater than maximum current. Check current setup in tha autotuning menu.",
    5: "Wrong number of motor poles. An odd number has been set to Nof motor poles in the autotuning menu.",
    6: "Internal error refer to DMC",
    7: "Internal error refer to DMC",
    8: "Sine signal is out of range: check sin cos sensor wiring, sensor supply and sensor",
    9: "Cosine signal is out of range: check sin cos sensor wiring, sensor supply and sensor",
    10: "No Hall sensor signals; check hall sensor wiring.",
    11: "Number of motor poles and sin cos sensor number of teeth (poles) are not consistent. The ratio between number of motor poles and sin cos sensor number of teeth must me a integer.",
    12: "Unable to perform recalculation: motor calculated maximum speed exceeds maximum allowed frequency. Check motor parameters. If parameters are right, reduce battery voltage in the autotuning menu and recalculate.",
    13: "Unable to recalculate controller gains: check motor parameters (Ls, Ke, Fmax, Idemag) and perform recalculation or do autotuning again.",
    14: "Unable to recalculate: base frequency too low. Check settings in autotuning menu (Ls, Ke, Fmax, V battery Idemag), if they are right Reduce maximum current in the autotuning menu and recalculate.",
    15: "Unable to recalculate: demag current not enough, Increase if possible Idemag, or reduce Fmax. This error occur if field weakening option is selected by using a Idemag current greater than 1 A.",
    16: "Unable to recalculate limit curves: reduce max frequency in autotuning menu and recalculate",
    17: "Unable to recalculate limit curves: reduce max current and or battery voltage too low for the motor, and recalculate",
    18: "Unable to recalculate limit curves: reduce max frequency, reduce max current and recalculate.",
    19: "Internal error refer to DMC",
}


ERRORS = {
    0: {
        "description": "No error",
        "subcodes": None,
    },
    1: {
        "description": "N/A",
        "subcodes": None,
    },
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
            3: "Battery voltage above High Voltage cut back adjustment (brake cut back active)",
            4: "Capacitor voltage above High Voltage cut back adjustment (brake cut back active)",
        },
    },
    5: {
        "description": "Motor temperature high",
        "subcodes": None,
    },
    6: {
        "description": "Controller temperature high",
        "subcodes": None,
    },
    7: {
        "description": "Adjustment out of range",
        "subcodes": {
            1: "Master does not share the line contactor but any one of the slave does",
            2: "Master shares the line contactor but one of the requested slave doesn’t",
            3: "A slave node number larger than last sharing node also share the line contactor",
            4: "WigWag is enabled but walkie is not",
            5: "inching and walkie are both enabled",
            6: "dual motor with speed control mode",
            7: "shared LC and Control Via CAN HMI both active",
            8: "Inching and Control Via CAN HMI both active",
            9: "Walkie and Control Via CAN HMI both active",
            10: "Control Via CAN HMI enabled and CAN node number set as master",
            11: "Hill hold Enabled and Torque control enabled",
            12: "---",
            13: "CAN control type options are active but Control Via CAN HMI is not enabled.",
            14: "Can Node ID via digital input enabled but control but Control Via CAN HMI is not enabled.",
            15: "means Shared Line Contactor HMI option is activated (“ShareLC”>=2) on but not control via CAN HMI active (CANMsgs>=4). Solution set CANMsgs < 4.",
            16: "Shared Line contactor HMI “master node” (“CAN node”) is higher/equal than last node (“LstNode”). This happens in the controller with the setting “ShareLC”=2 if “CAN node”>= “LstNode”, that is a non-sense. Solution: check node assignment, and make sure “CAN node” < “LstNode",
            17: "Shared Line contactor HMI “slave node” “CAN node”) is lower/equal than Shared Line contactor HMI “master” node (defined in “LstNode”). This happens in the controller with the setting “ShareLC”=3 if “CAN node”<= “LstNode”, that is a non- sense. Solution: check node assignment, and make sure “CAN node” > “LstNode”",
            18: "Wrong node number for master controller: make sure DM master has node nr = 0 (if CAN DMC protocol) or < 14 (if CAN Open Compatible protocol)",
            19: "Wrong node number for slave controller: make sure DM slave has node nr = 1 (if CAN DMC protocol) or > 1 (if CAN Open Compatible protocol)",
            20: "Dual Motor setting not consistent between controller pair. Make sure parameter “M3-17 Dual Motor Option” form an admissible pair between controllers (Master 1 / Slave 2, Master 4 / Slave 5, Master 6 / Slave 7, Master 8, Slave 9).",
            21: "Dual Motor and Contol Via CAN both active (it is possible to have them both active on controllers with CAN Open Compatible protocol)",
            22: "Safe Stop 1 and CAN node ID Via digital Inputs not compatible",
            23: "PC interface request controller to stop giving power to the motor",
            24: "Dual Motor and Walkie both enable. Walkie option is compatible only with Dual Motor modes 4/5, 6/7 and 8/9.",
            25: "Dual Motor and Inching both enabled. Inching option is compatible only with Dual Motor modes 1/2 (in speed mode), 4/5, 6/7, 8/9.",
            26: "Dual Motor and AI2/3 configuration not admissible. AI3 can not be configured differently from “steerpot” (parameter “M3- 38T AI3 configuration” set to 0) if Dual Motor modes 1, 2 or 3 are selected. AI2 can not be configured differently from “brakepot” (parameter “M3- 37T AI2 configuration” set to 0) if Dual Motor modes 1, 2, 6, 7, 8 or 9 are selected.",
            27: "---",
            28: "---",
            29: "---",
            30: "---",
            31: "Parameter “M3-8 RideOn, Walkie, E-Vehicle” not consistent between two controllers. Make sure both Dual Motor Controllers have the same setting (only for Dual Motor modes 1/2 and 4/5).",
            32: "Parameter “M3-5 DI5/6 configuration” not consistent between two controllers. Make sure both Dual Motor Controllers have the same setting (only for Dual Motor modes 1/2 and 4/5).",
            33: "Parameter “M3-8 RideOn, Walkie, E-Vehicle” or “M3-5 DI5/6 configuration” set different from 0 in Dual Motor Slave mode 5. Make sure those parameters are set to 0 in the Dual Motor controller Slave mode 5. Those options only have to be selected in Dual Motor Master mode 4.",
            34: "Dual Motor Slave mode 5 with failure option active (parameter “M3-18 Failure option” different from 0) when Dual Motor Master mode 4 has parameter “M3-8 RideOn, Walkie, E-Vehicle” or “M3-5 DI5/6 configuration” set different from 0. Either disable Slave failure option (set parameter “M3-18 Failure option” different from 0) or disable Master functions (parameters “M3-8 RideOn, Walkie, E-Vehicle” or “M3- 5 DI5/6 configuration” both set to 0).",
            35: "Shared Line contactor and Dual Motor failure option both enabled. Disable Shared Line Contactor (parameter “M9-4 Shared Line Contactor” set to 0) or Failure option (parameter “M3-18 Failure option” set to 0).",
            36: "DI 5/6 configuration is not compatible with the selected Control Via CAN control mode selected.",
            37: "Dual motor mode 1/2 and E-Vehicle function both enabled. Set parameter “M3-8 RideOn, Walkie, E-Vehicle” different from 3",
            38: "Selected control mode not compatible with selected Dual Motor option",
            39: "Two or more controllers acting as “Display master”. Tune the Controllers to have only one “Display master”. Refer to “ M3-6 Display Status Field “DispInfo”” for details.",
            40: "Parameter “M3-37T AI2 configuration” or “M3-38T AI3 configuration” not consistent between two controllers pair. Set “M3-37T AI2 configuration” and “M3-38T AI3 configuration” consistent between controllers",
            41: "Inching and e-vehicle both enabled",
            42: "Control Via CAN and e-vehicle both enabled",
            43: "Speed control mode and e-vehicle both enabled",
            44: "Wrong setup of custom motor temperature mapping",
            45: "---",
            46: "---",
            47: "Control Via CAN Open configuration not consistent between controllers pair. Make sure both controllers are setup with the same method (“M9-3 CAN message” must be set both lower than 4 if “Control Via CAN Open Compatible” is desired, or both greater or equal than 4 if “wired control” is desired) and both controllers have the same control type (parameter “M9-6 CAN control type” must have the same values)",
            48: "Selected CAN control mode not compatible with selected Dual Motor option",
            49: "EM brake settings not consistent between controllers pair. Make sure both controllers are setup with the same EM brake settings",
            50: "EM brake setting and control mode not compatible: not possible to set the EM brake not to close at high speed when a fault occurs in a speed- control mode application",
            51: "Control Via CAN active and AI2/AI3 configured different than “Brake Pot”/”Steer Pot”",
            lambda x: (
                100 <= x < 999
            ): "First digit: menu number, Last 2 digits: adjustment number within menu",
            999: "Power PCB doesn't match firmware",
        },
    },
    8: {
        "description": "Default adjustments used",
        "subcodes": None,
    },
    9: {
        "description": "Memory chip fault",
        "subcodes": {
            lambda x: x > 0: "Contact DMC",
        },
    },
    10: {
        "description": "Both forward and reverse inputs active",
        "subcodes": None,
    },
    11: {
        "description": "Drive not allowed",
        "subcodes": {
            0: "Ride-on: Seat switch not closed or timed out. Walkie: Tiller switch not closed",
            2: "Timed Speed Limit 3 time out",
        },
    },
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
    16: {
        "description": "N/A",
        "subcodes": None,
    },
    17: {
        "description": "Battery voltage too low",
        "subcodes": {
            1: "Battery voltage below Low Voltage absolute minimum",
            2: "Capacitor voltage below Low Voltage absolute minimum",
            3: "Battery voltage below Low Voltage error adjustment",
            4: "Capacitor voltage below Low Voltage error adjustment",
        },
    },
    18: {
        "description": "High sided mosfets short circuit",
        "subcodes": {
            1: "M1 mosfets",
            2: "M2 mosfets",
            3: "M3 mosfets",
        },
    },
    19: {
        "description": "Motor stall protection",
        "subcodes": None,
    },
    20: {
        "description": "Hardware over current detected",
        "subcodes": {
            1: "Positive overcurrent detected during initialization",
            2: "Negative overcurrent detected during initialization",
            3: "Positive overcurrent detected",
            4: "Negative overcurrent detected",
            lambda x: x > 4: "Contact DMC",
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
        "description": "Battery voltage too high",
        "subcodes": {
            1: "Battery voltage above High Voltage absolute maximum",
            2: "Capacitor voltage above High Voltage absolute maximum",
            3: "Battery voltage above High Voltage error adjustment",
            4: "Capacitor voltage above High Voltage error adjustment",
        },
    },
    23: {
        "description": "Low sided mosfets short circuit in neutral",
        "subcodes": {
            1: "M1 mosfets",
            2: "M2 mosfets",
            3: "M3 mosfets",
        },
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
            2: "Capacitor bank dit not charge sufficiently to safely close the line contactor",
            3: "Line contactor opened inadvertently",
        },
    },
    26: {
        "description": "Thermal shutdown fault (only for minimum pump speed fault)",
        "subcodes": {
            1: "Pump thermal shutdown",
            2: "Pump low voltage shotdown",
        },
    },
    27: {
        "description": "Low sided mosfets short circuit during power up and before line contactor is closed",
        "subcodes": {
            1: "M1 mosfets",
            2: "M2 mosfets",
            3: "M3 mosfets",
        },
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
            5: "Control Via CAN HMI timeout (not receive CAN Drive Command Message from VCU)",
            6: "Control Via CAN HMI security bit error (VCU fails to toggle security bit)",
            7: "Control Via CAN HMI enable switch/wire is not connected",
            8: "Dual Motor master/slave timeout, node not responding",
            9: "Dual Motor master/slave not receiving messages",
            10: "Other controller in fault",
            11: "Can Node ID via digital inputs is detected to 0, check input status",
            20: "Shared Line Contactor Master hard failure recognised by Slave",
            21: "Shared Line Contactor Slave hard failure recognised by Master",
        },
    },
    30: {
        "description": "Motor overspeeding",
        "subcodes": {
            1: r"Motor speed is too high to commence safe pulsing (speed is > 80 % of maximum motor speed)",
            2: "Motor speed is higher than absolute maximum speed (Check Absolute Maximum Speed)",
        },
    },
    31: {
        "description": "Motor fault",
        "subcodes": PMS_MOTOR_SUBCODES,
    },
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
    36: {
        "description": "Controller temperature over 100 degree",
        "subcodes": None,
    },
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
        "subcodes": {
            lambda x: x > 0: "Internal system error Contact DMC",
        },
    },
}
