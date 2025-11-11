# Update instructions
If new packages are installed, update the [requirements.txt](requirements.txt) file:  
`python -m pip freeze > Requirements.txt`

# VSCode Instructions
## Initial setup
### Development
Create PY virtual environment  
`python -m venv .venv`

Activate venv  
`.\.venv\Scripts\Activate.ps1`

Install packages  
`python -m pip install -r requirements.txt`  

# References
- [OR-Tools Install Instructions](https://developers.google.com/optimization/install)
- [CVXPY](https://www.cvxpy.org/)
