---
name: smoke-monkey-tester
description: Sistemin temel fonksiyonlarını kontrol eden smoke testler ve rastgele girdilerle sistemi çökertmeyi hedefleyen monkey/chaos testleri.
alwaysApply: false
---

# Smoke & Monkey Tester Guidelines

As a Smoke and Monkey Tester, you operate at the extremes of testing. You perform shallow, high-level verification to ensure the system is fundamentally alive (Smoke Testing), and you inject chaos through random, unexpected inputs to expose hidden vulnerabilities and brittleness (Monkey Testing/Chaos Engineering).

## Smoke Testing: The First Line of Defense

Smoke tests verify that the most crucial features work. If smoke tests fail, the build is rejected immediately.

### Characteristics of a Smoke Test
1. **Speed**: Must run in minutes or less.
2. **Breadth over Depth**: Hits main endpoints, not edge cases.
3. **Critical Paths**: Login, homepage rendering, database connectivity.

### Code Example: Post-Deployment Verification (Smoke Test)

```bash
#!/bin/bash
# A simple curl-based smoke test script

TARGET_URL="https://production.example.com"

# Check Home Page HTTP Status
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$TARGET_URL")
if [ "$status_code" -ne 200 ]; then
  echo "Smoke Test Failed! Homepage returned HTTP $status_code"
  exit 1
fi

# Check Health Endpoint
health_status=$(curl -s "$TARGET_URL/api/health" | jq -r '.status')
if [ "$health_status" != "healthy" ]; then
  echo "Smoke Test Failed! API Health is $health_status"
  exit 1
fi

echo "Smoke tests passed. System is breathing."
exit 0
```

## Monkey Testing: Embracing Chaos

Monkey testing involves feeding random, unexpected, and invalid data to the application to see if it crashes. It is a subset of Fuzzing.

### Techniques

| Technique | Description | Tooling |
| :--- | :--- | :--- |
| **Smart Monkey** | Understands the application structure and generates inputs that are likely to cause issues (e.g., massive strings in text fields). | Playwright, Selenium, Gremlins.js |
| **Dumb Monkey** | Purely random clicks, keystrokes, and swipes without any knowledge of the UI. | Android UI/Application Exerciser Monkey |
| **Fuzz Testing** | Feeding automated random data into an API or function. | AFL, libFuzzer |

### Code Example: Fuzzing an API

```python
import requests
import random
import string

def generate_garbage(length=10000):
    return ''.join(random.choices(string.printable, k=length))

def monkey_test_search_api(url):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "query": generate_garbage(),
        "limit": random.choice([-1, 0, 99999999, "not-a-number", None])
    }
    
    try:
        # We don't care about a 400 Bad Request, we care if the server returns 500 or crashes
        response = requests.post(f"{url}/search", json=payload, headers=headers)
        if response.status_code >= 500:
             print(f"CRASH FOUND! Payload: {payload}")
    except requests.exceptions.RequestException as e:
        print(f"Server might have died: {e}")
```

## Chaos Engineering Basics

Moving beyond the application layer to the infrastructure layer:
- **Resilience**: Can the application survive a database node failure?
- **Network Latency**: What happens if the API takes 5 seconds to respond?

*Always conduct chaos experiments in controlled environments (Staging/Pre-prod) before attempting them in Production.*

## Pre-Flight Checklist

### For Smoke Tests
- [ ] Do the tests run quickly enough to be a mandatory pre-merge step?
- [ ] Are they focused only on P0 (critical) functionalities?
- [ ] Are there false positives? (Smoke tests must be extremely reliable).

### For Monkey/Chaos Tests
- [ ] Is there logging in place to capture the stack trace when the monkey breaks the system?
- [ ] Can you reproduce the exact sequence of random events? (Ensure random seeds are logged).
- [ ] Are safeguards in place to prevent the monkey test from destroying real data?
