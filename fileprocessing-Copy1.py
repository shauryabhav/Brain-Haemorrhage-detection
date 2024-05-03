import splitfolders

'''
    INPUT : Specify path to root directory containing subdirectory (named as labels)
    OUTPUT : Path to output directory
'''
input_folder = "/workspace/data/data_dir/finaldata"
output_folder = "/workspace/data/data_dir/model-data"

splitfolders.ratio(input_folder, output_folder, seed = 42, ratio=(.7,.1,.2))

# import os
# import shutil
# import random

# def split_folders(input_folder, output_folder, ratios=(0.7, 0.1, 0.2), seed=42):
#     random.seed(seed)

#     # Create output folders
#     train_folder = os.path.join(output_folder, 'train')
#     validation_folder = os.path.join(output_folder, 'validation')
#     test_folder = os.path.join(output_folder, 'test')

#     for folder in [train_folder, validation_folder, test_folder]:
#         os.makedirs(folder, exist_ok=True)

#     # List all subdirectories (labels)
#     labels = os.listdir(input_folder)

#     for label in labels:
#         label_path = os.path.join(input_folder, label)
#         images = os.listdir(label_path)
#         random.shuffle(images)

#         # Calculate the number of images for each split
#         num_images = len(images)
#         num_train = int(ratios[0] * num_images)
#         num_validation = int(ratios[1] * num_images)

#         # Copy images to respective folders
#         for image in images[:num_train]:
#             shutil.copy(os.path.join(label_path, image), os.path.join(train_folder, label, image))
#         for image in images[num_train:num_train+num_validation]:
#             shutil.copy(os.path.join(label_path, image), os.path.join(validation_folder, label, image))
#         for image in images[num_train+num_validation:]:
#             shutil.copy(os.path.join(label_path, image), os.path.join(test_folder, label, image))

# # Example usage
# input_folder = "data/data_dir/Patients_CT/NH_0"
# output_folder = "data/data_dir/Patients_CT/final_0"
# split_folders(input_folder, output_folder, ratios=(0.7, 0.1, 0.2), seed=42)
