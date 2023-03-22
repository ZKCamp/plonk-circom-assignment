import os

import sys
import subprocess

from glob import glob

print(os.getcwd())
files = glob("valid_proof/*.json")

if not len(files):
    sys.exit(1)

print(files)
for file in files:

    process = subprocess.Popen(
        f"snarkjs plonk verify verification_key.json public.json {file}",
          shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    out = ""
    for line in process.stdout.readlines():
        line_str = line.decode("utf-8")
        print(line_str)
        out += line_str

    if "OK!" not in out:
        sys.exit(1)

