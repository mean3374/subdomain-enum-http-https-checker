import socket
import subprocess
import requests
import concurrent.futures
import warnings
from tqdm import tqdm
from tabulate import tabulate

warnings.filterwarnings("ignore", category=requests.urllib3.exceptions.InsecureRequestWarning)

def nslookup(domain):
    try:
        address = socket.gethostbyname(domain)
        return 'Address: ' + address
    except socket.gaierror:
        return 'Address: N/A'

def check_http_https_status(domain):
    with requests.Session() as session:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            http_future = executor.submit(session.get, f"http://{domain}", timeout=5)
            https_future = executor.submit(session.get, f"https://{domain}", verify=False, timeout=5)

        try:
            http_response = http_future.result()
            http_status_code = http_response.status_code if http_response else None
        except requests.exceptions.RequestException:
            http_status_code = None

        try:
            https_response = https_future.result()
            https_status_code = https_response.status_code if https_response else None
        except requests.exceptions.RequestException:
            https_status_code = None

    if http_status_code and http_status_code == 200:
        status = "HTTP only"
        status_code = f"HTTP: {http_status_code}"
    else:
        status = "Not reachable"
        status_code = "N/A"

    if https_status_code and https_status_code == 200:
        if http_status_code and http_status_code == 200:
            status = "Both HTTP&HTTPS"
            status_code = f"HTTP: {http_status_code}, HTTPS: {https_status_code}"
        else:
            status = "HTTPS only"
            status_code = f"HTTPS: {https_status_code}"

    address = nslookup(domain)
    return domain, status, status_code, address

def perform_assetfinder(domain_name):
    assetfinder_command = f'assetfinder.exe --subs-only {domain_name}'
    process = subprocess.run(assetfinder_command, capture_output=True, text=True, shell=True)
    return process.stdout.splitlines()

def write_to_table(output_file, data):
    data_with_no = [[str(i + 1)] + row for i, row in enumerate(data)]
    table = tabulate(data_with_no, headers=["No", "Domain", "Status", "Status Code", "Address"], tablefmt="pretty")
    with open(output_file, "a") as file:
        file.write(table + "\n")

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")

    output_file = f"output_of_{domain_name}.txt"

    subdomains = perform_assetfinder(domain_name)
    total_count = len(subdomains)

    counts = [0, 0]
    table_data = []

    with concurrent.futures.ThreadPoolExecutor() as executor, tqdm(total=total_count, desc="Processing subdomains") as pbar:
        futures = []
        for subdomain in subdomains:
            future = executor.submit(check_http_https_status, subdomain)
            future.add_done_callback(lambda p: pbar.update())
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            domain, status, status_code, address = future.result()
            table_data.append([domain, status, status_code, address])

    for domain, status, status_code, address in table_data:
        if "HTTP only" in status:
            counts[0] += 1
        if "HTTPS only" in status:
            counts[1] += 1

    both_count = 0
    for domain, status, status_code, address in table_data:
        if "Both HTTP&HTTPS" in status:
            both_count += 1

    summary = f"\nSummary:\nTotal: {total_count}\nHTTP only: {counts[0]}\nHTTPS only: {counts[1]}\nBoth HTTP&HTTPS: {both_count}\n"

    write_to_table(output_file, table_data)
    with open(output_file, "a") as file:
        print(summary)
        file.write(summary)
