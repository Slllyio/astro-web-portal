
from typing import List, Dict
from engine.models import MatrixEntry, ChartData, HouseData

# Rashi Multipliers (1=Aries to 12=Pisces)
RASHI_MULTIPLIERS = [7, 10, 8, 4, 10, 5, 7, 8, 9, 5, 11, 12]

class ChartPurifier:
    def process_matrix(self, matrix: List[MatrixEntry]):
        """
        Phase 2: Purification.
        Updates each chart in the matrix with Shodhya Pinda values.
        """
        for entry in matrix:
            self.purify_chart(entry.chart)

    def purify_chart(self, chart: ChartData):
        # 1. Extract SAV scores mapped by Rashi ID
        rashi_scores = {h.rashi_id: h.sav_score for h in chart.houses.values()}
        
        # 2. Perform Trikona Shodhana (Triangular Reduction)
        # Groups: (1,5,9), (2,6,10), (3,7,11), (4,8,12)
        purified_scores = rashi_scores.copy()
        
        for start_rashi in range(1, 5): # 1, 2, 3, 4
            group = [start_rashi, start_rashi + 4, start_rashi + 8]
            scores = [purified_scores[r] for r in group]
            min_score = min(scores)
            
            # Subtract min from all (Reduction)
            for r in group:
                purified_scores[r] -= min_score
                
        # 3. Perform Ekadhipatya Shodhana (Dual Lordship)
        # Simplified: If planets are in their own signs, etc. 
        # For this Engine Proof-of-Concept, we'll skip the complex conditional logic 
        # and assume Trikona is the primary reductor for "Pure Potential".
        # We will keep purified_scores as is from Trikona for now.
        
        # 4. Calculate Shodhya Pinda (Pure Potential)
        # Formula here: Purified Score * Rashi Multiplier
        # (ignoring Planet Multiplier for SAV-based simplification)
        
        for h_num, house in chart.houses.items():
            r_id = house.rashi_id
            p_score = purified_scores[r_id]
            multiplier = RASHI_MULTIPLIERS[r_id - 1]
            
            # Store the final value
            house.shodhya_pinda = p_score * multiplier
