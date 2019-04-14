from dotenv import load_dotenv
import os 
import requests
import argparse
from urllib.parse import urlparse


def make_shortlink(long_url, token):
  url = 'https://api-ssl.bitly.com/v4/shorten'
  headers = {
    "Authorization" : token
  }
  payload = {
    "long_url" : long_url
  }
  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()
  return response.json()['link']

def check_link(url, token):
  url = 'https://api-ssl.bitly.com/v4/bitlinks/{}{}#{}'.format(urlparse(url).netloc, urlparse(url).path, urlparse(url).fragment)
  headers = {
    "Authorization" : token
  }
  response = requests.get(url, headers=headers)
  response.raise_for_status()
  return response.json()

def count_clicks(bitlink, token):
  url = 'https://api-ssl.bitly.com/v4/bitlinks/{}{}/clicks'.format(urlparse(bitlink).netloc, urlparse(bitlink).path)
  headers = {
    "Authorization" : token
  }
  response = requests.get(url, headers=headers)
  response.raise_for_status()
  return response.json()["link_clicks"]

def main():
  load_dotenv()
  token = os.getenv("TOKEN")
  parser = argparse.ArgumentParser()
  parser.add_argument('link')
  user_link = parser.parse_args().link
  try:
    check_link(user_link, token) 
    print(count_clicks(user_link, token)) 
  except requests.exceptions.HTTPError: 
    try:
      data = make_shortlink(user_link, token) 
      print(data) 
    except requests.exceptions.HTTPError as error: 
      exit("Can't get data from server:\n{0}".format(error))

if __name__ == '__main__':
  main()

