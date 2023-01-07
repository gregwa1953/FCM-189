#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     toml1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #189
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

#import tomllib
import tomli
import tomli_w
import pprint

with open("config.toml", "rb") as f:
    data = tomli.load(f)

pprint.pprint(data)
# print(f'{data=}')
print(f"Available Themes: {data['Themes']['available_themes']}")
default_theme = data['Themes']['default_theme']
current_theme = data['Themes']['current_theme']
print(f'Your default Theme is: {default_theme}')
print(f'Your current Theme is: {current_theme}')
program_version = data['Program_Info']['version']
print(f'Program version {program_version}')

# Change the current theme
current_theme = "clam"
data['Themes']["current_theme"] = current_theme
with open("config.toml", "wb") as f:
    tomli_w.dump(data, f)
