#!/usr/bin/env python3
# BSD 3-Clause License
#
# Copyright (c) 2024, Code Crafting With Anton
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
