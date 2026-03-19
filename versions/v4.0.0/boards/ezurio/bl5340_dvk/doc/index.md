---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ezurio/bl5340_dvk/doc/index.html
original_path: boards/ezurio/bl5340_dvk/doc/index.html
---

# BL5340 DVK

Board Overview

[![../../../../_images/bl5340_dvk_top.jpg](../../../../_images/bl5340_dvk_top.jpg)
](../../../../_images/bl5340_dvk_top.jpg)

BL5340 DVK

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf5340

## Overview

The BL5340 Development Kit provides support for the Ezurio
BL5340 module which is powered by a dual-core Nordic Semiconductor
nRF5340 ARM Cortex-M33F CPU. The nRF5340 inside the BL5340 module is a
dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running
  at a fixed 64 MHz, referred to as the **network core**.

The `bl5340_dvk/nrf5340/cpuapp` build target provides support for the application
core on the BL5340 module. The `bl5340_dvk/nrf5340/cpunet` build target provides
support for the network core on the BL5340 module. If ARM TrustZone is
used then the `bl5340_dvk/nrf5340/cpuapp` build target provides support for the
non-secure partition of the application core on the BL5340 module.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- IDAU
- I2C
- I2S
- MPU
- NVIC
- PWM
- QSPI
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- USB
- WDT

More information about the module can be found on the
[BL5340 homepage](https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules) [[2]](#id5).

The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
contains the processor’s information and the datasheet.

## Hardware

The BL5340 DVK has two external oscillators. The frequency of
the slow clock is 32.768KHz. The frequency of the main clock
is 32MHz.

### Supported Features

The `bl5340_dvk/nrf5340/cpuapp` board configuration supports the following
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
| QSPI(M) | on-chip | nor |
| PWM | on-chip | pwm |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

The `bl5340_dvk/nrf5340/cpunet` board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UARTE | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
for a complete list of hardware features.

### Connections and IOs

An eight-pin GPIO port expander is used to provide additional inputs
and outputs to the BL5340 module.

Refer to the [TI TCA9538 datasheet](https://www.ti.com/lit/gpn/TCA9538) [[4]](#id10) for further details.

#### LEDs

- LED1 (blue) = via TCA9538 port expander channel P4 (active low)
- LED2 (blue) = via TCA9538 port expander channel P5 (active low)
- LED3 (blue) = via TCA9538 port expander channel P6 (active low)
- LED4 (blue) = via TCA9538 port expander channel P7 (active low)

#### Push buttons

- BUTTON1 = SW1 = via TCA9538 port expander channel P0 (active low)
- BUTTON2 = SW2 = via TCA9538 port expander channel P1 (active low)
- BUTTON3 = SW3 = via TCA9538 port expander channel P2 (active low)
- BUTTON4 = SW4 = via TCA9538 port expander channel P3 (active low)
- BOOT = boot (active low)

### External Memory

Several external memory sources are available for the BL5340 DVK. These
are described as follows.

#### Flash Memory

A Macronix MX25R6435FZNIL0 8MB external QSPI Flash memory part is
incorporated for application image storage and large datasets.

Refer to the [Macronix MX25R6435FZNIL0 datasheet](https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf) [[5]](#id12) for further details.

#### EEPROM Memory

A 32KB Giantec GT24C256C-2GLI-TR EEPROM is available via I2C for
storage of infrequently updated data and small datasets.

Refer to the [Giantec GT24C256C-2GLI-TR datasheet](https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C_DS_Cu.pdf) [[6]](#id14) for further details.

#### External Memory

An on-board micro SD card slot is available for use with micro SD cards.

### Sensors

The BL5340 DVK incorporates two sensors for user application testing.
These are described as follows.

#### Temperature, Pressure, Humidity & Air Quality Sensor

A Bosch BME680 Temperature, Pressure, Humidity & Air Quality sensor is
available via I2C for environmental measurement applications.

Refer to the [Bosch BME680 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf) [[7]](#id16) for further details.

#### 3-Axis Accelerometer

An ST Microelectronics LIS3DH 3-Axis Accelerometer is available via I2C
for vibration and motion detection applications.

Refer to the [ST Microelectronics LIS3DH datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf) [[8]](#id18) for further details.

### Ethernet

Cabled 10/100 Base-T Ethernet Connectivity is available via a Microchip
ENC424J600 Ethernet controller.

Refer to the [Microchip ENC424J600 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf) [[9]](#id20) for further details.

### TFT Display & Capacitive Touch Screen Controller

A 2.8 inch, 240 x 320 pixel TFT display with capacitive touch
controller is included with the BL5340 DVK for user interface
application features.

Refer to the [ER\_TFTM028\_4 datasheet](https://www.buydisplay.com/download/manual/ER-TFTM028-4_Datasheet.pdf) [[10]](#id22) for a high level overview of the
display.

An ILI9341 TFT controller is incorporated in the TFT module and
acts as the main controller, controlled via SPI.

Refer to the [ILI9341 datasheet](https://www.buydisplay.com/download/ic/ILI9341.pdf) [[11]](#id24) for further details.

An FT6206 Capacitive Touch Controller, controlled via I2C is
also incorporated in the TFT module.

Refer to the [FT6206 datasheet](https://www.buydisplay.com/download/ic/FT6206.pdf) [[12]](#id26) for further details.

### Real-Time Clock

A real-time clock is available for accurate time data availability.

Refer to the [Microchip MCP7940N datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf) [[13]](#id28) for further details.

### DAC

A 10-bit Digital to Analog Converter is incorporated for generation of
variable voltages.

Refer to the [Microchip MCP4725 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf) [[14]](#id30) for further details.

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id3)) on the application
  core. The IDAU is implemented with the System Protection Unit and is
  used to define secure and non-secure memory maps. By default, all of
  the memory space (Flash, SRAM, and peripheral address space) is
  defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

The BL5340’s application core supports the Armv8-M Security Extension.
Applications built for the `bl5340_dvk/nrf5340/cpuapp` board by default
boot in the Secure state.

The BL5340’s network core does not support the Armv8-M Security
Extension. The IDAU may configure bus accesses by the network core to
have Secure attribute set; the latter allows to build and run Secure
only applications on the BL5340 module.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the BL5340 module may contain a Secure and a Non-Secure
firmware image for the application core. The Secure image can be built
using either Zephyr or [Trusted Firmware M](https://www.trustedfirmware.org/projects/tf-m/) [[15]](#id32) (TF-M). Non-Secure
firmware images are always built using Zephyr. The two alternatives are
described below.

Note

By default the Secure image for BL5340’s application core is
built using TF-M.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the
Non-Secure firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for the application core using `-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

   > - Build the Non-Secure firmware image as a regular Zephyr application
   > - Build a TF-M (secure) firmware image
   > - Merge the output image binaries together
   > - Optionally build a bootloader image (MCUboot)

Note

Depending on the TF-M configuration, an application DTS overlay may
be required, to adjust the Non-Secure image Flash and SRAM starting
address and sizes.

2. Build the application firmware for the network core using
   `-DBOARD=bl5340_dvk/nrf5340/cpunet`.

#### Building the Secure firmware using Zephyr

The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for the application core
   using `-DBOARD=bl5340_dvk/nrf5340/cpuapp` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for the application core
   using `-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`.
3. Merge the two binaries together.
4. Build the application firmware for the network core using
   `-DBOARD=bl5340_dvk/nrf5340/cpunet`.

When building a Secure/Non-Secure application for the BL5340’s
application core, the Secure application will have to set the IDAU
(SPU) configuration to allow Non-Secure access to all CPU resources
utilized by the Non-Secure application firmware. SPU configuration
shall take place before jumping to the Non-Secure application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=bl5340_dvk/nrf5340/cpuapp` for
the firmware running on the BL5340’s application core, and using
`-DBOARD=bl5340_dvk/nrf5340/cpunet` for the firmware running
on the BL5340’s network core.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then you can build and flash
applications as usual ([Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Warning

The BL5340 has a flash read-back protection feature. When flash
read-back protection is active, you will need to recover the chip
before reflashing. If you are flashing with
[west](../../../../develop/west/build-flash-debug.md#west-build-flash-debug), run this command for more
details on the related `--recover` option:

```shell
west flash -H -r nrfjprog --skip-rebuild
```

Note

Flashing and debugging applications on the BL5340 DVK requires
upgrading the nRF Command Line Tools to version 10.12.0 or newer.
Further information on how to install the nRF Command Line Tools can
be found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application running on the
BL5340’s application core.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BL5340 DVK board
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpuapp samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging
boards with a Segger IC.

## Testing Bluetooth on the BL5340 DVK

Many of the Bluetooth examples will work on the BL5340 DVK.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

## References

[[1](#id4)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[[2](#id6)]

[https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules](https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules)

[3]
([1](#id8),[2](#id9))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[4](#id11)]

[https://www.ti.com/lit/gpn/TCA9538](https://www.ti.com/lit/gpn/TCA9538)

[[5](#id13)]

[https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf](https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf)

[[6](#id15)]

[https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C\_DS\_Cu.pdf](https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C_DS_Cu.pdf)

[[7](#id17)]

[https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf)

[[8](#id19)]

[https://www.st.com/resource/en/datasheet/lis3dh.pdf](https://www.st.com/resource/en/datasheet/lis3dh.pdf)

[[9](#id21)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf)

[[10](#id23)]

[https://www.buydisplay.com/download/manual/ER-TFTM028-4\_Datasheet.pdf](https://www.buydisplay.com/download/manual/ER-TFTM028-4_Datasheet.pdf)

[[11](#id25)]

[https://www.buydisplay.com/download/ic/ILI9341.pdf](https://www.buydisplay.com/download/ic/ILI9341.pdf)

[[12](#id27)]

[https://www.buydisplay.com/download/ic/FT6206.pdf](https://www.buydisplay.com/download/ic/FT6206.pdf)

[[13](#id29)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf)

[[14](#id31)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf)

[[15](#id33)]

[https://www.trustedfirmware.org/projects/tf-m/](https://www.trustedfirmware.org/projects/tf-m/)
