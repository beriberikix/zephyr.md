---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gardena/sgrm/doc/index.html
original_path: boards/gardena/sgrm/doc/index.html
---

# Smart Garden Radio Module

Board Overview

[![../../../../_images/sgrm.webp](../../../../_images/sgrm.webp)
](../../../../_images/sgrm.webp)

Smart Garden Radio Module

Vendor:
:   GARDENA GmbH

Architecture:
:   arm

SoC:
:   sim3u167

## Overview

This is a SoM that is used as a radio module by the GARDENA smart gateway ([manual](https://www.gardena.com/tdrdownload//pub000070911/doc000120830), [FOSS parts](https://github.com/husqvarnagroup/smart-garden-gateway-public)).

## Hardware

- Silicon Labs [SiM3U167-B-GM](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.SiM3U167-B-GQ?tab=specs) SoC
- Silicon Labs [Si4467](https://www.silabs.com/wireless/proprietary/ezradiopro-sub-ghz-ics/device.si4467?tab=specs) transceiver (via SPI)
- Controls an RGB LED via high drive pins. It’s expected to mirror the state of 3 low-drive pins
  coming from the Linux SoC.
- UART is connected to the Linux SoC. Usually it’s used for PPP, but it can also be used for
  debugging when PPP is not active.

### Supported Features

The `sgrm` board target supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| DMA | on-chip | dma |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |

### Connections and IOs

| Pin | Name | Note |
| --- | --- | --- |
| PB0.0 | TX (O) | Serial connection to the Linux SoM |
| PB0.1 | RX (I) |
| PB0.2 | RTS (O) |
| PB0.3 | CTS (I) |
| PB0.4 | LED red (I) | Controlled by the Linux SoM |
| PB0.5 | LED green (I) |
| PB0.6 | LED blue (I) |
| PB0.13 | TX (O) | UART1 for debugging (no connection to Linux SoM) |
| PB0.14 | RX (I) |
| PB4.0 | LED red (O) | Mirrors PB0.4 |
| PB4.1 | LED green (O) | Mirrors PB0.5 |
| PB4.2 | LED blue (O) | Mirrors PB0.6 |

## Programming and Debugging

### Flashing

The easiest way is to do this via SSH from the Linux SoM that’s connected to the SiM3U SoM.

On your building machine:

```shell
scp -O build/zephyr/zephyr.hex root@IP:/tmp/
```

On the gateway:

```shell
openocd -f board/gardena_radio.cfg -c 'program /tmp/zephyr.hex verify exit'
reset-rm
```

### Debugging

The easiest way is to do this via SSH from the Linux gateway as well:

```shell
openocd -f board/gardena_radio.cfg -c init
```
