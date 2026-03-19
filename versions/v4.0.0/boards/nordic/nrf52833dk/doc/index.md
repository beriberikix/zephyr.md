---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nordic/nrf52833dk/doc/index.html
original_path: boards/nordic/nrf52833dk/doc/index.html
---

# nRF52833 DK

## Overview

The nRF52833 Development Kit (PCA10100) hardware provides
support for the Nordic Semiconductor nRF52833 ARM Cortex-M4F CPU and
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

More information about the board can be found at the
[nRF52833 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK) [[5]](#id13) [[1]](#id3). [nRF52833 Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf52833/page/keyfeatures_html5.html) [[6]](#id16) [[2]](#id6)
contains the processor’s information and the datasheet.

## Hardware

nRF52833 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf52833dk/nrf52833` board configuration supports the following
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
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [nRF52833 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK) [[5]](#id13) [[1]](#id3) and [nRF52833 DK Hardware guide](https://docs.nordicsemi.com/bundle/ug_nrf52833_dk/page/UG/dk/intro.html) [[7]](#id19) [[3]](#id9)
for a complete list of nRF52833 Development Kit board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.13
- LED2 (green) = P0.14
- LED3 (green) = P0.15
- LED4 (green) = P0.16

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.12
- BUTTON3 = SW3 = P0.24
- BUTTON4 = SW4 = P0.25
- BOOT = SW5 = boot/reset

## Programming and Debugging

Applications for the `nrf52833dk/nrf52833` board configuration can be built,
flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF52 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf52833dk/nrf52833 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons in the nRF52833 DK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/nordic/nrf52833dk/nrf52833dk\_nrf52833.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf52833dk/nrf52833dk_nrf52833.dts).

## Changing UART1 pins

The following approach can be used when an application needs to use another set
of pins for UART1:

1. Add devicetree overlay file to the main directory of your application:

   ```devicetree
   &pinctrl {
      uart1_default_alt: uart1_default_alt {
         group1 {
            psels = <NRF_PSEL(UART_TX, 0, 14)>,
                    <NRF_PSEL(UART_RX, 0, 16)>;
         };
      };
      /* required if CONFIG_PM_DEVICE=y */
      uart1_sleep_alt: uart1_sleep_alt {
         group1 {
            psels = <NRF_PSEL(UART_TX, 0, 14)>,
                    <NRF_PSEL(UART_RX, 0, 16)>;
            low-power-enable;
         };
      };
   };

   &uart1 {
     pinctrl-0 = <&uart1_default_alt>;
     /* if sleep state is not used, use /delete-property/ pinctrl-1; and
      * skip the "sleep" entry.
      */
     pinctrl-1 = <&uart1_sleep_alt>;
     pinctrl-names = "default", "sleep";
   };
   ```

   In the overlay file above, pin P0.16 is used for RX and P0.14 is used for TX

See [Set devicetree overlays](../../../../build/dts/howtos.md#set-devicetree-overlays) for further details.

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the [nRF52833 Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf52833/page/keyfeatures_html5.html) [[6]](#id16) [[2]](#id6), chapter 7 ‘Hardware and Layout’.
In the table 7.1.1 ‘aQFN73 ball assignments’ select the pins marked
‘General purpose I/O’. Note that pins marked as ‘low frequency I/O only’ can only be used
in under-10KHz applications. They are not suitable for 115200 speed of UART.

## References

[1]
([1](#id4),[2](#id5))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK)

[2]
([1](#id7),[2](#id8))

[https://docs.nordicsemi.com/bundle/ps\_nrf52833/page/keyfeatures\_html5.html](https://docs.nordicsemi.com/bundle/ps_nrf52833/page/keyfeatures_html5.html)

[[3](#id10)]

[https://docs.nordicsemi.com/bundle/ug\_nrf52833\_dk/page/UG/dk/intro.html](https://docs.nordicsemi.com/bundle/ug_nrf52833_dk/page/UG/dk/intro.html)

[[4](#id12)]

[https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52820](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52820)

# nRF52820 emulation on nRF52833 DK

## Overview

The `nrf52833dk/nrf52820` board is a modified version of the
[nRF52833 DK](#nrf52833dk-nrf52833) that enforces the limitations imposed by the nRF52820
IC, which is a variant of the original nRF52833. Since Nordic does not offer a
development kit for the nRF52820 you can use this board to develop for this IC
while using the nRF52833 Development Kit (PCA10100).

See [nRF52833 DK](#nrf52833dk-nrf52833) for more information about the development board
and [nRF52820 website](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52820) [[8]](#id21) [[4]](#id11) for the official reference on the IC itself.

## References

[5]
([1](#id14),[2](#id15))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52833-DK)

[6]
([1](#id17),[2](#id18))

[https://docs.nordicsemi.com/bundle/ps\_nrf52833/page/keyfeatures\_html5.html](https://docs.nordicsemi.com/bundle/ps_nrf52833/page/keyfeatures_html5.html)

[[7](#id20)]

[https://docs.nordicsemi.com/bundle/ug\_nrf52833\_dk/page/UG/dk/intro.html](https://docs.nordicsemi.com/bundle/ug_nrf52833_dk/page/UG/dk/intro.html)

[[8](#id22)]

[https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52820](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52820)
