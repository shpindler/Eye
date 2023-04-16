package report

import (
	"testing"

	"github.com/shpindler/eye/internal/scanner"
)

func TestGenerateReport(t *testing.T) {
	results := []scanner.ScanResult{
		// Add test results
	}

	err := GenerateReport(results)
	if err != nil {
		t.Fatalf("Failed to generate report: %v", err)
	}

	// Add more test cases for report generation
}
