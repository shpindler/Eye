package scanner

import (
	"testing"

	"github.com/shpindler/eye/internal/config"
)

func TestScanner(t *testing.T) {
	cfg := &config.Config{
		// Set necessary configurations for testing
	}

	s, err := NewScanner(cfg)
	if err != nil {
		t.Fatalf("Failed to initialize scanner: %v", err)
	}

	results, err := s.Scan()
	if err != nil {
		t.Fatalf("Scanner failed: %v", err)
	}

	// Add more test cases for your scanner
}
