import requests

# Target URL and wordlist
target_url = "http://httpbin.org"  # A reliable testing site that echoes back requests
wordlist = ["status/200", "status/404", "status/403", "admin", "login"]

# Add headers to mimic a real web browser (prevents blocking)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print(f"[*] Starting directory scan on: {target_url}\n")

for word in wordlist:
    full_url = f"{target_url}/{word}"
    
    try:
        # Send request with headers and a short timeout
        response = requests.get(full_url, headers=headers, timeout=3)
        
        if response.status_code == 200:
            print(f"[+] Discovered Endpoint: {full_url} (Status: 200)")
        elif response.status_code == 403:
            print(f"[!] Forbidden Endpoint: {full_url} (Status: 403)")
        else:
            print(f"[-] Checked: {full_url} (Status: {response.status_code})")
            
    except requests.exceptions.ConnectionError:
        print(f"[-] Connection failed for: {full_url}")
    except requests.exceptions.Timeout:
        print(f"[-] Request timed out for: {full_url}")

print("\n[*] Scan complete!")
