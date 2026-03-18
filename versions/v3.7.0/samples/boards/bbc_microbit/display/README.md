---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/bbc_microbit/display/README.html
original_path: samples/boards/bbc_microbit/display/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BBC micro:bit display

## Overview

A simple example that demonstrates how to use the 5x5 LED matrix display
on the BBC micro:bit board.

## Building

This project outputs various things on the BBC micro:bit display. It can
be built as follows:

```shell
west build -b bbc_microbit samples/boards/bbc_microbit/display
```

### Sample Output

The sample app displays a countdown of the characters 9-0, iterates
through all pixels one-by-one, displays a smiley face, some animations,
and finally the text “Hello Zephyr!” by scrolling.
