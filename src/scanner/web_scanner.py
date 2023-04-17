from typing import Dict, List

import requests


def check_web_server_version(url: str) -> Dict[str, str]:
    try:
        response = requests.get(url, timeout=3)
        server_header = response.headers.get("Server", "")

        return {"url": url, "server_header": server_header}
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {"url": url, "server_header": "Error"}


def scan_websites(websites: List[str]) -> List[Dict[str, str]]:
    server_versions = []

    for website in websites:
        server_version = check_web_server_version(website)
        server_versions.append(server_version)

    return server_versions


if __name__ == "__main__":
    websites_to_scan = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    print("Scanning websites...")
    web_servers = scan_websites(websites_to_scan)

    for web_server in web_servers:
        print(f"{web_server['url']} - {web_server['server_header']}")
