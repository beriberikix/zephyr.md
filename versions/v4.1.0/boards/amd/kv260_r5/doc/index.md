---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/amd/kv260_r5/doc/index.html
original_path: boards/amd/kv260_r5/doc/index.html
---

# KV260 Development Board RPU Cortex-R5

Board Overview

[![../../../../_images/kv260-starter-kit.jpg](../../../../_images/kv260-starter-kit.jpg)
](../../../../_images/kv260-starter-kit.jpg)

KV260 Development Board RPU Cortex-R5

Name:
:   `kv260_r5`

Vendor:
:   Advanced Micro Devices (AMD), Inc.

Architecture:
:   arm

SoC:
:   zynqmp\_rpu

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/kv260_r5/doc/index.rst/../..)

## Overview

This configuration provides support for the RPU, real-time processing unit on Xilinx
KV260 development board, it can operate as following:

- Two independent R5 cores with their own TCMs (tightly coupled memories)
- Or as a single dual lock step unit with double the TCM size.

This processing unit is based on an ARM Cortex-R5 CPU, it also enables the following devices:

- ARM PL-390 Generic Interrupt Controller
- Xilinx Zynq TTC (Cadence TTC)
- Xilinx Zynq UART

## Hardware

### Supported Features

The `kv260_r5` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `kv260_r5/zynqmp_rpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L14) | [`arm,cortex-r5f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5f.md#std-dtcompatible-arm-cortex-r5f) |
| Ethernet | on-chip | Xilinx GEM Ethernet controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L104) | [`xlnx,gem`](../../../../build/dts/api/bindings/ethernet/xlnx%2Cgem.md#std-dtcompatible-xlnx-gem) |
| GPIO & Headers | on-chip | Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L212) | [`xlnx,ps-gpio`](../../../../build/dts/api/bindings/gpio/xlnx%2Cps-gpio.md#std-dtcompatible-xlnx-ps-gpio) |
| on-chip | Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO controller bank node[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L223) | [`xlnx,ps-gpio-bank`](../../../../build/dts/api/bindings/gpio/xlnx%2Cps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L101) | [`arm,gic-v1`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v1.md#std-dtcompatible-arm-gic-v1) |
| IPM | on-chip | The Xilinx IPI(Inter Processor Interrupt) mailbox controller is to manage messaging between two Xilinx Zynq UltraScale+ MPSoC IPI agents[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L23) | [`xlnx,zynqmp-ipi-mailbox`](../../../../build/dts/api/bindings/ipm/xlnx%2Czynqmp-ipi-mailbox.md#std-dtcompatible-xlnx-zynqmp-ipi-mailbox) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L18) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Xilinx ZynqMP SoC pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L14) | [`xlnx,pinctrl-zynqmp`](../../../../build/dts/api/bindings/pinctrl/xlnx%2Cpinctrl-zynqmp.md#std-dtcompatible-xlnx-pinctrl-zynqmp) |
| Serial controller | on-chip | Xilinx PS UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L43)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L34) | [`xlnx,xuartps`](../../../../build/dts/api/bindings/serial/xlnx%2Cxuartps.md#std-dtcompatible-xlnx-xuartps) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L23) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Xilinx ZynqMP PS TTC timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L52)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L65) | [`xlnx,ttcps`](../../../../build/dts/api/bindings/timer/xlnx%2Cttcps.md#std-dtcompatible-xlnx-ttcps) |

### Devices

#### System Timer

This board configuration uses a system timer tick frequency of 1000 Hz.

#### Serial Port

This board configuration uses a single serial communication channel with the
on-chip UART1.

#### Memories

Although Flash, DDR and OCM memory regions are defined in the DTS file,
all the code plus data of the application will be loaded in the sram0 region,
which points to the DDR memory. The ocm0 memory area is currently available
for usage, although nothing is placed there by default.

### Known Problems or Limitations

The following platform features are unsupported:

- Dual-redundant Core Lock-step (DCLS) execution is not supported yet.
- Only the first core of the R5 subsystem is supported.
- Xilinx Zynq TTC driver does not support tickless mode operation.
- The Cortex-R5 and the Cortex-A53 shares the same UART controller, more details below.

## Programming and Debugging

Currently the best way to run this sample is by loading it through remoteproc
from the APU, running Linux, to the RPU, assuming the target board has a compatible
Linux kernel.
Users can make use of Xilinx’s pre-built Petalinux reference images as a starting point to enable
remoteproc support, it is based around 5.15 Xilinx maintained kernel, as described here:

[https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM#PetaLinux](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM#PetaLinux)

The other option is to use the reference image from the openAMP project, the link
below points, betweem the options, to the kv260 target:

[https://github.com/OpenAMP/openamp-ci-builds/releases/tag/v2022.12](https://github.com/OpenAMP/openamp-ci-builds/releases/tag/v2022.12)

Select the option `xilinx-kv260.tar.gz`, and just decompress it to the target rootfs
partition of user’s SD card:

```shell
$ sudo mount /dev/<user-sd> /media/rootfs
$ sudo tar -C /media/rootfs -xzf xilinx-kv260.tar.gz
$ sudo umount /media/rootfs
```

Your SD file may be ready for use, just plug it to the slot located in the board.

After getting the Linux image running on the target board, build a Zephyr application,
such as the hello world sample shown below:

```shell
# From the root of the zephyr repository
west build -b kv260_r5 samples/hello_world
```

Due to a hardware limitation, both Linux and Zephyr share the same UART
controller, meaning when the Zephyr application is started it will takeover the
console from Linux.

To avoid this limitation when accessing the Linux shell, the best approach is to
connect to the board using `ssh` over the network (not using the FTDI
USB interface on the board), with the dev board and the host computer
connected to the same network.

Assuming you are using the default `petalinux` user from the Xilinx
reference image , open a terminal on the host machine and ssh into the
development board with the board’s IP address (found via `ifconfig`):

```shell
$ ssh petalinux@<board-ip-address>
```

The initial password should be `petalinux`. On another terminal deploy
the Zephyr application `.elf` file using utility like the `scp` or `rsync`,
for example:

```shell
$ scp /path/to/zephyr_app_elf_file  petalinux@<board-ip-address>:/home/petalinux
```

After that move the file to `/lib/firmware` directory, then you be able to start the firmware
on the desired RPU via remoteproc with:

```shell
$ sudo -i # You need to operate the remoteproc as root
$ echo zephyr.elf > /sys/class/remoteproc/remoteproc0/firmware
$ echo start > /sys/class/remoteproc/remoteproc0/state
```

With another terminal connected to UART1 on the host machine
(available via one of the tty ports with the on-board FTDI chip),
you should see the Zephyr application running:

```shell
*** Booting Zephyr OS build v3.4.0  ***
Hello World kv260_r5!
```

## References

1. ARMv7-A and ARMv7-R Architecture Reference Manual (ARM DDI 0406C ID051414)
2. Cortex-R5 and Cortex-R5F Technical Reference Manual (ARM DDI 0460C ID021511)
3. Zynq UltraScale+ Device Technical Reference Manual (UG1085)
4. Kria KV260 Vision AI Starter Kit User Guide (UG1089)
