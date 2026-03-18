---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/u-blox/ubx_bmd380eval/doc/index.html
original_path: boards/u-blox/ubx_bmd380eval/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# u-blox EVK-BMD-34/48: BMD-380-EVAL

## Overview

The BMD-380-EVAL hardware provides support for the
u-blox BMD-380 Bluetooth 5.0 module, based on The
Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU and
the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- USB
- WDT

![BMD-340-EVAL](../../../../_images/BMD-34-38-EVAL1.jpg)

BMD-340-EVAL (Credit: u-blox AG)

Note

The BMD-380-EVAL shares the same pin headers and assignments as the
BMD-340-EVAL with four exceptions. The BMD-340-EVAL is shown here.
See the pin tables below for the exceptions.

More information about the BMD-340-EVAL and the BMD-340 module
can be found at the [u-blox website](https://www.u-blox.com/docs/UBX-19039467) [[1]](#id2). All of the Nordic Semiconductor
examples for the nRF52840 DK (nrf52840dk\_nrf52840) may be used without
modification.

## Hardware

The BMD-380 on the BMD-380-EVAL contains an internal high-frequency
oscillator at 32MHz. There is also a low frequency (slow) oscillator
of 32.768kHz. The BMD-380 itself does not include the slow crystal;
however, the BMD-380-eval does.

Note

When targeting a custom design without a slow crystal, be sure
to modify code to utilize the internal RC oscillator for the
slow clock.

### Supported Features

The BMD-380-EVAL board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth, IEEE 802.15.4 |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See the [u-blox website](https://www.u-blox.com/docs/UBX-19039467) [[1]](#id2) for a complete list of BMD-380-EVAL
hardware features.

### Connections and IOs

#### LED

- LED1 (red) = P0.13
- LED2 (red) = P0.14
- LED3 (green) = P0.15
- LED4 (green) = P0.16
- D5 (red) = OB LED 1
- D6 (green) = OB LED 2

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.12
- BUTTON3 = SW3 = P0.24
- BUTTON4 = SW4 = P0.25
- BOOT = SW5 = boot/reset

#### External Connectors

![BMD-340-EVAL pin-out](../../../../_images/bmd-340-eval_pin_out1.jpg)

Note

The BMD-380-EVAL shares the same pin headers and assignments as the
BMD-340-EVAL with four exceptions. The BMD-340-EVAL is shown here.
See the pin tables below for the exceptions.

Note

The pin numbers noted below are referenced to
the pin 1 markings on the BMD-380-EVAL
for each header

J-Link Prog Connector (J2)

| PIN # | Signal Name |
| --- | --- |
| 1 | VDD |
| 2 | IMCU\_TMSS |
| 3 | GND |
| 4 | IMCU\_TCKS |
| 5 | V5V |
| 6 | IMCU\_TDOS |
| 7 | Cut off |
| 8 | IMCU\_TDIS |
| 9 | Cut off |
| 10 | IMCU\_RESET |

Debug OUT (J3)

| PIN # | Signal Name |
| --- | --- |
| 1 | EXT\_VTG |
| 2 | EXT\_SWDIO |
| 3 | GND |
| 4 | EXT\_SWDCLK |
| 5 | GND |
| 6 | EXT\_SWO |
| 7 | N/C |
| 8 | N/C |
| 9 | EXT\_GND\_DETECT |
| 10 | EXT\_RESET |

Debug IN (J26)

| PIN # | Signal Name |
| --- | --- |
| 1 | BMD-340\_VCC |
| 2 | BMD-340\_SWDIO |
| 3 | GND |
| 4 | BMD-340\_SWDCLK |
| 5 | GND |
| 6 | BMD-340\_SWO |
| 7 | N/C |
| 8 | N/C |
| 9 | GND |
| 10 | BMD-340\_RESET |

Auxiliary (J9)

| PIN # | Signal Name |
| --- | --- |
| 1 | P0.10 / NFC2 |
| 2 | P0.09 / NFC1 |
| 3 | P0.08 |
| 4 | P0.07 |
| 5 | P0.06 |
| 6 | P0.05 / AIN3 |
| 7 | P0.01 / XL2 |
| 8 | P0.00 / XL1 |

Auxiliary (J10)

| PIN # | Signal Name |
| --- | --- |
| 1 | P0.11 / TRACED[2] |
| 2 | P0.12 / TRACED[1] |
| 3 | P0.13 |
| 4 | P0.14 |
| 5 | P0.15 |
| 6 | P0.16 |
| 7 | P0.17 / QSPI\_CS |
| 8 | P0.18 / RESET |
| 9 | P0.19 / QSPI\_CLK |
| 10 | P0.20 / QSPI\_D0 |
| 11 | P0.21 / QSPI\_D1 |
| 12 | P0.22 / QSPI\_D2 |
| 13 | P0.23 / QSPI\_D3 |
| 14 | P0.24 |
| 15 | P0.25 |
| 16 | P1.00 / TRACED[0] |
| 17 | P1.09 / TRACED[3] |
| 18 | No connection |

Power (J5)

| PIN # | Signal Name | BMD-380 Functions |
| --- | --- | --- |
| 1 | VSHLD | N/A |
| 2 | VSHLD | N/A |
| 3 | RESET | P0.18 / RESET |
| 4 | VSHLD | N/A |
| 5 | V5V | N/A |
| 6 | GND | N/A |
| 7 | GND | N/A |
| 8 | N/C | N/A |

Analog in (J8)

| PIN # | Signal Name | BMD-380 Functions |
| --- | --- | --- |
| 1 | A0 | P0.03 / AIN1 |
| 2 | A1 | P0.04 / AIN2 |
| 3 | A2 | P0.28 / AIN4 |
| 4 | A3 | P0.29 / AIN5 |
| 5 | A4 | P0.30 / AIN6 |
| 6 | A5 | P0.31 / AIN7 |

Digital I/O (J7)

| PIN # | Signal Name | BMD-380 Functions |
| --- | --- | --- |
| 1 | D7 | P1.08 |
| 2 |  | No connection |
| 3 | D5 | P1.06 |
| 4 | D4 | No connection |
| 5 |  | No connection |
| 6 |  | No connection |
| 7 | D1 (TX) | P1.02 |
| 8 |  | No connection |

Digital I/O (J6)

| PIN # | Signal Name | BMD-380 Functions |
| --- | --- | --- |
| 1 | SCL | P0.27 |
| 2 | SDA | P0.26 |
| 3 | AREF | P0.02 / AIN0 |
| 4 | GND | N/A |
| 5 | D13 (SCK) | P1.15 |
| 6 | D12 (MISO) | P1.14 |
| 7 | D11 (MOSI) | P1.13 |
| 8 | D10 (SS) | P1.12 |
| 9 | D9 | P1.11 |
| 10 | D8 | P1.10 |

J11

| PIN # | Signal Name | BMD-380 Functions |
| --- | --- | --- |
| 1 | D12 (MISO) | P0.14 |
| 2 | V5V | N/A |
| 3 | D13 (SCK) | P0.15 |
| 4 | D11 (MOSI) | P0.13 |
| 5 | RESET | N/A |
| 6 | N/A | N/A |

## Programming and Debugging

Applications for the BMD-380-EVAL board configurations can
be built and flashed in the usual way
(see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, the standard debugging targets
are not currently available.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BMD-380-EVAL
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ubx_bmd380eval/nrf52840 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging
u-blox boards with a Segger J-LINK-OB IC.

## Testing the LEDs and buttons in the BMD-380-EVAL

There are 2 samples that allow you to test that the buttons
(switches) and LEDs on the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The button and LED definitions can be found in
[boards/u-blox/ubx\_bmd340eval/ubx\_bmd340eval\_nrf52840.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_bmd340eval/ubx_bmd340eval_nrf52840.dts).

## Using UART1

The following approach can be used when an application needs to use
more than one UART for connecting peripheral devices:

1. Add device tree overlay file to the main directory of your
   application:

   ```devicetree
   &pinctrl {
      uart1_default: uart1_default {
         group1 {
            psels = <NRF_PSEL(UART_TX, 0, 14)>,
                    <NRF_PSEL(UART_RX, 0, 16)>;
         };
      };
      /* required if CONFIG_PM_DEVICE=y */
      uart1_sleep: uart1_sleep {
         group1 {
            psels = <NRF_PSEL(UART_TX, 0, 14)>,
                    <NRF_PSEL(UART_RX, 0, 16)>;
            low-power-enable;
         };
      };
   };

   &uart1 {
     compatible = "nordic,nrf-uarte";
     current-speed = <115200>;
     status = "okay";
     pinctrl-0 = <&uart1_default>;
     pinctrl-1 = <&uart1_sleep>;
     pinctrl-names = "default", "sleep";
   };
   ```

   In the overlay file above, pin P0.16 is used for RX and P0.14 is
   used for TX
2. Use the UART1 as `DEVICE_DT_GET(DT_NODELABEL(uart1))`

### Overlay file naming

The file has to be named `<board>.overlay` and placed in the app
main directory to be picked up automatically by the device tree
compiler.

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the data sheet for the BMD-380 at the [u-blox website](https://www.u-blox.com/docs/UBX-19039467) [[1]](#id2), Section 2
‘Pin definition’. In the table 3 select the pins marked ‘GPIO’.
Note that pins marked as ‘Standard drive, low frequency I/O only
(<10 kH’ can only be used in under-10KHz applications.
They are not suitable for 115200 speed of UART.

## References

[1]
([1](#id3),[2](#id4),[3](#id5))

[https://www.u-blox.com/docs/UBX-19039467](https://www.u-blox.com/docs/UBX-19039467)
