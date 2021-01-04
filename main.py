from discordwebhook import Discord

FILENAME = 'Changelog.md'
WEBHOOK_URL = ''
WEBHOOK_USERNAME = ''
WEBHOOK_AVATAR_URL = ''

file = open(FILENAME, 'r', encoding='utf-8')
CONTENT = file.read()
file.close()

discord = Discord(url=WEBHOOK_URL)
discord.post(
    content=CONTENT,
    username=WEBHOOK_USERNAME,
    avatar_url=WEBHOOK_AVATAR_URL
)

print(f'Message from {FILENAME} was sent successfully')
