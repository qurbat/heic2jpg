# heic2jpg
Convert HEIC image files to JPG using Python and ImageMagick

## Requirements
- Python
- ImageMagick

## Usage
I created this tool to work with `.HEIC` image files retrieved from the backup of devices running iOS.

The `heic2jpg.py` script can be copied to a directory containing `.HEIC` image files. The tool will look for images in subdirectories within the current working directory.

```
python heic2jpg.py
```

This command will start the process of converting any `HEIC` media present in the working directory (as well as any sucyh media in subdirectories) to the `JPG` file format using ImageMagick.
