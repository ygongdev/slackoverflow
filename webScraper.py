import urllib
import requests
from bs4 import BeautifulSoup
import html
from fake_useragent import UserAgent
from google import google

class StackoverflowWebScraper():
  def __init__(self):
    self.stackoverflow_base_api = "https://api.stackexchange.com/2.2"
    self.time_delay = 5
    self.ua = UserAgent() 

  # Uses Top Stackoverflow search results on Google Search.
  def get_top_question(self, question):
    search_results = google.search(question, 1)
    for result in search_results:
      # In case, the first search result isn't on stackoverflow, we search until we find one or reach end of results.
      if "https://stackoverflow.com/questions/" in result.link:
        # Grab the question id from the link
        question_id = result.link.replace("https://stackoverflow.com/questions/", "").split("/")[0]
        return {
          "title": result.name,
          "link": result.link,
          "question_id": question_id,
        }
    # Found nothing
    return None

  def get_top_answer(self, question_id):
    answer_request = requests.get(
      url="{0}/questions/{1}/answers".format(self.stackoverflow_base_api, str(question_id)),
      params={
        "order": "desc",
        "sort": "votes",
        "site": "stackoverflow",
        "filter": "withbody"
      },
      headers={
        "user-agent": self.ua.random # Rotates fake user agents
      }
    )

    answer_response = answer_request.json()
    top_answer = answer_response["items"][0]

    return top_answer

  # Uses stackoverflow API, but search results were highly inaccurate. Commented out for now.
  # def get_top_question(self, question):
  #   question_request = requests.get(
  #     url="{0}/search/advanced".format(self.stackoverflow_base_api),
  #     params={
  #       "order": "desc",
  #       "sort": "votes",
  #       "q": question,
  #       "site": "stackoverflow"
  #     }
  #   )

  #   question_response = question_request.json()
  #   top_question = question_response["items"][0]

  #   return top_question