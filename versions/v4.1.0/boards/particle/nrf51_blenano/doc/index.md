---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/particle/nrf51_blenano/doc/index.html
original_path: boards/particle/nrf51_blenano/doc/index.html
---

# Redbear Labs Nano

Board Overview

[![../../../../_images/nrf51_blenano.jpg](../../../../_images/nrf51_blenano.jpg)
](../../../../_images/nrf51_blenano.jpg)

Redbear Labs Nano

Name:
:   `nrf51_blenano`

Vendor:
:   Particle.io

Architecture:
:   arm

SoC:
:   nrf51822

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/particle/nrf51_blenano/doc/index.rst/../..)

## Overview

The Nano is a development board equipped with Nordic’s nRF51822 Bluetooth Low Energy SOC.
This board is available on [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id2).

## Hardware

nRF51 BLE Nano has two external oscillators. The frequency of the slow clock
is 32.768 kHz. The frequency of the main clock is 16 MHz.

### Supported Features

The `nrf51_blenano` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

BLE nano pinout

![BLE Nano](../../../../_images/nrf51_blenano1.jpg)

DAPLink board

![DAPLink](../../../../_images/daplink.jpg)

The DAPLink USB board acts as a dongle. DAPLink debug probes appear on the host computer as a USB disk.
It also regulates 5V from USB to 3.3V via the onboard LDO to power Nano.

More information about Nano and DAPLink can be found at the [RedBear Github](https://github.com/redbear/nRF5x) [[2]](#id5).

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
The [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id2) page links to a tutorial video that shows how to
properly solder headers and assemble the DAPLink and BLE Nano boards.

Now build and flash applications as usual. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west flash
```

### Debugging

After mounting the BLE Nano on its DAPLink board as described above,
you can debug an application in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west debug
```

## References

[1]
([1](#id3),[2](#id4))

[https://redbear.cc/product/ble-nano-kit.html](https://redbear.cc/product/ble-nano-kit.html)

[[2](#id6)]

[https://github.com/redbear/nRF5x](https://github.com/redbear/nRF5x)
