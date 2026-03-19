---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-1.11.html
original_path: releases/release-notes-1.11.html
---

# Zephyr Kernel 1.11.0

We are pleased to announce the release of Zephyr kernel version 1.11.0.

Major enhancements with this release include:

- Thread-level memory protection on x86, ARC and Arm, userspace and memory
  domains
- Symmetric Multi Processing (SMP) support on the Xtensa architecture.
- Initial Armv8-M architecture support.
- Native development environment on Microsoft Windows.
- Native build target on POSIX platforms.
- POSIX PSE52 partial support.
- Thread support via integration with OpenThread.
- Firmware over-the-air (FOTA) updates over BLE using MCUmgr.
- Lightweight flash storage layer for constrained devices.
- Additional SoC, platform and driver support for many of the already supported
  platforms.

The following sections provide detailed lists of changes by component.

## Kernel

- Initial Symmetric Multi Processing (SMP) support added:

  - SMP-aware scheduler
  - SMP timer and idling support
  - Available on the Xtensa architecture
- POSIX PSE52 support:

  - Timer, clock, scheduler and pthread APIs

## Architectures

- User space and system call related changes:

  - Added ARC user space implementation
  - Added Arm user space implementation
  - Fixed a few MPU related issues with stack guards
- Armv8-M initial architecture support, including the following cores:

  - Arm Cortex-M23
  - Arm Cortex-M33
- New POSIX architecture for native GNU/Linux and macOS build targets:

  - Targets native executables that can be run on the host operating system

## Boards

- New native\_posix board for the POSIX architecture:

  - Includes a template for hardware models
  - Adds support for console and logging
  - Interrupts and timers are simulated in several different configurations
- Added support for the following Arm boards:

  - adafruit\_trinket\_m0
  - arduino\_zero
  - lpcxpresso54114
  - nrf52\_sparkfun
  - nucleo\_f429zi
  - stm32f072\_eval
  - stm32f072b\_disco
- Removed Panther board support, which included boards/x86/panther and
  boards/arc/panther\_ss
- Refactored dts.fixup so common SoC-related fixes are in arch/<\*>/soc
  and board dts.fixup is only used for board-specific items.

## Drivers and Sensors

- New LED PWM driver for ESP32 SoC
- Fixed ESP32 I2C driver
- Added I2C master, QSPI flash, and GPIO drivers for nios-II
- Added PinMux, GPIO, serial drivers for LPC54114
- Added PinMux, GPIO, serial, SPI, and watchdog drivers for sam0
- Added APA102 and WS2821B led\_strip drivers
- Added native entropy driver
- Moved some sensors to dts
- Added AMG88xx, CCS811, and VL53L0x sensor drivers
- Redefined SENSOR\_CHAN\_HUMIDITY in percent

## Networking

- Generic OpenThread support added
- OpenThread support to nRF5 IEEE 802.15.4 driver added
- NXP MCUX ethernet driver IPv6 multicast join/leave enhancements
- Ethernet STM32 fixes
- IEEE 802.15.4 Sub-GHz TI CC1200 chip support added
- IEEE 802.15.4 test driver (upipe) hw filtering support added
- IEEE 802.15.4 radio API enhancements
- Net loopback driver fixes
- Net management API event enhancements
- IPv6 neighbor addition and removal can be monitored
- Static IPv4 and DHCPv4 configuration enhancements
- Bluetooth IPSP disconnect fix
- Network buffer enhancements
- ICMPv4 and ICMPv6 error checking fixes
- Network interface address handling enhancements
- Add routing support between network interfaces
- LWM2M fixes and enhancements
- Old legacy HTTP API removed
- Old legacy ZoAP API removed
- CoAP fixes
- TCP fixes
- HTTP fixes
- RPL fixes
- Net-app API fixes
- Net-shell fixes
- BSD socket API fixes

## Bluetooth

- Multiple fixes to the controller
- Fixed potential connection transmission deadlock issue with the help
  of a dedicated fragment pool
- Multiple fixes to Mesh support
- Added test automation for Mesh (for tests/bluetooth/tester)

## Build and Infrastructure

- Native development environment on Microsoft Windows:

  - Uses CMake and Kconfiglib to avoid requiring an emulation layer
  - Package management support with Chocolatey for simple setup
  - Build time now comparable to Linux and macOS using Ninja

## Libraries / Subsystems

- New management subsystem based on the cross-RTOS MCUmgr:

  - Secure Firmware Updates over BLE and serial
  - Support for file system access and statistics
  - mcumgr cross-platform command-line tool
- FCB (File Circular Buffer) lightweight storage layer:

  - Wear-leveling support for NOR flashes
  - Suitable for memory constrained devices

## HALs

- Updated Arm CMSIS from version 4.5.0 to 5.2.0
- Updated stm32cube stm32l4xx from version 1.9.0 to 1.10.0
- Updated stm32cube stm32f4xx from version 1.16.0 to 1.18.0
- Added Atmel SAMD21 HAL
- Added mcux 2.2.1 for LPC54114
- Added HAL for VL53L0x sensor from STM
- Imported and moved to nRFx 0.8.0 on Nordic SoCs
- Added QSPI Controller HAL driver

## Documentation

- Added MPU specific stack and userspace documentation
- Improved docs for Native (POSIX) support
- Docs for new samples and supported board
- General documentation clarifications and improvements
- Identify daily-built master-branch docs as “Latest” version
- Addressed Sphinx-generated intra-page link issues
- Updated doc generation tools (Doxygen, Sphinx, Breathe, Docutils)

## Tests and Samples

- Added additional tests and test improvements for user space testing

## Issue Related Items

These GitHub issues were addressed since the previous 1.10.0 tagged
release:

- [GitHub #1082](https://github.com/zephyrproject-rtos/zephyr/issues/1082) - build all tests have issues for devices that don’t exist on a given board
- [GitHub #1281](https://github.com/zephyrproject-rtos/zephyr/issues/1281) - spi\_ll\_stm32 driver does not support stm32f1soc
- [GitHub #1291](https://github.com/zephyrproject-rtos/zephyr/issues/1291) - Initial Posix PSE52 Support
- [GitHub #1460](https://github.com/zephyrproject-rtos/zephyr/issues/1460) - 1.10 Release Checklist
- [GitHub #1462](https://github.com/zephyrproject-rtos/zephyr/issues/1462) - rename nano\_internal.h to kernel\_internal.h
- [GitHub #1526](https://github.com/zephyrproject-rtos/zephyr/issues/1526) - Bluetooth:mesh:prov\_start: Invalid authentication
- [GitHub #1532](https://github.com/zephyrproject-rtos/zephyr/issues/1532) - There are no RISC-V boards in the list of supported boards
- [GitHub #1727](https://github.com/zephyrproject-rtos/zephyr/issues/1727) - Support out-of-tree board definitions
- [GitHub #1793](https://github.com/zephyrproject-rtos/zephyr/issues/1793) - I2S device APIs and Drivers
- [GitHub #1868](https://github.com/zephyrproject-rtos/zephyr/issues/1868) - Build System cleanup and Kernel / Application build separation
- [GitHub #1877](https://github.com/zephyrproject-rtos/zephyr/issues/1877) - Provide single point of notification for new data on multiple sockets.
- [GitHub #1890](https://github.com/zephyrproject-rtos/zephyr/issues/1890) - Memory Management
- [GitHub #1891](https://github.com/zephyrproject-rtos/zephyr/issues/1891) - Native Port
- [GitHub #1892](https://github.com/zephyrproject-rtos/zephyr/issues/1892) - NFC Stack
- [GitHub #1893](https://github.com/zephyrproject-rtos/zephyr/issues/1893) - Unified Kernel
- [GitHub #1921](https://github.com/zephyrproject-rtos/zephyr/issues/1921) - Bluetooth LE 4.2 Hardware Support
- [GitHub #1926](https://github.com/zephyrproject-rtos/zephyr/issues/1926) - build system does not re-link if linker script changed
- [GitHub #1930](https://github.com/zephyrproject-rtos/zephyr/issues/1930) - bluetooth tester shall support logging on Arduino101
- [GitHub #2007](https://github.com/zephyrproject-rtos/zephyr/issues/2007) - C++ compiler flags are not managed correctly
- [GitHub #2072](https://github.com/zephyrproject-rtos/zephyr/issues/2072) - create abstraction layer to directly use Altera HAL drivers for Nios II IP blocks
- [GitHub #2107](https://github.com/zephyrproject-rtos/zephyr/issues/2107) - handle configuration changes with more code coverage
- [GitHub #2239](https://github.com/zephyrproject-rtos/zephyr/issues/2239) - sporadic illegal instruction exception on Nios II in test\_errno
- [GitHub #2244](https://github.com/zephyrproject-rtos/zephyr/issues/2244) - LE Controller: remove util folder
- [GitHub #2280](https://github.com/zephyrproject-rtos/zephyr/issues/2280) - Move defaults.tc and .known-issue under tests/
- [GitHub #2347](https://github.com/zephyrproject-rtos/zephyr/issues/2347) - Thread Protocol v1.1 Dependencies on the IP Stack
- [GitHub #2365](https://github.com/zephyrproject-rtos/zephyr/issues/2365) - Port IOT Protocols to the new IP Stack
- [GitHub #2477](https://github.com/zephyrproject-rtos/zephyr/issues/2477) - no unit tests exist for CONFIG\_DEBUG\_INFO
- [GitHub #2620](https://github.com/zephyrproject-rtos/zephyr/issues/2620) - object files created outside of $O directory when obj-XYZ path is relative
- [GitHub #2722](https://github.com/zephyrproject-rtos/zephyr/issues/2722) - QEMU NIOS2 sporadic FAIL in tests/legacy/kernel/test\_timer/nanokernel
- [GitHub #2760](https://github.com/zephyrproject-rtos/zephyr/issues/2760) - Implement Virtual USB ethernet Adapter support
- [GitHub #2819](https://github.com/zephyrproject-rtos/zephyr/issues/2819) - legacy/kernel/test\_task\_priv randomly fails on EMSK ARC
- [GitHub #2889](https://github.com/zephyrproject-rtos/zephyr/issues/2889) - [ARC] legacy/benchmark/latency\_measure not measuring RIRQ/FIRQ
- [GitHub #2891](https://github.com/zephyrproject-rtos/zephyr/issues/2891) - implement \_tsc\_read equivalent for all architectures
- [GitHub #2912](https://github.com/zephyrproject-rtos/zephyr/issues/2912) - Develop Guideline for Handling Configuration Changes with More Code Coverage
- [GitHub #2937](https://github.com/zephyrproject-rtos/zephyr/issues/2937) - Thread-level Memory Protection Support
- [GitHub #2939](https://github.com/zephyrproject-rtos/zephyr/issues/2939) - Add Xtensa Port
- [GitHub #2943](https://github.com/zephyrproject-rtos/zephyr/issues/2943) - Support for the KW22D512 Kinetis MCU based USB Dongle
- [GitHub #2971](https://github.com/zephyrproject-rtos/zephyr/issues/2971) - I2C High-Speed Mode is not implemented
- [GitHub #2994](https://github.com/zephyrproject-rtos/zephyr/issues/2994) - The build system crashes when GCCARMEMB\_TOOLCHAIN\_PATH has a space in it
- [GitHub #3069](https://github.com/zephyrproject-rtos/zephyr/issues/3069) - XML encoding/decoding library
- [GitHub #3081](https://github.com/zephyrproject-rtos/zephyr/issues/3081) - Concise Binary Object Representation (CBOR)
- [GitHub #3083](https://github.com/zephyrproject-rtos/zephyr/issues/3083) - I2C problem Zephyr OS sensor example on NRF51 and F401re
- [GitHub #3127](https://github.com/zephyrproject-rtos/zephyr/issues/3127) - IP stack does not implement multicasting requirements of IPv6 RFCs and network driver model lacks features to implement it properly
- [GitHub #3240](https://github.com/zephyrproject-rtos/zephyr/issues/3240) - Unnecessary code footprint bloat due to “static inline”
- [GitHub #3279](https://github.com/zephyrproject-rtos/zephyr/issues/3279) - Reclaiming Memory
- [GitHub #3283](https://github.com/zephyrproject-rtos/zephyr/issues/3283) - Split net\_buf parsing context from the actual data
- [GitHub #3302](https://github.com/zephyrproject-rtos/zephyr/issues/3302) - samples/subsys/logging/logger-hook needs to be a test case
- [GitHub #3308](https://github.com/zephyrproject-rtos/zephyr/issues/3308) - [TAHI] No “ICMPv6 error message” is received while sending echo request with parameter problem header
- [GitHub #3316](https://github.com/zephyrproject-rtos/zephyr/issues/3316) - [IPv6 TAHI] Section 1: RFC 2460 - IPv6 Specification
- [GitHub #3317](https://github.com/zephyrproject-rtos/zephyr/issues/3317) - [IPv6 TAHI]Section 4: RFC 1981 - Path MTU Discovery for IPv6
- [GitHub #3318](https://github.com/zephyrproject-rtos/zephyr/issues/3318) - [IPv6 TAHI]Section 5: RFC 4443 - ICMPv6
- [GitHub #3322](https://github.com/zephyrproject-rtos/zephyr/issues/3322) - [IPv6 TAHI] Section 3: RFC 4862 - IPv6 Stateless Address Autoconfiguration
- [GitHub #3323](https://github.com/zephyrproject-rtos/zephyr/issues/3323) - [IPv6 TAHI] Section 2: RFC 4861 - Neighbor Discovery for IPv6
- [GitHub #3329](https://github.com/zephyrproject-rtos/zephyr/issues/3329) - Build warnings [-Wpointer-sign] with LLVM/icx (bluetooth\_ipsp)
- [GitHub #3345](https://github.com/zephyrproject-rtos/zephyr/issues/3345) - Missing board documentation for riscv32/zedboard\_pulpino
- [GitHub #3346](https://github.com/zephyrproject-rtos/zephyr/issues/3346) - Missing board documentation for riscv32/qemu\_riscv32
- [GitHub #3351](https://github.com/zephyrproject-rtos/zephyr/issues/3351) - Missing board documentation for arm/bbc\_microbit board
- [GitHub #3352](https://github.com/zephyrproject-rtos/zephyr/issues/3352) - Missing board documentation for arm/nrf51\_blenano
- [GitHub #3439](https://github.com/zephyrproject-rtos/zephyr/issues/3439) - IP stack: No MTU handling on send()
- [GitHub #3440](https://github.com/zephyrproject-rtos/zephyr/issues/3440) - IP stack: No TCP receive window handling
- [GitHub #3483](https://github.com/zephyrproject-rtos/zephyr/issues/3483) - Unify STM32 configuration files
- [GitHub #3546](https://github.com/zephyrproject-rtos/zephyr/issues/3546) - Enabling networking for targets w/o network hw causes hang on boot
- [GitHub #3565](https://github.com/zephyrproject-rtos/zephyr/issues/3565) - Symmetric multiprocessing (SMP) for Xtensa architecture
- [GitHub #3597](https://github.com/zephyrproject-rtos/zephyr/issues/3597) - Build warnings [-Wpointer-sign] with LLVM/icx (tests/net/ieee802154/crypto)
- [GitHub #3614](https://github.com/zephyrproject-rtos/zephyr/issues/3614) - cdc-acm error when printing one byte at a time
- [GitHub #3617](https://github.com/zephyrproject-rtos/zephyr/issues/3617) - Build warnings [-Wshift-overflow] with LLVM/icx (K\_MEM\_POOL\_DEFINE)
- [GitHub #3667](https://github.com/zephyrproject-rtos/zephyr/issues/3667) - \_IsInIsr doesn’t work properly on Cortex M0
- [GitHub #3685](https://github.com/zephyrproject-rtos/zephyr/issues/3685) - Test suite cleanup and Test Coverage
- [GitHub #3704](https://github.com/zephyrproject-rtos/zephyr/issues/3704) - Move all X86 boards to device tree
- [GitHub #3707](https://github.com/zephyrproject-rtos/zephyr/issues/3707) - intermittent work\_queue test failure
- [GitHub #3712](https://github.com/zephyrproject-rtos/zephyr/issues/3712) - RPL client node version bogus incrementation
- [GitHub #3718](https://github.com/zephyrproject-rtos/zephyr/issues/3718) - Mpu stack guard is not set when reaching main
- [GitHub #3747](https://github.com/zephyrproject-rtos/zephyr/issues/3747) - tests/kernel/mem\_slab/test\_mslab\_threadsafe/testcase.ini#test type:qemu-zephyr-arm
- [GitHub #3809](https://github.com/zephyrproject-rtos/zephyr/issues/3809) - Build warnings [-Wimplicit-function-declaration] with LLVM/icx (tests/drivers/pci\_enum)
- [GitHub #3833](https://github.com/zephyrproject-rtos/zephyr/issues/3833) - make device\_get\_binding() more efficient
- [GitHub #3834](https://github.com/zephyrproject-rtos/zephyr/issues/3834) - CDC\_ACM is limited to 4 bytes at a time for Arduino 101
- [GitHub #3838](https://github.com/zephyrproject-rtos/zephyr/issues/3838) - Some tests end up with 0 platforms due to bad filtering
- [GitHub #3850](https://github.com/zephyrproject-rtos/zephyr/issues/3850) - SPI fails on Nucleo\_f334r8
- [GitHub #3855](https://github.com/zephyrproject-rtos/zephyr/issues/3855) - Support board files located in application directory
- [GitHub #3856](https://github.com/zephyrproject-rtos/zephyr/issues/3856) - LwM2M: Support write attributes (section 5.4.4 of spec)
- [GitHub #3858](https://github.com/zephyrproject-rtos/zephyr/issues/3858) - Enable OpenThread support for Zephyr
- [GitHub #3859](https://github.com/zephyrproject-rtos/zephyr/issues/3859) - Create OpenThread platform adaptation for Zephyr
- [GitHub #3860](https://github.com/zephyrproject-rtos/zephyr/issues/3860) - Create OpenThread network interface driver
- [GitHub #3862](https://github.com/zephyrproject-rtos/zephyr/issues/3862) - Verify that the OpenThread requirements are fulfilled by Zephyr 15.4 radio driver
- [GitHub #3870](https://github.com/zephyrproject-rtos/zephyr/issues/3870) - Create a shell to configure OpenThread stack
- [GitHub #3872](https://github.com/zephyrproject-rtos/zephyr/issues/3872) - build on windows failed “ error: unrecognized command line option ‘-no-pie’”
- [GitHub #3918](https://github.com/zephyrproject-rtos/zephyr/issues/3918) - Build error [use of undeclared identifier]with LLVM/icx (samples/net/nats)
- [GitHub #4000](https://github.com/zephyrproject-rtos/zephyr/issues/4000) - xtensa-vectors.S builds wrong versions of ISRs based on HAL information
- [GitHub #4010](https://github.com/zephyrproject-rtos/zephyr/issues/4010) - [CID: 174928]: Control flow issues in /tests/kernel/mem\_slab/mslab/src/slab.c
- [GitHub #4025](https://github.com/zephyrproject-rtos/zephyr/issues/4025) - Upgrade to TinyCrypt 0.2.7 has significant API changes
- [GitHub #4045](https://github.com/zephyrproject-rtos/zephyr/issues/4045) - convert to ztest for files in tests/kernel
- [GitHub #4105](https://github.com/zephyrproject-rtos/zephyr/issues/4105) - Sensors: move all the drivers using SPI bus to new SPI API
- [GitHub #4106](https://github.com/zephyrproject-rtos/zephyr/issues/4106) - Flash: move w25qxxdv driver to new SPI API
- [GitHub #4216](https://github.com/zephyrproject-rtos/zephyr/issues/4216) - samples:net:sockets:echo : communication blocks between client and server after few packets transmission
- [GitHub #4351](https://github.com/zephyrproject-rtos/zephyr/issues/4351) - arduino\_101: USB device is not listed after flashing with a Zephyr sample
- [GitHub #4401](https://github.com/zephyrproject-rtos/zephyr/issues/4401) - tests/net/ipv6/test.yaml :–Cannot add multicast IPv6 address
- [GitHub #4445](https://github.com/zephyrproject-rtos/zephyr/issues/4445) - sanitycheck –platform-limit is broken
- [GitHub #4513](https://github.com/zephyrproject-rtos/zephyr/issues/4513) - parsetab.py is getting corrupted when multiple instance of sanitycheck is executed simultaneously
- [GitHub #4549](https://github.com/zephyrproject-rtos/zephyr/issues/4549) - tests/crypto/mbedtls/testcase.yaml#test :Build failed
- [GitHub #4566](https://github.com/zephyrproject-rtos/zephyr/issues/4566) - k\_busy\_wait( ) gives compilation error when CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC is set to 0
- [GitHub #4568](https://github.com/zephyrproject-rtos/zephyr/issues/4568) - dts generation incorrect
- [GitHub #4576](https://github.com/zephyrproject-rtos/zephyr/issues/4576) - no testcase.yaml for tests/drivers/spi/spi\_loopback
- [GitHub #4578](https://github.com/zephyrproject-rtos/zephyr/issues/4578) - tests/net/socket/udp/testcase.yaml#test : Build failed on esp32
- [GitHub #4596](https://github.com/zephyrproject-rtos/zephyr/issues/4596) - tests/net/mgmt/testcase.yaml#test :failed due to un-handled exception
- [GitHub #4597](https://github.com/zephyrproject-rtos/zephyr/issues/4597) - tests/drivers/ipm/testcase.yaml#test :unable to print the Expected output
- [GitHub #4603](https://github.com/zephyrproject-rtos/zephyr/issues/4603) - sanitycheck either conceals information from user or spams it
- [GitHub #4606](https://github.com/zephyrproject-rtos/zephyr/issues/4606) - usb mass storage : config waits for Vendor ID and Product ID from user during building
- [GitHub #4633](https://github.com/zephyrproject-rtos/zephyr/issues/4633) - Implement flash page layout api in the Kinetis flash driver
- [GitHub #4635](https://github.com/zephyrproject-rtos/zephyr/issues/4635) - xtensa-esp32-elf-gcc.exe: error: unrecognized command line option ‘-no-pie’
- [GitHub #4653](https://github.com/zephyrproject-rtos/zephyr/issues/4653) - net: tcp->recv\_max\_ack isn’t used
- [GitHub #4666](https://github.com/zephyrproject-rtos/zephyr/issues/4666) - x86 device trees need interrupt controller nodes
- [GitHub #4687](https://github.com/zephyrproject-rtos/zephyr/issues/4687) - Windows: Remove all dependencies on MSYS2
- [GitHub #4699](https://github.com/zephyrproject-rtos/zephyr/issues/4699) - PWM LED Driver for ESP32
- [GitHub #4705](https://github.com/zephyrproject-rtos/zephyr/issues/4705) - tests/net/socket/tcp/ undefined reference to \_\_getreent
- [GitHub #4709](https://github.com/zephyrproject-rtos/zephyr/issues/4709) - tests/kernel/fatal/testcase.yaml#stack-sentinel : Kernel Panic
- [GitHub #4724](https://github.com/zephyrproject-rtos/zephyr/issues/4724) - sanitycheck build\_only option can be confusing
- [GitHub #4772](https://github.com/zephyrproject-rtos/zephyr/issues/4772) - doc: add contributing info about shippable failures
- [GitHub #4777](https://github.com/zephyrproject-rtos/zephyr/issues/4777) - need a testcase for version number of the kernel and version.h
- [GitHub #4779](https://github.com/zephyrproject-rtos/zephyr/issues/4779) - net: tcp: FIN isn’t sent when performing active close.
- [GitHub #4826](https://github.com/zephyrproject-rtos/zephyr/issues/4826) - Bluetooth IPSP example does not reach main() on qemu\_cortex\_m3
- [GitHub #4828](https://github.com/zephyrproject-rtos/zephyr/issues/4828) - device tree: Introduce bus objects (i2c-device)
- [GitHub #4851](https://github.com/zephyrproject-rtos/zephyr/issues/4851) - cmake does not show verbose output of build tools
- [GitHub #4885](https://github.com/zephyrproject-rtos/zephyr/issues/4885) - cmake: IS\_TEST guessing gets thrown off by symlinks
- [GitHub #4924](https://github.com/zephyrproject-rtos/zephyr/issues/4924) - dumb\_http\_server pollutes the source directory
- [GitHub #4934](https://github.com/zephyrproject-rtos/zephyr/issues/4934) - net: 15.4 network interfaces use incorrect MTU setting of 127
- [GitHub #4941](https://github.com/zephyrproject-rtos/zephyr/issues/4941) - LwM2M: support discovery other than ‘/’
- [GitHub #4983](https://github.com/zephyrproject-rtos/zephyr/issues/4983) - ARMv8-M basic support
- [GitHub #4989](https://github.com/zephyrproject-rtos/zephyr/issues/4989) - Bluetooth: PTS fails to connect to Zephyr
- [GitHub #5010](https://github.com/zephyrproject-rtos/zephyr/issues/5010) - changes to included linker scripts are not picked up by the build system
- [GitHub #5017](https://github.com/zephyrproject-rtos/zephyr/issues/5017) - Genuino/Arduino 101 Sensor Sample BMI160: Gyro Device not found
- [GitHub #5091](https://github.com/zephyrproject-rtos/zephyr/issues/5091) - MPU fault at drivers/flash/soc\_flash\_nrf5.c:493 with NFFS enabled on nrf52840\_pca10056
- [GitHub #5101](https://github.com/zephyrproject-rtos/zephyr/issues/5101) - LwM2M: device hang after requesting a firmware update to a loopback device IP
- [GitHub #5109](https://github.com/zephyrproject-rtos/zephyr/issues/5109) - yaml: fix key/value syntax to ‘mapping’ instead of ‘series’
- [GitHub #5130](https://github.com/zephyrproject-rtos/zephyr/issues/5130) - include guards missing in toolchain/gcc.h and toolchain/common.h
- [GitHub #5136](https://github.com/zephyrproject-rtos/zephyr/issues/5136) - “Distinguishing Features” section in docs is outdated and needs an update
- [GitHub #5143](https://github.com/zephyrproject-rtos/zephyr/issues/5143) - Cmake ignores setting CONFIG\_ETH\_MCUX\_0=n in prj.conf
- [GitHub #5148](https://github.com/zephyrproject-rtos/zephyr/issues/5148) - Lightweight flash storage layer
- [GitHub #5162](https://github.com/zephyrproject-rtos/zephyr/issues/5162) - Reduce duplication in UUID definitions?
- [GitHub #5184](https://github.com/zephyrproject-rtos/zephyr/issues/5184) - kernel system call handlers missing due to -Wl,–no-whole-archive
- [GitHub #5221](https://github.com/zephyrproject-rtos/zephyr/issues/5221) - Build doesn’t fail if total RAM usage is greater than the RAM available on the board
- [GitHub #5226](https://github.com/zephyrproject-rtos/zephyr/issues/5226) - Compiling with -O0 causes the kobject text area to exceed the limit (linker error)
- [GitHub #5228](https://github.com/zephyrproject-rtos/zephyr/issues/5228) - The build fails when building echo\_server with nrf52840\_pca10056
- [GitHub #5240](https://github.com/zephyrproject-rtos/zephyr/issues/5240) - I2C is enabled by default on ESP32
- [GitHub #5247](https://github.com/zephyrproject-rtos/zephyr/issues/5247) - Object tracing test case fails in NRF boards
- [GitHub #5256](https://github.com/zephyrproject-rtos/zephyr/issues/5256) - \_nano\_tick\_delta, sys\_tick\_delta, sys\_tick\_delta\_32: not used or tested
- [GitHub #5270](https://github.com/zephyrproject-rtos/zephyr/issues/5270) - Not all IEEE802154\_MCR20A\_RAW references were removed
- [GitHub #5282](https://github.com/zephyrproject-rtos/zephyr/issues/5282) - net: IPv6 DAD is incorrect, wouldn’t work (“always succeed”) on mcast medium like Ethernet
- [GitHub #5283](https://github.com/zephyrproject-rtos/zephyr/issues/5283) - reference to non-existing functions in arch/x86/core/intstub.S
- [GitHub #5305](https://github.com/zephyrproject-rtos/zephyr/issues/5305) - flash: use generated FLASH\_WRITE\_BLOCK\_SIZE in flash\_stm32\_api
- [GitHub #5317](https://github.com/zephyrproject-rtos/zephyr/issues/5317) - IPSP deadlock during disconnect -> net\_if\_down
- [GitHub #5326](https://github.com/zephyrproject-rtos/zephyr/issues/5326) - IPSP ping fails
- [GitHub #5328](https://github.com/zephyrproject-rtos/zephyr/issues/5328) - build system should try and create conf if not found for non-zephyr SDK
- [GitHub #5334](https://github.com/zephyrproject-rtos/zephyr/issues/5334) - CMake: Ninja support is broken
- [GitHub #5345](https://github.com/zephyrproject-rtos/zephyr/issues/5345) - Cmake: ext: Header file include error: No such file or directory
- [GitHub #5348](https://github.com/zephyrproject-rtos/zephyr/issues/5348) - rom\_report is broken for some environments
- [GitHub #5351](https://github.com/zephyrproject-rtos/zephyr/issues/5351) - Some libraries should automatically be linked with ‘app’
- [GitHub #5355](https://github.com/zephyrproject-rtos/zephyr/issues/5355) - qemu\_x86/qemu\_x86\_nommu hangs on big executable files
- [GitHub #5370](https://github.com/zephyrproject-rtos/zephyr/issues/5370) - [Coverity CID: 180699] Error handling issues in /tests/bluetooth/tester/src/gatt.c
- [GitHub #5374](https://github.com/zephyrproject-rtos/zephyr/issues/5374) - merge\_config.sh can behave differently from merge\_config.py
- [GitHub #5379](https://github.com/zephyrproject-rtos/zephyr/issues/5379) - sample: net/socket/http\_get: no printf output
- [GitHub #5382](https://github.com/zephyrproject-rtos/zephyr/issues/5382) - P2P Device Firmware Update (FOTA) over BLE and Serial
- [GitHub #5391](https://github.com/zephyrproject-rtos/zephyr/issues/5391) - drivers: stm32 clock control: F0 Series with PREDIV1 Support uses wrong PLLSOURCE define for HSI clock
- [GitHub #5401](https://github.com/zephyrproject-rtos/zephyr/issues/5401) - delta\_ticks\_from\_prev become negative and waiting tasks never scheduled
- [GitHub #5406](https://github.com/zephyrproject-rtos/zephyr/issues/5406) - UART1 on STM32F0 Series not working: errors in makro to enable clock
- [GitHub #5418](https://github.com/zephyrproject-rtos/zephyr/issues/5418) - Provide a python based replacement for gperf
- [GitHub #5419](https://github.com/zephyrproject-rtos/zephyr/issues/5419) - Provide a python based kconfig processing script, replacement for conf/mconf..
- [GitHub #5428](https://github.com/zephyrproject-rtos/zephyr/issues/5428) - can not build for esp32
- [GitHub #5444](https://github.com/zephyrproject-rtos/zephyr/issues/5444) - bluetooth controller fails when building with -Wshadow
- [GitHub #5448](https://github.com/zephyrproject-rtos/zephyr/issues/5448) - STM32: Entropy test could not build
- [GitHub #5449](https://github.com/zephyrproject-rtos/zephyr/issues/5449) - STM32: provide default configuration for entropy sample
- [GitHub #5453](https://github.com/zephyrproject-rtos/zephyr/issues/5453) - gitlint should allow tabs in commit messages
- [GitHub #5458](https://github.com/zephyrproject-rtos/zephyr/issues/5458) - [ESP32] Make error
- [GitHub #5466](https://github.com/zephyrproject-rtos/zephyr/issues/5466) - sanitycheck: “CMake Error: : System Error: File name too long”
- [GitHub #5467](https://github.com/zephyrproject-rtos/zephyr/issues/5467) - NFFS file system does no build when newlib libc is used
- [GitHub #5471](https://github.com/zephyrproject-rtos/zephyr/issues/5471) - cmake errors at -B containing @
- [GitHub #5476](https://github.com/zephyrproject-rtos/zephyr/issues/5476) - Native port (posix) to write own PID into a file
- [GitHub #5477](https://github.com/zephyrproject-rtos/zephyr/issues/5477) - Native port (posix) to support receiving signals
- [GitHub #5483](https://github.com/zephyrproject-rtos/zephyr/issues/5483) - Native port (POSIX) should accept command-line arguments
- [GitHub #5484](https://github.com/zephyrproject-rtos/zephyr/issues/5484) - net: ARP/ND: Possibility for deadlocks and DoS
- [GitHub #5486](https://github.com/zephyrproject-rtos/zephyr/issues/5486) - Bluetooth: Cannot connect to prevoiusly disconnected device when BT\_PRIVACY is enabled
- [GitHub #5488](https://github.com/zephyrproject-rtos/zephyr/issues/5488) - target\_ld\_options will apply flags that should be skipped
- [GitHub #5493](https://github.com/zephyrproject-rtos/zephyr/issues/5493) - NFFS does not work with STM32L4 devices due to flash restrictions
- [GitHub #5497](https://github.com/zephyrproject-rtos/zephyr/issues/5497) - cmake: allow to link external libraries with –whole-archive
- [GitHub #5499](https://github.com/zephyrproject-rtos/zephyr/issues/5499) - config BT\_CTLR\_DEBUG\_PINS
- [GitHub #5504](https://github.com/zephyrproject-rtos/zephyr/issues/5504) - net: Incorrect logic for TCP “ackerr” statistics
- [GitHub #5530](https://github.com/zephyrproject-rtos/zephyr/issues/5530) - [Coverity CID: 181848] Null pointer dereferences in /subsys/bluetooth/host/mesh/access.c
- [GitHub #5531](https://github.com/zephyrproject-rtos/zephyr/issues/5531) - [Coverity CID: 181847] Incorrect expression in /samples/drivers/crypto/src/main.c
- [GitHub #5539](https://github.com/zephyrproject-rtos/zephyr/issues/5539) - tests/kernel/fatal/stack-sentinel fails when asserts are enabled
- [GitHub #5546](https://github.com/zephyrproject-rtos/zephyr/issues/5546) - (Stupid) questions about coverage reports
- [GitHub #5548](https://github.com/zephyrproject-rtos/zephyr/issues/5548) - coverage should be collected from code built with -O0
- [GitHub #5557](https://github.com/zephyrproject-rtos/zephyr/issues/5557) - Cloning Zephyr with git’s core.autocrlf=true leads to obscure errors
- [GitHub #5565](https://github.com/zephyrproject-rtos/zephyr/issues/5565) - net: Kconfig: NET\_BUF\_LOG and NET\_BUF\_SIMPLE\_LOG unrightly select STDOUT\_CONSOLE
- [GitHub #5566](https://github.com/zephyrproject-rtos/zephyr/issues/5566) - kconfig: STDOUT\_CONSOLE unrightly stuffed under subsys/debug
- [GitHub #5576](https://github.com/zephyrproject-rtos/zephyr/issues/5576) - None of the :github:’XYZ’ links work in the 1.10 release notes
- [GitHub #5589](https://github.com/zephyrproject-rtos/zephyr/issues/5589) - Issue with using generic gcc cross compile with cmake
- [GitHub #5601](https://github.com/zephyrproject-rtos/zephyr/issues/5601) - docs for cc3220sf\_launchxl are out of date/incorrect
- [GitHub #5608](https://github.com/zephyrproject-rtos/zephyr/issues/5608) - Bluetooth LE continuous scan weird behaviour
- [GitHub #5619](https://github.com/zephyrproject-rtos/zephyr/issues/5619) - zephyr.git/tests/misc/test\_build/testcase.yaml#test\_newlib @ esp32:xtensa BUILD failed
- [GitHub #5626](https://github.com/zephyrproject-rtos/zephyr/issues/5626) - Building samples failed
- [GitHub #5640](https://github.com/zephyrproject-rtos/zephyr/issues/5640) - MacOS compile error with -std=gnu89
- [GitHub #5645](https://github.com/zephyrproject-rtos/zephyr/issues/5645) - build failures with asserts enabled/newlib: arch/arm/core/cortex\_m/mpu/nxp\_mpu.c
- [GitHub #5646](https://github.com/zephyrproject-rtos/zephyr/issues/5646) - userbuffer\_validate test fails with double fault if CONFIG\_USERSPACE disabled
- [GitHub #5650](https://github.com/zephyrproject-rtos/zephyr/issues/5650) - i2c driver test on ESP32 fails with error
- [GitHub #5651](https://github.com/zephyrproject-rtos/zephyr/issues/5651) - [In Progress] arch: arm: linkder: vt must be linked at address 0x00000000 for Cortex-M0
- [GitHub #5660](https://github.com/zephyrproject-rtos/zephyr/issues/5660) - doc: make: make htmldocs fails in genrest.py/kconfiglib.py
- [GitHub #5673](https://github.com/zephyrproject-rtos/zephyr/issues/5673) - kconfig regression: Existing configuration is overwritten on reconfiguration
- [GitHub #5687](https://github.com/zephyrproject-rtos/zephyr/issues/5687) - docs: Confusing treatment of “Sensor Drivers” in Zephyr subsystem docs
- [GitHub #5692](https://github.com/zephyrproject-rtos/zephyr/issues/5692) - sensors: struct sensor\_value::val2 is confusingly defined
- [GitHub #5693](https://github.com/zephyrproject-rtos/zephyr/issues/5693) - sensors: SENSOR\_CHAN\_HUMIDITY confusingly defined in “milli percent”, SENSOR\_CHAN\_DISTANCE inconsistently defined in millimeters
- [GitHub #5696](https://github.com/zephyrproject-rtos/zephyr/issues/5696) - net\_app: Static vs DHCPv4 behavior appears to be not as described
- [GitHub #5699](https://github.com/zephyrproject-rtos/zephyr/issues/5699) - Zephyr installs a broken pyOCD
- [GitHub #5717](https://github.com/zephyrproject-rtos/zephyr/issues/5717) - CONTRIBUTING instructions are Linux-specific and don’t work for Windows
- [GitHub #5719](https://github.com/zephyrproject-rtos/zephyr/issues/5719) - need a zephyr-env.sh equivalent for Windows developers
- [GitHub #5720](https://github.com/zephyrproject-rtos/zephyr/issues/5720) - Add CONFIG\_NOOPTIMIZATIONS option
- [GitHub #5722](https://github.com/zephyrproject-rtos/zephyr/issues/5722) - dts board configuration is incompatible with “build all” kind of test
- [GitHub #5724](https://github.com/zephyrproject-rtos/zephyr/issues/5724) - [Windows] Instructions for setting up a bash-less environment uses bashisms
- [GitHub #5726](https://github.com/zephyrproject-rtos/zephyr/issues/5726) - CI should use the same generator as the sanitycheck default
- [GitHub #5737](https://github.com/zephyrproject-rtos/zephyr/issues/5737) - [Coverity CID: 182195] Error handling issues in /subsys/fs/fcb/fcb\_walk.c
- [GitHub #5740](https://github.com/zephyrproject-rtos/zephyr/issues/5740) - [Coverity CID: 181923] Incorrect expression in /subsys/bluetooth/controller/ll\_sw/ctrl.c
- [GitHub #5741](https://github.com/zephyrproject-rtos/zephyr/issues/5741) - [Coverity CID: 181922] Incorrect expression in /subsys/bluetooth/controller/ll\_sw/ctrl.c
- [GitHub #5743](https://github.com/zephyrproject-rtos/zephyr/issues/5743) - Windows and Linux are writing .config files with options re-ordered
- [GitHub #5749](https://github.com/zephyrproject-rtos/zephyr/issues/5749) - Exception and Interrupt vector forwarding
- [GitHub #5753](https://github.com/zephyrproject-rtos/zephyr/issues/5753) - Bluetooth: controller: In nRF5 radio. c RATEBOOST event not cleared in ISRs
- [GitHub #5755](https://github.com/zephyrproject-rtos/zephyr/issues/5755) - Support flash in jlink runner
- [GitHub #5756](https://github.com/zephyrproject-rtos/zephyr/issues/5756) - MCUboot-compatible builds in Zephyr
- [GitHub #5760](https://github.com/zephyrproject-rtos/zephyr/issues/5760) - doc: device.h defines device\_power\_management\_api group twice
- [GitHub #5761](https://github.com/zephyrproject-rtos/zephyr/issues/5761) - NRF5 BLE radio driver: PPI18 is cleared unconditionally
- [GitHub #5762](https://github.com/zephyrproject-rtos/zephyr/issues/5762) - Windows 10 WSL does not supports Native POSIX Boards
- [GitHub #5766](https://github.com/zephyrproject-rtos/zephyr/issues/5766) - boards: nucleo\_f413zh: Likely outdated OpenOCD info in docs
- [GitHub #5771](https://github.com/zephyrproject-rtos/zephyr/issues/5771) - Linking issues with host cross compile with cmake
- [GitHub #5772](https://github.com/zephyrproject-rtos/zephyr/issues/5772) - sanitycheck crashes if ZEPHYR\_BASE has symlinks in its path
- [GitHub #5778](https://github.com/zephyrproject-rtos/zephyr/issues/5778) - Add/fix flash controller nodes for NXP kinetis SoCs
- [GitHub #5779](https://github.com/zephyrproject-rtos/zephyr/issues/5779) - bluetooth test\_controller\_4\_0 fails to build on nrf52840\_pca10056
- [GitHub #5784](https://github.com/zephyrproject-rtos/zephyr/issues/5784) - make rom\_report fails for qemu\_x86 (not finding zephyr.bin)
- [GitHub #5794](https://github.com/zephyrproject-rtos/zephyr/issues/5794) - wiki/Development-Model is out of date
- [GitHub #5808](https://github.com/zephyrproject-rtos/zephyr/issues/5808) - msys2 getting started instructions are missing Ninja install step
- [GitHub #5817](https://github.com/zephyrproject-rtos/zephyr/issues/5817) - socket.h: Using #define for POSIX redefinition of zsock\_ functions has unintended consequences
- [GitHub #5821](https://github.com/zephyrproject-rtos/zephyr/issues/5821) - [MSYS2] Unable to build Zephyr
- [GitHub #5823](https://github.com/zephyrproject-rtos/zephyr/issues/5823) - Bluetooth: Collision during Start Encryption procedure
- [GitHub #5836](https://github.com/zephyrproject-rtos/zephyr/issues/5836) - spi: stm32: convert remaining boards that support SPI to using dts
- [GitHub #5853](https://github.com/zephyrproject-rtos/zephyr/issues/5853) - Using newlibc in a project breaks ‘rom\_report’ and ‘ram\_report’ targets.
- [GitHub #5866](https://github.com/zephyrproject-rtos/zephyr/issues/5866) - ram\_report not working for qemu targets
- [GitHub #5877](https://github.com/zephyrproject-rtos/zephyr/issues/5877) - sensors: Cleanup Kconfig for address, driver & bus name
- [GitHub #5881](https://github.com/zephyrproject-rtos/zephyr/issues/5881) - enabling THREAD\_MONITOR causes tests to fail
- [GitHub #5886](https://github.com/zephyrproject-rtos/zephyr/issues/5886) - [Coverity CID: 182602] Integer handling issues in /drivers/interrupt\_controller/system\_apic.c
- [GitHub #5887](https://github.com/zephyrproject-rtos/zephyr/issues/5887) - [Coverity CID: 182597] Control flow issues in /drivers/sensor/vl53l0x/vl53l0x.c
- [GitHub #5888](https://github.com/zephyrproject-rtos/zephyr/issues/5888) - [Coverity CID: 182594] Control flow issues in /drivers/sensor/lsm6ds0/lsm6ds0.c
- [GitHub #5889](https://github.com/zephyrproject-rtos/zephyr/issues/5889) - [Coverity CID: 182593] Control flow issues in /drivers/sensor/vl53l0x/vl53l0x.c
- [GitHub #5890](https://github.com/zephyrproject-rtos/zephyr/issues/5890) - [Coverity CID: 182588] Integer handling issues in /drivers/sensor/hts221/hts221.c
- [GitHub #5903](https://github.com/zephyrproject-rtos/zephyr/issues/5903) - Code coverage reports seem wrong
- [GitHub #5919](https://github.com/zephyrproject-rtos/zephyr/issues/5919) - Remove obsolete FLASH\_DRIVER\_NAME
- [GitHub #5938](https://github.com/zephyrproject-rtos/zephyr/issues/5938) - Incorrectly reported coverage changes
- [GitHub #5952](https://github.com/zephyrproject-rtos/zephyr/issues/5952) - API k\_delayed\_work\_submit\_to\_queue() make a delayed\_work unusable
- [GitHub #5958](https://github.com/zephyrproject-rtos/zephyr/issues/5958) - “Ninja flash” swallows user prompts
- [GitHub #5968](https://github.com/zephyrproject-rtos/zephyr/issues/5968) - datastructure for LIFO
- [GitHub #5982](https://github.com/zephyrproject-rtos/zephyr/issues/5982) - nRF5x subscribe will cause HardFault while disconnect and reconnect
- [GitHub #5989](https://github.com/zephyrproject-rtos/zephyr/issues/5989) - workstation setup instructions are broken for Fedora
- [GitHub #5992](https://github.com/zephyrproject-rtos/zephyr/issues/5992) - doc: Discrepancy in Zephyr memory domain API documentation
- [GitHub #5994](https://github.com/zephyrproject-rtos/zephyr/issues/5994) - samples/bluetooth/ipsp: build failed for MICRO-BIT & NRF51-PCA10028 HW
- [GitHub #5996](https://github.com/zephyrproject-rtos/zephyr/issues/5996) - Need a “ps aux” like command to list all running threads and their attributes
- [GitHub #6010](https://github.com/zephyrproject-rtos/zephyr/issues/6010) - Removal of old HTTP API is causing errors and faults
- [GitHub #6013](https://github.com/zephyrproject-rtos/zephyr/issues/6013) - updated workstations setup breaks FC27
- [GitHub #6023](https://github.com/zephyrproject-rtos/zephyr/issues/6023) - Bluetooth: Invalid behaviour of Transport Layer after Incomplete timer expiration
- [GitHub #6025](https://github.com/zephyrproject-rtos/zephyr/issues/6025) - mbedTLS: Buffer overflow security issue, requires upgrade to 2.7.0
- [GitHub #6050](https://github.com/zephyrproject-rtos/zephyr/issues/6050) - IPSP sample failed: Cannot bind IPv6 mcast (-2)
- [GitHub #6062](https://github.com/zephyrproject-rtos/zephyr/issues/6062) - build failure in tests/boards/altera\_max10/i2c\_master with sys log enabled
- [GitHub #6064](https://github.com/zephyrproject-rtos/zephyr/issues/6064) - k\_is\_in\_isr() returns false inside “direct” interrupts on several arches
- [GitHub #6081](https://github.com/zephyrproject-rtos/zephyr/issues/6081) - echo server crash from corrupt ICMPv4 packet
- [GitHub #6083](https://github.com/zephyrproject-rtos/zephyr/issues/6083) - Bluetooth: Regression in MESH tests
- [GitHub #6091](https://github.com/zephyrproject-rtos/zephyr/issues/6091) - [Coverity CID: 182780] Error handling issues in /samples/net/sockets/http\_get/src/http\_get.c
- [GitHub #6092](https://github.com/zephyrproject-rtos/zephyr/issues/6092) - [Coverity CID: 182779] Memory - corruptions in /drivers/flash/soc\_flash\_nios2\_qspi.c
- [GitHub #6102](https://github.com/zephyrproject-rtos/zephyr/issues/6102) - [Coverity CID: 182769] Error handling issues in /subsys/bluetooth/host/mesh/beacon.c
- [GitHub #6121](https://github.com/zephyrproject-rtos/zephyr/issues/6121) - doc: unit tests documentation refers to non existing sample code
- [GitHub #6127](https://github.com/zephyrproject-rtos/zephyr/issues/6127) - net: Semantics of CONFIG\_NET\_BUF\_POOL\_USAGE changed (incorrectly)
- [GitHub #6131](https://github.com/zephyrproject-rtos/zephyr/issues/6131) - mbedtls: Name of config-mini-tls1\_2.h contradicts description
- [GitHub #6135](https://github.com/zephyrproject-rtos/zephyr/issues/6135) - build error with gcc 7.3
- [GitHub #6164](https://github.com/zephyrproject-rtos/zephyr/issues/6164) - timer: cortex\_m: Incorrect read of clock cycles counter after idle tickless period
- [GitHub #6185](https://github.com/zephyrproject-rtos/zephyr/issues/6185) - [MSYS2] Unable to build hello\_world sample
- [GitHub #6194](https://github.com/zephyrproject-rtos/zephyr/issues/6194) - K64F ethernet regression since f7ec62eb
- [GitHub #6197](https://github.com/zephyrproject-rtos/zephyr/issues/6197) - echo server crash from corrupt ICMPv6 packet
- [GitHub #6204](https://github.com/zephyrproject-rtos/zephyr/issues/6204) - bluetooth controller: crc init is not random
- [GitHub #6217](https://github.com/zephyrproject-rtos/zephyr/issues/6217) - echo server crash from corrupt ICMPv6 NS packet
- [GitHub #6229](https://github.com/zephyrproject-rtos/zephyr/issues/6229) - Bluetooth, nRF51: ticker\_success\_assert during flash erase
- [GitHub #6231](https://github.com/zephyrproject-rtos/zephyr/issues/6231) - samples/bluetooth/eddystone: failed to connect with central device
- [GitHub #6232](https://github.com/zephyrproject-rtos/zephyr/issues/6232) - samples/bluetooth/central\_hr: Run time HARD fault occurs
- [GitHub #6233](https://github.com/zephyrproject-rtos/zephyr/issues/6233) - samples/bluetooth/central: Run time HARD fault occurs
- [GitHub #6235](https://github.com/zephyrproject-rtos/zephyr/issues/6235) - echo server crash from ICMPv6 NS source link layer address anomaly
- [GitHub #6238](https://github.com/zephyrproject-rtos/zephyr/issues/6238) - spi: stm32f0 IRQ priority is invalid
- [GitHub #6240](https://github.com/zephyrproject-rtos/zephyr/issues/6240) - “Previous execution” and “Next execution” display problem.
- [GitHub #6257](https://github.com/zephyrproject-rtos/zephyr/issues/6257) - test, please ignore
- [GitHub #6261](https://github.com/zephyrproject-rtos/zephyr/issues/6261) - [Coverity CID: 182887] Control flow issues in /drivers/gpio/gpio\_esp32.c
- [GitHub #6263](https://github.com/zephyrproject-rtos/zephyr/issues/6263) - ARC: Implement userspace
- [GitHub #6264](https://github.com/zephyrproject-rtos/zephyr/issues/6264) - ARM: Implement Userspace
- [GitHub #6279](https://github.com/zephyrproject-rtos/zephyr/issues/6279) - Add doc to samples/bluetooth/mesh & samples/bluetooth/mesh\_demo
- [GitHub #6284](https://github.com/zephyrproject-rtos/zephyr/issues/6284) - docs.zephyrproject.org should be served with HTTPS
- [GitHub #6309](https://github.com/zephyrproject-rtos/zephyr/issues/6309) - Non-blocking BSD sockets not working as expected
- [GitHub #6312](https://github.com/zephyrproject-rtos/zephyr/issues/6312) - The shell sample does not working on k64f board
- [GitHub #6315](https://github.com/zephyrproject-rtos/zephyr/issues/6315) - echo server crash from malformed ICMPv6 NA
- [GitHub #6322](https://github.com/zephyrproject-rtos/zephyr/issues/6322) - shell crashes when enter is pressed
- [GitHub #6323](https://github.com/zephyrproject-rtos/zephyr/issues/6323) - “SPI master port SPI\_1 not found\* when porting spi ethernet device enc28j60 on stm32\_min\_dev board
- [GitHub #6324](https://github.com/zephyrproject-rtos/zephyr/issues/6324) - doc: Project coding standards: page not found
- [GitHub #6333](https://github.com/zephyrproject-rtos/zephyr/issues/6333) - How do I implement GPIO on the f429zi board?
- [GitHub #6339](https://github.com/zephyrproject-rtos/zephyr/issues/6339) - samples/drivers/gpio Sample doesn’t work on ESP32 after SMP support was added
- [GitHub #6346](https://github.com/zephyrproject-rtos/zephyr/issues/6346) - ESP-32 preemption regressions with asm2
- [GitHub #6382](https://github.com/zephyrproject-rtos/zephyr/issues/6382) - echo server: crash from unsolicited RA reachable time anomaly
- [GitHub #6393](https://github.com/zephyrproject-rtos/zephyr/issues/6393) - echo server: crash from NS flood
- [GitHub #6429](https://github.com/zephyrproject-rtos/zephyr/issues/6429) - How to add custom driver subdirectory to application project?
- [GitHub #6432](https://github.com/zephyrproject-rtos/zephyr/issues/6432) - daily doc build pages don’t indicate their version
- [GitHub #6439](https://github.com/zephyrproject-rtos/zephyr/issues/6439) - ESP32 doesn’t compile in master
- [GitHub #6444](https://github.com/zephyrproject-rtos/zephyr/issues/6444) - tests/kernel/mem\_protect/obj\_validation/ fails to build
- [GitHub #6455](https://github.com/zephyrproject-rtos/zephyr/issues/6455) - k\_sleep() fails on ESP32 sometimes
- [GitHub #6469](https://github.com/zephyrproject-rtos/zephyr/issues/6469) - tests/crypto/ecc\_dsa results in FATAL EXCEPTION on esp32
- [GitHub #6470](https://github.com/zephyrproject-rtos/zephyr/issues/6470) - tests/crypto/ecc\_dh results in FATAL EXCEPTION on esp32
- [GitHub #6471](https://github.com/zephyrproject-rtos/zephyr/issues/6471) - tests/crypto/aes results in Assertion failure on esp32
- [GitHub #6472](https://github.com/zephyrproject-rtos/zephyr/issues/6472) - tests/crypto/sha256 results in Assertion failure on esp32
- [GitHub #6505](https://github.com/zephyrproject-rtos/zephyr/issues/6505) - Userspace support: stack corruption for ARC em7d v2.3
