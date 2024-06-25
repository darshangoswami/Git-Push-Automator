import os
import subprocess

leetcode_folder = '/Users/dexter/Developer/LeetCode'

current_subfolders = set(next(os.walk(leetcode_folder))[1])

print(current_subfolders)