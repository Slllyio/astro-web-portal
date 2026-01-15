
from typing import Dict, List

class BAVCalculator:
    """
    Implements standard Paraśara Ashtakavarga Rules.
    (Rekhas/Bindus contributed by planets in houses from themselves and others).
    """

    # BINDU TABLES (Benefic Places)
    # 1-indexed houses from the reference planet
    RULES = {
        "Sun": {
            "Sun": [1, 2, 4, 7, 8, 9, 10, 11],
            "Moon": [3, 6, 10, 11],
            "Mars": [1, 2, 4, 7, 8, 9, 10, 11],
            "Mercury": [3, 5, 6, 9, 10, 11, 12],
            "Jupiter": [5, 6, 9, 11],
            "Venus": [6, 7, 12],
            "Saturn": [1, 2, 4, 7, 8, 9, 10, 11],
            "Lagna": [3, 4, 6, 10, 11, 12]
        },
        "Moon": {
            "Sun": [3, 6, 7, 8, 10, 11],
            "Moon": [1, 3, 6, 7, 10, 11],
            "Mars": [2, 3, 5, 6, 9, 10, 11],
            "Mercury": [1, 3, 4, 5, 7, 8, 10, 11],
            "Jupiter": [1, 4, 7, 8, 10, 11, 12],
            "Venus": [3, 4, 5, 7, 9, 10, 11],
            "Saturn": [3, 5, 6, 11],
            "Lagna": [3, 6, 10, 11]
        },
        "Mars": {
            "Sun": [3, 5, 6, 10, 11],
            "Moon": [3, 6, 11],
            "Mars": [1, 2, 4, 7, 8, 9, 10, 11],
            "Mercury": [3, 5, 6, 11],
            "Jupiter": [6, 10, 11, 12],
            "Venus": [6, 8, 11, 12],
            "Saturn": [1, 4, 7, 8, 9, 10, 11],
            "Lagna": [1, 3, 6, 10, 11]
        },
        "Mercury": {
            "Sun": [5, 6, 9, 11, 12],
            "Moon": [2, 4, 6, 8, 10, 11],
            "Mars": [1, 2, 4, 7, 8, 9, 10, 11],
            "Mercury": [1, 3, 5, 6, 9, 10, 11, 12],
            "Jupiter": [6, 8, 11, 12],
            "Venus": [1, 2, 3, 4, 5, 8, 9, 11],
            "Saturn": [1, 2, 4, 7, 8, 9, 10, 11],
            "Lagna": [1, 2, 4, 6, 8, 10, 11]
        },
        "Jupiter": {
            "Sun": [1, 2, 3, 4, 7, 8, 9, 10, 11],
            "Moon": [2, 5, 7, 9, 11],
            "Mars": [1, 2, 4, 7, 8, 10, 11],
            "Mercury": [1, 2, 4, 5, 6, 9, 10, 11],
            "Jupiter": [1, 2, 3, 4, 7, 8, 10, 11],
            "Venus": [2, 5, 6, 9, 10, 11],
            "Saturn": [3, 5, 6, 12],
            "Lagna": [1, 2, 4, 5, 6, 7, 9, 10, 11]
        },
        "Venus": {
            "Sun": [8, 11, 12],
            "Moon": [1, 2, 3, 4, 5, 8, 9, 11, 12],
            "Mars": [3, 4, 6, 9, 11, 12],
            "Mercury": [3, 5, 6, 9, 11],
            "Jupiter": [5, 8, 9, 10, 11],
            "Venus": [1, 2, 3, 4, 5, 8, 9, 10, 11],
            "Saturn": [3, 4, 5, 8, 9, 10, 11],
            "Lagna": [1, 2, 3, 4, 5, 8, 9, 11]
        },
        "Saturn": {
            "Sun": [1, 2, 4, 7, 8, 10, 11],
            "Moon": [3, 6, 11],
            "Mars": [3, 5, 6, 10, 11, 12],
            "Mercury": [6, 8, 9, 10, 11, 12],
            "Jupiter": [5, 6, 11, 12],
            "Venus": [6, 11, 12],
            "Saturn": [3, 5, 6, 11],
            "Lagna": [1, 3, 4, 6, 10, 11]
        }
    }
    
    # Mapping planet names to index if needed, but we used names in main mock.
    
    @staticmethod
    def calculate_bav(candidate_planet: str, all_positions: Dict[str, int]) -> Dict[int, int]:
        """
        Calculates the BAV distribution (12 signs) for a given candidate planet (e.g. "Sun").
        
        Args:
           candidate_planet: The planet for which we are calculating BAV (e.g. "Sun" BAV).
           all_positions: Dict of {PlanetName: RashiIndex (1-12)}. 
                          MUST include "Lagna".
                          
        Returns:
            Dict {RashiIndex (1-12): 1 or 0} -> Does it get a bindu?
            WAIT: BAV is usually represented as: Rashi 1 has X points.
            But BAV for Sun means: "Contribution of ALL planets to Sun's BAV".
            
            NO, wait. 
            BAV of Sun (Sun's Ashtakavarga) = Sum of points given by Sun, Moon... etc. TOWARDS Sun.
            
            The RULES dict above: rules["Sun"]["Moon"] means:
            "In Sun's BAV, Moon gives points in houses X, Y, Z from Moon itself."
            
        """
        if candidate_planet not in BAVCalculator.RULES:
            return {}

        # Initialize 12 Rashis with 0
        bav_counts = {r: 0 for r in range(1, 13)}
        
        rules = BAVCalculator.RULES[candidate_planet]
        
        # Iterate through all contributors (Sun..Sat + Lagna)
        for donor, benefics in rules.items():
            if donor not in all_positions:
                continue
                
            donor_rashi = all_positions[donor] # 1-12
            
            for house_offset in benefics:
                # Calculate target rashi
                # If donor is in Rashi 1, and offset is 1, target is 1.
                # If donor is in Rashi 1, and offset is 2, target is 2.
                target_rashi = (donor_rashi + house_offset - 1) % 12
                if target_rashi == 0: target_rashi = 12
                
                bav_counts[target_rashi] += 1
                
        return bav_counts

    @staticmethod
    def calculate_sarvashtakavarga(all_positions_rashi: Dict[str, int]) -> Dict[int, Dict[str, int]]:
        """
        Calculates SAV for all 12 Rashis.
        Returns: { Rashi_ID: { "Sun": bindus_contributed_by_sun_rule_to_this_rashi... (Wait) } }
        
        Correction:
        SAV for a Rashi = Sum of (Sun's BAV in that Rashi + Moon's BAV in that Rashi ...)
        
        We need to calculate BAV for ALL 7 planets.
        Then sum them up per Rashi.
        
        Return format:
        {
            Rashi_ID (1-12): {
                 "total": int (SAV),
                 "bav_breakdown": { "Sun": int (bindus in Sun's BAV for this Rashi), ... }
            }
        }
        
        Wait, breakdown is usually:
        "In Aries, Sun contributes 1, Moon contributes 0..." 
        Actually, the "Contribution" concept is subtly different.
        
        Standard Output:
        Rashi 1 Total = 30.
        Composed of: Sun's BAV(in Rashi 1) + Moon's BAV(in Rashi 1) + ...
        
        So we iterate all 7 candidate planets.
        """
        
        rashi_totals = {r: {"total": 0, "breakdown": {}} for r in range(1, 13)}
        planets = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
        
        for p in planets:
            # Calculate p's BAV Chart
            p_bav = BAVCalculator.calculate_bav(p, all_positions_rashi)
            
            # Add to totals
            for r in range(1, 13):
                score = p_bav[r]
                rashi_totals[r]["total"] += score
                rashi_totals[r]["breakdown"][p] = score
                
        return rashi_totals
