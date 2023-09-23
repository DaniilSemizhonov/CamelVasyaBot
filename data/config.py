BOT_TOKEN = 'telegram token' #CamelVasyaBot

HEROKU_APP_NAME = 'app name'

WEBHOOK_HOST = f"https://{HEROKU_APP_NAME}.herokuapp.com"
WEBHOOK_PATH = '/webhook/' + BOT_TOKEN
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
ADMINS = []#admins telegram id

