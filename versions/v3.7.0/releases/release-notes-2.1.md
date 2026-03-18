---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/release-notes-2.1.html
original_path: releases/release-notes-2.1.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Zephyr 2.1.0

We are pleased to announce the release of Zephyr kernel version 2.1.0.

Major enhancements with this release include:

- Normalized APIs across all architectures.
- Expanded support for ARMv6-M architecture.
- Added support for numerous new boards and shields.
- Added numerous new drivers and sensors.
- Added new TCP stack implementation (experimental).
- Added BLE support on Vega platform (experimental).
- Memory size improvements to Bluetooth host stack.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

No security vulnerabilities received.

## Kernel

- Add arch abstraction for irq\_offload()
- Add architecture interface headers and normalized APIs across all arches
- Show faulting CPU on fatal error message
- Improve C++ compatibility
- Modified arch API namespace to allow automatic arch API documentation
  generation
- Use logging for userspace errors

## Architectures

- ARC:

  - Increased the exception handling stack size
  - Implement DIRECT IRQ support
  - Implement z\_arch\_system\_halt()
- ARM:

  - Added support for memory protection features (user mode and
    hardware-based stack overflow detection) in ARMv6-M architecture
  - Added QEMU support for ARMv6-M architecture
  - Extended test coverage for ARM-specific kernel features in ARMv6-M
    architecture
  - Enhanced runtime MPU programming in ARMv8-M architecture, making
    the full partitioning of kernel SRAM memory a user-configurable
    feature.
  - Added CMSIS support for Cortex-R architectures.
  - Updated CMSIS headers to version 5.6
  - Added missing Cortex-R CPU device tree bindings.
  - Fixed incorrect Cortex-R device tree specification.
  - Fixed several bugs in ARM architecture implementation
- POSIX:

  - Added support for CONFIG\_DYNAMIC\_INTERRUPTS (native\_posix
    & nrf52\_bsim)
- RISC-V:

  - Add support to boot multicore system
- x86:

  - Add basic ACPI and non-trivial memory map support
  - Add SMP support (64-bit mode only)
  - Inline direct ISR functions

## Boards & SoC Support

- Added support for these SoC series:

- Atmel SAMD51, SAME51, SAME53, SAME54
- Nordic Semiconductor nRF53
- NXP Kinetis KV5x
- STMicroelectronics STM32G4

- Added support for these ARM boards:

  - actinius\_icarus
  - cc3235sf\_launchxl
  - decawave\_dwm1001\_dev
  - degu\_evk
  - frdm\_k22f
  - frdm\_k82f
  - mec1501modular\_assy6885
  - nrf52833\_pca10100
  - nrf5340\_dk\_nrf5340
  - nucleo\_g431rb
  - pico\_pi\_m4
  - qemu\_cortex\_r0
  - sensortile\_box
  - steval\_fcu001v1
  - stm32f030\_demo
  - stm32l1\_disco
  - twr\_kv58f220m
- Added support for these following shields:

  - adafruit\_2\_8\_tft\_touch\_v2
  - dfrobot\_can\_bus\_v2\_0
  - link\_board\_eth
  - ssd1306\_128x32
  - ssd1306\_128x64
  - waveshare\_epaper
  - x\_nucleo\_idb05a1
- Added CAN support for Olimexino STM32 board

## Drivers and Sensors

- ADC

  - Added support for STM32G4X in STM32 driver
  - Added Microchip XEC ADC driver
- Bluetooth

  - Added RPMsg transport HCI driver
- CAN

  - Added API to read the bus-state and error counters
  - Added API for bus-off recovery
  - Optimizations for the MCP2515 driver
  - Bug fixes
- Clock Control

  - Added support for nRF52833 in nRF driver
  - Added support for STM32G4X in STM32 driver
- Console

  - Removed deprecated function console\_register\_line\_input
- Counter

  - Added support for STM32L1 and STM32G4X in STM32 driver
  - Removed QMSI driver
  - Added Microchip XEC driver
- Display

  - Enhanced SSD1306 driver to support build time selection
  - Enhanced SSD16XX driver to use bytestring property for LUT and parameters
- DMA

  - Added generic STM32 driver
  - Removed QMSI driver
- EEPROM

  - Added EEPROM device driver API
  - Added Atmel AT24 (and compatible) I2C EEPROM driver
  - Added Atmel AT25 (and compatible) SPI EEPROM driver
  - Added native\_posix EEPROM emulation driver
- Entropy

  - Added RV32M1 driver
  - Added support for STM32G4X in STM32 driver
- Ethernet

  - Added MAC address configuration and carrier state detection to STM32 driver
  - Added ENC424J600 driver
  - Removed DesignWare driver
- Flash

  - Added deep-power-down mode support in SPI NOR driver
  - Fixed STM32 driver for 2MB parts
  - Added support for STM32G4X in STM32 driver
  - Removed QMSI driver
- GPIO

  - Added support for STM32G4X in STM32 driver
  - Removed QMSI, SCH, and SAM3 drivers
- Hardware Info

  - Added LiteX DNA driver
- I2C

  - Converted remaining drivers to device tree
  - Added support for STM32G4X in STM32 driver
  - Fixed DesignWare driver for 64-bit
  - Removed QMSI driver
  - Added proper error handling in XEC driver
- I2S

  - Refactored STM32 driver
- IEEE 802.15.4

  - Added CC13xx / CC26xx driver
- Interrupt Controller

  - Added support for SAME54 to SAM0 EIC driver
  - Added support for STM32G4X in STM32 driver
  - Converted RISC-V plic to use multi-level irq support
- IPM

  - Added nRFx driver
- Keyboard Scan

  - Added Microchip XEC driver
- LED

  - Removed non-DTS support from LP5562, PCA9633, and LP3943 drivers
- Modem

  - Added simple power management to modem receiver
- Pinmux

  - Added support for STM32G4X in STM32 driver
  - Removed QMSI driver
- PS/2

  - Added Microchip XEC driver
- PWM

  - Added PWM shell
  - Added Microchip XEC driver
  - Removed QMSI driver
- Sensor

  - Fixed raw value scaling and SPI burst transfers in LIS2DH driver
  - Converted various drivers to device tree
  - Fixed fractional part calculation in ENS210 driver
  - Added OPT3001 light sensor driver
  - Added SI7060 temperature sensor driver
  - Added TMP116 driver
  - Implemented single shot mode in SHT3XD driver
  - Added single/double tap trigger support in LIS2DW12 driver
- Serial

  - Added support for SAME54 to SAM0 driver
  - Added support for STM32G4X in STM32 driver
  - Added support for 2 stop bits in nRF UARTE and UART drivers
  - Removed QMSI driver
  - Added ESP32 driver with FIFO/interrupt support
- SPI

  - Added support for nRF52833 in nRFx driver
  - Added support for STM32G4X in STM32 driver
  - Added RV32M1 driver
  - Added Microchip XEC driver
  - Added LiteX driver
  - Removed Intel Quark driver
- Timer

  - Fixed starving clock announcements in SYSTICK and nRF drivers
  - Fixed clamp tick adjustment in tickless mode in various drivers
  - Fixed calculation of absolute cycles in SYSTICK driver
  - Fixed lost ticks from unannounced elapsed in nRF driver
  - Fixed SMP bug in ARC driver
  - Added STM32 LPTIM driver
  - Changed CC13X2/CC26X2 to use RTC instead of SYSTICK for system clock
- USB

  - Added support for nRF52833 in nRFx driver
  - Added support for STM32G4X in STM32 driver
  - Enabled ZLP hardware handling for variable-length data storage
- Video

  - Added MCUX CSI and Aptina MT9M114 drivers
  - Added software video pattern generator driver
- Watchdog

  - Added support for SAME54 to SAM0 driver
  - Converted drivers to use device tree
  - Removed QMSI driver
  - Added STM32 WWDG driver
  - Added Microchip XEC driver
- WiFi

  - Implemented TCP/UDP socket offload with TLS in Inventek eS-WiFi driver

## Networking

- Added new TCP stack implementation. The new TCP stack is still experimental
  and is turned off by default. Users wanting to experiment with it can set
  `CONFIG_NET_TCP2` Kconfig option.
- Added support for running MQTT protocol on top of a Websocket connection.
- Added support for enabling DNS in LWM2M.
- Added support for resetting network statistics in net-shell.
- Added support for getting statistics about the time it took to receive or send
  a network packet.
- Added support for sending a PPP Echo-Reply packet when a Echo-Request packet
  is received.
- Added CC13xx / CC26xx device drivers for IEEE 802.15.4.
- Added TCP/UDP socket offload with TLS for eswifi network driver.
- Added support for sending multiple SNTP requests to increase reliability.
- Added support for choosing a default network protocol in socket() call.
- Added support for selecting either native IP stack, which is the default, or
  offloaded IP stack. This can save ROM and RAM as we do not need to enable
  network functionality that is not going to be used in the network device.
- Added support for LWM2M client initiated de-register.
- Updated the supported version of OpenThread.
- Updated OpenThread configuration to use mbedTLS provided by Zephyr.
- Various fixes to TCP connection establishment.
- Fixed delivery of multicast packets to all listening sockets.
- Fixed network interface initialization when using socket offloading.
- Fixed initial message id seed value for sent CoAP messages.
- Fixed selection of network interface when using “net ping” command to send
  ICMPv4 echo-request packet.
- Networking sample changes for:

  - http\_client
  - dumb\_http\_server\_mt
  - dumb\_http\_server
  - echo\_server
  - mqtt\_publisher
  - zperf
- Network device driver changes for:

  - Ethernet enc424j600 (new driver)
  - Ethernet enc28j60
  - Ethernet stm32
  - WiFi simplelink
  - Ethernet DesignWare (removed)

## Bluetooth

- Host:

  - Reworked the Host transmission path to improve memory footprint and remove potential deadlocks
  - Document HCI errors for connected callback
  - GATT: Added a `bt_gatt_is_subscribed()` function to check if attribute has been subscribed
  - GATT: Added an initializer for GATT CCC structures
  - HCI: Added a function to get the connection handle of a connection
  - Added ability to load CCC settings on demand to reduce memory usage
  - Made the time to run slave connection parameters update procedure configurable
  - Folded consecutive calls to bt\_rand into one to reduce overhead
  - Added key displacement feature for key storage
  - Reduced severity of unavoidable warnings
  - Added support C++20 designated initializers
  - Mesh: Add the model extension concept as described in the Mesh Profile Specification
  - Mesh: Added support for acting as a Provisioner
- BLE split software Controller:

  - Numerous bug fixes
  - Fixed several control procedure (LLCP) handling issues
  - Added experimental BLE support on Vega platform.
  - Added a hook for flushing in LLL
  - Implemented the LLL reset functions in a call from ll\_reset
  - Made the number of TX ctrl buffers configurable
  - Added support for Zero Latency IRQs
- BLE legacy software Controller:

  - Multiple bug fixes

## Build and Infrastructure

- Deprecated kconfig functions dt\_int\_val, dt\_hex\_val, and dt\_str\_val.
  Use new functions that utilize eDTS info such as dt\_node\_reg\_addr.
  See [scripts/kconfig/kconfigfunctions.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfigfunctions.py) for details.
- Deprecated direct use of the `DT_` Kconfig symbols from the generated
  `generated_dts_board.conf`. This was done to have a single source of
  Kconfig symbols coming from only Kconfig (additionally the build should
  be slightly faster). For Kconfig files we should utilize functions from
  [scripts/kconfig/kconfigfunctions.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfigfunctions.py). See
  [Custom Kconfig Preprocessor Functions](../build/kconfig/preprocessor-functions.md#kconfig-functions) for usage details. For sanitycheck yaml usage
  we should utilize functions from
  [scripts/sanity\_chk/expr\_parser.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/sanity_chk/expr_parser.py). Its possible that a
  new function might be required for a particular use pattern that isn’t
  currently supported.
- Various parts of the binding format have been simplified. The format is
  better documented now too.

## Libraries / Subsystems

- Random

  - Add cryptographically secure random functions
  - Add bulk fill random functions

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Documentation

- A new Getting Started Guide simplifies and streamlines the “out of
  box” experience for developers, from setting up their development
  environment through running the blinky sample.
- Many additions and updates to architecture, build, and process docs including
  sanity check, board porting, Bluetooth, scheduling, timing,
  peripherals, configuration, and user mode.
- Documentation for new boards and samples.
- Improvements and clarity of API documentation.

## Tests and Samples

- We have implemented additional tests and significantly expanded the amount
  of test cases in existing tests to increase code coverage.

## Issue Related Items

These GitHub issues were addressed since the previous 2.0.0 tagged
release:

- [GitHub #21177](https://github.com/zephyrproject-rtos/zephyr/issues/21177) - Long ATT MTU reports wrong length field in write callback.
- [GitHub #21148](https://github.com/zephyrproject-rtos/zephyr/issues/21148) - nrf51: uart\_1 does not compile
- [GitHub #21131](https://github.com/zephyrproject-rtos/zephyr/issues/21131) - Bluetooth: host: Subscriptions not removed upon unpair
- [GitHub #21139](https://github.com/zephyrproject-rtos/zephyr/issues/21139) - west: runners: blackmagicprobe: Keyboard Interrupt shouldn’t kill the process
- [GitHub #21126](https://github.com/zephyrproject-rtos/zephyr/issues/21126) - drivers: spi\_nrfx\_spim: Incorrect handling of extended SPIM configuration
- [GitHub #21115](https://github.com/zephyrproject-rtos/zephyr/issues/21115) - Request a new repository for the Xtensa HAL
- [GitHub #21113](https://github.com/zephyrproject-rtos/zephyr/issues/21113) - k\_sem\_give reschedules cooperative threads unexpectedly
- [GitHub #21102](https://github.com/zephyrproject-rtos/zephyr/issues/21102) - Slack link at [https://www.zephyrproject.org/](https://www.zephyrproject.org/) is expired
- [GitHub #21077](https://github.com/zephyrproject-rtos/zephyr/issues/21077) - Help: Pull request “Identity/Emails issues”
- [GitHub #21059](https://github.com/zephyrproject-rtos/zephyr/issues/21059) - Bluetooth sent callback delayed more than ATT
- [GitHub #21049](https://github.com/zephyrproject-rtos/zephyr/issues/21049) - Bluetooth: Multiple issues with net\_buf usage
- [GitHub #21048](https://github.com/zephyrproject-rtos/zephyr/issues/21048) - timer case fail on qemu\_xtensa and mps2\_an385
- [GitHub #21004](https://github.com/zephyrproject-rtos/zephyr/issues/21004) - cmd\_data buffer corruption
- [GitHub #20970](https://github.com/zephyrproject-rtos/zephyr/issues/20970) - Bluetooth: Mesh: seg\_tx\_reset in the transport layer
- [GitHub #20969](https://github.com/zephyrproject-rtos/zephyr/issues/20969) - No SOURCES given to target: drivers\_\_gpio
- [GitHub #20968](https://github.com/zephyrproject-rtos/zephyr/issues/20968) - [Coverity CID :206016] Side effect in assertion in tests/kernel/sched/metairq/src/main.c
- [GitHub #20967](https://github.com/zephyrproject-rtos/zephyr/issues/20967) - [Coverity CID :206017] Out-of-bounds read in drivers/ipm/ipm\_nrfx\_ipc.c
- [GitHub #20966](https://github.com/zephyrproject-rtos/zephyr/issues/20966) - [Coverity CID :206018] Side effect in assertion in tests/kernel/sched/metairq/src/main.c
- [GitHub #20965](https://github.com/zephyrproject-rtos/zephyr/issues/20965) - [Coverity CID :206019] Side effect in assertion in tests/kernel/sched/metairq/src/main.c
- [GitHub #20964](https://github.com/zephyrproject-rtos/zephyr/issues/20964) - [Coverity CID :206020] Bad bit shift operation in drivers/ipm/ipm\_nrfx\_ipc.c
- [GitHub #20963](https://github.com/zephyrproject-rtos/zephyr/issues/20963) - [Coverity CID :206021] Side effect in assertion in tests/kernel/sched/metairq/src/main.c
- [GitHub #20962](https://github.com/zephyrproject-rtos/zephyr/issues/20962) - [Coverity CID :206022] Out-of-bounds read in drivers/ipm/ipm\_nrfx\_ipc.c
- [GitHub #20939](https://github.com/zephyrproject-rtos/zephyr/issues/20939) - long duration timeouts can cause loss of time
- [GitHub #20938](https://github.com/zephyrproject-rtos/zephyr/issues/20938) - ATT/L2CAP “deadlock”
- [GitHub #20936](https://github.com/zephyrproject-rtos/zephyr/issues/20936) - tests/kernel/mem\_protect/protection fails on ARMv8-M
- [GitHub #20933](https://github.com/zephyrproject-rtos/zephyr/issues/20933) - x\_nucleo\_iks01a3 shield: STM LSM6DSO sensor does not work after h/w or s/w reset
- [GitHub #20931](https://github.com/zephyrproject-rtos/zephyr/issues/20931) - intel\_s1000\_crb samples can’t be built with latest master
- [GitHub #20926](https://github.com/zephyrproject-rtos/zephyr/issues/20926) - ztest\_1cpu\_user\_unit\_test() doesn
- [GitHub #20892](https://github.com/zephyrproject-rtos/zephyr/issues/20892) - our nRF52840 board power management sleep duration
- [GitHub #20883](https://github.com/zephyrproject-rtos/zephyr/issues/20883) - [Coverity CID :205808] Integer handling issues in tests/net/lib/coap/src/main.c
- [GitHub #20882](https://github.com/zephyrproject-rtos/zephyr/issues/20882) - [Coverity CID :205806] Integer handling issues in tests/net/lib/coap/src/main.c
- [GitHub #20881](https://github.com/zephyrproject-rtos/zephyr/issues/20881) - [Coverity CID :205786] Integer handling issues in tests/net/lib/coap/src/main.c
- [GitHub #20880](https://github.com/zephyrproject-rtos/zephyr/issues/20880) - [Coverity CID :205780] Integer handling issues in tests/net/lib/coap/src/main.c
- [GitHub #20879](https://github.com/zephyrproject-rtos/zephyr/issues/20879) - [Coverity CID :205812] Incorrect expression in tests/kernel/spinlock/src/main.c
- [GitHub #20878](https://github.com/zephyrproject-rtos/zephyr/issues/20878) - [Coverity CID :205801] Incorrect expression in tests/kernel/mp/src/main.c
- [GitHub #20872](https://github.com/zephyrproject-rtos/zephyr/issues/20872) - [Coverity CID :205779] Parse warnings in subsys/usb/class/hid/core.c
- [GitHub #20871](https://github.com/zephyrproject-rtos/zephyr/issues/20871) - [Coverity CID :205815] Memory - illegal accesses in subsys/shell/shell.c
- [GitHub #20868](https://github.com/zephyrproject-rtos/zephyr/issues/20868) - [Coverity CID :205814] Null pointer dereferences in subsys/net/ip/6lo.c
- [GitHub #20867](https://github.com/zephyrproject-rtos/zephyr/issues/20867) - [Coverity CID :205803] Integer handling issues in subsys/fs/nvs/nvs.c
- [GitHub #20866](https://github.com/zephyrproject-rtos/zephyr/issues/20866) - [Coverity CID :205795] Integer handling issues in subsys/fs/nvs/nvs.c
- [GitHub #20846](https://github.com/zephyrproject-rtos/zephyr/issues/20846) - [Coverity CID :205775] Memory - corruptions in samples/net/sockets/big\_http\_download/src/big\_http\_download.c
- [GitHub #20845](https://github.com/zephyrproject-rtos/zephyr/issues/20845) - [Coverity CID :205824] Memory - corruptions in samples/net/mqtt\_publisher/src/main.c
- [GitHub #20842](https://github.com/zephyrproject-rtos/zephyr/issues/20842) - [Coverity CID :205787] Memory - corruptions in drivers/usb/device/usb\_dc\_native\_posix\_adapt.c
- [GitHub #20841](https://github.com/zephyrproject-rtos/zephyr/issues/20841) - [Coverity CID :205839] Error handling issues in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20840](https://github.com/zephyrproject-rtos/zephyr/issues/20840) - [Coverity CID :205821] Error handling issues in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20839](https://github.com/zephyrproject-rtos/zephyr/issues/20839) - [Coverity CID :205813] Error handling issues in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20838](https://github.com/zephyrproject-rtos/zephyr/issues/20838) - [Coverity CID :205790] Null pointer dereferences in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20837](https://github.com/zephyrproject-rtos/zephyr/issues/20837) - [Coverity CID :205777] Error handling issues in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20836](https://github.com/zephyrproject-rtos/zephyr/issues/20836) - [Coverity CID :205776] Error handling issues in drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #20834](https://github.com/zephyrproject-rtos/zephyr/issues/20834) - [Coverity CID :205825] API usage errors in boards/posix/native\_posix/hw\_models\_top.c
- [GitHub #20833](https://github.com/zephyrproject-rtos/zephyr/issues/20833) - Bluetooth: Deadlock in Host API from SMP callbacks.
- [GitHub #20826](https://github.com/zephyrproject-rtos/zephyr/issues/20826) - [Coverity CID :205798] API usage errors in boards/posix/native\_posix/hw\_models\_top.c
- [GitHub #20811](https://github.com/zephyrproject-rtos/zephyr/issues/20811) - spi driver
- [GitHub #20804](https://github.com/zephyrproject-rtos/zephyr/issues/20804) - sanitycheck: unimplemented documented option
- [GitHub #20800](https://github.com/zephyrproject-rtos/zephyr/issues/20800) - Ready thread is not swapped in after being woken up in IRQ
- [GitHub #20797](https://github.com/zephyrproject-rtos/zephyr/issues/20797) - echo server qemu\_x86 e1000 crash when coverage is enabled
- [GitHub #20781](https://github.com/zephyrproject-rtos/zephyr/issues/20781) - peripheral\_hr on VEGABoard disconnects from central\_hr after BT\_CONN\_PARAM\_UPDATE\_TIMEOUT
- [GitHub #20771](https://github.com/zephyrproject-rtos/zephyr/issues/20771) - onoff\_level\_lighting\_vnd\_app mcumgr unable to connect to provisioned node
- [GitHub #20769](https://github.com/zephyrproject-rtos/zephyr/issues/20769) - nucleo\_g431rb: Settings subsystem fails to initialise
- [GitHub #20743](https://github.com/zephyrproject-rtos/zephyr/issues/20743) - doc: settings.rst has references to mynewt structures
- [GitHub #20741](https://github.com/zephyrproject-rtos/zephyr/issues/20741) - Reel board Ethernet Support using the Link board ETH
- [GitHub #20735](https://github.com/zephyrproject-rtos/zephyr/issues/20735) - Cannot flash with jlink on windows.
- [GitHub #20726](https://github.com/zephyrproject-rtos/zephyr/issues/20726) - arm: Specifying sp register in asm’s clobber list is deprecated in GCC 9
- [GitHub #20715](https://github.com/zephyrproject-rtos/zephyr/issues/20715) - rtc driver may interrupt in a short time for large timeouts on cc13x2/cc26x2
- [GitHub #20707](https://github.com/zephyrproject-rtos/zephyr/issues/20707) - Define GATT service at run-time
- [GitHub #20695](https://github.com/zephyrproject-rtos/zephyr/issues/20695) - nRF5340: misc fixes for nRF53 porting
- [GitHub #20692](https://github.com/zephyrproject-rtos/zephyr/issues/20692) - samples: CAN: kconfig: CONFIG\_CAN\_AUTO\_BOFF\_RECOVERY does not exist
- [GitHub #20681](https://github.com/zephyrproject-rtos/zephyr/issues/20681) - samples: sensor: lps22hb: Reference to undefined CONFIG\_LPS22HB\_TRIGGER symbol
- [GitHub #20666](https://github.com/zephyrproject-rtos/zephyr/issues/20666) - Unexpected UART Kconfig warnings during build
- [GitHub #20660](https://github.com/zephyrproject-rtos/zephyr/issues/20660) - Bluetooth: host: bt\_conn\_create\_le sometimes fails to stop pre-scan before connecting
- [GitHub #20658](https://github.com/zephyrproject-rtos/zephyr/issues/20658) - The misc-flasher runner is not usable
- [GitHub #20651](https://github.com/zephyrproject-rtos/zephyr/issues/20651) - Bluetooth: disable and restart BT functionality
- [GitHub #20639](https://github.com/zephyrproject-rtos/zephyr/issues/20639) - x\_nucleo\_iks01a3 sample is not working anymore after #20560 has been merged
- [GitHub #20621](https://github.com/zephyrproject-rtos/zephyr/issues/20621) - Invalid baudrate on stm32 usart
- [GitHub #20620](https://github.com/zephyrproject-rtos/zephyr/issues/20620) - Advertiser seen alternating between RPA an ID address with privacy enabled
- [GitHub #20613](https://github.com/zephyrproject-rtos/zephyr/issues/20613) - HCI reset command complete before LL reset done
- [GitHub #20603](https://github.com/zephyrproject-rtos/zephyr/issues/20603) - tests/kernel/critical failed on sam\_e70\_xplained board in v.1.14-branch
- [GitHub #20598](https://github.com/zephyrproject-rtos/zephyr/issues/20598) - tests/lib/mem\_alloc newlibnano target run time error
- [GitHub #20587](https://github.com/zephyrproject-rtos/zephyr/issues/20587) - undefined reference when enabling CONFIG\_STACK\_CANARIES
- [GitHub #20582](https://github.com/zephyrproject-rtos/zephyr/issues/20582) - samples/subsys/logging/syst is broken when building with gcc-arm-none-eabi-7-2018-q2-update
- [GitHub #20571](https://github.com/zephyrproject-rtos/zephyr/issues/20571) - devicetree: fix non-deterministic multi-level interrupt encodings
- [GitHub #20558](https://github.com/zephyrproject-rtos/zephyr/issues/20558) - Build failure for samples/bluetooth/peripheral\_hr/sample.bluetooth.peripheral\_hr\_rv32m1\_vega\_ri5cy on rv32m1\_vega\_ri5cy
- [GitHub #20545](https://github.com/zephyrproject-rtos/zephyr/issues/20545) - imgtool: signing image fails: missing DT\_FLASH\_WRITE\_BLOCK\_SIZE
- [GitHub #20540](https://github.com/zephyrproject-rtos/zephyr/issues/20540) - [Coverity CID :205656]Error handling issues in /tests/net/tcp/src/main.c
- [GitHub #20539](https://github.com/zephyrproject-rtos/zephyr/issues/20539) - [Coverity CID :205637]Resource leaks in /tests/net/socket/tcp/src/main.c
- [GitHub #20538](https://github.com/zephyrproject-rtos/zephyr/issues/20538) - [Coverity CID :205673]Memory - corruptions in /tests/net/ppp/driver/src/main.c
- [GitHub #20536](https://github.com/zephyrproject-rtos/zephyr/issues/20536) - [Coverity CID :205607]Memory - corruptions in /tests/net/ppp/driver/src/main.c
- [GitHub #20535](https://github.com/zephyrproject-rtos/zephyr/issues/20535) - [Coverity CID :205619]Null pointer dereferences in /tests/net/ieee802154/fragment/src/main.c
- [GitHub #20534](https://github.com/zephyrproject-rtos/zephyr/issues/20534) - [Coverity CID :205669]Incorrect expression in /tests/kernel/mem\_protect/stack\_random/src/main.c
- [GitHub #20533](https://github.com/zephyrproject-rtos/zephyr/issues/20533) - [Coverity CID :205667]Error handling issues in /tests/drivers/counter/counter\_basic\_api/src/test\_counter.c
- [GitHub #20530](https://github.com/zephyrproject-rtos/zephyr/issues/20530) - [Coverity CID :205663]Memory - corruptions in /tests/crypto/tinycrypt/src/sha256.c
- [GitHub #20515](https://github.com/zephyrproject-rtos/zephyr/issues/20515) - [Coverity CID :205670]Code maintainability issues in /subsys/settings/src/settings\_nvs.c
- [GitHub #20514](https://github.com/zephyrproject-rtos/zephyr/issues/20514) - [Coverity CID :205633]Memory - illegal accesses in /subsys/settings/src/settings.c
- [GitHub #20513](https://github.com/zephyrproject-rtos/zephyr/issues/20513) - [Coverity CID :205621]Memory - illegal accesses in /subsys/net/lib/websocket/websocket.c
- [GitHub #20512](https://github.com/zephyrproject-rtos/zephyr/issues/20512) - [Coverity CID :143683]Error handling issues in /subsys/fs/fcb/fcb.c
- [GitHub #20511](https://github.com/zephyrproject-rtos/zephyr/issues/20511) - [Coverity CID :205612]Control flow issues in /subsys/disk/disk\_access\_spi\_sdhc.c
- [GitHub #20510](https://github.com/zephyrproject-rtos/zephyr/issues/20510) - [Coverity CID :205660]Incorrect expression in /subsys/debug/tracing/ctf/ctf\_top.c
- [GitHub #20509](https://github.com/zephyrproject-rtos/zephyr/issues/20509) - [Coverity CID :205632]Incorrect expression in /subsys/debug/tracing/ctf/ctf\_top.c
- [GitHub #20508](https://github.com/zephyrproject-rtos/zephyr/issues/20508) - [Coverity CID :205634]Code maintainability issues in /samples/net/sockets/websocket\_client/src/main.c
- [GitHub #20507](https://github.com/zephyrproject-rtos/zephyr/issues/20507) - [Coverity CID :205662]Memory - illegal accesses in /samples/net/sockets/dumb\_http\_server\_mt/src/main.c
- [GitHub #20506](https://github.com/zephyrproject-rtos/zephyr/issues/20506) - [Coverity CID :205672]Null pointer dereferences in /samples/drivers/espi/src/main.c
- [GitHub #20505](https://github.com/zephyrproject-rtos/zephyr/issues/20505) - [Coverity CID :205613]Null pointer dereferences in /samples/drivers/espi/src/main.c
- [GitHub #20504](https://github.com/zephyrproject-rtos/zephyr/issues/20504) - [Coverity CID :205661]Incorrect expression in /drivers/watchdog/wdt\_wwdg\_stm32.c
- [GitHub #20503](https://github.com/zephyrproject-rtos/zephyr/issues/20503) - [Coverity CID :205655]Error handling issues in /drivers/watchdog/wdt\_wwdg\_stm32.c
- [GitHub #20502](https://github.com/zephyrproject-rtos/zephyr/issues/20502) - [Coverity CID :205665]Integer handling issues in /drivers/video/mt9m114.c
- [GitHub #20501](https://github.com/zephyrproject-rtos/zephyr/issues/20501) - [Coverity CID :205643]Integer handling issues in /drivers/video/mt9m114.c
- [GitHub #20499](https://github.com/zephyrproject-rtos/zephyr/issues/20499) - [Coverity CID :205625]Error handling issues in /drivers/sensor/lsm6dso/lsm6dso\_shub.c
- [GitHub #20498](https://github.com/zephyrproject-rtos/zephyr/issues/20498) - [Coverity CID :205628]Error handling issues in /drivers/sensor/amg88xx/amg88xx\_trigger.c
- [GitHub #20496](https://github.com/zephyrproject-rtos/zephyr/issues/20496) - [Coverity CID :205630]Memory - illegal accesses in /drivers/pwm/pwm\_mchp\_xec.c
- [GitHub #20495](https://github.com/zephyrproject-rtos/zephyr/issues/20495) - [Coverity CID :205622]Memory - illegal accesses in /drivers/pwm/pwm\_mchp\_xec.c
- [GitHub #20494](https://github.com/zephyrproject-rtos/zephyr/issues/20494) - [Coverity CID :205617]Memory - corruptions in /drivers/kscan/kscan\_mchp\_xec.c
- [GitHub #20493](https://github.com/zephyrproject-rtos/zephyr/issues/20493) - [Coverity CID :205668]Insecure data handling in /drivers/ethernet/eth\_enc424j600.c
- [GitHub #20489](https://github.com/zephyrproject-rtos/zephyr/issues/20489) - [Coverity CID :205645]Integer handling issues in /drivers/counter/counter\_mchp\_xec.c
- [GitHub #20488](https://github.com/zephyrproject-rtos/zephyr/issues/20488) - [Coverity CID :205614]Integer handling issues in /drivers/clock\_control/nrf\_clock\_calibration.c
- [GitHub #20487](https://github.com/zephyrproject-rtos/zephyr/issues/20487) - [Coverity CID :205648]Memory - corruptions in /arch/arc/core/mpu/arc\_mpu\_v3\_internal.h
- [GitHub #20480](https://github.com/zephyrproject-rtos/zephyr/issues/20480) - i2c driver for cc13xx/cc26xx is configured with incorrect frequency
- [GitHub #20472](https://github.com/zephyrproject-rtos/zephyr/issues/20472) - drivers/flash: nRF flash driver uses absolute addressing instead of relative
- [GitHub #20450](https://github.com/zephyrproject-rtos/zephyr/issues/20450) - Bluetooth: hci\_uart: conn param update request from peripheral ignored
- [GitHub #20449](https://github.com/zephyrproject-rtos/zephyr/issues/20449) - ‘west flash’ command failed on sam\_e70\_xplained board.
- [GitHub #20445](https://github.com/zephyrproject-rtos/zephyr/issues/20445) - tests/kernel/critical failed on mimxrt1050\_evk board.
- [GitHub #20444](https://github.com/zephyrproject-rtos/zephyr/issues/20444) - sanitycheck error with tests/arch/x86/info.
- [GitHub #20438](https://github.com/zephyrproject-rtos/zephyr/issues/20438) - Kernel timeout API does not document well accepted values
- [GitHub #20431](https://github.com/zephyrproject-rtos/zephyr/issues/20431) - sockets\_tls: missing sendmsg
- [GitHub #20425](https://github.com/zephyrproject-rtos/zephyr/issues/20425) - storage/flash\_map: flash\_area\_get\_sectors can’t fetch sectors on devices with non-zero flash base address
- [GitHub #20423](https://github.com/zephyrproject-rtos/zephyr/issues/20423) - drivers/flash: flash\_get\_page\_info\_by\_off uses relative addresses
- [GitHub #20422](https://github.com/zephyrproject-rtos/zephyr/issues/20422) - Device with bonds should not accept new keys without user awareness
- [GitHub #20417](https://github.com/zephyrproject-rtos/zephyr/issues/20417) - BME280 wrong pressure unit?
- [GitHub #20416](https://github.com/zephyrproject-rtos/zephyr/issues/20416) - sample: sensor: fxos8700 issues
- [GitHub #20406](https://github.com/zephyrproject-rtos/zephyr/issues/20406) - misc.app\_dev.libcxx test fails to build for qemu\_x86\_64
- [GitHub #20371](https://github.com/zephyrproject-rtos/zephyr/issues/20371) - Sanitycheck filtering broken
- [GitHub #20351](https://github.com/zephyrproject-rtos/zephyr/issues/20351) - sample vl53l0x fails on disco\_l475\_iot1
- [GitHub #20332](https://github.com/zephyrproject-rtos/zephyr/issues/20332) - Nordic: DocLib links are obsolete
- [GitHub #20325](https://github.com/zephyrproject-rtos/zephyr/issues/20325) - samples/drivers/i2c\_scanner does not work on STM32 NUCLEO and DISCOVERY boards
- [GitHub #20313](https://github.com/zephyrproject-rtos/zephyr/issues/20313) - Zperf documentation points to wrong iPerf varsion
- [GitHub #20310](https://github.com/zephyrproject-rtos/zephyr/issues/20310) - SDHC : Could not enable SPI clock on nucleo\_f091rc
- [GitHub #20299](https://github.com/zephyrproject-rtos/zephyr/issues/20299) - bluetooth: host: Connection not being unreferenced when using CCC match callback
- [GitHub #20297](https://github.com/zephyrproject-rtos/zephyr/issues/20297) - Bluetooth: can’t close bt\_driver log output
- [GitHub #20285](https://github.com/zephyrproject-rtos/zephyr/issues/20285) - ST lis2dh sample with motion callback
- [GitHub #20284](https://github.com/zephyrproject-rtos/zephyr/issues/20284) - zephyr-env.sh Is this supposed to be unsetopt posixargzero ?
- [GitHub #20274](https://github.com/zephyrproject-rtos/zephyr/issues/20274) - Kconfig new libc changes cause echo server cmake error
- [GitHub #20260](https://github.com/zephyrproject-rtos/zephyr/issues/20260) - logging system call
- [GitHub #20255](https://github.com/zephyrproject-rtos/zephyr/issues/20255) - Meta-IRQs making cooperative threads preemptive
- [GitHub #20250](https://github.com/zephyrproject-rtos/zephyr/issues/20250) - hci\_usb: scanning crashes controller if a lot of devices are nearby
- [GitHub #20246](https://github.com/zephyrproject-rtos/zephyr/issues/20246) - Module Request: hal\_unisoc
- [GitHub #20245](https://github.com/zephyrproject-rtos/zephyr/issues/20245) - HTTP parser error with chunked transfer encoding
- [GitHub #20244](https://github.com/zephyrproject-rtos/zephyr/issues/20244) - mesh: demo: BT fails it init
- [GitHub #20232](https://github.com/zephyrproject-rtos/zephyr/issues/20232) - Bluetooth: Kernel panic on gatt discover in shell app
- [GitHub #20225](https://github.com/zephyrproject-rtos/zephyr/issues/20225) - [TOPIC-GPIO] sam\_e70\_xplained fails 2-pin active-low pull test
- [GitHub #20224](https://github.com/zephyrproject-rtos/zephyr/issues/20224) - [TOPIC-GPIO] rv32m1\_vega\_ri5cy fails 2-pin double-edge detection test
- [GitHub #20223](https://github.com/zephyrproject-rtos/zephyr/issues/20223) - [TOPIC-GPIO] efr32mg\_sltb004a fails 2-pin double-edge detection test
- [GitHub #20205](https://github.com/zephyrproject-rtos/zephyr/issues/20205) - ztest testing.ztest does not have a prj.conf with CONFIG\_ZTEST=y
- [GitHub #20202](https://github.com/zephyrproject-rtos/zephyr/issues/20202) - tests/arch/arm/arm\_interrupt failed on sam\_e70\_xplained board.
- [GitHub #20177](https://github.com/zephyrproject-rtos/zephyr/issues/20177) - sanitycheck error with tests/benchmarks/timing\_info.
- [GitHub #20176](https://github.com/zephyrproject-rtos/zephyr/issues/20176) - tests/drivers/pwm/pwm\_api failed on reel\_board.
- [GitHub #20167](https://github.com/zephyrproject-rtos/zephyr/issues/20167) - posix clock: unexpected value for CLOCK\_REALTIME when used with newlib
- [GitHub #20163](https://github.com/zephyrproject-rtos/zephyr/issues/20163) - doc: storage settings not clear
- [GitHub #20135](https://github.com/zephyrproject-rtos/zephyr/issues/20135) - Bluetooth: controller: split: Missing initialization of master terminate\_ack flag
- [GitHub #20122](https://github.com/zephyrproject-rtos/zephyr/issues/20122) - Deadlock in ASAN leak detection on exit
- [GitHub #20110](https://github.com/zephyrproject-rtos/zephyr/issues/20110) - Crash in hci\_driver.c when create\_connection\_cancel is issued after create connection
- [GitHub #20109](https://github.com/zephyrproject-rtos/zephyr/issues/20109) - altera\_nios2 support decision required
- [GitHub #20105](https://github.com/zephyrproject-rtos/zephyr/issues/20105) - tests/subsys/fs/fcb/ Using uninitialised memory/variables
- [GitHub #20104](https://github.com/zephyrproject-rtos/zephyr/issues/20104) - Kconfig is too slow
- [GitHub #20100](https://github.com/zephyrproject-rtos/zephyr/issues/20100) - Slave PTP clock time is updated with large value when Master PTP Clock time has changed
- [GitHub #20088](https://github.com/zephyrproject-rtos/zephyr/issues/20088) - tests/net/icmpv6/ failed on mimxrt1050\_evk board.
- [GitHub #20086](https://github.com/zephyrproject-rtos/zephyr/issues/20086) - Broken-looking duplicated ESPI\_XEC symbol
- [GitHub #20072](https://github.com/zephyrproject-rtos/zephyr/issues/20072) - Incompatible pointer types in Nordic Driver nrfx\_usbd.h
- [GitHub #20071](https://github.com/zephyrproject-rtos/zephyr/issues/20071) - Incompatible pointer types in Nordic Driver
- [GitHub #20049](https://github.com/zephyrproject-rtos/zephyr/issues/20049) - Build warnings in several unit tests
- [GitHub #20045](https://github.com/zephyrproject-rtos/zephyr/issues/20045) - z\_sched\_abort: sched\_spinlock should be released before k\_busy\_wait
- [GitHub #20042](https://github.com/zephyrproject-rtos/zephyr/issues/20042) - Telnet can connect only once
- [GitHub #20033](https://github.com/zephyrproject-rtos/zephyr/issues/20033) - Thread suspend only works if followed by k\_sleep in thread that is performing the suspension
- [GitHub #20032](https://github.com/zephyrproject-rtos/zephyr/issues/20032) - Make it clear in HTML docs what monospaced text is a link
- [GitHub #20030](https://github.com/zephyrproject-rtos/zephyr/issues/20030) - stm32 can: zcan\_frame from fifo uninitialized
- [GitHub #20022](https://github.com/zephyrproject-rtos/zephyr/issues/20022) - sanitycheck is not failing on build warnings
- [GitHub #20021](https://github.com/zephyrproject-rtos/zephyr/issues/20021) - Add a module to Zephyr to include TF-M project and it’s related repos
- [GitHub #20016](https://github.com/zephyrproject-rtos/zephyr/issues/20016) - STM32F4: cannot erase sectors from bank2
- [GitHub #20010](https://github.com/zephyrproject-rtos/zephyr/issues/20010) - Cannot flash mimxrt1050\_evk board
- [GitHub #20007](https://github.com/zephyrproject-rtos/zephyr/issues/20007) - tests/net/mld failed on mimxrt1050\_evk board.
- [GitHub #20000](https://github.com/zephyrproject-rtos/zephyr/issues/20000) - Invalid callback parameters in drivers/serial/uart\_nrfx\_uarte.c (using async API)
- [GitHub #19969](https://github.com/zephyrproject-rtos/zephyr/issues/19969) - [TOPIC-GPIO] mcux driver problems with pull configuration
- [GitHub #19963](https://github.com/zephyrproject-rtos/zephyr/issues/19963) - settings test tests/subsys/settings/fcb/raw failing
- [GitHub #19918](https://github.com/zephyrproject-rtos/zephyr/issues/19918) - Incremental builds broken for OpenAMP sample
- [GitHub #19917](https://github.com/zephyrproject-rtos/zephyr/issues/19917) - Bluetooth: Controller: Missing LL\_ENC\_RSP after HCI LTK Negative Reply
- [GitHub #19915](https://github.com/zephyrproject-rtos/zephyr/issues/19915) - tests/net/icmpv6 failed on sam\_e70 board.
- [GitHub #19914](https://github.com/zephyrproject-rtos/zephyr/issues/19914) - tests/net/shell failed on sam\_e70 board.
- [GitHub #19910](https://github.com/zephyrproject-rtos/zephyr/issues/19910) - Bluetooth: Mesh: Thread stack can reduce by use malloc&free function
- [GitHub #19898](https://github.com/zephyrproject-rtos/zephyr/issues/19898) - CONFIG\_NET\_ROUTE\_MCAST and CONFIG\_NET\_ROUTING can’t be enabled
- [GitHub #19889](https://github.com/zephyrproject-rtos/zephyr/issues/19889) - Buffer leak in GATT for Write Without Response and Notifications
- [GitHub #19885](https://github.com/zephyrproject-rtos/zephyr/issues/19885) - SMP doesn’t work on ARC any longer
- [GitHub #19877](https://github.com/zephyrproject-rtos/zephyr/issues/19877) - Broken partition size
- [GitHub #19872](https://github.com/zephyrproject-rtos/zephyr/issues/19872) - sensor/lis2dh: using runtime scale other than 2g generates strange values
- [GitHub #19871](https://github.com/zephyrproject-rtos/zephyr/issues/19871) - display/ssd1306: allow “reverse display” in kconfig or dts
- [GitHub #19867](https://github.com/zephyrproject-rtos/zephyr/issues/19867) - modem: ublox-sara-r4/u2 build error
- [GitHub #19848](https://github.com/zephyrproject-rtos/zephyr/issues/19848) - stm32wb MPU failure
- [GitHub #19841](https://github.com/zephyrproject-rtos/zephyr/issues/19841) - MIPI Sys-T logging/tracing support
- [GitHub #19837](https://github.com/zephyrproject-rtos/zephyr/issues/19837) - SS register is 0 when taking exceptions on qemu\_x86\_long
- [GitHub #19833](https://github.com/zephyrproject-rtos/zephyr/issues/19833) - missing or empty reg/ranges property when trying to build blink\_led example
- [GitHub #19820](https://github.com/zephyrproject-rtos/zephyr/issues/19820) - Bluetooth: Host: Unable to use whitelist in peripheral only build
- [GitHub #19818](https://github.com/zephyrproject-rtos/zephyr/issues/19818) - Compiler error for counter example (nRF52\_pca10040)
- [GitHub #19811](https://github.com/zephyrproject-rtos/zephyr/issues/19811) - native\_posix stack smashing
- [GitHub #19802](https://github.com/zephyrproject-rtos/zephyr/issues/19802) - Zephyr was unable to find the toolchain after update to zephyr version 1.13.0
- [GitHub #19795](https://github.com/zephyrproject-rtos/zephyr/issues/19795) - bt\_gatt\_attr\_next returns first attribute in table for attributes with static storage.
- [GitHub #19791](https://github.com/zephyrproject-rtos/zephyr/issues/19791) - How to use CMSIS DSP Library on nRF52832 running zephyr LTS Version(V1.14) ?
- [GitHub #19783](https://github.com/zephyrproject-rtos/zephyr/issues/19783) - floating point in C++ on x86\_64 uses SSE
- [GitHub #19775](https://github.com/zephyrproject-rtos/zephyr/issues/19775) - net\_calc\_chksum: Use of un-initialized memory on 64 bit targets
- [GitHub #19769](https://github.com/zephyrproject-rtos/zephyr/issues/19769) - CONFIG\_FLASH\_SIZE should be CONFIG\_FLASH\_END and specified in hex
- [GitHub #19767](https://github.com/zephyrproject-rtos/zephyr/issues/19767) - Bluetooth: Mesh: Provision Random buffer has too small size
- [GitHub #19762](https://github.com/zephyrproject-rtos/zephyr/issues/19762) - tests/net/lib/tls\_credentials failed on sam\_e70\_xplained board.
- [GitHub #19759](https://github.com/zephyrproject-rtos/zephyr/issues/19759) - z\_arch\_switch() passed pointer to NULL outgoing switch handle on dummy thread context switch
- [GitHub #19748](https://github.com/zephyrproject-rtos/zephyr/issues/19748) - k\_sleep(K\_FOREVER) behavior unexpected
- [GitHub #19734](https://github.com/zephyrproject-rtos/zephyr/issues/19734) - “make gdbserver” doesn’t work properly for qemu\_x86\_long
- [GitHub #19724](https://github.com/zephyrproject-rtos/zephyr/issues/19724) - Bluetooth: Mesh: Receiving an access message
- [GitHub #19722](https://github.com/zephyrproject-rtos/zephyr/issues/19722) - Settings: settings\_file\_save\_priv() use of uninitialized variable
- [GitHub #19721](https://github.com/zephyrproject-rtos/zephyr/issues/19721) - samples/bluetooth/ipsp does not respond to pings from Linux
- [GitHub #19717](https://github.com/zephyrproject-rtos/zephyr/issues/19717) - Add provisions for supporting multiple CMSIS variants
- [GitHub #19701](https://github.com/zephyrproject-rtos/zephyr/issues/19701) - mem\_pool\_threadsafe sporadic failures impacting CI
- [GitHub #19700](https://github.com/zephyrproject-rtos/zephyr/issues/19700) - nrfx\_uart RX hang on errors
- [GitHub #19697](https://github.com/zephyrproject-rtos/zephyr/issues/19697) - tests/subsys/fs/fat\_fs\_api uses unitialized variables
- [GitHub #19692](https://github.com/zephyrproject-rtos/zephyr/issues/19692) - [TOPIC-GPIO] gpi\_api\_1pin test failures
- [GitHub #19685](https://github.com/zephyrproject-rtos/zephyr/issues/19685) - Samples: BluetoothMesh: not able to connect with device over GATT to provision it
- [GitHub #19683](https://github.com/zephyrproject-rtos/zephyr/issues/19683) - nrf: clock reimplementation breaks test
- [GitHub #19678](https://github.com/zephyrproject-rtos/zephyr/issues/19678) - Noticeable delay between processing multiple client connection requests (200ms+)
- [GitHub #19660](https://github.com/zephyrproject-rtos/zephyr/issues/19660) - missing file reference in samples/sensor/ti\_hdc doc
- [GitHub #19649](https://github.com/zephyrproject-rtos/zephyr/issues/19649) - [TOPIC-GPIO]: Replace GPIO\_INT\_DEBOUNCE with GPIO\_DEBOUNCE
- [GitHub #19638](https://github.com/zephyrproject-rtos/zephyr/issues/19638) - Bluetooth: Mesh: Provisioning Over PB-ADV
- [GitHub #19629](https://github.com/zephyrproject-rtos/zephyr/issues/19629) - tinycbor buffer overflow causing mcumgr image upload failure
- [GitHub #19612](https://github.com/zephyrproject-rtos/zephyr/issues/19612) - ICMPv6 packet is routed to wrong interface when peer is not found in neighbor cache
- [GitHub #19604](https://github.com/zephyrproject-rtos/zephyr/issues/19604) - Bluetooth: ATT does not release all buffers on disconnect
- [GitHub #19603](https://github.com/zephyrproject-rtos/zephyr/issues/19603) - addition to winbond,w25q16.yaml required for SPI CS to be controlled by driver
- [GitHub #19599](https://github.com/zephyrproject-rtos/zephyr/issues/19599) - ARC builds missing z\_arch\_start\_cpu() when !SMP
- [GitHub #19592](https://github.com/zephyrproject-rtos/zephyr/issues/19592) - Request new repository to host the Eclipse plugin for building Zephyr applications
- [GitHub #19569](https://github.com/zephyrproject-rtos/zephyr/issues/19569) - nRF RTC Counter with compile time decision about support of custom top value
- [GitHub #19560](https://github.com/zephyrproject-rtos/zephyr/issues/19560) - Console on CDC USB crashes when CONFIG\_USB\_COMPOSITE\_DEVICE=y
- [GitHub #19552](https://github.com/zephyrproject-rtos/zephyr/issues/19552) - [TOPIC-GPIO]: Support for legacy interrupt configuration breaks new API contract
- [GitHub #19550](https://github.com/zephyrproject-rtos/zephyr/issues/19550) - drivers/pcie: `pcie\_get\_mbar()` should return a `void \*` not `u32\_t`
- [GitHub #19549](https://github.com/zephyrproject-rtos/zephyr/issues/19549) - kernel/mem\_protection/stackprot fails on NXP RT series platforms on v1.14.1-rc3 release
- [GitHub #19544](https://github.com/zephyrproject-rtos/zephyr/issues/19544) - make usb power settings in “Configuration Descriptor” setable
- [GitHub #19543](https://github.com/zephyrproject-rtos/zephyr/issues/19543) - net: tcp: echo server stops if CONFIG\_POSIX\_MAX\_FDS is not set
- [GitHub #19539](https://github.com/zephyrproject-rtos/zephyr/issues/19539) - Support MQTT over Websocket
- [GitHub #19537](https://github.com/zephyrproject-rtos/zephyr/issues/19537) - debug:object\_tracing: The trace list is not complete once we initialize the object on the trace list
- [GitHub #19536](https://github.com/zephyrproject-rtos/zephyr/issues/19536) - devicetree bindings path misinterpreted
- [GitHub #19535](https://github.com/zephyrproject-rtos/zephyr/issues/19535) - Doubly freed memory in the pipe\_api test
- [GitHub #19525](https://github.com/zephyrproject-rtos/zephyr/issues/19525) - Can’t change the slave latency on a connection.
- [GitHub #19515](https://github.com/zephyrproject-rtos/zephyr/issues/19515) - Bluetooth: Controller: assertion failed
- [GitHub #19509](https://github.com/zephyrproject-rtos/zephyr/issues/19509) - Bluetooth: stm32wb55: Unable to pair with privacy-enabled peer
- [GitHub #19490](https://github.com/zephyrproject-rtos/zephyr/issues/19490) - Bluetooth: split: ‘e’ assert during disconnect
- [GitHub #19484](https://github.com/zephyrproject-rtos/zephyr/issues/19484) - Bluetooth: split: bt\_set\_name() asserts due to flash and radio coex
- [GitHub #19472](https://github.com/zephyrproject-rtos/zephyr/issues/19472) - drivers: usb\_dc\_stm32: shows after some time errors and warnings
- [GitHub #19459](https://github.com/zephyrproject-rtos/zephyr/issues/19459) - Bluetooth: Mesh: Mesh Model State Binding.
- [GitHub #19456](https://github.com/zephyrproject-rtos/zephyr/issues/19456) - arch/x86: make use of z\_bss\_zero() and z\_data\_copy()
- [GitHub #19452](https://github.com/zephyrproject-rtos/zephyr/issues/19452) - Bluetooth: Mesh: Mesh model implementation?
- [GitHub #19447](https://github.com/zephyrproject-rtos/zephyr/issues/19447) - SEGGER\_RTT.h: No such file or directory
- [GitHub #19438](https://github.com/zephyrproject-rtos/zephyr/issues/19438) - boot flags incorrect after image swapping
- [GitHub #19437](https://github.com/zephyrproject-rtos/zephyr/issues/19437) - tests/kernel/sched/schedule\_api tests fail to build
- [GitHub #19432](https://github.com/zephyrproject-rtos/zephyr/issues/19432) - nrfx: nrf52840\_pca10056 SPIM1 cannot be selected without SPIM3
- [GitHub #19420](https://github.com/zephyrproject-rtos/zephyr/issues/19420) - power: system power management sleep duration
- [GitHub #19419](https://github.com/zephyrproject-rtos/zephyr/issues/19419) - Build automation and testing tools
- [GitHub #19415](https://github.com/zephyrproject-rtos/zephyr/issues/19415) - typo in nucleo\_l496zg.dts
- [GitHub #19413](https://github.com/zephyrproject-rtos/zephyr/issues/19413) - Not able to scan and connect to other ble devices with HCI commands
- [GitHub #19398](https://github.com/zephyrproject-rtos/zephyr/issues/19398) - net: ENC28J60 driver does not respond to ping
- [GitHub #19385](https://github.com/zephyrproject-rtos/zephyr/issues/19385) - compilation error
- [GitHub #19381](https://github.com/zephyrproject-rtos/zephyr/issues/19381) - `k\_yield()` exhibits different behavior with `CONFIG\_SMP`
- [GitHub #19376](https://github.com/zephyrproject-rtos/zephyr/issues/19376) - Build on a ARM host
- [GitHub #19374](https://github.com/zephyrproject-rtos/zephyr/issues/19374) - net: echo server: TCP add support for multiple connections
- [GitHub #19370](https://github.com/zephyrproject-rtos/zephyr/issues/19370) - bugs in kernel/atomic\_c
- [GitHub #19367](https://github.com/zephyrproject-rtos/zephyr/issues/19367) - net: TCP/IPv4: TCP stops working after dropping segment with incorrect checksum
- [GitHub #19363](https://github.com/zephyrproject-rtos/zephyr/issues/19363) - arc: bug in \_firq\_enter
- [GitHub #19353](https://github.com/zephyrproject-rtos/zephyr/issues/19353) - arch/x86: QEMU doesn’t appear to support x2APIC
- [GitHub #19347](https://github.com/zephyrproject-rtos/zephyr/issues/19347) - Bluetooth: BL654 USB dongle not found after flashing
- [GitHub #19342](https://github.com/zephyrproject-rtos/zephyr/issues/19342) - Bluetooth: Mesh: Persistent storage of Virtual Addresses
- [GitHub #19320](https://github.com/zephyrproject-rtos/zephyr/issues/19320) - build error using logger in test case
- [GitHub #19319](https://github.com/zephyrproject-rtos/zephyr/issues/19319) - tests/kernel/spinlock only runs on ESP32
- [GitHub #19317](https://github.com/zephyrproject-rtos/zephyr/issues/19317) - need a minimal log implementation that maps to printk()
- [GitHub #19307](https://github.com/zephyrproject-rtos/zephyr/issues/19307) - \_interrupt\_stack is defined in the kernel, but declared in arch headers
- [GitHub #19299](https://github.com/zephyrproject-rtos/zephyr/issues/19299) - kernel/spinlock: A SMP race condition in SPIN\_VALIDATE
- [GitHub #19284](https://github.com/zephyrproject-rtos/zephyr/issues/19284) - Service Changed indication not being sent in some cases
- [GitHub #19270](https://github.com/zephyrproject-rtos/zephyr/issues/19270) - GPIO: STM32: Migration to new API
- [GitHub #19267](https://github.com/zephyrproject-rtos/zephyr/issues/19267) - Service changed not notified upon reconnection.
- [GitHub #19265](https://github.com/zephyrproject-rtos/zephyr/issues/19265) - Bluetooth: Mesh: Friend Send model message to LPN
- [GitHub #19263](https://github.com/zephyrproject-rtos/zephyr/issues/19263) - Bluetooth: Mesh: Friend Clear Procedure Timeout
- [GitHub #19250](https://github.com/zephyrproject-rtos/zephyr/issues/19250) - NVS: Overwriting an item with a shorter matching item fails
- [GitHub #19239](https://github.com/zephyrproject-rtos/zephyr/issues/19239) - tests/kernel/common failed on iotdk board.
- [GitHub #19238](https://github.com/zephyrproject-rtos/zephyr/issues/19238) - tests/subsys/usb/device failed on reel\_board.
- [GitHub #19235](https://github.com/zephyrproject-rtos/zephyr/issues/19235) - move drivers/timer/apic\_timer.c to devicetree
- [GitHub #19231](https://github.com/zephyrproject-rtos/zephyr/issues/19231) - native\_posix\_64/tests/subsys/fs/fat\_fs\_api/filesystem.fat fails
- [GitHub #19227](https://github.com/zephyrproject-rtos/zephyr/issues/19227) - IOTDK uses QMSI DT binding
- [GitHub #19226](https://github.com/zephyrproject-rtos/zephyr/issues/19226) - Device Tree Enhancements in 2.1
- [GitHub #19219](https://github.com/zephyrproject-rtos/zephyr/issues/19219) - drivers/i2c/i2c\_dw.c is not 64-bit clean
- [GitHub #19216](https://github.com/zephyrproject-rtos/zephyr/issues/19216) - Ext library for WIN1500: different values of AF\_INET
- [GitHub #19198](https://github.com/zephyrproject-rtos/zephyr/issues/19198) - Bluetooth: LL split assert on connect
- [GitHub #19191](https://github.com/zephyrproject-rtos/zephyr/issues/19191) - problem with implementation of sock\_set\_flag
- [GitHub #19186](https://github.com/zephyrproject-rtos/zephyr/issues/19186) - BLE: Mesh: IVI Initiator When ivi in progress timeout
- [GitHub #19181](https://github.com/zephyrproject-rtos/zephyr/issues/19181) - sock\_set\_flag implementation in sock\_internal.h does not work for 64 bit pointers
- [GitHub #19178](https://github.com/zephyrproject-rtos/zephyr/issues/19178) - Segmentation fault when running echo server
- [GitHub #19177](https://github.com/zephyrproject-rtos/zephyr/issues/19177) - re-valuate commit 0951ce2
- [GitHub #19176](https://github.com/zephyrproject-rtos/zephyr/issues/19176) - NET: LLMNR: zephyr drops IPV4 LLMNR packets
- [GitHub #19167](https://github.com/zephyrproject-rtos/zephyr/issues/19167) - Message queues bug when using C++
- [GitHub #19165](https://github.com/zephyrproject-rtos/zephyr/issues/19165) - zephyr\_file generates bad links on branches
- [GitHub #19164](https://github.com/zephyrproject-rtos/zephyr/issues/19164) - compiling native\_posix64 with unistd.h & net/net\_ip.h fail
- [GitHub #19144](https://github.com/zephyrproject-rtos/zephyr/issues/19144) - arch/x86: CONFIG\_BOOT\_TIME\_MEASUREMENT broken
- [GitHub #19135](https://github.com/zephyrproject-rtos/zephyr/issues/19135) - net: ipv4: udp: echo server sends malformed data bytes in reply to broadcast packet
- [GitHub #19133](https://github.com/zephyrproject-rtos/zephyr/issues/19133) - Scheduler change in #17369 introduces crashes
- [GitHub #19103](https://github.com/zephyrproject-rtos/zephyr/issues/19103) - zsock\_accept\_ctx blocks even when O\_NONBLOCK is specified
- [GitHub #19098](https://github.com/zephyrproject-rtos/zephyr/issues/19098) - Failed to flash on ESP32
- [GitHub #19096](https://github.com/zephyrproject-rtos/zephyr/issues/19096) - No error thrown for device tree node with missing required property of type compound
- [GitHub #19079](https://github.com/zephyrproject-rtos/zephyr/issues/19079) - Enable shield sample on stm32mp157c\_dk2
- [GitHub #19078](https://github.com/zephyrproject-rtos/zephyr/issues/19078) - search for board specific shield overlays doesn’t always work
- [GitHub #19066](https://github.com/zephyrproject-rtos/zephyr/issues/19066) - Build error with qemu\_x86\_64
- [GitHub #19065](https://github.com/zephyrproject-rtos/zephyr/issues/19065) - Build error with stm32h747i\_disco\_m4
- [GitHub #19064](https://github.com/zephyrproject-rtos/zephyr/issues/19064) - Correct docs for K\_THREAD\_DEFINE
- [GitHub #19059](https://github.com/zephyrproject-rtos/zephyr/issues/19059) - i2c\_ll\_stm32\_v2: nack on write is not handled correctly
- [GitHub #19051](https://github.com/zephyrproject-rtos/zephyr/issues/19051) - [Zephyr v2.0.0 nrf52840] Unable to reconnect to recently bonded peripheral
- [GitHub #19039](https://github.com/zephyrproject-rtos/zephyr/issues/19039) - Bluetooth: Qualification test case GATT/SR/UNS/BI-02-C fails
- [GitHub #19038](https://github.com/zephyrproject-rtos/zephyr/issues/19038) - [zephyr branch 1.14 and master -stm32-netusb]:errors when i view RNDIS Device‘s properties on Windows 10
- [GitHub #19034](https://github.com/zephyrproject-rtos/zephyr/issues/19034) - sanitycheck fail with ninja option with single-core machine
- [GitHub #19031](https://github.com/zephyrproject-rtos/zephyr/issues/19031) - nrfx\_clock.c functions are not available with CONFIG\_NRFX\_CLOCK
- [GitHub #19015](https://github.com/zephyrproject-rtos/zephyr/issues/19015) - Bluetooth: Mesh: Node doesn’t respond to “All Proxies” address
- [GitHub #19013](https://github.com/zephyrproject-rtos/zephyr/issues/19013) - [Zephyr 1.14]: NetUsb and Ethernet work together
- [GitHub #19004](https://github.com/zephyrproject-rtos/zephyr/issues/19004) - problems in sanitycheck/CI infrastructure revealed by post-release change
- [GitHub #18999](https://github.com/zephyrproject-rtos/zephyr/issues/18999) - assignment in assert in test of arm\_thread\_arch causes build failures
- [GitHub #18990](https://github.com/zephyrproject-rtos/zephyr/issues/18990) - C++ New allocates memory from kernel heap
- [GitHub #18988](https://github.com/zephyrproject-rtos/zephyr/issues/18988) - BLE Central auto enables indications and notifies
- [GitHub #18986](https://github.com/zephyrproject-rtos/zephyr/issues/18986) - DTS: transition from alias to node label as the standard prefix
- [GitHub #18973](https://github.com/zephyrproject-rtos/zephyr/issues/18973) - z\_arch\_system\_halt() does not block interrupts
- [GitHub #18961](https://github.com/zephyrproject-rtos/zephyr/issues/18961) - [Coverity CID :203912]Error handling issues in /samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #18957](https://github.com/zephyrproject-rtos/zephyr/issues/18957) - NET\_L2: modem drivers (offloaded) aren’t assigned a net\_l2 which causes a crash in net\_if\_up()/net\_if\_down()
- [GitHub #18956](https://github.com/zephyrproject-rtos/zephyr/issues/18956) - memory protection for x86 dependent on XIP
- [GitHub #18935](https://github.com/zephyrproject-rtos/zephyr/issues/18935) - [Zephyr 1.14] drivers: flash: spi\_nor: Problematic write with page boundaries
- [GitHub #18880](https://github.com/zephyrproject-rtos/zephyr/issues/18880) - boards: mec15xxevb\_assy6853: consider moving ARCH\_HAS\_CUSTOM\_BUSY\_WAIT to SoC definition
- [GitHub #18873](https://github.com/zephyrproject-rtos/zephyr/issues/18873) - zsock\_socket() should support proto==0
- [GitHub #18870](https://github.com/zephyrproject-rtos/zephyr/issues/18870) - zsock\_getaddrinfo() returns garbage values if IPv4 address is passed and hints->ai\_family == AF\_INET6
- [GitHub #18858](https://github.com/zephyrproject-rtos/zephyr/issues/18858) - Runner support for stm32flash utility
- [GitHub #18832](https://github.com/zephyrproject-rtos/zephyr/issues/18832) - Doc: contact-us page should use slack invite (not zephyrproject.slack.com)
- [GitHub #18824](https://github.com/zephyrproject-rtos/zephyr/issues/18824) - tests/subsys/usb/device/ failed on sam\_e70 board.
- [GitHub #18816](https://github.com/zephyrproject-rtos/zephyr/issues/18816) - ssd1306 driver can’t work with lvgl
- [GitHub #18807](https://github.com/zephyrproject-rtos/zephyr/issues/18807) - Support the Ubuntu Cross Toolchain
- [GitHub #18803](https://github.com/zephyrproject-rtos/zephyr/issues/18803) - LTS - support time
- [GitHub #18787](https://github.com/zephyrproject-rtos/zephyr/issues/18787) - arch/x86: retire loapic\_timer.c driver in favor of new apic\_timer.c
- [GitHub #18749](https://github.com/zephyrproject-rtos/zephyr/issues/18749) - Avenger96 regressed in mainline for U-Boot M4 boot
- [GitHub #18695](https://github.com/zephyrproject-rtos/zephyr/issues/18695) - Watchdog: stm32: Wrong timeout value when watchdog started at boot
- [GitHub #18657](https://github.com/zephyrproject-rtos/zephyr/issues/18657) - drivers/timer/hpet.c should use devicetree, not CONFIG\_\* for MMIO/IRQ data
- [GitHub #18652](https://github.com/zephyrproject-rtos/zephyr/issues/18652) - Optimization flags from CMAKE\_BUILD\_TYPE are not taken into account
- [GitHub #18592](https://github.com/zephyrproject-rtos/zephyr/issues/18592) - (nRF51) The RSSI signal does not rise above -44 dBm
- [GitHub #18591](https://github.com/zephyrproject-rtos/zephyr/issues/18591) - tests/kernel/fifo/fifo\_timeout/kernel.fifo.timeout.poll fails to run on multiple ARM platforms
- [GitHub #18585](https://github.com/zephyrproject-rtos/zephyr/issues/18585) - STM32G4 support
- [GitHub #18583](https://github.com/zephyrproject-rtos/zephyr/issues/18583) - hci\_usb: NRF52840 connecting addtional peripheral fails
- [GitHub #18540](https://github.com/zephyrproject-rtos/zephyr/issues/18540) - MEC1501 ADC is missing in HAL
- [GitHub #18539](https://github.com/zephyrproject-rtos/zephyr/issues/18539) - MEC1501 PWM is missing in HAL
- [GitHub #18488](https://github.com/zephyrproject-rtos/zephyr/issues/18488) - Bluetooth: Mesh: Friend queue message seqnum order
- [GitHub #18480](https://github.com/zephyrproject-rtos/zephyr/issues/18480) - Microchip’s MEC1501 HAL is broken (watchdog part)
- [GitHub #18465](https://github.com/zephyrproject-rtos/zephyr/issues/18465) - timeutil\_timegm() has undefined behavior
- [GitHub #18451](https://github.com/zephyrproject-rtos/zephyr/issues/18451) - [Coverity CID :203528]Integer handling issues in /tests/lib/fdtable/src/main.c
- [GitHub #18449](https://github.com/zephyrproject-rtos/zephyr/issues/18449) - [Coverity CID :203458]Integer handling issues in /tests/lib/fdtable/src/main.c
- [GitHub #18450](https://github.com/zephyrproject-rtos/zephyr/issues/18450) - [Coverity CID :203505]Integer handling issues in /tests/lib/fdtable/src/main.c
- [GitHub #18448](https://github.com/zephyrproject-rtos/zephyr/issues/18448) - [Coverity CID :203429]Integer handling issues in /tests/lib/fdtable/src/main.c
- [GitHub #18440](https://github.com/zephyrproject-rtos/zephyr/issues/18440) - [Coverity CID :203439]Memory - corruptions in /tests/kernel/mem\_protect/protection/src/main.c
- [GitHub #18441](https://github.com/zephyrproject-rtos/zephyr/issues/18441) - [Coverity CID :203460]Memory - corruptions in /tests/kernel/mem\_protect/protection/src/main.c
- [GitHub #18373](https://github.com/zephyrproject-rtos/zephyr/issues/18373) - [Coverity CID :203399]API usage errors in /samples/boards/olimex\_stm32\_e407/ccm/src/main.c
- [GitHub #18341](https://github.com/zephyrproject-rtos/zephyr/issues/18341) - settings: test setting FS back-end using littlefs
- [GitHub #18340](https://github.com/zephyrproject-rtos/zephyr/issues/18340) - settings: make NVS the default backend
- [GitHub #18308](https://github.com/zephyrproject-rtos/zephyr/issues/18308) - net: TCP/IPv6 set of fragmented packets causes Zephyr to quit
- [GitHub #18305](https://github.com/zephyrproject-rtos/zephyr/issues/18305) - Native Posix target can not use features with newlib dependencies
- [GitHub #18297](https://github.com/zephyrproject-rtos/zephyr/issues/18297) - Bluetooth: SMP: Pairing issues
- [GitHub #18282](https://github.com/zephyrproject-rtos/zephyr/issues/18282) - tests/kernel/sched/schedule\_api/ fails on LPC54114\_m4
- [GitHub #18160](https://github.com/zephyrproject-rtos/zephyr/issues/18160) - Cleanup dts compatible for “nxp,kinetis-sim” on nxp\_ke1xf
- [GitHub #18143](https://github.com/zephyrproject-rtos/zephyr/issues/18143) - stm32f SPI Slave TX does not work correctly, but occurs OVERRUN err
- [GitHub #18138](https://github.com/zephyrproject-rtos/zephyr/issues/18138) - xtensa arch has two different implementations
- [GitHub #18105](https://github.com/zephyrproject-rtos/zephyr/issues/18105) - BSD socket offload with IPv4 and IPv6 disabled breaks many client-based net samples
- [GitHub #18031](https://github.com/zephyrproject-rtos/zephyr/issues/18031) - samples/shields/x\_nucleo\_iks01a3 test is stucking due to dca45cb commit
- [GitHub #17998](https://github.com/zephyrproject-rtos/zephyr/issues/17998) - STM32 (Nucleo L476RG) SPI pins floating
- [GitHub #17983](https://github.com/zephyrproject-rtos/zephyr/issues/17983) - Bluetooth: Re-establish security before notifications/indications can be sent
- [GitHub #17949](https://github.com/zephyrproject-rtos/zephyr/issues/17949) - stm32 i2c driver has problems with AHB\_PRESCALER, APB1\_PRESCALER, APB2\_PRESCALER
- [GitHub #17892](https://github.com/zephyrproject-rtos/zephyr/issues/17892) - arch/x86: clean up segmentation.h
- [GitHub #17888](https://github.com/zephyrproject-rtos/zephyr/issues/17888) - arch/x86: remove IAMCU ABI support
- [GitHub #17832](https://github.com/zephyrproject-rtos/zephyr/issues/17832) - x86: update mmustructs.h and x86\_mmu.c to support long mode
- [GitHub #17829](https://github.com/zephyrproject-rtos/zephyr/issues/17829) - support default property values in devicetree bindings
- [GitHub #17805](https://github.com/zephyrproject-rtos/zephyr/issues/17805) - [Zepyhr v1.14.0 and master] Unable to run commands of mcumgr tool over UART like reset
- [GitHub #17781](https://github.com/zephyrproject-rtos/zephyr/issues/17781) - Question:Is it possible to connect the device on internet using bluetooth connection?
- [GitHub #17645](https://github.com/zephyrproject-rtos/zephyr/issues/17645) - VSCode debugging Zephyr application
- [GitHub #17626](https://github.com/zephyrproject-rtos/zephyr/issues/17626) - Change sanitycheck to use ‘gcovr’ instead of ‘lcov’
- [GitHub #17625](https://github.com/zephyrproject-rtos/zephyr/issues/17625) - driver: gpio: PCAL9535A: can’t write to register (read is possible)
- [GitHub #17548](https://github.com/zephyrproject-rtos/zephyr/issues/17548) - Can’t set thread name with k\_thread\_create prevents useful tracing information
- [GitHub #17546](https://github.com/zephyrproject-rtos/zephyr/issues/17546) - Bluetooth: Central Scan fails continuously if last connect attempt failed to complete
- [GitHub #17454](https://github.com/zephyrproject-rtos/zephyr/issues/17454) - Bluetooth: Mesh: Add provisioner support
- [GitHub #17443](https://github.com/zephyrproject-rtos/zephyr/issues/17443) - Kconfig: move arch-specific stack sizes to arch trees?
- [GitHub #17430](https://github.com/zephyrproject-rtos/zephyr/issues/17430) - arch/x86: drivers/interrupt\_controller/system\_apic.c improperly classifies IRQs
- [GitHub #17361](https://github.com/zephyrproject-rtos/zephyr/issues/17361) - \_THREAD\_QUEUED overlaps with x86 \_EXC\_ACTIVE in k\_thread.thread\_state
- [GitHub #17337](https://github.com/zephyrproject-rtos/zephyr/issues/17337) - ArmV7-M mpu sub region alignment
- [GitHub #17239](https://github.com/zephyrproject-rtos/zephyr/issues/17239) - Too many open files crash when running “sanitycheck” with no arguments
- [GitHub #17234](https://github.com/zephyrproject-rtos/zephyr/issues/17234) - CONFIG\_KERNEL\_ENTRY appears to be superfluous
- [GitHub #17133](https://github.com/zephyrproject-rtos/zephyr/issues/17133) - arch/x86: x2APIC EOI should be inline
- [GitHub #17104](https://github.com/zephyrproject-rtos/zephyr/issues/17104) - arch/x86: fix -march flag for Apollo Lake
- [GitHub #17064](https://github.com/zephyrproject-rtos/zephyr/issues/17064) - drivers/serial/uart\_ns16550: CMD\_SET\_DLF should be removed
- [GitHub #17004](https://github.com/zephyrproject-rtos/zephyr/issues/17004) - arch/x86: build errors with newest build-grub.sh scripts
- [GitHub #16900](https://github.com/zephyrproject-rtos/zephyr/issues/16900) - Inline assembly in Arm z\_arch\_switch\_to\_main\_thread missing clobber list
- [GitHub #16880](https://github.com/zephyrproject-rtos/zephyr/issues/16880) - Systematic \*-zephyr-eabi/bin/ld: warning: toolchain\_is\_ok cannot find entry symbol \_start; defaulting to 000::00XXXXX
- [GitHub #16791](https://github.com/zephyrproject-rtos/zephyr/issues/16791) - build system does not see changes in DTS dependencies
- [GitHub #16723](https://github.com/zephyrproject-rtos/zephyr/issues/16723) - nrfx: uart: power management does not include CTS/RTS pins
- [GitHub #16721](https://github.com/zephyrproject-rtos/zephyr/issues/16721) - PCIe build warnings from devicetree
- [GitHub #16673](https://github.com/zephyrproject-rtos/zephyr/issues/16673) - usb\_dc\_stm32: If i remove the cable while writing, the program will freeze.
- [GitHub #16599](https://github.com/zephyrproject-rtos/zephyr/issues/16599) - drivers: usb\_dc\_nrfx: unstable handling of hosts suspend/resume
- [GitHub #16529](https://github.com/zephyrproject-rtos/zephyr/issues/16529) - LTS 1.14.0: sanitycheck: Cannot identify OOT boards and shields
- [GitHub #16452](https://github.com/zephyrproject-rtos/zephyr/issues/16452) - drivers: ethernet: stm32, sam, mcux: LAA bit not set
- [GitHub #16421](https://github.com/zephyrproject-rtos/zephyr/issues/16421) - drivers: rtc: stm32: correct tm\_mon conversion
- [GitHub #16376](https://github.com/zephyrproject-rtos/zephyr/issues/16376) - posix ext: Implement eventfd()
- [GitHub #16320](https://github.com/zephyrproject-rtos/zephyr/issues/16320) - The routing option CONFIG\_NET\_ROUTING needs clarification
- [GitHub #16223](https://github.com/zephyrproject-rtos/zephyr/issues/16223) - stm32: Unable to send 64 byte packet over control endpoint
- [GitHub #16167](https://github.com/zephyrproject-rtos/zephyr/issues/16167) - Implement interrupt driven GPIO on LPC families
- [GitHub #16097](https://github.com/zephyrproject-rtos/zephyr/issues/16097) - STM32 Ethernet driver should be able to detect the carrier state
- [GitHub #16041](https://github.com/zephyrproject-rtos/zephyr/issues/16041) - stm32f407 flash erase error sometimes
- [GitHub #16035](https://github.com/zephyrproject-rtos/zephyr/issues/16035) - facing problem with SDHC driver disk mount, need help to debug better
- [GitHub #16032](https://github.com/zephyrproject-rtos/zephyr/issues/16032) - Socket UDP: Low transmission efficiency
- [GitHub #16031](https://github.com/zephyrproject-rtos/zephyr/issues/16031) - Toolchain abstraction
- [GitHub #15912](https://github.com/zephyrproject-rtos/zephyr/issues/15912) - add Reject as an option to pull request reviews
- [GitHub #15881](https://github.com/zephyrproject-rtos/zephyr/issues/15881) - tests/net/buf fails on qemu\_x86\_64
- [GitHub #15841](https://github.com/zephyrproject-rtos/zephyr/issues/15841) - Support AT86RF233
- [GitHub #15604](https://github.com/zephyrproject-rtos/zephyr/issues/15604) - Suspicious PCI and build\_on\_all default test coverage
- [GitHub #15603](https://github.com/zephyrproject-rtos/zephyr/issues/15603) - Unable to use C++ Standard Library
- [GitHub #15598](https://github.com/zephyrproject-rtos/zephyr/issues/15598) - Standard devicetree connectors for boards
- [GitHub #15494](https://github.com/zephyrproject-rtos/zephyr/issues/15494) - 2.0 Release Checklist
- [GitHub #15359](https://github.com/zephyrproject-rtos/zephyr/issues/15359) - The docs incorrectly state that common.dts integrates with mcuboot
- [GitHub #15323](https://github.com/zephyrproject-rtos/zephyr/issues/15323) - blink\_led sample does not work on most of the nRF boards
- [GitHub #15196](https://github.com/zephyrproject-rtos/zephyr/issues/15196) - logging: Support for blocking deferred logging
- [GitHub #15027](https://github.com/zephyrproject-rtos/zephyr/issues/15027) - doc: PDF generation broken
- [GitHub #14906](https://github.com/zephyrproject-rtos/zephyr/issues/14906) - USB: NXP Device controller does not pass testusb tests
- [GitHub #14683](https://github.com/zephyrproject-rtos/zephyr/issues/14683) - need end-to-end memory protection samples
- [GitHub #13725](https://github.com/zephyrproject-rtos/zephyr/issues/13725) - drivers: ssd1306: When 128x32 is used, only half of the screen is output.
- [GitHub #13708](https://github.com/zephyrproject-rtos/zephyr/issues/13708) - No Arduino interface definition for Nordic dev. kits
- [GitHub #13417](https://github.com/zephyrproject-rtos/zephyr/issues/13417) - tests/drivers/watchdog/wdt\_basic\_api/testcase.yaml: test\_wdt\_no\_callback() failed at “Waiting to restart MCU”
- [GitHub #13000](https://github.com/zephyrproject-rtos/zephyr/issues/13000) - sanitycheck serializes running tests on ARC simulator
- [GitHub #12969](https://github.com/zephyrproject-rtos/zephyr/issues/12969) - settings: loading key-value pairs for given subtree
- [GitHub #12965](https://github.com/zephyrproject-rtos/zephyr/issues/12965) - POSIX subsys: Need more fine-grained enable options
- [GitHub #12961](https://github.com/zephyrproject-rtos/zephyr/issues/12961) - ARM Memory Protection functions not invoked in SWAP for ARMv6/ARMv8-M Baseline
- [GitHub #12703](https://github.com/zephyrproject-rtos/zephyr/issues/12703) - how to configure interrupt signals on shields via device tree?
- [GitHub #12677](https://github.com/zephyrproject-rtos/zephyr/issues/12677) - USB: There are some limitations for users to process descriptors
- [GitHub #12653](https://github.com/zephyrproject-rtos/zephyr/issues/12653) - Sanitycheck should not write results into scripts/sanity\_chk
- [GitHub #12535](https://github.com/zephyrproject-rtos/zephyr/issues/12535) - Bluetooth: suspend private address (RPA) rotating
- [GitHub #12509](https://github.com/zephyrproject-rtos/zephyr/issues/12509) - Fix rounding in \_ms\_to\_ticks()
- [GitHub #12504](https://github.com/zephyrproject-rtos/zephyr/issues/12504) - STM32: add USB\_OTG\_HS example
- [GitHub #12206](https://github.com/zephyrproject-rtos/zephyr/issues/12206) - OpenThread apps want to download and build OpenThread every time!
- [GitHub #12114](https://github.com/zephyrproject-rtos/zephyr/issues/12114) - assertion using nRF5 power clock with BLE and nRF5 temp sensor
- [GitHub #11743](https://github.com/zephyrproject-rtos/zephyr/issues/11743) - logging: add user mode access
- [GitHub #11717](https://github.com/zephyrproject-rtos/zephyr/issues/11717) - qemu\_x86 ‘s SeaBIOS clears the screen every time it runs
- [GitHub #11655](https://github.com/zephyrproject-rtos/zephyr/issues/11655) - Alleged multiple design and implementation issues with logging
- [GitHub #11501](https://github.com/zephyrproject-rtos/zephyr/issues/11501) - RFC: Improve CI and add more status items
- [GitHub #10748](https://github.com/zephyrproject-rtos/zephyr/issues/10748) - Work waiting on pollable objects
- [GitHub #10701](https://github.com/zephyrproject-rtos/zephyr/issues/10701) - API: Prefix (aio\_) conflict between POSIX AsyncIO and Designware AnalogIO Comparator
- [GitHub #10503](https://github.com/zephyrproject-rtos/zephyr/issues/10503) - User defined USB function & usb\_get\_device\_descriptor()
- [GitHub #10338](https://github.com/zephyrproject-rtos/zephyr/issues/10338) - Add PyLint checking of all python scripts in CI
- [GitHub #10256](https://github.com/zephyrproject-rtos/zephyr/issues/10256) - Add support for shield x-nucleo-idb05a1
- [GitHub #9482](https://github.com/zephyrproject-rtos/zephyr/issues/9482) - Enable mpu on lpc54114
- [GitHub #9249](https://github.com/zephyrproject-rtos/zephyr/issues/9249) - Get non ST, STM32 Based boards compliant with default configuration guidelines
- [GitHub #9248](https://github.com/zephyrproject-rtos/zephyr/issues/9248) - Get Olimex boards compliant with default configuration guidelines
- [GitHub #9245](https://github.com/zephyrproject-rtos/zephyr/issues/9245) - Get TI SoC based boards compliant with default configuration guidelines
- [GitHub #9244](https://github.com/zephyrproject-rtos/zephyr/issues/9244) - Get SILABS board compliant with default configuration guidelines
- [GitHub #9243](https://github.com/zephyrproject-rtos/zephyr/issues/9243) - Get NXP SoC based boards compliant with default configuration guidelines
- [GitHub #9241](https://github.com/zephyrproject-rtos/zephyr/issues/9241) - Get ATMEL SoC based boards compliant with default configuration guidelines
- [GitHub #9240](https://github.com/zephyrproject-rtos/zephyr/issues/9240) - Get ARM boards compliant with default configuration guidelines
- [GitHub #9239](https://github.com/zephyrproject-rtos/zephyr/issues/9239) - Get NIOS boards compliant with default configuration guidelines
- [GitHub #9237](https://github.com/zephyrproject-rtos/zephyr/issues/9237) - Get RISCV boards compliant with default configuration guidelines
- [GitHub #9236](https://github.com/zephyrproject-rtos/zephyr/issues/9236) - Get X86 boards compliant with default configuration guidelines
- [GitHub #9235](https://github.com/zephyrproject-rtos/zephyr/issues/9235) - Get XTENSA boards compliant with default configuration guidelines
- [GitHub #9193](https://github.com/zephyrproject-rtos/zephyr/issues/9193) - STM32: Move DMA driver to LL/HAL and get it STM32 generic
- [GitHub #8758](https://github.com/zephyrproject-rtos/zephyr/issues/8758) - All nRF drivers: migrate configuration from Kconfig to DTS
- [GitHub #7909](https://github.com/zephyrproject-rtos/zephyr/issues/7909) - tests/kernel/common.test\_bitfield fails on max10
- [GitHub #7375](https://github.com/zephyrproject-rtos/zephyr/issues/7375) - Codecov does not report coverage of code that is not covered by the native\_posix test suite
- [GitHub #7213](https://github.com/zephyrproject-rtos/zephyr/issues/7213) - DTS should use (one or more) prefixes on all defines
- [GitHub #6991](https://github.com/zephyrproject-rtos/zephyr/issues/6991) - Enhance test reporting and maintain one source for testcase meta data
- [GitHub #6858](https://github.com/zephyrproject-rtos/zephyr/issues/6858) - Default board configuration guidelines
- [GitHub #6446](https://github.com/zephyrproject-rtos/zephyr/issues/6446) - sockets: Accept on non-blocking socket is currently blocking
- [GitHub #6152](https://github.com/zephyrproject-rtos/zephyr/issues/6152) - Inter-applications flash layout exchange mechanism
- [GitHub #5138](https://github.com/zephyrproject-rtos/zephyr/issues/5138) - dts: boards: provide generic dtsi file for ‘generic’ boards
- [GitHub #4028](https://github.com/zephyrproject-rtos/zephyr/issues/4028) - C++ 11 Support
- [GitHub #3981](https://github.com/zephyrproject-rtos/zephyr/issues/3981) - ESP32 uart driver does not support Interrupt/fifo mode
- [GitHub #3877](https://github.com/zephyrproject-rtos/zephyr/issues/3877) - Use mbedtls from Zephyr instead of openthread
- [GitHub #652](https://github.com/zephyrproject-rtos/zephyr/issues/652) - Provide a mean to find tests with 0 platforms due to bad filtering
- [GitHub #3497](https://github.com/zephyrproject-rtos/zephyr/issues/3497) - refactor \_NanoFatalErrorHandler
- [GitHub #3181](https://github.com/zephyrproject-rtos/zephyr/issues/3181) - scalable solution for test case stack sizes
- [GitHub #3124](https://github.com/zephyrproject-rtos/zephyr/issues/3124) - Atmel SAM RTC driver
- [GitHub #3056](https://github.com/zephyrproject-rtos/zephyr/issues/3056) - arch-specific inline functions cannot manipulate \_kernel
- [GitHub #2686](https://github.com/zephyrproject-rtos/zephyr/issues/2686) - Add qemu\_cortex\_m0/m0+ board.
- [GitHub #2490](https://github.com/zephyrproject-rtos/zephyr/issues/2490) - Provide sanity test cases for NANO\_ESF/NANO\_ISF structures
- [GitHub #2144](https://github.com/zephyrproject-rtos/zephyr/issues/2144) - clearly document internal kernel interfaces
