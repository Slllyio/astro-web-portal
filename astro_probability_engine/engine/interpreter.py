
from typing import Dict, List, Any

class AstrologicalInterpreter:
    """
    Translates statistical data (scores, positions) into traditional
    astrological inferences and narratives.
    """

    # Knowledge Base (Simplified for the specific signatures we found, expandable)
    NAKSHATRA_NAMES = {
        1: "Ashwini", 2: "Bharani", 3: "Krittika", 4: "Rohini", 5: "Mrigashira",
        6: "Ardra", 7: "Punarvasu", 8: "Pushya", 9: "Ashlesha", 10: "Magha",
        11: "Purva Phalguni", 12: "Uttara Phalguni", 13: "Hasta", 14: "Chitra",
        15: "Swati", 16: "Vishakha", 17: "Anuradha", 18: "Jyeshtha", 19: "Mula",
        20: "Purva Ashadha", 21: "Uttara Ashadha", 22: "Shravana", 23: "Dhanishta",
        24: "Shatabhisha", 25: "Purva Bhadrapada", 26: "Uttara Bhadrapada", 27: "Revati"
    }
    
    NAKSHATRA_MEANINGS = {
        1: "Ashwini (The Horsemen): Swift action, healing, pioneering energy. Ruled by Ashwini Kumaras.",
        2: "Bharani (The Bearer): Power of restraint, carrying burden, transformation. Ruled by Yama.",
        3: "Krittika (The Cutter): Sharp discernment, burning, purification. Ruled by Agni.",
        4: "Rohini (The Red One): Growth, fertility, beauty, material desires. Ruled by Brahma.",
        5: "Mrigashira (The Deer's Head): Searching, exploration, restlessness, gentleness. Ruled by Soma.",
        6: "Ardra (The Moist One): Power of effort and achievement, often through storm/struggle. Ruled by Rudra.",
        7: "Punarvasu (The Return of Light): Renewal, restoration, repetition. Ruled by Aditi.",
        8: "Pushya (The Nourisher): Nourishment, support, spiritual growth. Ruled by Brihaspati.",
        9: "Ashlesha (The Embracer): Coiling energy, kundalini, secretive wisdom. Ruled by Nagas.",
        10: "Magha (The Mighty): Ancestral power, throne, regal authority. Ruled by Pitris.",
        11: "Purva Phalguni (The Former Red One): Pleasure, creativity, relationships. Ruled by Bhaga.",
        12: "Uttara Phalguni (The Latter Red One): Wealth through relationships, kindness, patronage. Ruled by Aryaman.",
        13: "Hasta (The Hand): Skilled hands, craftmanship, grasping nature. Ruled by Savitar.",
        14: "Chitra (The Bright): The Architect. Creativity, design, visual aesthetics. Ruled by Tvashtar.",
        15: "Swati (The Sword): Independence, flexibility, trade winds. Ruled by Vayu.",
        16: "Vishakha (The Forked Branch): Goal-oriented, determination, split energies. Ruled by Indra-Agni.",
        17: "Anuradha (The Disciple): Devotion, friendship, rising from ashes. Ruled by Mitra.",
        18: "Jyeshtha (The Eldest): Seniority, protection, umbrella, eldest child. Ruled by Indra.",
        19: "Mula (The Root): Foundational, digging deep, destruction before creation. Ruled by Nirriti.",
        20: "Purva Ashadha (The Invincible): Unbeatable execution, declaration of war, improvement. Ruled by Apah (Water).",
        21: "Uttara Ashadha (The Universal): Permanent victory, firm alliances. Ruled by Vishvadevas.",
        22: "Shravana (The Ear): Listening, learning, connection. Ruled by Vishnu.",
        23: "Dhanishta (The Wealthiest): Wealth, music, rhythm, fame. Ruled by Vasus.",
        24: "Shatabhisha (The Hundred Healers): Healing, secrecy, mystery. Ruled by Varuna.",
        25: "Purva Bhadrapada (The Former Happy Feet): Intensity, fire, spiritual transformation. Ruled by Aja Ekapada.",
        26: "Uttara Bhadrapada (The Latter Happy Feet): Depth, cosmic rain, serpent energy. Ruled by Ahir Budhnya.",
        27: "Revati (The Wealthy): Nourishment, safe journey, final liberation. Ruled by Pushan."
    }

    RASHI_NATURE = {
        1: "Aries (Mesha): Dynamic, pioneering, aggressive, head-strong.",
        2: "Taurus (Vrishabha): Stable, practical, artistic, stubborn.",
        3: "Gemini (Mithuna): Intellectual, versatile, communicative, dual-natured.",
        4: "Cancer (Karka): Emotional, nurturing, domestic, intuitive.",
        5: "Leo (Simha): Royal, creative, dramatic, egoistic.",
        6: "Virgo (Kanya): Analytical, critical, service-oriented, perfectionist.",
        7: "Libra (Tula): Diplomatic, balanced, artistic, indecisive.",
        8: "Scorpio (Vrishchika): Intense, secretive, transformative, magnetic.",
        9: "Sagittarius (Dhanu): Philosophical, optimistic, expansive, adventurous.",
        10: "Capricorn (Makara): Structural, ambitious, disciplined, public life.",
        11: "Aquarius (Kumbha): Innovative, humanitarian, eccentric, futuristic.",
        12: "Pisces (Meena): Dreamy, spiritual, compassionate, escapist."
    }

    PLANET_NATURE = {
        "Sun": {
            "karaka": "Atma Karaka (Soul), Pitru Karaka (Father), Rajya Karaka (Authority)",
            "desc": "Vitality, Ego, Leadership, and the 'Inner King'."
        },
        "Moon": {
            "karaka": "Matru Karaka (Mother), Mana Karaka (Mind)",
            "desc": "Emotions, Psychiatry, Public Interaction, and Peace of Mind."
        },
        "Mars": {
            "karaka": "Bhatru Karaka (Siblings), Bhumi Karaka (Land)",
            "desc": "Aggression, Logic, Engineering, Real Estate, and Willpower."
        },
        "Mercury": {
            "karaka": "Vidya Karaka (Knowledge), Vyavahara Karaka (Trade)",
            "desc": "Intellect, Communication, Analytics, Astrology, and Commerce."
        },
        "Jupiter": {
            "karaka": "Putra Karaka (Children), Dhana Karaka (Wealth), Jnana Karaka (Wisdom)",
            "desc": "Expansion, Luck, Spirituality, Teaching, and Optimism."
        },
        "Venus": {
            "karaka": "Kalatra Karaka (Spouse/Desire), Vahana Karaka (Vehicles)",
            "desc": "Love, Arts, Luxury, Diplomacy, and Reproductive Health."
        },
        "Saturn": {
            "karaka": "Ayush Karaka (Longevity), Karma Karaka (Profession)",
            "desc": "Discipline, Delay, Fear, Structure, Democracy, and Hard Labour."
        },
         "Rahu": {
            "karaka": "Maya Karaka (Illusion), Videsha Karaka (Foreign)",
            "desc": "Obsession, Unconventional Success, Technology, and Out-of-the-box thinking."
        },
         "Ketu": {
            "karaka": "Moksha Karaka (Liberation)",
            "desc": "Detachment, Spirituality, abstract mathematics, and sudden breaks."
        }
    }

    # Current Transits (Jan 2026 Reference)
    # Ideally this comes from a service, but for "Principles" demonstration we define the current context.
    CURRENT_TRANSITS = {
        "Saturn": 12,  # Pisces
        "Jupiter": 3,  # Gemini
        "Rahu": 11,    # Aquarius
        "Ketu": 5      # Leo
    }

    def predict_transit_impacts(self, rashi_data: Dict[str, Any]) -> List[str]:
        # Legacy method placeholder or remove if unused. 
        # Kept for compatibility but not primary anymore.
        pass

    # Future Major Transits (Hardcoded for Demo Accuracy)
    # Source: Standard Ephemeris
    FUTURE_TRANSITS = [
        {
            "planet": "Jupiter",
            "current_rashi": 3, # Gemini
            "next_rashi": 4,    # Cancer
            "transition_date": "2026-06-02", # Approx date
            "description": "Jupiter moves from Gemini to Cancer"
        },
        {
            "planet": "Saturn",
            "current_rashi": 12, # Pisces
            "next_rashi": 1,     # Aries
            "transition_date": "2028-02-23",
            "description": "Saturn moves from Pisces to Aries"
        },
        {
            "planet": "Rahu",
            "current_rashi": 11, # Aquarius
            "next_rashi": 10,    # Capricorn (Retrograde)
            "transition_date": "2026-10-17",
            "description": "Rahu moves from Aquarius to Capricorn"
        }
    ]

    def analyze_transit_shift(self, rashi_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Analyzes the SHIFT in fortune.
        """
        forecasts = []
        
        for transit in self.FUTURE_TRANSITS:
            p = transit['planet']
            # Use Integers for lookup as Analyzer produces Integer keys
            curr_r = int(transit['current_rashi'])
            next_r = int(transit['next_rashi'])
            
            # Get Karaka info
            karaka_info = self.PLANET_NATURE.get(p, {"karaka": "General factor", "desc": "Influence"})
            karaka_str = karaka_info['karaka']
            
            # Scores (Default to 25 if data missing)
            # Try both int and str to be safe, but Analyzer likely returns Int keys
            def get_score(rid):
                if rid in rashi_data: return rashi_data[rid].get('mean_score', 25)
                if str(rid) in rashi_data: return rashi_data[str(rid)].get('mean_score', 25)
                return 25
                
            curr_score = get_score(curr_r)
            next_score = get_score(next_r)
            
            # 1. Determine Zone Quality
            def get_zone_type(s):
                if s >= 30: return "GOLDEN"
                if s >= 25: return "AVERAGE"
                return "WEAK"
                
            curr_zone = get_zone_type(curr_score)
            next_zone = get_zone_type(next_score)
            
            # 2. Determine Trend Logic
            trend = ""
            details = ""
            
            if curr_zone == "GOLDEN" and next_zone == "GOLDEN":
                trend = "SUSTAINED PROSPERITY"
                details = (f"You are moving from one Powerhouse ({curr_score:.1f}) to another ({next_score:.1f}). "
                           f"This is a rare, extended period of high achievement for **{karaka_str}**. "
                           f"Expect consistent growth in {karaka_info['desc']}.")
            elif curr_zone == "WEAK" and next_zone == "WEAK":
                trend = "PROLONGED CHALLENGE"
                details = (f"The testing phase continues. You move from a low-energy zone ({curr_score:.1f}) to another ({next_score:.1f}). "
                           f"Matters related to **{karaka_str}** will require extra patience. "
                           f"Focus on preservation rather than expansion in {karaka_info['desc']}.")
            elif curr_zone == "WEAK" and next_zone == "GOLDEN":
                trend = "MAJOR BREAKTHROUGH"
                details = (f"Relief is here. You leave a struggle zone ({curr_score:.1f}) and enter a zone of abundance ({next_score:.1f}). "
                           f"This is a specific turning point for **{karaka_str}**. "
                           f"Expect sudden luck and expansion in {karaka_info['desc']}.")
            elif curr_zone == "GOLDEN" and next_zone == "WEAK":
                trend = "SUDDEN DROP / CAUTION"
                details = (f"Prepare for a cooldown. You leave a peak phase ({curr_score:.1f}) for a restrictive one ({next_score:.1f}). "
                           f"Protect your gains related to **{karaka_str}**. "
                           f"Do not take new risks in {karaka_info['desc']}.")
            elif next_score > curr_score:
                trend = "IMPROVING"
                details = (f"Conditions improve slightly ({curr_score:.1f} -> {next_score:.1f}). "
                           f"Better resource availability for **{karaka_str}**.")
            elif next_score < curr_score:
                trend = "DECLINING"
                details = (f"Conditions tighten slightly ({curr_score:.1f} -> {next_score:.1f}). "
                           f"Expect to work harder for benefits related to **{karaka_str}**.")
            else:
                trend = "STABLE"
                details = f"Conditions remain steady ({curr_score:.1f} -> {next_score:.1f}) for all matters of **{karaka_str}**."
                
            forecasts.append({
                "header": f"{transit['description']} ({transit['transition_date']})",
                "trend": trend,
                "current_score": curr_score,
                "next_score": next_score,
                "analysis": details,
                "karaka_context": karaka_info['karaka']
            })
            
        return forecasts

    # Tithi Meanings Map
    TITHI_MEANINGS = {
        "Pratipada": "The First Step. Good for planning and inception.",
        "Dwitiya": "Expansion. Good for laying foundations.",
        "Tritiya": "Energy/Power. Good for bold actions.",
        "Chaturthi": "Obstacle Removal. Good for overcoming enemies (but avoid good works).",
        "Panchami": "Healing/Lakshmi. Good for medicine and wealth.",
        "Shashthi": "Victory. Good for stubborn tasks.",
        "Saptami": "Health/Partnership. Good for journey and socializing.",
        "Ashtami": "Conflict/Strength. Good for battles, bad for auspicious start.",
        "Navami": "Aggression. Good for debating and competing.",
        "Dashami": "Virtue/Dharma. Good for noble deeds and government work.",
        "Ekadashi": "Fasting/Spirituality. Good for detox and prayer.",
        "Dwadashi": "Renown/Vision. Good for big goals and fame.",
        "Trayodashi": "Victory/Pradosha. Good for overcoming guilt and karma.",
        "Chaturdashi": "Cruelty/Force. Good for destructive actions or cleaning.",
        "Purnima": "Fullness/Completion. Peak creative energy.",
        "Amavasya": "Ancestors/Void. Good for meditation and secret works."
    }

    def generate_narrative(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates a comprehensive narrative report.
        """
        narrative = {
            "universal_identity": [],  # Common Links
            "strategic_strengths": [], # Rashi Scores (Detailed)
            "karmic_challenges": [],   # Weak Rashis (Detailed)
            "transit_timeline": []     # Future Forecast
        }
        
        # 1. Full Common Links Analysis
        common_links = analysis_results.get("common_links", {})
        nakshatras = common_links.get("nakshatra_positions", [])
        
        for item in nakshatras:
            planet = item['planet']
            nak_id = item['nakshatra_id']
            # Get Nakshatra name and full meaning
            nak_name = self.NAKSHATRA_NAMES.get(nak_id, f"Nakshatra {nak_id}")
            meaning = self.NAKSHATRA_MEANINGS.get(nak_id, f"Nakshatra {nak_id}")
            p_nature_info = self.PLANET_NATURE.get(planet, {"karaka": "Influence", "desc": "General Energy"})
            
            entry = (
                f"**{planet} in {nak_name}**: "
                f"\n   - *Core Theme*: {p_nature_info['karaka']} - {p_nature_info['desc']}"
                f"\n   - *Nakshatra Influence*: {meaning}"
                f"\n   - *Interpretation*: For everyone born on this day, {planet} operates through the lens of {nak_name}. "
                "This is a fixed trait of your generation/cohort."
            )
            narrative["universal_identity"].append(entry)
                
        # 2. Strategic Strengths & Challenges (Detailed Elaboration)
        rashi_data = analysis_results.get("rashi_analysis", {})
        sorted_rashis = sorted(rashi_data.items(), key=lambda x: x[1]['mean_score'], reverse=True)
        
        top3 = sorted_rashis[:3]
        bot3 = sorted_rashis[-3:]
        
        # Helper for Detailed Explanations
        def explain_strength(r_id, driver):
            # Dynamic text generation based on Rashi nature
            elem = "Fire" if r_id in [1,5,9] else "Earth" if r_id in [2,6,10] else "Air" if r_id in [3,7,11] else "Water"
            desc = "intuition and emotional connection." # Default for Water
            if elem == "Fire": desc = "action and initiative."
            elif elem == "Earth": desc = "tangible assets and stability."
            elif elem == "Air": desc = "ideas and networks."
            
            return (f"This zone is a natural powerhouse for you. Because it is supported by **{driver}**, "
                    f"efforts placed here yield maximum return with minimal friction. "
                    f"As a {elem} sign, expect results to manifest through {desc}")

        def explain_weakness(r_id, driver):
             elem = "Fire" if r_id in [1,5,9] else "Earth" if r_id in [2,6,10] else "Air" if r_id in [3,7,11] else "Water"
             impact = "growth/optimism" # Default
             if driver == "Mars": impact = "confidence/startups"
             elif driver == "Venus": impact = "money/relationships"
             elif driver == "Mercury": impact = "communication/contracts"
             elif driver == "Moon": impact = "emotional peace"
             elif driver == "Sun": impact = "authority/ego"
             elif driver == "Saturn": impact = "structure/career"
             elif driver == "Jupiter": impact = "growth/optimism"
             
             return (f"This is a 'Karmic Bottleneck'. The energy here is restricted or requires double the effort. "
                     f"Since **{driver}** is the ruler, you may face delays in matters of {impact}. "
                     "Remedial measure: Patience and deliberate planning.")

        for r_id_str, stats in top3:
            r_id = int(r_id_str)
            score = stats['mean_score']
            r_name = self.RASHI_NATURE.get(r_id, f"Rashi {r_id}")
            driver = stats['key_insights']['primary_driver']
            
            narrative["strategic_strengths"].append(
                f"**{r_name} (Score: {score:.1f})**: Top-Tier Zone.\n"
                f"> {explain_strength(r_id, driver)}"
            )

        for r_id_str, stats in bot3:
            r_id = int(r_id_str)
            score = stats['mean_score']
            if score < 26: 
                r_name = self.RASHI_NATURE.get(r_id, f"Rashi {r_id}")
                driver = stats['key_insights']['primary_driver']
                narrative["karmic_challenges"].append(
                    f"**{r_name} (Score: {score:.1f})**: Resistance Zone.\n"
                    f"> {explain_weakness(r_id, driver)}"
                )

        # 3. Kingmaker
        p_power = analysis_results.get("planet_power", {})
        if p_power:
            sorted_power = sorted(p_power.items(), key=lambda x: x[1], reverse=True)
            top_planet, top_score = sorted_power[0]
            p_nature = self.PLANET_NATURE.get(top_planet, {"karaka": "Influence", "desc": "Power"})
            narrative["power_rank"] = {
                "kingmaker": f"**{top_planet}** is the Kingmaker ({top_score} Bindus).",
                "insight": f"It is the single biggest contributor to the chart's strength. Success comes through {p_nature['desc']}"
            }

        # 4. Transit Timeline
        narrative["transit_timeline"] = self.analyze_transit_shift(rashi_data)
        
        # 5. Elemental Balance
        elem_counts = analysis_results.get("elemental_balance", {})
        total_planets = sum(elem_counts.values())
        if total_planets > 0:
            dominant_elem = max(elem_counts, key=elem_counts.get)
            percent = (elem_counts[dominant_elem] / total_planets) * 100
            desc_map = {
                "Fire": "Driven by action and intuition.",
                "Earth": "Focused on results and stability.",
                "Air": "Intellectual and social.",
                "Water": "Emotional and sensitive."
            }
            narrative["elemental_analysis"] = {
                "dominant": dominant_elem,
                "percentage": round(percent, 1),
                "insight": f"With {percent:.1f}% planets in {dominant_elem}, the core temperament is **{dominant_elem.upper()}**. {desc_map.get(dominant_elem, '')}"
            }
            
        # 6. Peak Times (Ascendant Scenarios)
        # Format as list of dicts: {asc, time, score}
        peak_raw = analysis_results.get("peak_times", [])
        peak_narrative = []
        for p in peak_raw:
            r_id = p['ascendant']
            r_name = self.RASHI_NATURE.get(r_id, f"Rashi {r_id}").split(":")[0] 
            peak_narrative.append({
                "ascendant": r_name,
                "time": p['time'],
                "score": p['score']
            })
        narrative["peak_times_table"] = peak_narrative

        # 7. Directional Strength
        narrative["directional_strength"] = analysis_results.get("directional_strength", {})
        
        # 8. Yogas
        narrative["yogas"] = analysis_results.get("yogas", [])
        
        # 9. Tithi
        tithi_data = analysis_results.get("tithi_info", {})
        tithi_name = tithi_data.get("tithi", "").split(" ")[0] # extract "Dwadashi"
        tithi_meaning = self.TITHI_MEANINGS.get(tithi_name, "A phase of the moon.")
        
        tithi_data["meaning"] = tithi_meaning
        narrative["tithi_info"] = tithi_data
        
        # 10. Life Activation Windows
        narrative["life_activation_windows"] = analysis_results.get("life_activation_windows", [])

        return narrative
