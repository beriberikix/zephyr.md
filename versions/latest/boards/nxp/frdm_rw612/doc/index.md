---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nxp/frdm_rw612/doc/index.html
original_path: boards/nxp/frdm_rw612/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NXP FRDM\_RW612

## Overview

The RW612 is a highly integrated, low-power tri-radio wireless MCU with an
integrated 260 MHz ARM Cortex-M33 MCU and Wi-Fi 6 + Bluetooth Low Energy (LE) 5.3 / 802.15.4
radios designed for a broad array of applications, including connected smart home devices,
gaming controllers, enterprise and industrial automation, smart accessories and smart energy.

The RW612 MCU subsystem includes 1.2 MB of on-chip SRAM and a high-bandwidth Quad SPI interface
with an on-the-fly decryption engine for securely accessing off-chip XIP flash.

The advanced design of the RW612 delivers tight integration, low power and highly secure
operation in a space- and cost-efficient wireless MCU requiring only a single 3.3 V power supply.

## Hardware

- 260 MHz ARM Cortex-M33, tri-radio cores for Wifi 6 + BLE 5.3 + 802.15.4
- 1.2 MB on-chip SRAM

### Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| MCI\_IOMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| USART | on-chip | serial |
| BLE | on-chip | Bluetooth |
| DMA | on-chip | dma |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| TRNG | on-chip | entropy |
| WWDT | on-chip | watchdog |
| USBOTG | on-chip | usb |
| CTIMER | on-chip | counter |
| MRT | on-chip | counter |
| OS\_TIMER | on-chip | os timer |

The default configuration can be found in the defconfig file:

> [boards/nxp/frdm\_rw612/frdm\_rw612\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_defconfig)

Other hardware features are not currently supported

## Fetch Binary Blobs

To support Bluetooth, frdm\_rw612 requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the JLink Firmware.

### Configuring a Console

Connect a USB cable from your PC to J10, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b frdm_rw612 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.6.0 *****
Hello World! frdm_rw612
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b frdm_rw612 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v3.6.0 *****
Hello World! frdm_rw612
```

### Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

Those binary blobs can be used in two different ways, depending if [`CONFIG_NXP_MONOLITHIC_BT`](../../../../kconfig.md#CONFIG_NXP_MONOLITHIC_BT "CONFIG_NXP_MONOLITHIC_BT")
is enabled or not:

- [`CONFIG_NXP_MONOLITHIC_BT`](../../../../kconfig.md#CONFIG_NXP_MONOLITHIC_BT "CONFIG_NXP_MONOLITHIC_BT") is enabled (default):

The required binary blob will be linked with the application image directly, forming
one single monolithic image.
The user has nothing else to do other than flashing the application to the board.

- [`CONFIG_NXP_MONOLITHIC_BT`](../../../../kconfig.md#CONFIG_NXP_MONOLITHIC_BT "CONFIG_NXP_MONOLITHIC_BT") is disabled:

In this case, the BLE blob won’t be linked with the application, so the user needs to manually
flash the BLE binary blob to the board at the address `0x18540000`.
The binary blob will be located here: `<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x/rw61x_sb_ble_a2.bin`

### Resources
