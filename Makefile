CC=gcc
ARGS=-Wall -g

install:
        mkdir -p $(root)/usr/share/plymouth/themes/buster
        cp -R src $(root)/usr/share/plymouth/themes/buster
