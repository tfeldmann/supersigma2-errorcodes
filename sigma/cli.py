import argparse

from .parser import code_to_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "code", nargs="*", help='A DMC SuperSigma2 error code, e.g. "12.2"'
    )

    args = parser.parse_args()
    if args.code:
        # print results for all given codes
        for code in args.code:
            print(code_to_string(code))
    else:
        # interactive mode
        while True:
            try:
                inp = input("Enter supersigma 2 error code: ")
                if not inp:
                    break
                print(code_to_string(inp))
            except KeyboardInterrupt:
                break
