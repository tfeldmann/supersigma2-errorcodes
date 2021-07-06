# supersigma2-errorcodes

A python parser for DMC SuperSigma2 error codes.

## Installation

Needs Python >= 3.6.

Install using `pip`:

```
pip install supersigma2-errorcodes
```

If you only need the standalone `sigma`-script to parse error codes in the command line,
it is recommended to use `pipx` for the installation:

```
pipx install supersigma2-errorcodes
```

## Command line usage

A `sigma` command line script is installed by pip which can be used like this:

```shell
$ sigma 13.2 18.3 19.2
[13.2] Accelerator more than 50% at power up: Wig-wag high at power up
[18.3] High sided mosfets short circuit: M3 mosfets
[19] Motor stall protection
```

If no error codes are given, the usage is interactive.

## Library usage

```python
from sigma import code_to_string

code_to_string("12.2")
>>> "[12.2] Power up sequence fault: Traction: Forward switch active at power up"

code_to_string("18.3", include_code=False)
>>> "High sided mosfets short circuit: M3 mosfets"
```
