#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke — one line about trading life."""
import os

LINE = "I bought the dip, then the dip bought a shovel, and now we're both down here together waiting for the bull market to send a rope."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
