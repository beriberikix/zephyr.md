---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/sensing/simple/README.html
original_path: samples/subsys/sensing/simple/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sensing subsystem

## Overview

A simple sample that shows how to use the sensors with sensing subsystem APIs. It defines
two sensors, with the underlying device bmi160 emulator, and gets the sensor
data in defined interval.

The program runs in the following sequence:

1. Define the sensor in the dts
2. Open the sensor
3. Register call back.
4. Set sample interval
5. Run forever and get the sensor data.

## Building and Running

This application can be built and executed on [native\_sim](../../../../boards/native/native_sim/doc/index.md#native-sim) as follows:

```shell
west build -b native_sim samples/subsys/sensing/simple
west build -t run
```

To build for another board, change “native\_sim” above to that board’s name.
At the current stage, it only support native sim.
