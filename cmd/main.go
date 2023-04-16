package main

import (
	"fmt"
	"os"

	"github.com/shpindler/eye/internal/config"
	"github.com/shpindler/eye/internal/report"
	"github.com/shpindler/eye/internal/scanner"
)

func main() {
	// Load configuration
	cfg, err := config.LoadConfig()
	if err != nil {
		fmt.Println("Error loading configuration:", err)
		os.Exit(1)
	}

	// Initialize scanner
	s, err := scanner.NewScanner(cfg)
	if err != nil {
		fmt.Println("Error initializing scanner:", err)
		os.Exit(1)
	}

	// Run scanner
	results, err := s.Scan()
	if err != nil {
		fmt.Println("Error running scanner:", err)
		os.Exit(1)
	}

	// Generate report
	err = report.GenerateReport(results)
	if err != nil {
		fmt.Println("Error generating report:", err)
		os.Exit(1)
	}

	fmt.Println("Scan completed successfully.")
}
