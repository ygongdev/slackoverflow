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
CHARACTER_LIMIT = 200 # character limit for the response.

def reply_thread(thread_ts, channel, text):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        attachments=[
            {
                "title": "slackoverflow", # TODO: change pretext and title lol
                "pretext": "Adam",
                "text": text,
                "mrkdwn_in": ["text"]
            }
        ],
        thread_ts=thread_ts
    )

def post_to_channel(channel, text):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        attachments= [
            {
                "title": "slackoverflow", # TODO: change pretext and title lol
                "pretext": "Adam",
                "text": text,
                "mrkdwn_in": ["text"]
            }
        ]
    )

# OPTIONAL: Need to be able to reply to the parent's thread ts.
# OPTIONAL: Add reactions to indicate progress and completeness. 
def parse_events(slack_events):
    for event in slack_events:
        # TODO: Make sure that we at least take care of the obvious edge cases.
        if event["type"] == "message":
            if "subtype" in event:
                # Ignore bot messages
                if event["subtype"] == "bot_message":
                    return

            if "text" in event:
                message = event["text"]
                # If DMing bot
                if event["channel"][0] == "D":
                    response = generate_answer(message, True)
                    print(response)
                    post_to_channel(event["channel"], response)
                # If mentioning bot
                if bot_id in message:
                    message = message.replace("<@{0}>".format(bot_id), "")
                    response = generate_answer(message, False)
                    print(response)
                    reply_thread(event["ts"], event["channel"], response)

def html_markdown(text):
    text = text.replace('<p>', '').replace('</p>', '')
    text = text.replace('<b>', '*').replace('</b>', '*')
    text = text.replace('<code>', '`').replace('</code>', '`')
    text = text.replace('<pre>', '```').replace('</pre>', '```')
    text = text.replace('<em>', '_').replace('</em>', '_')
    text = text.replace('<strong>', '*').replace('</strong>', '*')
    text = text.replace('````', '```')
    return text

def generate_answer(message, dm=False):
    char_limit = CHARACTER_LIMIT * 3 if dm else CHARACTER_LIMIT
    question = web_scraper.get_top_question(message)
    response = "Couldn't find a matching question on stackoverflow. Try rephrasing your question."
    if question is not None:
        answer = web_scraper.get_top_answer(question["question_id"])
        response = "*Question:* {0}\n*Link*: {1}\n*Answer*:\n```{2}```".format(
            question["title"],
            question["link"],
            html_markdown(answer["body"])
        )
    return response

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
