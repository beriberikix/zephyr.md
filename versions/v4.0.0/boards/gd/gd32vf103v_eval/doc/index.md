---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gd/gd32vf103v_eval/doc/index.html
original_path: boards/gd/gd32vf103v_eval/doc/index.html
---

# GD32VF103V-EVAL

Board Overview

[![../../../../_images/gd32vf103v_eval.jpg](../../../../_images/gd32vf103v_eval.jpg)
](../../../../_images/gd32vf103v_eval.jpg)

GD32VF103V-EVAL

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   riscv

SoC:
:   gd32vf103

## Overview

The GD32V103V-EVAL board is a hardware platform that enables prototyping
on GD32VF103VB RISC-V MCU.

The GD32VF103VB features a single-core RISC-V 32-bit MCU which can run up
to 108 MHz with flash accesses zero wait states, 128 KiB of Flash, 32 KiB of
SRAM and 80 GPIOs.

## Hardware

- GD32VF103VBT6 MCU
- AT24C02C 2Kb EEPROM
- GD25Q16 16Mbit SPI and QSPI NOR Flash
- 4 x User LEDs
- 1 x Joystick (L/R/U/D/C)
- 2 x USART (RS-232 at J1/J2 connectors)
- 1 x POT connected to an ADC input
- USB FS connector
- Headphone interface
- 1 x CAN
- 3.2” RGB-LCD (320x240)
- GD-Link on board programmer
- J-Link/JTAG connector

For more information about the GD32VF103 SoC and GD32VF103V-EVAL board:

- [GigaDevice RISC-V Mainstream SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/risc-v/mainstream-line/)
- [GD32VF103 Datasheet](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103 User Manual](https://www.gd32mcu.com/data/documents/userManual/GD32VF103_User_Manual_Rev1.4.pdf)
- [GD32VF103V-EVAL Documents](https://github.com/riscv-mcu/GD32VF103_Demo_Suites/tree/master/GD32VF103V_EVAL_Demo_Suites/Docs)

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| Machine timer | [`CONFIG_RISCV_MACHINE_TIMER`](../../../../kconfig.md#CONFIG_RISCV_MACHINE_TIMER "CONFIG_RISCV_MACHINE_TIMER") | `riscv,machine-timer` |
| Nuclei ECLIC Interrupt Controller | [`CONFIG_NUCLEI_ECLIC`](../../../../kconfig.md#CONFIG_NUCLEI_ECLIC "CONFIG_NUCLEI_ECLIC") | [`nuclei,eclic`](../../../../build/dts/api/bindings/interrupt-controller/nuclei%2Ceclic.md#std-dtcompatible-nuclei-eclic) |
| PWM | [`CONFIG_PWM`](../../../../kconfig.md#CONFIG_PWM "CONFIG_PWM") | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| ADC | [`CONFIG_ADC`](../../../../kconfig.md#CONFIG_ADC "CONFIG_ADC") | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |

### Serial Port

The GD32VF103V-EVAL board has two serial communications port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

Before programming your board make sure to configure boot and serial jumpers
as follows:

- JP2/3: Select 2-3 for both (boot from user memory)
- JP5/6: Select 1-2 positions (labeled as `USART0`)

### Using GD-Link

The GD32VF103V-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a JTAG header
(JP1) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32vf103v_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. On Linux the
   terminal should be something like `/dev/ttyUSB0`. For example:

   ```shell
   minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
3. To flash an image:

   ```shell
   west build -b gd32vf103v_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32vf103v\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32vf103v_eval samples/hello_world
   west debug
   ```
