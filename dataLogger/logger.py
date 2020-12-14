import logging
import logging.handlers
import json
import os, sys
from datetime import datetime


def logger(name=None):
    ''' 받은 name 객체는 사용자
    logger 객체 가쟈오기, logging 객체 자체를 가져옴
    info, debug, warn, critical 사용가능
    콘솔은 Debug 레벨, 슬랙은 Warn 레벨부터'''
    return make_logger(name);

def success():
#    로거 객체 오버라이드 하면 되지 않을까..?

def fail():

def make_logger(name=None):
    with open('config.json', 'r') as f:
        config = json.load(f)

    slack_token = config['slack']['token']
    slack_channel = config['slack']['channel']

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] (%(levelname)s) %(filename)s : %(message)s")

    date ='{:%Y-%m-%d}'.format(datetime.now())
    filename = 'logs/'+date+'_'+name+'.log'

    console = logging.StreamHandler()
    file_handler = logging.FileHandler(filename, 'w')
    slack_handler = SlackHandler(slack_token, slack_channel)

    console.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    slack_handler.setLevel(logging.WARN)

    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    slack_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)
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