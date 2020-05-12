# OCRAP - Simple

OCRAP - Simple helps archive your saved Reddit posts for future consumption.

## What's the point?

OCRAP - which is short for Overly Complicated Reddit Archival Process - is a
tool to better manage the submissions that you save. Reddit will only save your
latest 1,000 posts into your saved area and even then, you can't search it. If
you have an old, old, old, Reddit account or two like I do, it's easy for some
of those posts you saved and want to find again to end up lost forever.

OCRAP - Simple attempts to help by clearing out your saved queue by moving them
to a private subreddit where you can also search through them.

There is a more complicated and fully fleshed out version that doesn't have the
simple suffix on the way. But this was meant to scratch my own personal itch
a little bit faster. It was written extremely quickly and I'm sure it reflects
that.

## Configuration

**_NOTE_**: The subreddit you wish to archive to, must already exist. It is
strongly recommended that you create a subreddit exclusively for OCRAP - Simple
to archive post to and make it private. If you make it private and have
multiple accounts configured, you will need to make sure each one has access
to the private subreddit.

- At the very top of the file is a key named `dest_subreddit`. This needs to
  be the name of the subreddit that OCRAP - Simple will copy the posts to.
  Example: `dest_subreddit = "OCRAPTesting"`

**_WARNING_**: DO NOT COMMIT YOUR CONFIG.TOML FILE TO SOURCE CONTROL OR LET IT
LEAVE THE HOST WHERE `ocrap-simple.py` IS RUNNING. IT HAS YOUR REDDIT USERNAME
AND PASSWORD IN IT. THIS IS YOUR ONLY WARNING.

For each Reddit account whose saved posts you would like archived:

- Copy the `config.toml.example` file to `config.toml`.
- Replace the name in the `[[ accounts ]]` block with the Reddit username you
  are going to be archiving the saved posts of.

- Go to https://www.reddit.com/prefs/apps and click the button that says
  "are you a developer? create an app..."
- For the name field, enter "OCRAP - Simple".
- Select the "script" option.
- And even though we won't be using it, for the "redirect url" field, enter
  something like: http://localhost:8080.
- Click the "create app" button.

- Copy the string that appears beneath the block that says
  'personal use script' and paste it into the `config.toml` file as the
  client_id.
- Copy the string to the right of the 'secret' field and paste it into the
  `config.toml` file as the client_secret.

- Finally, enter the password for the account into the `config.toml` file.

To add additional accounts, simply add another block that begins with
`[[ accounts ]]` to the `config.toml` file and repeat the process.

## Usage

### Docker

I would say this is the prefered way of running this as you can set it and
forget it in the background.

- Simply build the container: `docker build -t ocrap-simple`
- And then run it: `docker run ocrap-simple`

### Alternatively

OCRAP - Simple hasn't been tested anywhere other than on Ubuntu 18.04 w/
python 3.8.2. Once you have that setup - and preferably in a virtualenvironment

- it's as asimple as:

- `pip install requirements.txt`
- `python ocrap-simple.py`

## Contributing

If you feel compelled to contribute to this little toy, please create a fork,
make your changes and then make a pull request. However, if you create an issue
with a feature request without putting in the work to add it yourself, please
know that it is likely to be dismissed. It's nothing personal, I just only
want to invest the energy that I have in the features that I want. If that
doesn't work for you, I would love to see this project forked and worked on
by someone who is excited about including a larger community on it's
development.

## License

[MIT](https://choosealicense.com/licenses/mit/)
