---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/dht_polling/README.html
original_path: samples/sensor/dht_polling/README.html
---

# Generic digital humidity temperature sensor polling

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/dht_polling/README.rst/..)

## Overview

This sample application demonstrates how to use digital humidity temperature
sensors.

## Building and Running

This sample supports up to 10 humidity/temperature sensors. Each sensor needs to
be aliased as `dhtN` where `N` goes from `0` to `9`. For example:

```devicetree
/ {
      aliases {
                      dht0 = &hs300x;
              };
      };
```

Make sure the aliases are in devicetree.

It also requires a correct fixture setup when the sensor is present.
For the correct execution of that sample in twister, add into boards’s
map-file next fixture settings:

```text
- fixture: fixture_i2c_hs300x
```

Then build and run with:

```shell
west build -b <board to use> samples/sensor/dht_polling
west flash
```

### Sample Output

```shell
hs300x@44: temp is 25.31 °C humidity is 30.39 %RH
hs300x@44: temp is 25.51 °C humidity is 30.44 %RH
hs300x@44: temp is 25.51 °C humidity is 30.37 %RH
hs300x@44: temp is 25.51 °C humidity is 30.39 %RH
hs300x@44: temp is 25.31 °C humidity is 30.37 %RH
hs300x@44: temp is 25.31 °C humidity is 30.35 %RH
hs300x@44: temp is 25.51 °C humidity is 30.37 %RH
hs300x@44: temp is 25.51 °C humidity is 30.37 %RH
hs300x@44: temp is 25.51 °C humidity is 30.39 %RH
hs300x@44: temp is 25.51 °C humidity is 30.44 %RH
hs300x@44: temp is 25.51 °C humidity is 30.53 %RH
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
