---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf54l15pdk_nrf54l15/doc/index.html
original_path: boards/arm/nrf54l15pdk_nrf54l15/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF54L15 PDK

## Overview

Note

All software for the nRF54L15 SoC is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The nRF54L15 Preview Development Kit hardware provides
support for the Nordic Semiconductor nRF54L15 Arm Cortex-M33 CPU and
the following devices:

- SAADC
- CLOCK
- RRAM
- GPIO
- TWIM
- MPU
- NVIC
- PWM
- GRTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT

![nRF54L15 PDK](../../../../_images/nrf54l15pdk_nrf54l15.webp)

nRF54L15 PDK (Credit: Nordic Semiconductor)

## Hardware

nRF54L15 PDK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The nrf54l15pdk\_nrf54l15 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| SAADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| RRAM | on-chip | flash |
| GPIO | on-chip | gpio |
| TWIM | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| GRTC | on-chip | counter |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.

## Programming and Debugging

Applications for the `nrf54l15pdk_nrf54l15_cpuapp` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello-world)
application.

Warning

When programming the device, you might get an error similar to the following message:

```text
ERROR: The operation attempted is unavailable due to readback protection in
ERROR: your device. Please use --recover to unlock the device.
```

This error occurs when readback protection is enabled.
To disable the readback protection, you must *recover* your device.

Enter the following command to recover the core:

```text
west flash --recover
```

The `--recover` command erases the flash memory and then writes a small binary into
the recovered flash memory.
This binary prevents the readback protection from enabling itself again after a pin
reset or power cycle.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

To build and program the sample to the nRF54L15 PDK, complete the following steps:

First, connect the nRF54L15 PDK to you computer using the IMCU USB port on the PDK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54l15pdk_nrf54l15_cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54L15 PDK

Test the nRF54L15 PDK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
