import SimpleITK as sitk
import gzip
import shutil
import os
from pathlib import Path

# Base path for the dataset
base_path = Path('dataset/PROMISE12/training_data')

# Pattern to match .mhd files
pattern = "*.mhd"

# Search for all .mhd files in the directory
for mhd_file in base_path.glob(pattern):
    # Corresponding .raw file
    raw_file = mhd_file.with_suffix('.raw')

    # Define the output file paths
    output_file_path_nii = str(mhd_file).replace('.mhd', '.nii')
    output_file_path_nii_gz = output_file_path_nii + '.gz'
    
    # Read the image using SimpleITK
    image = sitk.ReadImage(str(mhd_file))
    
    # Write out the image to a .nii file
    sitk.WriteImage(image, output_file_path_nii)
    
    # Compress the .nii file using gzip
    with open(output_file_path_nii, 'rb') as f_in, gzip.open(output_file_path_nii_gz, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    
    # Remove the temporary .nii file
    os.remove(output_file_path_nii)
    
    # Remove the original .mhd and .raw files
    os.remove(mhd_file)
    os.remove(raw_file)
    
    # Optionally, you can print out the name of the files that have been converted and deleted
    print(f"Converted to .nii.gz and deleted original files: {mhd_file.name} and {raw_file.name}")

# The original .mhd and .raw files should now be deleted from the base_path directory.