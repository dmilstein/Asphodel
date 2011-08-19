#!/bin/bash

python example.py
dot universe.dot -Tpng -o universe.png
dot universe-fog.dot -Tpng -o universe-fog.png
dot universe.dot -Tcmapx -o universe.cmapx
