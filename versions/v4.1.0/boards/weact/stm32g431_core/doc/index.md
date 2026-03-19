---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/weact/stm32g431_core/doc/index.html
original_path: boards/weact/stm32g431_core/doc/index.html
---

# STM32G431 Core Board

Board Overview

Name:
:   `weact_stm32g431_core`

Vendor:
:   WeAct Studio

Architecture:
:   arm

SoC:
:   stm32g431xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/weact/stm32g431_core/doc/index.rst/../..)

The WeAct STM32G431 Core Board is a low-cost bare-bones STM32G431-based development
board. See the [STM32G431CB website](https://www.st.com/en/microcontrollers-microprocessors/stm32g431cb.html) [[2]](#id3) for more information about the MCU. More information
about the board, including schematics, is available from the [WeAct GitHub](https://github.com/WeActStudio/WeActStudio.STM32G431CoreBoard) [[1]](#id1).

## Modifications USB-C Power Delivery

The board does not support USB-C PD in its standard configuration. To enable USB-C PD, CC1
and CC2 need to be disconnected from their pull-down resistors and be connected to PB6 and
PB4 respectively. Dead battery support requires PA9 and PA10 to be routed to CC1 and
CC2. VBUS also needs to be connected to the MCU through a voltage divider.

The pull-downs are disconnected by removing the zero-Ohm resistors on SB8 and SB9 next to
the USB-C connector. SB3, SB5, SB6, and SB7 then need to be closed to connect the CCx
lines to the MCU. The voltage divider is connected to PB2 by closing SB4.

After these modifications have been made, PA9, PA10, PB2, PB4, and PB6 should be
considered reserved for USB-C and not available for other applications.

Warning

The internal USB DFU boot loader may not work correctly with machines that respect USB
PD signaling unless dead battery support has been enabled. A USB-C to USB-A adapter or
programming using the SWD port can be used as a workaround.

### Supported Features

The `weact_stm32g431_core` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA3
- UCPD1 CCx : PB6/PB4 (not connected by default)
- UCPD1 DBCCx : PA9/PA10 (not connected by default)
- BUTTON (User) : PC13
- BUTTON (BOOT0) : PB8
- LED0 : PC6
- ADC (VBUS) : PB2

The ADC is disabled by default since the VBUS voltage divider is not connected in the
board’s standard configuration.

#### Hardware Configuration

| Solder bridge | Default | Description |
| --- | --- | --- |
| SB1/SB2 | Open | Route PC14/PC15 (LSE) to header |
| SB6/SB7 | Open | Connect PB4/PB6 (UCPD1\_CCx) to USB-C CCx pins |
| SB3/SB5 | Open | Connect PA9/PA10 (UCPD1\_DBCCx) to PB6/PB4 |
| SB4 | Open | Connect PB2 to VBUS voltage divider |
| SB8/SB9 | Closed | Connect USB-CCx to pull-down resistors |
| SB10 | Open | VBUS protection diode bypass |

#### Clock Sources

The board has two external oscillators. The frequency of the slow clock (LSE) is 32.768
kHz. The frequency of the main clock (HSE) is 8 MHz.

The default configuration sources the system clock from the PLL, which is derived from
HSE, and is set at 144 MHz. The 48 MHz clock used by the USB interface is derived from the
PLL instead of the internal 48 MHz oscillator.

## Programming and Debugging

The MCU is normally programmed using the ROM bootloader or the exposed SWD port.

Please note that some laptops may not detect the ROM bootloader correctly if the CCx
pull-downs have been disconnected by opening SB8 and SB9 unless dead battery support has
been enabled by closing SB3 and SB5. A USB-C to USB-A adapter can be used as a workaround
if this is a problem.

### Flashing an Application

Connect a USB-C cable and the board should power ON. Force the board into DFU mode by
keeping the BOOT0 switch pressed while pressing and releasing the NRST switch.

The dfu-util runner is supported on this board and so a sample can be built and tested
easily.

```shell
# From the root of the zephyr repository
west build -b weact_stm32g431_core samples/basic/blinky
west flash
```

### Debugging

The board can be debugged by installing the included 100 mil (0.1 inch) header, and
attaching an SWD debugger to the 3V3 (3.3V), GND, SCK, and DIO pins on that header.

## References

[[1](#id2)]

[https://github.com/WeActStudio/WeActStudio.STM32G431CoreBoard](https://github.com/WeActStudio/WeActStudio.STM32G431CoreBoard)

[[2](#id4)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g431cb.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g431cb.html)
