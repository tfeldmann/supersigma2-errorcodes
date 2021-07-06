import re
from .errors import ERROR_CODES

# https://regex101.com/r/HMNQQ4/1
ERROR_CODE_REGEX = re.compile(r"^(\d+)(?:[\.\-\,\s](\d+))?$")

SEVERITY = {
    1: {
        "category": "Controller warning fault",
        "effect": "Reduces only performance",
        "to_reset": "Fault will reset itself (if possible)",
    },
    2: {
        "category": "Drive error fault",
        "effect": "Commences graceful neutral brake",
        "to_reset": "Requires a neutral recycle action to reset fault",
    },
    3: {
        "category": "Soft error fault",
        "effect": "Immediately stops pulsing",
        "to_reset": "Requires a neutral recycle action to reset fault",
    },
    4: {
        "category": "Hard error fault",
        "effect": "Immediately stops giving power to the motor and open line contactor",
        "to_reset": "Reset only by a key switch recycle",
    },
}


def code_to_string(code: str):
    try:
        return translate(*parse_code(code))
    except Exception as e:
        return "Parsing error (%s)" % e


def parse_code(code: str):
    """
    Splits a error code in the form of "12.2" into its components ("12", "1").
    If no subcode is found, the second item in the tuple is None.
    Raises a ValueError if the code is invalid.
    """
    match = ERROR_CODE_REGEX.match(code.strip())
    if not match:
        raise ValueError("Invalid error code %s" % code)
    return match.groups()


def descriptions(code, subcode=None):
    code, subcode = int(code), int(subcode) if subcode else None

    # get fault_code
    try:
        entry = ERROR_CODES[code]
        fault_msg = entry["description"]
        subdict = entry["subcodes"]
    except KeyError:
        return "<unknown>", ""

    if subdict is None or subcode is None:
        return fault_msg, ""

    # get sub fault code
    try:
        subfault_msg = subdict[subcode]
        return fault_msg, subfault_msg
    except KeyError:
        # try special cases
        for key in subdict.keys():
            if callable(key) and key(subcode):
                return fault_msg, subdict[key]
        return fault_msg, "<unknown>"


def translate(code: int, subcode=None, *, include_code=True):
    fault_msg, sub_msg = descriptions(code, subcode)

    if include_code:
        if subcode and sub_msg:
            return "[%s.%s] %s: %s" % (code, subcode, fault_msg, sub_msg)
        return "[%s] %s" % (code, fault_msg)

    if subcode and sub_msg:
        return "%s: %s" % (fault_msg, sub_msg)
    return fault_msg
