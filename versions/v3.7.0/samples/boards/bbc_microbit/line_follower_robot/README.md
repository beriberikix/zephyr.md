---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/bbc_microbit/line_follower_robot/README.html
original_path: samples/boards/bbc_microbit/line_follower_robot/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BBC micro:bit line-follower robot

## Overview

This sample controls a stand-alone line-following DFRobot Maqueen
robot chassis containing a BBC micro:bit board.

## Requirements

To build and run this sample you’ll need a [DFRobot Maqueen robot
chassis (ROB0148)](https://www.dfrobot.com/product-1783.html)
with a BBC micro:bit board. Use black tape to create a line track
for the robot to follow. Build and flash the program to the BBC
micro:bit board (described below), turn on the robot,
and put it on the black line track.

## Building and running

Build and flash this sample project using these commands:

```shell
west build -b bbc_microbit samples/boards/bbc_microbit/line_follower_robot
west flash
```

## Sample Output

The sample program controls the robot to follow a line track and does
not write to the console. You can watch this [robot video](https://youtu.be/tIvoHQjo8a4)
to see it in action.
