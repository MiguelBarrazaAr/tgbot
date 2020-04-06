#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2020: Miguel Barraza

class Command():
  text = "test"
  def __init__(self, bot):
    self.bot = bot
    self.data = {}
  
  def validate(self, text):
    return text in self.text
  
  def run(self):
    pass
  
  def send(self, text):
    self.bot.send(self.data["id"], text)


class SplitCommand(Command):
  def validate(self, text):
    data = text.split(" ")
    self.option = data[1:]
    return data[0] in self.text
