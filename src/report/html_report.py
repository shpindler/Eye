from typing import Dict, List

from jinja2 import Template


def generate_html_report(filename: str, vulnerabilities: List[Dict]) -> None:
    template_string = """
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerability Scan Report</title>
</head>
<body>
    <h1>Vulnerability Scan Report</h1>
    {% for vuln in vulnerabilities %}
        <h2>{{ vuln.cve_id }}</h2>
        <p>Description: {{ vuln.description }}</p>
        <p>Severity: {{ vuln.severity }}</p>
        <p>Score: {{ vuln.score }}</p>
        <hr>
    {% endfor %}
</body>
</html>
"""
    template = Template(template_string)
    rendered_html = template.render(vulnerabilities=vulnerabilities)

    with open(filename, "w") as f:
        f.write(rendered_html)


if __name__ == "__main__":
    from knowledge_base.nvd_db import nvd_db

    # Assuming you have a list of vulnerabilities
    vulnerabilities = nvd_db.search_vulnerabilities("apache")

    # Generate an HTML report
    html_filename = "vulnerability_scan_report.html"
    generate_html_report(html_filename, vulnerabilities)
    print(f"HTML report saved as {html_filename}")
