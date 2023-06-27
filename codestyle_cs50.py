# PEP = python enhancement proposal
# PEP 8 standardised what Python code should look like
# peps.python.org/pep-0008/
# READABILITY COUNTS
# Consistency within:
# --> consistency within the/a style guide
# --> consistency within a specific project
# --> consistency within one module or function

# - Indentation. Python enforces indentation.
# - Tabs or Spaces? FOUR SPACES with Python. When using VS Code, hitting tab actually converts into four spaces.
# - Max Line Length
# - Blank lines / whitespace. Readability of code.
# - Imports. How and where. 

# Program called pylint is a LINTER
# pip install pylint
# but very noisy / overwhelming!!!

# pycodestyle might be better for beginner
# pycodestyle.pycqa.org

# black 
# pip install black
# black.readthedocs.io
# an "opinionated formatter"
# "Any customer can have their car any colour they want, so long as it's black - Henry Ford"

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
}
for student in students:
    print(student)

