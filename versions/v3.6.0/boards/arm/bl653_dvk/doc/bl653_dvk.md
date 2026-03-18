---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/bl653_dvk/doc/bl653_dvk.html
original_path: boards/arm/bl653_dvk/doc/bl653_dvk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Laird Connectivity BL653 DVK

## Overview

The BL653 Development Kit (453-00039-K1, 453-00041-K1) hardware provides
support for the Laird Connectivity BL653 module powered by a Nordic Semiconductor nRF52833 ARM Cortex-M4F CPU.

This development kit has the following features:

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

![BL653 Development Kit](../../../../_images/bl653_dvk.jpg)

BL653 Development Kit Board

More information about the board can be found at the
[BL653 website](https://www.lairdconnect.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl653-series-bluetooth-51-802154-nfc-module) [[1]](#id2).

## Hardware

### Supported Features

The BL653 DVK board configuration supports the following
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
See [BL653 website](https://www.lairdconnect.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl653-series-bluetooth-51-802154-nfc-module) [[1]](#id2)
for a complete list of BL653 Development Kit board hardware features.

### Connections and IOs

#### LED

- LED1 (blue) = P0.13
- LED2 (blue) = P0.14
- LED3 (blue) = P0.15
- LED4 (blue) = P0.16

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.12
- BUTTON3 = SW9 = P0.24
- BUTTON4 = SW10 = P0.25
- RESET = SW3 = nReset/IF BOOT

## Programming and Debugging

Applications for the `bl653_dvk` board configuration can be built, flashed,
and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

NOTE: On the BL653 development board, the FTDI USB should be used to access the UART console.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BL653 development kit
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl653_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic based boards with a
Segger IC.

## Testing Bluetooth on the BL653 DVK

Many of the Bluetooth examples will work on the BL653 DVK.
Try them out:

- [Bluetooth: Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble-peripheral)
- [Bluetooth: Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth-eddystone-sample)
- [Bluetooth: iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth-ibeacon-sample)

## Testing the LEDs and buttons on the BL653 DVK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/arm/bl653\_dvk/bl653\_dvk.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/bl653_dvk/bl653_dvk.dts).

## Using UART1

The following approach can be used when an application needs to use
more than one UART for connecting peripheral devices:

1. Add devicetree overlay file to the main directory of your application:

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

See [Set devicetree overlays](../../../../build/dts/howtos.md#set-devicetree-overlays) for further details.

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the [nRF52833 Product Specification](https://infocenter.nordicsemi.com/pdf/nRF52833_OPS_v0.7.pdf) [[2]](#id5), chapter 7 ‘Hardware and Layout’.
In the table 7.1.1 ‘aQFN73 ball assignments’ select the pins marked
‘General purpose I/O’. Note that pins marked as ‘low frequency I/O only’ can only be used
in under-10KHz applications. They are not suitable for 115200 speed of UART.

## References

[1]
([1](#id3),[2](#id4))

[https://www.lairdconnect.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl653-series-bluetooth-51-802154-nfc-module](https://www.lairdconnect.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl653-series-bluetooth-51-802154-nfc-module)

[[2](#id6)]

[https://infocenter.nordicsemi.com/pdf/nRF52833\_OPS\_v0.7.pdf](https://infocenter.nordicsemi.com/pdf/nRF52833_OPS_v0.7.pdf)
