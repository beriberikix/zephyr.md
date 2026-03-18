---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/ubx_evkninab4_nrf52833/doc/index.html
original_path: boards/arm/ubx_evkninab4_nrf52833/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# u-blox EVK NINA-B40x

## Overview

The u-blox NINA-B4 Evaluation Kit hardware is a Bluetooth low energy
module based on the Nordic Semiconductor nRF52833 ARM Cortex-M4F CPU
and has support for the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- USB
- WDT

![../../../../_images/EVK-NINA-B406_Top_web.jpg](../../../../_images/EVK-NINA-B406_Top_web.jpg)

EVK NINA-B4

More information about the NINA-B4 module and the EVK-NINA-B4 can be
found at [NINA-B40 product page](https://www.u-blox.com/en/product/nina-b40-series-open-cpu) [[1]](#id2) and [EVK-NINA-B4 product page](https://www.u-blox.com/en/product/evk-nina-b4) [[2]](#id4).

### Supported Features

The ubx\_evkninab4\_nrf52833 board configuration supports the following
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
| RADIO | on-chip | Bluetooth low energy |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [EVK-NINA-B4 product page](https://www.u-blox.com/en/product/evk-nina-b4) [[2]](#id4) and [NINA-B40 Data Sheet](https://www.u-blox.com/en/docs/UBX-19049405) [[3]](#id7)
for a complete list of EVK NINA-B4 hardware features.

### Connections and IOs

#### LED

- LED0 (red) = P0.13
- LED1 (green) = P1.01
- LED2 (blue) = P1.00

#### Push buttons

- BUTTON1 = SW1 = P1.01 (Shared with green LED)
- BUTTON2 = SW2 = P0.02

#### General information on module pin numbering

The numbering of the pins on the module and EVK do not follow the GPIO
numbering on the nRF52833 SoC. Please see the [NINA-B40 Data Sheet](https://www.u-blox.com/en/docs/UBX-19049405) [[3]](#id7) for
information on how to map NINA-B40 pins to the pin numbering on the
nRF52833 SoC.

The reason for this is the u-blox module family concept where different
modules share the same pinout and can be interchanged, see
[NINA module family Nested design](https://www.u-blox.com/en/docs/UBX-17065600) [[4]](#id11).

## Programming and Debugging

Applications for the `ubx_evkninab4_nrf52833` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); however, the standard
debugging targets are not currently available.

### Flashing

Build and flash applications as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details)

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Open a terminal program to the USB Serial Port installed when connecting
the board and listen for output.

Settings: 115200, 8N1, no flow control.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ubx_evknina4_nrf52833 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging boards
containing a Nordic Semiconductor chip with a Segger IC.

## Testing the LEDs and buttons in the EVK NINA-B40x

There are 2 samples that allow you to test that the buttons (switches)
and LEDs on the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The button and LED definitions can be found in
[boards/arm/ubx\_evkninab4\_nrf52833/ubx\_evkninab4\_nrf52833.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/ubx_evkninab4_nrf52833/ubx_evkninab4_nrf52833.dts).

Note that the buttons on the EVK-NINA-B4 are marked SW1 and SW2, which
are named sw0 and sw1 in the dts file.
Also note that the SW1 button and the green LED are connected on HW level.

## Using UART1

The following approach can be used when an application needs to use
more than one UART for connecting peripheral devices:

1. Add device tree overlay file to the main directory of your application:

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

   In the overlay file above, pin P0.16 is used for RX and P0.14 is used for TX
2. Use the UART1 as `DEVICE_DT_GET(DT_NODELABEL(uart1))`

### Overlay file naming

The file has to be named `<board>.overlay` and placed in the app main directory to be
picked up automatically by the device tree compiler.

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the data sheet for the NINA-B4 at [NINA-B40 Data Sheet](https://www.u-blox.com/en/docs/UBX-19049405) [[3]](#id7), Section 3 ‘Pin definition’.
In the table 7 select the pins marked ‘GPIO\_xx’. Note that pins marked as ‘Radio sensitive pin’
can only be used in under-10KHz applications. They are not suitable for 115200 speed of UART.

## References

[[1](#id3)]

[https://www.u-blox.com/en/product/nina-b40-series-open-cpu](https://www.u-blox.com/en/product/nina-b40-series-open-cpu)

[2]
([1](#id5),[2](#id6))

[https://www.u-blox.com/en/product/evk-nina-b4](https://www.u-blox.com/en/product/evk-nina-b4)

[3]
([1](#id8),[2](#id9),[3](#id10))

[https://www.u-blox.com/en/docs/UBX-19049405](https://www.u-blox.com/en/docs/UBX-19049405)

[[4](#id12)]

[https://www.u-blox.com/en/docs/UBX-17065600](https://www.u-blox.com/en/docs/UBX-17065600)
