import os
import time
from slackclient import SlackClient
import requests
import subprocess

# instantiate Slack client
slack_client = SlackClient("xoxb-320320014259-SzaOtWuXgvp5ZZa2eNIUhyag")
# starterbot's user ID in Slack: value is assigned after the bot starts up
bot_id = None

# constants
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM

def reply_thread(thread_ts, channel, text):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        thread_ts=thread_ts
    )

def parse_events(slack_events):
    for event in slack_events:
        if event['type'] == 'message':
            message = event['text']
            if bot_id in message:
                message = ' '.join(message.split(' ')[1:])
                print(message) # Do something with the message


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
