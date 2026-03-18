---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/release-notes-1.10.html
original_path: releases/release-notes-1.10.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Zephyr Kernel 1.10.0

We are pleased to announce the release of Zephyr kernel version 1.10.0.

Major enhancements with this release include:

- Initial alpha-quality thread-level memory protection on x86, userspace and memory
  domains
- Major overhaul to the build system and a switch from Kbuild to CMake.
- Newtron Flash Filesystem (NFFS) Support
- Increased testsuite coverage and migrated majority of testcases to use ztest
- Integration with MCUBOOT Bootloader
- Additional SoC, platform and driver support for many of the already supported
  platforms.

The following sections provide detailed lists of changes by component.

## Kernel

- Remove deprecated k\_mem\_pool\_defrag code
- Initial alpha-quality thread-level memory protection on x86, userspace and memory
  domains:

  - Same kernel & driver APIs for kernel and user mode threads
  - System calls for privilege elevation
  - Stack overflow protection
  - Kernel object and device driver permission tracking
  - Simple app vs. kernel memory separation
  - Memory domain APIs for fine-tuning memory region permissions
  - Stack memory protection from other threads
- Add the following application-facing memory domain APIs:

  - k\_mem\_domain\_init() - to initialize a memory domain
  - k\_mem\_domain\_destroy() - to destroy a memory domain
  - k\_mem\_domain\_add\_partition() - to add a partition into a domain
  - k\_mem\_domain\_remove\_partition() - to remove a partition from a domain
  - k\_mem\_domain\_add\_thread() - to add a thread into a domain
  - k\_mem\_domain\_remove\_thread() - to remove a thread from a domain
- add k\_calloc() which uses kernel heap to implement traditional calloc()
  semantics.
- Introduce object validation mechanism: All system calls made from userspace,
  which involve pointers to kernel objects (including device drivers), will need
  to have those pointers validated; userspace must never be able to crash the
  kernel by passing it garbage.

## Architectures

- nrf52: Add support for LOW\_POWER state and SYSTEM\_OFF
- Architecture specific memory domain APIs added
- Tickless Kernel Implementation for Xtensa
- Added support for the following ARM SoCs:

  - NXP i.MX RT1052
  - Silabs EFM32WG
  - STM F0
  - TI MSP432P4xx

## Boards

- Jailhouse port: The port will enable Zephyr to run as a guest OS on x86-64
  systems. It comes with a test on QEMU to validate that, thus this new board
  introduction.
- Power Management for nrf52 series SOC
- Added support for the following ARM boards:

  - 96b\_neonkey
  - efm32wg\_stk3800
  - mimxrt1050\_evk
  - msp\_exp432p401r\_launchxl
  - nucleo\_f030r8
  - nucleo\_f091rc
  - stm32f411e\_disco
  - stm32f412g\_disco
  - stm32l476g\_disco
  - usb\_kw24d512

## Drivers and Sensors

- timer: Add Support for TICKLESS KERNEL in xtensa\_sys\_timer
- Rename `random` to `entropy`
- Add Atmel SAM I2S (SSC) driver
- Add Atmel SAM DMA (XDMAC) driver
- Add plantower PMS7003 Driver
- Add Altera shim driver for JTAG UART soft IP
- Add Altera shim driver for timer soft IP
- Introduce mcux ccm driver
- Introduce mcux igpio shim driver

## Networking

- HTTP API changed to use net-app API. Old HTTP API is deprecated.
- Loopback network interface support added. This is used in testing only.
- LWM2M multi-fragment network packet support added.
- New CoAP library implementation, supporting longer network packets.
- Deprecated ZoAP library.
- mDNS (multicast DNS) support added.
- SNTP (Simple Network Time Protocol) client library added.
- Various fixes for: TCP, RPL, ARP, DNS, LWM2M, Ethernet, net-app API, Network
  shell, and BSD socket API
- Network management API fixes.
- Networking sample application fixes.
- 6lo IPv6 header compression fixes.
- IEEE 802.15.4 generic fixes.
- IEEE 802.15.4 mcr20a driver fixes.
- IEEE 802.15.4 kw41z driver fixes.
- IEEE 802.15.4 nrf5 driver fixes.

## Bluetooth

- Multiple qualification-related fixes for Bluetooth Mesh
- Support for Bluetooth Mesh Friend Node role
- Support for Bluetooth Mesh Foundation Client Models
- New Bluetooth Mesh shell module and test application
- Support for PA/LNA amplifiers in the BLE Controller
- Support for additional VS commands in the BLE Controller
- Multiple stability fixes for the BLE Controller

## Build and Infrastructure

- The Zephyr project has migrated to CMake, an important step in a
  larger effort to make Zephyr easier to use for application developers
  working on different platforms with different development environment
  needs. This change retains Kconfig as-is, and replaces all Makefiles
  with corresponding CMakeLists.txt. The DSL-like Make language that
  KBuild offers is replaced by a set of CMake extensions that provide
  either simple one-to-one translations of KBuild features or introduce
  new concepts that replace KBuild concepts. Please re-read the Getting
  Started guide
  ([https://docs.zephyrproject.org/1.10.0/getting\_started/getting\_started.html](https://docs.zephyrproject.org/1.10.0/getting_started/getting_started.html))
  with updated instructions for setting up and developing on your host-OS.
  You *will* need to port your own out-of-tree scripts and Makefiles to
  CMake.

## Libraries / Subsystems

- The implementation for sys\_rand32\_get() function has been moved to a new
  “random” subsystem. There are new implementations for this function, one based
  in the Xoroshift128+ PRNG (using a hardware number generator to seed), and
  another that obtains random numbers directly from a hardware number generator
  driver. Hardware number generator drivers have been moved to a
  “drivers/entropy” directory; these drivers only expose the interface provided
  by include/entropy.h.
- TinyCrypt updated to version 0.2.8

## HALs

- Add Altera HAL for support NIOS-II boards
- Add mcux 2.3.0 for mimxrt1051 and mimxrt1052
- stm32cube: HAL/LL static library for stm32f0xx v.1.9.
- Add support for STM32 family USB driver
- Add Silabs Gecko SDK for EFM32WG SoCs
- Simplelink: Update cc32xx SDK to version 1.50.00.06

## Documentation

- Missing API documentation caused by doxygen subgroups and missing
  Sphinx directives now included.
- Note added to all released doc pages mentioning more current content could
  be available from the master branch version of the documentation.
- Documentation updated to use CMake (vs. Make) in all examples, and
  using a new Sphinx extension to keep examples consistent.
- Getting Started Guide material updated to include CMake dependencies
  and build instructions required for version 1.10.
- Instead of hiding all expected warnings from the document build
  process (there are some known doxygen/sphinx issues), the build
  now outputs all warnings, and then reports
  if any new/unexpected warnings or errors were detected.
- Obsolete V1 to V2 porting material removed.
- Continued updates to documentation for new board support, new samples,
  and new features.
- Integration of documentation with new zephyrproject.org website.
- Documentation moved to docs.zephyrproject.org site (with redirection
  from zephyrproject.org/doc)

## Tests and Samples

- Benchmarking: cleanup of the benchmarking code
- Add userspace protection tests
- Move all tests to ztest and cleanup coding style and formatting

## Issue Related Items

These GitHub issues were addressed since the previous 1.9.0 tagged
release:

- [GitHub #779](https://github.com/zephyrproject-rtos/zephyr/issues/779) - CI: shippable - provide some means to allow users to rebuild
- [GitHub #1166](https://github.com/zephyrproject-rtos/zephyr/issues/1166) - Keeping reusable components under samples/ leads to build issues
- [GitHub #1236](https://github.com/zephyrproject-rtos/zephyr/issues/1236) - Cleanup CONFIG\_EXECUTION\_BENCHMARKING
- [GitHub #1241](https://github.com/zephyrproject-rtos/zephyr/issues/1241) - tests/net/ipv6/ FAILED on qc1000:x86
- [GitHub #1242](https://github.com/zephyrproject-rtos/zephyr/issues/1242) - tests/kernel/mutex/mutex/ FAILED @ esp32
- [GitHub #1256](https://github.com/zephyrproject-rtos/zephyr/issues/1256) - [cmake] A board should support multiple configurations (variants)
- [GitHub #1270](https://github.com/zephyrproject-rtos/zephyr/issues/1270) - Issue : Information CC3220SF LaunchXL
- [GitHub #1280](https://github.com/zephyrproject-rtos/zephyr/issues/1280) - shell on Arduino Due prints “shell>” before the delayed boot banner
- [GitHub #1289](https://github.com/zephyrproject-rtos/zephyr/issues/1289) - C++ 11 support!
- [GitHub #1332](https://github.com/zephyrproject-rtos/zephyr/issues/1332) - sanitycheck builds too many duplicates in CI, make it smarter
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #1397](https://github.com/zephyrproject-rtos/zephyr/issues/1397) - no serialport output
- [GitHub #1415](https://github.com/zephyrproject-rtos/zephyr/issues/1415) - Problem with forcing new line in generated documentation.
- [GitHub #1416](https://github.com/zephyrproject-rtos/zephyr/issues/1416) - Regression added by commit cd35742a (net/ethernet/arp: Let ethernet L2 managing pkt’s reference while sending)
- [GitHub #1419](https://github.com/zephyrproject-rtos/zephyr/issues/1419) - test, please ignore
- [GitHub #1425](https://github.com/zephyrproject-rtos/zephyr/issues/1425) - spi.h and spi\_legacy.h documentation conflicts
- [GitHub #1428](https://github.com/zephyrproject-rtos/zephyr/issues/1428) - networking defines being used but not defined anywhere
- [GitHub #1435](https://github.com/zephyrproject-rtos/zephyr/issues/1435) - Could not connect to Eclipse Leshan Demo Server
- [GitHub #1445](https://github.com/zephyrproject-rtos/zephyr/issues/1445) - doc: groups of items in API documentation not displaying
- [GitHub #1450](https://github.com/zephyrproject-rtos/zephyr/issues/1450) - make kconfig help is difficult to understand
- [GitHub #1474](https://github.com/zephyrproject-rtos/zephyr/issues/1474) - tests/net/ipv6\_fragment build failure, missing testcase.yaml
- [GitHub #1487](https://github.com/zephyrproject-rtos/zephyr/issues/1487) - net/lib/dns doesn’t respect CONFIG\_NET\_IPV6=n
- [GitHub #1488](https://github.com/zephyrproject-rtos/zephyr/issues/1488) - Replacing Make/Kbuild with CMake
- [GitHub #1499](https://github.com/zephyrproject-rtos/zephyr/issues/1499) - doc: replace Mac OS with macOS
- [GitHub #1501](https://github.com/zephyrproject-rtos/zephyr/issues/1501) - doc: Fix link title
- [GitHub #1510](https://github.com/zephyrproject-rtos/zephyr/issues/1510) - “make debugserver” broken for qemu\_xtensa
- [GitHub #1522](https://github.com/zephyrproject-rtos/zephyr/issues/1522) - “make qemu” may not regenerate .config after changes to prj.conf
- [GitHub #1524](https://github.com/zephyrproject-rtos/zephyr/issues/1524) - doc: Remove “Changes from Version 1 Kernel” document
- [GitHub #1527](https://github.com/zephyrproject-rtos/zephyr/issues/1527) - make htmldocs failed
- [GitHub #1538](https://github.com/zephyrproject-rtos/zephyr/issues/1538) - esp32: is broken for the latest esp-idf version
- [GitHub #1542](https://github.com/zephyrproject-rtos/zephyr/issues/1542) - filter-known-issues.py fails if input file is empty
- [GitHub #1543](https://github.com/zephyrproject-rtos/zephyr/issues/1543) - doc: add process documentation for importing non-Apache2.0 licensed code
- [GitHub #1544](https://github.com/zephyrproject-rtos/zephyr/issues/1544) - regression: net: K64F: DHCP seems to fail a lot after 91041f9e
- [GitHub #1558](https://github.com/zephyrproject-rtos/zephyr/issues/1558) - Master reports itself as if it was 1.9.0 release
- [GitHub #1571](https://github.com/zephyrproject-rtos/zephyr/issues/1571) - Update to latest tinycrypt: v0.2.8
- [GitHub #1573](https://github.com/zephyrproject-rtos/zephyr/issues/1573) - tests/net/lib/http\_header\_fields/ fails with CONFIG\_HTTP\_PARSER\_STRICT enabled
- [GitHub #1580](https://github.com/zephyrproject-rtos/zephyr/issues/1580) - checkpatch output in shippable log displays without line breaks
- [GitHub #1581](https://github.com/zephyrproject-rtos/zephyr/issues/1581) - two tests fail in qemu\_cortex\_m3 with new SDK
- [GitHub #1597](https://github.com/zephyrproject-rtos/zephyr/issues/1597) - remove deprecated k\_mem\_pool\_defrag()
- [GitHub #1626](https://github.com/zephyrproject-rtos/zephyr/issues/1626) - Bluetooth LE dual mode topology
- [GitHub #1628](https://github.com/zephyrproject-rtos/zephyr/issues/1628) - Bluetooth LE data length extension
- [GitHub #1629](https://github.com/zephyrproject-rtos/zephyr/issues/1629) - LE privacy 1.2
- [GitHub #1630](https://github.com/zephyrproject-rtos/zephyr/issues/1630) - E2E tests for connection
- [GitHub #1632](https://github.com/zephyrproject-rtos/zephyr/issues/1632) - Implement Environmental Sensing Profile sample app
- [GitHub #1653](https://github.com/zephyrproject-rtos/zephyr/issues/1653) - enable stack canaries on ARC so we can run test\_stackprot
- [GitHub #1670](https://github.com/zephyrproject-rtos/zephyr/issues/1670) - Add Reject command handling
- [GitHub #1853](https://github.com/zephyrproject-rtos/zephyr/issues/1853) - Review all Kconfig variables used and Simplify
- [GitHub #1880](https://github.com/zephyrproject-rtos/zephyr/issues/1880) - Zephyr Build Management
- [GitHub #1883](https://github.com/zephyrproject-rtos/zephyr/issues/1883) - Audio Codec
- [GitHub #1885](https://github.com/zephyrproject-rtos/zephyr/issues/1885) - Display Interface
- [GitHub #1902](https://github.com/zephyrproject-rtos/zephyr/issues/1902) - uWeave
- [GitHub #2011](https://github.com/zephyrproject-rtos/zephyr/issues/2011) - tcf: add support for running altera\_max10 binaries
- [GitHub #2035](https://github.com/zephyrproject-rtos/zephyr/issues/2035) - doc: remove workaround for sphinx issue once 1.5 is released
- [GitHub #2202](https://github.com/zephyrproject-rtos/zephyr/issues/2202) - sporadic bad RAM pointer error under qemu\_nios2
- [GitHub #2277](https://github.com/zephyrproject-rtos/zephyr/issues/2277) - Update to a more recent version of micro-ecc in Zephyr
- [GitHub #2281](https://github.com/zephyrproject-rtos/zephyr/issues/2281) - purge usage of platform\_whitelist
- [GitHub #2411](https://github.com/zephyrproject-rtos/zephyr/issues/2411) - Look into supporting additional file systems under Zephyr FS API
- [GitHub #2580](https://github.com/zephyrproject-rtos/zephyr/issues/2580) - Failure in test\_nano\_work
- [GitHub #2723](https://github.com/zephyrproject-rtos/zephyr/issues/2723) - QEMU NIOS2 sporadic FAIL in tests/legacy/kernel/test\_context
- [GitHub #2775](https://github.com/zephyrproject-rtos/zephyr/issues/2775) - Ability to make Security / Vulnerability bugs non-public
- [GitHub #2793](https://github.com/zephyrproject-rtos/zephyr/issues/2793) - entropy subsystem
- [GitHub #2818](https://github.com/zephyrproject-rtos/zephyr/issues/2818) - Add disk access based on flash on freedom board to interface with file system
- [GitHub #2853](https://github.com/zephyrproject-rtos/zephyr/issues/2853) - Customer: Zephyr Tutorial
- [GitHub #2855](https://github.com/zephyrproject-rtos/zephyr/issues/2855) - Customer: Sample code
- [GitHub #2858](https://github.com/zephyrproject-rtos/zephyr/issues/2858) - Customer: Training / Webinar / Video
- [GitHub #2942](https://github.com/zephyrproject-rtos/zephyr/issues/2942) - Support for NXP KW2xD MCU
- [GitHub #3039](https://github.com/zephyrproject-rtos/zephyr/issues/3039) - Simple Network Time Protocol support
- [GitHub #3058](https://github.com/zephyrproject-rtos/zephyr/issues/3058) - no good way to include library code outside of $(PROJECT\_BASE)
- [GitHub #3064](https://github.com/zephyrproject-rtos/zephyr/issues/3064) - Symmetric multiprocessing (SMP)
- [GitHub #3070](https://github.com/zephyrproject-rtos/zephyr/issues/3070) - Add Atmel SAM family DMA (XDMAC) driver
- [GitHub #3139](https://github.com/zephyrproject-rtos/zephyr/issues/3139) - Zephyr Tutorials and Training
- [GitHub #3142](https://github.com/zephyrproject-rtos/zephyr/issues/3142) - [PTS] GAP/TC\_SEC\_AUT\_BV\_12\_C fails
- [GitHub #3143](https://github.com/zephyrproject-rtos/zephyr/issues/3143) - [PTS] GAP/TC\_SEC\_AUT\_BV\_14\_C fails
- [GitHub #3144](https://github.com/zephyrproject-rtos/zephyr/issues/3144) - [PTS] GAP/TC\_PRIV\_CONN\_BV\_11\_C fails
- [GitHub #3146](https://github.com/zephyrproject-rtos/zephyr/issues/3146) - [PTS] SM/SLA/PROT/BV-02-C fails
- [GitHub #3147](https://github.com/zephyrproject-rtos/zephyr/issues/3147) - [PTS] SM/SLA/SIE/BV-01-C fails
- [GitHub #3158](https://github.com/zephyrproject-rtos/zephyr/issues/3158) - Add support for Panther board based on Quark SE C1000
- [GitHub #3184](https://github.com/zephyrproject-rtos/zephyr/issues/3184) - xtensa: Zephyr SDK build and emulation support
- [GitHub #3201](https://github.com/zephyrproject-rtos/zephyr/issues/3201) - Add Device Tree Documentation
- [GitHub #3268](https://github.com/zephyrproject-rtos/zephyr/issues/3268) - Add tickless kernel support in xtensa\_sys\_timer timer
- [GitHub #3274](https://github.com/zephyrproject-rtos/zephyr/issues/3274) - Lauterbach Debug Tools Support
- [GitHub #3275](https://github.com/zephyrproject-rtos/zephyr/issues/3275) - Tickless Kernel and Frequency Scaling
- [GitHub #3290](https://github.com/zephyrproject-rtos/zephyr/issues/3290) - introduce shared metadata for boards, samples and tests
- [GitHub #3294](https://github.com/zephyrproject-rtos/zephyr/issues/3294) - Application Development
- [GitHub #3297](https://github.com/zephyrproject-rtos/zephyr/issues/3297) - ROM-able
- [GitHub #3313](https://github.com/zephyrproject-rtos/zephyr/issues/3313) - [RESEARCH] Memory Protection Unit support
- [GitHub #3353](https://github.com/zephyrproject-rtos/zephyr/issues/3353) - Missing board documentation for arm/quark\_se\_c1000\_ble
- [GitHub #3355](https://github.com/zephyrproject-rtos/zephyr/issues/3355) - Missing board documentation for arm/nucleo\_f103rb
- [GitHub #3357](https://github.com/zephyrproject-rtos/zephyr/issues/3357) - Missing board documentation for arm/stm32\_mini\_a15
- [GitHub #3360](https://github.com/zephyrproject-rtos/zephyr/issues/3360) - Missing board documentation for x86/panther
- [GitHub #3364](https://github.com/zephyrproject-rtos/zephyr/issues/3364) - Missing board documentation for arc/panther\_ss
- [GitHub #3368](https://github.com/zephyrproject-rtos/zephyr/issues/3368) - Can Zephyr support SNMP (Simple Network Management Protocol)?
- [GitHub #3378](https://github.com/zephyrproject-rtos/zephyr/issues/3378) - Zephyr will not build with icecream
- [GitHub #3383](https://github.com/zephyrproject-rtos/zephyr/issues/3383) - Work up linker-based system call prototype for MPU enabling
- [GitHub #3412](https://github.com/zephyrproject-rtos/zephyr/issues/3412) - Provide a sample application for kernel\_event\_logger
- [GitHub #3415](https://github.com/zephyrproject-rtos/zephyr/issues/3415) - Building FS for Arduino 101
- [GitHub #3432](https://github.com/zephyrproject-rtos/zephyr/issues/3432) - Port Zephyr to Silabs EFM32WG-STK3800
- [GitHub #3484](https://github.com/zephyrproject-rtos/zephyr/issues/3484) - Provide stm32cube LL based UART driver
- [GitHub #3485](https://github.com/zephyrproject-rtos/zephyr/issues/3485) - Provide stm32cube LL based I2C driver
- [GitHub #3486](https://github.com/zephyrproject-rtos/zephyr/issues/3486) - Provide stm32cube LL based SPI driver
- [GitHub #3587](https://github.com/zephyrproject-rtos/zephyr/issues/3587) - Move board related device tree files where the board is defined
- [GitHub #3588](https://github.com/zephyrproject-rtos/zephyr/issues/3588) - Move all X86 boards and related SoCs to device tree
- [GitHub #3600](https://github.com/zephyrproject-rtos/zephyr/issues/3600) - Build warnings [-Wpointer-sign] with LLVM/icx (tests/unit/bluetooth/at)
- [GitHub #3601](https://github.com/zephyrproject-rtos/zephyr/issues/3601) - Use QMSI mailbox driver for Quark SE
- [GitHub #3604](https://github.com/zephyrproject-rtos/zephyr/issues/3604) - the http\_client sample app cannot send GET request on Qemu x86
- [GitHub #3608](https://github.com/zephyrproject-rtos/zephyr/issues/3608) - Add functionality of Gesture Sensor
- [GitHub #3621](https://github.com/zephyrproject-rtos/zephyr/issues/3621) - Design system call interface for drivers
- [GitHub #3625](https://github.com/zephyrproject-rtos/zephyr/issues/3625) - Validation mechanism for user-supplied kernel object pointers
- [GitHub #3627](https://github.com/zephyrproject-rtos/zephyr/issues/3627) - x86: implement system calls
- [GitHub #3628](https://github.com/zephyrproject-rtos/zephyr/issues/3628) - implement APIs for dropping threads to unprivileged mode
- [GitHub #3630](https://github.com/zephyrproject-rtos/zephyr/issues/3630) - use API to validate user-supplied kernel buffers
- [GitHub #3632](https://github.com/zephyrproject-rtos/zephyr/issues/3632) - define set of architecture-specific memory protection APIs
- [GitHub #3635](https://github.com/zephyrproject-rtos/zephyr/issues/3635) - Device Driver Access Control
- [GitHub #3641](https://github.com/zephyrproject-rtos/zephyr/issues/3641) - define kernel system calls
- [GitHub #3643](https://github.com/zephyrproject-rtos/zephyr/issues/3643) - [PTS] PTS server stops working while executing TC\_SEC\_CSIGN\_BV\_01\_C test case
- [GitHub #3646](https://github.com/zephyrproject-rtos/zephyr/issues/3646) - Zoap message to use more than one fragment
- [GitHub #3682](https://github.com/zephyrproject-rtos/zephyr/issues/3682) - incremental builds do not work properly in Windows
- [GitHub #3683](https://github.com/zephyrproject-rtos/zephyr/issues/3683) - unable to follow directions to install Crosstool-NG on OS X
- [GitHub #3688](https://github.com/zephyrproject-rtos/zephyr/issues/3688) - OS X Setup Instructions Not Working on macOS Sierra
- [GitHub #3690](https://github.com/zephyrproject-rtos/zephyr/issues/3690) - Move to CMake or similar instead of Kbuild
- [GitHub #3697](https://github.com/zephyrproject-rtos/zephyr/issues/3697) - Use CMSIS \_\_NVIC\_PRIO\_BITS consistently
- [GitHub #3716](https://github.com/zephyrproject-rtos/zephyr/issues/3716) - define / implement application-facing memory domain APIs
- [GitHub #3728](https://github.com/zephyrproject-rtos/zephyr/issues/3728) - ESP32 i2c Driver Support
- [GitHub #3772](https://github.com/zephyrproject-rtos/zephyr/issues/3772) - test\_mem\_pool\_api crashes qemu\_x86 if CONFIG\_DEBUG=y
- [GitHub #3781](https://github.com/zephyrproject-rtos/zephyr/issues/3781) - iwdg: provide independent watchdog driver compliant with STM32Cube LL API
- [GitHub #3783](https://github.com/zephyrproject-rtos/zephyr/issues/3783) - Add mbedtls Crypto API shim driver
- [GitHub #3829](https://github.com/zephyrproject-rtos/zephyr/issues/3829) - PTS test case GATT/SR/GPA/BV-02-C crashes tester in QEMU
- [GitHub #3832](https://github.com/zephyrproject-rtos/zephyr/issues/3832) - ARM: implement API to validate user buffer
- [GitHub #3844](https://github.com/zephyrproject-rtos/zephyr/issues/3844) - Fix LWM2M header calculation in lwm2m\_engine.c
- [GitHub #3851](https://github.com/zephyrproject-rtos/zephyr/issues/3851) - Port SPI HCI driver on new SPI API
- [GitHub #3852](https://github.com/zephyrproject-rtos/zephyr/issues/3852) - x86: implement memory domain interface
- [GitHub #3892](https://github.com/zephyrproject-rtos/zephyr/issues/3892) - Add support for STM32F429I\_DISC1 board
- [GitHub #3897](https://github.com/zephyrproject-rtos/zephyr/issues/3897) - Static code scan (coverity) issues seen
- [GitHub #3922](https://github.com/zephyrproject-rtos/zephyr/issues/3922) - [PTS] GATT/SR/GAT/BV-01-C INCONC
- [GitHub #3923](https://github.com/zephyrproject-rtos/zephyr/issues/3923) - boards: provide support for Nucleo-64 F030R8
- [GitHub #3939](https://github.com/zephyrproject-rtos/zephyr/issues/3939) - Add Atmel SAM family I2S (Inter-IC Sound) driver based on SSC module
- [GitHub #3941](https://github.com/zephyrproject-rtos/zephyr/issues/3941) - x86: implement option for PAE-formatted page tables with NX bit
- [GitHub #3942](https://github.com/zephyrproject-rtos/zephyr/issues/3942) - x86: scope SMEP support in Zephyr
- [GitHub #3984](https://github.com/zephyrproject-rtos/zephyr/issues/3984) - Build warning: [-Wpointer-bool-conversion] with LLVM/icx (samples/bluetooth/mesh\_demo)
- [GitHub #3985](https://github.com/zephyrproject-rtos/zephyr/issues/3985) - Build warning: [-Wpointer-bool-conversion] with LLVM/icx (samples/bluetooth/mesh)
- [GitHub #4001](https://github.com/zephyrproject-rtos/zephyr/issues/4001) - GENERATED\_KERNEL\_OBJECT\_FILES end up in application memory
- [GitHub #4004](https://github.com/zephyrproject-rtos/zephyr/issues/4004) - integrate printk() with console subsystem
- [GitHub #4009](https://github.com/zephyrproject-rtos/zephyr/issues/4009) - I2C API is mixing two incompatible definitions of bit-fields
- [GitHub #4014](https://github.com/zephyrproject-rtos/zephyr/issues/4014) - memory protection: implicit kernel object permissions
- [GitHub #4016](https://github.com/zephyrproject-rtos/zephyr/issues/4016) - bluetooth linker not connected
- [GitHub #4022](https://github.com/zephyrproject-rtos/zephyr/issues/4022) - net: “queue: Use k\_poll if enabled” commit regressed BSD Sockets performance
- [GitHub #4026](https://github.com/zephyrproject-rtos/zephyr/issues/4026) - CC3220 WiFi Host Driver support
- [GitHub #4027](https://github.com/zephyrproject-rtos/zephyr/issues/4027) - extra unref happening on net\_context
- [GitHub #4029](https://github.com/zephyrproject-rtos/zephyr/issues/4029) - TinyTILE bluetooth app flash
- [GitHub #4030](https://github.com/zephyrproject-rtos/zephyr/issues/4030) - Coverity issue seen with CID: 175366 , in file: /subsys/bluetooth/host/smp.c
- [GitHub #4031](https://github.com/zephyrproject-rtos/zephyr/issues/4031) - Coverity issue seen with CID: 175365 , in file: /subsys/bluetooth/controller/hci/hci.c
- [GitHub #4032](https://github.com/zephyrproject-rtos/zephyr/issues/4032) - Coverity issue seen with CID: 175364 , in file: /subsys/bluetooth/host/mesh/proxy.c
- [GitHub #4033](https://github.com/zephyrproject-rtos/zephyr/issues/4033) - Coverity issue seen with CID: 175363 , in file: /subsys/bluetooth/host/smp.c
- [GitHub #4034](https://github.com/zephyrproject-rtos/zephyr/issues/4034) - Coverity issue seen with CID: 175362 , in file: /subsys/bluetooth/host/smp.c
- [GitHub #4035](https://github.com/zephyrproject-rtos/zephyr/issues/4035) - Coverity issue seen with CID: 175361 , in file: /samples/bluetooth/eddystone/src/main.c
- [GitHub #4036](https://github.com/zephyrproject-rtos/zephyr/issues/4036) - Coverity issue seen with CID: 175360 , in file: /subsys/bluetooth/host/mesh/prov.c
- [GitHub #4037](https://github.com/zephyrproject-rtos/zephyr/issues/4037) - Coverity issue seen with CID: 175359 , in file: /subsys/bluetooth/host/hci\_core.c
- [GitHub #4038](https://github.com/zephyrproject-rtos/zephyr/issues/4038) - Coverity issue seen with CID: 175358 , in file: /subsys/bluetooth/host/hci\_core.c
- [GitHub #4041](https://github.com/zephyrproject-rtos/zephyr/issues/4041) - flashing tinytile and use of minicom
- [GitHub #4043](https://github.com/zephyrproject-rtos/zephyr/issues/4043) - Add new user CONFIG to project
- [GitHub #4044](https://github.com/zephyrproject-rtos/zephyr/issues/4044) - Livelock in SMP pairing failed scenario
- [GitHub #4046](https://github.com/zephyrproject-rtos/zephyr/issues/4046) - BLE Central and BLE Peripheral roles at a moment on nRF52832
- [GitHub #4048](https://github.com/zephyrproject-rtos/zephyr/issues/4048) - HTTP Request Timeout Not Working
- [GitHub #4049](https://github.com/zephyrproject-rtos/zephyr/issues/4049) - AMP - Multi-core
- [GitHub #4050](https://github.com/zephyrproject-rtos/zephyr/issues/4050) - zephyr.git/tests/kernel/obj\_validation/testcase.yaml#test :Evaluation failure
- [GitHub #4051](https://github.com/zephyrproject-rtos/zephyr/issues/4051) - Coverity issue seen with CID: 177219 , in file: /drivers/flash/flash\_stm32f4x.c
- [GitHub #4054](https://github.com/zephyrproject-rtos/zephyr/issues/4054) - [CID: 177215 ], in file: /tests/subsys/dfu/mcuboot/src/main.c
- [GitHub #4055](https://github.com/zephyrproject-rtos/zephyr/issues/4055) - Coverity issue seen with CID: 177214 , in file: /samples/boards/microbit/pong/src/ble.c
- [GitHub #4056](https://github.com/zephyrproject-rtos/zephyr/issues/4056) - Coverity issue seen with CID: 177213 , in file: /tests/net/ipv6\_fragment/src/main.c
- [GitHub #4057](https://github.com/zephyrproject-rtos/zephyr/issues/4057) - Coverity issue seen with CID: 170744, in file: /samples/boards/microbit/pong/src/ble.c
- [GitHub #4058](https://github.com/zephyrproject-rtos/zephyr/issues/4058) - samples/net/http\_client: The HTTP client failed to send the GET request
- [GitHub #4059](https://github.com/zephyrproject-rtos/zephyr/issues/4059) - zephyr.git/tests/net/ipv6/testcase.yaml#test :evaluation failed
- [GitHub #4068](https://github.com/zephyrproject-rtos/zephyr/issues/4068) - [BLE, nRF51822] Error -ENOMEM when use bt\_gatt\_write\_without\_response function
- [GitHub #4099](https://github.com/zephyrproject-rtos/zephyr/issues/4099) - Add some docs to samples/net/ieee802154/hw
- [GitHub #4131](https://github.com/zephyrproject-rtos/zephyr/issues/4131) - gen\_syscalls.py may choke on non-ascii chars
- [GitHub #4135](https://github.com/zephyrproject-rtos/zephyr/issues/4135) - checkpatch.pl generates warning messages when run w/ perl-5.26
- [GitHub #4149](https://github.com/zephyrproject-rtos/zephyr/issues/4149) - Transition message on jira.zephyrproject.org needed
- [GitHub #4162](https://github.com/zephyrproject-rtos/zephyr/issues/4162) - build error in http\_get sample
- [GitHub #4165](https://github.com/zephyrproject-rtos/zephyr/issues/4165) - ieee802154\_uart\_pipe.c: warning: return from incompatible pointer type
- [GitHub #4182](https://github.com/zephyrproject-rtos/zephyr/issues/4182) - NET\_APP\_SETTINGS for 15.4 doesn’t seem to work (if to trust 15.4 shell)
- [GitHub #4186](https://github.com/zephyrproject-rtos/zephyr/issues/4186) - tcf.git/examples/test\_network\_linux\_zephyr.py#\_test :Compilation failure
- [GitHub #4188](https://github.com/zephyrproject-rtos/zephyr/issues/4188) - samples /net/echo\_server:failed to send packets to client
- [GitHub #4189](https://github.com/zephyrproject-rtos/zephyr/issues/4189) - ieee802154\_settings.c is duplicated in the codebase
- [GitHub #4190](https://github.com/zephyrproject-rtos/zephyr/issues/4190) - samples/net/echo\_client :failed to send data
- [GitHub #4193](https://github.com/zephyrproject-rtos/zephyr/issues/4193) - Zephyr libc(snprintf) is not comply with ISO standard.
- [GitHub #4195](https://github.com/zephyrproject-rtos/zephyr/issues/4195) - tests/net/udp/test\_udp.py#\_ipv4\_udp : evaluation failed
- [GitHub #4239](https://github.com/zephyrproject-rtos/zephyr/issues/4239) - unit tests broken in sanitycheck
- [GitHub #4249](https://github.com/zephyrproject-rtos/zephyr/issues/4249) - where is auto-pts py script of zephyr?
- [GitHub #4258](https://github.com/zephyrproject-rtos/zephyr/issues/4258) - samples/net/zoap\_server : unable to communicate between zoap client and server
- [GitHub #4264](https://github.com/zephyrproject-rtos/zephyr/issues/4264) - Getting started guide for windows: small error
- [GitHub #4289](https://github.com/zephyrproject-rtos/zephyr/issues/4289) - samples/mpu/mem\_domain\_apis\_test is broken
- [GitHub #4292](https://github.com/zephyrproject-rtos/zephyr/issues/4292) - net: tcp.c: prepare\_segment() may unrightly unref packet in case of error
- [GitHub #4295](https://github.com/zephyrproject-rtos/zephyr/issues/4295) - Error flashing board STM32373C-EVAL
- [GitHub #4301](https://github.com/zephyrproject-rtos/zephyr/issues/4301) - checkpatch.pl false positives block PR merge
- [GitHub #4310](https://github.com/zephyrproject-rtos/zephyr/issues/4310) - unable to flash quark\_se\_c1000\_devboard
- [GitHub #4312](https://github.com/zephyrproject-rtos/zephyr/issues/4312) - GDB: Ubuntu’s default GDB package does not support arm
- [GitHub #4323](https://github.com/zephyrproject-rtos/zephyr/issues/4323) - net: tcp.c: prepare\_segment() may leak fragments in case of error
- [GitHub #4325](https://github.com/zephyrproject-rtos/zephyr/issues/4325) - samples/net/http\_client: unable to send the proper http request to Apache server
- [GitHub #4327](https://github.com/zephyrproject-rtos/zephyr/issues/4327) - NET\_PKT\_TX\_SLAB\_DEFINE, NET\_PKT\_DATA\_POOL\_DEFINE description and usage are confusing
- [GitHub #4347](https://github.com/zephyrproject-rtos/zephyr/issues/4347) - net: BSD Sockets UDP sendto() impl broke tests/net/socket/udp/
- [GitHub #4353](https://github.com/zephyrproject-rtos/zephyr/issues/4353) - VM-VM qemu networking example crashes often
- [GitHub #4358](https://github.com/zephyrproject-rtos/zephyr/issues/4358) - k\_queue\_poll returns NULL with K\_FOREVER
- [GitHub #4366](https://github.com/zephyrproject-rtos/zephyr/issues/4366) - memory corruption in test\_pipe\_api
- [GitHub #4377](https://github.com/zephyrproject-rtos/zephyr/issues/4377) - Sniffing traffic in a VM-VM qemu setup crashes with a segfault in the monitor application
- [GitHub #4392](https://github.com/zephyrproject-rtos/zephyr/issues/4392) - zephyr/tests/benchmarks/footprint :build Failed
- [GitHub #4394](https://github.com/zephyrproject-rtos/zephyr/issues/4394) - Coverity issue seen with CID: 178058
- [GitHub #4395](https://github.com/zephyrproject-rtos/zephyr/issues/4395) - Coverity issue seen with CID: 178059
- [GitHub #4396](https://github.com/zephyrproject-rtos/zephyr/issues/4396) - Coverity issue seen with CID: 178060
- [GitHub #4397](https://github.com/zephyrproject-rtos/zephyr/issues/4397) - Coverity issue seen with CID: 178064
- [GitHub #4398](https://github.com/zephyrproject-rtos/zephyr/issues/4398) - zephyr/tests/crypto/ccm\_mode :-Evaluation failed due to esp32
- [GitHub #4419](https://github.com/zephyrproject-rtos/zephyr/issues/4419) - 6LoWPAN - source address uncompress corner case
- [GitHub #4421](https://github.com/zephyrproject-rtos/zephyr/issues/4421) - net: Duplicated functionality between net\_pkt\_get\_src\_addr() and net\_context.c:create\_sockaddr()
- [GitHub #4424](https://github.com/zephyrproject-rtos/zephyr/issues/4424) - Turning on network debug message w/ LwM2M sample client will result in stack check failure
- [GitHub #4429](https://github.com/zephyrproject-rtos/zephyr/issues/4429) - I2C: stm32-i2c-v2 Driver (F0/F3/F7) gets stuck in endless loop when handling restart conditions
- [GitHub #4442](https://github.com/zephyrproject-rtos/zephyr/issues/4442) - samples: net: ieee802154: Sample is not working on nRF52840 platform
- [GitHub #4459](https://github.com/zephyrproject-rtos/zephyr/issues/4459) - i2c: stm32-i2c-(v1/v2) don’t handle i2c\_burst\_write like expected
- [GitHub #4463](https://github.com/zephyrproject-rtos/zephyr/issues/4463) - Some tests and samples are missing a .yaml file
- [GitHub #4466](https://github.com/zephyrproject-rtos/zephyr/issues/4466) - warnings building echo\_client with nrf5
- [GitHub #4469](https://github.com/zephyrproject-rtos/zephyr/issues/4469) - CI problem with check-compliance.py
- [GitHub #4476](https://github.com/zephyrproject-rtos/zephyr/issues/4476) - Multiple build failures with i2c\_ll\_stm32.c driver
- [GitHub #4480](https://github.com/zephyrproject-rtos/zephyr/issues/4480) - Compilation failure for qemu\_x86 with CONFIG\_DEBUG\_INFO=y
- [GitHub #4481](https://github.com/zephyrproject-rtos/zephyr/issues/4481) - Build failure with CONFIG\_NET\_DEBUG\_APP=y
- [GitHub #4503](https://github.com/zephyrproject-rtos/zephyr/issues/4503) - CONFIG\_STACK\_SENTINEL inconsistencies
- [GitHub #4538](https://github.com/zephyrproject-rtos/zephyr/issues/4538) - Coverity issue seen with [CID:174928](CID:174928)
- [GitHub #4539](https://github.com/zephyrproject-rtos/zephyr/issues/4539) - Coverity issue seen with [CID:173658](CID:173658)
- [GitHub #4540](https://github.com/zephyrproject-rtos/zephyr/issues/4540) - Coverity issue seen with CID: 173657
- [GitHub #4541](https://github.com/zephyrproject-rtos/zephyr/issues/4541) - Coverity issue seen with CID: 173653
- [GitHub #4544](https://github.com/zephyrproject-rtos/zephyr/issues/4544) - [BLE Mesh] Error: Failed to advertise using Node ID
- [GitHub #4563](https://github.com/zephyrproject-rtos/zephyr/issues/4563) - [BLE Mesh]: How to handle the ‘Set” and ‘Get’ callbacks
- [GitHub #4565](https://github.com/zephyrproject-rtos/zephyr/issues/4565) - net\_context\_recv always fails with timeout=K\_FOREVER
- [GitHub #4567](https://github.com/zephyrproject-rtos/zephyr/issues/4567) - [BLE Mesh]: Multiple elements in a node
- [GitHub #4569](https://github.com/zephyrproject-rtos/zephyr/issues/4569) - LoRa: support LoRa
- [GitHub #4579](https://github.com/zephyrproject-rtos/zephyr/issues/4579) - [CID: 178249] Parse warnings in samples/mpu/mem\_domain\_apis\_test/src/main.c
- [GitHub #4580](https://github.com/zephyrproject-rtos/zephyr/issues/4580) - Coverity issue seen with CID: 178248
- [GitHub #4581](https://github.com/zephyrproject-rtos/zephyr/issues/4581) - Coverity issue seen with CID: 178247
- [GitHub #4582](https://github.com/zephyrproject-rtos/zephyr/issues/4582) - Coverity issue seen with CID: 178246
- [GitHub #4583](https://github.com/zephyrproject-rtos/zephyr/issues/4583) - [CID: 178245] Parse warnings in samples/mpu/mem\_domain\_apis\_test/src/main.c
- [GitHub #4584](https://github.com/zephyrproject-rtos/zephyr/issues/4584) - Coverity issue seen with CID: 178244
- [GitHub #4585](https://github.com/zephyrproject-rtos/zephyr/issues/4585) - Coverity issue seen with CID: 178243
- [GitHub #4586](https://github.com/zephyrproject-rtos/zephyr/issues/4586) - [CID: 178242]: Parse warnings samples/mpu/mem\_domain\_apis\_test/src/main.c
- [GitHub #4587](https://github.com/zephyrproject-rtos/zephyr/issues/4587) - Coverity issue seen with CID: 178241
- [GitHub #4588](https://github.com/zephyrproject-rtos/zephyr/issues/4588) - Coverity issue seen with CID: 178240
- [GitHub #4589](https://github.com/zephyrproject-rtos/zephyr/issues/4589) - [coverity] Null pointer dereferences in tests/net/app/src/main.c
- [GitHub #4591](https://github.com/zephyrproject-rtos/zephyr/issues/4591) - [CID: 178237] memory corruption in drivers/ieee802154/ieee802154\_mcr20a.c
- [GitHub #4592](https://github.com/zephyrproject-rtos/zephyr/issues/4592) - Coverity issue seen with CID: 178236
- [GitHub #4593](https://github.com/zephyrproject-rtos/zephyr/issues/4593) - Coverity issue seen with CID: 178235
- [GitHub #4594](https://github.com/zephyrproject-rtos/zephyr/issues/4594) - Coverity issue seen with CID: 178234
- [GitHub #4595](https://github.com/zephyrproject-rtos/zephyr/issues/4595) - Coverity issue seen with CID: 178233
- [GitHub #4600](https://github.com/zephyrproject-rtos/zephyr/issues/4600) - drivers:i2c\_ll\_stm32\_v2: Interrupt mode uses while loops
- [GitHub #4607](https://github.com/zephyrproject-rtos/zephyr/issues/4607) - tests/net/socket/udp/ is broken, again
- [GitHub #4630](https://github.com/zephyrproject-rtos/zephyr/issues/4630) - Sample app ‘coaps\_server’ fails to parse coap pkt
- [GitHub #4637](https://github.com/zephyrproject-rtos/zephyr/issues/4637) - [Coverity CID: 178334] Null pointer dereferences in /subsys/usb/class/netusb/function\_ecm.c
- [GitHub #4638](https://github.com/zephyrproject-rtos/zephyr/issues/4638) - build is failing when newlib is enabled
- [GitHub #4644](https://github.com/zephyrproject-rtos/zephyr/issues/4644) - Kconfig warnings when building any sample for nRF5x
- [GitHub #4652](https://github.com/zephyrproject-rtos/zephyr/issues/4652) - Document “make flash” in the “application development primer”
- [GitHub #4654](https://github.com/zephyrproject-rtos/zephyr/issues/4654) - Wrong file name for drivers/aio/aio\_comparator\_handlers.o
- [GitHub #4667](https://github.com/zephyrproject-rtos/zephyr/issues/4667) - x86 boards need device trees
- [GitHub #4668](https://github.com/zephyrproject-rtos/zephyr/issues/4668) - drivers/random/random\_handlers.c is built when no random driver has been kconfig’ed into the build
- [GitHub #4683](https://github.com/zephyrproject-rtos/zephyr/issues/4683) - net: tcp tcp\_retry\_expired cause assert
- [GitHub #4695](https://github.com/zephyrproject-rtos/zephyr/issues/4695) - samples/net/ieee802154 needs documentation
- [GitHub #4697](https://github.com/zephyrproject-rtos/zephyr/issues/4697) - [regression] net: echo\_server doesn’t accept IPv4 connections
- [GitHub #4738](https://github.com/zephyrproject-rtos/zephyr/issues/4738) - ble-mesh: proxy.c : Is clients-> conn a clerical error? it should be client-> conn?
- [GitHub #4744](https://github.com/zephyrproject-rtos/zephyr/issues/4744) - tests/net/ieee802154/l2/testcase.yaml#test : unable to acknowledge data from receiver
- [GitHub #4757](https://github.com/zephyrproject-rtos/zephyr/issues/4757) - kw41z-frdm: assertion failure while setting IRQ priority
- [GitHub #4759](https://github.com/zephyrproject-rtos/zephyr/issues/4759) - [PTS] GATT/CL/GAW/BV-02-C fails with INCONC
- [GitHub #4760](https://github.com/zephyrproject-rtos/zephyr/issues/4760) - stm32f4\_disco and frdm\_k64f samples/basic/blink\_led ,Choose supported PWM driver
- [GitHub #4766](https://github.com/zephyrproject-rtos/zephyr/issues/4766) - tests: mem\_pool: Fixed memory pool test case failure on quark d2000
- [GitHub #4780](https://github.com/zephyrproject-rtos/zephyr/issues/4780) - [Coverity CID: 178794] Error handling issues in /tests/subsys/dfu/mcuboot/src/main.c
- [GitHub #4781](https://github.com/zephyrproject-rtos/zephyr/issues/4781) - [Coverity CID: 178793] Incorrect expression in /tests/kernel/static\_idt/src/static\_idt.c
- [GitHub #4782](https://github.com/zephyrproject-rtos/zephyr/issues/4782) - [Coverity CID: 178792] Memory - illegal accesses in /subsys/net/lib/http/http\_app\_server.c
- [GitHub #4783](https://github.com/zephyrproject-rtos/zephyr/issues/4783) - [Coverity CID: 178791] Incorrect expression in /tests/kernel/static\_idt/src/static\_idt.c
- [GitHub #4784](https://github.com/zephyrproject-rtos/zephyr/issues/4784) - [Coverity CID: 178790] Memory - corruptions in /samples/net/http\_server/src/main.c
- [GitHub #4785](https://github.com/zephyrproject-rtos/zephyr/issues/4785) - [Coverity CID: 178789] Null pointer dereferences in /samples/net/http\_server/src/main.c
- [GitHub #4786](https://github.com/zephyrproject-rtos/zephyr/issues/4786) - [Coverity CID: 178788] Control flow issues in /tests/net/context/src/main.c
- [GitHub #4787](https://github.com/zephyrproject-rtos/zephyr/issues/4787) - [Coverity CID: 178787] Null pointer dereferences in /subsys/net/ip/net\_context.c
- [GitHub #4788](https://github.com/zephyrproject-rtos/zephyr/issues/4788) - [Coverity [CID:178786](CID:178786)] Memory - corruptions in /samples/net/http\_server/src/main.c
- [GitHub #4789](https://github.com/zephyrproject-rtos/zephyr/issues/4789) - [Coverity CID: 178785] Incorrect expression in /tests/kernel/static\_idt/src/static\_idt.c
- [GitHub #4791](https://github.com/zephyrproject-rtos/zephyr/issues/4791) - rpl-node uses testcase.ini instead of sample.yaml format
- [GitHub #4825](https://github.com/zephyrproject-rtos/zephyr/issues/4825) - Bluetooth IPSP error with qemu\_x86
- [GitHub #4827](https://github.com/zephyrproject-rtos/zephyr/issues/4827) - Ping command crashes kernel over qemu\_x86
- [GitHub #4841](https://github.com/zephyrproject-rtos/zephyr/issues/4841) - fix doc/devices/dts/device\_tree.rst path and Make references
- [GitHub #4844](https://github.com/zephyrproject-rtos/zephyr/issues/4844) - cmake: can’t flash stm32 with openocd
- [GitHub #4847](https://github.com/zephyrproject-rtos/zephyr/issues/4847) - custom 404 error page not being shown on docs.zephyrproject.org
- [GitHub #4853](https://github.com/zephyrproject-rtos/zephyr/issues/4853) - cmake: building unit test cases ignore EXTRA\_\* settings
- [GitHub #4864](https://github.com/zephyrproject-rtos/zephyr/issues/4864) - cmake: hts221 sensor sample not working anymore
- [GitHub #4881](https://github.com/zephyrproject-rtos/zephyr/issues/4881) - device\_get\_binding() returns failure in sample/drivers/crypto
- [GitHub #4889](https://github.com/zephyrproject-rtos/zephyr/issues/4889) - Flashing EM Starterkit with EM7D fails on master
- [GitHub #4899](https://github.com/zephyrproject-rtos/zephyr/issues/4899) - Convert opensda doc to CMake
- [GitHub #4901](https://github.com/zephyrproject-rtos/zephyr/issues/4901) - net: tcp: RST is sent after last ack is received
- [GitHub #4904](https://github.com/zephyrproject-rtos/zephyr/issues/4904) - cmake: BOOT\_BANNER disappeared
- [GitHub #4905](https://github.com/zephyrproject-rtos/zephyr/issues/4905) - cmake: flashing for quark\_se\_devboard is broken
- [GitHub #4910](https://github.com/zephyrproject-rtos/zephyr/issues/4910) - BT host CMakeLists.txt code should be agnostic to the FS implementation
- [GitHub #4912](https://github.com/zephyrproject-rtos/zephyr/issues/4912) - Not using the Zephyr SDK is broken
- [GitHub #4925](https://github.com/zephyrproject-rtos/zephyr/issues/4925) - application\_development test pollutes source directory
- [GitHub #4936](https://github.com/zephyrproject-rtos/zephyr/issues/4936) - net: 15.4 MAC addresses are shown differently between shell “net iface” and “ieee15\_4 get\_ext\_addr”
- [GitHub #4937](https://github.com/zephyrproject-rtos/zephyr/issues/4937) - ESP32 can’t boot
- [GitHub #4975](https://github.com/zephyrproject-rtos/zephyr/issues/4975) - Getting started documentation for Mac OS X inconsistent
- [GitHub #5004](https://github.com/zephyrproject-rtos/zephyr/issues/5004) - Normalize IEEE802514 driver “raw” mode.
- [GitHub #5008](https://github.com/zephyrproject-rtos/zephyr/issues/5008) - system call headers are not properly regenerated in CMake on incremental builds
- [GitHub #5009](https://github.com/zephyrproject-rtos/zephyr/issues/5009) - cmake creates too many build artifacts
- [GitHub #5014](https://github.com/zephyrproject-rtos/zephyr/issues/5014) - samples/drivers/crypto :Unable to find crypto device
- [GitHub #5019](https://github.com/zephyrproject-rtos/zephyr/issues/5019) - tests/kernel/mem\_protect/stackprot : input string is long stack overflow
- [GitHub #5025](https://github.com/zephyrproject-rtos/zephyr/issues/5025) - arduino\_due not generating proper config with cmake (crash)
- [GitHub #5026](https://github.com/zephyrproject-rtos/zephyr/issues/5026) - k\_poll() documentation is wrong
- [GitHub #5040](https://github.com/zephyrproject-rtos/zephyr/issues/5040) - Bluetooth mesh API documentation incomplete
- [GitHub #5047](https://github.com/zephyrproject-rtos/zephyr/issues/5047) - document error: getting\_started.rst
- [GitHub #5051](https://github.com/zephyrproject-rtos/zephyr/issues/5051) - Verify doxygen documented APIs are in the generated docs
- [GitHub #5055](https://github.com/zephyrproject-rtos/zephyr/issues/5055) - [Coverity CID: 179254] Possible Control flow issues in /samples/net/zperf/src/zperf\_udp\_receiver.c
- [GitHub #5056](https://github.com/zephyrproject-rtos/zephyr/issues/5056) - [Coverity CID: 179253] Control flow issues in /samples/net/zperf/src/zperf\_tcp\_receiver.c
- [GitHub #5057](https://github.com/zephyrproject-rtos/zephyr/issues/5057) - [Coverity CID: 179252] Null pointer dereferences in /samples/net/zperf/src/zperf\_udp\_receiver.c
- [GitHub #5058](https://github.com/zephyrproject-rtos/zephyr/issues/5058) - [Coverity CID: 179251] Control flow issues in /samples/net/zperf/src/zperf\_udp\_receiver.c
- [GitHub #5059](https://github.com/zephyrproject-rtos/zephyr/issues/5059) - [Coverity CID: 179250] Null pointer dereferences in /samples/net/zperf/src/zperf\_udp\_uploader.c
- [GitHub #5060](https://github.com/zephyrproject-rtos/zephyr/issues/5060) - [Coverity CID: 179249] Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #5061](https://github.com/zephyrproject-rtos/zephyr/issues/5061) - [Coverity CID: 179248] Control flow issues in /samples/net/zperf/src/zperf\_tcp\_receiver.c
- [GitHub #5062](https://github.com/zephyrproject-rtos/zephyr/issues/5062) - [Coverity CID: 179247] Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #5063](https://github.com/zephyrproject-rtos/zephyr/issues/5063) - samples/bluetooth: central\_hr sample app is not connecting with peripheral sample app on arduino\_101.
- [GitHub #5085](https://github.com/zephyrproject-rtos/zephyr/issues/5085) - bug: dts: stm32f1: wrong pinctrl base address
- [GitHub #5087](https://github.com/zephyrproject-rtos/zephyr/issues/5087) - Samples/bluetooth: Failed to connect with eddystone sample app on arduino\_101.
- [GitHub #5090](https://github.com/zephyrproject-rtos/zephyr/issues/5090) - no makefile in zephyr/samples/bluetooth/mesh examples
- [GitHub #5097](https://github.com/zephyrproject-rtos/zephyr/issues/5097) - zephyr\_library\_\*() configuration has lower precedence than global zephyr\_\*() configuration
- [GitHub #5107](https://github.com/zephyrproject-rtos/zephyr/issues/5107) - Default partition addressing for nrf52\_pca10040 is incompatible
- [GitHub #5116](https://github.com/zephyrproject-rtos/zephyr/issues/5116) - [Coverity CID: 179986] Null pointer dereferences in /subsys/bluetooth/host/mesh/access.c
- [GitHub #5117](https://github.com/zephyrproject-rtos/zephyr/issues/5117) - [Coverity CID: 179985] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5118](https://github.com/zephyrproject-rtos/zephyr/issues/5118) - [Coverity CID: 179984] Memory - corruptions in /drivers/ethernet/eth\_mcux.c
- [GitHub #5119](https://github.com/zephyrproject-rtos/zephyr/issues/5119) - [Coverity CID: 179983] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5120](https://github.com/zephyrproject-rtos/zephyr/issues/5120) - [Coverity CID: 179982] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5121](https://github.com/zephyrproject-rtos/zephyr/issues/5121) - [Coverity CID: 179981] Incorrect expression in /drivers/ieee802154/ieee802154\_kw41z.c
- [GitHub #5122](https://github.com/zephyrproject-rtos/zephyr/issues/5122) - [Coverity CID: 179980] Integer handling issues in /subsys/bluetooth/host/mesh/friend.c
- [GitHub #5123](https://github.com/zephyrproject-rtos/zephyr/issues/5123) - [Coverity CID: 179979] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5124](https://github.com/zephyrproject-rtos/zephyr/issues/5124) - [Coverity CID: 179978] Error handling issues in /subsys/bluetooth/host/mesh/health\_srv.c
- [GitHub #5125](https://github.com/zephyrproject-rtos/zephyr/issues/5125) - [Coverity CID: 179976] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5126](https://github.com/zephyrproject-rtos/zephyr/issues/5126) - [Coverity CID: 179975] Error handling issues in /subsys/bluetooth/host/mesh/health\_srv.c
- [GitHub #5127](https://github.com/zephyrproject-rtos/zephyr/issues/5127) - [Coverity CID: 179974] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5128](https://github.com/zephyrproject-rtos/zephyr/issues/5128) - [Coverity CID: 179973] Error handling issues in /subsys/bluetooth/host/mesh/cfg\_srv.c
- [GitHub #5140](https://github.com/zephyrproject-rtos/zephyr/issues/5140) - CMake migration regressed (changed behavior) of QEMU\_PTY=1
- [GitHub #5144](https://github.com/zephyrproject-rtos/zephyr/issues/5144) - BUG: cmake: make doesn’t update zephyr.hex file
- [GitHub #5145](https://github.com/zephyrproject-rtos/zephyr/issues/5145) - samples/bluetooth: Connection failure on peripheral CSC with Arduino 101
- [GitHub #5152](https://github.com/zephyrproject-rtos/zephyr/issues/5152) - CONFIG\_CPLUSPLUS is incompatible with the zephyr\_get\_\* API
- [GitHub #5159](https://github.com/zephyrproject-rtos/zephyr/issues/5159) - [nrf] Button example for nrf5x boards latches GPIO after 1 button press
- [GitHub #5176](https://github.com/zephyrproject-rtos/zephyr/issues/5176) - zephyr-v1.9.2 tag missing
- [GitHub #5177](https://github.com/zephyrproject-rtos/zephyr/issues/5177) - hci\_usb: Linking error
- [GitHub #5184](https://github.com/zephyrproject-rtos/zephyr/issues/5184) - kernel system call handlers missing due to -Wl,–no-whole-archive
- [GitHub #5186](https://github.com/zephyrproject-rtos/zephyr/issues/5186) - gen\_syscall\_header\_py is being run at the wrong time
- [GitHub #5189](https://github.com/zephyrproject-rtos/zephyr/issues/5189) - tests/subsys/fs/nffs\_fs\_api:-Evaluation failed
- [GitHub #5207](https://github.com/zephyrproject-rtos/zephyr/issues/5207) - Bluetooth subsystem uses acl\_in\_pool even for controllers not supporting flow control
- [GitHub #5211](https://github.com/zephyrproject-rtos/zephyr/issues/5211) - Kconfig: CPU\_HAS\_FPU dependencies problem
- [GitHub #5223](https://github.com/zephyrproject-rtos/zephyr/issues/5223) - CMake: Recent changes broke 3rd-party build system integration again
- [GitHub #5265](https://github.com/zephyrproject-rtos/zephyr/issues/5265) - ROM size increase due Zephyr compile options not stripping unused functions
- [GitHub #5266](https://github.com/zephyrproject-rtos/zephyr/issues/5266) - Ensure the Licensing page is up-to-date for the release
- [GitHub #5286](https://github.com/zephyrproject-rtos/zephyr/issues/5286) - NET\_L2: Symbols from the L2 implementation layer are exposed to users of L2
- [GitHub #5298](https://github.com/zephyrproject-rtos/zephyr/issues/5298) - Endless loop in uart pipe
