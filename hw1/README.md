# Ralf Pacia - AMS326 HW \#1 Setup Guide
### AMS326 - Numerical Analysis, Spring 2025
### Professor Yuefan Deng

## Requirements
- A Windows, MacOS, or Linux environment is suitable for running my HW1 code (it is written in Python)
- Python 3 must be installed and properly configured on your system. For reference, my program runs on Python 3.12.6.
- numpy must also be installed and properly configured on your system. To install numpy, run `pip install numpy` in a terminal window. The other libraries I use should already come preinstalled with Python 3.
- I recommend opening the `rpacia_ams326_hw1_p1.py` and `rpacia_ams326_hw1_p2.py` files in a programming software like VS Code, but it is also feasible to open from the command line (as long as you are `cd`-ed into the correct directory).

## Instructions
- Download the `hw1` folder into a destination folder of your choice, then `cd` into the `hw1` folder accordingly.
- Open a terminal window and ensure that you are in the hw1 folder.
- It is certainly helpful if you have ran Python programs on your machine before. I have included generic instructions to run the program as well.

### Windows
- If you are on **Windows**, you can use the following command(s) to run the program **with the methods of your choice** for problems 1 and 2 (please see the "Usage" section for more details): 

```
py rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo
py rpacia_ams326_hw1_p2.py polynomial|quadratic
```

or

```
python rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo
python rpacia_ams326_hw1_p2.py polynomial|quadratic
```

> NOTE: if you try to run the program using `python`, it must be properly configured as a PATH variable.
> If you are on a Windows machine, I recommend using the VS Code terminal or PowerShell to run the program using `py` instead.

### MacOS and Linux
- If you are on **MacOS or Linux**, you can use:
```
python3 rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo
python3 rpacia_ams326_hw1_p2.py polynomial|quadratic
```

## Usage
As you may have noticed, I had configured my program to parse command line arguments.

### Problem 1
For problem 1, if you want to run the bisection method, for example, you can run `py rpacia_ams326_hw1_p1.py bisect` (or similarly, using `python3` if you are not on Windows). If you want to run Newton's method, you can run `py rpacia_ams326_hw1_p1.py newton`. Similarly, you can also run it with the `secant` and `monte_carlo` arguments to run the secant and Monte Carlo methods, respectively. Note that only one method can be run at a time.

### Problem 2
Similarly, for problem 2, if you want to run the polynomial interpolation, you can run `py rpacia_ams326_hw1_p2.py polynomial`. If you want to run the quadratic fit, you can run `py rpacia_ams326_hw1_p2.py quadratic`. Note that only one method can be run at a time.