Secure Coding Review Using Python

1. Introduction

Secure Coding Review is the process of checking a program to identify security vulnerabilities and improve its safety.

2. Objective

The main objective of this project is to identify security vulnerabilities in a Python application and fix them using secure coding practices.

3. Programming Language

- Python

4. Application Selected

- Simple Calculator

5. Vulnerabilities Identified

The following security vulnerabilities were identified:

1. Code Injection: The eval() function can execute unwanted Python code.
2. Invalid Input: Incorrect user input may cause the program to crash.
3. Division by Zero: Dividing a number by zero causes an error.

6. Security Tool Used

Bandit: Bandit is a Python security tool used to identify common security issues in Python source code.

7. Security Improvements

The following improvements were made:

1. Removed the eval() function.
2. Used float() to validate numerical input.
3. Used try-except to handle invalid input.
4. Added a condition to prevent division by zero.
5. Added validation for mathematical operators.

8. Testing

The calculator was tested with:

- Addition
- Subtraction
- Multiplication
- Division
- Invalid input
- Division by zero

9. Result

The security review helped identify potential vulnerabilities and improve the safety of the calculator application.

Bandit was used to scan the Python source code, and the scan report was saved as security_report.txt.

10. Conclusion

This project helped me understand the importance of secure coding practices. I learned how to identify vulnerabilities, use Bandit for security scanning, and improve application security using Python.
Security Report

Tool Used

Bandit – Python Security Scanner.

Scan Details

- File scanned: calculator.py
- Lines of code scanned: 24
- Total security issues identified: 0

Severity Results

- High: 0
- Medium: 0
- Low: 0

Scan Result

No issues identified by Bandit.

Conclusion

The Python calculator was scanned using Bandit to identify common security vulnerabilities. No issues were detected by the scanner. Manual code review was also performed to check input validation, division by zero handling, invalid operators and exception handling.