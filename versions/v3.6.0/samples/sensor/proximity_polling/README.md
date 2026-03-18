---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/proximity_polling/README.html
original_path: samples/sensor/proximity_polling/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic Proximity Sensor Sample

## Overview

This sample demonstrates how to use one or multiple proximity sensors.

## Building and Running

The sample supports up to 10 proximity sensors. The number of the sensors will
automatically detected from the devicetree, you only need to set aliases from
`prox-sensor-0` to `prox-sensor-9`.

For example:

```devicetree
/ {
           aliases {
                   prox-sensor0 = &tmd2620;
           };
};
```

After creating the devicetree overlay you can build the sample with:

```shell
west build -b <your_board> samples/sensor/proximity_polling
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.2.0-210-gd95295f08646  ***
Proximity sensor sample application
Found 1 proximity sensor(s): tmd2620@29
Proximity on tmd2620@29: 202
Proximity on tmd2620@29: 205
Proximity on tmd2620@29: 204
Proximity on tmd2620@29: 60
Proximity on tmd2620@29: 1
```
