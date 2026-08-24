---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/variscite/imx93_var_dart/doc/index.html
original_path: boards/variscite/imx93_var_dart/doc/index.html
---

# DART-MX93

Board Overview

[![../../../../_images/imx93_var_dart.webp](https://docs.zephyrproject.org/4.2.0/_images/imx93_var_dart.webp)
](https://docs.zephyrproject.org/4.2.0/_images/imx93_var_dart.webp)

DART-MX93

Name:
:   `imx93_var_dart`

Vendor:
:   Variscite Ltd.

Architecture:
:   arm64, arm

SoC:
:   mimx9352

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/variscite/imx93_var_dart/doc/index.rst/../..)

## Overview

The DART-MX93 offers a high-performance processing for a low-power System-on-Module.
The product is based on the i.MX 93 family which represents NXP’s latest power-optimized
processors for smart home, building control, contactless HMI, IoT edge, and Industrial
applications.

The i.MX 93 includes powerful dual Arm® Cortex®-A55 processors with speeds up to 1.7 GHz
integrated with a NPU that accelerates machine learning inference. A general-purpose Arm®
Cortex®-M33 running up to 250 MHz is for real-time and low-power processing. Robust control
networks are possible via CAN-FD interface. Also, dual 1 Gbps Ethernet controllers, one
supporting Time Sensitive Networking (TSN), drive gateway applications with low latency.

Zephyr OS is ported to run on either the Cortex®-A55 or the Cortex®-M33.

## Specs Summary

> - CPU
>
>   - NXP i.MX 93:
>   - 2x Cortex®-A55 @ 1.7GHz
>   - 1x Cortex®-M33 @ 250 MHz
>   - 1x Ethos-U65 microNPU 0.5 TOPS
> - Memory
>
>   - Up to 2GB LPDDR4 RAM
> - GPU
>
>   - PXP 2D Pixel acceleration engine
> - NPU (Neural Processing Unit)
>
>   - Neural Network performance (256 MACs operating up to 1.0 GHz and 2 OPS/MAC)
>   - NPU targets 8-bit and 16-bit integer RNN
>   - Handles 8-bit weights
> - Display
>
>   - LVDS up to 1366x768p60 or 1280x800p60
>   - Parallel RGB up to 1366x768p60 or 1280x800p60
>   - 1x MIPI DSI up to 1920x1200p60 24-bit
> - Network
>
>   - 2x 10/100/1000 Mbit/s Ethernet Interface
>   - Certified Wi-Fi 802.11ax/ac/a/b/g/n
>   - Bluetooth/BLE 5.4
> - Camera
>
>   - One 2-lane MIPI CSI-2 camera input
> - Audio
>
>   - Headphones
>   - Microphone: Digital, Analog (stereo)
>   - 3x I2S(SAI), S/PDIF, PDM 4CH
> - USB
>
>   - 2x USB 2.0 OTG
> - Serial interfaces
>
>   - SPI: x7
>   - I2C: x7
>   - UART: x7, up to 5 Mbps
>   - CAN: x2
> - Temperature range
>
>   - -40°C to 85°C

More information about the SoM can be found at the
[Variscite Wiki](https://variwiki.com/index.php?title=DART-MX93) and
[Variscite website](https://www.variscite.com/product/system-on-module-som/cortex-a55/dart-mx93-nxp-i-mx93/).

## Supported Features

The `imx93_var_dart` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### `imx93_var_dart/mimx9352/a55` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L29)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L23) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm,cortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| CAN | on-chip | NXP FlexCAN CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L329) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L79) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| Counter | on-chip | NXP Timer/PWM Module (TPM) used as timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L434) | [`nxp,tpm-timer`](../../../../build/dts/api/bindings/counter/nxp,tpm-timer.md#std-dtcompatible-nxp-tpm-timer) |
| DAI | on-chip | NXP Synchronous Audio Interface (SAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L364) | [`nxp,dai-sai`](../../../../build/dts/api/bindings/dai/nxp,dai-sai.md#std-dtcompatible-nxp-dai-sai) |
| DMA | on-chip | NXP enhanced Direct Memory Access (eDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L353) | [`nxp,edma`](../../../../build/dts/api/bindings/dma/nxp,edma.md#std-dtcompatible-nxp-edma) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L404) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L410) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L425) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX RGPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L85) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L145) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart_mimx9352_a55.dts?plain=1#L61) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L55) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart_mimx9352_a55.dts?plain=1#L53) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L419) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L64) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L68) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 1.1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L50) | [`arm,psci-1.1`](../../../../build/dts/api/bindings/pm_cpu_ops/arm,psci-1.1.md#std-dtcompatible-arm-psci-1.1) |
| SDHC | on-chip | NXP imx USDHC controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L378) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart_mimx9352_a55.dts?plain=1#L35)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L125) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L241) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L37) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### `imx93_var_dart/mimx9352/m33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L17) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L33) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L38) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L53) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| GPIO & Headers | on-chip | i.MX RGPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L59) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart_mimx9352_m33.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart_mimx9352_m33.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L43) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L47) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_dart/imx93_var_dart-m33-common.dtsi?plain=1#L11)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L91) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

Note

It is recommended to disable peripherals used by the M33 core on the Linux host.

### Devices

#### System Clock

This board configuration uses a system clock frequency of 24 MHz.
Cortex-A55 Core runs up to 1.7 GHz.
Cortex-M33 Core runs up to 200MHz in which SYSTICK runs on same frequency.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART7 for A55 core and M33 core.

## Programming and Debugging (A55)

Copy the compiled `zephyr.bin` to the boot directory of the SD card and
plug the SD card into the board. Power it up and stop the U-Boot execution at
prompt.

Use U-Boot to load and run zephyr.bin on the Cortex-A55:

```shell
load mmc $mmcdev:$mmcpart $loadaddr /boot/zephyr.bin
dcache off; icache flush; go $loadaddr
```

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample:

```shell
# From the root of the zephyr repository
west build -b imx93_var_dart/mimx9352/a55 samples/hello_world
```

This will build an image with the hello\_world sample app. When loaded and executed
it will display the following ram console output:

```shell
*** Booting Zephyr OS build v4.0.0-44-g93cbaccbbc41 ***
Hello World! imx93_var_dart/mimx9352/a55
```

## Programming and Debugging (M33)

The `imx93_var_dart` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

There are two methods to load M33 Core images: U-Boot command and Linux remoteproc.

### Load and Run M33 Zephyr Image from U-Boot

Load and run Zephyr on M33 from A55 using U-Boot by copying the compiled
`zephyr.bin` to the boot directory of the SD card and plug the SD
card into the board. Power it up and stop the U-Boot execution at prompt.

Load the M33 binary onto the desired memory and start its execution using:

```shell
load mmc $mmcdev:$mmcpart 0x80000000 /boot/zephyr.bin
cp.b 0x80000000 0x201e0000 0x30000
bootaux 0x1ffe0000 0
```

### Load and Run M33 Zephyr Image by using Linux remoteproc

Transfer built binaries `zephyr.bin` and `zephyr.elf` to the SoM’s `/boot` and
`/lib/firmware` respectively using `scp` or through an USB drive.

Before running Cortex-M33 binaries from Linux it is necessary to enable the device tree
dedicated to be used with Cortex-M33 applications:

```shell
root@imx93-var-som:~# fw_setenv fdt_file imx93-var-dart-dt8mcustomboard-m33.dtb
root@imx93-var-som:~# reboot
```

It is possible to execute Zephyr binaries using Variscite remoteproc scripts made
for MCUXpresso binaries:

```shell
root@imx93-var-som:~# /etc/remoteproc/variscite-rproc-linux -f /lib/firmware/zephyr.elf
[  125.449838] remoteproc remoteproc0: powering up imx-rproc
[  125.459162] remoteproc remoteproc0: Booting fw image zephyr.elf, size 469356
[  125.468958] remoteproc remoteproc0: No resource table in elf
[  125.987142] remoteproc remoteproc0: remote processor imx-rproc is now up
```

Which should yield the following result on the UART7 serial console:

```shell
*** Booting Zephyr OS build v4.0.0-44-g93cbaccbbc41 ***
Hello World! imx93_var_dart/mimx9352/m33
```

You can also configure U-Boot to load firmware on boot:

```shell
root@imx93-var-som:~# /etc/remoteproc/variscite-rproc-u-boot -f /boot/zephyr.bin
Configuring for TCM memory
+ fw_setenv m33_addr 0x201E0000
+ fw_setenv fdt_file imx93-var-dart-dt8mcustomboard-m33.dtb
+ fw_setenv use_m33 yes
+ fw_setenv m33_bin zephyr.bin

Finished: Please reboot, the m33 firmware will run during U-Boot
```

For more information about Variscite remoteproc scripts and general Cortex-M33
support, visit [Variscite Wiki](https://variwiki.com/index.php?title=DART-MX93).

## References

- [Variscite Wiki](https://variwiki.com/index.php?title=DART-MX93)
- [Variscite website](https://www.variscite.com/product/system-on-module-som/cortex-a55/dart-mx93-nxp-i-mx93/)
- [NXP website](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-processors/i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93)
