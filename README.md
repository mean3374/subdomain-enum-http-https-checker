# subdomain-enum-http-https-checker
The "Subdomain enumeration HTTP/HTTPS Status Checker" is a Python script designed to check the HTTP/HTTPS status of subdomains for a given domain. It helps users identify which subdomains are accessible via HTTP, HTTPS, both, or not reachable.

This Python script checks the HTTP/HTTPS status of subdomains of a given domain. It uses the `requests` library to make HTTP requests, `tqdm` to display progress bars, and `tabulate` to format the output into tables.

## Requirements

- Python 3.x
- Install the required Python packages by running: `pip install -r requirements.txt`

## Usage

1. Clone the repository or download the script.
2. Install the required packages using `pip`:
3. Run the script:
4. Enter the domain name for which you want to check the subdomains' HTTP/HTTPS status.

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




