from typing import Dict, List

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generate_pdf_report(filename: str, vulnerabilities: List[Dict]) -> None:
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Vulnerability Scan Report", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    for vuln in vulnerabilities:
        cve_id = Paragraph(f"CVE ID: {vuln['cve_id']}", styles["Heading2"])
        description = Paragraph(
            f"Description: {vuln['description']}", styles["BodyText"]
        )
        severity = Paragraph(f"Severity: {vuln['severity']}", styles["BodyText"])
        score = Paragraph(f"Score: {vuln['score']}", styles["BodyText"])

        elements.append(cve_id)
        elements.append(description)
        elements.append(severity)
        elements.append(score)
        elements.append(Spacer(1, 12))

    doc.build(elements)


if __name__ == "__main__":
    from knowledge_base.nvd_db import nvd_db

    # Assuming you have a list of vulnerabilities
    vulnerabilities = nvd_db.search_vulnerabilities("apache")

    # Generate a PDF report
    pdf_filename = "vulnerability_scan_report.pdf"
    generate_pdf_report(pdf_filename, vulnerabilities)
    print(f"PDF report saved as {pdf_filename}")
