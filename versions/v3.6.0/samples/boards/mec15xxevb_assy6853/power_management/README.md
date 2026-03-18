---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/mec15xxevb_assy6853/power_management/README.html
original_path: samples/boards/mec15xxevb_assy6853/power_management/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MEC15xx sample board test application

## Overview

This sample demonstrates power management features on MEC15xx-based boards.
It showcase simple app that allows to enter into light and deep sleep.

## Building and Running

The sample can be built and executed on boards using west.
No pins configurations, except GPIO014 is used as indicator for entry/exit.

### Sample output

```shell
Wake from Light Sleep
Wake from Deep Sleep
ResumeBBBAA
Wake from Light Sleep
Suspend...
Wake from Deep Sleep
ResumeBBBAA
```

note:: The values shown above might differ.
