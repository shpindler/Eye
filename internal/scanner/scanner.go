package scanner

import (
	"errors"

	"github.com/shpindler/eye/internal/config"
)

type Scanner struct {
	config *config.Config
}

func NewScanner(cfg *config.Config) (*Scanner, error) {
	return &Scanner{config: cfg}, nil
}

func (s *Scanner) Scan() ([]ScanResult, error) {
	return nil, errors.New("not implemented")
}

type ScanResult struct {
	// Fields for the scan result
}
