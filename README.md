# Extractarr

## Introduction

`extractarr` is a Python-based utility designed to monitor specified directories for newly downloaded archive files and automatically extract them. It supports a variety of archive formats like `.rar`, `.zip`, `.tar`, `.7z`, and others. This tool is especially useful for automating the extraction process in scenarios like downloading TV shows, movies, music, or any other data that comes in compressed formats.

## Features

- **Directory Monitoring**: Watches specified directories for new archive files.
- **Supports Multiple Formats**: Works with `.rar`, `.zip`, `.tar`, `.7z`, and more.
- **Automatic Extraction**: Automatically extracts new archives into designated folders.
- **System Integration**: Runs as a systemd service for continuous operation.

## Installation
### Prerequisites

- Python 3.6 or higher.
- System dependencies: `p7zip` (for Linux users).
- [Optional] Virtual environment (recommended).

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/zampierilucas/extractarr.git
   cd extractarr
   ```

2. **Create and Activate a Virtual Environment (Optional):**
    ```bash
    python -m venv venv
    source venv/bin/activat
    ```

3. **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Build the Application:**
    ```bash
    make build
    ```

5. **Install the Application:**
    ```bash
    sudo make install
    ```

## Usage
After installation, extractarr will start monitoring the configured directories automatically.
To check the status of the service:

```bash
systemctl status extractarr.service
```

To restart the service:

```bash
sudo systemctl restart extractarr.service
```

## Configuration

Edit the `.config/extractarr/config.yml` file to specify directories to monitor and other settings.
Uninstallation

## To uninstall:
```bash
sudo make uninstall
```

## Contributing

Contributions to extractarr are welcome! If you have a feature request, bug report, or a pull request, please open an issue or submit a PR on the repository.
