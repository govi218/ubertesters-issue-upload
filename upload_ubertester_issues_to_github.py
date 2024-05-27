import csv
import os
import sys

def merge_debug_info_with_body(row):
    body = f"""Number: {row["Number"]}
Severity: {row["Severity"]}
Priority: {row["Priority"]}
Instructions: \n{row["Body"]}
Type: {row["Type"]}
Device: {row["Device"]}
Reporter: {row["Reporter"]}
Body: {row["Body"]}
Build: {row["Build"]}
Attachments: {row["Attachments"]}
"""
    return body

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python upload_ubertester_issues_to_github.py input.csv github_token github_project github_repository")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    github_token = sys.argv[2]
    github_org = sys.argv[3]
    github_repo = sys.argv[4]

    try:
        with open(input_csv_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print(f"Error: Input file '{input_csv_file}' not found.")
        sys.exit(1)

    github_formatted_issues = []
    for row in data:
        github_formatted_issues.append({
            "title": f"{row['Number']} - {row['Title']}",
            "body": merge_debug_info_with_body(row)
        })

    output_csv_file = "ubertesters_github_issues.csv"
    try:
        fieldnames = ["title", "body"]
        with open(output_csv_file, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(github_formatted_issues)
        print(f"Output CSV file '{output_csv_file}' created successfully.")
    except IOError:
        print(f"Error: Unable to create output file '{output_csv_file}'.")
        sys.exit(1)

    githubCsvTools_path = os.popen("which githubCsvTools").read().strip()
    if os.path.isfile(githubCsvTools_path) and os.access(githubCsvTools_path, os.X_OK):
        os.system(f"githubCsvTools {output_csv_file}  -t {github_token} -o {github_org} -r {github_repo}")
    else:
        print("Error: 'githubCsvTools' is not installed or not executable.")