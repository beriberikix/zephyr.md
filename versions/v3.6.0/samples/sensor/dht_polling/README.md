---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/dht_polling/README.html
original_path: samples/sensor/dht_polling/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic Digital Humidity Temperature sensor polling sample

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

Make sure the aliases are in devicetree, then build and run with:

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
