import os
import shutil

def organize_files(folder_path, output_folder_path):
    # Create folders for NH_0 and NH_1
    nh_0_folder = os.path.join(output_folder_path, 'NH_0')
    nh_1_folder = os.path.join(output_folder_path, 'NH_1')

    # Create folders if they don't exist
    os.makedirs(nh_0_folder, exist_ok=True)
    os.makedirs(nh_1_folder, exist_ok=True)

    # Iterate through patient folders
    for patient_folder in os.listdir(folder_path):
        if patient_folder.startswith('.'):
            continue  # Skip hidden folders

        patient_folder_path = os.path.join(folder_path, patient_folder)

        # Check if it's a directory
        if os.path.isdir(patient_folder_path):
            print(f"Processing patient folder: {patient_folder}")

            # Iterate through brain folders
            brain_folder_path = os.path.join(patient_folder_path, 'brain')
            
            # Check if the 'Brain' folder exists
            if not os.path.exists(brain_folder_path):
                print(f"Brain folder not found for patient {patient_folder}")
                continue

            for image_file in os.listdir(brain_folder_path):
                image_file_path = os.path.join(brain_folder_path, image_file)

                # Check if it's a file
                if os.path.isfile(image_file_path):
                    print(f"Processing image file: {image_file}")

                    # Move the file to the appropriate folder based on the filename
                    if image_file.endswith("_0.jpg"):
                        destination_folder = nh_0_folder
                    elif image_file.endswith("_1.jpg"):
                        destination_folder = nh_1_folder
                    else:
                        print(f"Invalid filename format for {image_file}")
                        continue

                    destination_file_path = os.path.join(destination_folder, image_file)

                    # Print statements for debugging
                    print(f"Original file path: {image_file_path}")
                    print(f"New file path: {destination_file_path}")

                    # Move the file
                    shutil.move(image_file_path, destination_file_path)
                    print(f"Moved: {image_file} -> {destination_file_path}")

# Replace 'your_folder_path' and 'your_output_folder_path' with the actual paths to your data
folder_path = r'data/data_dir/Patients_CT'
output_folder_path = r'data/data_dir/Patients_CT'  # This should be the same as your main folder

# Check if directories exist
if not os.path.exists(folder_path):
    print(f"Error: Folder path does not exist: {folder_path}")
    exit()

# Call the function to organize files into NH_0 and NH_1 folders
organize_files(folder_path, output_folder_path)
