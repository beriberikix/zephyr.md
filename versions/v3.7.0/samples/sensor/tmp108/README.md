---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/tmp108/README.html
original_path: samples/sensor/tmp108/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# TMP108 sample

## Description

This sample writes the temperature to the console once every 3 seconds. There are
macro definitions included for turning off and on alerts if that is set up, and
also using low power one shot mode.

## Requirements

A board with the [`ti,tmp108`](../../../build/dts/api/bindings/sensor/ti%2Ctmp108.md#std-dtcompatible-ti-tmp108) built in to its [devicetree](../../../build/dts/index.md#dt-guide),
or a devicetree overlay with such a node added.

### Sample Output

```shell
** Booting Zephyr OS build zephyr-v2.6.0-1923-g72bb75a360ce  ***
TI TMP108 Example, arm
Temperature is 22.875C
Temperature is 22.875C
Temperature is 22.875C
Temperature is 22.875C
Temperature is 22.875C
Temperature is 22.875C
```
