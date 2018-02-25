# slackoverflow
A Slack bot for your stackoverflow needs.

# Table of Contents
1. [Features](#features)
2. [Integration](#integration)
3. [Usage](#usage)
4. [Development](#development)
5. [Contributing](#contributing)
6. [Contributors](#contributors)
7. [License](#license)

## Features <a name="features"></a>
  * Pulls the top answer of the most relevant question matching your query.

## Integration <a name="integration"></a>
Head over to http://adamhe.me/slack-bots/ and click on the `Add to Slack` button to add slackoverflow into your team!

## Usage <a name="usage"></a>
  * Open Slack, either browser or desktop.
  * In any channel, mention the bot along with a question that you want to ask on stackoverflow, e.g `@slackoverflow how does a es6 promise work?` You can also direct message the bot directly if you don't want to clutter a channel.

## Development <a name="development"></a>
1. Create an app on slack.
2. Obtain your api token.
3. Add your api token into your environment as `SLACK_API_TOKEN`. 
4. `git clone` this repository.
5. `pip install -r requirements.txt` to install all the dependencies. Note for `Google-Search-API`, you might have to get it from the github repository if `pip install` doesn't work
6. Add the bot into any Slack teams (most likely one that you made for testing/developing).
7. Run the bot via `python slackoverflow.py` and have fun developing!

## Contributing <a name="contributing"></a>
[Contributing Guide](https://github.com/ygongdev/slackoverflow/blob/master/CONTRIBUTING.md)

## Contributors <a name="contributors"></a>
[Contribuors](https://github.com/ygongdev/slackoverflow/blob/master/CONTRIBUTORS.md)

## License <a name="license"></a>
[MIT License](https://github.com/ygongdev/slackoverflow/blob/master/LICENSE.md)
