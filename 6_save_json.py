import json

results = {
    "test_login": "passed",
    "test_signup": "failed",
    "test_payment": "passed"
}


with open("test_results.json", "w") as f:
    json.dump(results, f, indent=4)
