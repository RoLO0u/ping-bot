from __future__ import annotations
from typing import Dict, List
import json

Texts = Dict[str, Dict[str, str]]

TextsButtons = Dict[str, Dict[str, List[str]]]

with open("texts.json", "r", encoding="utf-8") as raw:
    texts: Texts = json.load(raw)