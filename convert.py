import glob
import os
from wand.image import Image
from tqdm.contrib.concurrent import process_map

# Key config variables
## Must be outside of current directory 
output_dir = '../heif/heic/'

## Select the different image filetypes we want to convert, and also capitalize since MacOS is finnicky about that
filetypes = ['jpg', 'jpeg', 'png', 'heic']
filetypes.extend([x.upper() for x in filetypes])

def heic_convert(filename):
    with Image(filename=filename) as img:
      filename_new = output_dir + filename.rsplit('.',1)[0] + '.heic'
      # filenames.set_description(f"Processing {filename_new}")
      img.save(filename=filename_new)
      return

def print_summary():
  allowed_filetypes = filetypes
  
  filenames = glob.glob('**/*.*', recursive=True)
  
  nonallowed_filetype_count = {}
  allowed_filetype_count    = {}
  for filename in filenames:
    filetype = filename.rsplit('.')[-1]
    if filetype in allowed_filetypes:
      if filetype not in allowed_filetype_count.keys():
        allowed_filetype_count[filetype] = 1
      else:
        allowed_filetype_count[filetype] += 1 
    else:
      if filetype not in nonallowed_filetype_count.keys():
        nonallowed_filetype_count[filetype] = 1
      else:
        nonallowed_filetype_count[filetype] += 1
  print(f"Converting: {allowed_filetype_count}")
  print(f"Not converting: {nonallowed_filetype_count}")

if __name__ == '__main__':
  # Print out types of files that will not be processed
  print_summary()
  
  # Copy directory structure over to output directory
  dirs = glob.glob('**/*/', recursive=True)
  for dir in dirs:
    os.makedirs(output_dir + dir, exist_ok=True)

  # Recursively search the current directory for all files ending with the extension filetypes listed above
  filenames = glob.glob(f"**/*.*[{*filetypes,}]", recursive=True)

  # Multithreading gives us about a 50% speedup
  # other options available: https://stackoverflow.com/questions/41920124/multiprocessing-use-tqdm-to-display-a-progress-bar
  r = process_map(heic_convert, filenames, max_workers=2, chunksize=16)