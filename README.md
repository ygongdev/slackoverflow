# slackoverflow
A Slack bot for your stackoverflow needs.

## Features
  * Pulls the top answer of the most relevant question matching your query.

## Integration
Head over to http://adamhe.me/slack-bots/ and click on the `Add to Slack` button to add slackoverflow into your team!

## Usage
  * Open Slack, either browser or desktop.
  * In any channel, mention the bot along with a question that you want to ask on stackoverflow, e.g `@slackoverflow how does a es6 promise work?` You can also direct message the bot directly if you don't want to clutter a channel.

## Development
1. Create an app on slack.
2. Obtain your api token.
3. Add your api token into your environment as `SLACK_API_TOKEN`. 
4. `git clone` this repository.
5. `pip install -r requirements.txt` to install all the dependencies. Note for `Google-Search-API`, you might have to get it from the github repository if `pip install` doesn't work
6. Add the bot into any Slack teams (most likely one that you made for testing/developing).
7. Run the bot via `python slackoverflow.py` and have fun developing!

## Contributor Guide
[CONTRIBUTING Guide](https://github.com/ygongdev/slackoverflow/blob/master/CONTRIBUTING.md)

## License 
[MIT License](https://github.com/ygongdev/slackoverflow/blob/master/LICENSE.md)
