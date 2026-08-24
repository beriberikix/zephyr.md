---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/ls1046ardb/doc/index.html
original_path: boards/nxp/ls1046ardb/doc/index.html
---

# LS1046A RDB

Board Overview

Name:
:   `ls1046ardb`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64

SoC:
:   ls1046a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/ls1046ardb/doc/index.rst/../..)

## Overview

The LS1046A reference design board (RDB) is a high-performance computing,
evaluation, and development platform that supports the Layerscape LS1046A
architecture processor. The LS1046ARDB board supports the Layerscape LS1046A
processor and is optimized to support the DDR4 memory and a full complement
of high-speed SerDes ports.

The Layerscape LS1046A processor integrates four 64-bit Arm(R) Cortex(R) A72
cores with packet processing acceleration and high-speed peripherals. The
impressive performance of more than 32,000 CoreMarks, paired with 10 Gb
Ethernet, PCIe Gen. 3, SATA 3.0, USB 3.0 and QSPI interfaces provides an
excellent combination for a range of enterprise and service provider
networking, storage, security and industrial applications.

## Hardware

LS1046A RDB boards supports the following features:

- Four 32/64-bit Arm(R) Cortex(R)V8 A72 CPUs, up to 1.6 GHz core speed
- Supports 8 GB DDR4 SDRAM memory
- SDHC port connects directly to an adapter card slot, featuring 4 GB eMMCi
  memory device
- One 512 MB SLC NAND flash with ECC support (1.8 V)
- CPLD connection: 8-bit registers in CPLD to configure mux/demux selections
- Support two 64 MB onboard QSPI NOR flash memories
- USB:
  - Two USB 3.0 controllers with integrated PHYs.
  - One USB1 3.0 port is connected to a Type A host connector.
  - One USB1 3.0 port is configured as On-The-Go (OTG) with a Micro-AB connector.
  - One USB2.0 is connected to miniPCIe connector .
- Ethernet:
  - Supports SGMII 1G PHYs at Lane 2 and Lane 3
  - Supports SFP+module with XFI retimers
  - Supports AQR106/107 10G PHY with XFI/2.5G SGMII
- PCIe and SATA:
  - Mini PCIe express x1 (Gen1/2/3)card
  - Standard PCIe x1 (Gen1/2/3) card
  - Standard PCIe x1 (Gen1/2/3) card
  - One SATA 3.0 connector

### Supported Features

The `ls1046ardb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ls1046ardb/ls1046a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A72 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L33) | [`arm,cortex-a72`](../../../../build/dts/api/bindings/cpu/arm,cortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L40) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v2.md#std-dtcompatible-arm-gic-v2) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L71) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L58) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `ls1046ardb/ls1046a/smp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A72 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L28) | [`arm,cortex-a72`](../../../../build/dts/api/bindings/cpu/arm,cortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L40) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v2.md#std-dtcompatible-arm-gic-v2) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L49) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm,psci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L71) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L58) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `ls1046ardb/ls1046a/smp/4cores` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A72 CPU[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L18) | [`arm,cortex-a72`](../../../../build/dts/api/bindings/cpu/arm,cortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L40) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v2.md#std-dtcompatible-arm-gic-v2) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L49) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm,psci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L71) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_ls1046a.dtsi?plain=1#L58) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

Note

There are two serial ports on the board: uart1 and uart2. Zephyr is using
uart2 as serial console.

## Programming and Debugging

The `ls1046ardb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Use the following configuration to run basic Zephyr applications and
kernel tests on LS1046A RDB board. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

1. Non-SMP mode

```shell
# From the root of the zephyr repository
west build -b ls1046ardb samples/synchronization
```

This will build an image with the synchronization sample app.

Use u-boot to load and kick Zephyr.bin to CPU Core0:

```shell
tftp c0000000 zephyr.bin; dcache off; dcache flush; icache flush; icache off; go  0xc0000000;
```

Or kick Zephyr.bin to any other CPU Cores, for example run Zephyr on Core3:

```shell
tftp c0000000 zephyr.bin; dcache off; dcache flush; icache flush; icache off; cpu 3 release 0xc0000000;
```

It will display the following console output:

```shell
*** Booting Zephyr OS build zephyr-v2.5.0-1922-g3265b69d47e7  ***
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
thread_b: Hello World from cpu 0 on nxp_ls1046ardb!
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
```

2. SMP mode running on 4 CPU Cores

```shell
# From the root of the zephyr repository
west build -b ls1046ardb/ls1046a/smp/4cores samples/synchronization
```

This will build an image with the synchronization sample app.

Use u-boot to load and kick Zephyr.bin to CPU Core0:

```shell
tftp c0000000 zephyr.bin; dcache off; dcache flush; icache flush; icache off; go  0xc0000000;
```

It will display the following console output:

```shell
*** Booting Zephyr OS build zephyr-v2.5.0-1922-g3265b69d47e7  ***
Secondary CPU core 1 (MPID:0x1) is up
Secondary CPU core 2 (MPID:0x2) is up
Secondary CPU core 3 (MPID:0x3) is up
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
thread_b: Hello World from cpu 1 on nxp_ls1046ardb!
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
```

3. SMP mode running on 2 CPU Cores: Core2 and Core3

```shell
# From the root of the zephyr repository
west build -b ls1046ardb/ls1046a/smp samples/synchronization
```

This will build an image with the synchronization sample app.

Use u-boot to load and kick Zephyr.bin to CPU Core2:

```shell
tftp c0000000 zephyr.bin; dcache off; dcache flush; icache flush; icache off; cpu 2 release 0xc0000000;
```

It will display the following console output:

```shell
*** Booting Zephyr OS build zephyr-v2.5.0-1922-g3265b69d47e7  ***
Secondary CPU core 1 (MPID:0x3) is up
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
thread_b: Hello World from cpu 1 on nxp_ls1046ardb!
thread_a: Hello World from cpu 0 on nxp_ls1046ardb!
```

4. Running Zephyr on Jailhouse inmate Cell

Use the following to run Zephyr in Jailhouse inmate, need to configure Jailhouse
inmate Cell to use a single Core for Zephyr non-SMP mode, or use Core2 and Core3
for Zephyr SMP 2cores image.

1. Use root Cell dts to boot root Cell Linux.
2. Install Jailhouse module:

```shell
modprobe jailhouse
```

3. Run Zephyr demo in inmate Cell:

```shell
jailhouse enable ls1046a-rdb.cell
jailhouse cell create ls1046a-rdb-inmate-demo.cell
jailhouse cell load 1 zephyr.bin --address 0xc0000000
jailhouse cell start 1
```

### Flashing

Zephyr image can be loaded in DDR memory at address 0xc0000000 from SD Card,
EMMC, QSPI Flash or downloaded from network in uboot.

### Debugging

LS1046A RDB board includes one JTAG connector on board, connect it to
CodeWarrior TAP for debugging.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

### References

[Layerscape LS1046A Reference Design Board](https://www.nxp.com/design/qoriq-developer-resources/layerscape-ls1046a-reference-design-board:LS1046A-RDB)

[LS1046A Reference Manual](https://www.nxp.com/webapp/Download?colCode=LS1046ARM)
