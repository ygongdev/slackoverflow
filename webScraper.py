import urllib
import requests
from bs4 import BeautifulSoup
import html
import html2text

class StackoverflowWebScraper():
  def __init__(self):
    self.stackoverflow_base_api = "https://api.stackexchange.com/2.2",
    self.time_delay = 5

  def get_top_question(self, question):
    question_request = requests.get(
      url="https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=votes&q=" + question + "&site=stackoverflow"
    )

    question_response = question_request.json()
    top_question = question_response["items"][0]

    return top_question

  def get_top_answer(self, question_id):

    answer_request = requests.get(
      url="https://api.stackexchange.com/2.2/questions/" + str(question_id) + "/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
    )

    answer_response = answer_request.json()
    top_answer = answer_response["items"][0]

    return top_answer

  def run(self):

    top_question_id = top_question["question_id"]
    top_question_url = top_question["link"]
    top_question_title = html.unescape(top_question["title"])

    print(html2text.html2text(top_answer))

