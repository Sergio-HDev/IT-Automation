#!/usr/bin/env python3

import os
from PIL import Image
import coloring


directory = 'images'
new_directory = 'new_images'

for filename in os.listdir(directory):
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(new_directory, filename)
    if os.path.isfile(old_file) and not filename.startswith('.'):
        #print(old_file)
        #print(new_file)
        print('Opening "{}"'.format(old_file))
        f = Image.open(old_file).convert('RGB')
        print('Resizing, rotating and converting "{}"'.format(old_file))
        f.resize((128, 128)).rotate(270).save(new_file, format='jpeg')
        print(coloring.green('Done with "{}"\n'.format(old_file)))
