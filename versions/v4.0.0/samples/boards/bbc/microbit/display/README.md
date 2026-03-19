---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/bbc/microbit/display/README.html
original_path: samples/boards/bbc/microbit/display/README.html
---

# LED matrix display

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/bbc/microbit/display/README.rst/..)

## Overview

A simple example that demonstrates how to use the 5x5 LED matrix display
on the BBC micro:bit board.

## Building

This project outputs various things on the BBC micro:bit display. It can
be built as follows:

```shell
west build -b bbc_microbit samples/boards/bbc/microbit/display
```

### Sample Output

The sample app displays a countdown of the characters 9-0, iterates
through all pixels one-by-one, displays a smiley face, some animations,
and finally the text “Hello Zephyr!” by scrolling.
