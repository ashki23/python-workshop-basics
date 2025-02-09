# Python Basics: A Beginner's Guide to Programming

*A workshop for **Mentoring Math Minds** program at Saint Louis University.*

The workshop is designed to introduce the fundamentals of Python programming in an engaging and interactive way. Participants will learn key concepts such as variables, data types, basic operations, and control flow structures like loops and conditional statements. They will also explore essential data structures such as lists and dictionaries, and understand how to write reusable code using functions. The workshop includes hands-on exercises and a mini-project. By the end of the session, participnets will have the foundational skills to start coding confidently and continue exploring Python independently.

### **Main topics**  
1. **Introduction to Python**: Why Python, setting up the environment.  
2. **Variables and Data Types**: Strings, integers, floats, booleans.  
3. **Input/Output and Basic Operations**: User input, print statements, arithmetic, and comparisons.  
4. **Control Flow**: `if`, `else`, and `elif` statements.  
5. **Loops**: `for` and `while` loops.  
6. **Data Structures**: Lists and dictionaries.  
7. **Functions**: Defining, using parameters, and return values.  
8. **Debugging**: Identifying and fixing common programming errors.  
9. **Generative AI**: A brief introduction to leveraging AI tools like ChatGPT to assist with coding and problem-solving.  
10. **Mini-Project**: Practical application of learned concepts.

## Setup the environment

### Install Python  
To install the latest version of Python on your system, follow these instructions:  
- **Linux**: Python is typically preinstalled on most Linux distributions.
- **Cloud**: Since most cloud platforms run on Linux, Python is typically preinstalled.
- **macOS**: Follow [section 5.1.1](https://docs.python.org/3/using/mac.html#installation-steps). Alternatively, if you have a package manager like [Homebrew](https://brew.sh), you can use it to install Python. 
- **Windows**: Refer to [section 4.1.1](https://docs.python.org/3/using/windows.html#installation-steps) in the Python documentation. Be sure to check the option "Add Python to PATH" during installation. Alternatively, if you have [WSL](https://learn.microsoft.com/en-us/windows/wsl/about) installed, you can use Python in WSL. 

### Install Visual Studio Code  
Download and install Visual Studio Code from [this link](https://code.visualstudio.com/Download). We are using VS Code as an integrated development environment (IDE) to create scripts, execute terminal commands, and manage files all in one place.

If you choose to run your Python code on a Linux terminal or cloud services like GCP or AWS, installing VS Code is unnecessary. Instead, you should be familiar with a terminal-based text editor like Nano, Emacs, or Vim.

## Python virtual environments
To run Python projects, it's best practice to create a dedicated virtual environment for each project to manage dependencies. To create a virtual environment (called `.venv`), use the following commands in the terminal:

```bash 
# macOS/Linux
# You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
python3 -m venv .venv

# Windows
# You can also use `py -3 -m venv .venv`
python -m venv .venv
```

To actiavte the `.venv` virtual environment use:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.\.venv\Scripts\Activate.ps1
```

Alternatively, you can use VS Code to create and activate the virtual environments (see [here](https://code.visualstudio.com/docs/python/environments)).



