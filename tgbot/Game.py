#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2020: Miguel Barraza

class Game():
  def __init__(self, bot):
    self.bot = bot
    self.data = {}
    self.user = {}
    self.user["command"] = {}
  
  def send(self, text):
    self.bot.send(self.data["id"], text)
  
  def setCommand(self, key, value, *args):
    self.user["command"][key] = (value, args)