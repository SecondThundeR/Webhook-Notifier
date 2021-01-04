function sendMessage() {
  const fs = require('fs');
	const { Webhook } = require('discord-webhook-node');
	const hook = new Webhook('');
	const IMAGE_URL = '';
	const WEBHOOK_NAME = ''
	const FILENAME = 'Changelog.md'
	const CONTENT = fs.readFileSync(FILENAME,'utf8');

	hook.setUsername(WEBHOOK_NAME);
	hook.setAvatar(IMAGE_URL);
	hook.send(CONTENT);

	console.log(`[Webhook-Notifier] Message from ${FILENAME} was sent successfully`)
}

sendMessage();
