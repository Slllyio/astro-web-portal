from flask import Flask, render_template, request, send_file, jsonify
import sys
import os
import datetime
import tempfile
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

# Add current and engine directories to path for imports
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'astro_probability_engine'))

from astro_probability_engine.astrology.real_service import SkyfieldAstrologyService
from astro_probability_engine.engine.generator import MatrixGenerator
from astro_probability_engine.engine.purifier import ChartPurifier
from astro_probability_engine.engine.analyzer import MatrixAnalyzer
from astro_probability_engine.engine.interpreter import AstrologicalInterpreter

app = Flask(__name__)

def generate_astrological_report(dob):
    """
    Generates complete astrological report for given DOB.
    Returns: (narrative_dict, sample_count)
    """
# Initialize services globally to avoid reloading on every request
service = SkyfieldAstrologyService()
generator = MatrixGenerator(service)
purifier = ChartPurifier()
analyzer = MatrixAnalyzer()

def generate_astrological_report(dob):
    """
    Generates complete astrological report for given DOB.
    Returns: (narrative_dict, sample_count)
    """
    # Generate matrix
    matrix = generator.generate_matrix(dob)
    
    # Purify
    purifier.process_matrix(matrix)
    
    # Analyze with DOB for life activation windows
    results = analyzer.analyze(matrix, dob=dob)
    
    return results['narrative'], results['sample_count']

def convert_narrative_to_markdown(narrative, dob, sample_count):
    """
    Converts narrative dictionary to formatted markdown string.
    """
    lines = []
    lines.append("# Astrological Probability Report: Universal Signatures\n")
    lines.append(f"**Date of Analysis**: {dob.strftime('%Y-%m-%d')} | **Sample Size**: {sample_count} Charts\n")
    lines.append("This report identifies the *immutable astrological DNA* of this date.\n")
    lines.append("---\n")
    
    # I. Universal Identity
    lines.append("## I. The Universal Identity (Fixed Promise)\n")
    for item in narrative.get('universal_identity', []):
        parts = item.split(":", 1)
        if len(parts) == 2:
            lines.append(f"### {parts[0].strip()}\n")
            lines.append(parts[1].strip().replace("\n", "\n> ") + "\n")
    
    # II. Power Architecture
    lines.append("\n---\n")
    lines.append("## II. Planetary Power Architecture\n")
    
    if "power_rank" in narrative:
        pr = narrative["power_rank"]
        lines.append(f"### The Kingmaker: {pr['kingmaker'].split('(')[0].replace('**', '').strip()}\n")
        lines.append(f"> {pr['kingmaker']} {pr['insight']}\n")
    
    lines.append("\n### Strategic Citadels\n")
    for item in narrative.get('strategic_strengths', []):
        lines.append(f"- {item}\n")
        
    lines.append("\n### Karmic Bottlenecks\n")
    for item in narrative.get('karmic_challenges', []):
        lines.append(f"- {item}\n")
    
    # III. Transit Forecasting
    lines.append("\n---\n")
    lines.append("## III. Transit Forecasting (2026-2028)\n\n")
    lines.append("| Event | Date | Trend | Analysis |\n")
    lines.append("| :--- | :--- | :--- | :--- |\n")
    
    for item in narrative.get('transit_timeline', []):
        header = item['header'].split('(')[0].strip()
        date = item['header'].split('(')[1].replace(')', '').strip()
        trend = f"**{item['trend']}**"
        analysis = item['analysis']
        lines.append(f"| {header} | {date} | {trend} | {analysis} |\n")
    
    # IV. Elemental DNA
    lines.append("\n---\n")
    lines.append("## IV. The Elemental DNA\n")
    if "elemental_analysis" in narrative:
        elem = narrative["elemental_analysis"]
        lines.append(f"**Dominant Element**: {elem['dominant'].upper()} ({elem['percentage']}%)\n")
        lines.append(f"> {elem['insight']}\n")
    
    # V. Peak Potential Windows
    lines.append("\n---\n")
    lines.append("## V. Peak Potential Windows\n\n")
    lines.append("| Ascendant | Best Time | Score |\n")
    lines.append("| :--- | :--- | :--- |\n")
    for p in narrative.get('peak_times_table', []):
        lines.append(f"| **{p['ascendant']}** | {p['time']} | **{p['score']}** |\n")
    
    # VI. Hidden Dimensions
    lines.append("\n---\n")
    lines.append("## VI. Hidden Dimensions\n")
    
    dirs = narrative.get("directional_strength", {})
    if dirs:
        lines.append(f"### Directional Mastery: {dirs.get('winner', 'Unknown')}\n")
    
    yogas = narrative.get("yogas", [])
    if yogas:
        lines.append("\n### Universal Yogas\n")
        for y in yogas:
            lines.append(f"- **{y['name']}**: {y['desc']}\n")
    
    tithi = narrative.get("tithi_info", {})
    if tithi:
        lines.append(f"\n### Tithi: {tithi.get('tithi', 'Unknown')}\n")
        lines.append(f"> {tithi.get('meaning', '')}\n")
    
    # VII. Life Activation Windows
    life_windows = narrative.get("life_activation_windows", [])
    if life_windows:
        lines.append("\n---\n")
        lines.append("## VII. Life Activation Windows\n\n")
        lines.append("| Period | Planet → Zone | Age | Duration |\n")
        lines.append("| :--- | :--- | :--- | :--- |\n")
        
        interp = AstrologicalInterpreter()
        for w in life_windows:
            r_name = interp.RASHI_NATURE.get(w['target_rashi'], f"Rashi {w['target_rashi']}").split(":")[0]
            lines.append(f"| {w['entry_date']} | **{w['planet']}** → {r_name} | {w['age']} years | {w['duration_months']} months |\n")
    
    return ''.join(lines)

@app.route('/')
def index():
    """Render the main portal page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_report():
    """
    API endpoint to generate report.
    Expects JSON: {"dob": "YYYY-MM-DD"}
    Returns: Styled HTML report
    """
    try:
        data = request.get_json()
        dob_str = data.get('dob')
        
        if not dob_str:
            return jsonify({"error": "Date of birth is required"}), 400
        
        # Parse DOB
        dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date()
        
        # Generate narrative (THIS IS THE BOTTLENECK - takes ~60s)
        print(f"Generating report for {dob}...")
        narrative, sample_count = generate_astrological_report(dob)
        
        # Convert to markdown
        markdown_content = convert_narrative_to_markdown(narrative, dob, sample_count)
        
        # Convert markdown to HTML
        html_content = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
        
        # Add beautiful CSS styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Astrological Report - {dob_str}</title>
            <style>
                body {{
                    font-family: 'Georgia', 'Times New Roman', serif;
                    max-width: 900px;
                    margin: 40px auto;
                    padding: 20px;
                    line-height: 1.7;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: #333;
                }}
                .container {{
                    background: white;
                    padding: 50px;
                    border-radius: 15px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                }}
                h1 {{
                    color: #1a237e;
                    font-size: 2.5rem;
                    text-align: center;
                    border-bottom: 4px solid #3f51b5;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                h2 {{
                    color: #283593;
                    font-size: 1.8rem;
                    margin-top: 40px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid #5c6bc0;
                }}
                h3 {{
                    color: #3f51b5;
                    font-size: 1.3rem;
                    margin-top: 25px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 25px 0;
                    font-size: 0.95rem;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                th {{
                    background: linear-gradient(135deg, #3f51b5 0%, #5c6bc0 100%);
                    color: white;
                    padding: 15px;
                    text-align: left;
                    font-weight: 600;
                }}
                td {{
                    padding: 12px 15px;
                    border-bottom: 1px solid #e0e0e0;
                }}
                tr:nth-child(even) {{
                    background-color: #f8f9fa;
                }}
                tr:hover {{
                    background-color: #e8eaf6;
                    transition: background-color 0.3s ease;
                }}
                blockquote {{
                    background: #f5f5f5;
                    border-left: 5px solid #3f51b5;
                    padding: 15px 20px;
                    margin: 15px 0;
                    font-style: italic;
                    color: #555;
                }}
                hr {{
                    border: none;
                    height: 2px;
                    background: linear-gradient(90deg, transparent, #bdbdbd, transparent);
                    margin: 30px 0;
                }}
                strong {{
                    color: #1a237e;
                    font-weight: 600;
                }}
                ul {{
                    list-style: none;
                    padding-left: 0;
                }}
                li {{
                    padding: 8px 0;
                    padding-left: 30px;
                    position: relative;
                }}
                li:before {{
                    content: "✦";
                    position: absolute;
                    left: 5px;
                    color: #3f51b5;
                    font-size: 1.2rem;
                }}
                .print-btn {{
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: linear-gradient(135deg, #3f51b5 0%, #5c6bc0 100%);
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 25px;
                    cursor: pointer;
                    font-size: 1rem;
                    box-shadow: 0 4px 15px rgba(63, 81, 181, 0.4);
                    transition: transform 0.2s;
                }}
                .print-btn:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 6px 20px rgba(63, 81, 181, 0.6);
                }}
                @media print {{
                    body {{
                        background: white;
                    }}
                    .print-btn {{
                        display: none;
                    }}
                    .container {{
                        box-shadow: none;
                        padding: 0;
                    }}
                }}
            </style>
        </head>
        <body>
            <button class="print-btn" onclick="window.print()">🖨️ Print Report</button>
            <div class="container">
                {html_content}
            </div>
        </body>
        </html>
        """
        
        print(f"Report generated successfully!")
        
        # Return HTML directly
        return styled_html
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
