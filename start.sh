#!/bin/bash
pip install -r requirements.txt
playwright install
scrapyrt -i 0.0.0.0 -p $PORT
