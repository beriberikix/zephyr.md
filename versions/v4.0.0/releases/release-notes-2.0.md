---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/release-notes-2.0.html
original_path: releases/release-notes-2.0.html
---

# Zephyr 2.0.0

We are pleased to announce the release of Zephyr RTOS version 2.0.0.

Major enhancements with this release include:

- The kernel now supports both 32- and 64-bit architectures.
- We added support for SOCKS5 proxy. SOCKS5 is an Internet protocol that
  exchanges network packets between a client and server through a proxy server.
- Introduced support for 6LoCAN, a 6Lo adaption layer for Controller Area
  Networks.
- We added support for [Point-to-Point Protocol (PPP)](../connectivity/networking/api/ppp.md#ppp). PPP is a
  data link layer (layer 2) communications protocol used to establish a direct
  connection between two nodes.
- We added support for UpdateHub, an end-to-end solution for large scale
  over-the-air device updates.
- We added support for ARM Cortex-R Architecture (Experimental).

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following security vulnerability (CVE) was addressed in this
release:

- Fixes CVE-2019-9506: The Bluetooth BR/EDR specification up to and
  including version 5.1 permits sufficiently low encryption key length
  and does not prevent an attacker from influencing the key length
  negotiation. This allows practical brute-force attacks (aka “KNOB”)
  that can decrypt traffic and inject arbitrary ciphertext without the
  victim noticing.

## Kernel

- New kernel API for per-thread disabling of Floating Point Services for
  ARC, ARM Cortex-M, and x86 architectures.
- New system call to set the clock frequency at runtime.
- Additional support for compatibility with 64-bit architectures.
- Userspace mutexes are now supported through the new k\_futex primitive.
- Improvements to the slab allocator.
- Fixed the implementation of k\_thread\_name\_set() with userspace enabled.
- Boosted the default tick rate for tickless kernels to improve the
  precision of timeouts.

## Architectures

- ARM:

  - Added initial support for ARM Cortex-R architecture (Experimental)
  - We enhanced the support for Floating Point Services in Cortex-M
    architecture, implementing and enabling lazy-stacking for FPU
    capable threads and fixing stack overflow detection for FPU
    capable supervisor threads
  - Added QEMU support for ARMv8-M Mainline architecture
  - Optimized the IRQ locking time in thread context switch
  - Fixed several critical bugs in User Mode implementation
  - Added test coverage for ARM-specific kernel features
  - Improved support for linking TrustZone Secure Entry functions into
    Non-Secure firmware
- ARC:

  - Added support for ARC HS architecture
  - Added SMP support for ARC HS architecture
  - Added support for ARC SecureShield based TEE (Experimental)
  - Fixed several critical bugs in interrupt and exception handling
  - Enhance the support for Floating Point Services
- POSIX:

  - Fixed race condition with terminated threads which had never been
    scheduled by kernel. On very loaded systems it could cause swap errors.
- x86:

  - Dropped support for the Intel Quark microcontroller family.
  - A new lightweight PCI implementation has been introduced which supports
    MSI and other features required for PCIe devices. The previous PCI
    implementation has been deprecated and will be removed in 2.1.
- RISC-V:

  - Added support for the SiFive HiFive1 Rev B development board.
  - Added support for LiteX VexRiscv soft core.
  - Added support for 64-bit RISC-V, renaming the architecture from “riscv32”
    to “riscv”.
  - Added 64-bit QEMU support.
  - Added DeviceTree bindings for RISC-V memory devices, CPU interrupt
    controllers, and platform-local interrupt controllers.

## Boards & SoC Support

- Added native\_posix\_64: A 64 bit variant of native\_posix
- Added support for these ARC boards:

  - emsdp
  - hsdk
  - nsim for hs
- Added support for these ARM boards:

  - atsamr21\_xpro
  - cc1352r1\_launchxl
  - cc26x2r1\_launchxl
  - holyiot\_yj16019
  - lpcxpresso55s69
  - mec15xxevb\_assy6853
  - mikroe\_mini\_m4\_for\_stm32
  - mimxrt1015\_evk
  - mps2\_an521
  - nrf51\_pca10031
  - nrf52811\_pca10056
  - nucleo\_g071rb
  - nucleo\_wb55rg
  - qemu\_cortex\_r5
  - stm32h747i\_disco
  - stm32mp157c\_dk2
  - twr\_ke18f
  - v2m\_musca\_b1
  - 96b\_avenger96
  - 96b\_meerkat96
  - 96b\_wistrio
- Added support for these RISC-V boards:

  - hifive1\_revb
  - litex\_vexriscv
  - qemu\_riscv64
- Added support for the gpmrb x86 board
- Added support for these following shields:

  - frdm\_cr20a
  - link\_board\_can
  - sparkfun\_sara\_r4
  - wnc\_m14a2a
  - x\_nucleo\_iks01a3
- Removed support for these boards:

  - arduino\_101
  - arduino\_101\_sss
  - curie\_ble
  - galileo
  - quark\_d2000\_crb
  - quark\_se\_c1000\_devboard
  - quark\_se\_c1000\_ss\_devboard
  - quark\_se\_c1000\_ble
  - tinytile
  - x86\_jailhouse

## Drivers and Sensors

- ADC

  - Added API to support calibration
  - Enabled ADC on STM32WB
  - Removed Quark D2000 ADC driver
  - Added NXP ADC12 and SAM0 ADC drivers
  - Added ADC shell
- Audio

  - Added support for two microphones (stereo) in the mpxxdtyy driver
- CAN

  - Added support for canbus Ethernet translator
  - Added 6LoCAN implementation
  - Added MCP2515, NXP FlexCAN, and loopback drivers
  - Added CAN shell
- Clock Control

  - Added NXP Kinetis MCG, SCG, and PCC drivers
  - Added STM32H7, STM32L1X, and STM32WB support
  - Removed Quark SE driver
- Counter

  - Added optional flags to alarm configuration structure and extended set channel alarm flags
  - Added top\_value setting configuration structure to API
  - Enabled counter for STM32WB
  - Added NXP GPT, “CMOS” RTC, SiLabs RTCC, and SAM0 drivers
  - Removed Quark D2000 support from QMSI driver
- Display

  - Added ST7789V based LCD driver
  - Renamed ssd1673 driver to ssd16xx
  - Added framebuffer driver with multiboot support
  - Added support for Seeed 2.8” TFT touch shield v2.0
- DMA

  - Added API to retrieve runtime status
  - Added SAM0 DMAC driver
  - Removed Quark SE C1000 support from QMSI driver
- Entropy

  - Added TI CC13xx / CC26xx driver
- ESPI

  - Added Microchip XEC driver
- Ethernet

  - Added LiteEth driver
- Flash

  - Removed Quark SE C1000 driver
  - Removed support for Quark D2000 from QMSI driver
  - Added STM32G0XX and STM32WB support to STM32 driver
  - Added RV32M1 and native POSIX drivers
- GPIO

  - Added stm32f1x SWJ configuration
  - Removed Quark SE C1000 and D2000 support from DesignWare driver
  - Added support for STM32H7, STM32L1X, and STM32WB to STM32 driver
  - Added Microchip XEC and TI CC13x2 / CC26x2 drivers
  - Added HT16K33 LED driver
  - Added interrupt support to SAM0 driver
- Hardware Info

  - Added ESP32 and SAM0 drivers
- I2C

  - Added support for STM32MP1, STM32WB, and STM32L1X to STM32 driver
  - Added STM32F10X slave support
  - Added power management to nrf TWI and TWIM drivers
  - Added TI CC13xx / CC26xx, Microchip MEC, SAM0, and RV32M1 drivers
  - Rewrote DesignWare driver for PCI(e) support
- IEEE 802.15.4

  - Fixed KW41z fault and dBm mapping
- Interrupt Controller

  - Added initial support for ARC TCC
  - Added GIC400, LiteX, and SAM0 EIC drivers
  - Added support for STM32G0X, STM32H7, STM32WB, and STM32MP1 to STM32 driver
  - Removed MVIC driver
- IPM

  - Removed Quark SE driver
  - Added MHU and STM32 drivers
- LED

  - Added Holtek HT16K33 LED driver
- Modem

  - Introduced socket helper layer
  - Introduced command handler and UART interface driver layers
  - Introduced modem context helper driver
  - Added u-blox SARA-R4 modem driver
- Pinmux

  - Added SPI support to STM32MP1
  - Enabled ADC, PWM, I2C, and SPI pins on STM32WB
  - Added Microchip XEC and TI CC13x2 / CC26x2 drivers
- PWM

  - Added NXP PWM driver
  - Added support for STM32G0XX to STM32 driver
- Sensor

  - Added STTS751 temperature sensor driver
  - Added LSM6DSO and LPS22HH drivers
  - Renamed HDC1008 driver to ti\_hdc and added support for 1050 version
  - Added LED current, proximity pulse length, ALS, and proximity gain configurations to APDS9960 driver
  - Reworked temperature and acceleration conversions, and added interrupt handling in ADXL362 driver
  - Added BME680 driver and AMS ENS210 drivers
- Serial

  - Added Xilinx ZynqMP PS, LiteUART, and TI CC12x2 / CC26x2 drivers
  - Added support for virtual UARTS over RTT channels
  - Added support for STM32H7 to STM32 driver
  - Removed support for Quark D2000 from QMSI driver
  - Enabled interrupts in LPC driver
  - Implemented ASYNC API in SAM0 driver
  - Added PCI(e) support to NS16550 driver
- SPI

  - Added support for STM32MP1X and STM32WB to STM32 driver
  - Removed support for Quark SE C1000 from DesignWare driver
  - Added TI CC13xx / CC26xx driver
  - Implemented ASYNC API in SAM0 driver
- Timer

  - Added Xilinx ZynqMP PS ttc driver
  - Added support for SMP to ARC V2 driver
  - Added MEC1501 32 KHZ, local APIC timer, and LiteX drivers
  - Replaced native POSIX system timer driver with tickless support
  - Removed default selection of SYSTICK timer for ARM platforms
- USB

  - Added NXP EHCI driver
  - Implemented missing API functions in SAM0 driver
- WiFi

  - Implemented TCP listen/accept and UDP support in eswifi driver

## Networking

- Added support for [SOCKS5 proxy](https://en.wikipedia.org/wiki/SOCKS).
  See also [RFC1928](https://tools.ietf.org/html/rfc1928) for details.
- Added support for 6LoCAN, a 6Lo adaption layer for Controller Area Networks.
- Added support for [Point-to-Point Protocol (PPP)](../connectivity/networking/api/ppp.md#ppp).
- Added support for UpdateHub, an end-to-end solution for large scale
  over-the-air update of devices.
  See [UpdateHub.io](https://updatehub.io/) for details.
- Added support to automatically register network socket family.
- Added support for `getsockname()` function.
- Added SO\_PRIORITY support to `setsockopt()`
- Added support for VLAN tag stripping.
- Added IEEE 802.15.4 API for ACK configuration.
- Added dispatching support to SocketCAN sockets.
- Added user mode support to PTP clock API.
- Added user mode support to network interface address functions.
- Added AF\_NET\_MGMT socket address family support. This is for receiving network
  event information in user mode application.
- Added user mode support to `net_addr_ntop()` and `net_addr_pton()`
- Added support for sending network management events when DNS server is added
  or deleted.
- Added LiteEth Ethernet driver.
- Added support for `sendmsg()` API.
- Added [civetweb](https://civetweb.github.io/civetweb/) HTTP API support.
- Added LWM2M IPSO Accelerometer, Push Button, On/Off Switch and Buzzer object
  support.
- Added LWM2M Location and Connection Monitoring object support.
- Added network management L4 layer. The L4 management events are used
  when monitoring network connectivity.
- Allow net-mgmt API to pass information length to application.
- Removed network management L1 layer as it was never used.
- By default a network interface is set to UP when the device starts.
  If this is not desired, then it is possible to disable automatic start.
- Allow collecting network packet TX throughput times in the network stack.
  This information can be seen in net-shell.
- net-shell Ping command overhaul.
- Accept UDP packet with missing checksum.
- 6lo compression rework.
- Incoming connection handling refactoring.
- Network interface refactoring.
- IPv6 fragmentation fixes.
- TCP data length fixes if TCP options are present.
- SNTP client updates.
- Trickle timer re-init fixes.
- `getaddrinfo()` fixes.
- Fixes in DHCPv4, LWM2M, gPTP, and MQTT
- DNS fixes for non-compressed answers.
- mDNS and LLMNR resolver fixes.
- Ethernet ARP fixes.
- OpenThread updates and fixes.
- Network device driver fixes for:

  - Ethernet e1000
  - Ethernet enc28j60
  - Ethernet mcux
  - Ethernet stellaris
  - Ethernet gmac
  - Ethernet stm32
  - WiFi eswifi
  - IEEE 802.15.4 kw41z
  - IEEE 802.15.4 nrf5

## Bluetooth

- Host:

  - GATT: Added support for database hashes, Read Using Characteristic
    UUID, static services, disabling the dynamic database, and notifying
    and indicating by UUID
  - GATT: Simplified the bt\_gatt\_notify\_cb() API
  - GATT: Added additional attributes to the Device Information Service
  - GATT: Several protocol and database fixes
  - Settings: Transitioned to new optimized settings model and support for custom backends
  - Completed support for directed advertising and Out-Of-Band (OOB) pairing
  - Added support for fine-grained control of security establishment, including
    forcing a pairing procedure in case of key loss
  - Switched to separate, dedicated pools for discardable events and number of
    completed packets events
  - Extended and improved the Bluetooth shell with several commands
  - BLE qualification up to the 5.1 specification
  - BLE Mesh: Several fixes and improvements
- BLE split software Controller:

  - The split software Controller is now the default
  - Added support for the Data Length Update procedure
  - Improved and documented the ticker packet scheduler for improved conflict resolution
  - Added support for out-of-tree user-defined commands and events,
    Zephyr Vendor Specific Commands, and user-defined protocols
  - Converted several control procedures to be queueable
  - Nordic: Decorrelated address generation from resolution
  - Nordic: Added support for Controller-based privacy, fast encryption
    setup, RSSI, low-latency ULL processing of messages, nRF52811 IC BLE
    radio, PA/LNA on Port 1 GPIO pins, and radio event abort
  - BLE qualification up to the 5.1 specification
- BLE legacy software Controller:

  - BLE qualification up to the 5.1 specification
  - Multiple control procedures fixes and improvements

## Build and Infrastructure

- The devicetree Python scripts have been rewritten to be more robust and
  easier to understand and change. The new scripts are these three files:

  - [scripts/dts/dtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/dtlib.py) – a low-level `.dts` parsing
    library
  - [scripts/dts/edtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/edtlib.py) – a higher-level library that adds
    information from bindings
  - [scripts/dts/gen\_defines.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/gen_defines.py) – generates a C header from the
    devicetree files for the board

  The new scripts verify `category: optional/required` and `type:` settings
  given in bindings for nodes, and add some new types, like `phandle-array`.
  Error messages and other output is now more helpful.

  See the updated documentation in [dts/binding-template.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/binding-template.yaml).

  The old scripts are kept around to generate a few deprecated `#define`s.
  They will be removed in the Zephyr 2.2 release.
- Changed ARM Embedded toolchain to default to nano variant of newlib

## Libraries / Subsystems

- File Systems: Added support for littlefs

## HALs

- HALs are now moved out of the main tree as external modules and reside
  in their own standalone repositories.

## Documentation

- We’ve made many updates to component, subsystem, and process
  documentation bringing our documentation up-to-date with code changes,
  additions, and improvements, as well as new supported boards and
  samples.

## Tests and Samples

- We have implemented additional tests and significantly expanded the
  amount of test cases in existing tests to increase code coverage.

## Issue Related Items

These GitHub issues were addressed since the previous 1.14.0 tagged
release:

- [GitHub #18964](https://github.com/zephyrproject-rtos/zephyr/issues/18964) - [Coverity CID :203911]Memory - corruptions in /tests/bluetooth/uuid/src/main.c
- [GitHub #18963](https://github.com/zephyrproject-rtos/zephyr/issues/18963) - [Coverity CID :203910]Memory - corruptions in /tests/bluetooth/uuid/src/main.c
- [GitHub #18959](https://github.com/zephyrproject-rtos/zephyr/issues/18959) - [Coverity CID :203907]Parse warnings in /include/bluetooth/conn.h
- [GitHub #18923](https://github.com/zephyrproject-rtos/zephyr/issues/18923) - (BLE) Dynamic TX Power Control
- [GitHub #18906](https://github.com/zephyrproject-rtos/zephyr/issues/18906) - Problem on build when calling objcopy to generate isrList.bin
- [GitHub #18865](https://github.com/zephyrproject-rtos/zephyr/issues/18865) - Fatal Usage Fault When Bluetooth And OpenThread Are Enabled On NRF52840 Multiprotocol Support
- [GitHub #18828](https://github.com/zephyrproject-rtos/zephyr/issues/18828) - Bluetooth: controller: crash terminating link during encryption procedure
- [GitHub #18821](https://github.com/zephyrproject-rtos/zephyr/issues/18821) - Documentation: parent vs child in DeviceTree nodes
- [GitHub #18819](https://github.com/zephyrproject-rtos/zephyr/issues/18819) - Bluetooth: LL split assert upon disconnection
- [GitHub #18814](https://github.com/zephyrproject-rtos/zephyr/issues/18814) - Module Request: LoRaMac-Node
- [GitHub #18813](https://github.com/zephyrproject-rtos/zephyr/issues/18813) - fs: nvs: Cannot delete entries
- [GitHub #18808](https://github.com/zephyrproject-rtos/zephyr/issues/18808) - Docs for gpmrb board incorrectly refer to up\_squared board
- [GitHub #18804](https://github.com/zephyrproject-rtos/zephyr/issues/18804) - Channel Selection Algorithm Modification In Zephyr
- [GitHub #18802](https://github.com/zephyrproject-rtos/zephyr/issues/18802) - Bluetooth: UUID: Missing tests and confusing documentation
- [GitHub #18799](https://github.com/zephyrproject-rtos/zephyr/issues/18799) - bt\_uuid\_create\_le() and bt\_uuid\_create() have endianness issues, and only one of them is needed
- [GitHub #18795](https://github.com/zephyrproject-rtos/zephyr/issues/18795) - FS:NVS: garbage collection when restart
- [GitHub #18784](https://github.com/zephyrproject-rtos/zephyr/issues/18784) - Can not build link\_board\_can shield
- [GitHub #18774](https://github.com/zephyrproject-rtos/zephyr/issues/18774) - (nRF51) NVS example doesn’t work
- [GitHub #18765](https://github.com/zephyrproject-rtos/zephyr/issues/18765) - LwM2M: DNS handling via offload socket API is broken
- [GitHub #18760](https://github.com/zephyrproject-rtos/zephyr/issues/18760) - hello\_world sample instructions don’t work
- [GitHub #18739](https://github.com/zephyrproject-rtos/zephyr/issues/18739) - k\_uptime\_get\_32() does not behave as documented
- [GitHub #18732](https://github.com/zephyrproject-rtos/zephyr/issues/18732) - net: mDNS name resolving issue between 2 Zephyr nodes
- [GitHub #18726](https://github.com/zephyrproject-rtos/zephyr/issues/18726) - arc: should not rely on that ERET has a copy of ilink
- [GitHub #18725](https://github.com/zephyrproject-rtos/zephyr/issues/18725) - arc: the IRM bit of SEC\_STAT is not handled corrected
- [GitHub #18724](https://github.com/zephyrproject-rtos/zephyr/issues/18724) - arc: interrupt stack is not switched correctly
- [GitHub #18717](https://github.com/zephyrproject-rtos/zephyr/issues/18717) - USB broken on disco l475 iot board
- [GitHub #18705](https://github.com/zephyrproject-rtos/zephyr/issues/18705) - SMP fails to allocate buffer and pairing times out
- [GitHub #18693](https://github.com/zephyrproject-rtos/zephyr/issues/18693) - POSIX: Some headers were missing from PR #16621
- [GitHub #18687](https://github.com/zephyrproject-rtos/zephyr/issues/18687) - [Coverity CID :203623]Memory - illegal accesses in /tests/subsys/settings/fcb\_init/src/settings\_test\_fcb\_init.c
- [GitHub #18686](https://github.com/zephyrproject-rtos/zephyr/issues/18686) - [Coverity CID :203622]Parse warnings in /opt/zephyr-sdk-0.10.3/nios2-zephyr-elf/nios2-zephyr-elf/include/c++/8.3.0/bits/refwrap.h
- [GitHub #18685](https://github.com/zephyrproject-rtos/zephyr/issues/18685) - [Coverity CID :203621]Parse warnings in /opt/zephyr-sdk-0.10.3/nios2-zephyr-elf/nios2-zephyr-elf/include/c++/8.3.0/bits/refwrap.h
- [GitHub #18684](https://github.com/zephyrproject-rtos/zephyr/issues/18684) - [Coverity CID :203620]Parse warnings in /opt/zephyr-sdk-0.10.3/nios2-zephyr-elf/nios2-zephyr-elf/include/c++/8.3.0/bits/refwrap.h
- [GitHub #18683](https://github.com/zephyrproject-rtos/zephyr/issues/18683) - [Coverity CID :190988]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/drivers/imx/fsl\_elcdif.c
- [GitHub #18682](https://github.com/zephyrproject-rtos/zephyr/issues/18682) - [Coverity CID :190984]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/drivers/imx/fsl\_elcdif.c
- [GitHub #18681](https://github.com/zephyrproject-rtos/zephyr/issues/18681) - [Coverity CID :190979]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/drivers/imx/fsl\_elcdif.c
- [GitHub #18680](https://github.com/zephyrproject-rtos/zephyr/issues/18680) - [Coverity CID :190959]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/drivers/imx/fsl\_elcdif.c
- [GitHub #18679](https://github.com/zephyrproject-rtos/zephyr/issues/18679) - [Coverity CID :198643]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MKE18F16/fsl\_clock.c
- [GitHub #18678](https://github.com/zephyrproject-rtos/zephyr/issues/18678) - [Coverity CID :198642]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MKE18F16/fsl\_clock.c
- [GitHub #18677](https://github.com/zephyrproject-rtos/zephyr/issues/18677) - [Coverity CID :198641]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MKE18F16/fsl\_clock.c
- [GitHub #18676](https://github.com/zephyrproject-rtos/zephyr/issues/18676) - [Coverity CID :190994]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MK64F12/fsl\_clock.c
- [GitHub #18675](https://github.com/zephyrproject-rtos/zephyr/issues/18675) - [Coverity CID :190982]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MK64F12/fsl\_clock.c
- [GitHub #18674](https://github.com/zephyrproject-rtos/zephyr/issues/18674) - [Coverity CID :190962]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MK64F12/fsl\_clock.c
- [GitHub #18673](https://github.com/zephyrproject-rtos/zephyr/issues/18673) - [Coverity CID :190947]Incorrect expression in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/MK64F12/fsl\_clock.c
- [GitHub #18672](https://github.com/zephyrproject-rtos/zephyr/issues/18672) - [Coverity CID :198948]Control flow issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/LPC55S69/fsl\_clock.c
- [GitHub #18671](https://github.com/zephyrproject-rtos/zephyr/issues/18671) - [Coverity CID :198947]Integer handling issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/LPC55S69/fsl\_clock.c
- [GitHub #18670](https://github.com/zephyrproject-rtos/zephyr/issues/18670) - [Coverity CID :182600]Integer handling issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/devices/LPC54114/fsl\_clock.c
- [GitHub #18669](https://github.com/zephyrproject-rtos/zephyr/issues/18669) - [Coverity CID :158891]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nxp/mcux/components/phyksz8081/fsl\_phy.c
- [GitHub #18668](https://github.com/zephyrproject-rtos/zephyr/issues/18668) - [Coverity CID :203544]Integer handling issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nordic/nrfx/drivers/src/nrfx\_usbd.c
- [GitHub #18667](https://github.com/zephyrproject-rtos/zephyr/issues/18667) - [Coverity CID :203513]Integer handling issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nordic/nrfx/drivers/src/nrfx\_usbd.c
- [GitHub #18666](https://github.com/zephyrproject-rtos/zephyr/issues/18666) - [Coverity CID :203506]Integer handling issues in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nordic/nrfx/drivers/src/nrfx\_usbd.c
- [GitHub #18665](https://github.com/zephyrproject-rtos/zephyr/issues/18665) - [Coverity CID :203436]Memory - illegal accesses in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/hal/nordic/nrfx/drivers/src/nrfx\_usbd.c
- [GitHub #18664](https://github.com/zephyrproject-rtos/zephyr/issues/18664) - [Coverity CID :203416]Uninitialized variables in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/fs/littlefs/lfs.c
- [GitHub #18663](https://github.com/zephyrproject-rtos/zephyr/issues/18663) - [Coverity CID :203413]Null pointer dereferences in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/fs/littlefs/lfs.c
- [GitHub #18662](https://github.com/zephyrproject-rtos/zephyr/issues/18662) - [Coverity CID :61908]Insecure data handling in /home/aasthagr/zephyrproject-external-coverity-new/zephyrproject/modules/crypto/mbedtls/library/ssl\_tls.c
- [GitHub #18658](https://github.com/zephyrproject-rtos/zephyr/issues/18658) - Bluetooth BR/EDR encryption key negotiation vulnerability
- [GitHub #18654](https://github.com/zephyrproject-rtos/zephyr/issues/18654) - cc3220sf\_launchxl fails tests/kernel/interrupt/arch.interrupt
- [GitHub #18645](https://github.com/zephyrproject-rtos/zephyr/issues/18645) - Disconnect because of data packets during encryption procedure
- [GitHub #18615](https://github.com/zephyrproject-rtos/zephyr/issues/18615) - sam e70 xplained failed to build hello world
- [GitHub #18599](https://github.com/zephyrproject-rtos/zephyr/issues/18599) - tests/kernel/fifo/fifo\_timeout fails on cc3220sf\_launchxl
- [GitHub #18598](https://github.com/zephyrproject-rtos/zephyr/issues/18598) - tests/net/trickle failed on multiple plartforms
- [GitHub #18595](https://github.com/zephyrproject-rtos/zephyr/issues/18595) - USB CDC endless loop with BLE on NRF52
- [GitHub #18593](https://github.com/zephyrproject-rtos/zephyr/issues/18593) - tests/arch/arm/arm\_zero\_latency\_irqs fails on cc3220sf\_launchxl
- [GitHub #18592](https://github.com/zephyrproject-rtos/zephyr/issues/18592) - (nRF51) The RSSI signal does not rise above -44 dBm
- [GitHub #18590](https://github.com/zephyrproject-rtos/zephyr/issues/18590) - tests/kernel/fatal/kernel.common.stack\_sentinel fails on FRDM-KW41Z
- [GitHub #18587](https://github.com/zephyrproject-rtos/zephyr/issues/18587) - tests/kernel/fifo/fifo\_timeout/kernel.fifo.timeout fails to run on lpcxpresso54114\_m4
- [GitHub #18584](https://github.com/zephyrproject-rtos/zephyr/issues/18584) - BT LL assert on LL/CON/ADV/BV-04-C
- [GitHub #18580](https://github.com/zephyrproject-rtos/zephyr/issues/18580) - Bluetooth: Security fail on initial pairing
- [GitHub #18574](https://github.com/zephyrproject-rtos/zephyr/issues/18574) - Some platforms: “reel\_board”, “frdm\_k64f” and “sam\_e70\_xplained” are be built failure
- [GitHub #18572](https://github.com/zephyrproject-rtos/zephyr/issues/18572) - Bluetooth: GATT: Unable to indicate by UUID
- [GitHub #18563](https://github.com/zephyrproject-rtos/zephyr/issues/18563) - log\_strdup missing error messages seen when running wifi sample
- [GitHub #18547](https://github.com/zephyrproject-rtos/zephyr/issues/18547) - Bluetooth: GATT: Fix using variable size storage for CCC
- [GitHub #18546](https://github.com/zephyrproject-rtos/zephyr/issues/18546) - Hard Fault when connecting to BLE device
- [GitHub #18524](https://github.com/zephyrproject-rtos/zephyr/issues/18524) - No disconnection event during “heavy” indication stream
- [GitHub #18522](https://github.com/zephyrproject-rtos/zephyr/issues/18522) - BLE: Mesh: When transport send seg\_msg to LPN
- [GitHub #18521](https://github.com/zephyrproject-rtos/zephyr/issues/18521) - BLE: Mesh: when friend send msg to LPN
- [GitHub #18508](https://github.com/zephyrproject-rtos/zephyr/issues/18508) - tests/net/trickle failed on frdm\_k64f board
- [GitHub #18476](https://github.com/zephyrproject-rtos/zephyr/issues/18476) - Custom module with west
- [GitHub #18462](https://github.com/zephyrproject-rtos/zephyr/issues/18462) - potential buffer overrun in logging infrastructure
- [GitHub #18461](https://github.com/zephyrproject-rtos/zephyr/issues/18461) - [Coverity CID :203487]Parse warnings in /usr/lib/gcc/x86\_64-redhat-linux/8/include/stdint-gcc.h
- [GitHub #18460](https://github.com/zephyrproject-rtos/zephyr/issues/18460) - [Coverity CID :203527]Parse warnings in /usr/include/unistd.h
- [GitHub #18459](https://github.com/zephyrproject-rtos/zephyr/issues/18459) - [Coverity CID :203509]Null pointer dereferences in /tests/subsys/usb/desc\_sections/src/desc\_sections.c
- [GitHub #18458](https://github.com/zephyrproject-rtos/zephyr/issues/18458) - [Coverity CID :203422]Memory - illegal accesses in /tests/subsys/fs/littlefs/src/testfs\_util.c
- [GitHub #18457](https://github.com/zephyrproject-rtos/zephyr/issues/18457) - [Coverity CID :203419]Security best practices violations in /tests/net/traffic\_class/src/main.c
- [GitHub #18456](https://github.com/zephyrproject-rtos/zephyr/issues/18456) - [Coverity CID :203401]Security best practices violations in /tests/net/traffic\_class/src/main.c
- [GitHub #18455](https://github.com/zephyrproject-rtos/zephyr/issues/18455) - [Coverity CID :203490]Error handling issues in /tests/net/socket/net\_mgmt/src/main.c
- [GitHub #18454](https://github.com/zephyrproject-rtos/zephyr/issues/18454) - [Coverity CID :203499]Null pointer dereferences in /tests/net/icmpv6/src/main.c
- [GitHub #18453](https://github.com/zephyrproject-rtos/zephyr/issues/18453) - [Coverity CID :203480]Null pointer dereferences in /tests/net/context/src/main.c
- [GitHub #18446](https://github.com/zephyrproject-rtos/zephyr/issues/18446) - [Coverity CID :203532]Incorrect expression in /tests/kernel/sched/schedule\_api/src/user\_api.c
- [GitHub #18445](https://github.com/zephyrproject-rtos/zephyr/issues/18445) - [Coverity CID :203507]Error handling issues in /tests/kernel/mutex/sys\_mutex/src/main.c
- [GitHub #18444](https://github.com/zephyrproject-rtos/zephyr/issues/18444) - [Coverity CID :203516]Memory - corruptions in /tests/kernel/mem\_protect/userspace/src/main.c
- [GitHub #18443](https://github.com/zephyrproject-rtos/zephyr/issues/18443) - [Coverity CID :203454]Error handling issues in /tests/kernel/mem\_protect/sys\_sem/src/main.c
- [GitHub #18442](https://github.com/zephyrproject-rtos/zephyr/issues/18442) - [Coverity CID :203465]Memory - corruptions in /tests/kernel/mem\_protect/protection/src/main.c
- [GitHub #18439](https://github.com/zephyrproject-rtos/zephyr/issues/18439) - [Coverity CID :203437]Incorrect expression in /tests/kernel/fp\_sharing/float\_disable/src/k\_float\_disable.c
- [GitHub #18438](https://github.com/zephyrproject-rtos/zephyr/issues/18438) - [Coverity CID :203407]Incorrect expression in /tests/kernel/fp\_sharing/float\_disable/src/k\_float\_disable.c
- [GitHub #18437](https://github.com/zephyrproject-rtos/zephyr/issues/18437) - [Coverity CID :203478]Program hangs in /tests/kernel/common/src/sflist.c
- [GitHub #18436](https://github.com/zephyrproject-rtos/zephyr/issues/18436) - [Coverity CID :203424]Control flow issues in /tests/kernel/common/src/sflist.c
- [GitHub #18434](https://github.com/zephyrproject-rtos/zephyr/issues/18434) - [Coverity CID :203486]Memory - corruptions in /tests/bluetooth/uuid/src/main.c
- [GitHub #18433](https://github.com/zephyrproject-rtos/zephyr/issues/18433) - [Coverity CID :203431]Memory - corruptions in /tests/bluetooth/uuid/src/main.c
- [GitHub #18432](https://github.com/zephyrproject-rtos/zephyr/issues/18432) - [Coverity CID :203502]Error handling issues in /tests/bluetooth/tester/src/gap.c
- [GitHub #18431](https://github.com/zephyrproject-rtos/zephyr/issues/18431) - [Coverity CID :203391]Null pointer dereferences in /tests/bluetooth/gatt/src/main.c
- [GitHub #18430](https://github.com/zephyrproject-rtos/zephyr/issues/18430) - [Coverity CID :203540]Incorrect expression in /tests/arch/arm/arm\_zero\_latency\_irqs/src/arm\_zero\_latency\_irqs.c
- [GitHub #18429](https://github.com/zephyrproject-rtos/zephyr/issues/18429) - [Coverity CID :203525]Incorrect expression in /tests/arch/arm/arm\_thread\_swap/src/arm\_thread\_arch.c
- [GitHub #18428](https://github.com/zephyrproject-rtos/zephyr/issues/18428) - [Coverity CID :203479]Incorrect expression in /tests/arch/arm/arm\_thread\_swap/src/arm\_thread\_arch.c
- [GitHub #18427](https://github.com/zephyrproject-rtos/zephyr/issues/18427) - [Coverity CID :203392]Incorrect expression in /tests/arch/arm/arm\_thread\_swap/src/arm\_thread\_arch.c
- [GitHub #18426](https://github.com/zephyrproject-rtos/zephyr/issues/18426) - [Coverity CID :203455]Incorrect expression in /tests/arch/arm/arm\_ramfunc/src/arm\_ramfunc.c
- [GitHub #18424](https://github.com/zephyrproject-rtos/zephyr/issues/18424) - [Coverity CID :203489]Memory - corruptions in /tests/application\_development/gen\_inc\_file/src/main.c
- [GitHub #18423](https://github.com/zephyrproject-rtos/zephyr/issues/18423) - [Coverity CID :203473]Null pointer dereferences in /subsys/usb/usb\_descriptor.c
- [GitHub #18421](https://github.com/zephyrproject-rtos/zephyr/issues/18421) - [Coverity CID :203504]Uninitialized variables in /subsys/net/lib/sockets/sockets\_net\_mgmt.c
- [GitHub #18420](https://github.com/zephyrproject-rtos/zephyr/issues/18420) - [Coverity CID :203468]Control flow issues in /subsys/net/lib/sockets/sockets\_net\_mgmt.c
- [GitHub #18419](https://github.com/zephyrproject-rtos/zephyr/issues/18419) - [Coverity CID :203397]Control flow issues in /subsys/net/lib/sockets/sockets\_net\_mgmt.c
- [GitHub #18418](https://github.com/zephyrproject-rtos/zephyr/issues/18418) - [Coverity CID :203445]Error handling issues in /subsys/net/lib/sockets/getnameinfo.c
- [GitHub #18417](https://github.com/zephyrproject-rtos/zephyr/issues/18417) - [Coverity CID :203501]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_timer.c
- [GitHub #18416](https://github.com/zephyrproject-rtos/zephyr/issues/18416) - [Coverity CID :203475]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_timer.c
- [GitHub #18415](https://github.com/zephyrproject-rtos/zephyr/issues/18415) - [Coverity CID :203420]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_timer.c
- [GitHub #18414](https://github.com/zephyrproject-rtos/zephyr/issues/18414) - [Coverity CID :203496]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_push\_button.c
- [GitHub #18413](https://github.com/zephyrproject-rtos/zephyr/issues/18413) - [Coverity CID :203488]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_push\_button.c
- [GitHub #18412](https://github.com/zephyrproject-rtos/zephyr/issues/18412) - [Coverity CID :203482]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_push\_button.c
- [GitHub #18411](https://github.com/zephyrproject-rtos/zephyr/issues/18411) - [Coverity CID :203450]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_onoff\_switch.c
- [GitHub #18410](https://github.com/zephyrproject-rtos/zephyr/issues/18410) - [Coverity CID :203448]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_onoff\_switch.c
- [GitHub #18409](https://github.com/zephyrproject-rtos/zephyr/issues/18409) - [Coverity CID :203427]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_onoff\_switch.c
- [GitHub #18408](https://github.com/zephyrproject-rtos/zephyr/issues/18408) - [Coverity CID :203533]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_light\_control.c
- [GitHub #18407](https://github.com/zephyrproject-rtos/zephyr/issues/18407) - [Coverity CID :203519]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_light\_control.c
- [GitHub #18406](https://github.com/zephyrproject-rtos/zephyr/issues/18406) - [Coverity CID :203511]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_buzzer.c
- [GitHub #18405](https://github.com/zephyrproject-rtos/zephyr/issues/18405) - [Coverity CID :203426]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_buzzer.c
- [GitHub #18404](https://github.com/zephyrproject-rtos/zephyr/issues/18404) - [Coverity CID :203414]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_buzzer.c
- [GitHub #18403](https://github.com/zephyrproject-rtos/zephyr/issues/18403) - [Coverity CID :203539]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_accelerometer.c
- [GitHub #18402](https://github.com/zephyrproject-rtos/zephyr/issues/18402) - [Coverity CID :203530]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_accelerometer.c
- [GitHub #18401](https://github.com/zephyrproject-rtos/zephyr/issues/18401) - [Coverity CID :203438]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_accelerometer.c
- [GitHub #18400](https://github.com/zephyrproject-rtos/zephyr/issues/18400) - [Coverity CID :203483]Control flow issues in /subsys/net/lib/conn\_mgr/events\_handler.c
- [GitHub #18399](https://github.com/zephyrproject-rtos/zephyr/issues/18399) - [Coverity CID :203457]Control flow issues in /subsys/net/l2/ppp/lcp.c
- [GitHub #18398](https://github.com/zephyrproject-rtos/zephyr/issues/18398) - [Coverity CID :203514]Control flow issues in /subsys/net/l2/ppp/ipv6cp.c
- [GitHub #18397](https://github.com/zephyrproject-rtos/zephyr/issues/18397) - [Coverity CID :203512]Memory - corruptions in /subsys/net/l2/ppp/ipv6cp.c
- [GitHub #18396](https://github.com/zephyrproject-rtos/zephyr/issues/18396) - [Coverity CID :203435]Error handling issues in /subsys/net/l2/ppp/fsm.c
- [GitHub #18395](https://github.com/zephyrproject-rtos/zephyr/issues/18395) - [Coverity CID :203471]Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #18394](https://github.com/zephyrproject-rtos/zephyr/issues/18394) - [Coverity CID :203464]Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #18393](https://github.com/zephyrproject-rtos/zephyr/issues/18393) - [Coverity CID :203541]Integer handling issues in /subsys/net/ip/6lo.c
- [GitHub #18392](https://github.com/zephyrproject-rtos/zephyr/issues/18392) - [Coverity CID :203494]Integer handling issues in /subsys/fs/littlefs\_fs.c
- [GitHub #18391](https://github.com/zephyrproject-rtos/zephyr/issues/18391) - [Coverity CID :203403]Memory - corruptions in /subsys/disk/disk\_access\_usdhc.c
- [GitHub #18390](https://github.com/zephyrproject-rtos/zephyr/issues/18390) - [Coverity CID :203441]Null pointer dereferences in /subsys/bluetooth/mesh/transport.c
- [GitHub #18389](https://github.com/zephyrproject-rtos/zephyr/issues/18389) - [Coverity CID :203396]Null pointer dereferences in /subsys/bluetooth/mesh/access.c
- [GitHub #18388](https://github.com/zephyrproject-rtos/zephyr/issues/18388) - [Coverity CID :203545]Memory - corruptions in /subsys/bluetooth/host/smp.c
- [GitHub #18387](https://github.com/zephyrproject-rtos/zephyr/issues/18387) - [Coverity CID :203536]Memory - corruptions in /subsys/bluetooth/host/smp.c
- [GitHub #18385](https://github.com/zephyrproject-rtos/zephyr/issues/18385) - [Coverity CID :203534]Memory - corruptions in /subsys/bluetooth/host/hci\_core.c
- [GitHub #18384](https://github.com/zephyrproject-rtos/zephyr/issues/18384) - [Coverity CID :203495]Control flow issues in /subsys/bluetooth/host/gatt.c
- [GitHub #18383](https://github.com/zephyrproject-rtos/zephyr/issues/18383) - [Coverity CID :203447]Memory - corruptions in /subsys/bluetooth/host/att.c
- [GitHub #18382](https://github.com/zephyrproject-rtos/zephyr/issues/18382) - [Coverity CID :203524]Incorrect expression in /subsys/bluetooth/controller/ticker/ticker.c
- [GitHub #18381](https://github.com/zephyrproject-rtos/zephyr/issues/18381) - [Coverity CID :203393]Control flow issues in /subsys/bluetooth/controller/ll\_sw/ull\_conn.c
- [GitHub #18380](https://github.com/zephyrproject-rtos/zephyr/issues/18380) - [Coverity CID :203461]Null pointer dereferences in /subsys/bluetooth/controller/ll\_sw/ull.c
- [GitHub #18379](https://github.com/zephyrproject-rtos/zephyr/issues/18379) - [Coverity CID :203493]Control flow issues in /soc/arm/st\_stm32/stm32h7/soc\_m7.c
- [GitHub #18377](https://github.com/zephyrproject-rtos/zephyr/issues/18377) - [Coverity CID :203535]Error handling issues in /samples/net/sockets/civetweb/src/main.c
- [GitHub #18376](https://github.com/zephyrproject-rtos/zephyr/issues/18376) - [Coverity CID :203462]Error handling issues in /samples/net/sockets/civetweb/src/main.c
- [GitHub #18375](https://github.com/zephyrproject-rtos/zephyr/issues/18375) - [Coverity CID :203440]Null pointer dereferences in /samples/net/nats/src/main.c
- [GitHub #18374](https://github.com/zephyrproject-rtos/zephyr/issues/18374) - [Coverity CID :203523]Error handling issues in /samples/drivers/counter/alarm/src/main.c
- [GitHub #18372](https://github.com/zephyrproject-rtos/zephyr/issues/18372) - [Coverity CID :203543]Memory - illegal accesses in /samples/bluetooth/eddystone/src/main.c
- [GitHub #18371](https://github.com/zephyrproject-rtos/zephyr/issues/18371) - [Coverity CID :203542]Error handling issues in /lib/posix/pthread.c
- [GitHub #18370](https://github.com/zephyrproject-rtos/zephyr/issues/18370) - [Coverity CID :203469]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #18369](https://github.com/zephyrproject-rtos/zephyr/issues/18369) - [Coverity CID :203425]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #18368](https://github.com/zephyrproject-rtos/zephyr/issues/18368) - [Coverity CID :203411]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #18367](https://github.com/zephyrproject-rtos/zephyr/issues/18367) - [Coverity CID :203409]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #18366](https://github.com/zephyrproject-rtos/zephyr/issues/18366) - [Coverity CID :203452]Control flow issues in /drivers/timer/xlnx\_psttc\_timer.c
- [GitHub #18365](https://github.com/zephyrproject-rtos/zephyr/issues/18365) - [Coverity CID :203434]Control flow issues in /drivers/timer/xlnx\_psttc\_timer.c
- [GitHub #18364](https://github.com/zephyrproject-rtos/zephyr/issues/18364) - [Coverity CID :203467]Memory - corruptions in /drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #18363](https://github.com/zephyrproject-rtos/zephyr/issues/18363) - [Coverity CID :203492]Memory - corruptions in /drivers/net/ppp.c
- [GitHub #18362](https://github.com/zephyrproject-rtos/zephyr/issues/18362) - [Coverity CID :203412]Control flow issues in /drivers/net/ppp.c
- [GitHub #18361](https://github.com/zephyrproject-rtos/zephyr/issues/18361) - [Coverity CID :203515]Uninitialized variables in /drivers/flash/flash\_stm32l4x.c
- [GitHub #18360](https://github.com/zephyrproject-rtos/zephyr/issues/18360) - [Coverity CID :203531]Memory - corruptions in /drivers/espi/espi\_mchp\_xec.c
- [GitHub #18359](https://github.com/zephyrproject-rtos/zephyr/issues/18359) - [Coverity CID :203521]Memory - illegal accesses in /drivers/espi/espi\_mchp\_xec.c
- [GitHub #18358](https://github.com/zephyrproject-rtos/zephyr/issues/18358) - [Coverity CID :203497]Memory - corruptions in /drivers/espi/espi\_mchp\_xec.c
- [GitHub #18357](https://github.com/zephyrproject-rtos/zephyr/issues/18357) - [Coverity CID :203485]Memory - illegal accesses in /drivers/espi/espi\_mchp\_xec.c
- [GitHub #18356](https://github.com/zephyrproject-rtos/zephyr/issues/18356) - [Coverity CID :203430]Integer handling issues in /drivers/espi/espi\_mchp\_xec.c
- [GitHub #18355](https://github.com/zephyrproject-rtos/zephyr/issues/18355) - [Coverity CID :203466]Memory - illegal accesses in /drivers/can/can\_mcux\_flexcan.c
- [GitHub #18354](https://github.com/zephyrproject-rtos/zephyr/issues/18354) - [Coverity CID :203449]Memory - illegal accesses in /boards/posix/native\_posix/cmdline\_common.c
- [GitHub #18353](https://github.com/zephyrproject-rtos/zephyr/issues/18353) - [Coverity CID :203522]Null pointer dereferences in /arch/arm/core/cortex\_m/fault.c
- [GitHub #18352](https://github.com/zephyrproject-rtos/zephyr/issues/18352) - devicetree: support multiple values in io-channels
- [GitHub #18334](https://github.com/zephyrproject-rtos/zephyr/issues/18334) - DNS resolution is broken for some addresses in master/2.0-pre
- [GitHub #18326](https://github.com/zephyrproject-rtos/zephyr/issues/18326) - Bluetooth: Mesh: LPN: Remove msg from cache on rejection Enhancement
- [GitHub #18320](https://github.com/zephyrproject-rtos/zephyr/issues/18320) - tests/drivers/can/api/peripheral.can fail on FRDM-K64F
- [GitHub #18306](https://github.com/zephyrproject-rtos/zephyr/issues/18306) - Unable to reconnect paired devices with controller privacy disabled (host privacy enabled)
- [GitHub #18301](https://github.com/zephyrproject-rtos/zephyr/issues/18301) - menuconfig target can corrupt build configuration
- [GitHub #18298](https://github.com/zephyrproject-rtos/zephyr/issues/18298) - Unable to build mesh-demo for BBC micro:bit
- [GitHub #18292](https://github.com/zephyrproject-rtos/zephyr/issues/18292) - tests/net/lib/dns\_addremove failed on frdm\_k64f board.
- [GitHub #18284](https://github.com/zephyrproject-rtos/zephyr/issues/18284) - tests/kernel/fp\_sharing/float\_disable and tests/kernel/mutex/mutex\_api and tests/kernel/sleep fails on twr\_ke18f
- [GitHub #18283](https://github.com/zephyrproject-rtos/zephyr/issues/18283) - tests/crypto/tinycrypt\_hmac\_prng and tests/crypto/mbedtls and tests/posix/fs build failure on mimxrt1015\_evk
- [GitHub #18281](https://github.com/zephyrproject-rtos/zephyr/issues/18281) - tests/kernel/mem\_protect/protection fails on LPC54114\_m4
- [GitHub #18272](https://github.com/zephyrproject-rtos/zephyr/issues/18272) - xtensa ASM2 has no support for dynamic interrupts
- [GitHub #18269](https://github.com/zephyrproject-rtos/zephyr/issues/18269) - Documentation improvement for macOS
- [GitHub #18263](https://github.com/zephyrproject-rtos/zephyr/issues/18263) - flash sector erase fails on stm32f412
- [GitHub #18261](https://github.com/zephyrproject-rtos/zephyr/issues/18261) - CONFIG\_TIMESLICING=n breaks kernel
- [GitHub #18258](https://github.com/zephyrproject-rtos/zephyr/issues/18258) - sys\_get\_be64() is missing from sys/byteorder.h
- [GitHub #18253](https://github.com/zephyrproject-rtos/zephyr/issues/18253) - Network samples echo\_client doesn’t work if only IPv4 enabled.
- [GitHub #18246](https://github.com/zephyrproject-rtos/zephyr/issues/18246) - Build failures with current tree
- [GitHub #18238](https://github.com/zephyrproject-rtos/zephyr/issues/18238) - drivers/modem/modem\_socket: modem\_socket\_put() sock\_fd parameter not handled correctly
- [GitHub #18232](https://github.com/zephyrproject-rtos/zephyr/issues/18232) - drivers: can: mcux: TX callback and can\_detach don’t work propperly
- [GitHub #18231](https://github.com/zephyrproject-rtos/zephyr/issues/18231) - MCUBoot not cleaning up properly before booting Zephyr?
- [GitHub #18228](https://github.com/zephyrproject-rtos/zephyr/issues/18228) - stm32h747i\_disco: Fix SYS\_CLOCK\_TICKS\_PER\_SEC
- [GitHub #18212](https://github.com/zephyrproject-rtos/zephyr/issues/18212) - README file missing for civetweb sample
- [GitHub #18205](https://github.com/zephyrproject-rtos/zephyr/issues/18205) - tests/net/socket/udp fails when code coverage is enabled on qemu\_x86
- [GitHub #18202](https://github.com/zephyrproject-rtos/zephyr/issues/18202) - Disable Duplicate scan, no longer available
- [GitHub #18201](https://github.com/zephyrproject-rtos/zephyr/issues/18201) - bug: west flash with –hex-file param used to work w/o path specified
- [GitHub #18198](https://github.com/zephyrproject-rtos/zephyr/issues/18198) - SDK 0.10.2 rv32m1\_vega samples/subsys/logging/logger build fails
- [GitHub #18194](https://github.com/zephyrproject-rtos/zephyr/issues/18194) - [zephyr 1.14][MESH/NODE/CFG/HBP/BV-05-C] Zephyr does not send Heartbeat message on friendship termination
- [GitHub #18188](https://github.com/zephyrproject-rtos/zephyr/issues/18188) - [zephyr 1.14] Re-enabling CCC gets broken when used along with Robust Caching
- [GitHub #18183](https://github.com/zephyrproject-rtos/zephyr/issues/18183) - [zephyr 1.14][GATT/SR/GAS/BV-07-C] GATT Server does not inform change-unaware client about DB changes
- [GitHub #18181](https://github.com/zephyrproject-rtos/zephyr/issues/18181) - Some platforms(e.g. sam\_e70\_xplained) will be flashed failure if the platforms have not generated HEX file although they are built successfully.
- [GitHub #18178](https://github.com/zephyrproject-rtos/zephyr/issues/18178) - BLE Mesh When Provisioning Use Input OOB Method
- [GitHub #18171](https://github.com/zephyrproject-rtos/zephyr/issues/18171) - gen\_defines creates identical labels for multicell pwms definition
- [GitHub #18155](https://github.com/zephyrproject-rtos/zephyr/issues/18155) - i2c\_ll\_stm32\_v1: I2C\_CR1:STOP is not cleared
- [GitHub #18154](https://github.com/zephyrproject-rtos/zephyr/issues/18154) - Qemu: mps2+: missing documentation
- [GitHub #18150](https://github.com/zephyrproject-rtos/zephyr/issues/18150) - [zephyr 1.14] Host does not change the RPA
- [GitHub #18141](https://github.com/zephyrproject-rtos/zephyr/issues/18141) - arc: the caculation of exception stack is wrong
- [GitHub #18140](https://github.com/zephyrproject-rtos/zephyr/issues/18140) - xtensa passes NULL esf on fatal error
- [GitHub #18132](https://github.com/zephyrproject-rtos/zephyr/issues/18132) - getting\_started should indicate upgrade rather than just install west
- [GitHub #18131](https://github.com/zephyrproject-rtos/zephyr/issues/18131) - devicetree should check input against declared type
- [GitHub #18092](https://github.com/zephyrproject-rtos/zephyr/issues/18092) - Assert in BT controller on RPA timeout
- [GitHub #18090](https://github.com/zephyrproject-rtos/zephyr/issues/18090) - [zephyr 1.14][MESH/NODE/FRND/FN/BV-08-C] Mesh Friend queues more messages than indicates it’s Friend Cache
- [GitHub #18080](https://github.com/zephyrproject-rtos/zephyr/issues/18080) - LWM2M bootstrap issue
- [GitHub #18059](https://github.com/zephyrproject-rtos/zephyr/issues/18059) - k\_busy\_wait passed milliseconds instead of microseconds
- [GitHub #18052](https://github.com/zephyrproject-rtos/zephyr/issues/18052) - z\_fatal\_error missing log\_strdup
- [GitHub #18048](https://github.com/zephyrproject-rtos/zephyr/issues/18048) - [zephyr 1.14] Zephyr with privacy does not disconnect device with unresolvable RPA
- [GitHub #18042](https://github.com/zephyrproject-rtos/zephyr/issues/18042) - Only corporate members can join the slack channel
- [GitHub #18034](https://github.com/zephyrproject-rtos/zephyr/issues/18034) - It’s impossible to build Zephyr via cmake/make with west 0.6.0 installed
- [GitHub #18029](https://github.com/zephyrproject-rtos/zephyr/issues/18029) - why kconfiglib.py doesn’t throw error for file drivers/serial/Kconfig.nrfx
- [GitHub #18021](https://github.com/zephyrproject-rtos/zephyr/issues/18021) - Socket vtable can access null pointer callback function
- [GitHub #18019](https://github.com/zephyrproject-rtos/zephyr/issues/18019) - BT scan via shell fatal error
- [GitHub #18013](https://github.com/zephyrproject-rtos/zephyr/issues/18013) - BLE Mesh On Net Buffer free issue
- [GitHub #18011](https://github.com/zephyrproject-rtos/zephyr/issues/18011) - arc: the offset generation of accl\_regs is wrong
- [GitHub #18009](https://github.com/zephyrproject-rtos/zephyr/issues/18009) - Dead link in documentation
- [GitHub #18005](https://github.com/zephyrproject-rtos/zephyr/issues/18005) - BLE Mesh When Friend Clear Procedure Timeout
- [GitHub #18002](https://github.com/zephyrproject-rtos/zephyr/issues/18002) - Flash using open source stlink, instead of SEGGER jlink?
- [GitHub #17997](https://github.com/zephyrproject-rtos/zephyr/issues/17997) - fix extern “C” use throughout Zephyr
- [GitHub #17996](https://github.com/zephyrproject-rtos/zephyr/issues/17996) - BUILD\_ASSERT not active in three of five shippable platforms
- [GitHub #17990](https://github.com/zephyrproject-rtos/zephyr/issues/17990) - BLE Mesh When IV update test procedure
- [GitHub #17979](https://github.com/zephyrproject-rtos/zephyr/issues/17979) - Security level cannot be elevated after re-connection with privacy
- [GitHub #17977](https://github.com/zephyrproject-rtos/zephyr/issues/17977) - BLE Mesh When IV Update Procedure
- [GitHub #17971](https://github.com/zephyrproject-rtos/zephyr/issues/17971) - [zephyr 1.14] Unable to register GATT service that was unregistered before
- [GitHub #17967](https://github.com/zephyrproject-rtos/zephyr/issues/17967) - drivers/pwm/pwm\_api test failed on frdm\_k64f board.
- [GitHub #17965](https://github.com/zephyrproject-rtos/zephyr/issues/17965) - kernel/sleep/ test failed on reel\_board.
- [GitHub #17962](https://github.com/zephyrproject-rtos/zephyr/issues/17962) - BLE Mesh Recommended memory allocation due to who is assigned who releases the strategy
- [GitHub #17956](https://github.com/zephyrproject-rtos/zephyr/issues/17956) - Is POSIX I/O supported on peripheral?
- [GitHub #17951](https://github.com/zephyrproject-rtos/zephyr/issues/17951) - RFC: update FS API for readdir consistency
- [GitHub #17948](https://github.com/zephyrproject-rtos/zephyr/issues/17948) - Bluetooth: privacy: Reconnection issue
- [GitHub #17944](https://github.com/zephyrproject-rtos/zephyr/issues/17944) - [zephyr 1.14] LE Enhanced Connection Complete indicates Resolved Public once connected to Public peer address
- [GitHub #17936](https://github.com/zephyrproject-rtos/zephyr/issues/17936) - Bluetooth: Mesh: The canceled buffer is not free, causing a memory leak
- [GitHub #17932](https://github.com/zephyrproject-rtos/zephyr/issues/17932) - BLE Mesh When Friend Send Seg Message To LPN
- [GitHub #17926](https://github.com/zephyrproject-rtos/zephyr/issues/17926) - CAN | nrf52 | device tree error: zephyrproject/zephyr/dts/bindings/can/microchip,mcp2515.yaml (in ‘reg’): ‘category’ from !included file overwritten (‘required’ replaced with ‘optional’)
- [GitHub #17923](https://github.com/zephyrproject-rtos/zephyr/issues/17923) - SPI1 on nrf52\_pca10040 is dead by default
- [GitHub #17922](https://github.com/zephyrproject-rtos/zephyr/issues/17922) - Driver: modem helper should make it easier to implement a modem
- [GitHub #17920](https://github.com/zephyrproject-rtos/zephyr/issues/17920) - Bluetooth: Security problem
- [GitHub #17907](https://github.com/zephyrproject-rtos/zephyr/issues/17907) - BLE Mesh when resend use GATT bearer
- [GitHub #17899](https://github.com/zephyrproject-rtos/zephyr/issues/17899) - tests/kernel/mem\_protect/stackprot/kernel.memory\_protection fails on nsim\_em
- [GitHub #17897](https://github.com/zephyrproject-rtos/zephyr/issues/17897) - k\_busy\_wait not working when using 32KHz timer driver
- [GitHub #17891](https://github.com/zephyrproject-rtos/zephyr/issues/17891) - fs/nvs: nvs\_init can hang if no nvs\_ate available
- [GitHub #17882](https://github.com/zephyrproject-rtos/zephyr/issues/17882) - [zephyr 1.14] Database Out of Sync error is not returned as expected
- [GitHub #17880](https://github.com/zephyrproject-rtos/zephyr/issues/17880) - Unable to re-connect to privacy enabled peer when using stack generated Identity
- [GitHub #17876](https://github.com/zephyrproject-rtos/zephyr/issues/17876) - BME680 sensor sample not building
- [GitHub #17870](https://github.com/zephyrproject-rtos/zephyr/issues/17870) - Incorrect report received lenght and offset in async API
- [GitHub #17869](https://github.com/zephyrproject-rtos/zephyr/issues/17869) - Unlocking nested k\_sched\_lock() cause forced preemption
- [GitHub #17864](https://github.com/zephyrproject-rtos/zephyr/issues/17864) - cpp\_synchronization sample not working on nucleo\_l476rg
- [GitHub #17861](https://github.com/zephyrproject-rtos/zephyr/issues/17861) - Tester application lacks BTP Discover All Primary Services handler
- [GitHub #17857](https://github.com/zephyrproject-rtos/zephyr/issues/17857) - GATT: Incorrect byte order for GATT database hash
- [GitHub #17853](https://github.com/zephyrproject-rtos/zephyr/issues/17853) - kernel panic in tests/kernel/sched/schedule\_api
- [GitHub #17851](https://github.com/zephyrproject-rtos/zephyr/issues/17851) - riscv/m2gl025: timer tests broken
- [GitHub #17843](https://github.com/zephyrproject-rtos/zephyr/issues/17843) - Bluetooth: controller: v1.14.x release conformance test failures
- [GitHub #17821](https://github.com/zephyrproject-rtos/zephyr/issues/17821) - Mesh Bug on access.c
- [GitHub #17820](https://github.com/zephyrproject-rtos/zephyr/issues/17820) - Mesh bug report In access.c
- [GitHub #17816](https://github.com/zephyrproject-rtos/zephyr/issues/17816) - LVGL V5.3 build error if CONFIG\_LVGL\_COLOR\_16\_SWAP=y
- [GitHub #17812](https://github.com/zephyrproject-rtos/zephyr/issues/17812) - pthread\_cond\_timedwait interprets timeout wrong
- [GitHub #17809](https://github.com/zephyrproject-rtos/zephyr/issues/17809) - Bluetooth Mesh message cached too early when LPN
- [GitHub #17802](https://github.com/zephyrproject-rtos/zephyr/issues/17802) - [zephyr 1.14] Address type 0x02 is used by LE Create Connection in device privacy mode
- [GitHub #17800](https://github.com/zephyrproject-rtos/zephyr/issues/17800) - Bluetooth: GATT: Write Without Reponse to invalid handle asserts
- [GitHub #17794](https://github.com/zephyrproject-rtos/zephyr/issues/17794) - Timeutil\_api test fails with sanitycheck on iotdk board.
- [GitHub #17790](https://github.com/zephyrproject-rtos/zephyr/issues/17790) - MEC1501 configure warnings in eSPI (dts)
- [GitHub #17789](https://github.com/zephyrproject-rtos/zephyr/issues/17789) - Bluetooth: host: conn.c missing parameter copy
- [GitHub #17787](https://github.com/zephyrproject-rtos/zephyr/issues/17787) - openocd unable to flash hello\_world to cc26x2r1\_launchxl
- [GitHub #17784](https://github.com/zephyrproject-rtos/zephyr/issues/17784) - failing network tests with code coverage enabled in qemu\_x86 not failing when run with gdb
- [GitHub #17783](https://github.com/zephyrproject-rtos/zephyr/issues/17783) - network tests failing with code coverage enabled in qemu\_x86 (coverage.c)
- [GitHub #17782](https://github.com/zephyrproject-rtos/zephyr/issues/17782) - network tests failing with ‘unexpected eof’ with code coverage enabled in qemu\_x86 (TSS)
- [GitHub #17778](https://github.com/zephyrproject-rtos/zephyr/issues/17778) - Microchip XEC rtos Timer breaks gpios and k\_sleep?
- [GitHub #17772](https://github.com/zephyrproject-rtos/zephyr/issues/17772) - Compilation error of soc/arm/nxp\_imx/rt/soc.c
- [GitHub #17764](https://github.com/zephyrproject-rtos/zephyr/issues/17764) - Broken link to latest development version of docs
- [GitHub #17751](https://github.com/zephyrproject-rtos/zephyr/issues/17751) - build is broken for mec15xxevb\_assy6853
- [GitHub #17738](https://github.com/zephyrproject-rtos/zephyr/issues/17738) - STATIC\_ASSERT no longer defined when CONFIG\_NEWLIB\_LIBC is enabled
- [GitHub #17732](https://github.com/zephyrproject-rtos/zephyr/issues/17732) - cannot use bt\_conn\_security in connected callback
- [GitHub #17727](https://github.com/zephyrproject-rtos/zephyr/issues/17727) - how to make zephyr as a ble mesh provisioner to other BLE based board having ble mesh
- [GitHub #17726](https://github.com/zephyrproject-rtos/zephyr/issues/17726) - How to make Zephyr as a ble mesh provisioner ?
- [GitHub #17723](https://github.com/zephyrproject-rtos/zephyr/issues/17723) - Advertiser never clears state flags
- [GitHub #17715](https://github.com/zephyrproject-rtos/zephyr/issues/17715) - Missing ‘reg-names’ string in riscv32-litex-vexriscv.dtsi
- [GitHub #17703](https://github.com/zephyrproject-rtos/zephyr/issues/17703) - Add prop ‘clock-frequency’ to STM32 targets
- [GitHub #17697](https://github.com/zephyrproject-rtos/zephyr/issues/17697) - usb\_dc\_nrfx driver gets stuck after USB3CV HID Tests are performed on hid sample
- [GitHub #17692](https://github.com/zephyrproject-rtos/zephyr/issues/17692) - Proper way for joining a multicast group (NRF52840/OpenThread)
- [GitHub #17690](https://github.com/zephyrproject-rtos/zephyr/issues/17690) - samples/subsys/shell/fs does not work?
- [GitHub #17671](https://github.com/zephyrproject-rtos/zephyr/issues/17671) - ADC not supported by nrf52840\_pca10059 DTS file
- [GitHub #17665](https://github.com/zephyrproject-rtos/zephyr/issues/17665) - Missing ‘label’ on most nodes with ‘compatible = “pwm-leds”’
- [GitHub #17664](https://github.com/zephyrproject-rtos/zephyr/issues/17664) - Missing ‘clocks’ on most nodes with ‘compatible = “nxp,kinetis-usbd”’
- [GitHub #17663](https://github.com/zephyrproject-rtos/zephyr/issues/17663) - Missing ‘label’ on most nodes with ‘compatible = “fixed-clock”’
- [GitHub #17662](https://github.com/zephyrproject-rtos/zephyr/issues/17662) - Missing ‘label’ on nodes with ‘compatible = “jedec,spi-nor”’
- [GitHub #17657](https://github.com/zephyrproject-rtos/zephyr/issues/17657) - subsis/disk/disk\_access\_spi\_sdhc: response data eaten by idle byte consumption
- [GitHub #17650](https://github.com/zephyrproject-rtos/zephyr/issues/17650) - devicetree: missing preferred instance presence macro
- [GitHub #17635](https://github.com/zephyrproject-rtos/zephyr/issues/17635) - UnicodeDecodeError is raised while executing west build
- [GitHub #17630](https://github.com/zephyrproject-rtos/zephyr/issues/17630) - efr32mg\_sltb004a tick clock error
- [GitHub #17613](https://github.com/zephyrproject-rtos/zephyr/issues/17613) - POSIX arch: occasional failures of tests/kernel/sched/schedule\_api on CI
- [GitHub #17608](https://github.com/zephyrproject-rtos/zephyr/issues/17608) - NMP timeout when uploading image with mcumgr over BLE under Linux
- [GitHub #17600](https://github.com/zephyrproject-rtos/zephyr/issues/17600) - Enable Mesh Friend support in Bluetooth tester application
- [GitHub #17595](https://github.com/zephyrproject-rtos/zephyr/issues/17595) - two userspace tests fail if stack canaries are enabled in board configuration
- [GitHub #17591](https://github.com/zephyrproject-rtos/zephyr/issues/17591) - ARM: z\_arch\_except() is too permissive in user mode
- [GitHub #17590](https://github.com/zephyrproject-rtos/zephyr/issues/17590) - ARC: unable to induce kernel\_oops or stack check fail errors from user mode
- [GitHub #17586](https://github.com/zephyrproject-rtos/zephyr/issues/17586) - stack canary storage area should be read-only to user mode?
- [GitHub #17584](https://github.com/zephyrproject-rtos/zephyr/issues/17584) - k\_mutex is not SMP-safe
- [GitHub #17581](https://github.com/zephyrproject-rtos/zephyr/issues/17581) - linker script packing failure with subsys/fb fonts and native\_posix\_64
- [GitHub #17564](https://github.com/zephyrproject-rtos/zephyr/issues/17564) - Missing ‘stdlib.h’ include when C++ standard library is used.
- [GitHub #17559](https://github.com/zephyrproject-rtos/zephyr/issues/17559) - Assertion failed: zephyr toolchain variant invalid
- [GitHub #17557](https://github.com/zephyrproject-rtos/zephyr/issues/17557) - samples/net/wifi fails to build on cc3220sf\_launchxl
- [GitHub #17555](https://github.com/zephyrproject-rtos/zephyr/issues/17555) - CONFIG\_LOG doesn’t work on x86\_64 due to no working backends
- [GitHub #17554](https://github.com/zephyrproject-rtos/zephyr/issues/17554) - pyocd flash does not support the -b option for board ID so that the sanitycheck script can’t specified the board ID to flash when the host connected with multiple boards.
- [GitHub #17550](https://github.com/zephyrproject-rtos/zephyr/issues/17550) - SimpleLink WiFi host driver should revert back to using static memory model
- [GitHub #17547](https://github.com/zephyrproject-rtos/zephyr/issues/17547) - incorrect documentation for debugging nsim\_em / nsim\_sem
- [GitHub #17543](https://github.com/zephyrproject-rtos/zephyr/issues/17543) - dtc version 1.4.5 with ubuntu 18.04 and zephyr sdk-0.10.1
- [GitHub #17534](https://github.com/zephyrproject-rtos/zephyr/issues/17534) - Race condition in GATT API.
- [GitHub #17532](https://github.com/zephyrproject-rtos/zephyr/issues/17532) - List of missing device tree properties with ‘category: required’ in the binding for the node
- [GitHub #17525](https://github.com/zephyrproject-rtos/zephyr/issues/17525) - L2CAP: On insufficient authentication error received, Zephyr does unauthenticated pairing
- [GitHub #17511](https://github.com/zephyrproject-rtos/zephyr/issues/17511) - \_bt\_br\_channels\_area section missing in sanitycheck whitelist
- [GitHub #17508](https://github.com/zephyrproject-rtos/zephyr/issues/17508) - RFC: Change/deprecation in display API
- [GitHub #17507](https://github.com/zephyrproject-rtos/zephyr/issues/17507) - system timer drivers using the “new” API should not be configured with CONFIG\_TICKLESS\_KERNEL
- [GitHub #17497](https://github.com/zephyrproject-rtos/zephyr/issues/17497) - Bluetooth: Mesh: How to Write provision and configure data to flash?
- [GitHub #17488](https://github.com/zephyrproject-rtos/zephyr/issues/17488) - CDC\_ACM USB on nRF device fails after suspend
- [GitHub #17487](https://github.com/zephyrproject-rtos/zephyr/issues/17487) - v1.14-branch: SDK 0.10.1 support?
- [GitHub #17486](https://github.com/zephyrproject-rtos/zephyr/issues/17486) - nRF52: SPIM: Errata work-around status?
- [GitHub #17485](https://github.com/zephyrproject-rtos/zephyr/issues/17485) - sanitycheck: Over-zealous checking for binary sections
- [GitHub #17483](https://github.com/zephyrproject-rtos/zephyr/issues/17483) - mec15xxevb\_assy6853 board documentation is erroneous
- [GitHub #17480](https://github.com/zephyrproject-rtos/zephyr/issues/17480) - holyiot\_yj16019 cannot compile IEEE 802.15.4 L2
- [GitHub #17478](https://github.com/zephyrproject-rtos/zephyr/issues/17478) - net/buf test fails for qemu\_x86\_64
- [GitHub #17475](https://github.com/zephyrproject-rtos/zephyr/issues/17475) - [RTT] compile error when RTT console enabled
- [GitHub #17463](https://github.com/zephyrproject-rtos/zephyr/issues/17463) - Bluetooth: API limits usage of MITM flags in Pairing Request
- [GitHub #17460](https://github.com/zephyrproject-rtos/zephyr/issues/17460) - sample: gui/lvgl
- [GitHub #17450](https://github.com/zephyrproject-rtos/zephyr/issues/17450) - net: IPv6/UDP datagram with unspecified addr and zero hop limit causes Zephyr to quit
- [GitHub #17439](https://github.com/zephyrproject-rtos/zephyr/issues/17439) - sanitycheck: nrf52840-pca10056 (dev kit) picks up sample/drivers items which will fail due to missing HW
- [GitHub #17427](https://github.com/zephyrproject-rtos/zephyr/issues/17427) - net: IPv4/UDP datagram with zero src addr and TTL causes Zephyr to segfault
- [GitHub #17419](https://github.com/zephyrproject-rtos/zephyr/issues/17419) - arch:arc: remove the extra vairables used in irq and exception handling
- [GitHub #17415](https://github.com/zephyrproject-rtos/zephyr/issues/17415) - Settings Module - settings\_line\_val\_read() returning -EINVAL instead of 0 for deleted setting entries
- [GitHub #17410](https://github.com/zephyrproject-rtos/zephyr/issues/17410) - k\_work should have a user\_data field
- [GitHub #17408](https://github.com/zephyrproject-rtos/zephyr/issues/17408) - LwM2M: engine doesn’t support offloaded TLS stack
- [GitHub #17401](https://github.com/zephyrproject-rtos/zephyr/issues/17401) - LwM2M: requires that CONFIG\_NET\_IPV\* be enabled (can’t use 100% offloaded IP stack)
- [GitHub #17399](https://github.com/zephyrproject-rtos/zephyr/issues/17399) - LwM2M: Can’t use an alternate mbedtls implementation
- [GitHub #17381](https://github.com/zephyrproject-rtos/zephyr/issues/17381) - DTS compatible property processing assumes specific driver exists
- [GitHub #17379](https://github.com/zephyrproject-rtos/zephyr/issues/17379) - Wrong hex file generated for MCUboot
- [GitHub #17378](https://github.com/zephyrproject-rtos/zephyr/issues/17378) - samples: net: echo-server: no return packet
- [GitHub #17376](https://github.com/zephyrproject-rtos/zephyr/issues/17376) - device tree diagnostic failure in enum
- [GitHub #17368](https://github.com/zephyrproject-rtos/zephyr/issues/17368) - Time Slicing cause system sleep short time
- [GitHub #17366](https://github.com/zephyrproject-rtos/zephyr/issues/17366) - Regression: sanitycheck coverage generation defaults will error out for POSIX arch targets
- [GitHub #17365](https://github.com/zephyrproject-rtos/zephyr/issues/17365) - Documentation: sanitycheck coverage generation instructions lead to errors and no coverage report for POSIX boards
- [GitHub #17363](https://github.com/zephyrproject-rtos/zephyr/issues/17363) - SPI driver does not reset master mode fault on STM32
- [GitHub #17353](https://github.com/zephyrproject-rtos/zephyr/issues/17353) - Configuring with POSIX\_API disables NET\_SOCKETS\_POSIX\_NAMES
- [GitHub #17342](https://github.com/zephyrproject-rtos/zephyr/issues/17342) - CODEOWNERS is broken (III)
- [GitHub #17340](https://github.com/zephyrproject-rtos/zephyr/issues/17340) - Bluetooth Mesh: Unable to receive messages when RPL is full.
- [GitHub #17338](https://github.com/zephyrproject-rtos/zephyr/issues/17338) - kernel objects address check in elf\_helper.py
- [GitHub #17313](https://github.com/zephyrproject-rtos/zephyr/issues/17313) - drivers: usb\_dc\_mcux\_ehci does not compile
- [GitHub #17307](https://github.com/zephyrproject-rtos/zephyr/issues/17307) - device tree bindings disallow strings that begin with integers
- [GitHub #17294](https://github.com/zephyrproject-rtos/zephyr/issues/17294) - DB corruption when adding/removing service
- [GitHub #17288](https://github.com/zephyrproject-rtos/zephyr/issues/17288) - Bluetooth: controller: Fix handling of L2CAP start frame with zero PDU length
- [GitHub #17284](https://github.com/zephyrproject-rtos/zephyr/issues/17284) - unrecognized binary sections: [‘\_settings\_handlers\_area’]
- [GitHub #17281](https://github.com/zephyrproject-rtos/zephyr/issues/17281) - sanitycheck error on mimxrt1050\_evk samples/gui/lvgl/sample.gui.lvgl with no network connection
- [GitHub #17280](https://github.com/zephyrproject-rtos/zephyr/issues/17280) - How to use UART1 for nrf52\_pca10040
- [GitHub #17277](https://github.com/zephyrproject-rtos/zephyr/issues/17277) - no code coverage for k\_float\_disable() in user mode
- [GitHub #17266](https://github.com/zephyrproject-rtos/zephyr/issues/17266) - CDC\_ACM USB not recognized by windows as serial port
- [GitHub #17262](https://github.com/zephyrproject-rtos/zephyr/issues/17262) - insufficient code coverage for lib/os/base64.c
- [GitHub #17251](https://github.com/zephyrproject-rtos/zephyr/issues/17251) - w25q: erase operations must be erase-size aligned
- [GitHub #17250](https://github.com/zephyrproject-rtos/zephyr/issues/17250) - After first GC operation the 1st sector had become scratch and the 2nd sector had became write sector.
- [GitHub #17231](https://github.com/zephyrproject-rtos/zephyr/issues/17231) - Posix filesystem wrapper leaks internal FS desc structures
- [GitHub #17226](https://github.com/zephyrproject-rtos/zephyr/issues/17226) - [Coverity CID :61894]Security best practices violations in /home/aasthagr/zephyrproject/modules/crypto/mbedtls/library/rsa.c
- [GitHub #17225](https://github.com/zephyrproject-rtos/zephyr/issues/17225) - [Coverity CID :61905]Insecure data handling in /home/aasthagr/zephyrproject/modules/crypto/mbedtls/library/ssl\_cli.c
- [GitHub #17224](https://github.com/zephyrproject-rtos/zephyr/issues/17224) - [Coverity CID :78542]Null pointer dereferences in /home/aasthagr/zephyrproject/modules/crypto/mbedtls/library/rsa.c
- [GitHub #17223](https://github.com/zephyrproject-rtos/zephyr/issues/17223) - [Coverity CID :149311]Control flow issues in /home/aasthagr/zephyrproject/modules/crypto/mbedtls/library/cipher.c
- [GitHub #17222](https://github.com/zephyrproject-rtos/zephyr/issues/17222) - [Coverity CID :173947]Uninitialized variables in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cborattr/src/cborattr.c
- [GitHub #17221](https://github.com/zephyrproject-rtos/zephyr/issues/17221) - [Coverity CID :173979]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/tinycbor/src/cborparser.c
- [GitHub #17220](https://github.com/zephyrproject-rtos/zephyr/issues/17220) - [Coverity CID :173986]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cborattr/src/cborattr.c
- [GitHub #17219](https://github.com/zephyrproject-rtos/zephyr/issues/17219) - [Coverity CID :174014]Incorrect expression in /home/aasthagr/zephyrproject/modules/lib/tinycbor/src/cborparser.c
- [GitHub #17218](https://github.com/zephyrproject-rtos/zephyr/issues/17218) - [Coverity CID :186031]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cmd/fs\_mgmt/src/fs\_mgmt.c
- [GitHub #17217](https://github.com/zephyrproject-rtos/zephyr/issues/17217) - [Coverity CID :186038]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cmd/img\_mgmt/src/img\_mgmt.c
- [GitHub #17216](https://github.com/zephyrproject-rtos/zephyr/issues/17216) - [Coverity CID :186052]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cmd/fs\_mgmt/src/fs\_mgmt.c
- [GitHub #17215](https://github.com/zephyrproject-rtos/zephyr/issues/17215) - [Coverity CID :186054]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cmd/img\_mgmt/src/img\_mgmt\_state.c
- [GitHub #17214](https://github.com/zephyrproject-rtos/zephyr/issues/17214) - [Coverity CID :186060]Control flow issues in /home/aasthagr/zephyrproject/modules/lib/mcumgr/cmd/img\_mgmt/src/img\_mgmt\_state.c
- [GitHub #17213](https://github.com/zephyrproject-rtos/zephyr/issues/17213) - [Coverity CID :186188]Memory - illegal accesses in /home/aasthagr/zephyrproject/modules/lib/open-amp/open-amp/lib/rpmsg/rpmsg.c
- [GitHub #17212](https://github.com/zephyrproject-rtos/zephyr/issues/17212) - [Coverity CID :187076]Control flow issues in /home/aasthagr/zephyrproject/modules/hal/silabs/gecko/emlib/src/em\_cmu.c
- [GitHub #17211](https://github.com/zephyrproject-rtos/zephyr/issues/17211) - [Coverity CID :188746]Memory - illegal accesses in /home/aasthagr/zephyrproject/modules/hal/cypress/PDL/3.1.0/drivers/source/cy\_syslib.c
- [GitHub #17210](https://github.com/zephyrproject-rtos/zephyr/issues/17210) - [Coverity CID :190643]Error handling issues in /home/aasthagr/zephyrproject/modules/debug/segger/systemview/SEGGER\_SYSVIEW.c
- [GitHub #17209](https://github.com/zephyrproject-rtos/zephyr/issues/17209) - [Coverity CID :190927]Uninitialized variables in /home/aasthagr/zephyrproject/modules/lib/open-amp/open-amp/lib/remoteproc/remoteproc.c
- [GitHub #17208](https://github.com/zephyrproject-rtos/zephyr/issues/17208) - [Coverity CID :190941]Insecure data handling in /home/aasthagr/zephyrproject/modules/crypto/mbedtls/library/ssl\_tls.c
- [GitHub #17207](https://github.com/zephyrproject-rtos/zephyr/issues/17207) - [Coverity CID :190963]Code maintainability issues in /home/aasthagr/zephyrproject/modules/fs/nffs/src/nffs\_restore.c
- [GitHub #17206](https://github.com/zephyrproject-rtos/zephyr/issues/17206) - [Coverity CID :190975]Memory - illegal accesses in /home/aasthagr/zephyrproject/modules/lib/open-amp/open-amp/lib/include/openamp/rpmsg.h
- [GitHub #17205](https://github.com/zephyrproject-rtos/zephyr/issues/17205) - [Coverity CID :190999]Insecure data handling in /home/aasthagr/zephyrproject/modules/lib/open-amp/open-amp/lib/rpmsg/rpmsg\_virtio.c
- [GitHub #17204](https://github.com/zephyrproject-rtos/zephyr/issues/17204) - [Coverity CID :191000]Memory - corruptions in /home/aasthagr/zephyrproject/modules/lib/open-amp/open-amp/lib/remoteproc/remoteproc.c
- [GitHub #17203](https://github.com/zephyrproject-rtos/zephyr/issues/17203) - [Coverity CID :198951]Code maintainability issues in /home/aasthagr/zephyrproject/modules/debug/segger/systemview/SEGGER\_SYSVIEW.c
- [GitHub #17202](https://github.com/zephyrproject-rtos/zephyr/issues/17202) - [Coverity CID :199436]Uninitialized variables in /subsys/net/lib/sockets/sockets.c
- [GitHub #17201](https://github.com/zephyrproject-rtos/zephyr/issues/17201) - [Coverity CID :199437]Null pointer dereferences in /tests/net/ip-addr/src/main.c
- [GitHub #17200](https://github.com/zephyrproject-rtos/zephyr/issues/17200) - [Coverity CID :199438]Memory - illegal accesses in /drivers/interrupt\_controller/exti\_stm32.c
- [GitHub #17190](https://github.com/zephyrproject-rtos/zephyr/issues/17190) - net-mgmt should pass info element size to callback
- [GitHub #17188](https://github.com/zephyrproject-rtos/zephyr/issues/17188) - k\_uptime\_delta returns wrong times
- [GitHub #17182](https://github.com/zephyrproject-rtos/zephyr/issues/17182) - “tests/subsys/usb/device/” fails on reel\_board.
- [GitHub #17177](https://github.com/zephyrproject-rtos/zephyr/issues/17177) - ARM: userspace/test\_bad\_syscall fails on ARMv8-M
- [GitHub #17176](https://github.com/zephyrproject-rtos/zephyr/issues/17176) - deprecated counter\_set\_alarm is referenced in documentation
- [GitHub #17172](https://github.com/zephyrproject-rtos/zephyr/issues/17172) - insufficient code coverage for lib/os/mempool.c
- [GitHub #17170](https://github.com/zephyrproject-rtos/zephyr/issues/17170) - x86\_64 crash with spinning child thread
- [GitHub #17167](https://github.com/zephyrproject-rtos/zephyr/issues/17167) - ARC crash with spinning user thread
- [GitHub #17166](https://github.com/zephyrproject-rtos/zephyr/issues/17166) - arch/x86: eliminate support for CONFIG\_REALMODE
- [GitHub #17158](https://github.com/zephyrproject-rtos/zephyr/issues/17158) - Bluetooth: Update PICS for latest PTS 7.4.1
- [GitHub #17147](https://github.com/zephyrproject-rtos/zephyr/issues/17147) - UARTE device has no API when run on nrf52810
- [GitHub #17114](https://github.com/zephyrproject-rtos/zephyr/issues/17114) - drivers: usb\_dc\_stm32 broken after west update
- [GitHub #17111](https://github.com/zephyrproject-rtos/zephyr/issues/17111) - nucleo\_f030r8 build error
- [GitHub #17095](https://github.com/zephyrproject-rtos/zephyr/issues/17095) - Building with Xtensa toolchain fails
- [GitHub #17092](https://github.com/zephyrproject-rtos/zephyr/issues/17092) - Bluetooth: GAP/IDLE/NAMP/BV-01-C requires Read by UUID
- [GitHub #17065](https://github.com/zephyrproject-rtos/zephyr/issues/17065) - Misspelled CONFIG use in is\_rodata() for CONFIG\_RISCV32
- [GitHub #17063](https://github.com/zephyrproject-rtos/zephyr/issues/17063) - tests/kernel/tickless/tickless\_concept (qemu\_x86) fails even outside of CI
- [GitHub #17057](https://github.com/zephyrproject-rtos/zephyr/issues/17057) - Bluetooth: Mesh: Implementation doesn’t conform to latest errata and 1.0.1 version
- [GitHub #17055](https://github.com/zephyrproject-rtos/zephyr/issues/17055) - net: Incorrect data length after the connection is established
- [GitHub #17053](https://github.com/zephyrproject-rtos/zephyr/issues/17053) - Bluetooth Mesh: Periodic Publishing
- [GitHub #17043](https://github.com/zephyrproject-rtos/zephyr/issues/17043) - compile “hello-world” sample for esp32 board error
- [GitHub #17041](https://github.com/zephyrproject-rtos/zephyr/issues/17041) - [1.14] Bluetooth: Mesh: RPL handling is not in line with the spec
- [GitHub #17038](https://github.com/zephyrproject-rtos/zephyr/issues/17038) - code relocation generating different memory layout cause user mode not working
- [GitHub #17037](https://github.com/zephyrproject-rtos/zephyr/issues/17037) - MQTT with TLS support over SOCKS
- [GitHub #17031](https://github.com/zephyrproject-rtos/zephyr/issues/17031) - Compiler warnings in settings module in Zephyr 1.14
- [GitHub #17017](https://github.com/zephyrproject-rtos/zephyr/issues/17017) - #16827 Breaks Ethernet on FRDM-K64F
- [GitHub #17015](https://github.com/zephyrproject-rtos/zephyr/issues/17015) - #15910 Breaks Ethernet on STM32F7
- [GitHub #17013](https://github.com/zephyrproject-rtos/zephyr/issues/17013) - Bluetooth: Add error reason to pairing failed callbacks
- [GitHub #17007](https://github.com/zephyrproject-rtos/zephyr/issues/17007) - USB mass demo format fails on frdm\_k64f
- [GitHub #16989](https://github.com/zephyrproject-rtos/zephyr/issues/16989) - Errors when building application in Eclipse
- [GitHub #16971](https://github.com/zephyrproject-rtos/zephyr/issues/16971) - DFU supported for hci\_uart sample ?
- [GitHub #16946](https://github.com/zephyrproject-rtos/zephyr/issues/16946) - characteristic value handle vs characteristic handle
- [GitHub #16944](https://github.com/zephyrproject-rtos/zephyr/issues/16944) - Insufficient test coverage for lib/os/json.c
- [GitHub #16943](https://github.com/zephyrproject-rtos/zephyr/issues/16943) - Missing test coverage for lib/os/crc\*.c
- [GitHub #16934](https://github.com/zephyrproject-rtos/zephyr/issues/16934) - drivers: flash: stm32l4: Erase wait time is not enough
- [GitHub #16931](https://github.com/zephyrproject-rtos/zephyr/issues/16931) - logging: Assertion when in panic mode
- [GitHub #16926](https://github.com/zephyrproject-rtos/zephyr/issues/16926) - NXP LPC54102（LPC54114）: question about dual core(M4 and M0) running on flash
- [GitHub #16924](https://github.com/zephyrproject-rtos/zephyr/issues/16924) - Add DNS server added/removed events to net\_mgmt
- [GitHub #16915](https://github.com/zephyrproject-rtos/zephyr/issues/16915) - stack\_sentinel: rare ASSERTION FAIL [!(z\_arch\_curr\_cpu()->nested != 0U)] @ ZEPHYR\_BASE/kernel/thread.c:429 Threads may not be created in ISRs
- [GitHub #16911](https://github.com/zephyrproject-rtos/zephyr/issues/16911) - tests/kernel/sched/schedule\_api crash on qemu\_x86\_64 with SCHED\_MULTIQ enabled
- [GitHub #16907](https://github.com/zephyrproject-rtos/zephyr/issues/16907) - native\_posix build fails with X86\_64 on macOS
- [GitHub #16901](https://github.com/zephyrproject-rtos/zephyr/issues/16901) - No test coverage for CONFIG\_ZERO\_LATENCY\_IRQS
- [GitHub #16899](https://github.com/zephyrproject-rtos/zephyr/issues/16899) - fs/nvs: might loop-up if storage was not erased before first run
- [GitHub #16898](https://github.com/zephyrproject-rtos/zephyr/issues/16898) - bluetooth stack change affects timer behavior
- [GitHub #16894](https://github.com/zephyrproject-rtos/zephyr/issues/16894) - ARM: alignment problems in libc/newlib
- [GitHub #16893](https://github.com/zephyrproject-rtos/zephyr/issues/16893) - Bluetooth: Multiple local IDs, privacy problem
- [GitHub #16887](https://github.com/zephyrproject-rtos/zephyr/issues/16887) - ARM: threads’ privilege stack alignment is not optimal
- [GitHub #16872](https://github.com/zephyrproject-rtos/zephyr/issues/16872) - Bluetooth: LL: Peripheral crashes after a while with multiple Centrals
- [GitHub #16864](https://github.com/zephyrproject-rtos/zephyr/issues/16864) - Bluetooth: Mesh: Rx buffer exhaustion causes deadlock
- [GitHub #16862](https://github.com/zephyrproject-rtos/zephyr/issues/16862) - arc: -mfpu=fpuda\_all is not set when CONFIG\_FLOAT is configured
- [GitHub #16861](https://github.com/zephyrproject-rtos/zephyr/issues/16861) - nRF52: UARTE: Data corruption right after resuming device
- [GitHub #16830](https://github.com/zephyrproject-rtos/zephyr/issues/16830) - Bluetooth: controller: Follow up on ticker conflict resolution
- [GitHub #16823](https://github.com/zephyrproject-rtos/zephyr/issues/16823) - k\_busy\_wait() on nRF5x boards isn’t waiting long enough
- [GitHub #16803](https://github.com/zephyrproject-rtos/zephyr/issues/16803) - Deferred bt\_conn\_tx causes sysworkq deadlock
- [GitHub #16799](https://github.com/zephyrproject-rtos/zephyr/issues/16799) - Bluetooth: L2CAP: Interpretation of SCID and DCID in Disconnect is wrong
- [GitHub #16797](https://github.com/zephyrproject-rtos/zephyr/issues/16797) - [Zephyr v1.14.0] stm32: MCUboot bootloader results in Hardware exception
- [GitHub #16793](https://github.com/zephyrproject-rtos/zephyr/issues/16793) - kernel timeout\_list repeatedly add a thread
- [GitHub #16787](https://github.com/zephyrproject-rtos/zephyr/issues/16787) - [Coverity CID :198945]Null pointer dereferences in /subsys/bluetooth/controller/ll\_sw/ull\_conn.c
- [GitHub #16786](https://github.com/zephyrproject-rtos/zephyr/issues/16786) - [Coverity CID :198946]Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #16785](https://github.com/zephyrproject-rtos/zephyr/issues/16785) - [Coverity CID :198949]Error handling issues in /tests/net/socket/register/src/main.c
- [GitHub #16779](https://github.com/zephyrproject-rtos/zephyr/issues/16779) - [Zephyr v1.14] ARM: fix the start address of MPU guard in stack-fail checking (when building with no user mode)
- [GitHub #16778](https://github.com/zephyrproject-rtos/zephyr/issues/16778) - Build failures in various mimxrt boards
- [GitHub #16773](https://github.com/zephyrproject-rtos/zephyr/issues/16773) - DTS: generated output for each flash-controller
- [GitHub #16770](https://github.com/zephyrproject-rtos/zephyr/issues/16770) - Complete FP support for ARC
- [GitHub #16761](https://github.com/zephyrproject-rtos/zephyr/issues/16761) - nrf52840 usb driver with openthread
- [GitHub #16760](https://github.com/zephyrproject-rtos/zephyr/issues/16760) - K\_THREAD\_STACK\_EXTERN() confuses gen\_kobject\_list.py
- [GitHub #16750](https://github.com/zephyrproject-rtos/zephyr/issues/16750) - counter: lack of interrupt when CC=0
- [GitHub #16749](https://github.com/zephyrproject-rtos/zephyr/issues/16749) - IRQ\_CONNECT and irq\_enable calls in the SiFive UART driver is misconfigured
- [GitHub #16747](https://github.com/zephyrproject-rtos/zephyr/issues/16747) - bluetooth: peripheral: RX buffer size issues
- [GitHub #16746](https://github.com/zephyrproject-rtos/zephyr/issues/16746) - boards: nrf52840\_pca10059: Configure NFC pins as GPIOs by default
- [GitHub #16745](https://github.com/zephyrproject-rtos/zephyr/issues/16745) - PTHREAD\_MUTEX\_DEFINE(): don’t store into the \_k\_mutex section
- [GitHub #16739](https://github.com/zephyrproject-rtos/zephyr/issues/16739) - spi: stm32: pinmux: default configuration does not opt for low power consumption
- [GitHub #16734](https://github.com/zephyrproject-rtos/zephyr/issues/16734) - Bluetooth: GATT: Writing 1 byte to a CCC access invalid memory
- [GitHub #16733](https://github.com/zephyrproject-rtos/zephyr/issues/16733) - soc/stm32: Remove useless package digit for STM32 SoC Kconfig symbols
- [GitHub #16720](https://github.com/zephyrproject-rtos/zephyr/issues/16720) - drivers/loapic\_timer.c is buggy, needs cleanup
- [GitHub #16716](https://github.com/zephyrproject-rtos/zephyr/issues/16716) - soc: stm32: Is the setting of NUM\_IRQS in the F3 series wrong?
- [GitHub #16707](https://github.com/zephyrproject-rtos/zephyr/issues/16707) - Problem with k\_sleep
- [GitHub #16695](https://github.com/zephyrproject-rtos/zephyr/issues/16695) - code coverage: kernel/device.c
- [GitHub #16687](https://github.com/zephyrproject-rtos/zephyr/issues/16687) - basic disco sample fails
- [GitHub #16678](https://github.com/zephyrproject-rtos/zephyr/issues/16678) - LPN establishment of Friendship never completes if there is no response to the initial Friend Poll
- [GitHub #16676](https://github.com/zephyrproject-rtos/zephyr/issues/16676) - Settings enhancements
- [GitHub #16672](https://github.com/zephyrproject-rtos/zephyr/issues/16672) - nrf: spi: Excess current
- [GitHub #16670](https://github.com/zephyrproject-rtos/zephyr/issues/16670) - Memory reports do not work when Nordic proprietary LL is selected
- [GitHub #16661](https://github.com/zephyrproject-rtos/zephyr/issues/16661) - Symmetric multiprocessing (SMP) for ARC HS cores
- [GitHub #16639](https://github.com/zephyrproject-rtos/zephyr/issues/16639) - eth: pinging frdm k64f eventually leads to unresponsive ethernet device
- [GitHub #16634](https://github.com/zephyrproject-rtos/zephyr/issues/16634) - GATT indicate API inconsistent when using characteristic declaration attribute as argument
- [GitHub #16631](https://github.com/zephyrproject-rtos/zephyr/issues/16631) - SDK\_VERSION
- [GitHub #16624](https://github.com/zephyrproject-rtos/zephyr/issues/16624) - Building Grub fails when using gcc9
- [GitHub #16623](https://github.com/zephyrproject-rtos/zephyr/issues/16623) - Building with Openthread fails
- [GitHub #16607](https://github.com/zephyrproject-rtos/zephyr/issues/16607) - Building hello\_world fails for xtensa: xt-xcc ERROR parsing -Wno-address-of-packed-member: unknown flag
- [GitHub #16606](https://github.com/zephyrproject-rtos/zephyr/issues/16606) - Fault in CPU stats
- [GitHub #16604](https://github.com/zephyrproject-rtos/zephyr/issues/16604) - Zephyr fails to build with CPU load measurement enabled
- [GitHub #16603](https://github.com/zephyrproject-rtos/zephyr/issues/16603) - Bluetooth: Gatt Discovery: BT\_GATT\_DISCOVER\_PRIMARY returns all services while BT\_GATT\_DISCOVER\_SECONDARY returns none
- [GitHub #16602](https://github.com/zephyrproject-rtos/zephyr/issues/16602) - Bluetooth: GATT Discovery: Descriptor Discovery by range Seg Fault
- [GitHub #16600](https://github.com/zephyrproject-rtos/zephyr/issues/16600) - Bluetooth: Mesh: Proxy SAR timeout is not implemented
- [GitHub #16594](https://github.com/zephyrproject-rtos/zephyr/issues/16594) - net: dns: Zephyr is unable to unpack mDNS answers produced by another Zephyr node
- [GitHub #16584](https://github.com/zephyrproject-rtos/zephyr/issues/16584) - [Coverity CID :198863]Error handling issues in /subsys/net/lib/sntp/sntp.c
- [GitHub #16583](https://github.com/zephyrproject-rtos/zephyr/issues/16583) - [Coverity CID :198864]Parse warnings in /subsys/logging/log\_backend\_rtt.c
- [GitHub #16582](https://github.com/zephyrproject-rtos/zephyr/issues/16582) - [Coverity CID :198865]Null pointer dereferences in /drivers/usb/device/usb\_dc\_stm32.c
- [GitHub #16581](https://github.com/zephyrproject-rtos/zephyr/issues/16581) - [Coverity CID :198866]Null pointer dereferences in /subsys/net/lib/dns/llmnr\_responder.c
- [GitHub #16580](https://github.com/zephyrproject-rtos/zephyr/issues/16580) - [Coverity CID :198867]Parse warnings in /tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_system\_01.c
- [GitHub #16579](https://github.com/zephyrproject-rtos/zephyr/issues/16579) - [Coverity CID :198868]Parse warnings in /drivers/watchdog/wdt\_qmsi.c
- [GitHub #16578](https://github.com/zephyrproject-rtos/zephyr/issues/16578) - [Coverity CID :198869]Parse warnings in /subsys/shell/shell\_rtt.c
- [GitHub #16577](https://github.com/zephyrproject-rtos/zephyr/issues/16577) - [Coverity CID :198870]Error handling issues in /subsys/net/lib/lwm2m/lwm2m\_obj\_firmware\_pull.c
- [GitHub #16576](https://github.com/zephyrproject-rtos/zephyr/issues/16576) - [Coverity CID :198871]Parse warnings in /drivers/i2c/i2c\_qmsi\_ss.c
- [GitHub #16575](https://github.com/zephyrproject-rtos/zephyr/issues/16575) - [Coverity CID :198872]Parse warnings in /tests/subsys/settings/nffs/src/settings\_setup\_nffs.c
- [GitHub #16574](https://github.com/zephyrproject-rtos/zephyr/issues/16574) - [Coverity CID :198873]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #16573](https://github.com/zephyrproject-rtos/zephyr/issues/16573) - [Coverity CID :198874]Null pointer dereferences in /drivers/usb/device/usb\_dc\_stm32.c
- [GitHub #16572](https://github.com/zephyrproject-rtos/zephyr/issues/16572) - [Coverity CID :198875]Memory - corruptions in /drivers/flash/flash\_simulator.c
- [GitHub #16571](https://github.com/zephyrproject-rtos/zephyr/issues/16571) - [Coverity CID :198876]Parse warnings in /tests/subsys/fs/multi-fs/src/test\_nffs.h
- [GitHub #16570](https://github.com/zephyrproject-rtos/zephyr/issues/16570) - [Coverity CID :198877]Null pointer dereferences in /subsys/net/ip/net\_if.c
- [GitHub #16569](https://github.com/zephyrproject-rtos/zephyr/issues/16569) - [Coverity CID :198878]Error handling issues in /samples/net/sockets/echo\_server/src/tcp.c
- [GitHub #16568](https://github.com/zephyrproject-rtos/zephyr/issues/16568) - [Coverity CID :198879]Parse warnings in /tests/subsys/fs/fat\_fs\_dual\_drive/src/test\_fat\_mount.c
- [GitHub #16567](https://github.com/zephyrproject-rtos/zephyr/issues/16567) - [Coverity CID :198880]Possible Control flow issues in /samples/net/lwm2m\_client/src/lwm2m-client.c
- [GitHub #16566](https://github.com/zephyrproject-rtos/zephyr/issues/16566) - [Coverity CID :198881]Parse warnings in /drivers/serial/uart\_qmsi.c
- [GitHub #16565](https://github.com/zephyrproject-rtos/zephyr/issues/16565) - [Coverity CID :198882]Parse warnings in /drivers/console/rtt\_console.c
- [GitHub #16564](https://github.com/zephyrproject-rtos/zephyr/issues/16564) - [Coverity CID :198883]Parse warnings in /drivers/gpio/gpio\_qmsi\_ss.c
- [GitHub #16563](https://github.com/zephyrproject-rtos/zephyr/issues/16563) - [Coverity CID :198884]Parse warnings in /drivers/counter/counter\_qmsi\_aon.c
- [GitHub #16524](https://github.com/zephyrproject-rtos/zephyr/issues/16524) - FXOS8700 is not well supported in twr\_ke18f
- [GitHub #16519](https://github.com/zephyrproject-rtos/zephyr/issues/16519) - USAGE FAULT occurs when i2c\_write is called
- [GitHub #16518](https://github.com/zephyrproject-rtos/zephyr/issues/16518) - USB\_UART\_DTR\_WAIT not working on nrf52840\_pca10059
- [GitHub #16508](https://github.com/zephyrproject-rtos/zephyr/issues/16508) - tests/subsys/storage/flash\_map Instruction bus error on frdmk64 board
- [GitHub #16506](https://github.com/zephyrproject-rtos/zephyr/issues/16506) - tests/posix/fs missing ff.h
- [GitHub #16501](https://github.com/zephyrproject-rtos/zephyr/issues/16501) - Code Coverage for qemu\_x86 is not getting generated due to a build error
- [GitHub #16493](https://github.com/zephyrproject-rtos/zephyr/issues/16493) - [Coverity CID :198640]Resource leaks in /tests/net/socket/register/src/main.c
- [GitHub #16492](https://github.com/zephyrproject-rtos/zephyr/issues/16492) - [Coverity CID :198644]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #16487](https://github.com/zephyrproject-rtos/zephyr/issues/16487) - tests/kernel/timer/timer\_api/kernel.timer sporadically (high frequency) fails in CI on qemu-xtensa
- [GitHub #16483](https://github.com/zephyrproject-rtos/zephyr/issues/16483) - net: ipv6: udp: Zephyr replies to datagram with illegal checksum 0
- [GitHub #16478](https://github.com/zephyrproject-rtos/zephyr/issues/16478) - Bluetooth: Improper bonded peers handling
- [GitHub #16470](https://github.com/zephyrproject-rtos/zephyr/issues/16470) - Superfluous USB suspend after USB configured
- [GitHub #16463](https://github.com/zephyrproject-rtos/zephyr/issues/16463) - tests/subsys/settings/fcb\_init fails on second run
- [GitHub #16453](https://github.com/zephyrproject-rtos/zephyr/issues/16453) - sockets: getaddrinfo: AF\_UNSPEC handling was recently broken
- [GitHub #16432](https://github.com/zephyrproject-rtos/zephyr/issues/16432) - Weird link error of the console sample!
- [GitHub #16428](https://github.com/zephyrproject-rtos/zephyr/issues/16428) - samples/gui/lvgl does not work on PCA10056
- [GitHub #16426](https://github.com/zephyrproject-rtos/zephyr/issues/16426) - Missing included dependencies in many header files
- [GitHub #16419](https://github.com/zephyrproject-rtos/zephyr/issues/16419) - Bluetooth: XTAL feature regression
- [GitHub #16418](https://github.com/zephyrproject-rtos/zephyr/issues/16418) - drivers: watchdog: sam0: check if timeout is valid
- [GitHub #16417](https://github.com/zephyrproject-rtos/zephyr/issues/16417) - issues with can filter mode set
- [GitHub #16416](https://github.com/zephyrproject-rtos/zephyr/issues/16416) - sram size for RT1015 and RT1020 needs to be update.
- [GitHub #16415](https://github.com/zephyrproject-rtos/zephyr/issues/16415) - Build errors with C++
- [GitHub #16414](https://github.com/zephyrproject-rtos/zephyr/issues/16414) - Backport west build –pristine
- [GitHub #16413](https://github.com/zephyrproject-rtos/zephyr/issues/16413) - Missing dependency in cmake
- [GitHub #16412](https://github.com/zephyrproject-rtos/zephyr/issues/16412) - on reel\_board the consumption increases because TX pin is floating
- [GitHub #16411](https://github.com/zephyrproject-rtos/zephyr/issues/16411) - bad regex for west version check in host-tools.cmake
- [GitHub #16389](https://github.com/zephyrproject-rtos/zephyr/issues/16389) - ninja flash to intel quark d2000 zephyr
- [GitHub #16387](https://github.com/zephyrproject-rtos/zephyr/issues/16387) - STM32wb55 bluetooth samples fail
- [GitHub #16379](https://github.com/zephyrproject-rtos/zephyr/issues/16379) - net: ipv6: udp: Zephyr replies with illegal UDP checksum zero
- [GitHub #16375](https://github.com/zephyrproject-rtos/zephyr/issues/16375) - net: ipv4: udp: Zephyr does not reply to a valid datagram with checksum zero
- [GitHub #16366](https://github.com/zephyrproject-rtos/zephyr/issues/16366) - Build error on QEMU x86 and quark\_se\_c1000\_devboard
- [GitHub #16365](https://github.com/zephyrproject-rtos/zephyr/issues/16365) - lwm2m: enable with CONFIG\_NET\_RAW\_MODE
- [GitHub #16363](https://github.com/zephyrproject-rtos/zephyr/issues/16363) - Error building x\_nucleo\_iks01a1 sample on nucleo\_wb55rg after activating I2C Bus
- [GitHub #16360](https://github.com/zephyrproject-rtos/zephyr/issues/16360) - ARM: Implement configurable MPU-based stack overflow guards
- [GitHub #16354](https://github.com/zephyrproject-rtos/zephyr/issues/16354) - net: ipv6: Zephyr does not reply to fragmented packet
- [GitHub #16341](https://github.com/zephyrproject-rtos/zephyr/issues/16341) - Bluetooth: GATT Server failed to send Service Change Indication
- [GitHub #16339](https://github.com/zephyrproject-rtos/zephyr/issues/16339) - openthread: off-by-one error when calculating ot\_flash\_offset for settings
- [GitHub #16327](https://github.com/zephyrproject-rtos/zephyr/issues/16327) - doc: networking: overview has out of date info for LwM2M
- [GitHub #16326](https://github.com/zephyrproject-rtos/zephyr/issues/16326) - USB3CV Chapter 9 Tests failures
- [GitHub #16323](https://github.com/zephyrproject-rtos/zephyr/issues/16323) - net: ipv6: tcp: unexpected reply to malformed HBH in TCP/IPv6 SYN
- [GitHub #16318](https://github.com/zephyrproject-rtos/zephyr/issues/16318) - net: Network Offloading: Particle Boron
- [GitHub #16316](https://github.com/zephyrproject-rtos/zephyr/issues/16316) - ST modules organization
- [GitHub #16313](https://github.com/zephyrproject-rtos/zephyr/issues/16313) - LMP Response Timeout / LL Response Timeout (0x22) after ~40s when using LE Secure Connections
- [GitHub #16307](https://github.com/zephyrproject-rtos/zephyr/issues/16307) - cannot move location counter backwards error happen
- [GitHub #16303](https://github.com/zephyrproject-rtos/zephyr/issues/16303) - mbedtls: config-tls-generic.h: MBEDTLS\_PLATFORM\_NO\_STD\_FUNCTIONS seems ungrounded
- [GitHub #16296](https://github.com/zephyrproject-rtos/zephyr/issues/16296) - dts generation in correct for 2 registers and no-size
- [GitHub #16289](https://github.com/zephyrproject-rtos/zephyr/issues/16289) - Driver: modem ublox-sara-r4 not compiling
- [GitHub #16278](https://github.com/zephyrproject-rtos/zephyr/issues/16278) - [Zepyhr v1.14.0] Unable to update FW with mcumgr over UART
- [GitHub #16276](https://github.com/zephyrproject-rtos/zephyr/issues/16276) - net: ipv4: Zephyr replies to link-layer broadcast packet
- [GitHub #16275](https://github.com/zephyrproject-rtos/zephyr/issues/16275) - setting\_init crashes on qemu\_x86 when setting BT\_SETTINGS
- [GitHub #16273](https://github.com/zephyrproject-rtos/zephyr/issues/16273) - Calling k\_work\_submit can reenable interrupts
- [GitHub #16272](https://github.com/zephyrproject-rtos/zephyr/issues/16272) - bluetooth mesh proxy filter
- [GitHub #16268](https://github.com/zephyrproject-rtos/zephyr/issues/16268) - Add 32K RAM support for nRF51822 REVC/microbit board
- [GitHub #16257](https://github.com/zephyrproject-rtos/zephyr/issues/16257) - net: icmpv4: Zephyr sends echo reply with multicast source address
- [GitHub #16243](https://github.com/zephyrproject-rtos/zephyr/issues/16243) - std::vector push\_back() not working correctly
- [GitHub #16240](https://github.com/zephyrproject-rtos/zephyr/issues/16240) - USB Bluetooth and DFU classes cannot be enabled simultaneously on nRF52840
- [GitHub #16238](https://github.com/zephyrproject-rtos/zephyr/issues/16238) - k\_cycle\_get\_32() API is useless in some Zephyr configurations
- [GitHub #16236](https://github.com/zephyrproject-rtos/zephyr/issues/16236) - [docs] Windows installation guide, git part, is installed with non-intended configuration
- [GitHub #16234](https://github.com/zephyrproject-rtos/zephyr/issues/16234) - tests/benchmarks/latency\_measure can not calculate the real time thread switch for twr\_ke18f
- [GitHub #16229](https://github.com/zephyrproject-rtos/zephyr/issues/16229) - tests/kernel/common fails at test\_atomic on twr\_ke18f board
- [GitHub #16227](https://github.com/zephyrproject-rtos/zephyr/issues/16227) - Zephyr env: unset var in conditional activation
- [GitHub #16226](https://github.com/zephyrproject-rtos/zephyr/issues/16226) - ARM: IsInIsr(): inconsistencies between doc and implementation
- [GitHub #16225](https://github.com/zephyrproject-rtos/zephyr/issues/16225) - tests/kernel/msgq/msgq\_api twr\_ke18f fails with assert
- [GitHub #16224](https://github.com/zephyrproject-rtos/zephyr/issues/16224) - tests/subsys/storage/flash\_map meet mpu hardfault in twr\_ke18f board.
- [GitHub #16216](https://github.com/zephyrproject-rtos/zephyr/issues/16216) - tests/kernel/timer/timer\_api fails on nrf51\_pca10028 board
- [GitHub #16215](https://github.com/zephyrproject-rtos/zephyr/issues/16215) - FIFO queue data seems to get overwritten
- [GitHub #16211](https://github.com/zephyrproject-rtos/zephyr/issues/16211) - NVS: sector erase at startup (2-sectors configuration)
- [GitHub #16204](https://github.com/zephyrproject-rtos/zephyr/issues/16204) - Build STM32 : generate hex file fail
- [GitHub #16191](https://github.com/zephyrproject-rtos/zephyr/issues/16191) - boards/arm/{olimexino\_stm32, stm32\_min\_dev}: USB pinmux setup is skipped
- [GitHub #16185](https://github.com/zephyrproject-rtos/zephyr/issues/16185) - Compile error using entropy.h in C++ code
- [GitHub #16177](https://github.com/zephyrproject-rtos/zephyr/issues/16177) - STM32: Could not compile with CONFIG\_PINMUX=n
- [GitHub #16170](https://github.com/zephyrproject-rtos/zephyr/issues/16170) - CI fails because warning in LOG\_ERR() in drivers/i2s\_ll\_stm32.c
- [GitHub #16164](https://github.com/zephyrproject-rtos/zephyr/issues/16164) - [Coverity CID :198584]Uninitialized variables in /drivers/led/ht16k33.c
- [GitHub #16163](https://github.com/zephyrproject-rtos/zephyr/issues/16163) - [Coverity CID :198587]Incorrect expression in /tests/subsys/usb/desc\_sections/src/desc\_sections.c
- [GitHub #16162](https://github.com/zephyrproject-rtos/zephyr/issues/16162) - [Coverity CID :198588]Control flow issues in /drivers/gpio/gpio\_cc13xx\_cc26xx.c
- [GitHub #16161](https://github.com/zephyrproject-rtos/zephyr/issues/16161) - [Coverity CID :198589]Control flow issues in /drivers/i2c/i2c\_sam0.c
- [GitHub #16160](https://github.com/zephyrproject-rtos/zephyr/issues/16160) - [Coverity CID :198590]Control flow issues in /drivers/i2c/i2c\_sam0.c
- [GitHub #16159](https://github.com/zephyrproject-rtos/zephyr/issues/16159) - [Coverity CID :198591]Control flow issues in /drivers/sensor/adxl362/adxl362.c
- [GitHub #16158](https://github.com/zephyrproject-rtos/zephyr/issues/16158) - LwM2M: Fix incorrect last\_block handling in the firmware write callback
- [GitHub #16156](https://github.com/zephyrproject-rtos/zephyr/issues/16156) - Remove the LWM2M maximum number of instances limitation
- [GitHub #16155](https://github.com/zephyrproject-rtos/zephyr/issues/16155) - drivers: can: wrong value used for filter mode set
- [GitHub #16154](https://github.com/zephyrproject-rtos/zephyr/issues/16154) - Fix various issues with handling of floating values within the LWM2M subsystem
- [GitHub #16148](https://github.com/zephyrproject-rtos/zephyr/issues/16148) - ARM: Enable building with TRUSTED\_EXECUTION\_SECURE
- [GitHub #16145](https://github.com/zephyrproject-rtos/zephyr/issues/16145) - question: Using OpenThread API in Zephyr application
- [GitHub #16143](https://github.com/zephyrproject-rtos/zephyr/issues/16143) - posix: clock\_settime calculates the base time incorrectly
- [GitHub #16142](https://github.com/zephyrproject-rtos/zephyr/issues/16142) - NET: llmnr responder sends malformed packets
- [GitHub #16141](https://github.com/zephyrproject-rtos/zephyr/issues/16141) - posix: CONFIG\_POSIX\_API and CONFIG\_NET\_SOCKETS\_POSIX\_NAMES don’t make sense to use together, and conflict when doing so
- [GitHub #16138](https://github.com/zephyrproject-rtos/zephyr/issues/16138) - is this right for clock announcing in every CORE?
- [GitHub #16132](https://github.com/zephyrproject-rtos/zephyr/issues/16132) - The nRF mesh APP report “Invalid Publish Parameters”
- [GitHub #16110](https://github.com/zephyrproject-rtos/zephyr/issues/16110) - net: arp: request from own hardware but different IP address not dropped
- [GitHub #16107](https://github.com/zephyrproject-rtos/zephyr/issues/16107) - Using bt\_gatt\_read() with ‘by\_uuid’ method returns 3 extra bytes
- [GitHub #16103](https://github.com/zephyrproject-rtos/zephyr/issues/16103) - nrf5 802.15.4 driver requires Log subsys to be enabled
- [GitHub #16098](https://github.com/zephyrproject-rtos/zephyr/issues/16098) - net: arp: sender hardware address not used by ICMP/TCP/UDP
- [GitHub #16090](https://github.com/zephyrproject-rtos/zephyr/issues/16090) - mpu align support for code relocation on non-XIP system
- [GitHub #16089](https://github.com/zephyrproject-rtos/zephyr/issues/16089) - Mcux Ethernet driver does not detect carrier anymore (it’s alway on)
- [GitHub #16080](https://github.com/zephyrproject-rtos/zephyr/issues/16080) - Zephyr UART shell crashes on start if main() is blocked
- [GitHub #16079](https://github.com/zephyrproject-rtos/zephyr/issues/16079) - SAM0/SAMR SERIAL subsystem broken?
- [GitHub #16078](https://github.com/zephyrproject-rtos/zephyr/issues/16078) - Shell subsystem or SERIAL no longer works on SAM0/SAMR
- [GitHub #16072](https://github.com/zephyrproject-rtos/zephyr/issues/16072) - boards/up\_squared: k\_sleep() too long with local APIC timer
- [GitHub #16054](https://github.com/zephyrproject-rtos/zephyr/issues/16054) - Bluetooth sample app ‘peripheral’ failing to build for nRF52840
- [GitHub #16052](https://github.com/zephyrproject-rtos/zephyr/issues/16052) - Adafruit Trinket M0 Bossac Offset is Wrong
- [GitHub #16046](https://github.com/zephyrproject-rtos/zephyr/issues/16046) - modules are being processed too late.
- [GitHub #16042](https://github.com/zephyrproject-rtos/zephyr/issues/16042) - NDP should be enhanced with Security, RFC 3971
- [GitHub #16027](https://github.com/zephyrproject-rtos/zephyr/issues/16027) - support for no-flash systems
- [GitHub #16025](https://github.com/zephyrproject-rtos/zephyr/issues/16025) - webusb example app not reading data
- [GitHub #16012](https://github.com/zephyrproject-rtos/zephyr/issues/16012) - Source IP address for DHCP renewal messages is unset
- [GitHub #16010](https://github.com/zephyrproject-rtos/zephyr/issues/16010) - Coverage reporting fails on many tests
- [GitHub #16006](https://github.com/zephyrproject-rtos/zephyr/issues/16006) - The ArgonKey board documentation needs to align to the official information
- [GitHub #16002](https://github.com/zephyrproject-rtos/zephyr/issues/16002) - the spi base reg address in arc\_iot.dtsi has an error
- [GitHub #16001](https://github.com/zephyrproject-rtos/zephyr/issues/16001) - ARC iotdk supports MPU and fpu in hardware but not enabled in kconfig
- [GitHub #16000](https://github.com/zephyrproject-rtos/zephyr/issues/16000) - We need a CI check for commas in CODEOWNERS
- [GitHub #15998](https://github.com/zephyrproject-rtos/zephyr/issues/15998) - CODEOWNERS is broken (Again)
- [GitHub #15997](https://github.com/zephyrproject-rtos/zephyr/issues/15997) - Fix compile warning in samples/net/sockets/dumb\_http\_server
- [GitHub #15996](https://github.com/zephyrproject-rtos/zephyr/issues/15996) - tests/kernel/sched/schedule\_api/testcase.yaml#kernel.sched.slice\_reset fails on nrf52840\_pca10056, nrf52\_pca10040, nrf51\_pca10028
- [GitHub #15991](https://github.com/zephyrproject-rtos/zephyr/issues/15991) - [Coverity CID :198389]Memory - illegal accesses in /subsys/settings/src/settings\_runtime.c
- [GitHub #15990](https://github.com/zephyrproject-rtos/zephyr/issues/15990) - [Coverity CID :198390]Memory - illegal accesses in /subsys/settings/src/settings\_runtime.c
- [GitHub #15989](https://github.com/zephyrproject-rtos/zephyr/issues/15989) - [Coverity CID :198391]Memory - illegal accesses in /subsys/settings/src/settings\_runtime.c
- [GitHub #15988](https://github.com/zephyrproject-rtos/zephyr/issues/15988) - [Coverity CID :198392]Insecure data handling in /tests/net/socket/getaddrinfo/src/main.c
- [GitHub #15987](https://github.com/zephyrproject-rtos/zephyr/issues/15987) - [Coverity CID :198393]Error handling issues in /tests/net/socket/socket\_helpers.h
- [GitHub #15986](https://github.com/zephyrproject-rtos/zephyr/issues/15986) - [Coverity CID :198394]Error handling issues in /tests/net/socket/socket\_helpers.h
- [GitHub #15985](https://github.com/zephyrproject-rtos/zephyr/issues/15985) - [Coverity CID :198395]Memory - corruptions in /soc/arm/microchip\_mec/mec1501/soc.c
- [GitHub #15983](https://github.com/zephyrproject-rtos/zephyr/issues/15983) - Kernel tests assume SYS\_CLOCK\_TICKS\_PER\_SEC=100
- [GitHub #15981](https://github.com/zephyrproject-rtos/zephyr/issues/15981) - ARM: k\_float\_disable() as system call
- [GitHub #15975](https://github.com/zephyrproject-rtos/zephyr/issues/15975) - Openthread - fault with dual network interfaces
- [GitHub #15971](https://github.com/zephyrproject-rtos/zephyr/issues/15971) - Fail to connect sample bluetooth HID with Tizen OS (BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION)
- [GitHub #15970](https://github.com/zephyrproject-rtos/zephyr/issues/15970) - samples: microbit pong demo
- [GitHub #15964](https://github.com/zephyrproject-rtos/zephyr/issues/15964) - ARM: Cortex-M: enhance Sharing Floating-Point Registers Mode
- [GitHub #15961](https://github.com/zephyrproject-rtos/zephyr/issues/15961) - bug: west: ‘west flash’ doesn’t use specified hex file
- [GitHub #15941](https://github.com/zephyrproject-rtos/zephyr/issues/15941) - Stale 1.3.99 documentation under /latest
- [GitHub #15924](https://github.com/zephyrproject-rtos/zephyr/issues/15924) - Bluetooth: PTS: GATT server tests fail after merge of #15524
- [GitHub #15922](https://github.com/zephyrproject-rtos/zephyr/issues/15922) - BLE mesh:The Provisioner APP can’t find the micro:bit which is running the mesh sample
- [GitHub #15918](https://github.com/zephyrproject-rtos/zephyr/issues/15918) - stm32f7 GPIO Ports F & G Disabled by Default
- [GitHub #15917](https://github.com/zephyrproject-rtos/zephyr/issues/15917) - USB disconnect/reconnect
- [GitHub #15916](https://github.com/zephyrproject-rtos/zephyr/issues/15916) - [BLE] Mesh example qemu kernel panic
- [GitHub #15911](https://github.com/zephyrproject-rtos/zephyr/issues/15911) - Stack size is smaller than it should be
- [GitHub #15909](https://github.com/zephyrproject-rtos/zephyr/issues/15909) - stm32f7: DTCM included in sram0
- [GitHub #15906](https://github.com/zephyrproject-rtos/zephyr/issues/15906) - WEST ERROR: extension command build was improperly defined
- [GitHub #15904](https://github.com/zephyrproject-rtos/zephyr/issues/15904) - concerns with use of CONFIG\_BT\_MESH\_RPL\_STORE\_TIMEOUT in examples
- [GitHub #15893](https://github.com/zephyrproject-rtos/zephyr/issues/15893) - code coverage is not tested in CI
- [GitHub #15884](https://github.com/zephyrproject-rtos/zephyr/issues/15884) - tests/net/socket/getaddrinfo fails on mps2\_an385
- [GitHub #15878](https://github.com/zephyrproject-rtos/zephyr/issues/15878) - tests/net/lib/mqtt\_publisher/net.mqtt.tls fails to build on sam\_e70\_xplained
- [GitHub #15877](https://github.com/zephyrproject-rtos/zephyr/issues/15877) - all qemu\_x86\_64 tests hang on Ubuntu 18.04
- [GitHub #15864](https://github.com/zephyrproject-rtos/zephyr/issues/15864) - disk partitioning should not specified in DTS
- [GitHub #15844](https://github.com/zephyrproject-rtos/zephyr/issues/15844) - Network management API should support user space
- [GitHub #15842](https://github.com/zephyrproject-rtos/zephyr/issues/15842) - cdc\_acm: stm32: uart\_fifo\_fill() can’t transmit data out
- [GitHub #15835](https://github.com/zephyrproject-rtos/zephyr/issues/15835) - “#if XIP” block in qemu\_x86 DTS always evaluates to false
- [GitHub #15831](https://github.com/zephyrproject-rtos/zephyr/issues/15831) - qemu\_x86 DTS does not reflect actual emulated hardware layout
- [GitHub #15827](https://github.com/zephyrproject-rtos/zephyr/issues/15827) - ARM: Update ARM CMSIS to latest version
- [GitHub #15823](https://github.com/zephyrproject-rtos/zephyr/issues/15823) - Build failure for spi\_loopback on atsamr21\_xpro
- [GitHub #15817](https://github.com/zephyrproject-rtos/zephyr/issues/15817) - nrf52: HFXO is not turned off as expected
- [GitHub #15814](https://github.com/zephyrproject-rtos/zephyr/issues/15814) - [Coverity CID :186196]Unchecked return value in samples/sensor/lsm6dsl/src/main.c
- [GitHub #15794](https://github.com/zephyrproject-rtos/zephyr/issues/15794) - mps2\_an385 crashes if CONFIG\_INIT\_STACKS=y and CONFIG\_COVERAGE=y
- [GitHub #15789](https://github.com/zephyrproject-rtos/zephyr/issues/15789) - Networking documentation missing
- [GitHub #15778](https://github.com/zephyrproject-rtos/zephyr/issues/15778) - [Coverity CID :198001]Control flow issues in /subsys/bluetooth/host/mesh/settings.c
- [GitHub #15777](https://github.com/zephyrproject-rtos/zephyr/issues/15777) - [Coverity CID :198002]Null pointer dereferences in /subsys/net/l2/ethernet/arp.c
- [GitHub #15776](https://github.com/zephyrproject-rtos/zephyr/issues/15776) - [Coverity CID :198003]Error handling issues in /tests/net/net\_pkt/src/main.c
- [GitHub #15775](https://github.com/zephyrproject-rtos/zephyr/issues/15775) - [Coverity CID :198005]Memory - corruptions in /subsys/bluetooth/shell/gatt.c
- [GitHub #15774](https://github.com/zephyrproject-rtos/zephyr/issues/15774) - [Coverity CID :198006]Control flow issues in /subsys/bluetooth/host/settings.c
- [GitHub #15773](https://github.com/zephyrproject-rtos/zephyr/issues/15773) - [Coverity CID :198007]Memory - corruptions in /subsys/bluetooth/host/hci\_core.c
- [GitHub #15772](https://github.com/zephyrproject-rtos/zephyr/issues/15772) - [Coverity CID :198009]Memory - corruptions in /subsys/bluetooth/shell/gatt.c
- [GitHub #15771](https://github.com/zephyrproject-rtos/zephyr/issues/15771) - [Coverity CID :198010]Control flow issues in /samples/boards/nrf52/mesh/onoff\_level\_lighting\_vnd\_app/src/storage.c
- [GitHub #15770](https://github.com/zephyrproject-rtos/zephyr/issues/15770) - [Coverity CID :198011]Incorrect expression in /tests/subsys/usb/desc\_sections/src/desc\_sections.c
- [GitHub #15769](https://github.com/zephyrproject-rtos/zephyr/issues/15769) - [Coverity CID :198012]Memory - corruptions in /drivers/flash/flash\_simulator.c
- [GitHub #15768](https://github.com/zephyrproject-rtos/zephyr/issues/15768) - [Coverity CID :198013]Control flow issues in /subsys/bluetooth/host/mesh/settings.c
- [GitHub #15767](https://github.com/zephyrproject-rtos/zephyr/issues/15767) - [Coverity CID :198014]Memory - corruptions in /drivers/flash/flash\_simulator.c
- [GitHub #15766](https://github.com/zephyrproject-rtos/zephyr/issues/15766) - [Coverity CID :198016]Security best practices violations in /subsys/settings/src/settings\_runtime.c
- [GitHub #15765](https://github.com/zephyrproject-rtos/zephyr/issues/15765) - [Coverity CID :198018]Control flow issues in /subsys/bluetooth/host/mesh/settings.c
- [GitHub #15764](https://github.com/zephyrproject-rtos/zephyr/issues/15764) - [Coverity CID :198019]Security best practices violations in /subsys/settings/src/settings\_runtime.c
- [GitHub #15763](https://github.com/zephyrproject-rtos/zephyr/issues/15763) - [Coverity CID :198021]Control flow issues in /drivers/clock\_control/clock\_stm32\_ll\_mp1x.c
- [GitHub #15762](https://github.com/zephyrproject-rtos/zephyr/issues/15762) - [Coverity CID :198022]Security best practices violations in /subsys/settings/src/settings\_runtime.c
- [GitHub #15759](https://github.com/zephyrproject-rtos/zephyr/issues/15759) - usb: cdc\_acm: uart\_line\_ctrl\_set(dev, LINE\_CTRL\_DTR, &dtr) should always return 0 if USB port is not opened by host
- [GitHub #15751](https://github.com/zephyrproject-rtos/zephyr/issues/15751) - Incorrect flash map
- [GitHub #15749](https://github.com/zephyrproject-rtos/zephyr/issues/15749) - [question] errors using custom command in CMakeLists.txt
- [GitHub #15748](https://github.com/zephyrproject-rtos/zephyr/issues/15748) - ‘ninja flash’ does not work for IMXRT1052 target
- [GitHub #15736](https://github.com/zephyrproject-rtos/zephyr/issues/15736) - Generalize and improve async context for SPI, ADC, etc.
- [GitHub #15734](https://github.com/zephyrproject-rtos/zephyr/issues/15734) - Power management doesn’t work with CONFIG\_I2C=y on nRF52
- [GitHub #15733](https://github.com/zephyrproject-rtos/zephyr/issues/15733) - Bluetooth: controller: Central Encryption setup overlaps Length Request procedure
- [GitHub #15728](https://github.com/zephyrproject-rtos/zephyr/issues/15728) - tests/benchmarks/timing\_info: wrong value for context switch duration
- [GitHub #15720](https://github.com/zephyrproject-rtos/zephyr/issues/15720) - “z\_clock\_elapsed” implementation seems to be missing #linking #sched
- [GitHub #15719](https://github.com/zephyrproject-rtos/zephyr/issues/15719) - tests/ztests/mock/ : Stuck at test\_parameter\_tests
- [GitHub #15714](https://github.com/zephyrproject-rtos/zephyr/issues/15714) - samples/bluetooth/peripheral: could not connect with disco\_l475\_iot1 board
- [GitHub #15710](https://github.com/zephyrproject-rtos/zephyr/issues/15710) - [question] how about the current consumption on NRF52DK running power\_mgr sample?
- [GitHub #15709](https://github.com/zephyrproject-rtos/zephyr/issues/15709) - CODEOWNERS ignored in GitHub
- [GitHub #15706](https://github.com/zephyrproject-rtos/zephyr/issues/15706) - tunslip6: main: open: No such file or directory
- [GitHub #15698](https://github.com/zephyrproject-rtos/zephyr/issues/15698) - bluetooth: bt\_conn: No proper ID handling
- [GitHub #15696](https://github.com/zephyrproject-rtos/zephyr/issues/15696) - [question] why bt\_setting is dependant of printk in menuconfig?
- [GitHub #15679](https://github.com/zephyrproject-rtos/zephyr/issues/15679) - Can GPTP support multiple slave nodes
- [GitHub #15678](https://github.com/zephyrproject-rtos/zephyr/issues/15678) - Watchdog peripheral api docs aren’t generated correctly.
- [GitHub #15675](https://github.com/zephyrproject-rtos/zephyr/issues/15675) - DTS question about pinmix/GPIO
- [GitHub #15672](https://github.com/zephyrproject-rtos/zephyr/issues/15672) - net: socket send return error(-110) when http request 100 times
- [GitHub #15668](https://github.com/zephyrproject-rtos/zephyr/issues/15668) - Support request: Issue with documentation warning
- [GitHub #15664](https://github.com/zephyrproject-rtos/zephyr/issues/15664) - Zephyr modules failure report
- [GitHub #15652](https://github.com/zephyrproject-rtos/zephyr/issues/15652) - document the mailing list for nightly build results
- [GitHub #15639](https://github.com/zephyrproject-rtos/zephyr/issues/15639) - [question] how to get the bd\_addr from scan callback as shown on nrf-connect app?
- [GitHub #15637](https://github.com/zephyrproject-rtos/zephyr/issues/15637) - Support of device tree gpio-map
- [GitHub #15627](https://github.com/zephyrproject-rtos/zephyr/issues/15627) - Application compiled with CONFIG\_POSIX\_API doesn’t have access to POSIX headers
- [GitHub #15625](https://github.com/zephyrproject-rtos/zephyr/issues/15625) - target\_compile\_features in CMakeLists.txt triggers an error
- [GitHub #15622](https://github.com/zephyrproject-rtos/zephyr/issues/15622) - NXP RT10XX: Load code to ITCM
- [GitHub #15612](https://github.com/zephyrproject-rtos/zephyr/issues/15612) - bt\_set\_id\_addr() to allow public address as argument
- [GitHub #15608](https://github.com/zephyrproject-rtos/zephyr/issues/15608) - [question] my board won’t boot without debugger attached but no issue using nordic SDK
- [GitHub #15607](https://github.com/zephyrproject-rtos/zephyr/issues/15607) - nRF52: 2.4 GHz proprietary RF support
- [GitHub #15606](https://github.com/zephyrproject-rtos/zephyr/issues/15606) - trickle.c can’t work for multiple triggerings
- [GitHub #15605](https://github.com/zephyrproject-rtos/zephyr/issues/15605) - Unaligned memory access by ldrd
- [GitHub #15601](https://github.com/zephyrproject-rtos/zephyr/issues/15601) - pwm: nRF default prescalar value is wrong
- [GitHub #15597](https://github.com/zephyrproject-rtos/zephyr/issues/15597) - [question] How to include mesh related header files in my own source file
- [GitHub #15596](https://github.com/zephyrproject-rtos/zephyr/issues/15596) - net: Zephyr’s SNTP API time precision is not adequate
- [GitHub #15594](https://github.com/zephyrproject-rtos/zephyr/issues/15594) - net shell “net tcp send” command failed when repeated many times
- [GitHub #15588](https://github.com/zephyrproject-rtos/zephyr/issues/15588) - Does zephyr support different time slices for each thread?
- [GitHub #15587](https://github.com/zephyrproject-rtos/zephyr/issues/15587) - Zephyr was unable to find the toolchain
- [GitHub #15580](https://github.com/zephyrproject-rtos/zephyr/issues/15580) - SAMD21 Adafruit examples no longer run on boards
- [GitHub #15571](https://github.com/zephyrproject-rtos/zephyr/issues/15571) - Fix sanitycheck failures for v2m\_musca\_b1\_nonsecure
- [GitHub #15570](https://github.com/zephyrproject-rtos/zephyr/issues/15570) - Unbonded peripheral gets ‘Tx Buffer Overflow’ when erasing bond on master
- [GitHub #15565](https://github.com/zephyrproject-rtos/zephyr/issues/15565) - undefined references to ‘sys\_rand32\_get’
- [GitHub #15558](https://github.com/zephyrproject-rtos/zephyr/issues/15558) - support for power-of-two MPUs on non-XIP systems
- [GitHub #15551](https://github.com/zephyrproject-rtos/zephyr/issues/15551) - CMake enables -fmacro-prefix-map on GCC 7
- [GitHub #15549](https://github.com/zephyrproject-rtos/zephyr/issues/15549) - [FCB question] Is it true that fcb storage won’t overwrite old records which limits the max num?
- [GitHub #15546](https://github.com/zephyrproject-rtos/zephyr/issues/15546) - tests/kernel/mem\_protect/protection/: Reached unreachable code
- [GitHub #15526](https://github.com/zephyrproject-rtos/zephyr/issues/15526) - Unhandled identity in bt\_conn\_create\_slave\_le
- [GitHub #15522](https://github.com/zephyrproject-rtos/zephyr/issues/15522) - Extra padding in IPv4 link local ARP packets
- [GitHub #15520](https://github.com/zephyrproject-rtos/zephyr/issues/15520) - tests/ztest/mock: test\_multi\_value\_test: Unused mocked return value
- [GitHub #15516](https://github.com/zephyrproject-rtos/zephyr/issues/15516) - Implementation of CONFIG\_MAX\_PTHREAD\_COUNT
- [GitHub #15513](https://github.com/zephyrproject-rtos/zephyr/issues/15513) - nRF timer unnecessary configuration?
- [GitHub #15508](https://github.com/zephyrproject-rtos/zephyr/issues/15508) - No space to store CCC cfg
- [GitHub #15507](https://github.com/zephyrproject-rtos/zephyr/issues/15507) - NRF52840: usb composite MSC + HID (with CONFIG\_ENABLE\_HID\_INT\_OUT\_EP)
- [GitHub #15504](https://github.com/zephyrproject-rtos/zephyr/issues/15504) - Can I use one custom random static bd\_addr before provision?
- [GitHub #15501](https://github.com/zephyrproject-rtos/zephyr/issues/15501) - smp\_svr build issue
- [GitHub #15499](https://github.com/zephyrproject-rtos/zephyr/issues/15499) - gpio\_intel\_apl: gpio\_pin\_read() pin value doesn’t match documentation
- [GitHub #15497](https://github.com/zephyrproject-rtos/zephyr/issues/15497) - USB DFU: STM32: usb dfu mode doesn’t work
- [GitHub #15495](https://github.com/zephyrproject-rtos/zephyr/issues/15495) - tests/drivers/spi/spi\_loopback/peripheral.spi fails to build on several boards
- [GitHub #15486](https://github.com/zephyrproject-rtos/zephyr/issues/15486) - usb composite MSC + HID (with CONFIG\_ENABLE\_HID\_INT\_OUT\_EP)
- [GitHub #15483](https://github.com/zephyrproject-rtos/zephyr/issues/15483) - add mpu and fpu support for arc iotdk
- [GitHub #15481](https://github.com/zephyrproject-rtos/zephyr/issues/15481) - object\_access in common-rom.ld missed GROUP\_LINK\_IN(ROMABLE\_REGION)
- [GitHub #15477](https://github.com/zephyrproject-rtos/zephyr/issues/15477) - Zephyr network stack will up the Ethernet interface after its driver initialized (regardless of actual status)
- [GitHub #15472](https://github.com/zephyrproject-rtos/zephyr/issues/15472) - DNS resolver sample sends only one A query
- [GitHub #15465](https://github.com/zephyrproject-rtos/zephyr/issues/15465) - Fix build failures for test\_newlib & tests/lib/mem\_alloc/libraries.libc.newlib w/ARM gcc
- [GitHub #15451](https://github.com/zephyrproject-rtos/zephyr/issues/15451) - doc: settings Misleading examples
- [GitHub #15448](https://github.com/zephyrproject-rtos/zephyr/issues/15448) - help to use zephyr-ninja flash of st\_nucleo\_l476rg
- [GitHub #15447](https://github.com/zephyrproject-rtos/zephyr/issues/15447) - sanitycheck –coverage -p qemu\_x86: Fatal failures with tests/kernel/pipe/pipe/kernel.pipe
- [GitHub #15446](https://github.com/zephyrproject-rtos/zephyr/issues/15446) - ssanitycheck –coverage -p mps2\_an385: Some remaing test cases that are still failing
- [GitHub #15444](https://github.com/zephyrproject-rtos/zephyr/issues/15444) - Error initiating sdhc disk
- [GitHub #15443](https://github.com/zephyrproject-rtos/zephyr/issues/15443) - usb\_dc\_stm32: Missing semaphore initialization and missing pin remapping configuration
- [GitHub #15419](https://github.com/zephyrproject-rtos/zephyr/issues/15419) - reset and halt function
- [GitHub #15411](https://github.com/zephyrproject-rtos/zephyr/issues/15411) - tests/kernel/critical: Continuous reboot at test\_critical
- [GitHub #15408](https://github.com/zephyrproject-rtos/zephyr/issues/15408) - [Coverity CID :197596]Memory - corruptions in /tests/net/lib/mqtt\_packet/src/mqtt\_packet.c
- [GitHub #15391](https://github.com/zephyrproject-rtos/zephyr/issues/15391) - [Coverity CID :197613]Possible Control flow issues in /subsys/net/ip/net\_core.c
- [GitHub #15374](https://github.com/zephyrproject-rtos/zephyr/issues/15374) - PR 15230 introduces test failure for particle\_argon
- [GitHub #15373](https://github.com/zephyrproject-rtos/zephyr/issues/15373) - IPv4 link local packets are not sent with ARP ethernet type
- [GitHub #15355](https://github.com/zephyrproject-rtos/zephyr/issues/15355) - Driver for U-Blox SARA modem (used by Particle Boron)
- [GitHub #15354](https://github.com/zephyrproject-rtos/zephyr/issues/15354) - counter: stm32: Issue with LSE clock source selection
- [GitHub #15339](https://github.com/zephyrproject-rtos/zephyr/issues/15339) - RISC-V: RV32M1: Load access fault when accessing GPIO port E
- [GitHub #15334](https://github.com/zephyrproject-rtos/zephyr/issues/15334) - Unable to reset nRF52840 from nRF9160 on pca10090 DK
- [GitHub #15331](https://github.com/zephyrproject-rtos/zephyr/issues/15331) - CONFIG\_CODE\_DATA\_RELOCATION does not work with Cache enabled MCUs.
- [GitHub #15316](https://github.com/zephyrproject-rtos/zephyr/issues/15316) - printf causing usage fault
- [GitHub #15315](https://github.com/zephyrproject-rtos/zephyr/issues/15315) - doc: simplify cmake examples thanks to cmake’s new -B option
- [GitHub #15305](https://github.com/zephyrproject-rtos/zephyr/issues/15305) - add QEMU target for armv8-M with MPU support
- [GitHub #15282](https://github.com/zephyrproject-rtos/zephyr/issues/15282) - Enhance networking tests/net/all tests
- [GitHub #15279](https://github.com/zephyrproject-rtos/zephyr/issues/15279) - mempool alignment might cause a memory block allocated twice
- [GitHub #15272](https://github.com/zephyrproject-rtos/zephyr/issues/15272) - sanitycheck reports build errors as “handler crash”
- [GitHub #15246](https://github.com/zephyrproject-rtos/zephyr/issues/15246) - doc: confusion about dtc version
- [GitHub #15232](https://github.com/zephyrproject-rtos/zephyr/issues/15232) - tests/bluetooth/tester fails build if CONFIG\_TEST\_USERSPACE=n
- [GitHub #15193](https://github.com/zephyrproject-rtos/zephyr/issues/15193) - tests/net/socket/getaddrinfo tests too little
- [GitHub #15180](https://github.com/zephyrproject-rtos/zephyr/issues/15180) - testing flash driver clients in CI
- [GitHub #15159](https://github.com/zephyrproject-rtos/zephyr/issues/15159) - undefined reference to ‘bsearch’ #stdlib
- [GitHub #15156](https://github.com/zephyrproject-rtos/zephyr/issues/15156) - GH labels reorg
- [GitHub #15144](https://github.com/zephyrproject-rtos/zephyr/issues/15144) - West: how to set up for external modules
- [GitHub #15139](https://github.com/zephyrproject-rtos/zephyr/issues/15139) - implement sys\_sem that can reside in user memory
- [GitHub #15133](https://github.com/zephyrproject-rtos/zephyr/issues/15133) - Is the level2 interrupt supported for ARM cortex-M0P core?
- [GitHub #15119](https://github.com/zephyrproject-rtos/zephyr/issues/15119) - GPIO callback not disabled from an interrupt
- [GitHub #15116](https://github.com/zephyrproject-rtos/zephyr/issues/15116) - nrfx\_twim: (nRF52) driver unable to perform i2c\_burst\_write() correctly
- [GitHub #15115](https://github.com/zephyrproject-rtos/zephyr/issues/15115) - ARM: Cortex-M: enhance non-sharing floating point services
- [GitHub #15074](https://github.com/zephyrproject-rtos/zephyr/issues/15074) - ARM: Fix/Enhance Floating Point for ARM Cortex-M architecture
- [GitHub #15046](https://github.com/zephyrproject-rtos/zephyr/issues/15046) - Native\_posix: command line handling: Hint users why an option does not exist
- [GitHub #15003](https://github.com/zephyrproject-rtos/zephyr/issues/15003) - init\_iface in net\_if.c should check api->init
- [GitHub #14997](https://github.com/zephyrproject-rtos/zephyr/issues/14997) - Convert samples/sensor/bme280/src/main.c to use printk instead of printf
- [GitHub #14970](https://github.com/zephyrproject-rtos/zephyr/issues/14970) - samples/drivers/watchdog: Not showing “Waiting for reset…” for nrf boards
- [GitHub #14918](https://github.com/zephyrproject-rtos/zephyr/issues/14918) - olimexino stm32 CAN errors
- [GitHub #14904](https://github.com/zephyrproject-rtos/zephyr/issues/14904) - Sanitycheck report not clear if built or ran a test
- [GitHub #14828](https://github.com/zephyrproject-rtos/zephyr/issues/14828) - ARM: MPU-based HW thread stack protection not working properly when building with CONFIG\_FLOAT
- [GitHub #14826](https://github.com/zephyrproject-rtos/zephyr/issues/14826) - USB reset in suspended state
- [GitHub #14791](https://github.com/zephyrproject-rtos/zephyr/issues/14791) - Bluetooth: GATT Notification callbacks should have conn as argument
- [GitHub #14769](https://github.com/zephyrproject-rtos/zephyr/issues/14769) - kernel/userspace.c: Improve code coverage to 100%
- [GitHub #14744](https://github.com/zephyrproject-rtos/zephyr/issues/14744) - ARM: Core Stack Improvements/Bug fixes for 2.0 release
- [GitHub #14736](https://github.com/zephyrproject-rtos/zephyr/issues/14736) - kernel/include/kswap.h: Improve code coverage to 100%
- [GitHub #14734](https://github.com/zephyrproject-rtos/zephyr/issues/14734) - kernel/include/kernel\_structs.h: Improve code coverage to 100%
- [GitHub #14733](https://github.com/zephyrproject-rtos/zephyr/issues/14733) - kernel/work\_q.c: Improve code coverage to 100%
- [GitHub #14731](https://github.com/zephyrproject-rtos/zephyr/issues/14731) - kernel/userspace\_handler.c: Improve code coverage to 100%
- [GitHub #14730](https://github.com/zephyrproject-rtos/zephyr/issues/14730) - kernel/userspace.c: Improve code coverage to 100%
- [GitHub #14729](https://github.com/zephyrproject-rtos/zephyr/issues/14729) - kernel/timer.c: Improve code coverage to 100%
- [GitHub #14728](https://github.com/zephyrproject-rtos/zephyr/issues/14728) - kernel/timeout.c: Improve code coverage to 100%
- [GitHub #14727](https://github.com/zephyrproject-rtos/zephyr/issues/14727) - kernel/thread\_abort.c: Improve code coverage to 100%
- [GitHub #14726](https://github.com/zephyrproject-rtos/zephyr/issues/14726) - kernel/thread.c: Improve code coverage to 100%
- [GitHub #14725](https://github.com/zephyrproject-rtos/zephyr/issues/14725) - kernel/system\_work\_q.c: Improve code coverage to 100%
- [GitHub #14724](https://github.com/zephyrproject-rtos/zephyr/issues/14724) - kernel/stack.c: Improve code coverage to 100%
- [GitHub #14723](https://github.com/zephyrproject-rtos/zephyr/issues/14723) - kernel/sem.c: Improve code coverage to 100%
- [GitHub #14722](https://github.com/zephyrproject-rtos/zephyr/issues/14722) - kernel/sched.c: Improve code coverage to 100%
- [GitHub #14721](https://github.com/zephyrproject-rtos/zephyr/issues/14721) - kernel/queue.c: Improve code coverage to 100%
- [GitHub #14720](https://github.com/zephyrproject-rtos/zephyr/issues/14720) - kernel/poll.c: Improve code coverage to 100%
- [GitHub #14719](https://github.com/zephyrproject-rtos/zephyr/issues/14719) - kernel/pipes.c: Improve code coverage to 100%
- [GitHub #14718](https://github.com/zephyrproject-rtos/zephyr/issues/14718) - kernel/mutex.c: Improve code coverage to 100%
- [GitHub #14717](https://github.com/zephyrproject-rtos/zephyr/issues/14717) - kernel/msg\_q.c: Improve code coverage to 100%
- [GitHub #14716](https://github.com/zephyrproject-rtos/zephyr/issues/14716) - kernel/mempool.c: Improve code coverage to 100%
- [GitHub #14715](https://github.com/zephyrproject-rtos/zephyr/issues/14715) - kernel/mem\_slab.c: Improve code coverage to 100%
- [GitHub #14713](https://github.com/zephyrproject-rtos/zephyr/issues/14713) - kernel/mem\_domain.c: Improve code coverage to 100%
- [GitHub #14712](https://github.com/zephyrproject-rtos/zephyr/issues/14712) - kernel/mailbox.c: Improve coverage to 100%
- [GitHub #14711](https://github.com/zephyrproject-rtos/zephyr/issues/14711) - kernel/idle.c: Improve code coverage to 100%
- [GitHub #14710](https://github.com/zephyrproject-rtos/zephyr/issues/14710) - kernel/errno.c: Improve code coverage to 100%
- [GitHub #14709](https://github.com/zephyrproject-rtos/zephyr/issues/14709) - kernel/device.c: Improve code coverage to 100%
- [GitHub #14708](https://github.com/zephyrproject-rtos/zephyr/issues/14708) - kernel/include/ksched.h: Improve code coverage to 100%
- [GitHub #14707](https://github.com/zephyrproject-rtos/zephyr/issues/14707) - kernel/include/kernel\_offsets.h: Improve code coverage to 100%
- [GitHub #14706](https://github.com/zephyrproject-rtos/zephyr/issues/14706) - kernel/include/kernel\_internal.h: Imrpove code coverage to 100%
- [GitHub #14705](https://github.com/zephyrproject-rtos/zephyr/issues/14705) - kernel/smp.c: Improve code coverage to 100%
- [GitHub #14704](https://github.com/zephyrproject-rtos/zephyr/issues/14704) - kernel/int\_latency\_bench.c: Improve code coverage to 100%
- [GitHub #14703](https://github.com/zephyrproject-rtos/zephyr/issues/14703) - kernel/compiler\_stack\_protect.c: Improve code coverage to 100%
- [GitHub #14702](https://github.com/zephyrproject-rtos/zephyr/issues/14702) - kernel/atomic\_c.c : Improve code coverage to 100%
- [GitHub #14675](https://github.com/zephyrproject-rtos/zephyr/issues/14675) - Bluetooth: Controller privacy support (platforms with HW acceleration)
- [GitHub #14652](https://github.com/zephyrproject-rtos/zephyr/issues/14652) - Gitlint is more strict than checkpatch.pl
- [GitHub #14633](https://github.com/zephyrproject-rtos/zephyr/issues/14633) - undefined reference to ‘mbedtls\_debug\_set\_threshold’ when MBEDTLS\_DEBUG is enabled
- [GitHub #14605](https://github.com/zephyrproject-rtos/zephyr/issues/14605) - mimxrt1060\_evk cpp\_synchronization meets Hardware exception
- [GitHub #14604](https://github.com/zephyrproject-rtos/zephyr/issues/14604) - BLE disconnection caused by channel map request or connection parameter update request
- [GitHub #14599](https://github.com/zephyrproject-rtos/zephyr/issues/14599) - Can you add a ADC sample?
- [GitHub #14588](https://github.com/zephyrproject-rtos/zephyr/issues/14588) - static IP support on cc3220sf\_launchxl
- [GitHub #14547](https://github.com/zephyrproject-rtos/zephyr/issues/14547) - Kconfig shell prompt configuration
- [GitHub #14517](https://github.com/zephyrproject-rtos/zephyr/issues/14517) - LPCXpresso55S69 board support
- [GitHub #14493](https://github.com/zephyrproject-rtos/zephyr/issues/14493) - implement Zephyr futexes
- [GitHub #14467](https://github.com/zephyrproject-rtos/zephyr/issues/14467) - New HTTP API implementation
- [GitHub #14459](https://github.com/zephyrproject-rtos/zephyr/issues/14459) - usb: samples: mass: doesn’t build with FLASH overlay
- [GitHub #14292](https://github.com/zephyrproject-rtos/zephyr/issues/14292) - Typo “QPSI” in QSPI macros in some stm32 drivers
- [GitHub #14283](https://github.com/zephyrproject-rtos/zephyr/issues/14283) - tests/drivers/watchdog/wdt\_basic\_api fails on test\_wdt\_callback\_1() for Ardruino and quark\_se\_c1000\_ss\_devboard:arc
- [GitHub #14123](https://github.com/zephyrproject-rtos/zephyr/issues/14123) - Particle boards need a board initialization module for antenna configuration
- [GitHub #14082](https://github.com/zephyrproject-rtos/zephyr/issues/14082) - Update Segger host library to V2.52f
- [GitHub #14037](https://github.com/zephyrproject-rtos/zephyr/issues/14037) - Generic device driver object type
- [GitHub #14034](https://github.com/zephyrproject-rtos/zephyr/issues/14034) - Support for PPP protocol
- [GitHub #13963](https://github.com/zephyrproject-rtos/zephyr/issues/13963) - up\_squared: evaluate removal of SBL-related special configurations
- [GitHub #13935](https://github.com/zephyrproject-rtos/zephyr/issues/13935) - tests/crypto/rand32/crypto.rand32.random\_hw\_xoroshiro: Usage fault “Fatal fault in ISR! Spinning…”
- [GitHub #13897](https://github.com/zephyrproject-rtos/zephyr/issues/13897) - CONFIG\_LOG\_IMMEDIATE leads to unobvious faults in unrelated rotines due to stack overflow
- [GitHub #13817](https://github.com/zephyrproject-rtos/zephyr/issues/13817) - tests/ztest/test/mock fails to complete on nios2
- [GitHub #13799](https://github.com/zephyrproject-rtos/zephyr/issues/13799) - usb cdc acm fails when writing big chunks of data on stm32
- [GitHub #13766](https://github.com/zephyrproject-rtos/zephyr/issues/13766) - mimxrt1060\_evk tests/kernel/fatal meet many unwanted exceptions
- [GitHub #13749](https://github.com/zephyrproject-rtos/zephyr/issues/13749) - Can CONFIG\_SOC\_WATCH-related code be removed?
- [GitHub #13610](https://github.com/zephyrproject-rtos/zephyr/issues/13610) - kernel: Non-deterministic and very high ISR latencies
- [GitHub #13602](https://github.com/zephyrproject-rtos/zephyr/issues/13602) - How to get the port number for an ephemeral (randomly assigned) port
- [GitHub #13574](https://github.com/zephyrproject-rtos/zephyr/issues/13574) - Missing documentation for fcb and nffs
- [GitHub #13560](https://github.com/zephyrproject-rtos/zephyr/issues/13560) - STM32 USB: netusb: kernel crash when testing example echo\_server with nucleo\_f412zg (ECM on Windows)
- [GitHub #13444](https://github.com/zephyrproject-rtos/zephyr/issues/13444) - Build failure when including both socket.h and posix/time.h
- [GitHub #13441](https://github.com/zephyrproject-rtos/zephyr/issues/13441) - optimize x86 userspace page table memory usage
- [GitHub #13347](https://github.com/zephyrproject-rtos/zephyr/issues/13347) - tests/drivers/watchdog/wdt\_basic\_api fails on test\_wdt\_callback\_1() for Quark SE / arc
- [GitHub #13316](https://github.com/zephyrproject-rtos/zephyr/issues/13316) - Notification enabled before connection
- [GitHub #13288](https://github.com/zephyrproject-rtos/zephyr/issues/13288) - Disable JTAG debug port for free use GPIO PA15, PB3, PB4 on STM32F1 series
- [GitHub #13197](https://github.com/zephyrproject-rtos/zephyr/issues/13197) - LwM2M: support Connectivity Monitoring object (object id 4)
- [GitHub #13148](https://github.com/zephyrproject-rtos/zephyr/issues/13148) - Build on nucleo\_stm32f429zi
- [GitHub #13097](https://github.com/zephyrproject-rtos/zephyr/issues/13097) - openthread default configuration
- [GitHub #13075](https://github.com/zephyrproject-rtos/zephyr/issues/13075) - Review memory protection Kconfig policies for consistency and sanity
- [GitHub #13065](https://github.com/zephyrproject-rtos/zephyr/issues/13065) - CONFIG\_BT leads Fatal fault in ISR on esp32
- [GitHub #13003](https://github.com/zephyrproject-rtos/zephyr/issues/13003) - context switch in x86 memory domains needs optimization
- [GitHub #12942](https://github.com/zephyrproject-rtos/zephyr/issues/12942) - openthread: sleepy end device not supported by zephyr router
- [GitHub #12825](https://github.com/zephyrproject-rtos/zephyr/issues/12825) - SystemView Feature Not working
- [GitHub #12728](https://github.com/zephyrproject-rtos/zephyr/issues/12728) - docs: Hard to find guidelines for ext/ maintenance
- [GitHub #12681](https://github.com/zephyrproject-rtos/zephyr/issues/12681) - BLE Split Link Layer
- [GitHub #12633](https://github.com/zephyrproject-rtos/zephyr/issues/12633) - tests/boards/altera\_max10/i2c\_master failed with “failed to read HPD control” on altera\_max10
- [GitHub #12602](https://github.com/zephyrproject-rtos/zephyr/issues/12602) - STM32F415RG Support
- [GitHub #12553](https://github.com/zephyrproject-rtos/zephyr/issues/12553) - List of tests that keep failing sporadically
- [GitHub #12542](https://github.com/zephyrproject-rtos/zephyr/issues/12542) - nrf timers unstable with ticks faster than 100 Hz
- [GitHub #12478](https://github.com/zephyrproject-rtos/zephyr/issues/12478) - tests/drivers/ipm/peripheral.mailbox failing sporadically on qemu\_x86\_64 (timeout)
- [GitHub #12261](https://github.com/zephyrproject-rtos/zephyr/issues/12261) - i2c\_ll\_stm32\_v1 driver gets stuck
- [GitHub #12257](https://github.com/zephyrproject-rtos/zephyr/issues/12257) - GNU Arm Embedded Toolchain 8-2018-q4-major can’t produce hex files on Windows
- [GitHub #12245](https://github.com/zephyrproject-rtos/zephyr/issues/12245) - LWM2M registration timeout
- [GitHub #12228](https://github.com/zephyrproject-rtos/zephyr/issues/12228) - How to build images for client or server in bluetooth mesh examples?
- [GitHub #12160](https://github.com/zephyrproject-rtos/zephyr/issues/12160) - settings: NVS back-end
- [GitHub #12129](https://github.com/zephyrproject-rtos/zephyr/issues/12129) - Include: Clean up header file namespace
- [GitHub #12119](https://github.com/zephyrproject-rtos/zephyr/issues/12119) - 64bit architecture support
- [GitHub #12044](https://github.com/zephyrproject-rtos/zephyr/issues/12044) - [Question] [Blutooth Mesh] How proxy client create the proxy PDU
- [GitHub #12039](https://github.com/zephyrproject-rtos/zephyr/issues/12039) - clock\_control: API should allow callback to be specified
- [GitHub #11993](https://github.com/zephyrproject-rtos/zephyr/issues/11993) - drivers: Supporting driver-specific extensions to existing generic APIs
- [GitHub #11922](https://github.com/zephyrproject-rtos/zephyr/issues/11922) - ADC generic driver missing features: calibration, reference voltage value
- [GitHub #11918](https://github.com/zephyrproject-rtos/zephyr/issues/11918) - Dynamic pin configuration
- [GitHub #11740](https://github.com/zephyrproject-rtos/zephyr/issues/11740) - LL\_ASSERT in event\_common\_prepare in Zephyr v1.13
- [GitHub #11712](https://github.com/zephyrproject-rtos/zephyr/issues/11712) - Add support for newlib-nano
- [GitHub #11681](https://github.com/zephyrproject-rtos/zephyr/issues/11681) - Mesh Friend does not reply within ReceiveWindow
- [GitHub #11626](https://github.com/zephyrproject-rtos/zephyr/issues/11626) - k\_busy\_wait exits early on Nordic chips
- [GitHub #11617](https://github.com/zephyrproject-rtos/zephyr/issues/11617) - net: ipv4: udp: broadcast delivery not supported
- [GitHub #11535](https://github.com/zephyrproject-rtos/zephyr/issues/11535) - serial: uart\_irq\_tx\_ready() needs better documentation or correction of the test
- [GitHub #11455](https://github.com/zephyrproject-rtos/zephyr/issues/11455) - cdc\_acm uart\_fifo\_fill sample app doesn’t comply with the documentation
- [GitHub #11107](https://github.com/zephyrproject-rtos/zephyr/issues/11107) - clock\_control: API should support asynchronous and synchronous variants of turning on clocks
- [GitHub #10965](https://github.com/zephyrproject-rtos/zephyr/issues/10965) - wncm14a2a modem should be moved to a shield configuration
- [GitHub #10942](https://github.com/zephyrproject-rtos/zephyr/issues/10942) - Declaring an API Stable
- [GitHub #10935](https://github.com/zephyrproject-rtos/zephyr/issues/10935) - Support all UARTs on ESP32 WROOM module
- [GitHub #10915](https://github.com/zephyrproject-rtos/zephyr/issues/10915) - ESP 32 failed to boot while running crypto/rand32 tests
- [GitHub #10896](https://github.com/zephyrproject-rtos/zephyr/issues/10896) - Add STM32 ADC driver
- [GitHub #10739](https://github.com/zephyrproject-rtos/zephyr/issues/10739) - Cannot flash to STM32 Nucleo F446RE with SEGGER JLink
- [GitHub #10664](https://github.com/zephyrproject-rtos/zephyr/issues/10664) - FOTA: nRF52: integration of samples/bluetooth/mesh & smp\_srv
- [GitHub #10657](https://github.com/zephyrproject-rtos/zephyr/issues/10657) - tests/net/ieee802154/crypto does not work as expected
- [GitHub #10603](https://github.com/zephyrproject-rtos/zephyr/issues/10603) - Hard to find “todo”
- [GitHub #10463](https://github.com/zephyrproject-rtos/zephyr/issues/10463) - can: stm32: Update to new API
- [GitHub #10450](https://github.com/zephyrproject-rtos/zephyr/issues/10450) - usb/stm32: use dts extracted information to populate clock settings
- [GitHub #10420](https://github.com/zephyrproject-rtos/zephyr/issues/10420) - gcc: “Exec format error” - WSL in Windows 10 1803
- [GitHub #10150](https://github.com/zephyrproject-rtos/zephyr/issues/10150) - Getting LLVM work on ARM
- [GitHub #9954](https://github.com/zephyrproject-rtos/zephyr/issues/9954) - samples/hello\_world build failed on Windows/MSYS
- [GitHub #9898](https://github.com/zephyrproject-rtos/zephyr/issues/9898) - 1.14 Release Checklist
- [GitHub #9762](https://github.com/zephyrproject-rtos/zephyr/issues/9762) - Bluetooth mesh reliability issue?
- [GitHub #9570](https://github.com/zephyrproject-rtos/zephyr/issues/9570) - Network stack cleanup: deep TCP cleanup
- [GitHub #9509](https://github.com/zephyrproject-rtos/zephyr/issues/9509) - Unable to upload firmware over serial with mcumgr
- [GitHub #9333](https://github.com/zephyrproject-rtos/zephyr/issues/9333) - Support for STM32 L1-series
- [GitHub #9247](https://github.com/zephyrproject-rtos/zephyr/issues/9247) - Get ST Disco and Eval boards compliant with default configuration guidelines
- [GitHub #9070](https://github.com/zephyrproject-rtos/zephyr/issues/9070) - bluetooth ：BR ：The sample is incomplete
- [GitHub #9047](https://github.com/zephyrproject-rtos/zephyr/issues/9047) - Interrupt APIs.
- [GitHub #8978](https://github.com/zephyrproject-rtos/zephyr/issues/8978) - soc: Intel S1000: add low power memory management support
- [GitHub #8851](https://github.com/zephyrproject-rtos/zephyr/issues/8851) - Allow creation of Zephyr libraries outside of Zephyr tree
- [GitHub #8734](https://github.com/zephyrproject-rtos/zephyr/issues/8734) - USB: DFU timeout on nRF52840 due to long flash erase
- [GitHub #8728](https://github.com/zephyrproject-rtos/zephyr/issues/8728) - Network stack cleanup: Net IF
- [GitHub #8726](https://github.com/zephyrproject-rtos/zephyr/issues/8726) - Network stack cleanup: TCP
- [GitHub #8725](https://github.com/zephyrproject-rtos/zephyr/issues/8725) - Network stack cleanup: Net Context
- [GitHub #8723](https://github.com/zephyrproject-rtos/zephyr/issues/8723) - Network stack cleanup
- [GitHub #8722](https://github.com/zephyrproject-rtos/zephyr/issues/8722) - Network stack cleanup: connection
- [GitHub #8464](https://github.com/zephyrproject-rtos/zephyr/issues/8464) - sdk\_version file missing
- [GitHub #8419](https://github.com/zephyrproject-rtos/zephyr/issues/8419) - Bluetooth: tester: LPN Poll issue
- [GitHub #8404](https://github.com/zephyrproject-rtos/zephyr/issues/8404) - Bluetooth: controller: Reuse get\_entropy\_isr API
- [GitHub #8275](https://github.com/zephyrproject-rtos/zephyr/issues/8275) - when zephyr can support popular IDE develop?
- [GitHub #8125](https://github.com/zephyrproject-rtos/zephyr/issues/8125) - About BMI160 reading issue.
- [GitHub #8081](https://github.com/zephyrproject-rtos/zephyr/issues/8081) - Bluetooth: Deprecate TinyCrypt and use mbedTLS
- [GitHub #8062](https://github.com/zephyrproject-rtos/zephyr/issues/8062) - [Coverity CID :186196] Error handling issues in /samples/sensor/mcp9808/src/main.c
- [GitHub #7908](https://github.com/zephyrproject-rtos/zephyr/issues/7908) - tests/boards/altera\_max10/qspi fails on max10
- [GitHub #7589](https://github.com/zephyrproject-rtos/zephyr/issues/7589) - Migrate Websocket to BSD sockets
- [GitHub #7585](https://github.com/zephyrproject-rtos/zephyr/issues/7585) - Migrate HTTP to socket API
- [GitHub #7503](https://github.com/zephyrproject-rtos/zephyr/issues/7503) - LwM2M client: No registration retry after error?
- [GitHub #7462](https://github.com/zephyrproject-rtos/zephyr/issues/7462) - Convert mcr20a to be a shield when that functionality is merged
- [GitHub #7403](https://github.com/zephyrproject-rtos/zephyr/issues/7403) - RAM flash driver emulator
- [GitHub #7316](https://github.com/zephyrproject-rtos/zephyr/issues/7316) - native\_posix supersedes ztest mocking
- [GitHub #6906](https://github.com/zephyrproject-rtos/zephyr/issues/6906) - QM (Quality Managed) level qualification
- [GitHub #6823](https://github.com/zephyrproject-rtos/zephyr/issues/6823) - Optimize rendering of Kconfig documentation
- [GitHub #6817](https://github.com/zephyrproject-rtos/zephyr/issues/6817) - Question: Is supported for stack sharing among tasks in Zephyr? Or any plan?
- [GitHub #6816](https://github.com/zephyrproject-rtos/zephyr/issues/6816) - Question: Is KProbes supported in Zephyr? Or any plan?
- [GitHub #6773](https://github.com/zephyrproject-rtos/zephyr/issues/6773) - Publish doxygen-generated API pages
- [GitHub #6770](https://github.com/zephyrproject-rtos/zephyr/issues/6770) - Multiple Git Repositories
- [GitHub #6636](https://github.com/zephyrproject-rtos/zephyr/issues/6636) - Enable hardware flow control in mcux uart shim driver
- [GitHub #6605](https://github.com/zephyrproject-rtos/zephyr/issues/6605) - Question: Does WAMP protocol has any usecase for Zephyr
- [GitHub #6545](https://github.com/zephyrproject-rtos/zephyr/issues/6545) - ARM Cortex R Architecture support
- [GitHub #6370](https://github.com/zephyrproject-rtos/zephyr/issues/6370) - I can’t find adc name which is f429zi board
- [GitHub #6183](https://github.com/zephyrproject-rtos/zephyr/issues/6183) - sensor: Handling sensors with long measurement times
- [GitHub #6086](https://github.com/zephyrproject-rtos/zephyr/issues/6086) - Ideas/requirements for improved TLS support in Zephyr
- [GitHub #6039](https://github.com/zephyrproject-rtos/zephyr/issues/6039) - Implement interrupt driven USART on LPC54114
- [GitHub #5579](https://github.com/zephyrproject-rtos/zephyr/issues/5579) - Address untested options in kernel
- [GitHub #5529](https://github.com/zephyrproject-rtos/zephyr/issues/5529) - Explore Little File System (littlefs) support
- [GitHub #5460](https://github.com/zephyrproject-rtos/zephyr/issues/5460) - scripts: extract\_dts\_includes: check yaml dts binding property “category: “
- [GitHub #5457](https://github.com/zephyrproject-rtos/zephyr/issues/5457) - Add SDHC card support
- [GitHub #5423](https://github.com/zephyrproject-rtos/zephyr/issues/5423) - [nRF] on-target tests accidentally run twice
- [GitHub #5365](https://github.com/zephyrproject-rtos/zephyr/issues/5365) - Revisit DHCPv4 test, convert to ztest
- [GitHub #4628](https://github.com/zephyrproject-rtos/zephyr/issues/4628) - Sample app enabling sensors on disco\_l475\_iot1 board
- [GitHub #4506](https://github.com/zephyrproject-rtos/zephyr/issues/4506) - rework GPIO flags
- [GitHub #4505](https://github.com/zephyrproject-rtos/zephyr/issues/4505) - sanitycheck should distinguish compile errors from link errors
- [GitHub #4375](https://github.com/zephyrproject-rtos/zephyr/issues/4375) - Provide a script to find files not owned per the CODEOWNERS file
- [GitHub #4178](https://github.com/zephyrproject-rtos/zephyr/issues/4178) - Openweave Support
- [GitHub #3936](https://github.com/zephyrproject-rtos/zephyr/issues/3936) - BT: bt\_conn\_create\_le(): No way to find out error cause
- [GitHub #3930](https://github.com/zephyrproject-rtos/zephyr/issues/3930) - Need a CPU frequency driver for ESP-32
- [GitHub #3928](https://github.com/zephyrproject-rtos/zephyr/issues/3928) - [TIMER] k\_timer\_start should take 0 value for duration parameter
- [GitHub #3846](https://github.com/zephyrproject-rtos/zephyr/issues/3846) - to use {k\_wakeup} to cancel the delayed startup of one thread
- [GitHub #3805](https://github.com/zephyrproject-rtos/zephyr/issues/3805) - [test] test scheduling of threads along with networking conditions
- [GitHub #3767](https://github.com/zephyrproject-rtos/zephyr/issues/3767) - reconsider k\_mem\_pool APIs
- [GitHub #3759](https://github.com/zephyrproject-rtos/zephyr/issues/3759) - reconsider k\_mbox APIs
- [GitHub #3754](https://github.com/zephyrproject-rtos/zephyr/issues/3754) - Support static BT MAC address
- [GitHub #3749](https://github.com/zephyrproject-rtos/zephyr/issues/3749) - ESP32: Deep Sleep
- [GitHub #3722](https://github.com/zephyrproject-rtos/zephyr/issues/3722) - Enable Flash Cache for ESP32
- [GitHub #3710](https://github.com/zephyrproject-rtos/zephyr/issues/3710) - 802.15.4 Soft MAC 2015 version support
- [GitHub #3678](https://github.com/zephyrproject-rtos/zephyr/issues/3678) - Implement the Read Static Addresses Command
- [GitHub #3673](https://github.com/zephyrproject-rtos/zephyr/issues/3673) - reconsider k\_queue APIs
- [GitHub #3651](https://github.com/zephyrproject-rtos/zephyr/issues/3651) - add tickless idle and kernel support to RISCV32 pulpino
- [GitHub #3648](https://github.com/zephyrproject-rtos/zephyr/issues/3648) - Ability to unpair devices
- [GitHub #3640](https://github.com/zephyrproject-rtos/zephyr/issues/3640) - BLE central scan ignores changes in payload
- [GitHub #3547](https://github.com/zephyrproject-rtos/zephyr/issues/3547) - IP stack: Ideas for optimizations
- [GitHub #3500](https://github.com/zephyrproject-rtos/zephyr/issues/3500) - ESP8266 Architecture Configuration
- [GitHub #3499](https://github.com/zephyrproject-rtos/zephyr/issues/3499) - evaluate Emul8 as a replacement for QEMU in sanitycheck
- [GitHub #3442](https://github.com/zephyrproject-rtos/zephyr/issues/3442) - TCP connection locally isn’t possible
- [GitHub #3426](https://github.com/zephyrproject-rtos/zephyr/issues/3426) - Only supports classic Bluetooth compilation options
- [GitHub #3418](https://github.com/zephyrproject-rtos/zephyr/issues/3418) - Bluetooth True Wireless Stereo
- [GitHub #3417](https://github.com/zephyrproject-rtos/zephyr/issues/3417) - BT Phonebook Access Profles
- [GitHub #3399](https://github.com/zephyrproject-rtos/zephyr/issues/3399) - Texas Instruments CC2538 Support
- [GitHub #3396](https://github.com/zephyrproject-rtos/zephyr/issues/3396) - LLDP: Implement local MIB support with advertisement of mandatory TLVs
- [GitHub #3295](https://github.com/zephyrproject-rtos/zephyr/issues/3295) - Advanced Power Management
- [GitHub #3286](https://github.com/zephyrproject-rtos/zephyr/issues/3286) - Native Zephyr IP Stack Advanced Features
- [GitHub #3155](https://github.com/zephyrproject-rtos/zephyr/issues/3155) - xtensa: fix tests/kernel/mem\_protect/stackprot
- [GitHub #3040](https://github.com/zephyrproject-rtos/zephyr/issues/3040) - Add support for the Arduino Ethernet Shield V2
- [GitHub #2994](https://github.com/zephyrproject-rtos/zephyr/issues/2994) - The build system crashes when GCCARMEMB\_TOOLCHAIN\_PATH has a space in it
- [GitHub #2984](https://github.com/zephyrproject-rtos/zephyr/issues/2984) - frdm\_k64f bus exception bug due to peculiar RAM configuration
- [GitHub #2933](https://github.com/zephyrproject-rtos/zephyr/issues/2933) - Add zephyr support to openocd upstream
- [GitHub #2900](https://github.com/zephyrproject-rtos/zephyr/issues/2900) - Support for the BBC micro:bit Bluetooth Profile
- [GitHub #2856](https://github.com/zephyrproject-rtos/zephyr/issues/2856) - Customer: Floating Point samples
- [GitHub #2780](https://github.com/zephyrproject-rtos/zephyr/issues/2780) - Set the \_Swap() return value on ARC the same way it is now done on ARM ?
- [GitHub #2766](https://github.com/zephyrproject-rtos/zephyr/issues/2766) - BMI160 Oversampling Configuration
- [GitHub #2682](https://github.com/zephyrproject-rtos/zephyr/issues/2682) - Add support for UART A1 for TI CC3200 SoC
- [GitHub #2623](https://github.com/zephyrproject-rtos/zephyr/issues/2623) - nRF52 UART behaviour sensitive to timing of baud rate initialization.
- [GitHub #2611](https://github.com/zephyrproject-rtos/zephyr/issues/2611) - SDP client
- [GitHub #2587](https://github.com/zephyrproject-rtos/zephyr/issues/2587) - Support for BR/EDR SSP out-of-band pairing
- [GitHub #2586](https://github.com/zephyrproject-rtos/zephyr/issues/2586) - Support for LE SC out-of-band pairing
- [GitHub #2401](https://github.com/zephyrproject-rtos/zephyr/issues/2401) - 802.15.4 - LLDN frame support
- [GitHub #2400](https://github.com/zephyrproject-rtos/zephyr/issues/2400) - 802.15.4 - Multipurpose frame support
- [GitHub #2399](https://github.com/zephyrproject-rtos/zephyr/issues/2399) - 802.15.4 - TSCH Radio protocol support
- [GitHub #2398](https://github.com/zephyrproject-rtos/zephyr/issues/2398) - 802.15.4 - Update existing Management commands
- [GitHub #2397](https://github.com/zephyrproject-rtos/zephyr/issues/2397) - 802.15.4 - IE list support
- [GitHub #2396](https://github.com/zephyrproject-rtos/zephyr/issues/2396) - 802.15.4 - Management service: FFD level support
- [GitHub #2333](https://github.com/zephyrproject-rtos/zephyr/issues/2333) - Get IPv6 Ready approval
- [GitHub #2049](https://github.com/zephyrproject-rtos/zephyr/issues/2049) - Enable ARM M4F FPU lazy stacking
- [GitHub #2046](https://github.com/zephyrproject-rtos/zephyr/issues/2046) - Add a driver to support timer functions using the PWM H/W periphral timers
- [GitHub #1933](https://github.com/zephyrproject-rtos/zephyr/issues/1933) - nios2: implement nested interrupts
- [GitHub #1860](https://github.com/zephyrproject-rtos/zephyr/issues/1860) - Add support for getting OOB data
- [GitHub #1843](https://github.com/zephyrproject-rtos/zephyr/issues/1843) - nios2: enable interrupt driven serial console for JTAG UART
- [GitHub #1766](https://github.com/zephyrproject-rtos/zephyr/issues/1766) - nios2: implement asm atomic operations
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #335](https://github.com/zephyrproject-rtos/zephyr/issues/335) - images for the wiki
