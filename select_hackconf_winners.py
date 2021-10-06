# see https://kiwitcms.org/blog/kiwi-tcms-team/2021/09/01/win-6-superfan-tickets-for-hackconf-2021/

import json
import random
import requests

from pprint import pprint

participants = []

for page in range(1,3):
    response = requests.get(f"https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/issues/334558/participants?per_page=100&page={page}")
    response = json.loads(response.text)
    participants.extend(response)

assert len(participants) >= 122

for i in range(1, 7):
    winner = random.choice(participants)
    print(f"***** WINNER #{i}: {winner['name']}")
    pprint(winner)
