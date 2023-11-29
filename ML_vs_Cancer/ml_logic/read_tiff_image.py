import tifffile
import numpy as np

def read_tiff_image(file):
    try:
        # Read the TIFF image using tifffile
        tiff_data = tifffile.imread(file)

        # Convert to NumPy array if not already
        if not isinstance(tiff_data, np.ndarray):
            tiff_data = np.array(tiff_data)

        return tiff_data
    except Exception as e:
        print(f"Error reading TIFF image: {e}")
        return None
