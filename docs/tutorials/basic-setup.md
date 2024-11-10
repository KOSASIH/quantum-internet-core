# Basic Setup Tutorial

Welcome to the Basic Setup Tutorial for **Quantum Internet Core**! This guide will walk you through the initial setup and configuration to get you started with the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Git

## Step 1: Clone the Repository

Start by cloning the Quantum Internet Core repository to your local machine:

```bash
1 git clone https://github.com/KOSASIH/quantum-internet-core.git
2 cd quantum-internet-core
```

## Step 2: Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

```bash
1 python -m venv venv
2 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Step 3: Install Dependencies
Install the required dependencies using pip:

```bash
1 pip install -r requirements.txt
```

## Step 4: Verify the Installation
To ensure everything is set up correctly, run the following command:

```bash
1 python -c "import quantum_repeaters; print('Quantum Internet Core installed 
```

## Step 5: Run a Sample Program
You can run a sample program to test your setup. Create a new Python file named test.py and add the following code:

```python
1 from quantum_repeaters import Repeater
2 
3 # Create a quantum repeater instance
4 repeater = Repeater()
5 
6 # Start the repeater
7 repeater.start()
8 
9 print("Quantum repeater is running!")
```

- Run the program:

```bash
1 python test.py
```

If everything is set up correctly, you should see the message "Quantum repeater is running!"

## Conclusion
Congratulations! You have successfully set up the Quantum Internet Core. You can now explore the various components and start building your quantum communication applications. For more advanced usage, refer to the Advanced Usage Tutorial.
