#! /usr/bin/env python3
#  sel_copy.py -- selective_copy script -- walks through folder tree and searches for files with certiain extensions
#  Usage:	./sel_copy.py <folder_path> <sought_extension> -- folder_path is the path to the root of the folder tree
#										-- sought_extension should not begin with a period

"""
README:
Automate The Boring Stuff Python (Ch. 9 -- pg 213) Project
solved by Z Meeks 9/27/17

This script walks through a folder tree and searches for files matching the extension given in the
command line parameters and copies all of them to a new folder rooted at the beginning of where
the folder tree began
"""


import sys, os, shutil

if len(sys.argv) != 3:
	print("incorrect number of command line arguments given\n")
	sys.exit()
folder = os.path.abspath(sys.argv[1])
ext = sys.argv[2]
new_folder = os.path.join( folder, ext + "_files" )
if not os.path.exists(new_folder):
	os.makedirs(new_folder)
sz_ext = len(ext)
for foldername, subfolders, filenames in os.walk(folder):
	if foldername == new_folder:
		continue
	for filename in filenames:
		if filename[-sz_ext:] == ext and filename[-(sz_ext+1)] == '.':
			cur_dir = os.path.abspath(foldername)
			cur_path = os.path.join(cur_dir, filename)
			shutil.copy(cur_path,new_folder)

