import os
import pandas as pd

def rename_images_with_mapping(folder_path, csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Iterate through patient folders
    for patient_folder in os.listdir(folder_path):
        patient_folder_path = os.path.join(folder_path, patient_folder)

        # Check if it's a directory
        if os.path.isdir(patient_folder_path):
            print(f"Processing patient folder: {patient_folder}")

            # Iterate through brain folders
            brain_folder_path = os.path.join(patient_folder_path, 'brain')
            for image_file in os.listdir(brain_folder_path):
                image_file_path = os.path.join(brain_folder_path, image_file)

                # Check if it's a file
                if os.path.isfile(image_file_path):
                    print(f"Processing image file: {image_file}")

                    # Extract patient and slice numbers from the image file name
                    try:
                        slice_number = int(os.path.splitext(image_file)[0])
                        print(f"Extracted slice number: {slice_number}")
                    except ValueError:
                        print(f"Error extracting slice number from image file: {image_file}")
                        continue  # Skip to the next iteration if there's an error

                    # Find the corresponding row in the CSV file
                    patient_row = df[(df['PatientNumber'] == int(patient_folder)) & (df['SliceNumber'] == slice_number)]

                    # Check if a matching row is found
                    if not patient_row.empty:
                        # Get the value in 'No_Hemorrhage' column
                        no_hemorrhage_value = patient_row['No_Hemorrhage'].values[0]

                        # Create the new filename based on the convention
                        new_filename = f"{patient_folder}_{slice_number}_{no_hemorrhage_value}.jpg"

                        # Construct the new file path
                        new_file_path = os.path.join(brain_folder_path, new_filename)

                        # Print statements for debugging
                        print(f"Original file path: {image_file_path}")
                        print(f"New file path: {new_file_path}")

                        # Rename the file
                        os.rename(image_file_path, new_file_path)
                        print(f"Renamed: {image_file} -> {new_filename}")
                    else:
                        print(f"No matching row found in the CSV file for patient {patient_folder}, slice {slice_number}")

# Replace 'your_folder_path' and 'your_csv_file_path' with the actual paths to your data
folder_path = r'/workspace/data/data_dir/Patients_CT'
csv_file_path = r'/workspace/data/data_dir/hemorrhage_diagnosis.csv'

# Check if directories exist
if not os.path.exists(folder_path):
    print(f"Error: Folder path does not exist: {folder_path}")
    exit()

if not os.path.exists(csv_file_path):
    print(f"Error: CSV file path does not exist: {csv_file_path}")
    exit()

# Call the function to rename images with the category mapping
rename_images_with_mapping(folder_path, csv_file_path)
