---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mimxrt685_evk/doc/index.html
original_path: boards/arm/mimxrt685_evk/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP MIMXRT685-EVK

## Overview

The i.MX RT600 is a crossover MCU family optimized for 32-bit immersive audio
playback and voice user interface applications combining a high-performance
Cadence Tensilica HiFi 4 audio DSP core with a next-generation Cortex-M33
core. The i.MX RT600 family of crossover MCUs is designed to unlock the
potential of voice-assisted end nodes with a secure, power-optimized embedded
processor.

The i.MX RT600 family provides up to 4.5MB of on-chip SRAM and several
high-bandwidth interfaces to access off-chip flash, including an Octal/Quad SPI
interface with an on-the-fly decryption engine.

![MIMXRT685-EVK](../../../../_images/mimxrt685_evk.jpg)

## Hardware

- MIMXRT685SFVKB Cortex-M33 (300 MHz, 128 KB TCM) core processor with Cadence Xtensa HiFi4 DSP
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP protocol (supporting Cortex M33 debug only)
- High speed USB port with micro A/B connector for the host or device functionality
- UART, I2C and SPI port bridging from i.MX RT685 target to USB via the on-board debug probe
- 512 MB Macronix Octal SPI Flash operating at 1.8 V
- 4.5 MB Apmemory PSRAM
- Full size SD card slot (SDIO)
- NXP PCA9420UK PMIC
- User LEDs
- Reset and User buttons
- Arduino and PMod/Host expansion connectors
- NXP FXOS8700CQ accelerometer
- Stereo audio codec with line in/out and electret microphone
- Stereo NXP TFA9894 digital amplifiers, with option for external +5V power for higher performance speakers
- Support for up to eight off-board digital microphones via 12-pin header
- Two on-board DMICS

For more information about the MIMXRT685 SoC and MIMXRT685-EVK board, see
these references:

- [i.MX RT685 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600)
- [i.MX RT685 Datasheet](https://www.nxp.com/docs/en/data-sheet/DS-RT600.pdf)
- [i.MX RT685 Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM11147)
- [MIMXRT685-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt600-evaluation-kit:MIMXRT685-EVK)
- [MIMXRT685-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=UM11159)
- [MIMXRT685-EVK Schematics](https://www.nxp.com/downloads/en/design-support/RT685-DESIGNFILES.zip)

### Supported Features

NXP considers the MIMXRT685-EVK as a superset board for the i.MX RT6xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT6xx family. NXP prioritizes enabling
this board with new support for Zephyr features. The mimxrt685\_evk board
configuration supports the hardware features below. Another very similar
board is the [NXP MIMXRT595-EVK](../../mimxrt595_evk/doc/index.md#mimxrt595-evk), and that board may have additional features
already supported, which can also be re-used on this mimxrt685\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| OS\_TIMER | on-chip | os timer |
| IOCON | on-chip | pinmux |
| GPIO | on-chip | gpio |
| FLASH | on-chip | OctalSPI Flash |
| USART | on-chip | serial port-polling; serial port-interrupt |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| I2S | on-chip | i2s |
| CLOCK | on-chip | clock\_control |
| HWINFO | on-chip | Unique device serial number |
| RTC | on-chip | counter |
| PWM | on-chip | pwm |
| WDT | on-chip | watchdog |
| SDHC | on-chip | disk access |
| USB | on-chip | USB device |
| ADC | on-chip | adc |
| CTIMER | on-chip | counter |
| TRNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in the defconfig file:

> `boards/arm/mimxrt685_evk/mimxrt685_evk_cm33_defconfig`

Other hardware features are not currently supported by the port.

### Connections and IOs

The MIMXRT685 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | USART | USART RX |
| PIO0\_1 | USART | USART TX |
| PIO0\_14 | GPIO | GREEN LED |
| PIO1\_1 | GPIO | SW0 |
| PIO0\_17 | I2C | I2C SDA |
| PIO0\_18 | I2C | I2C SCL |
| PIO1\_5 | GPIO | FXOS8700 TRIGGER |
| PIO1\_5 | SPI | SPI MOSI |
| PIO1\_4 | SPI | SPI MISO |
| PIO1\_3 | SPI | SPI SCK |
| PIO1\_6 | SPI | SPI SSEL |
| PIO0\_23 | I2S | I2S DATAOUT |
| PIO0\_22 | I2S | I2S TX WS |
| PIO0\_21 | I2S | I2S TX SCK |
| PIO0\_9 | I2S | I2S DATAIN |
| PIO0\_29 | USART | USART TX |
| PIO0\_30 | USART | USART RX |
| PIO1\_11 | FLEXSPI0B\_DATA0 | OctalSPI Flash |
| PIO1\_12 | FLEXSPI0B\_DATA1 | OctalSPI Flash |
| PIO1\_13 | FLEXSPI0B\_DATA2 | OctalSPI Flash |
| PIO1\_14 | FLEXSPI0B\_DATA3 | OctalSPI Flash |
| PIO1\_29 | FLEXSPI0B\_SCLK | OctalSPI Flash |
| PIO2\_12 | PIO2\_12 | OctalSPI Flash |
| PIO2\_17 | FLEXSPI0B\_DATA4 | OctalSPI Flash |
| PIO2\_18 | FLEXSPI0B\_DATA5 | OctalSPI Flash |
| PIO2\_19 | FLEXSPI0B\_SS0\_N | OctalSPI Flash |
| PIO2\_22 | FLEXSPI0B\_DATA6 | OctalSPI Flash |
| PIO2\_23 | FLEXSPI0B\_DATA7 | OctalSPI Flash |
| PIO0\_27 | SCT0\_OUT7 | PWM |
| PIO1\_30 | SD0\_CLK | SD card |
| PIO1\_31 | SD0\_CMD | SD card |
| PIO2\_0 | SD0\_D0 | SD card |
| PIO2\_1 | SD0\_D1 | SD card |
| PIO2\_2 | SD0\_D2 | SD card |
| PIO2\_3 | SD0\_D3 | SD card |
| PIO2\_4 | SD0\_WR\_PRT | SD card |
| PIO2\_9 | SD0\_CD | SD card |
| PIO2\_10 | SD0\_RST | SD card |

### System Clock

The MIMXRT685 EVK is configured to use the OS Event timer
as a source for the system clock.

### Serial Port

The MIMXRT685 SoC has 8 FLEXCOMM interfaces for serial communication. One is
configured as USART for the console and the remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the LPC-Link2.

LinkServer CMSIS-DAPLPCLink2 JLink OnboardJLink External

1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
   search path. LinkServer works with the default CMSIS-DAP firmware included in
   the on-board debugger.
2. Make sure the jumpers JP17, JP18 and JP19 are installed.

linkserver is the default runner for this board

```shell
west flash
west debug
```

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To connect the SWD signals to onboard debug circuit, install jumpers JP17, JP18 and JP19,
   if not already done (these jumpers are installed by default).
3. Follow the instructions in [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to program the
   J-Link firmware. Please make sure you have the latest firmware for this board.

```shell
west flash -r jlink
west debug -r jlink
```

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To disconnect the SWD signals from onboard debug circuit, **remove** jumpers J17, J18,
   and J19 (these are installed by default).
3. Connect the J-Link probe to J2 10-pin header.

See [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) for more information.

```shell
west flash -r jlink
west debug -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J16, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. This example uses the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt685_evk_cm33 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0 *****
Hello World! mimxrt685_evk_cm33
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. This example uses the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt685_evk_cm33 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.3.0 *****
Hello World! mimxrt685_evk_cm33
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the image in flash is interfering and causing this issue.

```shell
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

You can fix it by erasing and reprogramming the flash with the following
steps:

1. Set the SW5 DIP switches to ON-ON-ON to prevent booting from flash.
2. Reset by pressing SW3
3. Run `west debug` or `west flash` again with a known working Zephyr
   application (example “Hello World”).
4. Set the SW5 DIP switches to ON-OFF-ON to boot from flash.
5. Reset by pressing SW3
