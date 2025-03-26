from github_com.kennethreitz import requests

assert requests.get('https://github.com/nvbn/import_from_github_com').status_code == 200