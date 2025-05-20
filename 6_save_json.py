import json
import csv

results = {
    "test_login": "passed",
    "test_signup": "failed",
    "test_payment": "passed"
}


with open("test_results.json", "w") as f:
    json.dump(results, f, indent=4)

with open("test_results.csv", "w") as f:
    writer = csv.writer(f)
    for test in results:
        writer.writerow([test, results[test]])
