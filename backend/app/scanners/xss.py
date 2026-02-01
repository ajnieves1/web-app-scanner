# XSS payloads used to test user input whether its reflected back into the page without sanitization

import requests

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>"
]

# Performs basic XSS scan against target URL
# 
# The scanner works this way:
# 1. Injects known XSS payloads into query
# 2. Sends HTTP GET rquests to target
# 3. Checks if payload appears unescaped in response
# 
# Limitations are as follows:
# - Only tests a single query parameter (?q=)
# - May produce false positives
# - Does not test POST requests
#
# Args:
# url (str): Base URL of target application
# Returns:
# list: A list of detected XSS findings
def scan_xss(url: str):
    findings = []
    # Iterate through each payload
    for payload in XSS_PAYLODS:
        # Construct URL by injecting payload into a query parameter "q"
        test_url = f"{url}?q={payload}"
        try:
            # Send the HTTP request to the target
            response = requests.get(test_url, timeout=5)

            # If the payload is reflected directly in the response body
            # this is a strong indicator of reflected XSS
            if payload in response.text:
                findings.append({
                    "type": "XSS",
                    "url": test_url,
                    "payload": payload,
                    "severity": "High",
                    "description": "Reflected XSS payload detected in response"
                })

        except requests.RequestException as e:
            # Network errors, timeouts, invalid URLs, etc
            # In a production scanner this should be logged
            # rather than silently ignored
            continue
    return findings