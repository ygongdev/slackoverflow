# slackoverflow
A Slack bot for stacked overflow.


## Integration
Head over to http://adamhe.me/slack-bots/ and click on the `Add to Slack` button to add slackoverflow into your team!

## Development
1. Create an app on slack.
2. Obtain your api token.
3. Add your api token into your environment as "SLACK_API_TOKEN"
4. `git clone` this repository.
5. `pip install -r requirements.txt` to install all the dependencies. Note for `Google-Search-API`, you might have to get it from the github repository if `pip install` doesn't work
6. Add the bot into any Slack teams (most likely one that you made for testing/developing).
7. Run the bot via `python slackoverflow.py` and have fun developing!
