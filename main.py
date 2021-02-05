from discordwebhook import Discord

FILENAME = 'Changelog.md'
WEBHOOK_URL = ''
WEBHOOK_USERNAME = ''
WEBHOOK_AVATAR_URL = ''

with open(FILENAME, 'r', encoding='utf-8') as file:
    CONTENT = file.read()
file.close()

if len(CONTENT) - 1 > 2000:
    print('Sorry, you hit the discord limit of 2000 characters. \n'
          'Remove some of the content so you can send the message. \n'
          f'The current number of characters is {len(CONTENT) - 1}')
else:
    discord = Discord(url=WEBHOOK_URL)
    discord.post(
        content=CONTENT,
        username=WEBHOOK_USERNAME,
        avatar_url=WEBHOOK_AVATAR_URL
    )
    print(f'Message from {FILENAME} was sent successfully')
