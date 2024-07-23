#!/usr/bin/env bash
# Run GitHub Actions locally
# Install act: https://nektosact.com/installation/index.html
# macOS/Linux: brew install act
# Other curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

PLATFORM=linux/arm64
# UBUNTU_IMAGE=catthehacker/ubuntu:full-22.04
UBUNTU_IMAGE=catthehacker/ubuntu:act-22.04

# docker pull image=$UBUNTU_IMAGE platform=$PLATFORM
act -P ubuntu-latest=$UBUNTU_IMAGE --container-architecture $PLATFORM
# act -P macos-latest=-self-hosted
