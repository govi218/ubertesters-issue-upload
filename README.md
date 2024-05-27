# Upload ubertesters issues to github

## Requirements
- Python 3.7+
- [Github CSV Tools](https://github.com/gavinr/github-csv-tools) (and nodeJS to use it)

## Usage
- Export issues from ubertesters into Excel. Convert the excel to a CSV using a spreadsheet editor.
- Make sure you have a Github Token, see [here](https://github.com/gavinr/github-csv-tools) for instructions to get one.
- Run `python upload_ubertester_issues_to_github.py input.csv github_token github_project github_repository`
