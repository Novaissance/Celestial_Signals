package signals

import (
    "time"
)

// SignalType represents the type of trading signal
type SignalType string

const (
    Buy  SignalType = "BUY"
    Sell SignalType = "SELL"
    Hold SignalType = "HOLD"
)

// Signal represents a trading signal
type Signal struct {
    Type      SignalType
    Timestamp time.Time
    Symbol    string
    Price     float64
    Strength  float64
    Aspects   []string
}

// Strategy interface for implementing signal strategies
type Strategy interface {
    GenerateSignal(marketData map[string]interface{}, 
                  planetaryData map[string]interface{}) (*Signal, error)
    ValidateConfig(config map[string]interface{}) bool
}