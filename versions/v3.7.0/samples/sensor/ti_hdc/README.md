---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/ti_hdc/README.html
original_path: samples/sensor/ti_hdc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# TI\_HDC Sample

## Description

This sample application periodically takes Temperature and Humidity
using the ti\_hdc sensor driver. The result is written to the console.

## Requirements

This sample needs a compatible sensor like HDC1010 or HDC1080
connected to the target board’s I2C connector.

Example Breakout Boards:

- Pmod HYGRO: Humidity and Temperature Sensor Breakout board

## Wiring

This sample is tested with the STM32L496ZG nucleo and the Pmod HYGRO
Temp/RH breakout board.

The sensor operates at 3.3V and uses I2C to communicate with the board.

External Wires:

- Breakout **GND** pin <–> Nucleo **GND** pin
- Breakout **VCC** pin <–> Nucleo **3V3** pin
- Breakout **SDA** pin <–> Nucleo **CN7-D14** pin
- Breakout **SCL** pin <–> Nucleo **CN7-D15** pin

## Building and Running

This sample builds one application for the HDC1080 sensor.
Build/Flash Steps:

```shell
west build -b nucleo_l496zg samples/sensor/ti_hdc/
west flash
```

## Sample Output

```shell
Running on arm!
Dev 0x20001160 name HDC1080 is ready!
Fetching...
Raw Temp = 25144, Temp = 23.305053 C, Raw RH = 32292, RH = 49.273681 %
Fetching...
Raw Temp = 25148, Temp = 23.315124 C, Raw RH = 32424, RH = 49.475097 %
...
```

## Build Testing

```shell
$ZEPHYR_BASE/scripts/twister -T $ZEPHYR_BASE/samples/sensor/ti_hdc/ -p nucleo_l496zg --device-testing --device-serial /dev/ttyACM0 -t build
```

## Target Testing

```shell
$ZEPHYR_BASE/scripts/twister -T $ZEPHYR_BASE/samples/sensor/ti_hdc/ -p nucleo_l496zg --device-testing --device-serial /dev/ttyACM0 -t target
```

## References
