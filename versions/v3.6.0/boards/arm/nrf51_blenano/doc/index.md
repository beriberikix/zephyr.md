---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf51_blenano/doc/index.html
original_path: boards/arm/nrf51_blenano/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Redbear Labs Nano

## Overview

The Nano is a development board equipped with Nordic’s nRF51822 Bluetooth Low Energy SOC.
This board is available on [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id1).

## Hardware

nRF51 BLE Nano has two external oscillators. The frequency of the slow clock
is 32.768 kHz. The frequency of the main clock is 16 MHz.

### Supported Features

The nrf51\_blenano board configuration supports the following nRF51
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| RTC | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| FLASH | on-chip | flash |
| RADIO | on-chip | Bluetooth |

### Connections and IOs

BLE nano pinout

![BLE Nano](../../../../_images/nrf51_blenano.jpg)

DAPLink board

![DAPLink](../../../../_images/daplink.jpg)

The DAPLink USB board acts as a dongle. DAPLink debug probes appear on the host computer as a USB disk.
It also regulates 5V from USB to 3.3V via the onboard LDO to power Nano.

More information about Nano and DAPLink can be found at the [RedBear Github](https://github.com/redbear/nRF5x) [[2]](#id4).

## Programming and Debugging

Applications for the `nrf51_blenano` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

To flash an application, you’ll need to connect your BLE Nano with the
DAPLink board, then attach that to your computer via USB.

Warning

Be careful to mount the BLE Nano correctly! The side of the board
with the VIN and GND pins should face **towards** the USB connector.
The [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id1) page links to a tutorial video that shows how to
properly solder headers and assemble the DAPLink and BLE Nano boards.

Now build and flash applications as usual. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west flash
```

### Debugging

After mounting the BLE Nano on its DAPLink board as described above,
you can debug an application in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west debug
```

## References

[1]
([1](#id2),[2](#id3))

[https://redbear.cc/product/ble-nano-kit.html](https://redbear.cc/product/ble-nano-kit.html)

[[2](#id5)]

[https://github.com/redbear/nRF5x](https://github.com/redbear/nRF5x)
