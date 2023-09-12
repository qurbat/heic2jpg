import os, subprocess

def convert_heic_to_jpg(directory):
    converted_files = {}
    for root, directories, files in os.walk(directory, topdown=True):
        for filename in files:
            if filename.lower().endswith(".heic"): 
                print('Converting %s...' % os.path.join(root, filename))
                subprocess.run(["magick.exe", "%s" % os.path.join(root, filename), "%s" % (filename[0:-5] + '.jpg')], cwd=root)
                converted_files[os.path.join(root, filename)] = True
                continue

    for filename, converted in converted_files.items():
        if converted:
            if os.path.exists(os.path.join(root, filename[0:-5] + '.jpg')):
                os.remove(filename)
            else:
                print('[!] Error: Converted image %s was not written to disk. Check to see if ImageMagick has been installed properly and is currently in PATH.' % os.path.join(root, filename[0:-5] + '.jpg'))

def main():
    directory = os.getcwd()
    convert_heic_to_jpg(directory)

if __name__ == "__main__":
    main()
