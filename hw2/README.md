# Ralf Pacia - AMS326 HW \#2 Setup Guide
### AMS326 - Numerical Analysis, Spring 2025
### Professor Yuefan Deng

## Requirements
- A Windows, MacOS, or Linux environment is suitable for running my HW2 code (it is written in Python)
- Python 3 must be installed and properly configured on your system. For reference, my program runs on Python 3.12.6.
- numpy must also be installed and properly configured on your system. To install numpy, run `pip install numpy` in a terminal window. The other libraries I use should already come preinstalled with Python 3.
- I recommend opening the `rpacia_ams326_hw2_p1.py` and `rpacia_ams326_hw2_p2.py` files in a programming editor like VS Code, but it is also feasible to open from the command line (as long as you are `cd`-ed into the correct directory).

## Instructions
- Download the `hw2` folder into a destination folder of your choice, then `cd` into the `hw2` folder accordingly.
- Open a terminal window and ensure that you are in the `hw2` folder.
- It is certainly helpful if you have ran Python programs on your machine before. I have included generic instructions to run the program as well.

### Windows
- If you are on **Windows**, you can use the following command(s) to run the program **with the methods of your choice** for problem 1 and problem 2 (please see the "Usage" section for more details): 

```
py rpacia_ams326_hw2_p1.py rectangle|trapezoid
py rpacia_ams326_hw2_p2.py
```

or

```
python rpacia_ams326_hw2_p1.py rectangle|trapezoid
python rpacia_ams326_hw2_p2.py
```

> NOTE: if you try to run the program using `python`, it must be properly configured as a PATH variable.
> If you are on a Windows machine, I recommend using the VS Code terminal or PowerShell to run the program using `py` instead.

### MacOS and Linux
- If you are on **MacOS or Linux**, you can use:
```
python3 rpacia_ams326_hw2_p1.py rectangle|trapezoid
python3 rpacia_ams326_hw2_p2.py
```

## Usage
As you may have noticed, I had configured my program to parse command line arguments for problem 1.

### Problem 1
For problem 1, if you want to run the rectangle method, for example, you can run `py rpacia_ams326_hw2_p1.py rectangle` (or similarly, using `python3` if you are not on Windows). If you want to run the trapezoid method, you can run `py rpacia_ams326_hw2_p1.py trapezoid`. Note that only one method can be run at a time.

### Problem 2
For problem 2, all you need to do is run the file using `py rpacia_ams326_hw2_p2.py` (or similarly, using `python3` if you are not on Windows) because I only implemented Gaussian elimination for solving Ax = b.