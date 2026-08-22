---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/distance_polling/README.html
original_path: samples/sensor/distance_polling/README.html
---

# Generic distance measurement

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/distance_polling/README.rst/..)

## Overview

This sample application periodically measures the distance of an object and
display it, via the console.

## Building and Running

This sample supports up to 5 distance sensors. Each sensor needs to be aliased
as `distanceN` where `N` goes from `0` to `4`. For example:

```devicetree
/ {
        aliases {
                distance0 = &vl53l1x;
        };
};
```

Make sure the aliases are in devicetree, then build and run with:

```shell
west build -b <board to use> samples/sensor/distance_polling
west flash
```

### Sample Output

```shell
vl53l1x: 0.153m
vl53l1x: 0.154m
vl53l1x: 0.154m
vl53l1x: 0.153m
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
