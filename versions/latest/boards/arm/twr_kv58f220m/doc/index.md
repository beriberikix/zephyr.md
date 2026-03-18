---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/twr_kv58f220m/doc/index.html
original_path: boards/arm/twr_kv58f220m/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP TWR-KV58F220M

## Overview

The TWR-KV58F220M is a development board for NXP Kinetis KV5x 32-bit
MCU-based platforms. The onboard OpenSDAv2 serial and debug adapter,
running an open source bootloader, offers options for serial
communication, flash programming, and run-control debugging.

![TWR-KV58F220M](../../../../_images/twr_kv58f220m.jpg)

TWR-KV58F220M (Credit: NXP)

## Hardware

- MKV58F1M0VLQ24 MCU (up to 240 MHz, 1 MB flash memory, 256 KB RAM,
  and 144 Low profile Quad Flat Package (LQFP))
- 1.8 V or 3.3 V MCU operation
- 6-axis FXOS8700CQ digital accelerometer and magnetometer
- Four user LEDs
- Four user push-buttons
- Potentiometer
- Two general purpose TWRPI headers
- Motor pin header

For more information about the KV5x SoC and the TWR-KV58F220M board, see
these NXP reference documents:

- [KV5x Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/general-purpose-mcus/kv-series-cortex-m4-m0-plus-m7/kinetis-kv5x-240-mhz-motor-control-and-power-conversion-ethernet-mcus-based-on-arm-cortex-m7:KV5x)
- [KV5x Datasheet](https://www.nxp.com/docs/en/data-sheet/KV5XP144M240.pdf)
- [KV5x Reference Manual](https://www.nxp.com/webapp/Download?colCode=KV5XP144M240RM)
- [TWR-KV58F220M Website](https://www.nxp.com/TWR-KV58F220M)
- [TWR-KV58F220M User Guide](https://www.nxp.com/webapp/Download?colCode=TWRKV58F220MUG)
- [TWR-KV58F220M Schematics](https://www.nxp.com/webapp/Download?colCode=TWR-KV58F220M-SCH)

### Supported Features

The twr\_kv58f220m board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| FLASH | on-chip | soc flash |
| I2C | on-chip | i2c |
| SENSOR | off-chip | fxos8700 polling; fxos8700 trigger |
| SPI | on-chip | spi |
| ADC | on-chip | adc |

The default configuration can be found in the defconfig file:
`boards/arm/twr_kv58f220m/twr_kv58f220m_defconfig`.

Other hardware features are not currently supported by the port.

### System Clock

The KV58 SoC is configured to use the 50 MHz external oscillator on the
board with the on-chip PLL to generate a 237.5 MHz system clock.

### Serial Port

The KV58 SoC has six UARTs. UART0 is configured for the console. The
remaining UARTs are not used.

### Accelerometer and magnetometer

The TWR-KV58F220M board by default only supports polling the FXOS8700
accelerometer and magnetometer for sensor values
(`CONFIG_FXOS8700_TRIGGER_NONE=y`).

In order to support FXOS8700 triggers (interrupts), shunts must be placed on
the jumpers `J2` and `J9`. A trigger option also must be enabled in Kconfig
(either `CONFIG_FXOS8700_TRIGGER_GLOBAL_THREAD=y` or
`CONFIG_FXOS8700_TRIGGER_OWN_THREAD=y`).

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

This board integrates an OpenSDA debug probe. However, it can currently only be
used for flashing the KV58 SoC by copying the compiled firmware to the USB Mass
Storage Device. The board cannot be debugged using the OpenSDA probe, since
pyOCD does not support the target. The OpenSDA J-Link firmware (as of release
2019-06-03) also cannot be used, since the flash algorithm for the KV58 seems to
be broken at the time of writing.

An external J-Link debug probe connected to the JTAG header J13 is used to debug
the target.

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Using west:

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
```

Using CMake and ninja:

```shell
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=twr_kv58f220m samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild
```

### Configuring a Console

Even though the OpenSDA probe cannot be used for debugging, we will use it as a
USB-to-serial adapter for the serial console.

Connect a USB cable from your PC to J22.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_kv58f220m
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_kv58f220m
```
