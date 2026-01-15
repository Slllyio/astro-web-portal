"""
Simple test to verify ReportLab PDF generation works correctly
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Create a simple test PDF
pdf_filename = "test_report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

story = []
styles = getSampleStyleSheet()

# Add some content
story.append(Paragraph("Test Astrological Report", styles['Title']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("This is a test to verify PDF generation works.", styles['BodyText']))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("Date of Birth: 1989-10-12", styles['BodyText']))

# Build PDF
try:
    doc.build(story)
    print(f"✅ Test PDF created successfully: {pdf_filename}")
    print("Try opening this file. If it works, the issue is with the main app logic.")
except Exception as e:
    print(f"❌ Error creating PDF: {e}")
    import traceback
    traceback.print_exc()
