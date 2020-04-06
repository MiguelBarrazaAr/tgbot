#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2020: Miguel Barraza
import telebot
from telebot import types
from .Command import Command, SplitCommand

class Bot():
  def __init__(self, token):
    self.admin = "c4p1" # password of admin
    self.bot = telebot.TeleBot(token)
    self.bot.set_update_listener(self.listener)
    self.commands = []
    self.active = True
  
  def listener(self, messages):
    for m in messages:
      id = m.chat.id
      if id > 0:
        name = m.chat.first_name
        group = False
      else:
        name = m.from_user.first_name
        group = True
      text = m.text
      try:
        cmd=self.searchCommand(text)
      except ValueError:
        info = "no te entiendo."
        self.bot.send_message(id, info)
      else:
        cmd.data = dict(id=id, name=name, text=text)
        cmd.run()
  
  def         searchCommand(self, text):
    for obj in self.commands:
      if obj.validate(text):
        return obj
    raise ValueError()
  
  def add(self, comandClass):
    self.commands.append(comandClass(self))
  
  def send(self, *args, **kwargs):
    return self.bot.send_message(*args, **kwargs)
  
  def stop(self):
    self.active = False
  
  def run(self):
    print("initialize bot...")
    self.bot.polling()
    while self.active:
      pass
    print("terminated bot.")

def init(token):
  return Bot(token)