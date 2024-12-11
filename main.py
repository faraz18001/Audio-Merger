import os
from pydub import AudioSegment

"""sorting the files based on numbers"""
def get_number(filename):
    # Extract the number from filename by removing the '.ogg' extension
    return int(filename.replace('.ogg', ''))

directory_path = './number_audio'
file_names = os.listdir(directory_path)

# Sort files based on the numeric part of filename
sorted_files = sorted(file_names, key=get_number)

def merge_functionality(sorted_files):
    numbered_files = sorted_files
    constant_file = './room_number_audio.ogg'
    
    # Create output directory if it doesn't exist
    output_dir = './merged_room_numbers'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load the constant "room number" audio
    room_number_audio = AudioSegment.from_ogg(constant_file)
    
    # Process each numbered file
    for number_file in numbered_files:
        # Load the number audio
        number_audio = AudioSegment.from_ogg(os.path.join(directory_path, number_file))
        
        # Concatenate room number audio with the number audio
        merged_audio = room_number_audio + number_audio
        
        # Get the number from filename for output file naming
        number = get_number(number_file)
        
        # Create output filename
        output_filename = f"room_number_{number}.ogg"
        
        # Save the merged audio
        output_path = os.path.join(output_dir, output_filename)
        merged_audio.export(output_path, format="ogg")
    
    return "Audio files merged successfully"

res = merge_functionality(sorted_files)
print(res)
