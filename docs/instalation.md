# Installation Instructions

To get started with the Quantum Internet Core, follow these installation instructions.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

## Installation Steps

1. **Clone the repository**:
   ```bash
   1 git clone https://github.com/KOSASIH/quantum-internet-core.git
   2 cd quantum-internet-core
   ```

2. **Set up a virtual environment (optional but recommended)**:

   ```bash
   1 python -m venv venv
   2 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   1 pip install -r requirements.txt
   ```

4. **Verify the installation**: You can run the following command to ensure everything is set up correctly:

   ```bash
   1 python -c "import quantum_repeaters; print('Quantum Internet Core installed successfully!')"
   ```

## Additional Setup
For advanced configurations, refer to the Configuration Management documentation.

If you encounter any issues during installation, please check the GitHub Issues page for solutions or report a new issue.
