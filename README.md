# heic2jpg
Convert HEIC image files to JPG image files using Python and ImageMagick

## Requirements
- Python
- ImageMagick

## Usage
I created this tool to work with '`.HEIC' image files retrieved from a device running iOS.

The heic2jpg.py script should be copied to a directory containing subdirectories with `.HEIC` image files.

```
python heic2jpg.py
```

This command will start the process of converting any `HEIC` media present in the working directory (as well as any sucyh media in subdirectories) to the `JPG` file format using ImageMagick.
