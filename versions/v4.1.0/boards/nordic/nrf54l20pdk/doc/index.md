---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nordic/nrf54l20pdk/doc/index.html
original_path: boards/nordic/nrf54l20pdk/doc/index.html
---

# nRF54L20 PDK

## Overview

Note

All software for the nRF54L20 SoC is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The nRF54L20 Preview Development Kit hardware provides
support for the Nordic Semiconductor nRF54L20 Arm Cortex-M33 CPU and
the following devices:

- CLOCK
- RRAM
- GPIO
- GRTC
- NVIC
- UARTE

## Hardware

nRF54L20 PDK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The `nrf54l20pdk/nrf54l20/cpuapp` board target configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CLOCK | on-chip | clock\_control |
| RRAM | on-chip | flash |
| GPIO | on-chip | gpio |
| GRTC | on-chip | system clock |
| NVIC | on-chip | arch/arm |
| UARTE | on-chip | serial |

Other hardware features have not been enabled yet for this board.

## Programming and Debugging

Applications for the `nrf54l20pdk/nrf54l20/cpuapp` board target can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

To build and program the sample to the nRF54L20 PDK, complete the following steps:

First, connect the nRF54L20 PDK to you computer using the IMCU USB port on the PDK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54l20pdk/nrf54l20/cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54L20 PDK

Test the nRF54L20 PDK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
