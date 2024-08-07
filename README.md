# Git Push Automator

I designed this automation script to streamline the process of tracking and pushing new solution folders for LeetCode problems to GitHub repository. It automatically detects new sub-folders within the local `LeetCode` directory and pushes them to the remote repository, ensuring the online repository is always up-to-date with the latest solutions. You can use it with any of your projects and modify the code to track all the files instead of just the sub-folders according to your requirements.

## Features

- **Automatic Detection**: Scans your local `LeetCode` folder for any new sub-folders that have been added.
- **Git Integration**: Automatically stages, commits, and pushes new folders to the remote GitHub repository.
- **User-Friendly Output**: Provides clear console messages to indicate the status of the automation process.

## How It Works

1. **Initialization**:

   - The script first identifies all current sub-folders in the specified `LeetCode` directory.
   - It then retrieves the list of tracked sub-folders from the Git repository.

2. **Detection of New Sub-Folders**:

   - Compares the current sub-folders with the tracked sub-folders to detect any new additions.
   - Excludes hidden files or directories such as `.git`.

3. **Git Operations**:
   - For each new sub-folder detected, the script stages the folder using `git add`.
   - Commits the changes with a message indicating the new addition.
   - Pushes the changes to the remote repository.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed on your machine.
- **Git**: Git must be installed and configured on your local machine.
- **GitHub Authentication**: Ensure you have authenticated your local Git setup to push changes to GitHub.

## Usage

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/your-repo.git

   ```

2. **Update Folder Path**:

   At line 4, add the path to the folder you want to work with, which is also the local repository.

3. **Navigate to Your Local Repository**:

   ```sh
   cd /path/to/your/repo

   ```

4. **Run the Script**:
   ```sh
   python3 main.py
   ```

5. **Add an alias to run the script conveniently [Optional]**:
   
   To your '.bashrc' or '.zshrc' add the following line:
   ```sh
   alias runmyscript='python /path/to/your/script.py'
   ```
   Run the alias in your terminal:
   ```sh
   runmyscript
   ```

## Future Plans

- ~~Create an alias to run the script from the root directory.~~
- LeetCode integrations to fetch latest solutions from LeetCode and push it to GitHub.
