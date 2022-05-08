# Core service application
# Handle background services
# Get tasks 
# Gather statistics
# Update files
# Perform other related actions
# - Calendar actions
# - Reminder application
# - News

from . import helpers
import os

# service start
# Get Vault folder
# Get daily note location
# Parse pending tasks

# service loop
## Task management
# once a day
# check if daily note created for today
# get tasks for today from previous day
# mark previous day as processed
# parse tasks
# tasks with date string go into .md file with future tasks
# tasks with obsidian file reference go into actions for that file
# tasks with that are completed to go completed tasks
# insert tasks without time into actions
# insert tasks with time in schedule
# tasks that are file references are processed recursively
# # tasks inside references are processed and added to tasks when scheduled
# # tasks that contain file references are added to that file
# 
# throughout the day
# tasks that are completed get a timestamp of completion time
# tasks that are incomplete are copied to a working file file with a task entered time and priority
# tasks that are incomplete are date parsed and put into schedule section if possible

## File organisation

# service stop cleanup