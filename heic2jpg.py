import os, subprocess, argparse

def convert_heic_to_jpg(directory, delete_heic):
    converted_files = {}
    for root, directories, files in os.walk(directory, topdown=True):
        for filename in files:
            if filename.lower().endswith(".heic"): 
                print('Converting %s...' % os.path.join(root, filename))
                subprocess.run(["magick", "%s" % os.path.join(root, filename), "%s" % (filename[0:-5] + '.jpg')], cwd=root)
                if not os.path.exists(os.path.join(root, filename[0:-5] + '.jpg')):
                    print('Error: Converted file %s does not exist. Is the ImageMagick binary in PATH?' % os.path.join(root, filename[0:-5] + '.jpg'))
                converted_files[os.path.join(root, filename)] = True
                continue

    if delete_heic:
        for filename, converted in converted_files.items():
            if converted:
                os.remove(filename)

def main():
    parser = argparse.ArgumentParser(description='Convert HEIC image files to JPG using ImageMagick.')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete HEIC files after conversion.')
    args = parser.parse_args()

    directory = os.getcwd()
    convert_heic_to_jpg(directory, args.delete)

if __name__ == "__main__":
    main()
