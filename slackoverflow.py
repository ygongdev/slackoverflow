import os
import time
from slackclient import SlackClient
import requests
import subprocess
from webScraper import StackoverflowWebScraper

# instantiate Slack client
slack_client = SlackClient("xoxb-320320014259-SzaOtWuXgvp5ZZa2eNIUhyag")
# starterbot's user ID in Slack: value is assigned after the bot starts up
bot_id = None

# instantiate scraper
web_scraper = StackoverflowWebScraper()

# constants
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM

def reply_thread(thread_ts, channel, text):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        attachments={
            "attachments": [
                {
                    "title": "slackoverflow",
                    "pretext": "Adam",
                    "text": text,
                    "mrkdwn_in": ["text"]
                }
            ]
        },
        thread_ts=thread_ts
    )

def html_mrkdwn(text):
    text = text.replace('<p>', '').replace('</p>', '')
    text = text.replace('<b>', '*').replace('</b>', '*')
    text = text.replace('<code>', '`').replace('</code>', '`')
    text = text.replace('<pre>', '```').replace('</pre>', '```')
    text = text.replace('<em>', '_').replace('</em>', '_')
    text = text.replace('<strong>', '*').replace('</strong>', '*')
    text = text.replace('````', '```')
    return text

def parse_events(slack_events):
    for event in slack_events:
        if event['type'] == 'message':

            message = event['text']
            if bot_id in message:
                message = message.replace("<@{0}>".format(bot_id), "")
                question = web_scraper.get_top_question(message)
                answer = web_scraper.get_top_answer(question["question_id"])
                response = "Question: {0}\nLink: {1}\nAnswer:\n```{2}```".format(
                  question["title"],
                  question["link"],
                  answer["body"][:100]
                )
                reply_thread(event["ts"], event["channel"], response)


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Slack is Overflowing")
        # Read bot's user ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            parse_events(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
