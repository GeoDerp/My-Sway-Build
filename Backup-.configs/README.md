
## Installation commands 

#### wpgtk
```bash
# Install gnome themes from wpgtk, and apply
# -g (Install gtk template), -G (Install linea nord gtk template), -i   Install icon-set
~/.local/lib/python3.13/site-packages/wpgtk/misc/wpg-install.sh -gGi
gsettings set org.gnome.desktop.wm.preferences theme "linea-nord-color"
gsettings set org.gnome.desktop.interface theme "linea-nord-color"
gsettings set org.gnome.desktop.interface icon-theme "Flattcolor-dark"
```

#### Sway
```bash
wpg -ta  ~/.config/sway/config
```

#### ulauncher 
```bash
wpg -ta ~/.config/ulauncher/user-themes/wpgtk-theme/theme.css
```

#### waybar
```bash
wpg -ta  ~/.config/waybar/style.css

```

#### VScode
See [vscode-wpgtk-theme](https://github.com/GeoDerp/vscode-wpgtk-theme)