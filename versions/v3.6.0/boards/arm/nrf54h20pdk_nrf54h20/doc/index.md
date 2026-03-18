---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf54h20pdk_nrf54h20/doc/index.html
original_path: boards/arm/nrf54h20pdk_nrf54h20/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF54H20 PDK

## Overview

Note

All software for the nRF54H20 SoC is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The nRF54H20 PDK is a single-board preview development kit for evaluation
and development on the Nordic nRF54H20 System-on-Chip (SoC).

The nRF54H20 is a multicore SoC with:

- an Arm Cortex-M33 core with DSP instructions, FPU, and Armv8-M Security
  Extensions, running at up to 320 MHz, referred to as the **application core**
- an Arm Cortex-M33 core with DSP instructions, FPU, and Armv8-M Security
  Extensions, running at up to 256 MHz, referred to as the **radio core**.

The `nrf54h20pdk_nrf54h20_cpuapp` build target provides support for
the application core on the nRF54H20 SoC.
The `nrf54h20pdk_nrf54h20_cpurad` build target provides support for
the radio core on the nRF54H20 SoC.

nRF54H20 SoC provides support for the following devices:

- ADC
- CLOCK
- GPIO
- GPIOTE
- GRTC
- I2C
- MRAM
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- SPI
- UART
- USB
- WDT

![nRF54H20 PDK](../../../../_images/nrf54h20pdk_nrf54h20.webp)

nRF54H20 PDK (Credit: Nordic Semiconductor)

## Hardware

nRF54H20 PDK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

### Supported Features

The nrf54h20pdk\_nrf54h20\_cpuapp board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GPIO | on-chip | gpio |
| GPIOTE | on-chip | gpio |
| GRTC | on-chip | system clock |
| UART | on-chip | serial |

The nrf54h20pdk\_nrf54h20\_cpurad board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GPIO | on-chip | gpio |
| GPIOTE | on-chip | gpio |
| GRTC | on-chip | system clock |
| UARTE | on-chip | serial |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

#### LEDs

- LED1 (green) = P9.0
- LED2 (green) = P9.1
- LED3 (green) = P9.2
- LED4 (green) = P9.3

#### Push buttons

- BUTTON1 = P0.8
- BUTTON2 = P0.9
- BUTTON3 = P0.10
- BUTTON4 = P0.11
- RESET (SW1)

## Programming and Debugging

Applications for both the `nrf54h20pdk_nrf54h20_cpuapp` and
`nrf54h20pdk_nrf54h20_cpurad` targets can be built, flashed,
and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello-world)
application.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

To build and program the sample to the nRF54H20 PDK, complete the following steps:

First, connect the nRF54H20 PDK to you computer using the IMCU USB port on the PDK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54h20pdk_nrf54h20_cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54H20 PDK

There are 2 samples that allow you to test that the buttons (switches) and LEDs
on the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/arm/nrf54h20pdk\_nrf54h20/nrf54h20pdk\_nrf54h20\_cpuapp.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/nrf54h20pdk_nrf54h20/nrf54h20pdk_nrf54h20_cpuapp.dts).
