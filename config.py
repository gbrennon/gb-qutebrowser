# gbrennon qutebrowser configs
# gb badwolf inspired theme

config.load_autoconfig(True)

# Extract colors from badwolf + your customizations
bg_dark = '#1c1c1c'
bg_medium = '#2a2a2a'
bg_light = '#45413b'
fg_primary = '#ffffff'
fg_secondary = '#aaaaaa'
accent_orange = '#d65d0e'
black = '#000000'

# Badwolf base colors (approximated from the scheme)
bg_badwolf = '#1c1b1a'
fg_badwolf = '#f8f6f2'
comment = '#857f78'
selection = '#453f37'
red = '#ff2c4b'
orange = '#ffa724'
yellow = '#ffc800'
green = '#aeee00'
cyan = '#8cffba'
blue = '#0a9dff'
purple = '#ff9eb8'

# Dark mode for web content
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.algorithm = "brightness-rgb"

# Completion (like your popup menus)
c.colors.completion.fg = fg_primary
c.colors.completion.odd.bg = bg_medium
c.colors.completion.even.bg = bg_dark
c.colors.completion.category.fg = accent_orange
c.colors.completion.category.bg = bg_light
c.colors.completion.category.border.top = bg_light
c.colors.completion.category.border.bottom = bg_light
c.colors.completion.item.selected.fg = black  # Like your Visual highlight
c.colors.completion.item.selected.bg = accent_orange
c.colors.completion.item.selected.border.top = accent_orange
c.colors.completion.item.selected.border.bottom = accent_orange
c.colors.completion.match.fg = orange  # Badwolf orange for matches

# Scrollbar
c.colors.completion.scrollbar.fg = fg_secondary
c.colors.completion.scrollbar.bg = bg_dark

# Context menu
c.colors.contextmenu.disabled.bg = bg_light
c.colors.contextmenu.disabled.fg = comment
c.colors.contextmenu.menu.bg = bg_medium
c.colors.contextmenu.menu.fg = fg_primary
c.colors.contextmenu.selected.bg = accent_orange
c.colors.contextmenu.selected.fg = black

# Downloads
c.colors.downloads.bar.bg = bg_dark
c.colors.downloads.start.fg = black
c.colors.downloads.start.bg = blue
c.colors.downloads.stop.fg = black
c.colors.downloads.stop.bg = green
c.colors.downloads.error.fg = red

# Hints
c.colors.hints.fg = black
c.colors.hints.bg = yellow
c.colors.hints.match.fg = accent_orange

# Keyhint
c.colors.keyhint.fg = fg_primary
c.colors.keyhint.suffix.fg = accent_orange
c.colors.keyhint.bg = bg_dark

# Messages
c.colors.messages.error.fg = fg_primary
c.colors.messages.error.bg = red
c.colors.messages.error.border = red
c.colors.messages.warning.fg = black
c.colors.messages.warning.bg = yellow
c.colors.messages.warning.border = yellow
c.colors.messages.info.fg = fg_primary
c.colors.messages.info.bg = bg_light
c.colors.messages.info.border = bg_light

# Prompts
c.colors.prompts.fg = fg_primary
c.colors.prompts.bg = bg_dark
c.colors.prompts.border = accent_orange
c.colors.prompts.selected.fg = black
c.colors.prompts.selected.bg = accent_orange

# Statusbar (matches your StatusLine settings)
c.colors.statusbar.normal.fg = fg_primary
c.colors.statusbar.normal.bg = bg_dark
c.colors.statusbar.insert.fg = bg_dark  # Like your StatusLine
c.colors.statusbar.insert.bg = accent_orange
c.colors.statusbar.passthrough.fg = black
c.colors.statusbar.passthrough.bg = cyan
c.colors.statusbar.private.fg = black
c.colors.statusbar.private.bg = purple
c.colors.statusbar.command.fg = fg_primary
c.colors.statusbar.command.bg = bg_dark
c.colors.statusbar.command.private.fg = fg_primary
c.colors.statusbar.command.private.bg = bg_dark
c.colors.statusbar.caret.fg = black
c.colors.statusbar.caret.bg = purple
c.colors.statusbar.caret.selection.fg = black
c.colors.statusbar.caret.selection.bg = blue
c.colors.statusbar.progress.bg = accent_orange
c.colors.statusbar.url.fg = fg_primary
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.hover.fg = cyan
c.colors.statusbar.url.success.http.fg = fg_primary
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = yellow

# Tabs (matches your TabLine settings)
c.colors.tabs.bar.bg = bg_medium  # TabLineFill
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = green
c.colors.tabs.indicator.error = red
c.colors.tabs.odd.fg = fg_primary  # TabLine
c.colors.tabs.odd.bg = bg_light
c.colors.tabs.even.fg = fg_primary
c.colors.tabs.even.bg = bg_light
c.colors.tabs.pinned.even.bg = bg_light
c.colors.tabs.pinned.even.fg = fg_primary
c.colors.tabs.pinned.odd.bg = bg_light
c.colors.tabs.pinned.odd.fg = fg_primary
c.colors.tabs.pinned.selected.even.bg = accent_orange  # TabLineSel
c.colors.tabs.pinned.selected.even.fg = black
c.colors.tabs.pinned.selected.odd.bg = accent_orange
c.colors.tabs.pinned.selected.odd.fg = black
c.colors.tabs.selected.odd.fg = black  # TabLineSel
c.colors.tabs.selected.odd.bg = accent_orange
c.colors.tabs.selected.even.fg = black
c.colors.tabs.selected.even.bg = accent_orange

# Font
c.fonts.default_family = "monospace"
c.fonts.default_size = "10pt"

# Additional settings
c.url.start_pages = ["about:blank"]
c.tabs.position = "top"
c.tabs.show = "multiple"
c.statusbar.show = "always"

config.bind('<Alt-b>', 'spawn --userscript bitwarden')
