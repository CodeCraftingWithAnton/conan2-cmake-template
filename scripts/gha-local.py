#!/usr/bin/env python3
"""
Run GitHub Actions locally
Install act: https://nektosact.com/installation/index.html
macOS/Linux: brew install act
Other curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
"""

import argparse
import subprocess
import platform
import shlex

local_runner = "-self-hosted"

docker_platform = platform.machine().lower()

matrix = {
  "windows-latest": {
    "image": "",
    "container-architecture": f"windows/{docker_platform}"
  },
  "ubuntu-latest": {
    "image": "catthehacker/ubuntu:act-22.04",
    "container-architecture": f"linux/{docker_platform}"
  },
  "macos-latest": {
    "image": local_runner,
  },
}

parser = argparse.ArgumentParser(description="Run GitHub Actions locally")
parser.add_argument("--host-only", action="store_true", help="Only run the host platform")
parser.add_argument("--include", nargs="+", help="Include the specified platforms", choices=matrix.keys())

args = parser.parse_args()

act_args = ["act"]
if args.host_only:
  act_args += ["-P"]
  if platform.system() == "Darwin":
    act_args += ["macos-latest=-self-hosted"]
  elif platform.system() == "Linux":
    act_args += ["ubuntu-latest=-self-hosted"]
  elif platform.system() == "Windows":
    act_args += ["windows-latest=-self-hosted"]
else:
  platforms = args.include if args.include else matrix.keys()

  for plat in platforms:
    entry = matrix[plat]
    act_args += ["-P", f"{plat}={entry['image']}"]
    if "container-architecture" in entry:
      act_args += ["--container-architecture", entry["container-architecture"]]

print(f"Running: {shlex.join(act_args)}")
subprocess.check_call(act_args)
