#!/bin/sh

# The following script maintains two branches to deploy the site:
# First, we branch off to a "deploy" branch where we can savely add the "public" dir
# Next, we create a fresh "master" branch with only the contents of the "public" dir

if output=$(git status --porcelain) && [ -z "$output" ]; then
  # Working directory clean

  # Delete old deploy branch
  git branch -D deploy

  # Create a new deploy branch
  git checkout -b deploy

  # Delete all the old site fragments
  rm -rf ./public

  # Build the project.
  zola build

  # Add untracked public folder
  git add ./public -f

  # Commit changes.
  msg="rebuilding site $(date)"
  if [ -n "$*" ]; then
    msg="$*"
  fi
  git commit -m "$msg"

  # Remove the latest deploy fragment
  git branch -D master

  # Create a new master branch with the commit state of /public
  git subtree split --prefix=public -b master

  # Force push
  git push -f origin master

  # Change back to the branch where we came from
  git checkout -
else 
  # Uncommitted changes
  printf "\033[0;32mNeed to run ./save.sh first\033[0m\n"
fi


