import ephem
from datetime import datetime
from typing import Dict, List, Any

class PlanetaryAspects:
    def __init__(self):
        self.planets = {
            'sun': ephem.Sun(),
            'moon': ephem.Moon(),
            'mars': ephem.Mars(),
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn()
        }
    
    def calculate_aspects(self, date: datetime = None) -> List[Dict[str, Any]]:
        """Calculate planetary aspects for given date."""
        if date is None:
            date = datetime.utcnow()
            
        aspects = []
        observer = ephem.Observer()
        observer.date = date
        
        for p1_name, p1 in self.planets.items():
            p1.compute(observer)
            for p2_name, p2 in self.planets.items():
                if p1_name >= p2_name:
                    continue
                    
                p2.compute(observer)
                angle = ephem.separation(p1, p2) * 180/ephem.pi
                
                aspects.append({
                    'planet1': p1_name,
                    'planet2': p2_name,
                    'angle': angle,
                    'aspect_type': self._get_aspect_type(angle)
                })
        
        return aspects
    
    def _get_aspect_type(self, angle: float) -> str:
        """Determine aspect type based on angle."""
        aspects = {
            0: 'conjunction',
            60: 'sextile',
            90: 'square',
            120: 'trine',
            180: 'opposition'
        }
        
        for degree, aspect in aspects.items():
            if abs(angle - degree) <= 5:  # 5 degree orb
                return aspect
                
        return 'none'