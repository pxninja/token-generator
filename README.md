# Token Generator

A [Sublime Text](https://www.sublimetext.com/) package that lets you generate new / random / five character / alpha-numeric strings with a hotkey, from the context menu (right clicking), or from the Command Palette.

Example output: `a1b2c`

## Installation

### Package Control

If you have [Package Control](https://packagecontrol.io/) installed:
1. In Sublime Text, open the Command Palette by typing <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Linux / Windows).
2. Type `install` and select `Package Control: Install Package`
3. A text prompt should appear shortly after Package Control loads a list of
   packages from the internet.
4. Type `token generator` and press <kbd>Enter</kbd>
5. That's it! The token generator is now installed.


### Manual Download

1. [Click here to download](https://github.com/pxninja/token-generator/archive/refs/heads/main.zip) the [ GitHub repository](https://github.com/pxninja/token-generator), and unzip the downloaded file.
2. In Sublime Text, open the Command Palette by typing <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Linux / Windows).
3. Type `browse` and select `Preferences: Browse Packages`
4. A window should appear with the "Packages" directory selected. Move the unzipped file into the "Packages" directory.
5. That's it! The token generator is now installed.

## Usage

Once Installed, you will be able to create new / random / five character / alpha-numeric tokens in 1 of 3 ways:
1. Keyboard Shortcut: <kbd>Command</kbd>+<kbd>Option</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd> (Linux / Windows).
2. Context Menu: right click within Sublime Text and select `New Token`.
3. Command Palette: open the Command Palette, type `new token`, and select `Token Generator: New Token`

By default, the Keyboard Shortcut option is *disabled*. To enable the Keyboard Shortcut, open the Command Palette, type `key binding` and select `Token Generator: Key Binding`.

By default, the Context Menu option is *enabled*. To disable the context menu option, open the Command Palette, type `settings` and select `Token Generator: Settings`.

The Command Palette option is always available.

## Settings

There are 4 settings:

1. String Length, `5` by default
2. Character Set, `abcdef0123456789` by default (aka. hexadecimal / base-16)
3. Force alpha numeric inclusion, `true` by default (aka. ensures string has at least 1 letter and 1 number)
4. Show in context menu, `true` by default (aka. it will be available in the context menu)

There are 940,800 unique tokens with these settings (16<sup>5</sup> - 10<sup>5</sup> - 6<sup>5</sup>). This is more than sufficient for the intended purpose. Don't go generating passwords with these settings.

To change these settings, open the Command Palette, type `token settings` and select `Token Generator: Settings`. Edit the settings as you would any other Sublime Text feature.

## But ... why?

Short randomized tokens are useful in a variety of contexts. The inspiration for this plugin was to help with CSS specificity issues. Notably to…

1. Mitigate name space collisions
2. Improve style management

Appending tokens to the end of an id or class name helps ensure uniqueness without silently breaking previous styles. No more name space collisions!

Creating a new id or class name? Easily append a unique token using the hot key (or right clicking) and `.btn` becomes `.btn-a1b2c`.

Want to find each instance of an existing style? In Sublime Text, type <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> (Linux / Windows) to find where `btn-a1b2c` lives in your project. Good luck finding / editing the correct `btn` style!

Naturally this raises questions around tree shaking. Want keep your style sheet from bloating? When you append unique tokens to id / class names (effectively treating them like GUIDs) you can delete the useless bits without silently breaking stuff.

All of this is to say: this Sublime Text plugin makes random token generation convenient, supporting better CSS management (among other use cases). No more copy / pasting from some other list of random tokens, or Googling for a generator. Now you can get a fresh token without ever leaving your code.

## License
[MIT License](https://github.com/pxninja/token-generator/blob/main/LICENSE)