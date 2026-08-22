---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/siwx917_rb4342a/doc/index.html
original_path: boards/silabs/radio_boards/siwx917_rb4342a/doc/index.html
---

# SiWx917 Wi-Fi 6 and Bluetooth LE 8 MB Flash + 8 MB ext PSRAM Radio Board (SLWRB4342A)

Board Overview

[![../../../../../_images/siwx917_rb4342a.webp](../../../../../_images/siwx917_rb4342a.webp)
](../../../../../_images/siwx917_rb4342a.webp)

SiWx917 Wi-Fi 6 and Bluetooth LE 8 MB Flash + 8 MB ext PSRAM Radio Board (SLWRB4342A)

Name:
:   `siwx917_rb4342a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   siwg917m111mgtba

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/siwx917_rb4342a/doc/index.rst/../..)

## Overview

The SiWx917-RB4342A (aka BRD4342A) radio board provides support for the Silicon
Labs SiWG917 SoC. This board cannot be used stand-alone and requires a a
[Wireless Pro Kit](https://www.silabs.com/development-tools/wireless/wireless-pro-kit-mainboard) Mainboard (Si-MB4002A aka BRD4002A), for power, debug
options etc.

SiWG917 is an ultra-low power SoC that includes hardware support for Single-Band
Wi-Fi 6 + Bluetooth LE 5.4, Matter…

## Hardware

For more information about the SiWG917 SoC and BRD4342A board, refer to these
documents:

- [SiWG917 Website](https://www.silabs.com/wireless/wi-fi/siwx917-wireless-socs)
- [SiWG917 Datasheet](https://www.silabs.com/documents/public/data-sheets/siwg917-datasheet.pdf)
- [SiWG917 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/siw917x-family-rm.pdf)
- [BRD4342A Website](https://www.silabs.com/development-tools/wireless/wi-fi/siwx91x-rb4342a-wifi-6-bluetooth-le-soc-radio-board)
- [BRD4342A User Guide](https://www.silabs.com/documents/public/user-guides/ug564-brd4342a-user-guide.pdf)

### Supported Features

The `siwx917_rb4342a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Refer to the [SiWx917 Wi-Fi Features (Alpha)](../../common/wifi.md#siwx917-wifi-features) page for a list of supported Wi-Fi features.

## Programming and Debugging

### Flashing

Applications for the `siwx917_rb4342a` board can be built in the usual
way. The flash method requires on [Simplicity Commander](https://www.silabs.com/developer-tools/simplicity-studio/simplicity-commander) installed on the host.

Then, connect the BRD4002A board with a mounted BRD4342A radio module to your
host computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b siwx917_rb4342a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! siwx917_rb4342a
```

### Debugging

Debuggning relies on JLink tool. JLink is not able to flash the firmware. So
debug session has to be done in two steps. `west flash` will flahs the
firmware using Simplicity Commander. Then `west attach` will use JLink to
attach to the board. The Zephyr image may has already booted when user runs
`west attach`. User may execute `monitor reset` in the gdb prompt to reset
the board.
