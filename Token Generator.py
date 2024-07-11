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

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.settings = sublime.load_settings('Token Generator.sublime-settings')

  def is_visible(self):
    return self.settings.get('show_in_context_menu', default = True)

  def run(self, edit):
    string_length = self.settings.get('string_length', default = 5)
    character_set = self.settings.get('character_set', default = 'abcdef0123456789')
    homogeny_okay = not self.settings.get('force_alpha_numeric_inclusion', default = True)
    
    while True:
      token = ''.join(random.choice(character_set) for _ in range(string_length))

      if homogeny_okay or string_length <= 1:
        break
      elif any(c.isalpha() for c in token) and any(c.isdigit() for c in token):
        break

    for region in self.view.sel():
      if region.empty():
        self.view.insert(edit, region.begin(), token)
      else:
        self.view.replace(edit, region, token)
