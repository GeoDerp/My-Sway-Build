.PHONY: help install check lint clean

help:
	@echo "Sway Desktop Environment - Ansible Setup"
	@echo ""
	@echo "Available targets:"
	@echo "  install         - Run the full Ansible playbook"
	@echo "  check           - Check playbook syntax"
	@echo "  lint            - Lint Ansible files"
	@echo "  dependencies    - Install only system dependencies"
	@echo "  wpgtk           - Install only wpgtk"
	@echo "  sway            - Install only Sway"
	@echo "  waybar          - Install only Waybar"
	@echo "  ulauncher       - Install only Ulauncher"
	@echo "  kitty           - Install only Kitty"
	@echo "  clean           - Clean Ansible cache and temp files"

install:
	ansible-playbook playbook.yml --ask-become-pass

check:
	ansible-playbook playbook.yml --syntax-check

lint:
	@command -v ansible-lint >/dev/null 2>&1 && ansible-lint playbook.yml || echo "ansible-lint not installed, skipping"

dependencies:
	ansible-playbook playbook.yml --tags dependencies --ask-become-pass

wpgtk:
	ansible-playbook playbook.yml --tags wpgtk --ask-become-pass

sway:
	ansible-playbook playbook.yml --tags sway --ask-become-pass

waybar:
	ansible-playbook playbook.yml --tags waybar --ask-become-pass

ulauncher:
	ansible-playbook playbook.yml --tags ulauncher --ask-become-pass

kitty:
	ansible-playbook playbook.yml --tags kitty --ask-become-pass

clean:
	rm -rf .ansible/
	find . -name "*.retry" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
