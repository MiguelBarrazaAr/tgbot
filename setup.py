#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup

setup(
        name='tgbot',
        zip_safe=False,
        version="0.3",
        description="""librería de manipulación y configuración de bot de telenet.
te permite mantener contextos, conservar datos, y tener otras funciones necesarias para construir tu bot.
esta orientada a el desarrollo de aventuras conversacionales para telegram.
""",
        author='Miguel Barraza',
        author_email='miguelbarraza2015@gmail.com',
        install_requires=[
            'setuptools',
            'pyTelegramBotAPI',
            'jsonpickle'
            ],
        packages=[
            'tgbot'
        ],
        url='http://www.miguelbarraza.com.ar',
        include_package_data = True,
)
