#!/bin/bash
repo="$HOME/tp-r504/TP14/rech.sh"
(crontab -l 2>/dev/null; echo "30 2 * * * $repo") | crontab -
