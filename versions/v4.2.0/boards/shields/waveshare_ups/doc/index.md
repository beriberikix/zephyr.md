---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/waveshare_ups/doc/index.html
original_path: boards/shields/waveshare_ups/doc/index.html
---

# Waveshare Pico UPS-B shield

## Overview

The Waveshare Pico UPS-B shield is an uninterruptible Power supply (UPS)
module designed for the Raspberry Pi Pico which uses the Texas Instruments’ INA219
current/power Monitor. It communicates with the Raspberry Pi Pico over I2C

![Waveshare Pico UPS-B shield](https://docs.zephyrproject.org/4.2.0/_images/waveshare_pico_ups_b.jpg)

Waveshare Pico UPS-B shield

### Hardware

- INA219

  > - Senses bus voltages from 0 to 26 V
  > - Reports current, voltage and power
  > - 16 Programmable Addresses
  > - SOT23-8 and SOIC-8 packages
  > - Calibration registers
- ETA6003

  > - Switching charger with power path management
  > - Up to 95% DC-DC efficiency
  > - 0mΩ power path MOSFET
  > - Up to 2.5A max charging current
- Connectivity

  > - Raspberry Pi Pico compatible (I2C)
  > - 2 pin jst header for Li-po battery
- Power Supply

  > - 3.3V ~ 5V
- Components

  > - Power switch
  > - Power LED
  > - Charging LED

For more information about the Waveshare Pico UPS-B:

- [Waveshare Pico UPS website](https://www.waveshare.com/wiki/Pico-UPS-B)
- [INA219 data sheet](https://www.ti.com/lit/ds/symlink/ina219.pdf)
- [ETA6003 data sheet](https://www.waveshare.com/w/upload/3/3f/ETA6003.pdf)

## Programming

Set `--shield waveshare_pico_ups_b` when you invoke `west build` or `cmake` in your Zephyr application. For
example:

```shell
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_ups_b samples/sensor/ina219
west flash
```
