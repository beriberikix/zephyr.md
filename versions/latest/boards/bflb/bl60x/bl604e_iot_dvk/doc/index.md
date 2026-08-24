---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/bflb/bl60x/bl604e_iot_dvk/doc/index.html
original_path: boards/bflb/bl60x/bl604e_iot_dvk/doc/index.html
---

# BL604E IOT DVK development board

Board Overview

[![../../../../../_images/bl_604e.webp](https://docs.zephyrproject.org/4.2.0/_images/bl_604e.webp)
](https://docs.zephyrproject.org/4.2.0/_images/bl_604e.webp)

BL604E IOT DVK development board

Name:
:   `bl604e_iot_dvk`

Vendor:
:   Bouffalo Lab (Nanjing) Co., Ltd.

Architecture:
:   riscv

SoC:
:   bl604e20q2i

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bflb/bl60x/bl604e_iot_dvk/doc/index.rst/../..)

## Overview

BL602/BL604 is a Wi-Fi+BLE chipset introduced by Bouffalo Lab, which is used
for low power consumption and high performance application development. The
wireless subsystem includes 2.4G radio, Wi-Fi 802.11b/g/n and BLE 5.0
baseband/MAC design. The microcontroller subsystem includes a 32-bit RISC CPU
with low power consumption, cache and memory. The power management unit
controls the low power consumption mode. In addition, it also supports
various security features. The external interfaces include SDIO, SPI, UART,
I2C, IR remote, PWM, ADC, DAC, PIR and GPIO.

The BL602 Development Board features a SiFive E24 32 bit RISC-V CPU with FPU,
it supports High Frequency clock up to 192Mhz, have 128k ROM, 276kB RAM,
2.4 GHz WIFI 1T1R mode, support 20 MHz, data rate up to 72.2 Mbps, BLE 5.0
with 2MB phy. It is a secure MCU which supports Secure boot, ECC-256 signed
image, QSPI/SPI Flash On-The-Fly AES Decryption and PKA (Public Key
Accelerator).

## Hardware

For more information about the Bouffalo Lab BL-60x MCU:

- [Bouffalo Lab BL60x MCU Website](https://en.bouffalolab.com/product/?type=detail&id=6)
- [Bouffalo Lab BL60x MCU Datasheet](https://github.com/bouffalolab/bl_docs/tree/main/BL602_DS/en)
- [Bouffalo Lab Development Zone](https://dev.bouffalolab.com/home?id=guest)
- [The RISC-V BL602 Book](https://lupyuen.github.io/articles/book)

### Supported Features

The `bl604e_iot_dvk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `bl604e_iot_dvk/bl604e20q2i` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | SiFive E24 Standard Core CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L61) | [`sifive,e24`](../../../../../build/dts/api/bindings/cpu/sifive%2Ce24.md#std-dtcompatible-sifive-e24) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L19) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | The BL60x PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L33) | [`bflb,bl60x-pll`](../../../../../build/dts/api/bindings/clock/bflb%2Cbl60x-pll.md#std-dtcompatible-bflb-bl60x-pll) |
| on-chip | The BL60x Root Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L40) | [`bflb,bl60x-root-clk`](../../../../../build/dts/api/bindings/clock/bflb%2Cbl60x-root-clk.md#std-dtcompatible-bflb-bl60x-root-clk) |
| on-chip | The BCLK clock, or peripheral clock Source Clock -> Root Clock -> / divider -> BCLK[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L48) | [`bflb,bclk`](../../../../../build/dts/api/bindings/clock/bflb%2Cbclk.md#std-dtcompatible-bflb-bclk) |
| on-chip | Bouffalolab BL60x Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L127) | [`bflb,bl60x-clock-controller`](../../../../../build/dts/api/bindings/clock/bflb%2Cbl60x-clock-controller.md#std-dtcompatible-bflb-bl60x-clock-controller) |
| GPIO & Headers | on-chip | Bouffalo Lab GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L114) | [`bflb,gpio`](../../../../../build/dts/api/bindings/gpio/bflb%2Cgpio.md#std-dtcompatible-bflb-gpio) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L69) | [`riscv,cpu-intc`](../../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| on-chip | SiFive RISC-V Core-Local Interruptor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L84) | [`sifive,clint0`](../../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cclint0.md#std-dtcompatible-sifive-clint0) |
| Pin control | on-chip | Bouffalo Lab Pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L106) | [`bflb,pinctrl`](../../../../../build/dts/api/bindings/pinctrl/bflb%2Cpinctrl.md#std-dtcompatible-bflb-pinctrl) |
| Serial controller | on-chip | Bouffalo Lab UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L148)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L157) | [`bflb,uart`](../../../../../build/dts/api/bindings/serial/bflb%2Cuart.md#std-dtcompatible-bflb-uart) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L190) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | BouffaloLab Efuse[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L141) | [`bflb,efuse`](../../../../../build/dts/api/bindings/syscon/bflb%2Cefuse.md#std-dtcompatible-bflb-efuse) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L98) | [`riscv,machine-timer`](../../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

### System Clock

The BL604E Development Board is configured to run at max speed (192MHz).

### Serial Port

The `bl604e_iot_dvk` board uses UART0 as default serial port. It is connected
to USB Serial converter and port is used for both program and console.

## Programming and Debugging

The `bl604e_iot_dvk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **bflb\_mcu\_tool** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

### Samples

#. Build the Zephyr kernel and the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample
application:

> ```shell
> # From the root of the zephyr repository
> west build -b bl604e_iot_dvk samples/hello_world
> west flash
> ```

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1

   Then, press and release RST button

   ```shell
   *** Booting Zephyr OS build v4.1.0 ***
   Hello World! bl604e_iot_dvk/bl604e20q2i
   ```

Congratulations, you have `bl604e_iot_dvk` configured and running Zephyr.
