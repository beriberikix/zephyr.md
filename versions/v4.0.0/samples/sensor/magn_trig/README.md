---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/magn_trig/README.html
original_path: samples/sensor/magn_trig/README.html
---

# Magnetometer trigger

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/magn_trig/README.rst/..)

## Overview

Sample application that reads magnetometer (X, Y, Z) data from
the available device that implements SENSOR\_TRIG\_DATA\_READY and SENSOR\_CHAN\_MAGN\_\*.

## Building and Running

```devicetree
/ {
  aliases {
    magn0 = &fxos8700;
  };
};
```

Make sure the aliases are in devicetree, then build and run with:

```shell
west build -b <board to use> samples/sensor/magn_trig
west flash
```

### Sample Output

```shell
fxos8700@1d (x, y, z):    (   -0.107000,     0.118000,    -1.026000)
fxos8700@1d (x, y, z):    (   -0.132000,     0.083000,    -0.981000)
fxos8700@1d (x, y, z):    (   -0.143000,     0.102000,    -0.931000)
fxos8700@1d (x, y, z):    (   -0.153000,     0.126000,    -0.843000)
fxos8700@1d (x, y, z):    (   -0.145000,     0.152000,    -0.802000)
fxos8700@1d (x, y, z):    (   -0.143000,     0.125000,    -0.740000)
fxos8700@1d (x, y, z):    (   -0.133000,     0.130000,    -0.736000)
fxos8700@1d (x, y, z):    (   -0.133000,     0.124000,    -0.776000)
fxos8700@1d (x, y, z):    (   -0.120000,     0.123000,    -0.776000)
fxos8700@1d (x, y, z):    (   -0.135000,     0.120000,    -0.782000)
fxos8700@1d (x, y, z):    (   -0.129000,     0.116000,    -0.787000)
```
