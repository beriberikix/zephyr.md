---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/bbc_microbit/sound/README.html
original_path: samples/boards/bbc_microbit/sound/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BBC micro:bit sound

## Overview

This sample demonstrates how to use a piezo buzzer connected
to port P0 on the edge connector of the **BBC micro:bit v1** or
using the on-board buzzer on the **BBC micro:bit v2**.

## Requirements

Using **BBC micro:bit v1**, a separate piezo buzzer must be connected to the board.
One example is the MI:Power board that has a piezo buzzer in addition to a
coin-cell battery. Resellers of this board can be fairly easily found using online search.

The upgraded **BBC micro:bit v2** board does not need a separate buzzer as it has one
built-in on the backside of the board (marked as ‘speaker’).

## Building and running

The sample can be built as follows:

### Building for a BBC micro:bit v1

```shell
west build -b bbc_microbit samples/boards/bbc_microbit/sound
west flash
```

### Building for a BBC micro:bit v2

```shell
west build -b bbc_microbit_v2 samples/boards/bbc_microbit/sound
west flash
```

#### Sample Output

This sample outputs sounds through a piezo buzzer based on
button presses of the two main buttons. For each press the current
output frequency will be printed on the 5x5 LED display.
