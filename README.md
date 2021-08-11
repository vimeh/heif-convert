
# HEIF Conversion Utility

## Context
I want to export all data from [Google Photos Takeout](https://takeout.google.com) into my iCloud library, which as of iOS 11 now uses [HEIF as standard](https://support.apple.com/en-us/HT207022). iCloud can accept the existing photo formats, but I think it'd be nice to see how much of a size reduction I can get by reencoding all my media into the new standard.

##  Installation

### System Requirements
- imagemagick
  - Might require a reinstall if [libheif](https://github.com/strukturag/libheif) is not installed first

### python3
- Wand, for access to the imagemagick API
  - Might require MAGICK_HOME directory to be set: eg, 
> ```export MAGICK_HOME=/opt/homebrew/Cellar/imagemagick/7.1.0-4_2```
- tqdm, for pretty progress bars