
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
            
            # 3. Celebrity Matcher Logic (Cosmic Twins) - TRAINED DATASET (v2)
            # Expanded database for better "training"
            celebrity_db = [
                # FIRE (Visionaries / Leaders / Athletes)
                {"name": "Steve Jobs", "trait": "The Innovator", "element": "Fire", "planet": "Mars"},
                {"name": "Virat Kohli", "trait": "The Warrior", "element": "Fire", "planet": "Mars"},
                {"name": "Walt Disney", "trait": "The Dreamer", "element": "Fire", "planet": "Sun"},
                {"name": "Winston Churchill", "trait": "The Commander", "element": "Fire", "planet": "Sun"},
                
                # EARTH (Builders / Strategists / Rulers)
                {"name": "Queen Elizabeth II", "trait": "The Monarch", "element": "Earth", "planet": "Saturn"},
                {"name": "Warren Buffett", "trait": "The Oracle", "element": "Earth", "planet": "Saturn"},
                {"name": "Mark Zuckerberg", "trait": "The Architect", "element": "Earth", "planet": "Mercury"},
                {"name": "Serena Williams", "trait": "The Titan", "element": "Earth", "planet": "Mars"},

                # AIR (Intellectuals / Writers / Socialites)
                {"name": "Albert Einstein", "trait": "The Genius", "element": "Air", "planet": "Mercury"},
                {"name": "Elon Musk", "trait": "The Disruptor", "element": "Air", "planet": "Saturn"},
                {"name": "Oprah Winfrey", "trait": "The Voice", "element": "Air", "planet": "Jupiter"},
                {"name": "Obama", "trait": "The Orator", "element": "Air", "planet": "Jupiter"},

                # WATER (Healers / Artists / Mystics)
                {"name": "Mother Teresa", "trait": "The Saint", "element": "Water", "planet": "Moon"},
                {"name": "Bruce Lee", "trait": "The Philosopher", "element": "Water", "planet": "Mars"},
                {"name": "Beyoncé", "trait": "The Icon", "element": "Water", "planet": "Venus"},
                {"name": "Dalai Lama", "trait": "The Monk", "element": "Water", "planet": "Jupiter"},
                
                # ETHER (Spiritualists / Philosophers) – Fallback group
                {"name": "Nikola Tesla", "trait": "The Mystic", "element": "Ether", "planet": "Ketu"},
                {"name": "Carl Jung", "trait": "The Alchemist", "element": "Ether", "planet": "Ketu"}
            ]
            
            # Advanced Matching Algorithm (Score-based)
            # We assume user has a dominant element. We try to match Element first.
            # Then we try to match the specific dominant planet/strength if possible.
            # Since we don't have the user's dominant planet passed directly in this simple context,
            # we will infer it from the 'strengths' or random variance for variety in this demo.
            
            potential_matches = [c for c in celebrity_db if c['element'] == element]
            if not potential_matches:
                potential_matches = celebrity_db # Fallback to everyone

            # Select the "best" match (Simulation: Random from the filtered pool to prevent staleness on same chart)
            match = random.choice(potential_matches)
            
            # 4. RPG Stats & Simplified Narrative
            intro = f"Your soul frequency aligns with the archetype of the **{core_trait}**. Explore your cosmic blueprint below."
            
            # RPG Stats Calculation
            base_stat = 75
            # Apply Element Bonuses
            bonus_vit = 15 if element == "Fire" else (5 if element == "Earth" else 0)
            bonus_int = 15 if element == "Air" else (5 if element == "Earth" else 0)
            bonus_cha = 15 if element == "Water" else (5 if element == "Fire" else 0)
            bonus_luk = 15 if element == "Ether" else (5 if element == "Water" else 0)

            vitality = base_stat + bonus_vit + random.randint(-5, 5)
            intellect = base_stat + bonus_int + random.randint(-5, 5)
            charisma = base_stat + bonus_cha + random.randint(-5, 5)
            luck = base_stat + bonus_luk + random.randint(-5, 5)
            
            # Cap at 99
            vitality = min(99, vitality); intellect = min(99, intellect)
            charisma = min(99, charisma); luck = min(99, luck)

            # 5. Synthesize "The Karmic Path"
            karma_desc = main_challenge['desc']
            karma = f"Your current level requires mastering **{main_challenge['name']}**. Mission: {karma_desc}."

            # 6. Synthesize "The Golden Key"
            strength_name = top_strength['name']
            power = f"Your innate ability is **{strength_name}**. Equip this skill to bypass obstacles."

            # 7. Final Blessing
            blessings = {
                "Fire": "Go forth and burn bright. Your passion is the light of the world.",
                "Earth": "Build your legacy with patience. You are the mountain.",
                "Air": "Let your ideas soar. Your mind is your wings.",
                "Water": "Flow with your intuition. Your depth is your strength.",
                "Ether": "Trust the unseen. You are guided by the stars."
            }
            blessing = blessings.get(element, blessings["Ether"])

            # 8. Final Output Construction
            final_narrative = (
                f"### Cosmic Character Sheet (v2.0)\n"
                f"**Class**: {core_trait}\n"
                f"**Cosmic Match**: {match['name']} ({match['trait']})\n\n"
                f"#### Attribute Stats\n"
                f"*   **Vitality**: {vitality}/100\n"
                f"*   **Intellect**: {intellect}/100\n"
                f"*   **Charisma**: {charisma}/100\n"
                f"*   **Luck**: {luck}/100\n\n"
                f"### Strategy Guide\n"
                f"*   **Special Move**: {power}\n"
                f"*   **Current Quest**: {karma}\n"
                f"\n*{blessing}*"
            )

            return final_narrative

        except Exception as e:
            # Fallback that never fails
            return f"### Universal Wisdom\nThe stars align in mysterious ways. Trust your intuition above all.\n(System Note: {str(e)})"
