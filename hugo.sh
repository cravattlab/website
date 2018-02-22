#!/usr/bin/env bash

# convenience script to allow one command for building and testing website on both
# linux and OSX

if [ "$(uname)" == "Darwin" ]; then
    bin/hugo_mac -s src ../build "$@"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    bin/hugo_linux -s src -d ../build "$@"
fi
