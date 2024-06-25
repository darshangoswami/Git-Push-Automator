import os
import subprocess

leetcode_folder = '/Users/dexter/Developer/LeetCode'

def run_command(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=leetcode_folder)
  if result.returncode != 0:
    print(f"Error running command: {command}")
    print(result.stderr)
  else:
    print(result.stdout)
  return result

current_subfolders = set(next(os.walk(leetcode_folder))[1])

print(current_subfolders)

tracked_subfolders = set(
  item.split('/')[0] for item in run_command('git ls-files').stdout.split('\n') if os.path.isdir(os.path.join(leetcode_folder, item.split('/')[0]))
)

print(tracked_subfolders)