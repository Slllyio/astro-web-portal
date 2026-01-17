
import os
from typing import Dict, Any, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class LLMEngine:
    def __init__(self, api_key: str):
        if not OpenAI:
            raise ImportError("OpenAI library not installed")
        if not api_key:
            raise ValueError("API Key required")
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini" # Cost-effective but smart

    def generate_insight(self, narrative_data: Dict[str, Any]) -> str:
        """
        Generates a cosmic narrative based on the analyzed data.
        """
        try:
            # Construct a comprehensive prompt
            system_prompt = (
                "You are 'AI Baba', a mystical yet technologically advanced Vedic Astrologer. "
                "Synthesize the provided chart data into a profound, spiritual, and actionable life reading. "
                "Do not list technical placements dryly. Instead, weave a story. "
                "Use the 'Soul Code' (Universal Identity), 'Karmic Structure' (Saturn/Rahu/Ketu), "
                "and 'Power Centers' (Strengths) to guide the user. "
                "Tone: Warm, wise, slightly enigmatic but very clear on advice. "
                "Structure: "
                "1. The Core Essence (Who you are at a soul level) "
                "2. The Karmic Path (Challenges and their purpose) "
                "3. The Golden Key (How to unlock success) "
                "4. Final Blessing."
            )

            # Extract full context
            context = {
                "identity": narrative_data.get("universal_identity", []), 
                "strengths": narrative_data.get("strategic_strengths", []),
                "challenges": narrative_data.get("karmic_challenges", []),
                "planetary_strength": narrative_data.get("planetary_strength", {}),
                "dasha_periods": narrative_data.get("dasha_periods", []),
                "element": narrative_data.get("elemental_analysis", {}),
                "yogas": [y['name'] for y in narrative_data.get("yogas", [])],
                "kingmaker": narrative_data.get("power_rank", {}),
                "tithi": narrative_data.get("tithi_info", {}),
                "directions": narrative_data.get("directional_strength", {}).get("winner", "Unknown")
            }

            user_prompt = f"Analyze this birth chart data:\n{str(context)}\n\nSpeak as AI Baba."

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"LLM Generation Error: {e}")
            return "AI Baba is meditating (Service Unavailable - Check API Key)."
