---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nxp/usb_kw24d512/doc/index.html
original_path: boards/nxp/usb_kw24d512/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NXP USB-KW24D512

## Overview

The USB-KW24D512 is an evaluation board in a convenient USB dongle
form factor based on the NXP MKW24D512 System-in-Package (SiP) device
(KW2xD wireless MCU series).
MKW24D512 wireless MCU provides a low-power, compact device with
integrated IEEE 802.15.4 radio. The board can be used as a packet sniffer,
network node, border router or as a development board.

## Hardware

- Kinetis KW2xD-2.4 GHz 802.15.4 Wireless Radio Microcontroller
  (50 MHz, 512 KB flash memory, 64 KB RAM, low-power, crystal-less USB)
- USB Type A Connector
- Two blue LEDs
- One user push button
- One reset button
- Integrated PCB Folded F-type antenna
- 10-pin (0.05”) JTAG debug port for target MCU

For more information about the KW2xD SiP and USB-KW24D512 board:

- [KW2xD Website](https://www.nxp.com/products/wireless/thread/kinetis-kw2xd-2.4-ghz-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m4-core:KW2xD)
- [KW2xD Datasheet](https://www.nxp.com/docs/en/data-sheet/MKW2xDxxx.pdf)
- [KW2xD Reference Manual](https://www.nxp.com/webapp/Download?colCode=MKW2XDXXXRM)
- [USB-KW24D512 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/ieee-802.15.4-packet-sniffer-usb-dongle-form-factor:USB-KW24D512)
- [USB-KW24D512 Hardware Reference Manual](https://www.nxp.com/webapp/Download?colCode=USB-KW2XHWRM)

### Supported Features

The USB-KW24D512 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| WATCHDOG | on-chip | watchdog |
| UART | on-chip | serial port-polling; serial port-interrupt |
| FLASH | on-chip | soc flash |
| USB | on-chip | USB device |
| RNGA | on-chip | entropy; random |
| FTFL | on-chip | flash programming |

The default configuration can be found in
[boards/nxp/usb\_kw24d512/usb\_kw24d512\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/usb_kw24d512/usb_kw24d512_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

The KW2xD SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTA1 | UART0\_RX | UART Console |
| PTA2 | UART0\_TX | UART Console |
| PTC4 | GPIO | SW1 |
| PTD4 | GPIO | Blue LED (D2) |
| PTD5 | GPIO | Blue LED (D3) |
| PTB10 | SPI1\_PCS0 | internal connected to MCR20A |
| PTB11 | SPI1\_SCK | internal connected to MCR20A |
| PTB16 | SPI1\_SOUT | internal connected to MCR20A |
| PTB17 | SPI1\_SIN | internal connected to MCR20A |
| PTB19 | GPIO | internal connected to MCR20A (Reset) |
| PTB3 | GPIO | internal connected to MCR20A (IRQ\_B) |
| PTC0 | GPIO | internal connected to MCR20A (GPIO5) |

### System Clock

USB-KW24D512 contains 32 MHz oscillator crystal, which is connected to the
clock pins of the radio transceiver. The MCU is configured to
use the 4 MHz external clock from the transceiver with the on-chip PLL
to generate a 48 MHz system clock.

### Serial Port

The KW2xD SoC has three UARTs. One is configured and can be used for the
console, but it uses the same pins as the JTAG interface and is only
accessible via the JTAG SWD connector.

### USB

The KW2xD SoC has a USB OTG (USBOTG) controller that supports both
device and host functions. Only USB device function is supported in Zephyr
at the moment. The USB-KW24D512 board has a USB Type A connector and
can only be used in device mode.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe).

#### [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Attach a J-Link 10-pin connector to J1.

### Configuring a Console

The console is available using [Segger RTT](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/).

Connect a USB cable from your PC to J5.

Once you have started a debug session, run telnet:

```shell
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
SEGGER J-Link V6.44 - Real time terminal output
SEGGER J-Link ARM V10.1, SN=600111924
Process: JLinkGDBServerCLExe
```

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west flash
```

The Segger RTT console is only available during a debug session. Use `attach`
to start one:

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west attach
```

Run telnet as shown earlier, and you should see the following message in the
terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! usb_kw24d512
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west debug
```

Run telnet as shown earlier, step through the application in your debugger, and
you should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! usb_kw24d512
```
