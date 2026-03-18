---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/dht/README.html
original_path: samples/sensor/dht/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DHT: Aosong DHT Digital-output Humidity and Temperature Sensor

## Description

This sample application periodically (0.5 Hz) measures the ambient
temperature and humidity. The result is written to the console.

## Wiring

This sample uses an external breakout for the sensor. A devicetree
overlay must be provided to identify the sensor variant and the GPIO
used to control the sensor.

## Building and Running

After providing a devicetree overlay that specifies the sensor location,
build this sample app using:

```shell
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 samples/sensor/dht
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v2.1.0-329-g38418b26c4cc  ***
[0:00:00.027]: 20.0 Cel ; 48.7 %RH
[0:00:02.053]: 19.8 Cel ; 48.7 %RH
[0:00:04.079]: 20.0 Cel ; 48.7 %RH
[0:00:06.105]: 19.8 Cel ; 48.7 %RH
[0:00:08.130]: 20.0 Cel ; 48.8 %RH
[0:00:10.156]: 20.1 Cel ; 48.8 %RH
[0:00:12.182]: 19.7 Cel ; 48.7 %RH
[0:00:14.207]: 20.0 Cel ; 48.8 %RH
```

<repeats endlessly>
