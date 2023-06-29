import simplejson as json
import os

def merge_json_files(folder_path):
    merged_data = []

    # List all files in the directory
    files = os.listdir(folder_path)

    # Filter the list to only json files
    json_files = [file for file in files if file.endswith('.json')]

    # Loop through all json files
    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)
        print('Reading file:', file_path)
        
        # Open each json file
        with open(file_path, 'r', encoding='utf-8') as file:
            # Load the data from the file and add it to the merged_data list
            for line in file:
                try:
                    data = json.loads(line)
                    merged_data.append(data)
                except json.JSONDecodeError:
                    print("Skipping invalid JSON in line:", line)

    # Save the merged data to a new file
    with open('merged.json', 'w', encoding='utf-8') as file:
        for item in merged_data:
            file.write(json.dumps(item, ensure_ascii=False))
            file.write('\n')

# Call the function with the path to your folder
merge_json_files('./')
