import sys
import os
import datetime

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.join(BASE_DIR, 'astro_probability_engine')
sys.path.append(BASE_DIR)
sys.path.append(ENGINE_DIR)

try:
    from astro_probability_engine.astrology.real_service import SkyfieldAstrologyService
    from astro_probability_engine.engine.generator import MatrixGenerator
    
    print("Imports successful.")

    # check for ephemeris
    if os.path.exists('de421.bsp'):
        print("Ephemeris file found.")
    else:
        print("WARNING: de421.bsp NOT found.")

    service = SkyfieldAstrologyService()
    generator = MatrixGenerator(service)
    
    dob = datetime.date(1990, 1, 1)
    matrix = generator.generate_matrix(dob)
    print("Matrix generation successful.")
    print(f"Matrix keys: {list(matrix.keys())}")

except Exception as e:
    print(f"Verification FAILED: {e}")
    import traceback
    traceback.print_exc()
