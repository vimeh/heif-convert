# %%
import glob
import os
from wand.image import Image
from tqdm.auto import tqdm

# Key config variables
## Outside of current directory 
output_dir = '../heif/heic/'

# Select the different image filetypes we want to convert, and also capitalize since MacOS is finnicky about that
filetypes = ['jpg', 'jpeg', 'png', 'heic']
filetypes.extend([x.upper() for x in filetypes])
# Copy directory structure over to output directory
dirs = glob.glob('**/*/', recursive=True)
for dir in dirs:
  os.makedirs(output_dir + dir, exist_ok=True)

# Recursively search the current directory for all files ending with the extension filetypes listed above
filenames = tqdm(glob.glob(f"**/*.*[{*filetypes,}]", recursive=True))
# %%
# Convert and save new images
for filename in filenames:
  with Image(filename=filename) as img:
    filename_new = '../heif/heic/' + filename.rsplit('.',1)[0] + '.heic'
    filenames.set_description(f"Processing {filename_new}")
    img.save(filename=filename_new)
# %%
filenames = tqdm(range(10))
for i in filenames:
  filenames.set_description("Processing %s" % i)
# %%
