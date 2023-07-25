# subdomain-enum-http-https-checker
The "Subdomain Enumeration HTTP/HTTPS Status Checker" is a Python script designed to enumerate subdomains for a given domain and verify their HTTP/HTTPS status. It serves as a valuable tool for penetration testers, automating tasks during the information-gathering phase and identifying subdomains that are accessible via HTTP, HTTPS, both, or unreachable.

This project uses the `requests` library to make HTTP requests, `tqdm` to display progress bars, and `tabulate` to format the output into tables.

## Requirements

- Python 3.x
- Install the required Python packages by running: `pip install -r requirements.txt`

## Usage

1. Clone the repository or download the script include assetfinder.exe file.
2. Install the required packages using `pip`:
3. Run the script using `python subdomain-enum-http-https-checker.py`:
4. Enter the domain name for which you want to enum and check HTTP/HTTPS status. For example, `example.com`

## Output

The script will generate a text file with the results named `output_of_{domain_name}.txt`. It will contain a table with the following columns:

- No: The serial number of the subdomain.
- Domain: The subdomain name.
- Status: The status of the subdomain (HTTP only, HTTPS only, Both HTTP&HTTPS, or Not reachable).
- Status Code: The HTTP status code if reachable, otherwise N/A.
- Address: The IP address of the subdomain if reachable, otherwise N/A.

The script will also print a summary at the end, indicating the total number of subdomains checked and the count of subdomains with HTTP only, HTTPS only, and Both HTTP&HTTPS status.

## Notes

- The `socket` and `subprocess` modules are part of the Python standard library, so they don't need to be installed separately.
- For Windows users, the script uses `assetfinder.exe` to find subdomains. Make sure you have it in your system's PATH or provide the full path to `assetfinder.exe`.




