"""

Token Generator
v1.0.0
https://github.com/pxninja/token-generator

Copyright (c) 2024, Samuel Davidson
Released under the MIT License
https://github.com/pxninja/token-generator/blob/LICENSE.md

"""

import sublime
import sublime_plugin
import random

class NewTokenCommand(sublime_plugin.TextCommand):

  def run(self, edit): 
    settings = sublime.load_settings('token-generator.sublime-settings')
    string_length = settings.get('string_length', default=5)
    character_set = settings.get('character_set', default='abcdef0123456789')
    canBeAnything = not settings.get('force_alpha_numeric_inclusion', default=True)
    
    while True:
      token = ''.join(random.choice(character_set) for _ in range(string_length))

      if canBeAnything or string_length <= 1:
        break
      elif any(c.isalpha() for c in token) and any(c.isdigit() for c in token):
        break

    for region in self.view.sel():
      if region.empty():
        self.view.insert(edit, region.begin(), token)
      else:
        self.view.replace(edit, region, token)