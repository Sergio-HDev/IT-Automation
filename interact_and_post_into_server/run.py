#! /usr/bin/env python3

import os
import requests


def data_processing(feedback_dir):
  '''Returns a list with dictionaries containing the data for feedback.'''

  feedback_files = []
  feedback_list = []

  for filename in os.listdir(feedback_dir):
    file = os.path.join(feedback_dir, filename)
    if os.path.isfile(file) and file.endswith('.txt'):
      feedback_files.append(file)

  for file in feedback_files:
    with open(file, 'r') as f:
      lines = f.readlines()
      feedback_list.append({
                           'title': lines[0].rstrip(),
                           'name': lines[1].rstrip(),
                           'date': lines[2].rstrip(),
                           'feedback': lines[3].rstrip()
                           })

  return feedback_list

print(data_processing('/data/feedback/'))

for p in data_processing('/data/feedback/'):
  response = requests.post("http://35.238.225.247/feedback/", data=p)
  response.raise_for_status()
