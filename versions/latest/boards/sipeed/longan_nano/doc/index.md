---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/sipeed/longan_nano/doc/index.html
original_path: boards/sipeed/longan_nano/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sipeed Longan Nano

![longan_nano](../../../../_images/longan_nano.jpg)

## Overview

The Sipeed Longan Nano and Longan Nano Lite is an simple and tiny development board with
an GigaDevice GD32VF103 SoC that based on N200 RISC-V IP core by Nuclei system technology.
More information can be found on:

- [Sipeed Longan website](https://longan.sipeed.com/en/)
- [GD32VF103 datasheet](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103 user manual](https://www.gd32mcu.com/data/documents/userManual/GD32VF103_User_Manual_Rev1.4.pdf)
- [Nuclei website](https://www.nucleisys.com/download.php)
- [Nuclei Bumblebee core documents](https://github.com/nucleisys/Bumblebee_Core_Doc)
- [Nuclei ISA Spec](https://doc.nucleisys.com/nuclei_spec/)

## Hardware

- 4 x universal 16-bit timer
- 2 x basic 16-bit timer
- 1 x advanced 16-bit timer
- Watchdog timer
- RTC
- Systick
- 3 x USART
- 2 x I2C
- 3 x SPI
- 2 x I2S
- 2 x CAN
- 1 x USBFS(OTG)
- 2 x ADC(10 channel)
- 2 x DAC

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| Machine timer | [`CONFIG_RISCV_MACHINE_TIMER`](../../../../kconfig.md#CONFIG_RISCV_MACHINE_TIMER "CONFIG_RISCV_MACHINE_TIMER") | `riscv,machine-timer` |
| Nuclei ECLIC Interrupt Controller | [`CONFIG_NUCLEI_ECLIC`](../../../../kconfig.md#CONFIG_NUCLEI_ECLIC "CONFIG_NUCLEI_ECLIC") | [`nuclei,eclic`](../../../../build/dts/api/bindings/interrupt-controller/nuclei%2Ceclic.md#std-dtcompatible-nuclei-eclic) |
| PWM | [`CONFIG_PWM`](../../../../kconfig.md#CONFIG_PWM "CONFIG_PWM") | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| I2C | [`CONFIG_I2C`](../../../../kconfig.md#CONFIG_I2C "CONFIG_I2C") | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| DAC | [`CONFIG_DAC`](../../../../kconfig.md#CONFIG_DAC "CONFIG_DAC") | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| ADC | [`CONFIG_ADC`](../../../../kconfig.md#CONFIG_ADC "CONFIG_ADC") | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| SPI | [`CONFIG_SPI`](../../../../kconfig.md#CONFIG_SPI "CONFIG_SPI") | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |

The microSD card reader in Longan Nano board is connected to SPI1.

### Serial Port

USART0 is on the opposite end of the USB.
Connect to TX0 (PA9) and RX0 (PA10).

## Programming and debugging

### Building & Flashing

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west flash
```

When using a custom toolchain it should be enough to have the downloaded
version of the binary in your `PATH`.

The default runner tries to flash the board via an external programmer using openocd.
To flash via the USB port, select the DFU runner when flashing:

```shell
west flash --runner dfu-util
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west debug
```
