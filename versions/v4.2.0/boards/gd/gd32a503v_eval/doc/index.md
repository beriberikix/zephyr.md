---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/gd/gd32a503v_eval/doc/index.html
original_path: boards/gd/gd32a503v_eval/doc/index.html
---

# GD32A503V-EVAL

Board Overview

[![../../../../_images/gd32a503v_eval.jpg](../../../../_images/gd32a503v_eval.jpg)
](../../../../_images/gd32a503v_eval.jpg)

GD32A503V-EVAL

Name:
:   `gd32a503v_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32a503

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32a503v_eval/doc/index.rst/../..)

## Overview

The GD32A503V-EVAL board is a hardware platform that enables design and debug
of the GigaDevice A503 Cortex-M4F High Performance MCU.

The GD32A503VD features a single-core ARM Cortex-M4F MCU which can run up
to 120-MHz with flash accesses zero wait states, 384kiB of Flash, 48kiB of
SRAM and 88 GPIOs.

## Hardware

- 2 user LEDs
- 2 user push buttons
- Reset Button
- ADC connected to a potentiometer
- 1 DAC channels
- GD25Q16 2Mib SPI Flash
- AT24C02C 2KiB EEPROM
- CS4344 Stereo DAC with Headphone Amplifier
- GD-Link interface

  - CMSIS-DAP swd debug interface over USB HID.
- 2 CAN FD ports

For more information about the GD32A503 SoC and GD32A503V-EVAL board:

- [GigaDevice Cortex-M33 High Performance SoC Website](https://www.gigadevice.com.cn/product/mcu/arm-cortex-m33/gd32a503vdt3)
- [GD32A503 Datasheet](https://www.gd32mcu.com/download/down/document_id/401/path_type/1)
- [GD32A503 Reference Manual](https://www.gd32mcu.com/download/down/document_id/402/path_type/1)
- [GD32A503V Eval Schematics](https://www.gd32mcu.com/download/down/document_id/404/path_type/1)
- [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

### Supported Features

The `gd32a503v_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32a503v_eval/gd32a503` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L21) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | GigaDevice GD32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L159)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L170) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L45) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L283) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L101) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L393) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L58) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L222) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigaDevice GD32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L111) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L187) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32a503v_eval/gd32a503v_eval.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L40) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| Miscellaneous | on-chip | GigaDevice GD32 System Configuration Registers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L181) | [`gd,gd32-syscfg`](../../../../build/dts/api/bindings/misc/gd%2Cgd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L65) | [`gd,gd32-nv-flash-v2`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v2.md#std-dtcompatible-gd-gd32-nv-flash-v2) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32a503v_eval/gd32a503v_eval.dts?plain=1#L94) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | GD32 Pin Controller (AF Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L215) | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| PWM | on-chip | GigaDevice GD32 PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L294) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L51) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L74)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L83) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L137)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L148) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L200) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L206) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32A503V-EVAL board has 3 serial communication ports. The default port
is UART0 at PIN-72 and PIN-73.

## Programming and Debugging

The `gd32a503v_eval` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **gd32isp** | ✅ |  |  |  |  |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Before program your board make sure to configure boot setting and serial port.
The default serial port is USART0.

| Boot-0 | Boot-1 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | SRAM |
| 1-2 | 2-3 | Bootloader |
| 2-3 | Any | Flash |

### Using GD-Link

The GD32A503V-EVAL includes an onboard programmer/debugger (GD-Link) which
allow flash programming and debug over USB. There are also program and debug
headers J2 and J100 that can be used with any ARM compatible tools.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
3. To flash an image:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32a503v\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   west debug
   ```

### Using ROM bootloader

The GD32A503 MCU have a ROM bootloader which allow flash programming. User
should install [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1) software at some Linux path. The recommended
is `$HOME/.local/bin`.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   ```
2. Enable board bootloader:

   - Remove boot-0 jumper
   - press reset button
3. To flash an image:

   ```shell
   west flash -r gd32isp [--port=/dev/ttyUSB0]
   ```
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1

   Press reset button

   You should see “Hello World! gd32a503v\_eval” in your terminal.
