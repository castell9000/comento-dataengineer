import logging
import logging.handlers
from slacker import Slacker

class SlackHandler(logging.handlers.HTTPHandler):
    # def __init__(self, token, channel='#general', emoji=True):
    #     super().__init__(host='slack.com', url='/api/chat.postMessage', secure=True)
    #     self.token = token
    #     self.channel = channel
    #     self.emoji = emoji

    def __init__():
        with open('config.json', 'r') as f:
            config = json.load(f)

        slack_token = config['slack']['token']
        slack_channel = congif['slack']['channel']

        token = slack_token
        slack = Slacker(token)
        slack.chat.post_message(slack_chnnel, 'message')

    # def mapLogRecord(self, record):
    #     if self.formatter is None:  # Formatter가 설정되지 않은 경우
    #         text = record.msg
    #     else:
    #         text = self.formatter.format(record)
    #
    #     emoji = (
    #         '' if self.emoji == False else
    #         ':bug:' if record.levelname == 'DEBUG' else
    #         ':pencil2:' if record.levelname == 'INFO' else
    #         ':warning:' if record.levelname == 'WARNING' else
    #         ':no_entry:' if record.levelname == 'ERROR' else
    #         ':rotating_light:' if record.levelname == 'CRITICAL' else
    #         ''
    #     )
    #
    #     return {
    #         'token': self.token,
    #         'channel': self.channel,
    #         'text': f'{emoji} {text}',
    #         'as_user': True,
    #     }