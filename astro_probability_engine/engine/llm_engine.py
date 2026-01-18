
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
            
            # 4. Deep Stat Calculation (Simplified)
            def calculate_stat(element_boost, base=72):
                val = base + random.randint(8, 18)
                if element == element_boost: val += 12
                return min(98, val)

            willpower = calculate_stat("Fire")
            intellect = calculate_stat("Air")
            wealth_iq = calculate_stat("Earth")
            intuition = calculate_stat("Water")
            leadership = calculate_stat("Fire")
            empathy = calculate_stat("Water")

            # 5. Karmic Path & Power (Clean text, no raw data)
            karma_name = main_challenge['name'] if isinstance(main_challenge['name'], str) else "Inner Shadow"
            power_name = top_strength['name'] if isinstance(top_strength['name'], str) else "Hidden Potential"

            # 7. Final Blessing
            blessings = {
                "Fire": "Go forth and burn bright. Your passion is the light of the world.",
                "Earth": "Build your legacy with patience. You are the mountain.",
                "Air": "Let your ideas soar. Your mind is your wings.",
                "Water": "Flow with your intuition. Your depth is your strength.",
                "Ether": "Trust the unseen. You are guided by the stars."
            }
            blessing = blessings.get(element, blessings["Ether"])

            # 8. Final Output - CLEAN HTML (No raw markdown)
            final_narrative = f"""
<div style="text-align: center; margin-bottom: 30px;">
    <span style="font-size: 1.5rem; color: var(--gold); font-weight: 600;">Your Cosmic Match</span><br>
    <span style="font-size: 2rem; font-weight: 700; color: white;">{match['name']}</span>
    <p style="color: var(--text-secondary); font-style: italic;">"{match['trait']}"</p>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 30px;">
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Willpower</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{willpower}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Intellect</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{intellect}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Intuition</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{intuition}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Leadership</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{leadership}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Wealth IQ</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{wealth_iq}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.9rem; color: var(--text-secondary);">Empathy</div>
        <div style="font-size: 1.8rem; font-weight: bold; color: var(--gold);">{empathy}</div>
    </div>
</div>

<div style="background: rgba(107, 70, 193, 0.15); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
    <h4 style="color: var(--gold); margin: 0 0 10px 0;">⚔️ Your Quest</h4>
    <p style="margin: 0; line-height: 1.8;">Master the energy of <strong>{karma_name}</strong>. This is where your soul seeks growth.</p>
</div>

<div style="background: rgba(255, 215, 0, 0.08); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
    <h4 style="color: var(--gold); margin: 0 0 10px 0;">🌟 Your Superpower</h4>
    <p style="margin: 0; line-height: 1.8;">Lean into <strong>{power_name}</strong>. This is your path of least resistance to success.</p>
</div>

<p style="text-align: center; font-style: italic; color: var(--gold); font-size: 1.15rem; margin-top: 30px;">
    "{blessing}"
</p>
"""

            return final_narrative

        except Exception as e:
            # Fallback that never fails
            return f"### Universal Wisdom\nThe stars align in mysterious ways. Trust your intuition above all.\n(System Note: {str(e)})"
