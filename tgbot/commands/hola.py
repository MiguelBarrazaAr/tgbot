#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2020: Miguel Barraza
from .. import bot

class Command(bot.Command):
  text = "hola"
  def run(self):
    self.send("hola amigo.")

