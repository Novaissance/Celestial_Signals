from abc import ABC, abstractmethod
from typing import Dict, Any

class SignalStrategy(ABC):
    """Abstract base class for signal strategies."""
    
    @abstractmethod
    def generate_signal(self, market_data: Dict[str, Any], 
                       planetary_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate trading signal based on market and planetary data."""
        pass
    
    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """Validate strategy configuration."""
        pass