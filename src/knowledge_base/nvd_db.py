from typing import Dict, List

import requests


class NVDVulnerabilityDatabase:
    NVD_API_BASE_URL = "https://services.nvd.nist.gov/rest/json"

    def search_vulnerabilities(self, search_string: str) -> List[Dict]:
        cve_items = self.fetch_vulnerabilities_by_keyword(search_string)
        vulnerabilities = []

        for item in cve_items:
            cve = item["cve"]["CVE_data_meta"]["ID"]
            description = item["cve"]["description"]["description_data"][0]["value"]
            severity = item["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]
            score = item["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]

            vulnerabilities.append(
                {
                    "cve_id": cve,
                    "description": description,
                    "severity": severity,
                    "score": score,
                }
            )

        return vulnerabilities

    def fetch_vulnerabilities_by_keyword(self, search_string: str) -> List[Dict]:
        url = (
            f"{self.NVD_API_BASE_URL}/cves/1.0"
            f"?keyword={search_string}&resultsPerPage=10"
        )
        response = requests.get(url)
        data = response.json()

        return data["result"]["CVE_Items"]


nvd_db = NVDVulnerabilityDatabase()


if __name__ == "__main__":
    # Search for vulnerabilities by keyword
    search_string = "apache"
    vulnerabilities = nvd_db.search_vulnerabilities(search_string)

    for vuln in vulnerabilities:
        print(f"CVE ID: {vuln['cve_id']}")
        print(f"Description: {vuln['description']}")
        print(f"Severity: {vuln['severity']}")
        print(f"Score: {vuln['score']}")
        print("-------------------------------")
