import os
import shutil


def main(dataset_folder):
    # Create new folders if they don't exist
    images_tr_folder = os.path.join(dataset_folder, 'imagesTr')
    labels_tr_folder = os.path.join(dataset_folder, 'labelsTr')
    
    os.makedirs(images_tr_folder, exist_ok=True)
    os.makedirs(labels_tr_folder, exist_ok=True)
    
    # Iterate through each case folder in the dataset
    for case_folder in os.listdir(dataset_folder):
        if not case_folder.startswith('case_'):
            continue
        print(case_folder)
        case_folder_path = os.path.join(dataset_folder, case_folder)
    
        # Check if it is a directory
        if os.path.isdir(case_folder_path):
            # Extract the numeric part from the case folder name
            # numeric_part = ''.join(filter(str.isdigit, case_folder))
            numeric_part = case_folder[6:]
    
            # Construct the new filenames
            imaging_filename = f'kidney_{numeric_part}.nii.gz'
            segmentation_filename = f'kidney_{numeric_part}.nii.gz'
    
            # Source paths
            imaging_source_path = os.path.join(case_folder_path, 'imaging.nii.gz')
            segmentation_source_path = os.path.join(case_folder_path, 'segmentation.nii.gz')
    
            # Destination paths
            imaging_dest_path = os.path.join(images_tr_folder, imaging_filename)
            segmentation_dest_path = os.path.join(labels_tr_folder, segmentation_filename)
    
            # Rename and move the files
            shutil.copy(imaging_source_path, imaging_dest_path)
            shutil.copy(segmentation_source_path, segmentation_dest_path)
    
    print("Conversion completed successfully.")
