---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzg3s_smarc/doc/index.html
original_path: boards/renesas/rzg3s_smarc/doc/index.html
---

# RZ/G3S SMARC Evaluation Board Kit

Board Overview

[![../../../../_images/rzg3s_smarc.webp](https://docs.zephyrproject.org/4.2.0/_images/rzg3s_smarc.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzg3s_smarc.webp)

RZ/G3S SMARC Evaluation Board Kit

Name:
:   `rzg3s_smarc`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a08g045s33gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzg3s_smarc/doc/index.rst/../..)

## Overview

The Renesas RZ/G3S SMARC Evaluation Board Kit (RZ/G3S-EVKIT) consists of a SMARC v2.1 module board and a carrier board.

- Device: RZ/G3S R9A08G045S33GBG

  - Cortex-A55 Single, Cortex-M33 x 2
  - BGA 359-pin, 14mmSq body, 0.5mm pitch
- SMARC v2.1 Module Board Functions

  - LPDDR4 SDRAM: 1GB x 1pc
  - QSPI flash memory: 128Mb x 1pc
  - eMMC memory: 64GB x 1pc
  - PMIC power supply RAA215300A2GNP#HA3 implemented
  - microSD card x2
  - I3C connector
  - JTAG connector
  - ADC x8 channels
  - Current monitor (USB Micro B)
- Carrier Board Functions

  - Gigabit Ethernet x2
  - USB2.0 x2ch (OTG x1ch, Host x1ch)
  - CAN-FD x2
  - microSD card x1
  - Mono speaker, Stereo headphone, Mic., and Aux..
  - PMOD x2
  - USB-Type C for power input
  - PCIe Gen2 4-lane slot (G3S supports only 1-lane)
  - M.2 Key E
  - M.2 Key B and SIM card
  - Coin cell battery holder (3.0V support)

## Hardware

The Renesas RZ/G3S MPU documentation can be found at [RZ/G3S Group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzg3s-general-purpose-microprocessors-single-core-arm-cortex-a55-11-ghz-cpu-and-dual-core-cortex-m33-250) [[2]](#id5)

[![RZ/G3S group feature](https://docs.zephyrproject.org/4.2.0/_images/rzg3s_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzg3s_block_diagram.webp)

RZ/G3S block diagram (Credit: Renesas Electronics Corporation)

## Multi-OS processing

The RZ/G3S-EVKIT allows different applications to be executed in RZ/G3S SoC. With its multi-core architecture,
each core can operate independently to perform customized tasks or exchange data using the OpenAMP framework.
Please see [OpenAMP Linux Zephyr RPMsg](../../../../samples/boards/renesas/openamp_linux_zephyr/README.md#rz-openamp-linux-zephyr "Enable message exchange between two cores, with the application core running Linux and the real-time core running Zephyr, using the OpenAMP library.") sample for reference.

### Supported Features

The `rzg3s_smarc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzg3s_smarc/r9a08g045s33gbg/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L24) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Renesas RZ ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L205) | [`renesas,rz-adc`](../../../../build/dts/api/bindings/adc/renesas%2Crz-adc.md#std-dtcompatible-renesas-rz-adc) |
| CAN | on-chip | Renesas RZ CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L478) | [`renesas,rz-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Crz-canfd-global.md#std-dtcompatible-renesas-rz-canfd-global) |
| on-chip | Renesas RZ CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L485)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L494) | [`renesas,rz-canfd`](../../../../build/dts/api/bindings/can/renesas%2Crz-canfd.md#std-dtcompatible-renesas-rz-canfd) |
| Clock control | on-chip | RZ Clock Pulse Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L53) | [`renesas,rz-cpg`](../../../../build/dts/api/bindings/clock/renesas%2Crz-cpg.md#std-dtcompatible-renesas-rz-cpg) |
| on-chip | Generic fixed-rate clock provider[26 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | Renesas RZ GTM Counter[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L561) | [`renesas,rz-gtm-counter`](../../../../build/dts/api/bindings/counter/renesas%2Crz-gtm-counter.md#std-dtcompatible-renesas-rz-gtm-counter) |
| DMA | on-chip | RZ DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L409) | [`renesas,rz-dma`](../../../../build/dts/api/bindings/dma/renesas%2Crz-dma.md#std-dtcompatible-renesas-rz-dma) |
| GPIO & Headers | on-chip | Renesas RZ GPIO Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L221) | [`renesas,rz-gpio-int`](../../../../build/dts/api/bindings/gpio/renesas%2Crz-gpio-int.md#std-dtcompatible-renesas-rz-gpio-int) |
| on-chip | Renesas RZ GPIO controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L236)[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L245) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| I2C | on-chip | Renesas RZ/G3S I2C controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L504) | [`renesas,rz-riic`](../../../../build/dts/api/bindings/i2c/renesas%2Crz-riic.md#std-dtcompatible-renesas-rz-riic) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg3s_smarc/rzg3s_smarc_r9a08g045s33gbg_cm33.dts?plain=1#L34) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | Renesas RZ external interrupt controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L840) | [`renesas,rz-ext-irq`](../../../../build/dts/api/bindings/interrupt-controller/renesas%2Crz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq) |
| Mailbox | on-chip | Renesas MHU MBOX[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L907) | [`renesas,rz-mhu-mbox`](../../../../build/dts/api/bindings/mbox/renesas%2Crz-mhu-mbox.md#std-dtcompatible-renesas-rz-mhu-mbox) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L32) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg3s_smarc/rzg3s_smarc_r9a08g045s33gbg_cm33.dts?plain=1#L78) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | Renesas RZ/G pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L216) | [`renesas,rzg-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crzg-pinctrl.md#std-dtcompatible-renesas-rzg-pinctrl) |
| PWM | on-chip | Renesas RZ GPT PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L709) | [`renesas,rz-gpt-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Crz-gpt-pwm.md#std-dtcompatible-renesas-rz-gpt-pwm) |
| Serial controller | on-chip | Renesas RZ SCIF UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L437)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L429) | [`renesas,rz-scif-uart`](../../../../build/dts/api/bindings/serial/renesas%2Crz-scif-uart.md#std-dtcompatible-renesas-rz-scif-uart) |
| SPI | on-chip | RENESAS RZ SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L962)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L973) | [`renesas,rz-rspi`](../../../../build/dts/api/bindings/spi/renesas%2Crz-rspi.md#std-dtcompatible-renesas-rz-rspi) |
| SRAM | on-board | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg3s_smarc/rzg3s_smarc_r9a08g045s33gbg_cm33.dts?plain=1#L63) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Renesas RZ GTM Timer[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L553) | [`renesas,rz-gtm`](../../../../build/dts/api/bindings/timer/renesas%2Crz-gtm.md#std-dtcompatible-renesas-rz-gtm) |
| on-chip | Renesas RZ OS timer[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L566) | [`renesas,rz-gtm-os-timer`](../../../../build/dts/api/bindings/timer/renesas%2Crz-gtm-os-timer.md#std-dtcompatible-renesas-rz-gtm-os-timer) |
| on-chip | Renesas RZ GPT[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a08g045.dtsi?plain=1#L698) | [`renesas,rz-gpt`](../../../../build/dts/api/bindings/timer/renesas%2Crz-gpt.md#std-dtcompatible-renesas-rz-gpt) |

## Programming and Debugging

The `rzg3s_smarc` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

RZ/G3S-EVKIT is designed to start different systems on different cores.
It uses Yocto as the build system to build Linux system and boot loaders
to run BL2 TF-A on Cortex-A55 System Core before starting Zephyr. The minimal steps are described below.

> 1. Follow ‘’2.2 Building Images’’ of [SMARC EVK of RZ/G3S Linux Start-up Guide](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104) [[3]](#id7) to prepare the build environment.
> 2. Before build, add `PLAT_M33_BOOT_SUPPORT=1` to meta-renesas/meta-rzg3s/recipes-bsp/trusted-firmware-a/trusted-firmware-a.bbappend.
>
> ```shell
>   require trusted-firmware-a.inc
>   COMPATIBLE_MACHINE_rzg3s = "(rzg3s-dev|smarc-rzg3s)"
>   PLATFORM_rzg3s-dev = "g3s"
>   EXTRA_FLAGS_rzg3s-dev = "BOARD=dev14_1_lpddr PLAT_SYSTEM_SUSPEND=vbat"
>   PLATFORM_smarc-rzg3s = "g3s"
>   EXTRA_FLAGS_smarc-rzg3s = "BOARD=smarc PLAT_SYSTEM_SUSPEND=vbat PLAT_M33_BOOT_SUPPORT=1"
> ```
>
> 3. Start the build:
>
> ```shell
> MACHINE=smarc-rzg3s bitbake core-image-minimal
> ```
>
> The below necessary artifacts will be located in the build/tmp/deploy/images
>
> | Artifacts | File name |
> | --- | --- |
> | Boot loader | bl2\_bp\_spi-smarc-rzg3s.srec  fip-smarc-rzg3s.srec |
> | Flash Writer | FlashWriter-smarc-rzg3s.mot |
>
> 4. Follow ‘’4.2 Startup Procedure’’ of [SMARC EVK of RZ/G3S Linux Start-up Guide](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104) [[3]](#id7) for power supply and board setting
>    at SCIF download (SW\_MODE[1:4] = OFF, ON, OFF, ON) and Cortex-A55 cold boot (SW\_CONFIG[1:6] = OFF, OFF, ON, OFF, OFF, OFF)
> 5. Follow ‘’4.3 Download Flash Writer to RAM’’ of [SMARC EVK of RZ/G3S Linux Start-up Guide](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104) [[3]](#id7) to download Flash Writer to RAM
> 6. Follow ‘’4.4 Write the Bootloader’’ of [SMARC EVK of RZ/G3S Linux Start-up Guide](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104) [[3]](#id7) to write the boot loader
>    to the target board by using Flash Writer.

Applications for the `rzg3s_smarc` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

### Console

The UART port for Cortex-M33 System Core can be accessed by connecting [Pmod USBUART](https://store.digilentinc.com/pmod-usbuart-usb-to-uart-interface/)
to the upper side of `PMOD1_3A`.

### Debugging

It is possible to load and execute a Zephyr application binary on
this board on the Cortex-M33 System Core from
the internal SRAM, using `JLink` debugger ([J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools)).

Note

Currently it’s required Renesas BL2 TF-A to be started on Cortex-A55 System Core
before starting Zephyr as it configures clocks and the Cortex-M33 System Core before starting it.

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rzg3s_smarc/r9a08g045s33gbg/cm33 samples/hello_world
west debug
```

### Flashing

Zephyr application can be flashed to QSPI storage and then loaded by
Renesas BL2 TF-A running on the Cortex-A55 System Core and starting binary on the Cortex-M33 System Core.

The Zephyr application binary has to be converted to Motorolla S-record [SREC](https://en.wikipedia.org/wiki/SREC_(file_format)) [[1]](#id3) format
which is generated automatically in Zephyr application build directory with the extension `s19`.

#### Flashing on QSPI using Flash Writer

Zephyr binary has to be converted to **srec** format.

- Download and start **Flash Writer** as described in ‘’4.3 Download Flash Writer to RAM’’ of [SMARC EVK of RZ/G3S Linux Start-up Guide](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104) [[3]](#id7)
- Use **XLS2** command to flash Zephyr binary
- Input when asked:

```shell
===== Please Input Program Top Address ============
  Please Input : H'23000
===== Please Input Qspi Save Address ===
  Please Input : H'200000
```

- Then send Zephyr **s19** file from terminal (use ‘’ascii’’ mode)
- Reboot the board in the **QSPI Boot Mode**

```shell
 -- Load Program to SRAM ---------------

Flash writer for RZ/G3S Series V0.60 Jan.26,2023
 Product Code : RZ/G3S
>XLS2
===== Qspi writing of RZ/G2 Board Command =============
Load Program to Spiflash
Writes to any of SPI address.
Program size & Qspi Save Address
===== Please Input Program Top Address ============
  Please Input : H'23000

===== Please Input Qspi Save Address ===
  Please Input : H'200000
please send ! ('.' & CR stop load)
I Flash memory...
Erase Completed
Write to SPI Flash memory.
======= Qspi  Save Information  =================
 SpiFlashMemory Stat Address : H'00200000
 SpiFlashMemory End Address  : H'002098E6
===========================================================
```

#### Flashing on QSPI using west

Before using `flash` command, the board must be set to Cortex-M33 cold boot (SW\_CONFIG[1:6] = OFF, OFF, ON, OFF, OFF, ON).
After flashing, it must be set back to Cortex-A55 cold boot to run.

The minimal version of SEGGER JLink SW which can perform flashing of QSPI memory is v7.96.

**Note:** It’s verified that we can perform flashing successfully with SEGGER JLink SW v7.98g so please use this or later
version.

```shell
west build -b rzg3s_smarc/r9a08g045s33gbg/cm33 samples/hello_world
west flash
```

### Troubleshooting

Linux and Zephyr application should not share SoC HW resources otherwise it will cause HW corruption and unpredictable behavior.
Therefore, HW resources assigned to Zephyr application must be disabled in Linux.

The below patch shows how to prevent Linux from configuring SCIF1 which is used by Zephyr.

```diff
diff --git a/arch/arm64/boot/dts/renesas/rzg3s-smarc.dtsi b/arch/arm64/boot/dts/renesas/rzg3s-smarc.dtsi
index f01801b18e8a..d9f9a0a2bb08 100644
--- a/arch/arm64/boot/dts/renesas/rzg3s-smarc.dtsi
+++ b/arch/arm64/boot/dts/renesas/rzg3s-smarc.dtsi
@@ -347,7 +347,7 @@ &scif1 {
        pinctrl-0 = <&scif1_pins>;
        pinctrl-names = "default";
        uart-has-rtscts;
-       status = "okay";
+       status = "disabled";
};
#elif SPDIF_SEL == SW_ON
&spdif {
```

## References

[[1](#id4)]

[https://en.wikipedia.org/wiki/SREC\_(file\_format)](https://en.wikipedia.org/wiki/SREC_(file_format))

[[2](#id6)]

[https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzg3s-general-purpose-microprocessors-single-core-arm-cortex-a55-11-ghz-cpu-and-dual-core-cortex-m33-250](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzg3s-general-purpose-microprocessors-single-core-arm-cortex-a55-11-ghz-cpu-and-dual-core-cortex-m33-250)

[3]
([1](#id8),[2](#id9),[3](#id10),[4](#id11),[5](#id12))

[https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev104)
