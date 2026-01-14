FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Install Chromium and chromedriver
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       chromium \
       chromium-driver \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Ensure /usr/bin/chromium exists (some images symlink differently)
RUN if [ -x "/usr/bin/chromium" ]; then echo chromium found; elif [ -x "/usr/bin/chromium-browser" ]; then ln -s /usr/bin/chromium-browser /usr/bin/chromium; fi || true

ENV CHROME_BIN=/usr/bin/chromium
