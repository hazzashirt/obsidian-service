# Core service application
# Handle background services
# Get Vault folder
# Get daily note location
# Get tasks 
# Gather statistics
# Update files
# Perform other related actions
# - Calendar actions
# - Reminder application
# - News

from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
