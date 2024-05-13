import msfconsole
import requests
from bs4 import BeautifulSoup
import re
import os

def get_user_url():
    """Prompts the user for a URL and validates it."""
    while True:
        url = input("Enter the URL to scan: ")
        if re.match(r"https?://[^\s]+", url):
            return url
        else:
            print("Invalid URL. Please enter a valid URL starting with http or https.")

def scan_url_for_cve(url):
    """Scans the URL for CVE vulnerabilities using Metasploit."""
    console = msfconsole.MsfConsole()
    result = console.execute(f"db_nmap -sV {url}", wait_for_response=True)
    cve_pattern = r"CVE-\d{4}-\d{4,7}"
    cves = re.findall(cve_pattern, result)
    return cves

def scan_url_for_exploits(url):
    """Scans the URL for exploitable vulnerabilities using Metasploit."""
    console = msfconsole.MsfConsole()
    result = console.execute(f"auxiliary/scanner/http/http_version {url}", wait_for_response=True)
    exploitable_pattern = r"Exploit exists in module"
    exploits = re.findall(exploitable_pattern, result)
    return exploits

def save_results_to_file(cves, exploits, filename="scan_results.txt"):
    """Saves the scan results to a text file."""
    with open(filename, "w") as file:
        file.write("--- CVE Vulnerabilities ---\n")
        if cves:
            for cve in cves:
                file.write(f"- {cve}\n")
        else:
            file.write("No CVE vulnerabilities found.\n")

        file.write("\n--- Exploitable Vulnerabilities ---\n")
        if exploits:
            for exploit in exploits:
                file.write(f"- {exploit}\n")
        else:
            file.write("No exploitable vulnerabilities found.\n")

def main():
    """Main function to execute the script."""
    url = get_user_url()
    cves = scan_url_for_cve(url)
    exploits = scan_url_for_exploits(url)
    save_results_to_file(cves, exploits)
    print(f"Scan results saved to scan_results.txt")

if __name__ == "__main__":
    main()
