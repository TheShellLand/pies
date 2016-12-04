#!/usr/bin/env python
# -*- coding: utf8 -*-


import zipfile

zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
