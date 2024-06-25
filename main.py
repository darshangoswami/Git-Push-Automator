import os
import subprocess

leetcode_folder = '/Users/dexter/Developer/LeetCode'
hidden_files = {'.git'}

def run_command(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=leetcode_folder)
  if result.returncode != 0:
    print(f"Error running command: {command}")
    print(result.stderr)
  else:
    print(result.stdout)
  return result

current_subfolders = set(next(os.walk(leetcode_folder))[1])

print(f"Current: {current_subfolders}")

tracked_subfolders = set(
  item.split('/')[0] for item in run_command('git ls-files').stdout.split('\n') if os.path.isdir(os.path.join(leetcode_folder, item.split('/')[0]))
)

print(f"Tracked: {tracked_subfolders}")

new_subfolders = (current_subfolders - tracked_subfolders) - hidden_files

print(f"New sub-folders: {new_subfolders}")

if new_subfolders:
  print(f"New sub-folder(s) found: {new_subfolders}")

  for subfolder in new_subfolders:
    run_command(f'git add {subfolder}')
    status = run_command('git status --short')
    if status.stdout:
        run_command(f"git commit -m 'added {subfolder}'")
    else:
        print(f"No changes to commit for {subfolder}")

  run_command('git push -u origin main')
else:
  print('No new sub-folder(s) found')