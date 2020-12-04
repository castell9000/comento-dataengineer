import logging
import logging.handlers
import json

def logger():
    return make_logger();


def make_logger(name=None):
    with open('config.json', 'r') as f:
        config = json.load(f)

    slack_token = config['slack']['token']
    slack_channel = config['slack']['channel']

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] (%(levelname)s) %(filename)s : %(message)s")

    console = logging.StreamHandler()
    slack_handler = SlackHandler(slack_token, slack_channel)

    console.setLevel(logging.INFO)
    slack_handler.setLevel(logging.DEBUG)

    console.setFormatter(formatter)
    slack_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(slack_handler)

    return logger

class SlackHandler(logging.handlers.HTTPHandler):
    def __init__(self, token, channel, emoji=False):
        super().__init__(host='slack.com', url='/api/chat.postMessage', secure=True)
        self.token = token
        self.channel = channel
        self.emoji = emoji

    def mapLogRecord(self, record):
        if self.formatter is None:  # Formatter가 설정되지 않은 경우
            text = record.msg
        else:
            text = self.formatter.format(record)

        return {
            'token': self.token,
            'channel': self.channel,
            'text': f'{text}',
            'as_user': True,
        }