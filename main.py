from urllib.parse import urlparse
import requests
import time


def normalize_url(website):
    website = website.strip()

    if not website.startswith("http://") and not website.startswith("https://"):
        website = "https://" + website

    return website


def validate_url(website):
    parsed_url = urlparse(website)

    if parsed_url.scheme in ["http", "https"] and parsed_url.netloc:
        return True

    return False


def get_domain(website):
    parsed_url = urlparse(website)
    return parsed_url.netloc


def check_https(website):
    if website.startswith("https://"):
        print("HTTPS: PASS")
        print("HTTPS connection detected")
        return 1

    print("HTTPS: WARNING")
    print("HTTPS connection not detected")
    return 0


def check_security_headers(response):
    score = 0

    print("Security Headers")
    print("--------------------------------")

    csp = response.headers.get("Content-Security-Policy")

    if csp:
        print("CSP: PASS")
        score += 1
    else:
        print("CSP: WARNING - Missing")

    x_frame = response.headers.get("X-Frame-Options")

    if x_frame and x_frame.upper() in ["DENY", "SAMEORIGIN"]:
        print("X-Frame-Options: PASS")
        score += 1
    else:
        print("X-Frame-Options: WARNING")

    x_content = response.headers.get("X-Content-Type-Options")

    if x_content and x_content.lower() == "nosniff":
        print("X-Content-Type-Options: PASS")
        score += 1
    else:
        print("X-Content-Type-Options: WARNING")

    hsts = response.headers.get("Strict-Transport-Security")

    if hsts and "max-age=" in hsts.lower():
        print("HSTS: PASS")
        score += 1
    else:
        print("HSTS: WARNING")

    referrer = response.headers.get("Referrer-Policy")

    if referrer:
        print("Referrer-Policy: PRESENT")
    else:
        print("Referrer-Policy: WARNING - Missing")

    permissions = response.headers.get("Permissions-Policy")

    if permissions:
        print("Permissions-Policy: PRESENT")
    else:
        print("Permissions-Policy: WARNING - Missing")

    return score


def show_website_information(response, response_time):
    print()
    print("Website Information")
    print("--------------------------------")
    print("Status Code:", response.status_code)
    print("Response Time:", round(response_time, 2), "seconds")
    print("Redirects:", len(response.history))

    content_type = response.headers.get("Content-Type")

    if content_type:
        print("Content-Type:", content_type)
    else:
        print("Content-Type: Not available")

    server = response.headers.get("Server")

    if server:
        print("Server:", server)
    else:
        print("Server: Not disclosed")


def show_security_level(score):
    print()
    print("================================")
    print("Security Score:", score, "/ 5")

    if score == 5:
        print("Security Level: GOOD")
    elif score >= 3:
        print("Security Level: NEEDS IMPROVEMENT")
    else:
        print("Security Level: LOW")

    print("================================")


print("================================")
print("        CYBERSHIELD")
print("================================")
print("Basic Web Security Checker")
print()

website = input("Enter website URL: ")

website = normalize_url(website)

print("You entered:", website)
print()

if not validate_url(website):
    print("Error: Invalid URL format")
    exit()

domain = get_domain(website)

print("Domain:", domain)
print()

score = 0

score += check_https(website)

print()

try:
    start_time = time.perf_counter()

    response = requests.get(
        website,
        timeout=5,
        allow_redirects=True
    )

    end_time = time.perf_counter()

    response_time = end_time - start_time

    print("Website Status: Reachable")

    show_website_information(response, response_time)

    print()

    score += check_security_headers(response)

    show_security_level(score)

except requests.Timeout:
    print("Error: Website request timed out")

except requests.ConnectionError:
    print("Error: Could not connect to website")

except requests.RequestException:
    print("Error: Something went wrong while checking website")