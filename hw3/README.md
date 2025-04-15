# Ralf Pacia - AMS326 HW \#3 Setup Guide
### AMS326 - Numerical Analysis, Spring 2025
### Professor Yuefan Deng

## Requirements
- A Windows, MacOS, or Linux environment is suitable for running my HW3 code (it is written in Python)
- Python 3 must be installed and properly configured on your system. For reference, my program runs on Python 3.12.6.
- numpy, shapely, and matplotlib must also be installed and properly configured on your system. To install numpy, run `pip install numpy` in a terminal window. To install shapely, run `pip install shapely` in a terminal window. To install matplotlib, run `pip install matplotlib` in a terminal window. The other libraries I use should already come preinstalled with Python 3.
- I recommend opening the `rpacia_ams326_hw3_p1.py`, `rpacia_ams326_hw3_p2.py`, and `rpacia_ams326_hw3_p3.py` files in a programming editor like VS Code, but it is also feasible to open from the command line (as long as you are `cd`-ed into the correct directory).

## Instructions
- Download the `hw3` folder into a destination folder of your choice, then `cd` into the `hw3` folder accordingly.
- Open a terminal window and ensure that you are in the `hw3` folder.
- It is certainly helpful if you have ran Python programs on your machine before. I have included generic instructions to run the program as well.

### Windows
- If you are on **Windows**, you can use the following command(s) to run the programs (please see the "Usage" section for more details): 

```
py rpacia_ams326_hw3_p1.py
py rpacia_ams326_hw3_p2.py <iterations>
py rpacia_ams326_hw3_p3.py
```

or

```
python rpacia_ams326_hw3_p1.py
python rpacia_ams326_hw3_p2.py <iterations>
python rpacia_ams326_hw3_p3.py
```

> NOTE: if you try to run the program using `python`, it must be properly configured as a PATH variable.
> If you are on a Windows machine, I recommend using the VS Code terminal or PowerShell to run the program using `py` instead.

### MacOS and Linux
- If you are on **MacOS or Linux**, you can use:
```
python3 rpacia_ams326_hw3_p1.py
python3 rpacia_ams326_hw3_p2.py <iterations>
python3 rpacia_ams326_hw3_p3.py
```

## Usage

### Problem 1
For problem 1, all you need to do is run the Python file. It should take under a minute, and the statistics are printed incrementally.
TODO: Need to add plotting.

### Problem 2
For problem 2, I used the Metropolis method for optimization with a default iteration count of `1_000_000`. You can also run the program with the optional `<iterations>` argument to specify a different number of iterations. For example, if you wanted to run the Metropolis method with `100_000` iterations instead, you can run `py rpacia_ams326_hw3_p2.py 100000`. If you don't want to specify an iteration count and just use the default iteration count, you can run `py rpacia_ams326_hw3_p2.py`. It may take around 10-15 minutes for the entire simulation to complete.
