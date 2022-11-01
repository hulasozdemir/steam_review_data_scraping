import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import json
import os

import requests
import steamreviews


response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
appList = pd.DataFrame(response.json()['applist']['apps'])
appLists = appList['appid'].values



request_params = dict()
# Reference: https://partner.steamgames.com/doc/store/localization#supported_languages
request_params['language'] = 'english'
steamreviews.download_reviews_for_app_id_batch(appLists, chosen_request_params=request_params);