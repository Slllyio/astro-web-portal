
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
            
            # 4. Synthesize "The Soul's Blueprint"
            intro_templates = [
                f"Your soul has chosen the path of the **{core_trait}**. This lifetime is a stage for your evolution.",
                f"At your core, you carry the frequency of the **{core_trait}**. The universe has encoded this into your being.",
                f"You are walking the sacred path of the **{core_trait}**. This is your fundamental truth."
            ]
            intro = random.choice(intro_templates)

            # 5. Synthesize "The Karmic Path"
            karmic_templates = [
                f"Your greatest growth lies in mastering **{main_challenge['name']}**. {main_challenge['desc']}. It is a gym for your spiritual muscles.",
                f"The cosmos challenges you through **{main_challenge['name']}**. Use this resistance to build character.",
                f"Pay close attention to **{main_challenge['name']}**. {main_challenge['desc']}."
            ]
            karma = random.choice(karmic_templates)

            # 6. Synthesize "The Golden Key"
            strength_name = top_strength['name']
            power_templates = [
                f"Your secret weapon is **{strength_name}**. When you lean into this energy, doors open.",
                f"Unlock your destiny by embracing **{strength_name}**. It is your path of least resistance.",
                f"Trust in your **{strength_name}**."
            ]
            power = random.choice(power_templates)

            # 7. Final Blessing & Celebrity Match
            blessings = {
                "Fire": "Go forth and burn bright. Your passion is the light of the world.",
                "Earth": "Build your legacy with patience. You are the mountain.",
                "Air": "Let your ideas soar. Your mind is your wings.",
                "Water": "Flow with your intuition. Your depth is your strength.",
                "Ether": "Trust the unseen. You are guided by the stars."
            }
            blessing = blessings.get(element, blessings["Ether"])

            # Combine
            final_narrative = (
                f"### The Core Essence\n{intro}\n\n"
                f"### The Karmic Path\n{karma}\n\n"
                f"### The Golden Key\n{power}\n\n"
                f"### Cosmic Twin\nYou share a spiritual lineage with **{match['name']}** ({match['trait']}). Like them, your power lies in the element of **{element}**.\n\n"
                f"### AI Baba's Blessing\n*{blessing}*"
            )

            return final_narrative

        except Exception as e:
            # Fallback that never fails
            return f"### Universal Wisdom\nThe stars align in mysterious ways. Trust your intuition above all.\n(System Note: {str(e)})"
