import time
import textwrap

import toml
import praw


config = toml.load("config.toml")


def get_reddit(account):
    return praw.Reddit(
        username=account["name"],
        password=account["password"],
        client_id=account["client_id"],
        client_secret=account["client_secret"],
        user_agent=f"OCRAP-Simple /{account['name']}",
    )


def fmt_post(title, subreddit, author, submission_type):
    title = (
        f"{textwrap.shorten(title, width=75, placeholder='...')} : "
        f"[/r/{subreddit}]"
        f"[/u/{author}]"
        f"[{submission_type}]"
    )

    comment = f"Original post info:\n r/{subreddit} \n/u/{author}"

    return title, comment


if __name__ == "__main__":
    while True:
        for account in config["accounts"]:
            time.sleep(config["sleep"])
            reddit = get_reddit(account)
            subreddit = reddit.subreddit(config["dest_subreddit"])
            for saved_submission in reddit.redditor(account["name"]).saved():
                if saved_submission.__class__.__name__ == "Submission":
                    title, comment = fmt_post(
                        title=saved_submission.title,
                        subreddit=saved_submission.subreddit.display_name,
                        author=saved_submission.author,
                        submission_type="POST",
                    )
                    link = (
                        f"https://www.reddit.com{saved_submission.permalink}"
                    )
                    archived_submission = subreddit.submit(
                        title=title, url=link
                    )
                    archived_submission.reply(comment)
                    saved_submission.unsave()
                elif saved_submission.__class__.__name__ == "Comment":
                    title, comment = fmt_post(
                        title=saved_submission.link_title,
                        subreddit=saved_submission.subreddit.display_name,
                        author=saved_submission.author,
                        submission_type="COMMENT",
                    )
                    link = saved_submission.link_permalink
                    archived_submission = subreddit.submit(
                        title=title, url=link
                    )
                    archived_submission.reply(comment)
                    saved_submission.unsave()
                else:
                    print(saved_submission.__class__.__name__)
                    print(dir(saved_submission))
