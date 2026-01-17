from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def test_render():
    # Mock data structure matching report.html expectations
    narrative = {
        "planetary_strength": {"Sun": 80, "Moon": 40},
        "dasha_periods": [{"planet": "Sun", "start_age": 20, "end_age": 26, "duration_years": 6}],
        "directional_strength": {
            "scores": {"East (Fire)": 150, "West (Air)": 120},
            "winner": "East (Fire)",
            "winner_score": 150
        },
        "remedies": [{"planet": "Moon", "strength": 40, "gemstone": "Pearl", "mantra": "Om", "color": "White", "day": "Mon"}],
        "yogas": [{"name": "Budhaditya", "desc": "Sun+Merc"}],
        "life_activation_windows": [{"entry_date": "2030", "planet": "Jupiter", "age": 40, "duration_months": 12, "significance": "High"}],
        "tithi_info": {"tithi": "Purnima", "meaning": "Full Moon"},
        "power_rank": {"kingmaker": "Sun"},
        "universal_identity": ["Sun: Identity"],
        "transit_timeline": []
    }
    
    dob = datetime(1990, 1, 1)
    numerology = {"day": 1, "destiny_reduced": 5, "rewards": [0, 8]}
    
    try:
        return render_template('report.html', narrative=narrative, dob=dob, numerology=numerology)
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == '__main__':
    with app.app_context():
        try:
            print(render_template('report.html', narrative=narrative, dob=dob, numerology=numerology))
            print("SUCCESS: Template rendered correctly")
        except Exception as e:
            print(f"FAILED: {e}")
