#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2020: Miguel Barraza
import pickle
import telebot
from telebot import types
from .Command import Command, SplitCommand
from .Game import Game

class Bot():
  def __init__(self, token, handle):
    self.admin = "c4p1" # password of admin
    self.bot = telebot.TeleBot(token)
    self.bot.set_update_listener(self.listener)
    self.handle = handle(self) # game handle
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
      self.loadUser(id)
      error=False
      try:
        cmd=self.searchCommand(text)
      except ValueError:
        error=True
      else:
        cmd.data = dict(id=id, name=name, text=text)
        return cmd.run()
      
      # buscamos si no existe un comando de usuario:
      try:
        method, data = self.handle.user["command"][text]
      except KeyError:
        info = "no te entiendo."
        self.bot.send_message(id, info)
      else:
        self.handle.data = dict(id=id, name=name, text=text)
        getattr(self.handle, method)(*data)
  
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
  
  def game(self, command, data, *args, **kwargs):
    self.handle.data = data
    return getattr(self.handle, command)(*args, **kwargs)
  
  def saveUser(self):
    f = open("user/"+self.handle.user["id"], "wb")
    pickle.dump(self.handle.user, f)
    f.close()
  
  def loadUser(self, id):
    id = str(id)
    try:
      f = open("user/"+id, "rb")
    except FileNotFoundError:
      self.handle.newUser(id)
      self.saveUser()
    else:
      self.handle.user = pickle.load(f)
      f.close()


def init(token, handle=None):
  return Bot(token, handle)