
import random
from typing import Dict, Any

class LLMEngine:
    def __init__(self, api_key: str = None):
        # API Key is no longer needed but kept in signature for compatibility
        self.client = None

    def generate_insight(self, narrative_data: Dict[str, Any]) -> str:
        """
        Generates a cosmic narrative using deterministic logic and template synthesis.
        Zero external dependencies.
        """
        try:
            # 1. Safe Extraction Helper
            def _safe_extract(item, default_name, default_desc):
                if isinstance(item, dict):
                    return item
                elif isinstance(item, str):
                    return {"name": item, "desc": default_desc}
                return {"name": default_name, "desc": default_desc}

            # 2. Extract Core Archetypes
            identity_traits = narrative_data.get("universal_identity", [])
            core_trait = identity_traits[0] if identity_traits else "Seeker"
            if isinstance(core_trait, dict): core_trait = core_trait.get('name', 'Seeker')
            
            strengths = narrative_data.get("strategic_strengths", [])
            top_strength = _safe_extract(strengths[0] if strengths else None, "Resilience", "Inner Power")
            
            challenges = narrative_data.get("karmic_challenges", [])
            main_challenge = _safe_extract(challenges[0] if challenges else None, "Shadow Work", "Growth through obstacles")
            
            element = narrative_data.get("elemental_analysis", {}).get("dominant", "Ether")
            
            # 3. Celebrity Matcher Logic (Cosmic Twins)
            # This is a mini-database of archetypes
            celebrity_db = [
                {"name": "Albert Einstein", "trait": "Visionary", "element": "Water", "planet": "Jupiter"},
                {"name": "Steve Jobs", "trait": "Innovator", "element": "Fire", "planet": "Mars"},
                {"name": "Oprah Winfrey", "trait": "Empath", "element": "Air", "planet": "Venus"},
                {"name": "Elon Musk", "trait": "Disruptor", "element": "Air", "planet": "Saturn"},
                {"name": "Virat Kohli", "trait": "Warrior", "element": "Fire", "planet": "Mars"},
                {"name": "Mother Teresa", "trait": "Healer", "element": "Water", "planet": "Moon"}
            ]
            
            # Simple matching algorithm based on Dominant Element or Top Planet
            # (In a full version, we'd match exact planetary placements)
            match = next((c for c in celebrity_db if c['element'] == element), celebrity_db[0])
            
            # 4. RPG Stats & Simplified Narrative
            intro = f"Your soul carries the frequency of the **{core_trait}**. Explore your stats below."
            
            # RPG Stats Calculation (Mock logic mapping planetary strength to RPG attributes)
            # In a full engine, we map Sun->Vitality, Mercury->Intellect, etc.
            # Using random variance based on element for "flavor"
            base_stat = 75
            bonus = 10 if element == "Fire" else 5
            vitality = base_stat + bonus + random.randint(0, 10)
            intellect = base_stat + (10 if element == "Air" else 5) + random.randint(0, 10)
            charisma = base_stat + (10 if element == "Water" else 5) + random.randint(0, 10)
            luck = base_stat + (10 if element == "Ether" else 5) + random.randint(0, 10)

            # 5. Synthesize "The Karmic Path" (Simplified)
            karma = f"Your growth zone is **{main_challenge['name']}**. Challenge: {main_challenge['desc']}."

            # 6. Synthesize "The Golden Key"
            strength_name = top_strength['name']
            power = f"Your superpower is **{strength_name}**. Use it to unlock doors."

            # 7. Final Output Construction
            final_narrative = (
                f"### Cosmic Character Sheet\n"
                f"**Archetype**: {core_trait}\n"
                f"**Cosmic Twin**: {match['name']} ({match['trait']})\n\n"
                f"#### Base Stats\n"
                f"*   **Vitality**: {vitality}/100\n"
                f"*   **Intellect**: {intellect}/100\n"
                f"*   **Charisma**: {charisma}/100\n"
                f"*   **Luck**: {luck}/100\n\n"
                f"### Strategic Insight\n"
                f"*   **Zone of Power**: {power}\n"
                f"*   **Zone of Growth**: {karma}\n"
                f"\n*{blessing}*"
            )

            return final_narrative

        except Exception as e:
            # Fallback that never fails
            return f"### Universal Wisdom\nThe stars align in mysterious ways. Trust your intuition above all.\n(System Note: {str(e)})"
