---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/litex/i2s/README.html
original_path: samples/boards/litex/i2s/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# I2S example

## Overview

This is a simple I2S audio transceiver example. You can plug any source of music and listen to it.

## Audio Format

The driver requires and provides Audio data with the following parameters:

- 44100 kHz sample rate
- Signed 24 bit PCM
- Stereo
- Little endian

## Building

```text
mkdir build && cd build
cmake -DBOARD=litex_vexriscv ..
make
```

## Known issues

It seems that after a few minutes some music delay occurs, this is because the sound driver is not able to send data as fast as it receives it.
