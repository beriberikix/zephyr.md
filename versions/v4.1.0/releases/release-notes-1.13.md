---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-1.13.html
original_path: releases/release-notes-1.13.html
---

# Zephyr Kernel 1.13.0

We are pleased to announce the release of Zephyr kernel version 1.13.0.

Major enhancements with this release include:

- Extensible and Pluggable Tracing Support
- Compartmentalized application memory organization
- Logging System Overhaul
- Introduce system calls for BSD socket APIs
- Support for IEEE 802.1AS-2011 generalized Precision Time Protocol (gPTP)
- Link Layer Discovery Protocol (LLDP) TX support
- Support for TLS and DTLS using BSD socket API
- Support for Link Layer Multicast Name Resolution (LLMNR)
- Introduced reworked ADC API and updated Nordic, NXP, Atmel, and
  Synopsys DesignWare drivers
- Support OS driven Power Management framework
- Basic support for Arm TrustZone in Armv8-M

The following sections provide detailed lists of changes by component.

## Kernel

- Remove kernel event manager, replaced by generic tracing interface
- Enhanced Timeout and Tick handling in kernel
- Compartmentalized application memory organization
- Fix errno access for user mode

## Architectures

- arch: arc: improve the reset code
- arch: arc: use a separate stack for exception handling
- arch: arc: refactor the arc stack check support
- arch: arm: stm32: enable instruction and data caches on STM32F7
- arch: arm: implement ARMv8-M MPU driver
- irq: Fix irq\_lock api usage
- arch: arm: macro API for defining non-secure entry functions
- arch: arm: allow processor to ignore/recover from faults
- arm: nxp: mpu: Consolidate k64 mpu regions
- arm: Print NXP MPU error information in BusFault dump
- arch: ARM: Change the march used by cortex-m0 and cortex-m0plus
- arch: arm: integrate ARM CMSE with CMake
- arch: arm: basic Arm TrustZone-M functionality for Cortex-M23 and Cortex-M33
- arch: arm: built-in stack protection using Armv8-M SPLIM registers
- arch: arm: API for using TT intrinsics in Secure/Non-Secure Armv8-M firmware
- arch: arm: clean up MPU code for ARM and NXP
- arch: arm: Set Zero Latency IRQ to priority level zero
- arch/arm: Fix locking in \_\_pendsv

## Boards & SoC Support

- x86: add SoC configuration for Apollo Lake
- x86: add support for UP Squared (Pentium/Celeron)
- arc: Support Synopsys ARC nSim instruction set simulator
- riscv32: riscv-privilege: Microsemi Mi-V support
- Added support for the following Arm boards:

  - efr32\_slwstk6061a
  - nrf52\_adafruit\_feather
  - nrf52810\_pca10040
  - nrf52840\_pca10059
  - nucleo\_f207zg
  - reel\_board
  - stm32f723e\_disco
  - stm32f746g\_disco
  - stm32f769i\_disco
  - udoo\_neo\_full\_m4
  - warp7\_m4

## Drivers and Sensors

- adc: Introduced reworked API and updated Nordic, NXP, Atmel, and
  Synopsys DesignWare drivers
- audio: Added TLV320DAC310x audio DAC driver
- can: Added can support for STM32L432
- clock\_control: Added STM32F7 family clock control
- entropy: Added support for STM32F7
- eth: Enabled gPTP support in mcux and gmac drivers
- eth: Added promiscuous mode support to native\_posix
- eth: mcux: Added an option for randomized, but stable MAC address
- gpio: Added STM32F7 GPIO support
- interrupt\_controller: Added STM32F7 EXTI support
- i2c: Added support for STM32F7
- i2c: Added i.MX shim driver
- i2c: Implemented slave support for stm32\_v2
- i2c: Added EEPROM I2C slave driver
- i2c: Added shims for nrfx TWI and TWIM drivers
- i2s: Exposed i2s APIs to user mode
- led: Added TI LP5562 and NXP PCA9633 drivers
- modem: Added Wistron WNC-M14A2A LTE-M Modem driver
- modem: Added modem receiver (tty) driver
- pinmux: Added STM32F7 pinmux support
- pwm: Added i.MX shim driver
- pwm: Added shim for nrfx PWM HW driver
- serial: Added power management to nRF UART driver
- serial: Added STM32F7 UART support
- serial: Allow to pass arbitrary user data to irq callback
- serial: Added UARTE driver for the nRFx family
- sensor: Added adxl372, mma8451q, adt7420 drivers
- sensor: lis2dh: Fix I2C burst read/write operations
- rtc: Added support for STM32
- usb: Added support for OTG FS on STM32F2 and STM32F7
- usb: Added High Speed support for DesignWare USB
- wifi: Added SimpleLink WiFi Offload Driver (wifi\_mgmt only)

## Networking

- Introduce system calls for BSD socket APIs.
- Add IPv4 autoconf support. This adds support for IPv4 link-local addresses
  (169.254.\*.\*)
- Add TLS and DTLS support to BSD socket API. They are configured via
  setsockopt() API.
- Add support for IEEE 802.1AS-2011 generalized Precision Time Protocol (gPTP)
  for ethernet networks. A sample application is created to show how to interact
  with gPTP code.
- Add support for PTP clock driver. This driver will be used by gPTP supported
  ethernet drivers.
- Add Link Layer Discovery Protocol (LLDP) TX support.
- Add support for managing Qav credit-based shaper algorithm.
- Add generic TX timestamping support.
- Add carrier detection support to ethernet L2 driver.
- Add support for having vendor specific ethernet statistics.
- Add getter support to ethernet management interface.
- Add promiscuous mode support to network interface. A sample application is
  created that shows how to use the user API for getting all network packets.
  The native\_posix ethernet driver supports promiscuous mode at this point.
- Add support for Link Layer Multicast Name Resolution (LLMNR). LLMNR is used in
  Microsoft Windows networks for local name resolution.
- Add API to net\_pkt to prefill a network packet to a pre-defined value.
- Add IEEE 802.1Qav support to Atmel GMAC ethernet driver.
- Add hardware TX timestamping support to Atmel GMAC ethernet driver.
- Add multiple hardware queue support to Atmel GMAC ethernet driver.
- Add gPTP support to Atmel GMAC ethernet driver.
- Add support for TI SimpleLink WiFI offload driver.
- Add support for randomized but stable MAC address in NXP MCUX ethernet driver.
- Add extra prints to net-shell for ethernet based network interfaces. The
  supported features and priority queue information is printed.
- Add and fix string to integer conversions in net-shell.
- Allow user to configure MAC address filters into ethernet devices.
- Catch network interface ON and OFF events in DHCPv4 and renew address lease if
  we re-connected.
- Remove forever timeouts when waiting a new network buffer to be available.
- Relay network interface up/down command from net-shell to Linux host for
  native\_posix ethernet driver.
- No need to join IPv6 solicited node multicast group for Bluetooth IPSP
  supported nodes.
- Allow external program to be started for native\_posix ethernet driver. This
  allows for example startup of wireshark when zeth is created.
- Network packet priority and traffic class fixes and clarifications.
- Lower memory consumption in net by using packed enums when applicable.
- Correctly notify net\_app server when TCP is disconnected.
- Register OpenThread used unicast and multicast IPv6 addresses for network
  interface.
- Enable Fast Connect policy for TI SimpleLink ethernet driver.
- Fix ieee802154 simulator driver channel/tx power settings.
- Handle large IPv6 packets properly.
- Enable gPTP support in native\_posix, NXP mcux and Atmel GMAC ethernet drivers.
  The native\_posix ethernet driver gPTP support is only for testing purposes.
- Network configuration (net\_config) library split from the net\_app library.
  (This change requires updating application configs to refer to corresponding
  NET\_CONFIG\_\* options instead of NET\_APP\_\*).
- Moving all layer 2 (L2) network code into subsys/net/l2 directory.
- Add MSS option on sending TCP SYN request.
- Fix TCP by processing zero window probes when our receive window is 0.
- IPv4, IPv6, ICMPv6, ARP code refactoring and cleanup.
- IPv6 address lifetime fixes.
- IPv6 fragmentation fixes.
- ARP fixes when using VLAN.
- Timeout too long lasting ARP requests.
- DHCPv4 fixes and timeout management refactoring.
- TCP retry, RST packet handling, and memory leak fixes.
- IP address print function enhancements.
- HTTP fix when sending the last chunk.
- MQTT fixes.
- LWM2M cleanups and fixes.
- Fix cache support in Atmel GMAC ethernet driver.
- Fix NXP MCUX ethernet driver to detect carrier lost event.
- Port native API echo-server/echo-client samples to BSD sockets API, with
  TLS/DTLS support.
- Handle out-of-buf situations gracefully in echo-client and echo-server sample
  applications.

## Bluetooth

- New user-friendly service population using a refreshed BT\_GATT\_CHARACTERISTIC
  macro.
- Added support for Bluetooth hardware in the native\_posix board, allowing
  developers to use the native POSIX architecture with Bluetooth.
- Added a new helper API to parse advertising data.
- Added a new flag, BT\_LE\_ADV\_OPT\_USE\_NAME, to include the Bluetooth Device
  Name in the advertising data.
- Added support for fixed passkeys to use in bonding procedures.
- Added a new Bluetooth shell command to send arbitrary HCI commands to the
  controller.
- Added a new feature to support multiple local identities using a single
  controller.
- Added a new, board-specific mesh sample for the nRF52x series that
  implements the following models:

  - Generic OnOff client and server.
  - Generic Level client and server.
  - Generic Power OnOff client and server.
  - Light Lightness client and server.
  - Light CTL client and server.
  - Vendor Model.
- Controller: Added a TX Power Kconfig option.
- Controller: Use the newly available nrfx utility functions to access the
  nRF5x hardware.
- Controller: Multiple bug fixes.
- Controller: Added support for the nRF52810 SoC from Nordic Semiconductor.
- New HCI driver quirks API to support controllers that need uncommon reset
  sequences.
- Host: Multiple bug fixes for GATT and SMP.
- Mesh: Multiple bug fixes.

## Build and Infrastructure

- Kconfig: Remove redundant ‘default n’ properties
- cmake: replace PROJECT\_SOURCE\_DIR with ZEPHYR\_BASE
- Kconfig: Switch to improved globbing statements

## Libraries / Subsystems

- Tracing: Basic support SEGGER systemview
- Logging: Introduce a new logging subsystem
- fs/nvs: Improved nvs for larger blocksizes
- subsys: console: Refactor code to allow per-UART “tty” wrapper

## HALs

- ext/hal: stm32cube: STM32L4: Enable legacy CAN API
- ext: Import Atmel SAMD20 header files from ASF library
- ext: gecko: Add Silabs Gecko SDK for EFR32FG1P SoCs
- drivers: add i.MX I2C driver shim
- hal: stm32f2x: Add HAL for the STM32F2x series
- ext: stm32cube: update stm32l4xx cube version
- ext: stm32cube: update stm32f7xx cube version
- ext: stm32cube: update stm32f4xx cube version
- ext: stm32cube: update stm32f3xx cube version
- ext: stm32cube: update stm32f1xx cube version
- ext: hal: nordic: Update nrfx to version 1.1.0
- net: drivers: wifi: SimpleLink WiFi Offload Driver (wifi\_mgmt only)
- ext/hal/nxp/imx: Import the nxp imx6 freertos bsp

## Documentation

- Simplified and more maintainable theme applied to documentation.
  Latest and previous four releases regenerated and published to
  [https://docs.zephyrproject.org](https://docs.zephyrproject.org)
- Updated contributing guidelines
- General organization cleanup and spell check on docs including content
  generated from Kconfig files and doxygen API comments.
- General improvements to documentation following code,
  implementation changes, and in support of new features, boards, and
  samples.
- Documentation generation now supported on Windows host systems
  (previously only linux doc generation was supported).
- PDF version of documentation can now be created

## Tests and Samples

- Enhanced benchmarks to support userspace
- Improve test coverage for the kernel

## Issue Related Items

These GitHub issues were addressed since the previous 1.12.0 tagged
release:

- [GitHub #9862](https://github.com/zephyrproject-rtos/zephyr/issues/9862) - tests/drivers/build\_all#test\_build\_sensors\_a\_m @ quark\_se\_c1000\_devboard:x86 BUILD failed
- [GitHub #9857](https://github.com/zephyrproject-rtos/zephyr/issues/9857) - tests/cmsis\_rtos\_v1 - test\_signal\_events\_signalled results in Assertion failure on all targets with PR#9856
- [GitHub #9840](https://github.com/zephyrproject-rtos/zephyr/issues/9840) - doc: potential broken link when referencing latest doc version
- [GitHub #9833](https://github.com/zephyrproject-rtos/zephyr/issues/9833) - Bluetooth Mesh incorrect reference to CONFIG\_BT\_SETTINGS
- [GitHub #9788](https://github.com/zephyrproject-rtos/zephyr/issues/9788) - update to mbedTLS 2.12.0
- [GitHub #9786](https://github.com/zephyrproject-rtos/zephyr/issues/9786) - arch: xtensa: build failure due to extra #endif
- [GitHub #9785](https://github.com/zephyrproject-rtos/zephyr/issues/9785) - Bluetooth: bt\_gatt\_service\_register() assumes sc delayed work handler is initialized
- [GitHub #9772](https://github.com/zephyrproject-rtos/zephyr/issues/9772) - Test application hangs without any console output on x86/ARC based boards @arduino\_101:arc
- [GitHub #9768](https://github.com/zephyrproject-rtos/zephyr/issues/9768) - [Coverity CID :187902] Memory - illegal accesses in /subsys/net/ip/ipv6\_fragment.c
- [GitHub #9766](https://github.com/zephyrproject-rtos/zephyr/issues/9766) - [Coverity CID :187904] Integer handling issues in /tests/benchmarks/timing\_info/src/semaphore\_bench.c
- [GitHub #9753](https://github.com/zephyrproject-rtos/zephyr/issues/9753) - ESP32: Failing to build project
- [GitHub #9746](https://github.com/zephyrproject-rtos/zephyr/issues/9746) - zephyr networking non socket client server, qemu\_x86 issue
- [GitHub #9744](https://github.com/zephyrproject-rtos/zephyr/issues/9744) - tests/kernel/mbox/mbox\_usage/testcase.yaml#kernel.mailbox crashes on ESP32
- [GitHub #9727](https://github.com/zephyrproject-rtos/zephyr/issues/9727) - Bluetooth: IPSP Sample Doc no match for new path
- [GitHub #9723](https://github.com/zephyrproject-rtos/zephyr/issues/9723) - tests/drivers/adc/adc\_api/ fails on sam\_e70\_xplained
- [GitHub #9718](https://github.com/zephyrproject-rtos/zephyr/issues/9718) - The test suite test\_spi (spi\_loopback) when built and run on the nrf52832\_pca10040 board
- [GitHub #9701](https://github.com/zephyrproject-rtos/zephyr/issues/9701) - Suggestion: Turn warnings into errors in extract\_dts\_includes.py
- [GitHub #9689](https://github.com/zephyrproject-rtos/zephyr/issues/9689) - Multiple tests are failing on sam\_e70\_xplained once the cache is enabled
- [GitHub #9684](https://github.com/zephyrproject-rtos/zephyr/issues/9684) - tests/posix/ fails on sam\_e70\_xplained
- [GitHub #9683](https://github.com/zephyrproject-rtos/zephyr/issues/9683) - Multiple testcases in tests/kernel/mem\_protect/mem\_protect, tests/kernel/alert, tests/kernel/mem\_pool test fails on sam\_e70\_xplained due to commit c090776
- [GitHub #9682](https://github.com/zephyrproject-rtos/zephyr/issues/9682) - tests/kernel/init: kernel.common.init.verify\_bootdelay fails on sam\_e70\_xplained
- [GitHub #9680](https://github.com/zephyrproject-rtos/zephyr/issues/9680) - tests/mem\_slab/mslab, tests/mem\_slab/mslab\_api and tests/mem\_slab/mslab\_threadsafe tests are crashing on sam\_e70\_xplained
- [GitHub #9677](https://github.com/zephyrproject-rtos/zephyr/issues/9677) - tests:cmsis\_rtos\_v1: test\_mutex crashes with bus fault on sam\_e70\_xplained
- [GitHub #9676](https://github.com/zephyrproject-rtos/zephyr/issues/9676) - benchmark.timing.userspace not working on nrf52840 with v1.13.0-rc1
- [GitHub #9671](https://github.com/zephyrproject-rtos/zephyr/issues/9671) - Zephyr with WNC-M14A2A not compiling
- [GitHub #9670](https://github.com/zephyrproject-rtos/zephyr/issues/9670) - Bluetooth: Mesh: Persistent Storage: AppKey not restored
- [GitHub #9667](https://github.com/zephyrproject-rtos/zephyr/issues/9667) - LwM2M: Writeable parameter /3311/0/5850 doesn’t persist write
- [GitHub #9665](https://github.com/zephyrproject-rtos/zephyr/issues/9665) - tests/drivers/watchdog/wdt\_basic\_api crashes on Quark D2k / SE and ESP32
- [GitHub #9664](https://github.com/zephyrproject-rtos/zephyr/issues/9664) - tests/kernel/threads/thread\_apis/kernel.threads.user\_mode crases on QEMU-x86
- [GitHub #9652](https://github.com/zephyrproject-rtos/zephyr/issues/9652) - [gen\_isr\_table@mimxrt1050\_evk](mailto:gen_isr_table%40mimxrt1050_evk) runs failure on R1.13\_RC1.
- [GitHub #9649](https://github.com/zephyrproject-rtos/zephyr/issues/9649) - readme of LPCxpresso54114\_mo core needs update for R1.13
- [GitHub #9646](https://github.com/zephyrproject-rtos/zephyr/issues/9646) - sanitycheck: crashes after test execution summary report are not caught
- [GitHub #9644](https://github.com/zephyrproject-rtos/zephyr/issues/9644) - [Coverity CID :187817] Error handling issues in /tests/benchmarks/timing\_info/src/msg\_passing\_bench.c
- [GitHub #9643](https://github.com/zephyrproject-rtos/zephyr/issues/9643) - [Coverity CID :187818] Error handling issues in /tests/benchmarks/timing\_info/src/msg\_passing\_bench.c
- [GitHub #9642](https://github.com/zephyrproject-rtos/zephyr/issues/9642) - [Coverity CID :187819] Memory - illegal accesses in /subsys/logging/log\_msg.c
- [GitHub #9641](https://github.com/zephyrproject-rtos/zephyr/issues/9641) - [Coverity CID :187820] Memory - illegal accesses in /subsys/bluetooth/host/hci\_core.c
- [GitHub #9640](https://github.com/zephyrproject-rtos/zephyr/issues/9640) - [Coverity CID :187821] Memory - illegal accesses in /subsys/bluetooth/host/hci\_core.c
- [GitHub #9639](https://github.com/zephyrproject-rtos/zephyr/issues/9639) - [Coverity CID :187822] Null pointer dereferences in /subsys/net/ip/tcp.c
- [GitHub #9638](https://github.com/zephyrproject-rtos/zephyr/issues/9638) - [Coverity CID :187823] Memory - corruptions in /samples/net/coap\_server/src/coap-server.c
- [GitHub #9637](https://github.com/zephyrproject-rtos/zephyr/issues/9637) - [Coverity CID :187824] Integer handling issues in /lib/cmsis\_rtos\_v1/cmsis\_thread.c
- [GitHub #9636](https://github.com/zephyrproject-rtos/zephyr/issues/9636) - [Coverity CID :187825] Error handling issues in /subsys/net/ip/udp.c
- [GitHub #9635](https://github.com/zephyrproject-rtos/zephyr/issues/9635) - [Coverity CID :187826] Error handling issues in /tests/benchmarks/timing\_info/src/msg\_passing\_bench.c
- [GitHub #9634](https://github.com/zephyrproject-rtos/zephyr/issues/9634) - [Coverity CID :187827] Null pointer dereferences in /subsys/logging/log\_msg.c
- [GitHub #9633](https://github.com/zephyrproject-rtos/zephyr/issues/9633) - [Coverity CID :187828] Error handling issues in /tests/benchmarks/timing\_info/src/msg\_passing\_bench.c
- [GitHub #9630](https://github.com/zephyrproject-rtos/zephyr/issues/9630) - STM32L4: something wrong with GPIO interrupts
- [GitHub #9623](https://github.com/zephyrproject-rtos/zephyr/issues/9623) - tests/net/lib/tls\_credentials/ crashed on sam\_e70\_xplained and frdm\_k64f
- [GitHub #9622](https://github.com/zephyrproject-rtos/zephyr/issues/9622) - tests/net/mgmt/ crashed on sam\_e70\_xplained
- [GitHub #9621](https://github.com/zephyrproject-rtos/zephyr/issues/9621) - tests/net/promiscuous crashed on sam\_e70\_xplained
- [GitHub #9619](https://github.com/zephyrproject-rtos/zephyr/issues/9619) - tests/net/socket/getaddrinfo/ - crashes on sam\_e70\_xplained and frdm\_k64f
- [GitHub #9618](https://github.com/zephyrproject-rtos/zephyr/issues/9618) - tests/net/udp/ - MPU fault on sam\_e70\_xplained
- [GitHub #9617](https://github.com/zephyrproject-rtos/zephyr/issues/9617) - tests/net/websocket/ - passed on QEMUx86 but the target crashed after that
- [GitHub #9614](https://github.com/zephyrproject-rtos/zephyr/issues/9614) - tests/net/socket/ faults on sam\_e70\_xplained and frdm\_k64f
- [GitHub #9611](https://github.com/zephyrproject-rtos/zephyr/issues/9611) - tests/kernel/sched/schedule\_api/testcase.yaml#kernel.sched.slice\_reset fails on nrf52840\_pca10056, sam\_e70\_xplained, nrf52\_pca10040
- [GitHub #9609](https://github.com/zephyrproject-rtos/zephyr/issues/9609) - tests/kernel/mem\_protect/stack\_random: kernel.memory\_protection.stack\_random fails on emsk7d\_v22
- [GitHub #9598](https://github.com/zephyrproject-rtos/zephyr/issues/9598) - tests/power/power\_states fail on arduino101:x86
- [GitHub #9597](https://github.com/zephyrproject-rtos/zephyr/issues/9597) - tests/subsys/fs/fat\_fs\_api assertion fail on arduino101
- [GitHub #9591](https://github.com/zephyrproject-rtos/zephyr/issues/9591) - @hci.h use of magic-number in bluetooth addr struct (Missing define in @bluetooth.h)
- [GitHub #9580](https://github.com/zephyrproject-rtos/zephyr/issues/9580) - peripheral\_hids does not remember bonds
- [GitHub #9575](https://github.com/zephyrproject-rtos/zephyr/issues/9575) - Network NULL pointer reference when enable net/dhcpv4 debug
- [GitHub #9574](https://github.com/zephyrproject-rtos/zephyr/issues/9574) - tests/cmsis\_rtos\_v1 - test\_mutex\_lock\_timeout results in Assertion failure on all targets with PR#9569
- [GitHub #9561](https://github.com/zephyrproject-rtos/zephyr/issues/9561) - Question: Does it support passing the bootloader(mcuboot) parameter to the kernel(zephyr)?
- [GitHub #9558](https://github.com/zephyrproject-rtos/zephyr/issues/9558) - DTC 1.4.7 breaks at least FRDM\_K64F builds
- [GitHub #9537](https://github.com/zephyrproject-rtos/zephyr/issues/9537) - ENC28J60 can’t receive packets properly
- [GitHub #9536](https://github.com/zephyrproject-rtos/zephyr/issues/9536) - console: missing kernel.h include in header
- [GitHub #9535](https://github.com/zephyrproject-rtos/zephyr/issues/9535) - broken callback handling in nrfx gpio driver
- [GitHub #9530](https://github.com/zephyrproject-rtos/zephyr/issues/9530) - Bluetooth/gatt: bt\_gatt\_notify never return -ENOMEM, undocumented return value.
- [GitHub #9527](https://github.com/zephyrproject-rtos/zephyr/issues/9527) - tests/kernel/sched/schedule\_api/testcase.yaml#kernel.sched.unlock\_preemptible fails on nrf52840\_pca10056, sam\_e70\_xplained, nrf52\_pca10040
- [GitHub #9523](https://github.com/zephyrproject-rtos/zephyr/issues/9523) - tests/kernel/mem\_protect/stackprot hangs without any console output on nrf51/52
- [GitHub #9494](https://github.com/zephyrproject-rtos/zephyr/issues/9494) - Nordic nrf52810\_pca10040 is missing default bluetooth configuration options
- [GitHub #9487](https://github.com/zephyrproject-rtos/zephyr/issues/9487) - tests/cmsis\_rtos\_v1 - test\_kernel\_systick results in Assertion failure on nrf51/52
- [GitHub #9486](https://github.com/zephyrproject-rtos/zephyr/issues/9486) - sanitycheck filter rules does not work
- [GitHub #9471](https://github.com/zephyrproject-rtos/zephyr/issues/9471) - soc: efr32fg1p: hello\_world sample app hangs when started by MCUboot
- [GitHub #9470](https://github.com/zephyrproject-rtos/zephyr/issues/9470) - LWM2M: TLV encoding of read result is wrong
- [GitHub #9468](https://github.com/zephyrproject-rtos/zephyr/issues/9468) - tests/kernel/mem\_pool/mem\_pool\_concept/testcase.yaml#kernel.memory\_pool fails on nrf52840\_pca10056, nrf52\_pca10040 and nrf51\_pca10028
- [GitHub #9466](https://github.com/zephyrproject-rtos/zephyr/issues/9466) - tests/kernel/context/testcase.yaml#kernel.common.k\_sleep fails on nrf52\_pca10040 and nrf52840\_pca10056
- [GitHub #9465](https://github.com/zephyrproject-rtos/zephyr/issues/9465) - tests/net/ptp/clock: PTP clock test are failing on FRDM\_K64f and same\_e70\_xplained platforms
- [GitHub #9462](https://github.com/zephyrproject-rtos/zephyr/issues/9462) - [Coverity CID :187670] Integer handling issues in /tests/net/ethernet\_mgmt/src/main.c
- [GitHub #9461](https://github.com/zephyrproject-rtos/zephyr/issues/9461) - [Coverity CID :187671] Uninitialized variables in /tests/net/iface/src/main.c
- [GitHub #9460](https://github.com/zephyrproject-rtos/zephyr/issues/9460) - [Coverity CID :187672] Uninitialized variables in /tests/net/iface/src/main.c
- [GitHub #9459](https://github.com/zephyrproject-rtos/zephyr/issues/9459) - tests/posix/timer fails on nRF51/52
- [GitHub #9452](https://github.com/zephyrproject-rtos/zephyr/issues/9452) - Error parsing DTS ‘compatible’ property list
- [GitHub #9446](https://github.com/zephyrproject-rtos/zephyr/issues/9446) - CI didn’t report failure due to ARC\_INIT issue
- [GitHub #9444](https://github.com/zephyrproject-rtos/zephyr/issues/9444) - sanitycheck not able to run due to CONFIG\_ARC\_INIT=n
- [GitHub #9441](https://github.com/zephyrproject-rtos/zephyr/issues/9441) - tests/kernel/gen\_isr\_table fails on mimxrt1050\_evk
- [GitHub #9413](https://github.com/zephyrproject-rtos/zephyr/issues/9413) - tests/cmsis\_rtos\_v1 - test\_signal\_events\_signalled results in Assertion failure on nrf51/52
- [GitHub #9402](https://github.com/zephyrproject-rtos/zephyr/issues/9402) - samples/drivers/watchdog fails on frdm\_k64f
- [GitHub #9396](https://github.com/zephyrproject-rtos/zephyr/issues/9396) - ./loop-socat.sh not running
- [GitHub #9392](https://github.com/zephyrproject-rtos/zephyr/issues/9392) - samples/bluetooth/hci\_uart ninja flash - UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe2 in position 360: ordinal not in range(128)
- [GitHub #9389](https://github.com/zephyrproject-rtos/zephyr/issues/9389) - ESP32 support: setting env var ESP\_DEVICE not working
- [GitHub #9356](https://github.com/zephyrproject-rtos/zephyr/issues/9356) - Test tests/crypto/rand32 hangs on nrf51\_pca10028
- [GitHub #9348](https://github.com/zephyrproject-rtos/zephyr/issues/9348) - samples: net: echo\_client/echo\_server does not work with IPv4 qemu\_x86
- [GitHub #9310](https://github.com/zephyrproject-rtos/zephyr/issues/9310) - nRF52\_PCA10040: Failing test\_slice\_reset
- [GitHub #9297](https://github.com/zephyrproject-rtos/zephyr/issues/9297) - [Coverity CID :187318] Error handling issues in /tests/posix/pthread\_key/src/pthread\_key.c
- [GitHub #9296](https://github.com/zephyrproject-rtos/zephyr/issues/9296) - [Coverity CID :187319] Control flow issues in /subsys/net/lib/sockets/sockets.c
- [GitHub #9295](https://github.com/zephyrproject-rtos/zephyr/issues/9295) - [Coverity CID :187320] Control flow issues in /drivers/ethernet/eth\_sam\_gmac.c
- [GitHub #9294](https://github.com/zephyrproject-rtos/zephyr/issues/9294) - [Coverity CID :187321] Possible Control flow issues in /samples/net/sockets/big\_http\_download/src/big\_http\_download.c
- [GitHub #9293](https://github.com/zephyrproject-rtos/zephyr/issues/9293) - [Coverity CID :187322] Incorrect expression in /tests/posix/pthread\_key/src/pthread\_key.c
- [GitHub #9292](https://github.com/zephyrproject-rtos/zephyr/issues/9292) - [Coverity CID :187323] Control flow issues in /subsys/net/ip/net\_if.c
- [GitHub #9291](https://github.com/zephyrproject-rtos/zephyr/issues/9291) - [Coverity CID :187324] Control flow issues in /subsys/net/lib/sockets/sockets.c
- [GitHub #9287](https://github.com/zephyrproject-rtos/zephyr/issues/9287) - net/dhcpv4: Fix single byte buffer filling madness
- [GitHub #9273](https://github.com/zephyrproject-rtos/zephyr/issues/9273) - k\_pipe\_alloc\_init() api is failing on qemu\_x86
- [GitHub #9270](https://github.com/zephyrproject-rtos/zephyr/issues/9270) - cmake: kconfig: menuconfig is not writing zephyr/.config
- [GitHub #9262](https://github.com/zephyrproject-rtos/zephyr/issues/9262) - tests/kernel/mem\_protect/userspace.access\_other\_memdomain fails on sam\_e70\_xplained and nrf52840\_pca10056
- [GitHub #9238](https://github.com/zephyrproject-rtos/zephyr/issues/9238) - Get POSIX board compliant with default configuration guidelines
- [GitHub #9234](https://github.com/zephyrproject-rtos/zephyr/issues/9234) - Get ARC boards compliant with default configuration guidelines
- [GitHub #9224](https://github.com/zephyrproject-rtos/zephyr/issues/9224) - sam\_e70\_xplained fails to build several tests
- [GitHub #9221](https://github.com/zephyrproject-rtos/zephyr/issues/9221) - calloc memory data is not initialized to zero for MINIMAL\_LIBC
- [GitHub #9198](https://github.com/zephyrproject-rtos/zephyr/issues/9198) - Out-of-Tree YAML and DTS support
- [GitHub #9196](https://github.com/zephyrproject-rtos/zephyr/issues/9196) - optimize gen\_kobject\_list.py
- [GitHub #9160](https://github.com/zephyrproject-rtos/zephyr/issues/9160) - net: openthread: Mesh Local IPv6 is not in zephyr stack
- [GitHub #9148](https://github.com/zephyrproject-rtos/zephyr/issues/9148) - samples/net/http\_server: Failed to respond back to CURL command on http Client
- [GitHub #9135](https://github.com/zephyrproject-rtos/zephyr/issues/9135) - Failure : “integer overflow in exp” on Altera-Max 10 platform
- [GitHub #9134](https://github.com/zephyrproject-rtos/zephyr/issues/9134) - Build failure with SAM\_e70 platform
- [GitHub #9131](https://github.com/zephyrproject-rtos/zephyr/issues/9131) - samples/net/coaps\_server: Failed to send response to coaps\_client
- [GitHub #9128](https://github.com/zephyrproject-rtos/zephyr/issues/9128) - doc build fails if no reST reference to file
- [GitHub #9113](https://github.com/zephyrproject-rtos/zephyr/issues/9113) - Enabling various thread options causes failures on cortex-M0 boards
- [GitHub #9108](https://github.com/zephyrproject-rtos/zephyr/issues/9108) - Which board is suit with esidon??
- [GitHub #9098](https://github.com/zephyrproject-rtos/zephyr/issues/9098) - Doc build failure not noticed by CI test system
- [GitHub #9081](https://github.com/zephyrproject-rtos/zephyr/issues/9081) - dynamic thread objects do not have a thread ID assigned
- [GitHub #9067](https://github.com/zephyrproject-rtos/zephyr/issues/9067) - Failed tests: posix.sema and posix\_checks on em\_starterkit\_em7d\_v22
- [GitHub #9061](https://github.com/zephyrproject-rtos/zephyr/issues/9061) - sanitycheck not printing QEMU console in some cases
- [GitHub #9058](https://github.com/zephyrproject-rtos/zephyr/issues/9058) - Kconfig default on BT\_ACL\_RX\_COUNT can be 1, but range is 2-64
- [GitHub #9054](https://github.com/zephyrproject-rtos/zephyr/issues/9054) - Build failures with mimxrt1050\_evk board
- [GitHub #9044](https://github.com/zephyrproject-rtos/zephyr/issues/9044) - “logging: Remove log.h including in headers limitation” breaks logging
- [GitHub #9032](https://github.com/zephyrproject-rtos/zephyr/issues/9032) - net/sockets/echo\_async crashes after several connections (qemu\_x86)
- [GitHub #9028](https://github.com/zephyrproject-rtos/zephyr/issues/9028) - STM32 SPI/I2S: LSB bit corrupted for the received data
- [GitHub #9019](https://github.com/zephyrproject-rtos/zephyr/issues/9019) - cmsis Include/ version mismatch
- [GitHub #9006](https://github.com/zephyrproject-rtos/zephyr/issues/9006) - Create driver for the MMA8451Q accelerometer sensor on FRDM-KL25Z
- [GitHub #9002](https://github.com/zephyrproject-rtos/zephyr/issues/9002) - [Coverity CID :187063] Control flow issues in /subsys/net/l2/ethernet/ethernet\_mgmt.c
- [GitHub #9001](https://github.com/zephyrproject-rtos/zephyr/issues/9001) - [Coverity CID :187064] Control flow issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #9000](https://github.com/zephyrproject-rtos/zephyr/issues/9000) - [Coverity CID :187065] Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #8998](https://github.com/zephyrproject-rtos/zephyr/issues/8998) - [Coverity CID :187068] Memory - illegal accesses in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #8997](https://github.com/zephyrproject-rtos/zephyr/issues/8997) - [Coverity CID :187069] Memory - illegal accesses in /subsys/logging/log\_msg.c
- [GitHub #8996](https://github.com/zephyrproject-rtos/zephyr/issues/8996) - [Coverity CID :187070] Control flow issues in /drivers/bluetooth/hci/spi.c
- [GitHub #8995](https://github.com/zephyrproject-rtos/zephyr/issues/8995) - [Coverity CID :187071] Insecure data handling in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #8994](https://github.com/zephyrproject-rtos/zephyr/issues/8994) - [Coverity CID :187072] Error handling issues in /samples/net/sockets/echo\_server/src/udp.c
- [GitHub #8993](https://github.com/zephyrproject-rtos/zephyr/issues/8993) - [Coverity CID :187073] Null pointer dereferences in /subsys/net/ip/utils.c
- [GitHub #8992](https://github.com/zephyrproject-rtos/zephyr/issues/8992) - [Coverity CID :187074] Incorrect expression in /samples/net/traffic\_class/src/main.c
- [GitHub #8991](https://github.com/zephyrproject-rtos/zephyr/issues/8991) - [Coverity CID :187075] Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #8990](https://github.com/zephyrproject-rtos/zephyr/issues/8990) - [Coverity CID :187077] Memory - corruptions in /samples/net/rpl\_border\_router/src/http.c
- [GitHub #8989](https://github.com/zephyrproject-rtos/zephyr/issues/8989) - [Coverity CID :187078] Control flow issues in /subsys/net/l2/ethernet/gptp/gptp\_md.c
- [GitHub #8988](https://github.com/zephyrproject-rtos/zephyr/issues/8988) - [Coverity CID :187079] Integer handling issues in /subsys/net/l2/ethernet/gptp/gptp.c
- [GitHub #8987](https://github.com/zephyrproject-rtos/zephyr/issues/8987) - [Coverity CID :187080] Control flow issues in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #8982](https://github.com/zephyrproject-rtos/zephyr/issues/8982) - tests/drivers/watchdog/wdt\_basic\_api results in FATAL EXCEPTION on esp32
- [GitHub #8977](https://github.com/zephyrproject-rtos/zephyr/issues/8977) - CMake Error
- [GitHub #8976](https://github.com/zephyrproject-rtos/zephyr/issues/8976) - nordic: watchdog: Cannot be initialized - circular dependency
- [GitHub #8968](https://github.com/zephyrproject-rtos/zephyr/issues/8968) - The tests/kernel/tickless/tickless\_concept fails on nRF5x
- [GitHub #8963](https://github.com/zephyrproject-rtos/zephyr/issues/8963) - tests/net/trickle, utils and icmpv6 hangs on sam\_e70\_xplained:arm
- [GitHub #8960](https://github.com/zephyrproject-rtos/zephyr/issues/8960) - Tcp connection not connecting
- [GitHub #8950](https://github.com/zephyrproject-rtos/zephyr/issues/8950) - ARM fault dumping code does too much, assumes all faults are fatal, and doesn’t work under some configurations
- [GitHub #8949](https://github.com/zephyrproject-rtos/zephyr/issues/8949) - nsim\_sem board does not work
- [GitHub #8933](https://github.com/zephyrproject-rtos/zephyr/issues/8933) - doc: build WARNING on windows 7
- [GitHub #8931](https://github.com/zephyrproject-rtos/zephyr/issues/8931) - STM32L4 CAN sample project does not compile
- [GitHub #8924](https://github.com/zephyrproject-rtos/zephyr/issues/8924) - Get rid of -fno-strict-overflow
- [GitHub #8906](https://github.com/zephyrproject-rtos/zephyr/issues/8906) - zsock\_getaddrinfo is not reentrant
- [GitHub #8899](https://github.com/zephyrproject-rtos/zephyr/issues/8899) - Failed test: kernel.common.timing.sleep on nrf52 (tests/kernel/sleep/kernel.common.timing)
- [GitHub #8898](https://github.com/zephyrproject-rtos/zephyr/issues/8898) - Failed test: kernel.timer.timer\_periodicity on nrf51/nrf52
- [GitHub #8897](https://github.com/zephyrproject-rtos/zephyr/issues/8897) - Failed test: kernel.tickless.tickless\_slice on nrf51/nrf52
- [GitHub #8896](https://github.com/zephyrproject-rtos/zephyr/issues/8896) - Failed test: kernel.sched.slice\_reset and kernel.sched.slice\_scheduling (tests/kernel/sched/schedule\_api/kernel.sched) on nrf51/nrf52
- [GitHub #8895](https://github.com/zephyrproject-rtos/zephyr/issues/8895) - Failed test: kernel.common.timing.pending on nrf51\_pca10028 and nrf52\_pca10040 (tests/kernel/pending/kernel.common.timing)
- [GitHub #8888](https://github.com/zephyrproject-rtos/zephyr/issues/8888) - http client example fails on mimxrt1050\_evk
- [GitHub #8887](https://github.com/zephyrproject-rtos/zephyr/issues/8887) - Ping command crash on mimxrt1050\_evk
- [GitHub #8871](https://github.com/zephyrproject-rtos/zephyr/issues/8871) - drivers: can: Compiling error due to stm23Cube update
- [GitHub #8866](https://github.com/zephyrproject-rtos/zephyr/issues/8866) - Failed test: net.arp.arp (tests/net/arp) on sam\_e70\_xplained
- [GitHub #8865](https://github.com/zephyrproject-rtos/zephyr/issues/8865) - Failed test: net.udp.udp (tests/net/udp/) on sam\_e70\_xplained
- [GitHub #8864](https://github.com/zephyrproject-rtos/zephyr/issues/8864) - ARM MPU \_arch\_buffer\_validate allowing reads to kernel memory
- [GitHub #8860](https://github.com/zephyrproject-rtos/zephyr/issues/8860) - GATT MTU Callback
- [GitHub #8849](https://github.com/zephyrproject-rtos/zephyr/issues/8849) - Allow application to define its own DTS bindings
- [GitHub #8833](https://github.com/zephyrproject-rtos/zephyr/issues/8833) - OpenThread: Minimal Thread Device (MTD) option is not building
- [GitHub #8829](https://github.com/zephyrproject-rtos/zephyr/issues/8829) - BLE “device name” characteristic of Generic Access Service is read only
- [GitHub #8820](https://github.com/zephyrproject-rtos/zephyr/issues/8820) - wifi\_winc1500 driver socket id stored in net\_context->user\_data may be overwritten at socket layer
- [GitHub #8815](https://github.com/zephyrproject-rtos/zephyr/issues/8815) - Nordic: Directly accessing GPIOTE might create unstable firmware (GPIO, PWM, BLE)
- [GitHub #8800](https://github.com/zephyrproject-rtos/zephyr/issues/8800) - cmake errors with menuconfig
- [GitHub #8798](https://github.com/zephyrproject-rtos/zephyr/issues/8798) - k\_cycle\_get\_32() implementation on nrf series is too slow.
- [GitHub #8791](https://github.com/zephyrproject-rtos/zephyr/issues/8791) - Request supporting OTG\_HS port on STM32F4/F7 SoCs
- [GitHub #8790](https://github.com/zephyrproject-rtos/zephyr/issues/8790) - K64F/Kinetis: extract\_dts\_includes.py warnings when building sample
- [GitHub #8752](https://github.com/zephyrproject-rtos/zephyr/issues/8752) - net: ARP is broken after PR #8608
- [GitHub #8732](https://github.com/zephyrproject-rtos/zephyr/issues/8732) - tests/subsys/usb/bos/ fails randomly
- [GitHub #8727](https://github.com/zephyrproject-rtos/zephyr/issues/8727) - Network stack cleanup: DHCPv4
- [GitHub #8720](https://github.com/zephyrproject-rtos/zephyr/issues/8720) - Network stack cleanup: IPv4
- [GitHub #8717](https://github.com/zephyrproject-rtos/zephyr/issues/8717) - posix: Memory is not returned to mempool when a pthread complete its execution
- [GitHub #8715](https://github.com/zephyrproject-rtos/zephyr/issues/8715) - buffer-overflow in tests/net/tx\_timestamp
- [GitHub #8713](https://github.com/zephyrproject-rtos/zephyr/issues/8713) - add DTS gpio support for NRF51
- [GitHub #8705](https://github.com/zephyrproject-rtos/zephyr/issues/8705) - Out of the box error in samples/subsys/nvs with nRF52-PCA10040
- [GitHub #8700](https://github.com/zephyrproject-rtos/zephyr/issues/8700) - [Coverity CID :186841] Null pointer dereferences in /subsys/usb/usb\_descriptor.c
- [GitHub #8699](https://github.com/zephyrproject-rtos/zephyr/issues/8699) - [Coverity CID :186842] Memory - illegal accesses in /drivers/interrupt\_controller/plic.c
- [GitHub #8698](https://github.com/zephyrproject-rtos/zephyr/issues/8698) - [Coverity CID :186843] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #8697](https://github.com/zephyrproject-rtos/zephyr/issues/8697) - [Coverity CID :186844] Parse warnings in /tests/net/ieee802154/fragment/src/main.c
- [GitHub #8696](https://github.com/zephyrproject-rtos/zephyr/issues/8696) - [Coverity CID :186845] Parse warnings in /tests/net/ieee802154/l2/src/ieee802154\_test.c
- [GitHub #8695](https://github.com/zephyrproject-rtos/zephyr/issues/8695) - [Coverity CID :186846] Null pointer dereferences in /tests/net/ptp/clock/src/main.c
- [GitHub #8694](https://github.com/zephyrproject-rtos/zephyr/issues/8694) - [Coverity CID :186847] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/inherit.c
- [GitHub #8693](https://github.com/zephyrproject-rtos/zephyr/issues/8693) - [Coverity CID :186848] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #8692](https://github.com/zephyrproject-rtos/zephyr/issues/8692) - [Coverity CID :186849] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #8691](https://github.com/zephyrproject-rtos/zephyr/issues/8691) - [Coverity CID :186850] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #8690](https://github.com/zephyrproject-rtos/zephyr/issues/8690) - [Coverity CID :186851] Error handling issues in /tests/bluetooth/mesh/src/microbit.c
- [GitHub #8689](https://github.com/zephyrproject-rtos/zephyr/issues/8689) - [Coverity CID :186852] Parse warnings in /tests/kernel/mem\_protect/mem\_protect/src/mem\_domain.c
- [GitHub #8669](https://github.com/zephyrproject-rtos/zephyr/issues/8669) - fault during my timer testing
- [GitHub #8668](https://github.com/zephyrproject-rtos/zephyr/issues/8668) - net: ARP is broken in master (at least) on STM32
- [GitHub #8658](https://github.com/zephyrproject-rtos/zephyr/issues/8658) - tests/net/trickle fails on FRDM k64f
- [GitHub #8657](https://github.com/zephyrproject-rtos/zephyr/issues/8657) - tests/net/ptp fails on QEMU x86
- [GitHub #8646](https://github.com/zephyrproject-rtos/zephyr/issues/8646) - CONFIG\_NET\_OFFLOAD defined in subsys/net/l2/, but not referenced there
- [GitHub #8643](https://github.com/zephyrproject-rtos/zephyr/issues/8643) - Add SAADC driver for nRF52
- [GitHub #8642](https://github.com/zephyrproject-rtos/zephyr/issues/8642) - ieee802154 tests fail to build
- [GitHub #8636](https://github.com/zephyrproject-rtos/zephyr/issues/8636) - MCUboot firmware update issue
- [GitHub #8611](https://github.com/zephyrproject-rtos/zephyr/issues/8611) - RT1050EVK: MPU FAULT with Zephyr OS v1.12.0-360-gf3d1b22 using ztest
- [GitHub #8610](https://github.com/zephyrproject-rtos/zephyr/issues/8610) - USB: Setup stage in control transfers
- [GitHub #8605](https://github.com/zephyrproject-rtos/zephyr/issues/8605) - mbedtls\_ssl\_close\_notify was called after DTLS context released
- [GitHub #8602](https://github.com/zephyrproject-rtos/zephyr/issues/8602) - master broken for stm32 ARM boards
- [GitHub #8600](https://github.com/zephyrproject-rtos/zephyr/issues/8600) - Not able to bind the adc device structure for nrf52832 controller
- [GitHub #8598](https://github.com/zephyrproject-rtos/zephyr/issues/8598) - [Coverity CID :186057] - Out of bounds write in samples/net/rpl\_border\_router/src/coap.c
- [GitHub #8596](https://github.com/zephyrproject-rtos/zephyr/issues/8596) - drivers: dma\_cavs: NULL pointer exception when DMA start called after DMA stop
- [GitHub #8593](https://github.com/zephyrproject-rtos/zephyr/issues/8593) - samples/mpu/mem\_domain\_apis\_test/kernel.memory\_protection.memory\_domains fails to build
- [GitHub #8587](https://github.com/zephyrproject-rtos/zephyr/issues/8587) - ZTEST should support multiple calls to mocked function
- [GitHub #8584](https://github.com/zephyrproject-rtos/zephyr/issues/8584) - ToolchainCapabilityDatabase.cmake:93 error in PR #8579
- [GitHub #8576](https://github.com/zephyrproject-rtos/zephyr/issues/8576) - there have a error in doc
- [GitHub #8567](https://github.com/zephyrproject-rtos/zephyr/issues/8567) - Can’t parse json
- [GitHub #8563](https://github.com/zephyrproject-rtos/zephyr/issues/8563) - Compilation warning/error on stm32l4: “\_\_weak” redefined
- [GitHub #8529](https://github.com/zephyrproject-rtos/zephyr/issues/8529) - tests/kernel/common/kernel.common fails for native\_posix on Ubuntu 16.04
- [GitHub #8528](https://github.com/zephyrproject-rtos/zephyr/issues/8528) - rpl-mesh-qemu sample, the net inface init failed.
- [GitHub #8511](https://github.com/zephyrproject-rtos/zephyr/issues/8511) - nrf52\_blenano2 tmp112 sensor sample build failed - redefined I2C
- [GitHub #8506](https://github.com/zephyrproject-rtos/zephyr/issues/8506) - tests/subsys/fs/fat\_fs\_api - test\_fat\_mount results into assertion failure on Arduino\_101 - FS init failed (-19)
- [GitHub #8502](https://github.com/zephyrproject-rtos/zephyr/issues/8502) - Compiling for native\_posix with newlib is missing various math symbols
- [GitHub #8501](https://github.com/zephyrproject-rtos/zephyr/issues/8501) - I think there is a issue about shell.
- [GitHub #8470](https://github.com/zephyrproject-rtos/zephyr/issues/8470) - Broken Arduino 101 Bluetooth Core flashing
- [GitHub #8466](https://github.com/zephyrproject-rtos/zephyr/issues/8466) - k\_sleep on mimxrt1050\_evk board broken
- [GitHub #8464](https://github.com/zephyrproject-rtos/zephyr/issues/8464) - sdk\_version file missing
- [GitHub #8462](https://github.com/zephyrproject-rtos/zephyr/issues/8462) - non-ASCII / non-UTF-8 files in ext/
- [GitHub #8452](https://github.com/zephyrproject-rtos/zephyr/issues/8452) - ieee802154: csma-ca: random backoff factor looks wrong
- [GitHub #8444](https://github.com/zephyrproject-rtos/zephyr/issues/8444) - “make clean” removes include directory
- [GitHub #8438](https://github.com/zephyrproject-rtos/zephyr/issues/8438) - cmake: Propagation of library specific compile flag
- [GitHub #8434](https://github.com/zephyrproject-rtos/zephyr/issues/8434) - Networking Problems, Size Missmatch 15 vs 13
- [GitHub #8431](https://github.com/zephyrproject-rtos/zephyr/issues/8431) - mqtt: unimplemented MQTT\_UNSUBACK in mqtt\_parser function in mqtt.c file
- [GitHub #8424](https://github.com/zephyrproject-rtos/zephyr/issues/8424) - HID example broken
- [GitHub #8416](https://github.com/zephyrproject-rtos/zephyr/issues/8416) - [Coverity CID :186580] Uninitialized variables in /drivers/can/stm32\_can.c
- [GitHub #8415](https://github.com/zephyrproject-rtos/zephyr/issues/8415) - [Coverity CID :186581] Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #8414](https://github.com/zephyrproject-rtos/zephyr/issues/8414) - [Coverity CID :186582] Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #8413](https://github.com/zephyrproject-rtos/zephyr/issues/8413) - [Coverity CID :186583] Error handling issues in /samples/net/sockets/dumb\_http\_server/src/socket\_dumb\_http.c
- [GitHub #8393](https://github.com/zephyrproject-rtos/zephyr/issues/8393) - `CONFIG_MULTITHREADING=n` builds call main() with interrupts locked
- [GitHub #8391](https://github.com/zephyrproject-rtos/zephyr/issues/8391) - nrf52\_blenano2 tmp112 sensor sample build failed.
- [GitHub #8390](https://github.com/zephyrproject-rtos/zephyr/issues/8390) - bluetooth: request APIs to notify application that pairing is complete or not
- [GitHub #8388](https://github.com/zephyrproject-rtos/zephyr/issues/8388) - Assigning to promptless symbols should have a better error message
- [GitHub #8385](https://github.com/zephyrproject-rtos/zephyr/issues/8385) - Missing documentation on bt\_conn\_auth\_cb(…)
- [GitHub #8382](https://github.com/zephyrproject-rtos/zephyr/issues/8382) - ESP32: add support for ESP-IDF bootloader
- [GitHub #8380](https://github.com/zephyrproject-rtos/zephyr/issues/8380) - cmake: ninja clean tries to remove include folders
- [GitHub #8378](https://github.com/zephyrproject-rtos/zephyr/issues/8378) - subsys: settings: Idea for a very simple settings system
- [GitHub #8371](https://github.com/zephyrproject-rtos/zephyr/issues/8371) - nRF5: enable UARTE peripheral support
- [GitHub #8367](https://github.com/zephyrproject-rtos/zephyr/issues/8367) - fs: nvs: auto restore FS on writing while power down error.
- [GitHub #8366](https://github.com/zephyrproject-rtos/zephyr/issues/8366) - mcumgr: unable to perform 2nd update
- [GitHub #8365](https://github.com/zephyrproject-rtos/zephyr/issues/8365) - mcumgr: improper response to “image list” command after update.
- [GitHub #8361](https://github.com/zephyrproject-rtos/zephyr/issues/8361) - \_\_ASSERT() triggers with `CONFIG_MULTITHREADING=n`
- [GitHub #8358](https://github.com/zephyrproject-rtos/zephyr/issues/8358) - Flashing Target Device FAIL
- [GitHub #8357](https://github.com/zephyrproject-rtos/zephyr/issues/8357) - bluetooth: request the capability to change gap device name programmatically
- [GitHub #8356](https://github.com/zephyrproject-rtos/zephyr/issues/8356) - Failed test: kernel.common.bitfield (tests/kernel/common) on Altera Max10
- [GitHub #8355](https://github.com/zephyrproject-rtos/zephyr/issues/8355) - CMake prints a spammy warning about “policy CMP0000”
- [GitHub #8350](https://github.com/zephyrproject-rtos/zephyr/issues/8350) - bluetooth: request BLE stack to support pre-set passkey for pairing
- [GitHub #8334](https://github.com/zephyrproject-rtos/zephyr/issues/8334) - nrf52840.dtsi contains “0x” in device label
- [GitHub #8329](https://github.com/zephyrproject-rtos/zephyr/issues/8329) - qustion: build-system: How to generate a preprocess file
- [GitHub #8327](https://github.com/zephyrproject-rtos/zephyr/issues/8327) - CONFIG\_SPI\_FLASH\_W25QXXDV\_MAX\_DATA\_LEN doesn’t work in proj.conf
- [GitHub #8322](https://github.com/zephyrproject-rtos/zephyr/issues/8322) - LwM2M: Occasional registration updates fail with 4.4 error
- [GitHub #8313](https://github.com/zephyrproject-rtos/zephyr/issues/8313) - Enable hardware stack checking for ARC em\_starterkit\_em7d (Secure mode)
- [GitHub #8311](https://github.com/zephyrproject-rtos/zephyr/issues/8311) - tests/benchmarks/sys\_kernel fails on frdm\_k64f, sam\_e70
- [GitHub #8309](https://github.com/zephyrproject-rtos/zephyr/issues/8309) - lpcxpresso54114\_m4: when i configed system clock from 48M to 96M the target can’t work.
- [GitHub #8302](https://github.com/zephyrproject-rtos/zephyr/issues/8302) - Failed test: peripheral.adc.adc on quark\_se
- [GitHub #8300](https://github.com/zephyrproject-rtos/zephyr/issues/8300) - Failed test: kernel.memory\_protection.userspace.access\_after\_revoke (in tests/kernel/mem\_protect/userspace)
- [GitHub #8299](https://github.com/zephyrproject-rtos/zephyr/issues/8299) - Failed test: kernel.memory\_pool.mpool\_alloc\_free\_isr (in tests/kernel/mem\_pool/mem\_pool\_api)
- [GitHub #8298](https://github.com/zephyrproject-rtos/zephyr/issues/8298) - Failed test: kernel.alert.isr\_alert\_consumed (in tests/kernel/alert/) on quark\_se\_c1000\_ss
- [GitHub #8293](https://github.com/zephyrproject-rtos/zephyr/issues/8293) - ARM: MPU faults should indicate faulting memory address
- [GitHub #8292](https://github.com/zephyrproject-rtos/zephyr/issues/8292) - Rework ARC exception stack
- [GitHub #8287](https://github.com/zephyrproject-rtos/zephyr/issues/8287) - LwM2M: Cancelling an observation doesn’t work
- [GitHub #8286](https://github.com/zephyrproject-rtos/zephyr/issues/8286) - LwM2M: Observe of not allowed value still creates observer
- [GitHub #8284](https://github.com/zephyrproject-rtos/zephyr/issues/8284) - Documentation build on Windows
- [GitHub #8283](https://github.com/zephyrproject-rtos/zephyr/issues/8283) - Failed test: kernel.mailbox.msg\_receiver\_unlimited (tests/kernel/mbox/mbox\_usage/) on ESP32
- [GitHub #8262](https://github.com/zephyrproject-rtos/zephyr/issues/8262) - [Bluetooth] MPU FAULT on sdu\_recv
- [GitHub #8255](https://github.com/zephyrproject-rtos/zephyr/issues/8255) - [RFC] Add support for system suspend/resume handling from kernel
- [GitHub #8252](https://github.com/zephyrproject-rtos/zephyr/issues/8252) - GPIO interrupt only called once on nRF52832
- [GitHub #8240](https://github.com/zephyrproject-rtos/zephyr/issues/8240) - ESP32: update to recent ESP-IDF
- [GitHub #8235](https://github.com/zephyrproject-rtos/zephyr/issues/8235) - nxp\_lpc54102: how to add lpc54102 support?
- [GitHub #8231](https://github.com/zephyrproject-rtos/zephyr/issues/8231) - GATT Macro Confusion
- [GitHub #8226](https://github.com/zephyrproject-rtos/zephyr/issues/8226) - drivers: can: stm32\_can: various issues
- [GitHub #8225](https://github.com/zephyrproject-rtos/zephyr/issues/8225) - Error mbedtls\_pk\_verify MBEDTLS\_ERR\_RSA\_VERIFY\_FAILED
- [GitHub #8215](https://github.com/zephyrproject-rtos/zephyr/issues/8215) - Update watchdog driver sample to new API
- [GitHub #8210](https://github.com/zephyrproject-rtos/zephyr/issues/8210) - Always rebuilding even though there are no changes.
- [GitHub #8206](https://github.com/zephyrproject-rtos/zephyr/issues/8206) - Stray files in libapp.a
- [GitHub #8203](https://github.com/zephyrproject-rtos/zephyr/issues/8203) - Implement system calls for the new socket APIs
- [GitHub #8199](https://github.com/zephyrproject-rtos/zephyr/issues/8199) - Tests: Crypto: rand32 faults on nrf51\_pca10028 and nrf52\_pca10040
- [GitHub #8188](https://github.com/zephyrproject-rtos/zephyr/issues/8188) - net: TCP: FIN packets aren’t queued for retransmission, loss leads to TCP timeout on peer’s side
- [GitHub #8183](https://github.com/zephyrproject-rtos/zephyr/issues/8183) - zsock\_getaddrinfo() is not reentrant
- [GitHub #8173](https://github.com/zephyrproject-rtos/zephyr/issues/8173) - Driver tests failing with an assertion on frdm\_k64f
- [GitHub #8138](https://github.com/zephyrproject-rtos/zephyr/issues/8138) - Unsatisfactory kernel benchmark results on SAM E-70 Xplained
- [GitHub #8128](https://github.com/zephyrproject-rtos/zephyr/issues/8128) - scheduler: threads using k\_sleep can be \_swap()’d back too early
- [GitHub #8125](https://github.com/zephyrproject-rtos/zephyr/issues/8125) - About BMI160 reading issue.
- [GitHub #8090](https://github.com/zephyrproject-rtos/zephyr/issues/8090) - tests/sched/schedule\_api fails to build on EMSK7d
- [GitHub #8041](https://github.com/zephyrproject-rtos/zephyr/issues/8041) - arm: NXP MPU does not report faulting address for Stacking Errors
- [GitHub #8039](https://github.com/zephyrproject-rtos/zephyr/issues/8039) - tests/shell failing on Arduino 101 / Quark SE arc
- [GitHub #8026](https://github.com/zephyrproject-rtos/zephyr/issues/8026) - Verify TLS server side operation
- [GitHub #8019](https://github.com/zephyrproject-rtos/zephyr/issues/8019) - ARP: should drop any packet pended when timeout
- [GitHub #8013](https://github.com/zephyrproject-rtos/zephyr/issues/8013) - Open-AMP power on can not communicate
- [GitHub #7999](https://github.com/zephyrproject-rtos/zephyr/issues/7999) - HCI UART with Linux host cannot connect to nrf52 6lowpan peripheral
- [GitHub #7978](https://github.com/zephyrproject-rtos/zephyr/issues/7978) - SSE and SSE\_FP\_MATH are set on frdm\_k64f, which doesn’t have it, triggering Kconfig warnings
- [GitHub #7977](https://github.com/zephyrproject-rtos/zephyr/issues/7977) - ARC\_INIT is set on boards that don’t have it, triggering Kconfig warnings
- [GitHub #7966](https://github.com/zephyrproject-rtos/zephyr/issues/7966) - Move k\_thread\_foreach() tests to tests/kernel/threads
- [GitHub #7924](https://github.com/zephyrproject-rtos/zephyr/issues/7924) - mcu\_mgmt: Memory corruption (cborattr suspected) - test case with smp\_svr
- [GitHub #7906](https://github.com/zephyrproject-rtos/zephyr/issues/7906) - tests/benchmarks/sys\_kernel fails on Arduino Due
- [GitHub #7884](https://github.com/zephyrproject-rtos/zephyr/issues/7884) - tests/power/power\_states never completes on Arduino 101’s arc core
- [GitHub #7882](https://github.com/zephyrproject-rtos/zephyr/issues/7882) - tests/dfu/mcuboot.test\_bank\_erase fails on nrf52840\_pca10056
- [GitHub #7869](https://github.com/zephyrproject-rtos/zephyr/issues/7869) - Improve Zero Latency IRQ on ARM
- [GitHub #7848](https://github.com/zephyrproject-rtos/zephyr/issues/7848) - CONFIG\_BMM150\_SET\_ATTR not defined (and now removed), giving dead code
- [GitHub #7800](https://github.com/zephyrproject-rtos/zephyr/issues/7800) - ext/lib/mgmt/mcumgr/cmd/log\_mgmt/Kconfig references MDLOG, but MDLOG doesn’t exist
- [GitHub #7758](https://github.com/zephyrproject-rtos/zephyr/issues/7758) - sanitycheck error with –coverage
- [GitHub #7705](https://github.com/zephyrproject-rtos/zephyr/issues/7705) - nxp\_kinetis/k6x boot MPU regions are configured incorrectly
- [GitHub #7703](https://github.com/zephyrproject-rtos/zephyr/issues/7703) - NUM\_KERNEL\_OBJECT\_FILES is too small
- [GitHub #7685](https://github.com/zephyrproject-rtos/zephyr/issues/7685) - API for 802.1Qav parameters configuration
- [GitHub #7678](https://github.com/zephyrproject-rtos/zephyr/issues/7678) - Unstable ping RTT with ethernet ipv4 networking
- [GitHub #7658](https://github.com/zephyrproject-rtos/zephyr/issues/7658) - [RFC] net: Split off net\_app\_settings lib to a separate directory under subsys/net/lib/
- [GitHub #7596](https://github.com/zephyrproject-rtos/zephyr/issues/7596) - API to communicate list of MAC addresses to the Ethernet controller
- [GitHub #7595](https://github.com/zephyrproject-rtos/zephyr/issues/7595) - Promiscuous mode and receiving all packets at applications level
- [GitHub #7571](https://github.com/zephyrproject-rtos/zephyr/issues/7571) - IP stack can’t recover from a packet overload
- [GitHub #7570](https://github.com/zephyrproject-rtos/zephyr/issues/7570) - usb: update bcdUSB to 2.00
- [GitHub #7553](https://github.com/zephyrproject-rtos/zephyr/issues/7553) - DHCP client does not notice missing link
- [GitHub #7509](https://github.com/zephyrproject-rtos/zephyr/issues/7509) - [Coverity CID :185398] Memory - corruptions in /samples/net/mbedtls\_sslclient/src/mini\_client.c
- [GitHub #7502](https://github.com/zephyrproject-rtos/zephyr/issues/7502) - samples/mbedtls\_sslclient: Discards TLS records, handshake does not work
- [GitHub #7473](https://github.com/zephyrproject-rtos/zephyr/issues/7473) - Bluetooth: Support for multiple local identity addresses
- [GitHub #7423](https://github.com/zephyrproject-rtos/zephyr/issues/7423) - samples: net: echo\_client: sample runs failed with prj\_qemu\_x86\_tls.conf configuration file
- [GitHub #7384](https://github.com/zephyrproject-rtos/zephyr/issues/7384) - ARM MPU region configuration possibly out of bounds
- [GitHub #7372](https://github.com/zephyrproject-rtos/zephyr/issues/7372) - Create socket options for certificates and ciphers
- [GitHub #7371](https://github.com/zephyrproject-rtos/zephyr/issues/7371) - Move TLS connection data out from net\_context
- [GitHub #7370](https://github.com/zephyrproject-rtos/zephyr/issues/7370) - Add Kconfig options to handle certificates and ciphers.
- [GitHub #7367](https://github.com/zephyrproject-rtos/zephyr/issues/7367) - Doxygen warnings about device.h macros
- [GitHub #7314](https://github.com/zephyrproject-rtos/zephyr/issues/7314) - Generate SPDX TagValue document as part of 1.13 release
- [GitHub #7310](https://github.com/zephyrproject-rtos/zephyr/issues/7310) - Provide signed Zephyr releases
- [GitHub #7243](https://github.com/zephyrproject-rtos/zephyr/issues/7243) - BLE DTM ll\_test does not set correct TXPower
- [GitHub #7230](https://github.com/zephyrproject-rtos/zephyr/issues/7230) - The guidelines for whether something should be in DTS or Kconfig are too vague
- [GitHub #7173](https://github.com/zephyrproject-rtos/zephyr/issues/7173) - Difference between the ZEPHYR\_BASE and PROJECT\_SOURCE\_DIR CMake variables is unclear
- [GitHub #7145](https://github.com/zephyrproject-rtos/zephyr/issues/7145) - Configuration file for Cross Toolchain on macOS
- [GitHub #7112](https://github.com/zephyrproject-rtos/zephyr/issues/7112) - ARMv8-M: API for checking permissions using ARMv8-M TT intrinsics
- [GitHub #7106](https://github.com/zephyrproject-rtos/zephyr/issues/7106) - tests: obj\_tracing: Test fails on ESP32, semaphore count is more than what is created in the application
- [GitHub #7042](https://github.com/zephyrproject-rtos/zephyr/issues/7042) - Ethernet network management interface additions for MAC filtering
- [GitHub #6982](https://github.com/zephyrproject-rtos/zephyr/issues/6982) - STM32F746G DISCOVERY board support
- [GitHub #6981](https://github.com/zephyrproject-rtos/zephyr/issues/6981) - STM32F7 series MCUs support
- [GitHub #6866](https://github.com/zephyrproject-rtos/zephyr/issues/6866) - build: requirements: No module named yaml and elftools
- [GitHub #6846](https://github.com/zephyrproject-rtos/zephyr/issues/6846) - need console subsystem abstraction for console syscalls
- [GitHub #6785](https://github.com/zephyrproject-rtos/zephyr/issues/6785) - Fail to compile when OT l2 debug is enabled.
- [GitHub #6778](https://github.com/zephyrproject-rtos/zephyr/issues/6778) - Push latest docs down into a “latest” folder
- [GitHub #6775](https://github.com/zephyrproject-rtos/zephyr/issues/6775) - Simplify left nav index on technical docs
- [GitHub #6749](https://github.com/zephyrproject-rtos/zephyr/issues/6749) - kconfig: The error message is misleading when values are out-of-range
- [GitHub #6730](https://github.com/zephyrproject-rtos/zephyr/issues/6730) - ARMv8-M: internal low-level (TrustZone) API & implementation for configuring IRQ target
- [GitHub #6727](https://github.com/zephyrproject-rtos/zephyr/issues/6727) - k\_mem\_pool crash with larger values of n\_max
- [GitHub #6681](https://github.com/zephyrproject-rtos/zephyr/issues/6681) - [Coverity CID: 183051] Error handling issues in /tests/benchmarks/app\_kernel/src/memmap\_b.c
- [GitHub #6678](https://github.com/zephyrproject-rtos/zephyr/issues/6678) - [Coverity CID: 183054] Memory - corruptions in /tests/lib/c\_lib/src/main.c
- [GitHub #6676](https://github.com/zephyrproject-rtos/zephyr/issues/6676) - [Coverity CID: 183056] Memory - corruptions in /tests/kernel/common/src/atomic.c
- [GitHub #6673](https://github.com/zephyrproject-rtos/zephyr/issues/6673) - [Coverity CID: 183059] Memory - corruptions in /samples/net/mbedtls\_dtlsclient/src/dtls\_client.c
- [GitHub #6593](https://github.com/zephyrproject-rtos/zephyr/issues/6593) - Allow configuring the USB serial number string in runtime
- [GitHub #6533](https://github.com/zephyrproject-rtos/zephyr/issues/6533) - 1.12 Release Checklist
- [GitHub #6522](https://github.com/zephyrproject-rtos/zephyr/issues/6522) - Should have a “dumb” O(N) scheduler
- [GitHub #6514](https://github.com/zephyrproject-rtos/zephyr/issues/6514) - samples/drivers/i2c\_fujitsu\_fram: Data comparison on data written and data read fails randomly
- [GitHub #6399](https://github.com/zephyrproject-rtos/zephyr/issues/6399) - How to using the PPI chanels from 20-31 in Nrf5 chip?
- [GitHub #6373](https://github.com/zephyrproject-rtos/zephyr/issues/6373) - ARMv8-M: Implement stack limit checking for Secure/Non-secure stack pointers
- [GitHub #6188](https://github.com/zephyrproject-rtos/zephyr/issues/6188) - doc: Merge non-apache contributing into CONTRIBUTING
- [GitHub #6132](https://github.com/zephyrproject-rtos/zephyr/issues/6132) - [RFC] Restructuring and cleanup of mbedTLS configurations
- [GitHub #5980](https://github.com/zephyrproject-rtos/zephyr/issues/5980) - NRF5 I2C standard speed 250kHz
- [GitHub #5939](https://github.com/zephyrproject-rtos/zephyr/issues/5939) - NRF5 I2C (TWI) driver
- [GitHub #5900](https://github.com/zephyrproject-rtos/zephyr/issues/5900) - net: Prototype a TLS convenience API based on sockets
- [GitHub #5896](https://github.com/zephyrproject-rtos/zephyr/issues/5896) - Accidentally using MSYS’s python from native windows leads to obscure error messages
- [GitHub #5833](https://github.com/zephyrproject-rtos/zephyr/issues/5833) - Script to import mcux sdk
- [GitHub #5733](https://github.com/zephyrproject-rtos/zephyr/issues/5733) - single threaded applications fail when asserts are enabled
- [GitHub #5732](https://github.com/zephyrproject-rtos/zephyr/issues/5732) - sanitycheck fails with gcc 7 as the host compiler
- [GitHub #5725](https://github.com/zephyrproject-rtos/zephyr/issues/5725) - Ninja: Running sanitycheck has byproducts outside of sanity-out
- [GitHub #5723](https://github.com/zephyrproject-rtos/zephyr/issues/5723) - cmake: Accept CONFIG\_XX overrides from command line
- [GitHub #5524](https://github.com/zephyrproject-rtos/zephyr/issues/5524) - reorg documentation structure on website (docs.zephyrproject.org)
- [GitHub #5445](https://github.com/zephyrproject-rtos/zephyr/issues/5445) - Shadowed declarations in bluetooth stack
- [GitHub #5371](https://github.com/zephyrproject-rtos/zephyr/issues/5371) - [Coverity CID: 180698] Null pointer dereferences in /tests/bluetooth/tester/src/gatt.c
- [GitHub #5366](https://github.com/zephyrproject-rtos/zephyr/issues/5366) - Document zephyr-app-commands usage
- [GitHub #5357](https://github.com/zephyrproject-rtos/zephyr/issues/5357) - CII Badge: Generate list of externally maintained dependencies
- [GitHub #5153](https://github.com/zephyrproject-rtos/zephyr/issues/5153) - [RFC] Discussion of “cmake” vs “make” variables, aka “build environment” vs “work environment” setup
- [GitHub #5132](https://github.com/zephyrproject-rtos/zephyr/issues/5132) - Soft real-time “tasklets” in kernel
- [GitHub #4963](https://github.com/zephyrproject-rtos/zephyr/issues/4963) - Convert NIOS2 boards to device tree
- [GitHub #4957](https://github.com/zephyrproject-rtos/zephyr/issues/4957) - Add build targets for each explicit debug/flash option
- [GitHub #4883](https://github.com/zephyrproject-rtos/zephyr/issues/4883) - Should command line examples be “cut and paste” ready?
- [GitHub #4829](https://github.com/zephyrproject-rtos/zephyr/issues/4829) - device tree: gpio
- [GitHub #4767](https://github.com/zephyrproject-rtos/zephyr/issues/4767) - USB: assign endpoints at runtime
- [GitHub #4762](https://github.com/zephyrproject-rtos/zephyr/issues/4762) - [nrf][power][Sample] nrf52 exits from Low Power Mode immedately
- [GitHub #4590](https://github.com/zephyrproject-rtos/zephyr/issues/4590) - [CID: 178238] Parse warnings in samples/mpu/mem\_domain\_apis\_test/src/main.c
- [GitHub #4283](https://github.com/zephyrproject-rtos/zephyr/issues/4283) - kconfig warning are being ignored by sanitycheck
- [GitHub #4060](https://github.com/zephyrproject-rtos/zephyr/issues/4060) - net: NET\_CONTEXT\_SYNC\_RECV relevant
- [GitHub #4047](https://github.com/zephyrproject-rtos/zephyr/issues/4047) - [nrf] nrf GPIO does not have sense configuration value
- [GitHub #4018](https://github.com/zephyrproject-rtos/zephyr/issues/4018) - zephyr.git/tests/net/mld/testcase.yaml#test :evalution failed
- [GitHub #3995](https://github.com/zephyrproject-rtos/zephyr/issues/3995) - net tcp retry triggers assert in kernel/sem.c:145
- [GitHub #3993](https://github.com/zephyrproject-rtos/zephyr/issues/3993) - Enabling Low Power Mode on nordic based platforms(nrf52/51)
- [GitHub #3980](https://github.com/zephyrproject-rtos/zephyr/issues/3980) - Remove adc\_enable/adc\_disable functions
- [GitHub #3947](https://github.com/zephyrproject-rtos/zephyr/issues/3947) - multiple build failures with XCC toolchain
- [GitHub #3935](https://github.com/zephyrproject-rtos/zephyr/issues/3935) - Bluetooth sample setup docs mentions unknown “btproxy” tool
- [GitHub #3903](https://github.com/zephyrproject-rtos/zephyr/issues/3903) - Static code scan (coverity) issues seen
- [GitHub #3845](https://github.com/zephyrproject-rtos/zephyr/issues/3845) - Enable Sphinx option doc\_role=’any’ for improved reference linking
- [GitHub #3826](https://github.com/zephyrproject-rtos/zephyr/issues/3826) - RISCV32 {\_\_irq\_wrapper} exception handling error under compressed instruction mode?
- [GitHub #3770](https://github.com/zephyrproject-rtos/zephyr/issues/3770) - mbedtls build error when CONFIG\_DEBUG=y
- [GitHub #3754](https://github.com/zephyrproject-rtos/zephyr/issues/3754) - Support static BT MAC address
- [GitHub #3666](https://github.com/zephyrproject-rtos/zephyr/issues/3666) - schedule\_api test uses zassert without cleaning up properly
- [GitHub #3631](https://github.com/zephyrproject-rtos/zephyr/issues/3631) - program text should be in its own memory region
- [GitHub #3602](https://github.com/zephyrproject-rtos/zephyr/issues/3602) - power\_mgr and power\_states: need build option to keep the app exiting in “active” state
- [GitHub #3583](https://github.com/zephyrproject-rtos/zephyr/issues/3583) - NUCLEO-L073RZ/NUCLEO-L053R8 Dev Board Support
- [GitHub #3458](https://github.com/zephyrproject-rtos/zephyr/issues/3458) - Port Zephyr to Silabs EFM32ZG-STK3200
- [GitHub #3395](https://github.com/zephyrproject-rtos/zephyr/issues/3395) - Provide a sample app that demonstrates VLANs
- [GitHub #3394](https://github.com/zephyrproject-rtos/zephyr/issues/3394) - Support basic VLAN tags
- [GitHub #3393](https://github.com/zephyrproject-rtos/zephyr/issues/3393) - VLAN: Expose through virtual network interfaces
- [GitHub #3377](https://github.com/zephyrproject-rtos/zephyr/issues/3377) - Missing le\_param\_updated callback when conn param update request fails
- [GitHub #3363](https://github.com/zephyrproject-rtos/zephyr/issues/3363) - Missing board documentation for nios2/qemu\_nois2
- [GitHub #3354](https://github.com/zephyrproject-rtos/zephyr/issues/3354) - Missing board documentation for x86/se\_c1000\_devboard
- [GitHub #3263](https://github.com/zephyrproject-rtos/zephyr/issues/3263) - improve Galileo flashing process
- [GitHub #3233](https://github.com/zephyrproject-rtos/zephyr/issues/3233) - LLDP Transmitting Agent
- [GitHub #3222](https://github.com/zephyrproject-rtos/zephyr/issues/3222) - No negative response if remote enabled encryption too soon
- [GitHub #3221](https://github.com/zephyrproject-rtos/zephyr/issues/3221) - re-pairing with no-bond legacy pairing results in using all zeros LTK
- [GitHub #3187](https://github.com/zephyrproject-rtos/zephyr/issues/3187) - frdm\_k64f: Ethernet networking starts to respond ~10s after boot
- [GitHub #3173](https://github.com/zephyrproject-rtos/zephyr/issues/3173) - k\_cpu\_atomic\_idle failed @ARM
- [GitHub #3150](https://github.com/zephyrproject-rtos/zephyr/issues/3150) - Si1153 Ambient Light Sensor, Proximity, and Gesture detector support
- [GitHub #3149](https://github.com/zephyrproject-rtos/zephyr/issues/3149) - Add support for ADXRS290
- [GitHub #3073](https://github.com/zephyrproject-rtos/zephyr/issues/3073) - Add Atmel SAM family DAC (DACC) driver
- [GitHub #3071](https://github.com/zephyrproject-rtos/zephyr/issues/3071) - Add Atmel SAM family Timer Counter (TC) driver
- [GitHub #3067](https://github.com/zephyrproject-rtos/zephyr/issues/3067) - Support Precision Time Protocol (PTP)
- [GitHub #3056](https://github.com/zephyrproject-rtos/zephyr/issues/3056) - arch-specific inline functions cannot manipulate \_kernel
- [GitHub #3025](https://github.com/zephyrproject-rtos/zephyr/issues/3025) - Implement \_tsc\_read equivalent for NiosII
- [GitHub #3024](https://github.com/zephyrproject-rtos/zephyr/issues/3024) - Implement \_tsc\_read equivalent for ARM
- [GitHub #3007](https://github.com/zephyrproject-rtos/zephyr/issues/3007) - Provide board documentation for all boards
- [GitHub #2991](https://github.com/zephyrproject-rtos/zephyr/issues/2991) - Enable NXP Cortex-M SoCs with MCUXpresso SDK
- [GitHub #2975](https://github.com/zephyrproject-rtos/zephyr/issues/2975) - add arc nSIM simulator build target
- [GitHub #2972](https://github.com/zephyrproject-rtos/zephyr/issues/2972) - extend sanitycheck to support ARC simulator
- [GitHub #2956](https://github.com/zephyrproject-rtos/zephyr/issues/2956) - I2C Slave Driver
- [GitHub #2954](https://github.com/zephyrproject-rtos/zephyr/issues/2954) - nRF5x interrupt-driven TX UART driver
- [GitHub #2952](https://github.com/zephyrproject-rtos/zephyr/issues/2952) - ADC: ADC fails to work when fetch multiple sequence entries
- [GitHub #2934](https://github.com/zephyrproject-rtos/zephyr/issues/2934) - Ecosystem and Tool Support
- [GitHub #2879](https://github.com/zephyrproject-rtos/zephyr/issues/2879) - ARC: Interrupt latency too large
- [GitHub #2645](https://github.com/zephyrproject-rtos/zephyr/issues/2645) - create DRAM\_BASE\_ADDRESS and SIZE config parameters
- [GitHub #2623](https://github.com/zephyrproject-rtos/zephyr/issues/2623) - nRF52 UART behaviour sensitive to timing of baud rate initialization.
- [GitHub #2568](https://github.com/zephyrproject-rtos/zephyr/issues/2568) - Have the kernel give the leftover memory to the IP stack
- [GitHub #2422](https://github.com/zephyrproject-rtos/zephyr/issues/2422) - O(1) pend queue support
- [GitHub #2353](https://github.com/zephyrproject-rtos/zephyr/issues/2353) - nRF5x: Refactor gpio\_nrf5.c to use the MDK headers
- [GitHub #1678](https://github.com/zephyrproject-rtos/zephyr/issues/1678) - support edge/pulse interrupts on ARC
- [GitHub #1662](https://github.com/zephyrproject-rtos/zephyr/issues/1662) - Problem sourcing the project environment file from zsh
- [GitHub #1600](https://github.com/zephyrproject-rtos/zephyr/issues/1600) - Could you give me BTP upper tester demo which can work on PC
- [GitHub #1464](https://github.com/zephyrproject-rtos/zephyr/issues/1464) - SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC is missing a default value
