# My-Sway-Build

A production-ready Sway desktop environment setup maintained with Ansible and themed with wpgtk. This project provides a complete, automated installation of a modern tiling window manager with consistent theming across all components.

![example](/img/screenshot.jpg)

## Quick Start

This repository provides an automated Ansible playbook to set up a complete Sway desktop environment with wpgtk theming.

### Installation

```bash
# Clone the repository
git clone https://github.com/GeoDerp/My-Sway-Build.git
cd My-Sway-Build

# Install required Ansible collections
ansible-galaxy collection install -r requirements.yml

# Run the Ansible playbook
make install
# Or: ansible-playbook playbook.yml -e user_home=/var/home/$USER -e target_user=$USER
```

For detailed installation instructions, configuration options, and troubleshooting, see [ANSIBLE_README.md](ANSIBLE_README.md).

### Post-Installation Setup

After running the playbook, you need to set up wpgtk theming:

```bash
# Add a wallpaper to wpgtk
wpg -a /path/to/your/wallpaper.jpg

# Apply the theme (this generates all color schemes)
wpg -s /path/to/your/wallpaper.jpg

# Start Sway
sway
```

**Note**: You must apply a wpgtk theme before starting Sway for the first time, otherwise colors won't be properly configured.

### Key Features

- ✅ **Fully automated setup** with Ansible
- ✅ **wpgtk integration** for consistent theming
- ✅ **Multi-distribution support** (Fedora, Ubuntu/Debian, Arch, openSUSE, rpm-ostree variants)
- ✅ **Modular role-based design** for easy customization
- ✅ **Pre-configured dotfiles** with best practices

### System Requirements

- **Display**: Wayland-compatible graphics driver
- **Memory**: Minimum 2GB RAM (4GB+ recommended)
- **Disk**: ~500MB for all components
- **Distributions**: Fedora, Ubuntu/Debian, Arch Linux, openSUSE, or rpm-ostree variants (Silverblue, Kinoite)
- **Dependencies**: Python 3, Ansible 2.9+, sudo privileges

## Components

- **Sway**: Tiling Wayland compositor
- **Waybar**: Customizable status bar
- **Ulauncher**: Application launcher (Alt+Space)
- **Kitty**: GPU-accelerated terminal with transparency
- **wpgtk**: Wallpaper and theme management
- **swaylock**: Screen locker with blurred background
- **swayidle**: Idle management with auto-lock

## Quick Reference

### Common Commands

```bash
# Change wallpaper/theme
wpg -s /path/to/wallpaper.jpg

# Lock screen
Win+L

# Open terminal
Alt+Enter

# Open launcher
Alt+D

# Switch workspaces
Alt+1, Alt+2, ... Alt+0

# Reload Sway config
Alt+Shift+R

# Exit Sway
Win+Shift+L
```

See [ANSIBLE_README.md](ANSIBLE_README.md#key-bindings) for complete keybinding list.

## Development Status

### Completed Features
- ✅ Ansible playbook with multi-distribution support
- ✅ wpgtk integration with automatic theme application
- ✅ Swaylock configuration with proper variable expansion
- ✅ Kitty terminal with wpgtk theming
- ✅ Waybar customization with wpgtk colors
- ✅ Ulauncher integration

### Planned Enhancements
- [ ] GUI tool for wallpaper management and theme application
- [ ] Optional Fish shell with Tacklebox integration
- [ ] GitHub Actions for automated testing across distributions
- [ ] Additional Waybar modules (Hue lighting integration)
- [ ] Enhanced Ulauncher themes and plugins 

