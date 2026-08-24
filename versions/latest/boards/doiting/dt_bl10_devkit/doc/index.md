---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/doiting/dt_bl10_devkit/doc/index.html
original_path: boards/doiting/dt_bl10_devkit/doc/index.html
---

# DT-BL10 coexistence Module Development Kit

Board Overview

[![../../../../_images/dt_bl10_devkit.webp](https://docs.zephyrproject.org/4.2.0/_images/dt_bl10_devkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/dt_bl10_devkit.webp)

DT-BL10 coexistence Module Development Kit

Name:
:   `dt_bl10_devkit`

Vendor:
:   Doctors of Intelligence & Technology

Architecture:
:   riscv

SoC:
:   bl602c20q2i

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/doiting/dt_bl10_devkit/doc/index.rst/../..)

## DT-BL10 Development Kit

### Overview

DT-BL10 Wi-Fi and BLE coexistence Module is a highly integrated single-chip
low power 802.11n Wireless LAN (WLAN) network controller. It combines an RISC
CPU, WLAN MAC, a lT1R capable WLAN baseband, RF, and Bluetooth in a single chip.
It also provides a bunch of configurable GPIO, which are configured as digital
peripherals for different applications and control usage.

DT-BL10 WiFi Module use BL602 as Wi-Fi and BLE coexistence soc chip. DT-BL10
WiFi Module integrates internal memories for complete WIFI protocol functions.
The embedded memory configuration also provides simple application developments.

DT-BL10 WiFi module supports the standard IEEE 802.11 b/g/n/e/i protocol and the
complete TCP/IP protocol stack. User can use it to add the WiFi function for the
installed devices, and also can be viewed as a independent network controller.

### Hardware

For more information about the Bouffalo Lab BL-602 MCU:

- [Bouffalo Lab BL602 MCU Website](https://www.bouffalolab.com/bl602)
- [Bouffalo Lab BL602 MCU Datasheet](https://github.com/bouffalolab/bl_docs/tree/main/BL602_DS/en)
- [Bouffalo Lab Development Zone](https://dev.bouffalolab.com/home?id=guest)
- [dt\_bl10\_devkit Schematic](https://github.com/SmartArduino/Doiting_BL/blob/master/board/DT-BL10%20User%20Mannual.pdf)
- [Doctors of Intelligence & Technology (www.doiting.com)](https://www.doiting.com)
- [The RISC-V BL602 Book](https://lupyuen.github.io/articles/book)

#### Supported Features

The `dt_bl10_devkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

##### `dt_bl10_devkit/bl602c20q2i` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | SiFive E24 Standard Core CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L61) | [`sifive,e24`](../../../../build/dts/api/bindings/cpu/sifive,e24.md#std-dtcompatible-sifive-e24) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L19) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | The BL60x PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L33) | [`bflb,bl60x-pll`](../../../../build/dts/api/bindings/clock/bflb,bl60x-pll.md#std-dtcompatible-bflb-bl60x-pll) |
| on-chip | The BL60x Root Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L40) | [`bflb,bl60x-root-clk`](../../../../build/dts/api/bindings/clock/bflb,bl60x-root-clk.md#std-dtcompatible-bflb-bl60x-root-clk) |
| on-chip | The BCLK clock, or peripheral clock Source Clock -> Root Clock -> / divider -> BCLK[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L48) | [`bflb,bclk`](../../../../build/dts/api/bindings/clock/bflb,bclk.md#std-dtcompatible-bflb-bclk) |
| on-chip | Bouffalolab BL60x Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L127) | [`bflb,bl60x-clock-controller`](../../../../build/dts/api/bindings/clock/bflb,bl60x-clock-controller.md#std-dtcompatible-bflb-bl60x-clock-controller) |
| GPIO & Headers | on-chip | Bouffalo Lab GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L114) | [`bflb,gpio`](../../../../build/dts/api/bindings/gpio/bflb,gpio.md#std-dtcompatible-bflb-gpio) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L69) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv,cpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| on-chip | SiFive RISC-V Core-Local Interruptor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L84) | [`sifive,clint0`](../../../../build/dts/api/bindings/interrupt-controller/sifive,clint0.md#std-dtcompatible-sifive-clint0) |
| Pin control | on-chip | Bouffalo Lab Pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L106) | [`bflb,pinctrl`](../../../../build/dts/api/bindings/pinctrl/bflb,pinctrl.md#std-dtcompatible-bflb-pinctrl) |
| Serial controller | on-chip | Bouffalo Lab UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L148)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L157) | [`bflb,uart`](../../../../build/dts/api/bindings/serial/bflb,uart.md#std-dtcompatible-bflb-uart) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L190) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | BouffaloLab Efuse[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L141) | [`bflb,efuse`](../../../../build/dts/api/bindings/syscon/bflb,efuse.md#std-dtcompatible-bflb-efuse) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl60x.dtsi?plain=1#L98) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv,machine-timer.md#std-dtcompatible-riscv-machine-timer) |

#### System Clock

The DT-BL10 board is configured to run at max speed (192MHz).

#### Serial Port

The `dt_bl10_devkit` board uses UART0 as default serial port. It is connected
to USB Serial converter and port is used for both program and console.

### Programming and Debugging

The `dt_bl10_devkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **bflb\_mcu\_tool** | ✅ (default) |  |

#### Samples

#. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample
application:

> ```shell
> # From the root of the zephyr repository
> west build -b dt_bl10_devkit samples/hello_world
> ```

1. To flash an image using blflash runner:

   1. Press D8 button
   2. Press and release EN button
   3. Release D8 button

   ```shell
   west flash
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

   Then, press and release EN button

   ```shell
   *** Booting Zephyr OS build v4.1.0-4682-g21b20de1eb34 ***
   Hello World! dt_bl10_devkit/bl602c20q2i
   ```

Congratulations, you have `dt_bl10_devkit` configured and running Zephyr.
