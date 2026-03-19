---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/apds9960/README.html
original_path: samples/sensor/apds9960/README.html
---

# APDS9960 RGB, ambient light, and gesture sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/apds9960/README.rst/..)

## Overview

This sample application demonstrates how to use the APDS9960 sensor to get
ambient light, RGB, and proximity (or gesture) data. This sample checks the
sensor in polling mode (without an interrupt trigger).

## Building and Running

This sample application uses an APDS9960 sensor connected to a board
(for example as shown in this
[Sparkfun APDS9960 tutorial](https://www.sparkfun.com/products/12787)).

```shell
west build -b reel_board samples/sensor/apds9960
west flash
```

### Sample Output

```shell
ambient light intensity without trigger is 387
proxy without trigger is 115
ambient light intensity without trigger is 386
proxy without trigger is 112
ambient light intensity without trigger is 386
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
