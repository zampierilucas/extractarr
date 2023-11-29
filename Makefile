# Makefile for the extractarr project

# Project specific configurations
APP_NAME=extractarr
INSTALL_DIR=/usr/local/bin
DIST_DIR=dist
BUILD_DIR=build
CONFIG_DIR=$(HOME)/.config/extractarr
CONFIG_FILE=$(CONFIG_DIR)/config.yml

# Python command to use
PYTHON=python3

.PHONY: setup build install uninstall clean

# Setup command
setup:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Setup complete."

# Build command
build:
	@echo "Building $(APP_NAME)..."
	pyinstaller main.spec
	@echo "$(APP_NAME) built successfully"

# Clean command
clean:
	@echo "Cleaning up..."
	rm -rf $(DIST_DIR) $(BUILD_DIR)
	@echo "Clean up completed"

# Install command
install:
	@echo "Installing $(APP_NAME)..."
	mkdir -p $(INSTALL_DIR)
	cp $(DIST_DIR)/$(APP_NAME) $(INSTALL_DIR)/$(APP_NAME)
	chmod +x $(INSTALL_DIR)/$(APP_NAME)
	mkdir -p $(CONFIG_DIR)
	if [ ! -f "$(CONFIG_FILE)" ]; then \
		echo "Creating default config.yml..."; \
	        echo "# Configuration settings for extractarr" > $(CONFIG_FILE); \
	        echo "# Add your configurations here" >> $(CONFIG_FILE); \
	fi
	cp init/systemd/$(APP_NAME).service /etc/systemd/system/$(APP_NAME).service
	systemctl enable $(APP_NAME).service
	@echo "$(APP_NAME) installed successfully to $(INSTALL_DIR)"
	@echo "Start it with `systemctl start $(APP_NAME).service`"

# Uninstall command
uninstall:
	@echo "Uninstalling $(APP_NAME)..."
	rm -f $(INSTALL_DIR)/$(APP_NAME)
	rm -f /etc/systemd/system/$(APP_NAME).service
	rm -f $(INSTALL_DIR)/$(APP_NAME)
	@echo "$(APP_NAME) uninstalled successfully from $(INSTALL_DIR)"
