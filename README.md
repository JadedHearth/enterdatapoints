## CSV-Script

A small python script to enter data points into a csv file.
Tested with Python 3.9.17 64-bit, MacOS Ventura 13.4.1(c).
Escape characters probably only work on *nix, not tested on Windows.

The configuration variables are defined as such at the start of the file:
```Java
HEADER = ["HeaderName1"] + ["HeaderName2"] + ["HeaderName3"] # (Any: list)
FILENAME = "table.csv" # (Any: string) Desired .csv filepath. Relative to where the script is being run from.
MUSTBENUMBER = True # (True | False) Enforce the entry of numbers.
```
