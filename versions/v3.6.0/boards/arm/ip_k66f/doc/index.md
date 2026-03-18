---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/ip_k66f/doc/index.html
original_path: boards/arm/ip_k66f/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SEGGER IP Switch Board

## Overview

The Segger IP Switch Board is a Evaluation board based on NXP Kinetis K66 MCU.
It comes with Micrel/Microchip KSZ8794CNX integrated 4-port 10/100 managed
Ethernet switch with Gigabit RGMII/MII/RMII interface.

- KSZ8794CNX enables evaluation for switch functions
- On-board debug probe J-Link-OB for programming

![IP-K66F](../../../../_images/ip_k66f.jpg)

## Hardware

- MK66FN2M0VMD18 MCU (180 MHz, 2 MB flash memory, 256 KB RAM, low-power,
  crystal-less USB
- Dual role USB interface with micro-B USB connector
- 2 User LED
- On-board debug probe J-Link-OB for programming
- Micrel/Microchip Ethernet Switch KSZ8794CNX with 3 RJ45 connectors

For more information about the K66F SoC and IP-K66F board:

- [K66F Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/k-series-cortex-m4/k6x-ethernet/kinetis-k66-180-mhz-dual-high-speed-full-speed-usbs-2mb-flash-microcontrollers-mcus-based-on-arm-cortex-m4-core:K66_180)
- [K66F Datasheet](https://www.nxp.com/docs/en/data-sheet/K66P144M180SF5V2.pdf)
- [K66F Reference Manual](https://www.nxp.com/webapp/Download?colCode=K66P144M180SF5RMV2)
- [IP-K66F Website](https://www.segger.com/evaluate-our-software/segger/embosip-switch-board/)
- [IP-K66F User Guide](https://www.segger.com/downloads/emnet/UM06002)
- [IP-K66F Schematics](https://www.segger.com/downloads/emnet/embOSIP_SwitchBoard_V2.0_WEB_Schematic.pdf)

### Supported Features

The ip\_k66f board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| WATCHDOG | on-chip | watchdog |
| FLASH | on-chip | soc flash |
| RTC | on-chip | rtc |

The default configuration can be found in the defconfig file:

> `boards/arm/ip_k66f/ip_k66f_defconfig`

Micrel/Microchip KSZ8794CNX Ethernet Switch is not currently
supported.

### Connections and IOs

The K66F SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTA8 | GPIO | Red LED |
| PTA10 | GPIO | RED LED |

### System Clock

The K66F SoC is configured to use the 12 MHz low gain crystal oscillator on the
board with the on-chip PLL to generate a 180 MHz system clock.

### Serial Port

The K66F SoC has six UARTs. None of them are used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe).

#### [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link Generic Firmware for V3.2 Bootloader](https://www.segger.com/downloads/jlink/OpenSDA_V3_2). Note that Segger
does provide an OpenSDA J-Link Board-Specific Firmware for this board, however
it is not compatible with the DAPLink bootloader.

The default flasher is `jlink` using the built-in SEGGER Jlink interface.

### Flashing

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ip_k66f samples/basic/blinky
west flash
```

Red LED0 should blink at 1 second delay.

### Debugging

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ip_k66f samples/basic/blinky
west debug
```

Step through the application in your debugger.

### Serial console

The `ip_k66f` board only uses Segger’s RTT console for providing serial
console. There is no physical serial port available.

- To communicate with this board one needs in one console:

`/opt/SEGGER/JLink_V664/JLinkRTTLogger -Device MK66FN2M0XXX18 -RTTChannel 1 -if SWD -Speed 4000 ~/rtt.log`

- In another one:

`nc localhost 19021`
