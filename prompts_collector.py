"""
Pseudo 

1. Get the prompts from Reddit
2. Summarize the prompts and Choose an art style
3. Generate the images from Wombo's dream

"""


# Getting the Prompts from Reddit 

subredditName = 'writingprompts'

def getRedditPosts(subredditName):
	wpcsv_columns = ['summary', 'style', 'genre', 'title', 'url', 'id', 'author']
	writing_prompts_dict = []
	wpCSV = loationPath+ "/wprompts500.csv"

	session = Session()
	reddit = redditInfo

	subreddit = reddit.subreddit(subredditName)
	top_subredditlist = subreddit.top(limit=500)

	for submission in top_subredditlist:
		# Adding Columns for user Summarization and Decisions
		array = ['', '','',submission.title, submission.url, submission.id, submission.author]
		writing_propmpts_dict.append(dict(zip(wpcsv_columns, array)))


	print(len(writing_prompts_dict))

	with open(wpCSV, "w") as csv_file:
		writer = scv.DictWriter(csv_file, wpcsv_columns)
		writer.writeheader()
		writer.writerows(writing_prompts_dict)
	csv_file.close()
