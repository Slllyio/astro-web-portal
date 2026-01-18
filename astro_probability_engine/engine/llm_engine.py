
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
            # 1. Extract Core Archetypes
            identity_traits = narrative_data.get("universal_identity", [])
            core_trait = identity_traits[0] if identity_traits else "Seeker"
            
            strengths = narrative_data.get("strategic_strengths", [])
            top_strength = strengths[0] if strengths else {"name": "Resilience", "desc": "Inner strength"}
            
            challenges = narrative_data.get("karmic_challenges", [])
            main_challenge = challenges[0] if challenges else {"name": "Shadow Work", "desc": "Overcoming obstacles"}
            
            element = narrative_data.get("elemental_analysis", {}).get("dominant", "Ether")
            
            # 2. Synthesize "The Soul's Blueprint"
            intro_templates = [
                f"Your soul has chosen the path of the **{core_trait}**. This lifetime is not accidental; it is a meticulously crafted stage for your evolution.",
                f"At your core, you carry the frequency of the **{core_trait}**. The universe has encoded this archetype into your very being.",
                f"You are walking the sacred path of the **{core_trait}**. This is your fundamental truth."
            ]
            intro = random.choice(intro_templates)

            # 3. Synthesize "The Karmic Path"
            karmic_templates = [
                f"Your greatest growth lies in mastering **{main_challenge['name']}**. {main_challenge['desc']}. It is not a punishment, but a gym for your spiritual muscles.",
                f"The cosmos challenges you through **{main_challenge['name']}**. {main_challenge['desc']}. Use this resistance to build your character.",
                f"Pay close attention to **{main_challenge['name']}**. {main_challenge['desc']}. This is where your gold is buried."
            ]
            karma = random.choice(karmic_templates)

            # 4. Synthesize "The Golden Key"
            strength_desc = top_strength.get('desc', 'your innate power') # Handle if it's a dict or extraction varies
            # Safe extraction if strength is just text or dict
            strength_name = top_strength['name'] if isinstance(top_strength, dict) else "Power"
            
            power_templates = [
                f"Your secret weapon is **{strength_name}**. When you lean into this energy, doors open. Use it wisely.",
                f"Unlock your destiny by embracing **{strength_name}**. It is your path of least resistance to success.",
                f"Trust in your **{strength_name}**. It is the wind in your sails."
            ]
            power = random.choice(power_templates)

            # 5. Final Blessing (Elemental)
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
                f"### AI Baba's Blessing\n*{blessing}*"
            )

            return final_narrative

        except Exception as e:
            return f"AI Baba is meditating on your complex chart... (Internal Synthesis Error: {str(e)})"
