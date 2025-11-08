# My-Sway-Build
My second Sway build, maintained using Ansible with wpgtk for theming

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
# Or: sudo ansible-playbook  playbook.yml  -e user_home=/var/home/$USER -e target_user=$USER
```

For detailed installation instructions, configuration options, and troubleshooting, see [ANSIBLE_README.md](ANSIBLE_README.md).

### Key Features

- ✅ **Fully automated setup** with Ansible
- ✅ **wpgtk integration** for consistent theming
- ✅ **Multi-distribution support** (Fedora, Ubuntu/Debian, Arch, openSUSE, rpm-ostree variants)
- ✅ **Modular role-based design** for easy customization
- ✅ **Pre-configured dotfiles** with best practices

## Components

- **Sway**: Tiling Wayland compositor
- **Waybar**: Customizable status bar
- **Ulauncher**: Application launcher
- **Kitty**: GPU-accelerated terminal with transparency
- **wpgtk**: Wallpaper and theme management

## Work In Progress

### Things to do
- [x] Build Ansible playbook
- [x] Figure out swaylock issue (not accepting arguments in sway config)
- [ ] Make GNOME GUI to interact with playbook and for easy maintenance of the sway build (place to insert new wallpaper)
- [ ] Fix directory issue with wpgtk and the blurred wallpaper image being considered as a wallpaper option
- [ ] Rice terminal (possibly switch terminal with one with opacity)
	- [ ] Implement fish? tackle/Tacklebox? with option to install
- [ ] Customize ulauncher some more
	- [x] On sway refresh, ulauncher refreshes as well
- [ ] Implement GitHub Actions to test playbook against Linux distributions
- [ ] Continue hue module development for Waybar 

