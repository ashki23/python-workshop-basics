# Python Basics: A Beginner's Guide to Programming

*A workshop for **Mentoring Math Minds** program at Saint Louis University.*

The workshop is designed to introduce the fundamentals of Python programming in an engaging and interactive way. Participants will learn key concepts such as variables, data types, basic operations, and control flow structures like loops and conditional statements. They will also explore essential data structures such as lists and dictionaries, and understand how to write reusable code using functions. The workshop includes hands-on exercises and a mini-project. By the end of the session, participnets will have the foundational skills to start coding confidently and continue exploring Python independently.

### **Main topics** 
In this workshop, we cover the following topics from [The Python Tutorial](https://docs.python.org/3/tutorial/index.html).

1. **Introduction and Set up**: Setting up the environment, and how to run Python (section [2](https://docs.python.org/3/tutorial/interpreter.html) and [12](https://docs.python.org/3/tutorial/venv.html)).
2. **Variables and Data Types**: Numbers, text, lists, arithmetic, and comparisons (section [3](https://docs.python.org/3/tutorial/introduction.html)).
3. **Control Flow Tools**: `if`, `else`, and `elif` statements and `for` and `while` loops (section [4](https://docs.python.org/3/tutorial/controlflow.html)).
4. **Functions**: Defining, using parameters, and return values (section [4](https://docs.python.org/3/tutorial/controlflow.html)).
5. **Data Structures**: Lists, dictionaries, tuples, and sets (section [5](https://docs.python.org/3/tutorial/datastructures.html)).
6. **Modules**: Import modules from the standard library, installed packages, or custom Python scripts (section [6](https://docs.python.org/3/tutorial/modules.html)).
7. **Input and Output**: Print, f-strings, strings, open, read and write functions (section [7](https://docs.python.org/3/tutorial/inputoutput.html)).
8. **Generative AI**: A brief introduction to leveraging AI tools like [ChatGPT](https://chatgpt.com) or [GitHub Copilot](https://github.com/features/copilot/tutorials) to assist with coding and problem-solving.  
9. **Mini-Project**: Practical application of learned concepts.

📚 **You can access the workshop content [here](https://github.com/ashki23/python-workshop-basics/blob/main/python_workshop_basics.ipynb).**

## Setup the environment
**In this workshop, we are using [Colab](https://colab.google), a Jupyter Notebook environment that runs Python in the cloud, so you don't need to install Python locally.** 

However, if you prefer to set up a local development environment on your computer, you can install Python and VS Code by following the instructions below.

#### Install Python
- **Linux**: Python is typically preinstalled on most Linux distributions.
- **macOS**: Follow [section 5.1.1](https://docs.python.org/3/using/mac.html#installation-steps). Alternatively, if you have a package manager like [Homebrew](https://brew.sh), you can use it to install Python. 
- **Windows**: Refer to [section 4.1.1](https://docs.python.org/3/using/windows.html#installation-steps) in the Python documentation. Be sure to check the option "Add Python to PATH" during installation. Alternatively, if you have [WSL](https://learn.microsoft.com/en-us/windows/wsl/about) installed, you can use Python in WSL. 

#### Install Visual Studio Code  
Download and install Visual Studio Code from [this link](https://code.visualstudio.com/Download). We are using VS Code as an integrated development environment (IDE) to create scripts, execute terminal commands, and manage files all in one place. We can also have Jupyter Notebooks in VS Code (see [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)).

## Using Python
Python can be used in two primary ways:

1. **Interactive Mode:** Open your terminal and type `python` or `python3` to launch the Python interpreter interactively. You can exit the interpreter by pressing `Control-D` on Unix, or by typing `quit()`.

2. **Running a Python Script:** Write your Python code in a script file and execute it from the terminal. For instance, to run `script.py` use the following command in the terminal: 
   ```bash
   python3 script.py
   ```

When using IDEs like Jupyter Notebook, you are primarily working in interactive mode. However, for solving larger problems and real-world programming, it is usually more efficient to create a Python script and run it in a dedicated environment, such as on an HPC system or in the cloud (or locally). Typically, this involves creating a virtual environment or a container with the necessary requirements.

## Packages
To run Python projects locally, it's best practice to create a dedicated virtual environment for each project to manage dependencies. To create and activate a virtual environment (called `.venv`), use the following commands in the terminal:

```bash 
# Create the virtual environment
# You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
python3 -m venv .venv

# Actiavte the virtual environment
source .venv/bin/activate
```

Alternatively, you can use VS Code to manage virtual environments (see [here](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command)). To remove a virtual environment, either run `rm -rf .venv` in the terminal or manually delete the `.venv` folder from the file explorer.

We can use the `pip` package manager to manage Python packages. The following commands can be used in the terminal to install, upgrade, or uninstall packages:

```bash
# Install a package
pip install <pkg-name>

# Install multiple packages using a requirements file
pip install -r requirements.txt 

# Upgrade a package
pip install --upgrade <pkg-name>

# Uninstall a package
pip uninstall <pkg-name>

# List installed packages
pip list

# Create a requirements file from the installed packages
pip freeze > requirements.txt 

# Cache management
pip cache info # view cache information 
pip cache purge # remove cache files
```

Make sure to replace `<pkg-name>` with the actual package name. For testing, let's install and uninstall the `sampleproject` package:

```bash
# Install
pip install sampleproject

# Uninstall
pip uninstall sampleproject
```
