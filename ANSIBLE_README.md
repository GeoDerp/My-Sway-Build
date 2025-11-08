# Sway Desktop Environment - Ansible Setup

This repository contains an Ansible playbook to automate the installation and configuration of a Sway desktop environment with wpgtk theming integration.

## Features

- **Automated installation** of Sway window manager and related components
- **wpgtk integration** for cohesive theming across all applications
- **Pre-configured dotfiles** following best practices
- **Multi-distribution support**: Fedora, Ubuntu/Debian, Arch Linux, openSUSE, and Fedora rpm-ostree variants (e.g., Silverblue, Kinoite)
- **Modular role-based design** for easy customization

## Components Installed

- **Sway**: Tiling Wayland compositor
- **Waybar**: Highly customizable status bar
- **Ulauncher**: Application launcher with wpgtk theme
- **Kitty**: Modern, GPU-accelerated terminal emulator
- **wpgtk**: Wallpaper and theming tool for consistent color schemes
- **Additional utilities**: swaylock, swayidle, grim, slurp, wf-recorder, and more

## Prerequisites

- A supported Linux distribution (Fedora, Fedora rpm-ostree variants, Ubuntu/Debian, Arch Linux, or openSUSE)
- Python 3 installed
- Ansible installed (version 2.9 or higher)
- Sudo privileges for installing system packages

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/GeoDerp/My-Sway-Build.git
cd My-Sway-Build
```

### 2. Install Ansible (if not already installed)

**Fedora:**
```bash
sudo dnf install ansible -y
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ansible -y
```

**Arch Linux:**
```bash
sudo pacman -S ansible
```

**openSUSE:**
```bash
sudo zypper install ansible
```

**Fedora rpm-ostree variants (Silverblue/Kinoite/etc.):**
```bash
sudo rpm-ostree install ansible
```

After installing Ansible, install the required collections:
```bash
ansible-galaxy collection install -r requirements.yml
```

### 3. Run the playbook

Run the complete setup:
```bash
ansible-playbook playbook.yml
```

Or run specific roles using tags:

```bash
# Install only system dependencies
ansible-playbook playbook.yml --tags dependencies

# Install only wpgtk
ansible-playbook playbook.yml --tags wpgtk

# Install Sway window manager
ansible-playbook playbook.yml --tags sway

# Install Waybar
ansible-playbook playbook.yml --tags waybar

# Install Ulauncher
ansible-playbook playbook.yml --tags ulauncher

# Install Kitty terminal
ansible-playbook playbook.yml --tags kitty
```

## Configuration

### wpgtk Setup

After installation, you need to add wallpapers and apply a theme:

1. Add a wallpaper:
   ```bash
   wpg -a /path/to/your/wallpaper.jpg
   ```

2. Apply the theme:
   ```bash
   wpg -s /path/to/your/wallpaper.jpg
   ```

3. The following configs are registered as wpgtk templates:
   - `~/.config/sway/config`
   - `~/.config/waybar/style.css`
   - `~/.config/ulauncher/user-themes/wpgtk-theme/theme.css`

### Starting Sway

To start Sway, simply run:
```bash
sway
```

Or add it to your login shell for auto-start (modify `~/.bash_profile`):
```bash
if [ -z "$WAYLAND_DISPLAY" ] && [ "$XDG_VTNR" -eq 1 ]; then
    exec sway
fi
```

## Key Bindings

See the [Sway config](Backup-.configs/sway/config) for complete keybinding documentation.

### Essential Shortcuts

- `Alt + Return`: Open terminal
- `Alt + d`: Launch application launcher (ulauncher)
- `Alt + Shift + q`: Kill focused window
- `Alt + Shift + r`: Reload Sway configuration
- `Super + l`: Lock screen
- `Alt + Shift + c`: Open Firefox
- `Alt + Shift + w`: Change wallpaper (random)
- `Alt + 1-0`: Switch to workspace 1-10
- `Alt + Shift + 1-0`: Move window to workspace 1-10
- `Print`: Take screenshot
- `Print + Shift`: Take screenshot of selected region

## Project Structure

```
.
├── ansible.cfg              # Ansible configuration
├── inventory.yml            # Inventory file
├── playbook.yml            # Main playbook
├── roles/                  # Ansible roles
│   ├── system_dependencies/
│   ├── wpgtk/
│   ├── sway/
│   ├── waybar/
│   ├── ulauncher/
│   └── kitty/
├── Backup-.configs/        # Dotfiles and configurations
│   ├── sway/
│   ├── waybar/
│   ├── ulauncher/
│   └── kitty/
└── README.md
```

## Customization

### Modifying Configurations

All configuration files are stored in the `Backup-.configs/` directory:

- **Sway**: `Backup-.configs/sway/config`
- **Waybar**: `Backup-.configs/waybar/config` and `style.css`
- **Ulauncher**: `Backup-.configs/ulauncher/user-themes/wpgtk-theme/`
- **Kitty**: `Backup-.configs/kitty/kitty.conf`

After modifying these files, run the playbook again to apply changes:
```bash
ansible-playbook playbook.yml
```

### Adding New Roles

To add a new component:

1. Create a new role directory: `mkdir -p roles/myapp/{tasks,defaults,files}`
2. Add tasks in `roles/myapp/tasks/main.yml`
3. Add the role to `playbook.yml`
4. Run the playbook with the new role

## Troubleshooting

### wpgtk not found

If wpgtk is not in your PATH after installation, add this to your `~/.bashrc`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Sway won't start

Check the logs:
```bash
journalctl -xe | grep sway
```

Common issues:
- Missing graphics drivers
- Incorrect display configuration
- Conflicting desktop environments

### Waybar not displaying

Ensure waybar is installed and the config is valid:
```bash
waybar -c ~/.config/waybar/config -s ~/.config/waybar/style.css
```

### wpgtk theme not applying

If colors aren't updating after adding a wallpaper:

1. Check if wpgtk is available:
   ```bash
   wpg --version
   ```

2. Manually reapply the theme:
   ```bash
   wpg -s /path/to/your/wallpaper.jpg
   ```

3. Verify template files are registered:
   ```bash
   wpg -t
   ```

### Swaylock shows blank/black screen

This usually happens when the wallpaper variables aren't properly expanded. Ensure:
- You've applied a wpgtk theme at least once
- The lock wallpaper exists: `ls ~/.config/wpg/wallpapers/*.lock.png`
- Run the playbook again to regenerate configs: `ansible-playbook playbook.yml`

### Kitty terminal shows "invalid color name" error

This occurs when wpgtk hasn't processed the template yet. Solution:
1. Apply a wpgtk theme: `wpg -s /path/to/wallpaper.jpg`
2. Run the playbook again: `ansible-playbook playbook.yml`

The playbook uses actual hex colors as fallbacks that wpgtk replaces when themes are applied.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Sway](https://swaywm.org/) - Tiling Wayland compositor
- [wpgtk](https://github.com/deviantfero/wpgtk) - Wallpaper and theming tool
- [Waybar](https://github.com/Alexays/Waybar) - Highly customizable Wayland bar
- [Ulauncher](https://ulauncher.io/) - Application launcher

## Author

GeoDerp

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
