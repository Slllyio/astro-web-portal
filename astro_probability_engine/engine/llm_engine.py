import random
from typing import Dict, Any

class LLMEngine:
    """
    Native AI Engine v4.0 - Deep Data-Driven Analysis
    Uses: Shad Bala, Yogas, Nakshatras, Dashas
    """
    
    # 27 Nakshatra Archetypes (The "Soul Code")
    NAKSHATRA_ARCHETYPES = {
        "Ashwini": ("The Healer", "Swift action and miraculous recovery"),
        "Bharani": ("The Bearer", "Transformation through intense experiences"),
        "Krittika": ("The Cutter", "Purification through fire and truth"),
        "Rohini": ("The Creator", "Fertility, beauty, and material abundance"),
        "Mrigashira": ("The Seeker", "Endless curiosity and the search for meaning"),
        "Ardra": ("The Storm", "Destruction that leads to renewal"),
        "Punarvasu": ("The Returner", "Renewal, restoration, and second chances"),
        "Pushya": ("The Nurturer", "Nourishment, teaching, and inner strength"),
        "Ashlesha": ("The Serpent", "Hidden power, mysticism, and transformation"),
        "Magha": ("The Throne", "Ancestral power and royal lineage"),
        "Purva Phalguni": ("The Artist", "Creativity, romance, and pleasure"),
        "Uttara Phalguni": ("The Patron", "Generosity, contracts, and partnerships"),
        "Hasta": ("The Craftsman", "Skill, dexterity, and manifestation"),
        "Chitra": ("The Architect", "Beauty, design, and structural perfection"),
        "Swati": ("The Wind", "Independence, flexibility, and trade"),
        "Vishakha": ("The Conqueror", "Focused ambition and triumph"),
        "Anuradha": ("The Devotee", "Friendship, devotion, and success abroad"),
        "Jyeshtha": ("The Elder", "Seniority, protection, and occult power"),
        "Mula": ("The Root", "Destruction of illusion, reaching the source"),
        "Purva Ashadha": ("The Invincible", "Unshakeable conviction and victory"),
        "Uttara Ashadha": ("The Universal", "Final victory through dharma"),
        "Shravana": ("The Listener", "Learning, connection, and fame"),
        "Dhanishta": ("The Drummer", "Wealth, music, and group harmony"),
        "Shatabhisha": ("The Healer", "Secrecy, healing, and aquatic energy"),
        "Purva Bhadrapada": ("The Scorcher", "Intensity, penance, and transformation"),
        "Uttara Bhadrapada": ("The Warrior", "Depth, wisdom, and cosmic protection"),
        "Revati": ("The Nurturer", "Safe travel, prosperity, and completion")
    }
    
    # Celebrity Database with Deep Stats for Matching
    CELEBRITY_DB = [
        # FIRE DOMINANT (High Willpower, Leadership)
        {"name": "Steve Jobs", "trait": "The Innovator", "element": "Fire", "nakshatra": "Purva Phalguni",
         "stats": {"willpower": 92, "intellect": 88, "intuition": 65, "leadership": 95, "wealth_iq": 85, "empathy": 55}},
        {"name": "Virat Kohli", "trait": "The Warrior", "element": "Fire", "nakshatra": "Jyeshtha",
         "stats": {"willpower": 95, "intellect": 70, "intuition": 60, "leadership": 88, "wealth_iq": 75, "empathy": 65}},
        {"name": "Walt Disney", "trait": "The Dreamer", "element": "Fire", "nakshatra": "Rohini",
         "stats": {"willpower": 85, "intellect": 78, "intuition": 80, "leadership": 82, "wealth_iq": 90, "empathy": 75}},
        {"name": "Amitabh Bachchan", "trait": "The Star", "element": "Fire", "nakshatra": "Swati",
         "stats": {"willpower": 88, "intellect": 75, "intuition": 72, "leadership": 85, "wealth_iq": 78, "empathy": 80}},
        
        # AIR DOMINANT (High Intellect)
        {"name": "Albert Einstein", "trait": "The Genius", "element": "Air", "nakshatra": "Punarvasu",
         "stats": {"willpower": 75, "intellect": 98, "intuition": 85, "leadership": 60, "wealth_iq": 55, "empathy": 70}},
        {"name": "Elon Musk", "trait": "The Disruptor", "element": "Air", "nakshatra": "Ardra",
         "stats": {"willpower": 90, "intellect": 95, "intuition": 70, "leadership": 85, "wealth_iq": 92, "empathy": 45}},
        {"name": "Oprah Winfrey", "trait": "The Voice", "element": "Air", "nakshatra": "Shravana",
         "stats": {"willpower": 85, "intellect": 82, "intuition": 88, "leadership": 90, "wealth_iq": 88, "empathy": 95}},
        {"name": "APJ Abdul Kalam", "trait": "The Missile Man", "element": "Air", "nakshatra": "Ashwini",
         "stats": {"willpower": 90, "intellect": 92, "intuition": 85, "leadership": 88, "wealth_iq": 50, "empathy": 90}},
        
        # EARTH DOMINANT (High Wealth IQ, Leadership)
        {"name": "Warren Buffett", "trait": "The Oracle", "element": "Earth", "nakshatra": "Dhanishta",
         "stats": {"willpower": 80, "intellect": 90, "intuition": 88, "leadership": 75, "wealth_iq": 98, "empathy": 65}},
        {"name": "Ratan Tata", "trait": "The Patriarch", "element": "Earth", "nakshatra": "Magha",
         "stats": {"willpower": 85, "intellect": 82, "intuition": 75, "leadership": 90, "wealth_iq": 92, "empathy": 88}},
        
        # WATER DOMINANT (High Intuition, Empathy)
        {"name": "Mother Teresa", "trait": "The Saint", "element": "Water", "nakshatra": "Pushya",
         "stats": {"willpower": 92, "intellect": 70, "intuition": 95, "leadership": 80, "wealth_iq": 40, "empathy": 98}},
        {"name": "Beyoncé", "trait": "The Icon", "element": "Water", "nakshatra": "Rohini",
         "stats": {"willpower": 88, "intellect": 75, "intuition": 85, "leadership": 82, "wealth_iq": 90, "empathy": 85}},
        {"name": "Dalai Lama", "trait": "The Monk", "element": "Water", "nakshatra": "Uttara Bhadrapada",
         "stats": {"willpower": 88, "intellect": 85, "intuition": 98, "leadership": 85, "wealth_iq": 45, "empathy": 95}},
        {"name": "Rabindranath Tagore", "trait": "The Poet", "element": "Water", "nakshatra": "Mrigashira",
         "stats": {"willpower": 70, "intellect": 92, "intuition": 95, "leadership": 65, "wealth_iq": 55, "empathy": 90}},
        
        # ETHER (Balanced/Mystical)
        {"name": "Nikola Tesla", "trait": "The Mystic", "element": "Ether", "nakshatra": "Ardra",
         "stats": {"willpower": 85, "intellect": 98, "intuition": 95, "leadership": 50, "wealth_iq": 30, "empathy": 60}},
    ]

    def __init__(self, api_key: str = None):
        self.client = None

    def generate_insight(self, narrative_data: Dict[str, Any]) -> str:
        try:
            # ============= 1. EXTRACT RAW DATA =============
            # Planetary Strength (Shad Bala)
            planetary_strength = narrative_data.get("planetary_strength", {})
            
            # Yogas
            yogas = narrative_data.get("yogas", [])
            
            # Dasha
            dasha_periods = narrative_data.get("dasha_periods", [])
            current_dasha = dasha_periods[0] if dasha_periods else {"planet": "Unknown", "years": "N/A"}
            
            # Element
            elemental = narrative_data.get("elemental_analysis", {})
            element = elemental.get("dominant", "Ether")
            
            # Moon Nakshatra (from universal_identity)
            identity = narrative_data.get("universal_identity", [])
            moon_nakshatra = "Ashwini"  # Default
            for entry in identity:
                if "Moon in" in entry:
                    # Extract nakshatra name from "**Moon in Rohini**"
                    parts = entry.split("Moon in ")
                    if len(parts) > 1:
                        moon_nakshatra = parts[1].split("**")[0].strip()
                    break
            
            # ============= 2. DATA-DRIVEN STATS (Using Real Shad Bala) =============
            def get_strength(planet, default=50):
                val = planetary_strength.get(planet, default)
                if isinstance(val, str):
                    try: val = float(val)
                    except: val = default
                return min(98, max(20, int(val)))
            
            sun = get_strength("Sun")
            moon = get_strength("Moon")
            mars = get_strength("Mars")
            mercury = get_strength("Mercury")
            jupiter = get_strength("Jupiter")
            venus = get_strength("Venus")
            saturn = get_strength("Saturn")
            
            # Calculate Stats from Real Planetary Strength
            willpower = int((sun + mars) / 2)
            intellect = int((mercury + jupiter) / 2)
            wealth_iq = int((jupiter + venus) / 2)
            intuition = int((moon + saturn) / 2)  # Moon + Saturn = Deep Intuition
            leadership = int((sun + saturn) / 2)
            empathy = int((venus + moon) / 2)
            
            # ============= 3. YOGA-BASED SCORING =============
            yoga_bonus = {"leadership": 0, "wealth": 0, "intellect": 0, "fame": 0}
            yoga_names = []
            for yoga in yogas:
                name = yoga.get("name", "") if isinstance(yoga, dict) else str(yoga)
                yoga_names.append(name)
                if "Raj" in name or "Raja" in name:
                    yoga_bonus["leadership"] += 12
                if "Dhan" in name or "Wealth" in name:
                    yoga_bonus["wealth"] += 12
                if "Budh" in name or "Mercury" in name:
                    yoga_bonus["intellect"] += 10
                if "Gaja" in name or "Kesari" in name:
                    yoga_bonus["fame"] += 10
            
            leadership += yoga_bonus["leadership"]
            wealth_iq += yoga_bonus["wealth"]
            intellect += yoga_bonus["intellect"]
            
            # Cap all stats
            willpower = min(98, willpower)
            intellect = min(98, intellect)
            wealth_iq = min(98, wealth_iq)
            intuition = min(98, intuition)
            leadership = min(98, leadership)
            empathy = min(98, empathy)
            
            # ============= 4. NAKSHATRA ARCHETYPE =============
            archetype_data = self.NAKSHATRA_ARCHETYPES.get(moon_nakshatra, ("The Seeker", "Endless curiosity"))
            archetype_name = archetype_data[0]
            archetype_desc = archetype_data[1]
            
            # ============= 5. CELEBRITY MATCHING (Stat-Based Similarity) =============
            # Calculate similarity score based on stat difference (lower = better match)
            user_stats = {
                "willpower": willpower, "intellect": intellect, "intuition": intuition,
                "leadership": leadership, "wealth_iq": wealth_iq, "empathy": empathy
            }
            
            best_match = self.CELEBRITY_DB[0]
            best_similarity = float('inf')
            
            for celeb in self.CELEBRITY_DB:
                celeb_stats = celeb.get("stats", {})
                if not celeb_stats:
                    continue
                    
                # Euclidean distance across all 6 stats
                distance = 0
                for stat_name in user_stats:
                    user_val = user_stats[stat_name]
                    celeb_val = celeb_stats.get(stat_name, 70)
                    distance += (user_val - celeb_val) ** 2
                
                # Add element bonus (favor same element)
                if celeb["element"] == element:
                    distance -= 500  # Significant bonus for element match
                
                if distance < best_similarity:
                    best_similarity = distance
                    best_match = celeb
            
            # Calculate match percentage (inverse of distance, normalized)
            match_pct = max(0, min(99, int(100 - (best_similarity ** 0.5) / 2)))
            
            # ============= 6. DASHA-AWARE ADVICE =============
            dasha_planet = current_dasha.get("planet", "Unknown")
            dasha_advice_map = {
                "Sun": "Focus on leadership, recognition, and self-expression.",
                "Moon": "Nurture your emotional world. Home and family are key.",
                "Mars": "Channel your energy into action. Avoid conflicts.",
                "Mercury": "Communication and learning are highlighted. Network!",
                "Jupiter": "Expand, teach, and embrace spiritual growth.",
                "Venus": "Art, love, and luxury are favored. Enjoy beauty.",
                "Saturn": "Discipline, patience, and long-term goals are essential.",
                "Rahu": "Embrace the unconventional. Take calculated risks.",
                "Ketu": "Spiritual detachment and past-life insights emerge."
            }
            dasha_advice = dasha_advice_map.get(dasha_planet, "Trust the cosmic timing.")
            
            # ============= 7. GENERATE CLEAN HTML OUTPUT =============
            # Blessings
            blessings = {
                "Fire": "Go forth and burn bright. Your passion is the light of the world.",
                "Earth": "Build your legacy with patience. You are the mountain.",
                "Air": "Let your ideas soar. Your mind is your wings.",
                "Water": "Flow with your intuition. Your depth is your strength.",
                "Ether": "Trust the unseen. You are guided by the stars."
            }
            blessing = blessings.get(element, blessings["Ether"])
            
            # Format Yoga list
            yoga_display = ", ".join(yoga_names[:3]) if yoga_names else "No major yogas detected"
            
            final_html = f"""
<div style="text-align: center; margin-bottom: 25px;">
    <span style="font-size: 1.1rem; color: var(--text-secondary);">Your Soul Archetype</span><br>
    <span style="font-size: 2.2rem; font-weight: 700; color: var(--gold);">{archetype_name}</span>
    <p style="color: var(--text-secondary); font-style: italic; margin-top: 5px;">"{archetype_desc}"</p>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 25px;">
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Willpower</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{willpower}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Intellect</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{intellect}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Intuition</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{intuition}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Leadership</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{leadership}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Wealth IQ</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{wealth_iq}</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 15px; text-align: center;">
        <div style="font-size: 0.85rem; color: var(--text-secondary);">Empathy</div>
        <div style="font-size: 1.6rem; font-weight: bold; color: var(--gold);">{empathy}</div>
    </div>
</div>

<div style="background: rgba(107, 70, 193, 0.15); border-radius: 12px; padding: 18px; margin-bottom: 15px;">
    <h4 style="color: var(--gold); margin: 0 0 8px 0; font-size: 1rem;">🌟 Your Cosmic Twin</h4>
    <p style="margin: 0; font-size: 1.1rem;"><strong>{best_match['name']}</strong> <span style="color: var(--text-secondary);">({best_match['trait']})</span></p>
</div>

<div style="background: rgba(255, 215, 0, 0.08); border-radius: 12px; padding: 18px; margin-bottom: 15px;">
    <h4 style="color: var(--gold); margin: 0 0 8px 0; font-size: 1rem;">⏳ Current Life Period: {dasha_planet}</h4>
    <p style="margin: 0; line-height: 1.7;">{dasha_advice}</p>
</div>

<div style="background: rgba(255, 255, 255, 0.03); border-radius: 12px; padding: 18px; margin-bottom: 15px;">
    <h4 style="color: var(--gold); margin: 0 0 8px 0; font-size: 1rem;">✨ Active Yogas</h4>
    <p style="margin: 0; color: var(--text-secondary);">{yoga_display}</p>
</div>

<p style="text-align: center; font-style: italic; color: var(--gold); font-size: 1.1rem; margin-top: 25px;">
    "{blessing}"
</p>
"""
            return final_html

        except Exception as e:
            return f"""
<div style="text-align: center; padding: 30px;">
    <p style="color: var(--gold); font-size: 1.2rem;">The stars align in mysterious ways.</p>
    <p style="color: var(--text-secondary); font-size: 0.9rem;">Trust your intuition above all.</p>
    <p style="color: #888; font-size: 0.75rem; margin-top: 15px;">(Debug: {str(e)})</p>
</div>
"""
