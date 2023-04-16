package config

import (
	"testing"
)

func TestLoadConfig(t *testing.T) {
	cfg, err := LoadConfig()
	if err != nil {
		t.Fatalf("Failed to load configuration: %v", err)
		// Add test cases for verifying the correctness of your configuration
	}
}
