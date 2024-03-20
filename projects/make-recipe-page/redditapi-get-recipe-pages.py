# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.


import praw

# Initialize the Reddit instance
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Fetch recipes from the "recipes" subreddit
subreddit = reddit.subreddit('recipes')
for submission in subreddit.search("flair:recipe", sort='relevance', time_filter='all', limit=5):
    print(submission.title)
    print(submission.url)
    print("\n")