# CyberShield

CyberShield is a beginner-friendly Python-based web security checker
that performs basic security and website information checks for a given
URL.

## Features

-   URL normalization and validation
-   Domain extraction
-   HTTPS detection
-   Website reachability check
-   HTTP status code
-   Response time
-   Redirect count
-   Content-Type detection
-   Basic server information
-   Content-Security-Policy (CSP) check
-   X-Frame-Options check
-   X-Content-Type-Options check
-   HTTP Strict Transport Security (HSTS) check
-   Referrer-Policy check
-   Permissions-Policy check
-   Basic security score and security level
-   Error handling for timeout and connection errors

## Technologies Used

-   Python
-   Requests
-   urllib
-   VS Code

## Requirements

-   Python 3.x
-   Requests library

Install Requests with:

``` bash
pip install requests
```

## How to Run

1.  Open the CyberShield project folder in VS Code.
2.  Open the terminal.
3.  Run:

``` bash
python main.py
```

4.  Enter a website URL when prompted.

Example:

``` text
https://youtube.com
```

## Example Output

``` text
Website Status: Reachable

Website Information
--------------------------------
Status Code: 200
Response Time: 0.46 seconds
Redirects: 0
Content-Type: text/html

Security Headers
--------------------------------
CSP: PASS
X-Frame-Options: WARNING
X-Content-Type-Options: PASS
HSTS: PASS
Referrer-Policy: WARNING - Missing
Permissions-Policy: PRESENT

Security Score: 4 / 5
Security Level: NEEDS IMPROVEMENT
```

## Security Score

The current score is based on five main checks:

-   HTTPS
-   Content-Security-Policy
-   X-Frame-Options
-   X-Content-Type-Options
-   HSTS

The score is intended as a basic educational indicator. A higher score
does not mean that a website is completely secure.

## Error Handling

CyberShield handles common request problems such as:

-   Request timeout
-   Connection failure
-   Other request-related errors
-   Invalid URL format

## Project Structure

``` text
CyberShield/
│
├── main.py
└── README.md
```

## Limitations

CyberShield performs basic checks only. It does not perform penetration
testing, vulnerability exploitation, malware analysis, or a complete
security audit.

Header checks are also limited to the checks implemented in the project
and should not be treated as a complete assessment of website security.

## Safe Use

Use CyberShield only with websites you own or are authorized to test. Do
not use it to perform unauthorized security testing.

## Future Improvements

-   More detailed header validation
-   HTTPS certificate information
-   Export security reports
-   Improved scoring system
-   Graphical user interface
-   More security checks
-   Detailed scan reports

## Learning Goal

This project was created to practice Python programming, HTTP requests,
web security concepts, error handling, and GitHub project documentation.

## Author

Naitik Barot

Diploma in Information Technology Student
