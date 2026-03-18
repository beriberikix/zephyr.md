---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/releases/release-notes-2.2.html
original_path: releases/release-notes-2.2.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr 2.2.1

This is a maintenance release for Zephyr 2.2 with fixes.

See [Zephyr 2.2.0](#zephyr-2-2-0) for the previous version release notes.

## Security Vulnerability Related

The following security vulnerabilities (CVE) were addressed in this release:

> - Fix CVE-2020-10028
> - Fix CVE-2020-10060
> - Fix CVE-2020-10063
> - Fix CVE-2020-10066

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Issues Fixed

These GitHub issues were addressed since the previous 2.2.0 tagged
release:

- [GitHub #23494](https://github.com/zephyrproject-rtos/zephyr/issues/23494) - Bluetooth: LL/PAC/SLA/BV-01-C fails if Slave-initiated Feature Exchange is disabled
- [GitHub #23485](https://github.com/zephyrproject-rtos/zephyr/issues/23485) - BT: host: Service Change indication sent regardless of whether it is needed or not.
- [GitHub #23482](https://github.com/zephyrproject-rtos/zephyr/issues/23482) - 2M PHY + DLE and timing calculations on an encrypted link are wrong
- [GitHub #23070](https://github.com/zephyrproject-rtos/zephyr/issues/23070) - Bluetooth: controller: Fix ticker implementation to avoid catch up
- [GitHub #22967](https://github.com/zephyrproject-rtos/zephyr/issues/22967) - Bluetooth: controller: ASSERTION FAIL on invalid packet sequence
- [GitHub #24183](https://github.com/zephyrproject-rtos/zephyr/issues/24183) - [v2.2] Bluetooth: controller: split: Regression slave latency during connection update
- [GitHub #23805](https://github.com/zephyrproject-rtos/zephyr/issues/23805) - Bluetooth: controller: Switching to non conn adv fails for Mesh LPN
- [GitHub #24086](https://github.com/zephyrproject-rtos/zephyr/issues/24086) - Bluetooth: SMP: Existing bond deleted on pairing failure
- [GitHub #24211](https://github.com/zephyrproject-rtos/zephyr/issues/24211) - [v2.2.x] lib: updatehub: Not working on Zephyr 2.x
- [GitHub #24601](https://github.com/zephyrproject-rtos/zephyr/issues/24601) - Bluetooth: Mesh: Config Client’s net\_key\_status pulls two key indexes, should pull one.
- [GitHub #25067](https://github.com/zephyrproject-rtos/zephyr/issues/25067) - Insufficient ticker nodes for vendor implementations
- [GitHub #25350](https://github.com/zephyrproject-rtos/zephyr/issues/25350) - Bluetooth: controller: Data transmission delayed by slave latency
- [GitHub #25483](https://github.com/zephyrproject-rtos/zephyr/issues/25483) - Bluetooth: controller: split: feature exchange not conform V5.0 core spec
- [GitHub #25478](https://github.com/zephyrproject-rtos/zephyr/issues/25478) - settings\_runtime\_set() not populating bt/cf
- [GitHub #25447](https://github.com/zephyrproject-rtos/zephyr/issues/25447) - cf\_set() returns 0 when no cfg is available

# Zephyr 2.2.0

We are pleased to announce the release of Zephyr RTOS version 2.2.0.

Major enhancements with this release include:

- We added initial support for 64-bit ARMv8-A architecture (Experimental).
- CANopen protocol support through 3rd party CANopenNode stack
- LoRa support was added through integration of the Semtech LoRaWAN endpoint
  stack and addition of a new SX1276 LoRa modem driver.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following security vulnerabilities (CVEs) were addressed in this release:

> - Fix CVE-2020-10019
> - Fix CVE-2020-10021
> - Fix CVE-2020-10023
> - Fix CVE-2020-10024
> - Fix CVE-2020-10026
> - Fix CVE-2020-10027
> - Fix CVE-2020-10028
> - Fix CVE-2020-10058

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## API Changes

### Deprecated in this release

- Settings

  - SETTINGS\_USE\_BASE64, encoding values in base64 is marked for removal.

### Stable API changes in this release

- GPIO

  - GPIO API has been reworked to support flags known from Linux DTS GPIO
    bindings. They will typically be defined in the board DTS file

    - GPIO\_ACTIVE\_LOW, GPIO\_ACTIVE\_HIGH used to set pin active level
    - GPIO\_OPEN\_DRAIN, GPIO\_OPEN\_SOURCE used to configure pin as open drain or
      open source
    - GPIO\_PULL\_UP, GPIO\_PULL\_DOWN used to configure pin bias
  - Reading / writing of pin logical level is supported by gpio\_pin\_get,
    gpio\_pin\_set functions.
  - Reading / writing of pin physical level is supported by gpio\_pin\_get\_raw,
    gpio\_pin\_set\_raw functions.
  - New set of port functions that operate simultaneously on multiple pins
    that belong to the same controller.
  - Interrupts should be configured by a dedicated
    gpio\_pin\_interrupt\_configure() function. Configuring interrupts via
    gpio\_pin\_configure() is still supported but this feature will be removed
    in future releases.
  - New set of flags allows to set arbitrary interrupt configuration (if
    supported by the driver) based on pin physical or logical levels.
  - New set of flags to configure pin as input, output or in/out as well as set
    output initial state.
  - Majority of the old GPIO API has been deprecated. While the care was taken
    to preserve backward compatibility due to the scope of the work it was not
    possible to fully achieve this goal. We recommend to switch to the new GPIO
    API as soon as possible.
  - Areas where the deprecated API may behave differently to the original old
    implementation are:

    - Configuration of pin interrupts, especially involving GPIO\_INT\_ACTIVE\_LOW
      and GPIO\_POL\_INV flags.
    - Behavior of gpio\_pin\_configure() when invoked without interrupt related
      flags. In the new implementation of this deprecated functionality the
      interrupts remain unmodified. In the original implementation some of the
      GPIO drivers would disable the interrupts.
  - Several drivers that rely on the functionality provided by the GPIO API
    were reworked to honor pin active level. Any external users of these
    drivers will have to update their DTS board files.

    - bluetooth/hci/spi.c
    - display/display\_ili9340.c
    - display/ssd1306.c
    - ieee802154/ieee802154\_mcr20a.c
    - ieee802154/ieee802154\_rf2xx.c
    - lora/sx1276.c
    - wifi/eswifi/eswifi\_core.c
    - majority of the sensor drivers
- PWM

  - The pwm\_pin\_set\_cycles(), pwm\_pin\_set\_usec(), and
    pwm\_pin\_set\_nsec() functions now take a flags parameter. The newly
    introduced flags are PWM\_POLARITY\_NORMAL and PWM\_POLARITY\_INVERTED
    for specifying the polarity of the PWM signal. The flags parameter
    can be set to 0 if no flags are required (the default is
    PWM\_POLARITY\_NORMAL).
  - Similarly, the pwm\_pin\_set\_t PWM driver API function function now
    takes a flags parameter. The PWM controller driver must check the
    value of the flags parameter and return -ENOTSUP if any
    unsupported flag is set.
- USB

  - The usb\_enable() function, which was previously invoked automatically
    by the USB stack, now needs to be explicitly called by the application
    in order to enable the USB subsystem.
  - The usb\_enable() function now takes a parameter, usb\_dc\_status\_callback
    which can be set by the application to a callback to receive status events
    from the USB stack. The parameter can also be set to NULL if no callback is required.
- nRF flash driver

  - The nRF Flash driver has changed its default write block size to 32-bit
    aligned. Previous emulation of 8-bit write block size can be selected using
    the CONFIG\_SOC\_FLASH\_NRF\_EMULATE\_ONE\_BYTE\_WRITE\_ACCESS Kconfig option.
    Usage of 8-bit write block size emulation is only recommended for
    compatibility with older storage contents.
- Clock control

  - The callback prototype (clock\_control\_cb\_t) has now additional argument
    (clock\_control\_subsys\_t) indicating which clock subsystem got started.

### Removed APIs in this release

- Shell

  - SHELL\_CREATE\_STATIC\_SUBCMD\_SET (deprecated), replaced by
    SHELL\_STATIC\_SUBCMD\_SET\_CREATE
  - SHELL\_CREATE\_DYNAMIC\_CMD (deprecated), replaced by SHELL\_DYNAMIC\_CMD\_CREATE
- Newtron Flash File System (NFFS) was removed. NFFS was removed since it has
  :   serious issues, not fixed since a long time. Where it was possible
      NFFS usage was replaced by LittleFS usage as the better substitute.

## Kernel

- Addressed some race conditions observed on SMP-enabled systems
- Propagate a distinct error code if a workqueue item is submitted that
  has already been completed
- Disable preemption when handing fatal errors
- Fix an issue with the system call stack frame if the system call is
  preempted and then later tries to Z\_OOPS()
- add k\_thread\_stack\_space\_get() system call for analyzing thread stack
  space. Older methods which had problems in some cases or on some
  architectures like STACK\_ANALYZE() are now deprecated.
- Many kernel object APIs now optionally return runtime error values
  instead of relying on assertions. Whether these return values, fail
  assertions, or do no checking at all is controlled by the new
  Kconfig options ASSERT\_ON\_ERRORS, NO\_RUNTIME\_CHECKS, RUNTIME\_ERROR\_CHECKS.
- Cleanups to the arch\_cpu\_start() API
- Spinlock validation now dumps the address of the incorrectly used spinlock
- Various improvements to the assertion mechanism
- k\_poll() may be passed 0 events, in which case it just puts the caller to
  sleep
- Add k\_thread\_foreach\_unlocked() API
- Add an assertion if k\_sleep() is called from an ISR
- Numerous 64-bit fixes, mostly related to data type sizes
- k\_mutex\_unlock() is now correctly a rescheduling point
- Calling k\_thread\_suspend() on the current thread now correctly invokes
  the scheduler
- Calling k\_thread\_suspend() on any thread cancels any pending timeouts for
  that thread
- Fix edge case in meta-IRQ preemption of co-operative threads

## Architectures

- ARC:

  - Fixed several irq-handling related issues
- ARM:

  - Added initial support for ARMv8-A 64-bit architecture (Experimental)
  - Added support for Direct Dynamic Interrupts in ARM Cortex-M
  - Fixed several critical bugs in ARM Cortex-R architecture port
  - Fixed several critical bugs in Stack Limit checking for ARMv8-M
  - Added QEMU emulation support for ARM Cortex-A53
  - Enhanced QEMU emulation support for ARM Cortex-R architecture
  - Enhanced test coverage for ARM-specific kernel features
  - Added support for GIC SGI and PPI interrupt types
  - Refactored GIC driver to support multiple GIC versions
- POSIX:

  - N/A
- RISC-V:

  - N/A
- x86:

  - Fix an issue with Kconfig values larger than INT\_MAX
  - Fix an issue where callee-saved registers could be unnecessarily
    saved on the stack when handling exceptions on x86\_64
  - Fix a potential race with saving RFLAGS on context switch on x86\_64
  - Enable 64-bit mode and X2APIC for the ‘acrn’ target
  - Add a poison value of 0xB9 to RIP if a thread is dispatched on multiple
    cores
  - Implement CONFIG\_USERSPACE on x86\_64
  - Fix an issue where reserved memory could be overwritten when loading the
    Zephyr image on qemu\_x86\_64
  - x86\_64 will now exit QEMU when encountering a fatal error, much like
    32-bit already does
  - Cleanups and improvements to exception debug messages

## Boards & SoC Support

- Added support for these SoC series:

- Atmel SAM4E
- Atmel SAMV71
- Broadcom BCM58400
- NXP i.MX RT1011
- Silicon Labs EFM32GG11B
- Silicon Labs EFM32JG12B
- ST STM32F098xx
- ST STM32F100XX
- ST STM32F767ZI
- ST STM32L152RET6
- ST STM32L452XC
- ST STM32G031
- Intel Apollolake Audio DSP

- Added support for these Xtensa boards:

  - Up Squared board Audio DSP
- Added support for these ARM boards:

  - Atmel SAM 4E Xplained Pro
  - Atmel SAM E54 Xplained Pro
  - Atmel SAM V71 Xplained Ultra
  - Broadcom BCM958401M2
  - Cortex-A53 Emulation (QEMU)
  - Google Kukui EC
  - NXP i.MX RT1010 Evaluation Kit
  - Silicon Labs EFM32 Giant Gecko GG11
  - Silicon Labs EFM32 Jade Gecko
  - ST Nucleo F767ZI
  - ST Nucleo G474RE
  - ST Nucleo L152RE
  - ST Nucleo L452RE
  - ST STM32G0316-DISCO Discovery kit
  - ST STM32VLDISCOVERY
- Removed support for these ARM boards:

  - TI CC2650
- Added support for these following shields:

  - ST7789V Display generic shield
  - TI LMP90100 Sensor Analog Frontend (AFE) Evaluation Board (EVB)
- Removed support for these following shields:

  - Link board CAN

## Drivers and Sensors

- ADC

  - Added LMP90xxx driver with GPIO
- Audio

  - N/A
- Bluetooth

  - Update SPI driver to new GPIO API
  - Minor fixes to H:5 (Three-wire UART) driver
- CAN

  - Support for CAN\_2 on STM32, but no simultaneous use of CAN\_1 and CAN\_2.
  - Support for STM32F3 and STM32F4 series
  - Added SocketCAN support to mcux flexcan driver
  - Fixed bit timing conversion in stm32 driver
  - Introduced can-primary device tree alias
- Clock Control

  - Modified driver for nRF platform to use single device with multiple
    subsystems, one for each clock source.
- Console

  - N/A
- Counter

  - The counter\_read() API function is deprecated in favor of
    counter\_get\_value(). The new API function adds a return value for
    indicating whether the counter was read successfully.
  - Added missing syscalls
- Crypto

  - Added AES GCM, ECB, and CBC support to crypto\_mtls\_shim
  - Added stm32 CRYP driver
- Debug

  - N/A
- Display

  - Added generic display driver sample
  - Added support for BGR565 pixel format
  - Added support for LVGL v6.1
  - Introduced KSCAN based ft5336 touch panel driver
  - Added support for LVGL touch input device
- DMA

  - dw: renaming cavs drivers into DesignWare
  - stm32: improvements over channels support
- EEPROM

  - Added EEPROM driver for STM32L0 and STM32L1 SoC series
  - Added EEPROM simulator (replacing native\_posix EEPROM driver)
- Entropy

  - Added support for sam0
  - Added LiteX PRBS module driver
- ESPI

  - N/A
- Ethernet

  - Support for SiLabs Giant Gecko GG11 Ethernet driver
  - Fixed Ethernet networking for LiteX VexRiscv
- Flash

  - Added Nordic JEDEC QSPI NOR flash driver
  - Unified native\_posix flash driver with drivers/flash/flash\_simulator
  - fixed: erase native\_posix flash in initialization
  - extend MCUX flash drive to support LPC55xxx devices
  - stm32: Replace register accesses for Flash driver to use STM32Cube
  - Nios2: qspi unaligned read support
  - sam0: Add support for SAME54
  - Added the flash driver of the stm32f1x family
- GPIO

  - Updated all drivers to the new API
  - Added LiteX GPIO driver
- Hardware Info

  - N/A
- I2C

  - Enabled interrupts by default in stm32 driver
  - Added I2C shell with scan command
  - Added LiteX I2C controller driver
  - Added STM32G0X support to stm32 driver
  - Added support for bus idle timeout property to mcux lpspi driver
  - Added support for SAME54 to sam0 driver
- I2S

  - N/A
- IEEE 802.15.4

  - Add support for IEEE 802.15.4 rf2xxx driver
- Interrupt Controller

  - Added support for multiple GIC versions
  - Renamed s1000 driver to cavs
  - Added SweRV Programmable Interrupt Controller driver
  - Fixed invalid channel bug for RV32M1 interrupt controller
- IPM

  - N/A
- Keyboard Scan

  - Added ft5336 touch panel driver
- LED

  - N/A
- LED Strip

  - Fixed up ws2812 driver
- LoRa

  - Added APIs and drivers needed to support LoRa technology by reusing the
    LoRaMac-node library.
- Modem

  - Add support for generic GSM modem
- Neural Net

  - N/A
- PCIe

  - N/A
- Pinmux

  - Removed CC2650 driver
- PS/2

  - N/A

> - PTP Clock
>
>   - N/A

- PWM

  - Added RV32M1 timer/PWM driver
  - Added LiteX PWM peripheral driver
  - Added support for intverted PWM signals
- Sensor

  - Fixed DRDY interrupt in lis3mdl driver
  - Added nxp kinetis temperature sensor driver
  - Reworked ccs811 driver
  - Fixed tmp007 driver to use i2c\_burst\_read
  - Introduced sensor shell module
  - Added ms5607 driver
- Serial

  - nRF UARTE driver support TX only mode with receiver permanently disabled.
  - Enabled shared interrupts support in uart\_pl011 driver
  - Implemented configure API in ns16550 driver
  - Removed cc2650 driver
  - Added async API system calls
- SPI

  - Added support for samv71 to sam driver
  - Added support for same54 support to sam0 driver
  - Added PM busy state support in DW driver
  - Added Gecko SPI driver
  - Added mcux flexcomm driver
- Timer

  - Optimized reads of MTIME/MTIMECMP on 64-bit RISC-V
  - Added per-core ARM architected timer driver
  - Added support for same54 to sam0 rtc timer driver
- USB

  - Add support for SAMV71 SoC
  - Add support for SAME54 SoC
  - Extend USB device support to all NXP IMX RT boards
- Video

  - N/A
- Watchdog

  - Added SiLabs Gecko watchdog driver
  - Added system calls
  - Fixed callback call on stm32 wwdg enable
- WiFi

  - Reworked offloading mechanism in eswifi and simplelink drivers

## Networking

- Add support to configure OpenThread Sleepy End Device (SED)
- Add 64-bit support to net\_buf APIs
- Add support for IEEE 802.15.4 rf2xxx driver
- Add TLS secure renegotiation support
- Add support for Timestamp and Record Route IPv4 options.
  They are only used for ICMPv4 Echo-Request packets.
- Add sample cloud application that shows how to connect to Azure cloud
- Add optional timestamp resource to some of the LWM2M IPSO objects
- Add support to poll() which can now return immediately when POLLOUT is set
- Add support to PPP for enabling connection setup to Windows
- Add signed certificate support to echo-server sample application
- Add support for handling multiple simultaneous mDNS requests
- Add support for SiLabs Giant Gecko GG11 Ethernet driver
- Add support for generic GSM modem which uses PPP to connect to data network
- Add UTC offset and timezone support to LWM2M
- Add RX time statistics support to packet socket
- Update ACK handling in IEEE 802.154 nrf5 driver and OpenThread
- Update MQTT PINGREQ count handling
- Update wpan\_serial sample to support more boards
- Update Ethernet e1000 driver debugging prints
- Update OpenThread to use settings subsystem
- Update IPv6 to use interface prefix in routing
- Update socket offloading support to support multiple registered interfaces
- Fix checks when waiting network interface to come up in configuration
- Fix zperf sample issue when running out of network buffers
- Fix PPP IPv4 Control Protocol (IPCP) handling
- Fix native\_posix Ethernet driver to read data faster
- Fix PPP option handling
- Fix MQTT to close connection faster
- Fix 6lo memory corruption during uncompression
- Fix echo-server sample application accept handling
- Fix Websocket to receive data in small chunks
- Fix Virtual LAN (VLAN) support to add link local address to network interface
- Various fixes to new TCP stack implementation
- Remove NATS sample application

## CAN Bus

- CANopen protocol support through 3rd party CANopenNode stack.
- Added native ISO-TP subsystem.
- Introduced CAN-PRIMARY alias.
- SocketCAN for MCUX flexcan.

## Bluetooth

- Host:

  - GAP: Add dynamic LE scan listener API
  - GAP: Pre-allocate connection objects for connectable advertising and
    whitelist initiator.
  - GAP: Fixes for multi-identity support
  - GAP: RPA timeout handling fixes
  - GAP: Add remote version information
  - GATT: Add return value to cfg\_write callback
  - L2CAP: move channel processing to the system workqueue
  - L2CAP: multiple fixes for credit-based flowcontrol
  - SMP: Add pairing\_accept callback
  - SMP: Fix Security Manager timeout handling
- Mesh:

  - Add support for Mesh Configuration Database
  - Multiple fixes to Friendship feature
  - Add support for sending segmented control messages
  - Add support for sending reliable model publication messages
- BLE split software Controller:

  - Multiple fixes, including all those required to pass qualification
  - Implemented software-deferred privacy for platforms without built-in
    address resolution support
  - Added dynamic TX power control, including a set of vendor-specific commands
    to read and write the TX power
  - Added a Kconfig option, BT\_CTLR\_PARAM\_CHECK, to enable additional parameter
    checking
  - Added basic support for SMI (Stable Modulation Index)
  - Ticker: Implemented dynamic rescheduling
  - Nordic: switched to using a single clock device for clock control
  - openisa: Added encryption and decryption support
- BLE legacy software Controller:

  - Multiple fixes
  - Added dynamic TX power control support

## USB Device Stack

- Stack:

  - API: Add support for user device status callback
  - Rework switching to alternate interface
  - Make USB Descriptor power options configurable
  - Derive USB device Serial Number String from HWINFO (required by USB MSC)
  - Move USB transfer functions to appropriate file as preparation for
    the rework
  - Windows OS compatibility: Set USB version to 2.1 when using BOS descriptor
  - Convert VBUS control to new GPIO API
- Classes:

  - CDC ACM: Memory and performance improvements, avoid ZLP during IN transactions
  - DFU: Limit upload length during DFU\_UPLOAD to the request buffer size
  - Loopback: Re-trigger usb\_write after interface configuration event

## Build and Infrastructure

- The minimum Python version supported by Zephyr’s build system and tools is
  now 3.6.
- Renamed `generated_dts_board.h` and `generated_dts_board.conf` to
  `devicetree.h` and `devicetree.conf`, along with various related
  identifiers. Including `generated_dts_board.h` now generates a warning
  saying to include `devicetree.h` instead.

## Libraries / Subsystems

- LoRa

  - LoRa support was added through official LoRaMac-node reference
    implementation.
- Logging

  - Improvements in immediate mode: less interrupts locking, better RTT usage,
    logging from thread context.
  - Improved notification about missing log\_strdup.
- mbedTLS updated to 2.16.4

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Documentation

- settings: include missing API subgoups into the documentation
- Documentation for new boards and samples.
- Improvements and clarity of API documentation.

## Tests and Samples

- Added sample for show settings subsystem API usage

## Issue Related Items

These GitHub issues were addressed since the previous 2.1.0 tagged
release:

- [GitHub #23351](https://github.com/zephyrproject-rtos/zephyr/issues/23351) - boards: nucle\_g474re: west flash doesn’t work
- [GitHub #23321](https://github.com/zephyrproject-rtos/zephyr/issues/23321) - Bluetooth: LE SC OOB authentication in central connects using different RPA
- [GitHub #23310](https://github.com/zephyrproject-rtos/zephyr/issues/23310) - GUI: LVGL: possible NULL dereference
- [GitHub #23281](https://github.com/zephyrproject-rtos/zephyr/issues/23281) - UART console input does not work on SAM E5x
- [GitHub #23268](https://github.com/zephyrproject-rtos/zephyr/issues/23268) - Unnecessary privileged stacks with CONFIG\_USERSPACE=y
- [GitHub #23244](https://github.com/zephyrproject-rtos/zephyr/issues/23244) - kernel.scheduler fails on frdmkw41z
- [GitHub #23231](https://github.com/zephyrproject-rtos/zephyr/issues/23231) - RISCV Machine Timer consistently interrupts long running system after soft reset
- [GitHub #23221](https://github.com/zephyrproject-rtos/zephyr/issues/23221) - status register value always reads 0x0000 in eth\_mcux\_phy\_setup
- [GitHub #23209](https://github.com/zephyrproject-rtos/zephyr/issues/23209) - Bug in tls\_set\_credential
- [GitHub #23208](https://github.com/zephyrproject-rtos/zephyr/issues/23208) - Can not flash test images into up\_squared board.
- [GitHub #23202](https://github.com/zephyrproject-rtos/zephyr/issues/23202) - Macro value for 10 bit ADC is wrong in MEC driver.
- [GitHub #23198](https://github.com/zephyrproject-rtos/zephyr/issues/23198) - rf2xx driver uses mutex in ISR
- [GitHub #23173](https://github.com/zephyrproject-rtos/zephyr/issues/23173) - west flash –nobuild, west flash-signed
- [GitHub #23172](https://github.com/zephyrproject-rtos/zephyr/issues/23172) - Common west flash, debug arguments like –hex-file can’t be used from command line
- [GitHub #23169](https://github.com/zephyrproject-rtos/zephyr/issues/23169) - “blinky” sample fails to build for BBC MicroBit (DT\_ALIAS\_LED0\_GPIOS\_CONTROLLER undefined)
- [GitHub #23168](https://github.com/zephyrproject-rtos/zephyr/issues/23168) - Toolchain docs: describe macOS un-quarantine procedure
- [GitHub #23165](https://github.com/zephyrproject-rtos/zephyr/issues/23165) - macOS setup fails to build for lack of “elftools” Python package
- [GitHub #23148](https://github.com/zephyrproject-rtos/zephyr/issues/23148) - bme280 sample does not compile
- [GitHub #23147](https://github.com/zephyrproject-rtos/zephyr/issues/23147) - tests/drivers/watchdog/wdt\_basic\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #23121](https://github.com/zephyrproject-rtos/zephyr/issues/23121) - Bluetooth: Mesh: Proxy servers only resends segments to proxy
- [GitHub #23110](https://github.com/zephyrproject-rtos/zephyr/issues/23110) - PTS: Bluetooth: GATT/SR/GAS/BV-07-C
- [GitHub #23109](https://github.com/zephyrproject-rtos/zephyr/issues/23109) - LL.TS Test LL/CON/SLA/BV-129-C fails (split)
- [GitHub #23072](https://github.com/zephyrproject-rtos/zephyr/issues/23072) - #ifdef \_\_cplusplus missing in tracking\_cpu\_stats.h
- [GitHub #23069](https://github.com/zephyrproject-rtos/zephyr/issues/23069) - Bluetooth: controller: Assert in data length update procedure
- [GitHub #23050](https://github.com/zephyrproject-rtos/zephyr/issues/23050) - subsys/bluetooth/host/conn.c: conn->ref is not 0 after disconnected
- [GitHub #23047](https://github.com/zephyrproject-rtos/zephyr/issues/23047) - cdc\_acm\_composite sample doesn’t catch DTR from second UART
- [GitHub #23035](https://github.com/zephyrproject-rtos/zephyr/issues/23035) - dhcpv4\_client sample not working on sam e70
- [GitHub #23023](https://github.com/zephyrproject-rtos/zephyr/issues/23023) - Bluetooth: GATT CCC problem (GATT Server)
- [GitHub #23015](https://github.com/zephyrproject-rtos/zephyr/issues/23015) - Ongoing LL control procedures fails with must-expire latency (BT\_CTLR\_CONN\_META)
- [GitHub #23004](https://github.com/zephyrproject-rtos/zephyr/issues/23004) - Can’t use west to flash test images into up\_squared board.
- [GitHub #23002](https://github.com/zephyrproject-rtos/zephyr/issues/23002) - unknown type name ‘class’
- [GitHub #22999](https://github.com/zephyrproject-rtos/zephyr/issues/22999) - pend() assertion can allow user threads to crash the kernel
- [GitHub #22985](https://github.com/zephyrproject-rtos/zephyr/issues/22985) - Check if Zephyr is affected by SweynTooth vulnerabilities
- [GitHub #22982](https://github.com/zephyrproject-rtos/zephyr/issues/22982) - PTS: Test framework: Bluetooth: GATT/SR/GAS/BV-01-C, GATT/SR/GAS/BV-07-C - BTP Error
- [GitHub #22979](https://github.com/zephyrproject-rtos/zephyr/issues/22979) - drivers: hwinfo: Build fails on some SoC
- [GitHub #22977](https://github.com/zephyrproject-rtos/zephyr/issues/22977) - ARM Cortex-M4 stack offset when not using Floating point register sharing
- [GitHub #22968](https://github.com/zephyrproject-rtos/zephyr/issues/22968) - Bluetooth: controller: LEGACY: ASSERTION failure on invalid packet sequence
- [GitHub #22967](https://github.com/zephyrproject-rtos/zephyr/issues/22967) - Bluetooth: controller: ASSERTION FAIL on invalid packet sequence
- [GitHub #22945](https://github.com/zephyrproject-rtos/zephyr/issues/22945) - Bluetooth: controller: ASSERTION FAIL Radio is on during flash operation
- [GitHub #22933](https://github.com/zephyrproject-rtos/zephyr/issues/22933) - k\_delayed\_work\_submit\_to\_queue returns error code when resubmitting previously completed work.
- [GitHub #22931](https://github.com/zephyrproject-rtos/zephyr/issues/22931) - GPIO callback is not triggered for tests/drivers/gpio/gpio\_basic\_api on microchip mec15xxevb\_assy6853 board
- [GitHub #22930](https://github.com/zephyrproject-rtos/zephyr/issues/22930) - PTS: Test Framework :Bluetooth: SM/MAS/PKE/BV-01-C INCONCLUSIV
- [GitHub #22929](https://github.com/zephyrproject-rtos/zephyr/issues/22929) - PTS: Test Framework :Bluetooth: SM/SLA/SIP/BV-01-C Error
- [GitHub #22928](https://github.com/zephyrproject-rtos/zephyr/issues/22928) - PTS: Test Framework: Bluetooth: SM/MAS/SIGN/BV-03-C, SM/MAS/SIGN/BI-01-C - INCONCLUSIV
- [GitHub #22927](https://github.com/zephyrproject-rtos/zephyr/issues/22927) - PTS: Test Framework: Bluetooth: SM/MAS/SIP/BV-02-C-INCONCLUSIV
- [GitHub #22926](https://github.com/zephyrproject-rtos/zephyr/issues/22926) - Bluetooth: Cannot establish security and discover GATT when using Split LL
- [GitHub #22914](https://github.com/zephyrproject-rtos/zephyr/issues/22914) - tests/arch/arm/arm\_irq\_vector\_table crashes for nRF5340
- [GitHub #22912](https://github.com/zephyrproject-rtos/zephyr/issues/22912) - [Coverity CID :208406] Macro compares unsigned to 0 in subsys/net/l2/ppp/ppp\_l2.c
- [GitHub #22902](https://github.com/zephyrproject-rtos/zephyr/issues/22902) - eth\_mcux\_phy\_setup called before ENET clock being enabled causes CPU to hang
- [GitHub #22893](https://github.com/zephyrproject-rtos/zephyr/issues/22893) - Problem using 3 instances of SPIM on NRF52840
- [GitHub #22890](https://github.com/zephyrproject-rtos/zephyr/issues/22890) - IP networking does not work on ATSAME70 Rev. B
- [GitHub #22888](https://github.com/zephyrproject-rtos/zephyr/issues/22888) - Can’t flash test image into iotdk board.
- [GitHub #22885](https://github.com/zephyrproject-rtos/zephyr/issues/22885) - Sanitycheck timeout all test cases on mec15xxevb\_assy6853 board.
- [GitHub #22874](https://github.com/zephyrproject-rtos/zephyr/issues/22874) - sanitycheck: when someone instance get stuck because of concurrent.futures.TimeoutErro exception, it always stuck
- [GitHub #22858](https://github.com/zephyrproject-rtos/zephyr/issues/22858) - WDT\_DISABLE\_AT\_BOOT, if enabled by default, degrades functionality of the watchdog
- [GitHub #22855](https://github.com/zephyrproject-rtos/zephyr/issues/22855) - drivers: enc28j60: waits for wrong interrupt
- [GitHub #22847](https://github.com/zephyrproject-rtos/zephyr/issues/22847) - Test gpio\_basic\_api hangs on cc3220sf\_launchxl
- [GitHub #22828](https://github.com/zephyrproject-rtos/zephyr/issues/22828) - kernel: fatal: interrupts left locked in TEST mode
- [GitHub #22822](https://github.com/zephyrproject-rtos/zephyr/issues/22822) - mesh: typo in condition in comp\_add\_elem of cfg\_srv
- [GitHub #22819](https://github.com/zephyrproject-rtos/zephyr/issues/22819) - #define \_current in kernel\_structs.h leaks into global namespace
- [GitHub #22814](https://github.com/zephyrproject-rtos/zephyr/issues/22814) - mcuboot doesn’t build with zephyr v2.1.0
- [GitHub #22803](https://github.com/zephyrproject-rtos/zephyr/issues/22803) - k\_delayed\_work\_cancel documentation inconsistent with behavior
- [GitHub #22801](https://github.com/zephyrproject-rtos/zephyr/issues/22801) - Bluetooth: Split LL: Reconnection problem
- [GitHub #22786](https://github.com/zephyrproject-rtos/zephyr/issues/22786) - Bluetooth: SM/MAS/PROT/BV-01-C FAIL
- [GitHub #22784](https://github.com/zephyrproject-rtos/zephyr/issues/22784) - system hangs in settings\_load() nrf52840 custom board
- [GitHub #22774](https://github.com/zephyrproject-rtos/zephyr/issues/22774) - Set USB version to 2.1 when CONFIG\_USB\_DEVICE\_BOS is set
- [GitHub #22730](https://github.com/zephyrproject-rtos/zephyr/issues/22730) - CONFIG\_BT\_SETTINGS writes bt/hash to storage twice
- [GitHub #22722](https://github.com/zephyrproject-rtos/zephyr/issues/22722) - posix: redefinition of symbols while porting zeromq to zephyr
- [GitHub #22720](https://github.com/zephyrproject-rtos/zephyr/issues/22720) - armv8-m: userspace: some parts in userspace enter sequence need to be atomic
- [GitHub #22698](https://github.com/zephyrproject-rtos/zephyr/issues/22698) - log\_stack\_usage: prints err: missinglog\_strdup()
- [GitHub #22697](https://github.com/zephyrproject-rtos/zephyr/issues/22697) - nrf52 telnet\_shell panic. Mutex using in ISR.
- [GitHub #22693](https://github.com/zephyrproject-rtos/zephyr/issues/22693) - net: config: build break when CONFIG\_NET\_NATIVE=n
- [GitHub #22689](https://github.com/zephyrproject-rtos/zephyr/issues/22689) - driver: modem: sara-u2 error when connecting
- [GitHub #22685](https://github.com/zephyrproject-rtos/zephyr/issues/22685) - armv8-m: userspace: syscall return sequence needs to be atomic
- [GitHub #22682](https://github.com/zephyrproject-rtos/zephyr/issues/22682) - arm: cortex-a: no default board for testing
- [GitHub #22660](https://github.com/zephyrproject-rtos/zephyr/issues/22660) - gpio: legacy level interrupt disable API not backwards compatible
- [GitHub #22658](https://github.com/zephyrproject-rtos/zephyr/issues/22658) - [Coverity CID :208189] Self assignment in soc/xtensa/intel\_apl\_adsp/soc.c
- [GitHub #22657](https://github.com/zephyrproject-rtos/zephyr/issues/22657) - [Coverity CID :208191] Dereference after null check in subsys/canbus/isotp/isotp.c
- [GitHub #22656](https://github.com/zephyrproject-rtos/zephyr/issues/22656) - [Coverity CID :208192] Out-of-bounds access in tests/subsys/canbus/isotp/implementation/src/main.c
- [GitHub #22655](https://github.com/zephyrproject-rtos/zephyr/issues/22655) - [Coverity CID :208193] Unchecked return value in tests/bluetooth/mesh/src/microbit.c
- [GitHub #22654](https://github.com/zephyrproject-rtos/zephyr/issues/22654) - [Coverity CID :208194] Arguments in wrong order in tests/subsys/canbus/isotp/implementation/src/main.c
- [GitHub #22653](https://github.com/zephyrproject-rtos/zephyr/issues/22653) - [Coverity CID :208196] Out-of-bounds access in drivers/eeprom/eeprom\_simulator.c
- [GitHub #22652](https://github.com/zephyrproject-rtos/zephyr/issues/22652) - [Coverity CID :208197] Pointless string comparison in tests/drivers/gpio/gpio\_basic\_api/src/main.c
- [GitHub #22651](https://github.com/zephyrproject-rtos/zephyr/issues/22651) - [Coverity CID :208198] Logical vs. bitwise operator in boards/xtensa/up\_squared\_adsp/bootloader/boot\_loader.c
- [GitHub #22650](https://github.com/zephyrproject-rtos/zephyr/issues/22650) - [Coverity CID :208199] Arguments in wrong order in tests/subsys/canbus/isotp/conformance/src/main.c
- [GitHub #22649](https://github.com/zephyrproject-rtos/zephyr/issues/22649) - [Coverity CID :208200] Bad bit shift operation in drivers/interrupt\_controller/intc\_exti\_stm32.c
- [GitHub #22648](https://github.com/zephyrproject-rtos/zephyr/issues/22648) - [Coverity CID :208201] Out-of-bounds write in soc/xtensa/intel\_apl\_adsp/soc.c
- [GitHub #22647](https://github.com/zephyrproject-rtos/zephyr/issues/22647) - [Coverity CID :208202] Arguments in wrong order in samples/subsys/canbus/isotp/src/main.c
- [GitHub #22646](https://github.com/zephyrproject-rtos/zephyr/issues/22646) - [Coverity CID :208203] Missing break in switch in drivers/interrupt\_controller/intc\_exti\_stm32.c
- [GitHub #22645](https://github.com/zephyrproject-rtos/zephyr/issues/22645) - [Coverity CID :208204] Arguments in wrong order in samples/subsys/canbus/isotp/src/main.c
- [GitHub #22644](https://github.com/zephyrproject-rtos/zephyr/issues/22644) - [Coverity CID :208205] Improper use of negative value in tests/subsys/canbus/isotp/implementation/src/main.c
- [GitHub #22642](https://github.com/zephyrproject-rtos/zephyr/issues/22642) - [Coverity CID :208207] Arguments in wrong order in tests/subsys/canbus/isotp/conformance/src/main.c
- [GitHub #22641](https://github.com/zephyrproject-rtos/zephyr/issues/22641) - [Coverity CID :208208] Arguments in wrong order in tests/subsys/canbus/isotp/implementation/src/main.c
- [GitHub #22640](https://github.com/zephyrproject-rtos/zephyr/issues/22640) - [Coverity CID :208209] ‘Constant’ variable guards dead code in drivers/gpio/gpio\_sx1509b.c
- [GitHub #22636](https://github.com/zephyrproject-rtos/zephyr/issues/22636) - Provide Linux-style IS\_ERR()/PTR\_ERR()/ERR\_PTR() helpers
- [GitHub #22626](https://github.com/zephyrproject-rtos/zephyr/issues/22626) - tests/drivers/counter/counter\_basic\_api failed on frdm\_k64f board.
- [GitHub #22624](https://github.com/zephyrproject-rtos/zephyr/issues/22624) - tests/kernel/semaphore/semaphore failed on iotdk board.
- [GitHub #22623](https://github.com/zephyrproject-rtos/zephyr/issues/22623) - tests/kernel/timer/timer\_api failed on mimxrt1050\_evk board.
- [GitHub #22616](https://github.com/zephyrproject-rtos/zephyr/issues/22616) - Zephyr doesn’t build if x86\_64 SDK toolchain isn’t install
- [GitHub #22584](https://github.com/zephyrproject-rtos/zephyr/issues/22584) - drivers: spi: spi\_mcux\_dspi: bus busy status ignored in async
- [GitHub #22563](https://github.com/zephyrproject-rtos/zephyr/issues/22563) - Common west flash/debug etc. arguments cannot be set in CMake
- [GitHub #22559](https://github.com/zephyrproject-rtos/zephyr/issues/22559) - crash in semaphore tests on ARC nsim\_em and nsim\_sem
- [GitHub #22557](https://github.com/zephyrproject-rtos/zephyr/issues/22557) - document guidelines/principles related to DT usage in Zephyr
- [GitHub #22556](https://github.com/zephyrproject-rtos/zephyr/issues/22556) - document DT macro generation rules
- [GitHub #22543](https://github.com/zephyrproject-rtos/zephyr/issues/22543) - No way to address a particular FTDI for OpenOCD
- [GitHub #22542](https://github.com/zephyrproject-rtos/zephyr/issues/22542) - GEN\_ABSOLUTE\_SYM cannot handle value larger than INT\_MAX on qemu\_x86\_64
- [GitHub #22539](https://github.com/zephyrproject-rtos/zephyr/issues/22539) - bt\_gatt: unable to save SC: no cfg left
- [GitHub #22535](https://github.com/zephyrproject-rtos/zephyr/issues/22535) - drivers: lora: Make the SX1276 driver independent of loramac module
- [GitHub #22534](https://github.com/zephyrproject-rtos/zephyr/issues/22534) - sanitycheck qemu\_x86\_coverage problem with SDK 0.11.1
- [GitHub #22532](https://github.com/zephyrproject-rtos/zephyr/issues/22532) - Doc build warning lvgl/README.rst
- [GitHub #22525](https://github.com/zephyrproject-rtos/zephyr/issues/22525) - stm32f7xx.h: No such file or directory
- [GitHub #22522](https://github.com/zephyrproject-rtos/zephyr/issues/22522) - GPIO test code tests/drivers/gpio/gpio\_basic\_api does not compile for microchip board mec15xxevb\_assy6853
- [GitHub #22519](https://github.com/zephyrproject-rtos/zephyr/issues/22519) - sanitycheck failures for native\_posix
- [GitHub #22514](https://github.com/zephyrproject-rtos/zephyr/issues/22514) - Bluetooth: gatt: CCC cfg not flushed if device was previously paired
- [GitHub #22510](https://github.com/zephyrproject-rtos/zephyr/issues/22510) - Build warnings in samples/net/cloud/google\_iot\_mqtt
- [GitHub #22489](https://github.com/zephyrproject-rtos/zephyr/issues/22489) - Request to enable CONFIG\_NET\_PKT\_RXTIME\_STATS for SOCK\_RAW
- [GitHub #22486](https://github.com/zephyrproject-rtos/zephyr/issues/22486) - Do we have driver for Texas Instruments DRV2605 haptic driver for ERM and LRA actuators?
- [GitHub #22484](https://github.com/zephyrproject-rtos/zephyr/issues/22484) - Linker error when building google\_iot\_mqtt sample with zephyr-sdk 0.11.1
- [GitHub #22482](https://github.com/zephyrproject-rtos/zephyr/issues/22482) - Unable to use LOG\_BACKEND\_DEFINE macro from log\_backend.h using C++
- [GitHub #22478](https://github.com/zephyrproject-rtos/zephyr/issues/22478) - Bluetooth - peripheral\_dis - settings\_runtime\_set not working
- [GitHub #22474](https://github.com/zephyrproject-rtos/zephyr/issues/22474) - boards that have Kconfig warnings on hello\_world.
- [GitHub #22466](https://github.com/zephyrproject-rtos/zephyr/issues/22466) - Add hx711 sensor
- [GitHub #22462](https://github.com/zephyrproject-rtos/zephyr/issues/22462) - onoff: why client must be reinitialized after each transition
- [GitHub #22455](https://github.com/zephyrproject-rtos/zephyr/issues/22455) - How to assign USB endpoint address manually in stm32f4\_disco for CDC ACM class driver
- [GitHub #22452](https://github.com/zephyrproject-rtos/zephyr/issues/22452) - not driver found in can bus samples for olimexino\_stm32
- [GitHub #22447](https://github.com/zephyrproject-rtos/zephyr/issues/22447) - samples: echo\_client sample breaks for UDP when larger than net if MTU
- [GitHub #22444](https://github.com/zephyrproject-rtos/zephyr/issues/22444) - [Coverity CID :207963] Argument cannot be negative in tests/net/socket/websocket/src/main.c
- [GitHub #22443](https://github.com/zephyrproject-rtos/zephyr/issues/22443) - [Coverity CID :207964] Dereference after null check in subsys/canbus/canopen/CO\_driver.c
- [GitHub #22442](https://github.com/zephyrproject-rtos/zephyr/issues/22442) - [Coverity CID :207965] Missing break in switch in drivers/i2c/i2c\_ll\_stm32\_v1.c
- [GitHub #22440](https://github.com/zephyrproject-rtos/zephyr/issues/22440) - [Coverity CID :207970] Out-of-bounds access in samples/net/sockets/websocket\_client/src/main.c
- [GitHub #22439](https://github.com/zephyrproject-rtos/zephyr/issues/22439) - [Coverity CID :207971] Negative array index read in subsys/net/l2/ppp/ipcp.c
- [GitHub #22438](https://github.com/zephyrproject-rtos/zephyr/issues/22438) - [Coverity CID :207973] Out-of-bounds access in tests/net/socket/websocket/src/main.c
- [GitHub #22437](https://github.com/zephyrproject-rtos/zephyr/issues/22437) - [Coverity CID :207974] Out-of-bounds read in tests/net/socket/websocket/src/main.c
- [GitHub #22436](https://github.com/zephyrproject-rtos/zephyr/issues/22436) - [Coverity CID :207975] Logically dead code in subsys/net/l2/ppp/ipcp.c
- [GitHub #22435](https://github.com/zephyrproject-rtos/zephyr/issues/22435) - [Coverity CID :207977] Logically dead code in subsys/canbus/canopen/CO\_driver.c
- [GitHub #22434](https://github.com/zephyrproject-rtos/zephyr/issues/22434) - [Coverity CID :207978] Dereference after null check in subsys/canbus/canopen/CO\_driver.c
- [GitHub #22433](https://github.com/zephyrproject-rtos/zephyr/issues/22433) - [Coverity CID :207980] Untrusted loop bound in tests/net/socket/websocket/src/main.c
- [GitHub #22432](https://github.com/zephyrproject-rtos/zephyr/issues/22432) - [Coverity CID :207982] Explicit null dereferenced in tests/lib/onoff/src/main.c
- [GitHub #22430](https://github.com/zephyrproject-rtos/zephyr/issues/22430) - [Coverity CID :207985] Argument cannot be negative in subsys/net/lib/websocket/websocket.c
- [GitHub #22424](https://github.com/zephyrproject-rtos/zephyr/issues/22424) - RFC: API Change: clock\_control
- [GitHub #22417](https://github.com/zephyrproject-rtos/zephyr/issues/22417) - Build warnings with atsamr21\_xpro
- [GitHub #22410](https://github.com/zephyrproject-rtos/zephyr/issues/22410) - arch: arm64: ARM64 port not working on real target
- [GitHub #22390](https://github.com/zephyrproject-rtos/zephyr/issues/22390) - Unable to build http\_get with TLS enabled on cc32xx
- [GitHub #22388](https://github.com/zephyrproject-rtos/zephyr/issues/22388) - Build warnings in http\_get on cc3220sf\_launchxl
- [GitHub #22366](https://github.com/zephyrproject-rtos/zephyr/issues/22366) - Bug in sockets.c (subsysnetlibsockets)
- [GitHub #22363](https://github.com/zephyrproject-rtos/zephyr/issues/22363) - drivers: clock\_control: clock\_stm32\_ll\_h7.c Move Power Configuration code
- [GitHub #22360](https://github.com/zephyrproject-rtos/zephyr/issues/22360) - test\_mqtt\_disconnect in mqtt\_pubsub fails
- [GitHub #22356](https://github.com/zephyrproject-rtos/zephyr/issues/22356) - An application hook for early init
- [GitHub #22343](https://github.com/zephyrproject-rtos/zephyr/issues/22343) - stm32f303 - irq conflict between CAN and USB
- [GitHub #22317](https://github.com/zephyrproject-rtos/zephyr/issues/22317) - samples/arc\_secure\_services fails on nsim\_sem
- [GitHub #22316](https://github.com/zephyrproject-rtos/zephyr/issues/22316) - samples/philosophers coop\_only scenario times out on nsim\_sem and nsim\_em
- [GitHub #22307](https://github.com/zephyrproject-rtos/zephyr/issues/22307) - net: ip: net\_pkt\_pull(): packet corruption when using CONFIG\_NET\_BUF\_DATA\_SIZE larger than 256
- [GitHub #22304](https://github.com/zephyrproject-rtos/zephyr/issues/22304) - ARM Cortex-M STMF401RE: execution too slow
- [GitHub #22299](https://github.com/zephyrproject-rtos/zephyr/issues/22299) - The file flash\_stm32wbx.c generates compilation error
- [GitHub #22297](https://github.com/zephyrproject-rtos/zephyr/issues/22297) - nucleo\_wb55rg:samples/bluetooth/peripheral/sample.bluetooth.peripheral fails to build on master
- [GitHub #22290](https://github.com/zephyrproject-rtos/zephyr/issues/22290) - ARC crashes due to concurrent system calls
- [GitHub #22280](https://github.com/zephyrproject-rtos/zephyr/issues/22280) - incorrect linker routing
- [GitHub #22275](https://github.com/zephyrproject-rtos/zephyr/issues/22275) - arm: cortex-R & M: CONFIG\_USERSPACE: intermittent Memory region write access failures
- [GitHub #22272](https://github.com/zephyrproject-rtos/zephyr/issues/22272) - aggregated devicetree source file needs to be restored to build directory
- [GitHub #22268](https://github.com/zephyrproject-rtos/zephyr/issues/22268) - timer not working when duration is too high
- [GitHub #22265](https://github.com/zephyrproject-rtos/zephyr/issues/22265) - Simultaneous BLE pairings getting the same slot in keys structure
- [GitHub #22259](https://github.com/zephyrproject-rtos/zephyr/issues/22259) - Bluetooth: default value 80 on BT\_ACL\_RX\_COUNT clamped to 64
- [GitHub #22258](https://github.com/zephyrproject-rtos/zephyr/issues/22258) - sanitycheck fails to merge OVERLAY\_CONFIG properly
- [GitHub #22257](https://github.com/zephyrproject-rtos/zephyr/issues/22257) - test wdt\_basic\_api failed on nucleo\_f746zg
- [GitHub #22245](https://github.com/zephyrproject-rtos/zephyr/issues/22245) - STM32G4xx: Wrong SystemCoreClock variable
- [GitHub #22243](https://github.com/zephyrproject-rtos/zephyr/issues/22243) - stm32g431rb: PLL setting result to slow exccution
- [GitHub #22210](https://github.com/zephyrproject-rtos/zephyr/issues/22210) - Bluetooth - bt\_gatt\_get\_value\_attr\_by\_uuid
- [GitHub #22207](https://github.com/zephyrproject-rtos/zephyr/issues/22207) - Bluetooth ：Mesh：Provison init should after proxy
- [GitHub #22204](https://github.com/zephyrproject-rtos/zephyr/issues/22204) - CONFIG\_BT\_DEBUG\_LOG vs atomic operations
- [GitHub #22202](https://github.com/zephyrproject-rtos/zephyr/issues/22202) - bt\_rand() is called over HCI when BT\_HOST\_CRYPTO=y, even if BT\_CTLR\_LE\_ENC=n
- [GitHub #22197](https://github.com/zephyrproject-rtos/zephyr/issues/22197) - dts: gen\_defines.py bails out on new path property type
- [GitHub #22188](https://github.com/zephyrproject-rtos/zephyr/issues/22188) - drivers: espi: xec : eSPI driver should not send VWire SUS\_ACK automatically in all cases
- [GitHub #22177](https://github.com/zephyrproject-rtos/zephyr/issues/22177) - Adafruit M0 boards are not set up to correctly flash in their code partitions
- [GitHub #22171](https://github.com/zephyrproject-rtos/zephyr/issues/22171) - West bossac runner inorrectly tries to include an offset parameter when flashing
- [GitHub #22128](https://github.com/zephyrproject-rtos/zephyr/issues/22128) - frdm\_k82f:samples/drivers/spi\_fujitsu\_fram/sample.drivers.spi.fujitsu\_fram fails
- [GitHub #22107](https://github.com/zephyrproject-rtos/zephyr/issues/22107) - mdns support with avahi as client
- [GitHub #22106](https://github.com/zephyrproject-rtos/zephyr/issues/22106) - intermittent emulator exit on samples/userspace/shared\_mem on qemu\_x86\_64
- [GitHub #22088](https://github.com/zephyrproject-rtos/zephyr/issues/22088) - Bluetooth Mesh friendship is cleared due to no Friend response reception
- [GitHub #22086](https://github.com/zephyrproject-rtos/zephyr/issues/22086) - L2CAP/SMP: Race condition possible in native posix central when bonding.
- [GitHub #22085](https://github.com/zephyrproject-rtos/zephyr/issues/22085) - HCI/CCO/BV-07-C & HCI/GEV/BV-01-C failing in EDTT
- [GitHub #22066](https://github.com/zephyrproject-rtos/zephyr/issues/22066) - tests/kernel/mem\_pool/mem\_pool\_threadsafe fails reliably on m2gl025\_miv
- [GitHub #22062](https://github.com/zephyrproject-rtos/zephyr/issues/22062) - Adafruit Feather M0 does not flash correctly - incorrect flash code offset and bossa version incompatibility
- [GitHub #22060](https://github.com/zephyrproject-rtos/zephyr/issues/22060) - Build fails with gnuarmemb under windows
- [GitHub #22051](https://github.com/zephyrproject-rtos/zephyr/issues/22051) - Bluetooth Central: Discovery of 128bit primary service fails with later versions of gcc.
- [GitHub #22048](https://github.com/zephyrproject-rtos/zephyr/issues/22048) - Failing LL.TS Data Length Update Tests (split)
- [GitHub #22037](https://github.com/zephyrproject-rtos/zephyr/issues/22037) - qemu\_cortex\_r5 excludes too many tests
- [GitHub #22036](https://github.com/zephyrproject-rtos/zephyr/issues/22036) - sanitycheck for qemu\_cortex\_r5 fails
- [GitHub #22026](https://github.com/zephyrproject-rtos/zephyr/issues/22026) - west: openocd runner fails for boards without support/openocd.cfg
- [GitHub #22014](https://github.com/zephyrproject-rtos/zephyr/issues/22014) - RTC prescaler overflow on nRF(52)
- [GitHub #22010](https://github.com/zephyrproject-rtos/zephyr/issues/22010) - Bluetooth ‘central’ failure on native\_posix
- [GitHub #22003](https://github.com/zephyrproject-rtos/zephyr/issues/22003) - ‘central’ failure on nrf52\_pca10040
- [GitHub #21996](https://github.com/zephyrproject-rtos/zephyr/issues/21996) - Native POSIX or QEMU X86 emulation does not detect Bluetooth HCI Vendor-Specific Extensions
- [GitHub #21989](https://github.com/zephyrproject-rtos/zephyr/issues/21989) - websocket: recv\_msg always returns full message length on last call
- [GitHub #21974](https://github.com/zephyrproject-rtos/zephyr/issues/21974) - make include hierarchy consistent with expected usage
- [GitHub #21970](https://github.com/zephyrproject-rtos/zephyr/issues/21970) - net: dns: mDNS resolving fails when responder is also enabled
- [GitHub #21967](https://github.com/zephyrproject-rtos/zephyr/issues/21967) - json: json\_obj\_parse will modify the input string
- [GitHub #21962](https://github.com/zephyrproject-rtos/zephyr/issues/21962) - drivers: usb: usb\_dc\_stm32: does not compile for stm32f3\_disco board
- [GitHub #21949](https://github.com/zephyrproject-rtos/zephyr/issues/21949) - net: TCP: echo server deadlock from TCP packet
- [GitHub #21935](https://github.com/zephyrproject-rtos/zephyr/issues/21935) - SPI - STM32: transceive() should handle null tx buffer
- [GitHub #21917](https://github.com/zephyrproject-rtos/zephyr/issues/21917) - cmake error with CONFIG\_COUNTER and CONFIG\_BT both enabled (nrf52 board)
- [GitHub #21914](https://github.com/zephyrproject-rtos/zephyr/issues/21914) - net: dns: Answers to multiple mDNS queries sent in parallel aren’t properly handled
- [GitHub #21888](https://github.com/zephyrproject-rtos/zephyr/issues/21888) - Print unmet Kconfig dependency
- [GitHub #21875](https://github.com/zephyrproject-rtos/zephyr/issues/21875) - sanitycheck warning for silabs,gecko-spi-usart.yaml
- [GitHub #21869](https://github.com/zephyrproject-rtos/zephyr/issues/21869) - IPv6 neighbors get added too eagerly
- [GitHub #21859](https://github.com/zephyrproject-rtos/zephyr/issues/21859) - Bluetooth LE Disconnect event not received
- [GitHub #21854](https://github.com/zephyrproject-rtos/zephyr/issues/21854) - HCI-UART: Bluetooth ACL data packets with 251 bytes not acknowledged
- [GitHub #21846](https://github.com/zephyrproject-rtos/zephyr/issues/21846) - RFC: API: Counter: counter\_read() has no way of indicating failure
- [GitHub #21837](https://github.com/zephyrproject-rtos/zephyr/issues/21837) - net: socket: Add dependency to mbedtls
- [GitHub #21813](https://github.com/zephyrproject-rtos/zephyr/issues/21813) - tests/kernel/timer/timer\_api failed on frdm\_k64f board.
- [GitHub #21812](https://github.com/zephyrproject-rtos/zephyr/issues/21812) - tests/arch/arm/arm\_irq\_advanced\_features failed on reel\_board.
- [GitHub #21800](https://github.com/zephyrproject-rtos/zephyr/issues/21800) - Xtensa doesn’t save SCOMPARE1 register on context switch
- [GitHub #21790](https://github.com/zephyrproject-rtos/zephyr/issues/21790) - tests/kernel/timer/timer\_api fails on nucleo\_g071rb board
- [GitHub #21789](https://github.com/zephyrproject-rtos/zephyr/issues/21789) - Merge topic-gpio back to master
- [GitHub #21784](https://github.com/zephyrproject-rtos/zephyr/issues/21784) - sanitycheck prints some build errors directly to the console
- [GitHub #21780](https://github.com/zephyrproject-rtos/zephyr/issues/21780) - OpenThread fails on nRF52840 Dongle (nrf52840\_pca10059)
- [GitHub #21775](https://github.com/zephyrproject-rtos/zephyr/issues/21775) - echo\_server and 802154 not build for NRF52811
- [GitHub #21768](https://github.com/zephyrproject-rtos/zephyr/issues/21768) - Make [CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS] dependent on [CONFIG\_MBEDTLS] in menuconfig
- [GitHub #21764](https://github.com/zephyrproject-rtos/zephyr/issues/21764) - [SARA-R4] MQTT publisher not working - Impossible to connect to broker
- [GitHub #21763](https://github.com/zephyrproject-rtos/zephyr/issues/21763) - at86rf2xx radio driver does not report whether a TX was ACKed
- [GitHub #21756](https://github.com/zephyrproject-rtos/zephyr/issues/21756) - tests/kernel/obj\_tracing failed on mec15xxevb\_assy6853 board.
- [GitHub #21755](https://github.com/zephyrproject-rtos/zephyr/issues/21755) - tests/drivers/adc/adc\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #21745](https://github.com/zephyrproject-rtos/zephyr/issues/21745) - tests: counter\_basic\_api: Failed on stm32 based boards
- [GitHub #21744](https://github.com/zephyrproject-rtos/zephyr/issues/21744) - dumb\_http\_server\_mt with overlay-tls.conf does not connect
- [GitHub #21735](https://github.com/zephyrproject-rtos/zephyr/issues/21735) - ARM: Cortex-M: IRQ lock/unlock() API non-functional but accessible from user mode
- [GitHub #21716](https://github.com/zephyrproject-rtos/zephyr/issues/21716) - nucleo\_g431rb: Hello world not working
- [GitHub #21715](https://github.com/zephyrproject-rtos/zephyr/issues/21715) - nucleo\_g431rb: Blinky too slow / wrong clock setup?
- [GitHub #21713](https://github.com/zephyrproject-rtos/zephyr/issues/21713) - CDC ACM USB class issue with high transfer rate and ZLP
- [GitHub #21702](https://github.com/zephyrproject-rtos/zephyr/issues/21702) - [Coverity CID :206599] Out-of-bounds access in tests/bluetooth/uuid/src/main.c
- [GitHub #21700](https://github.com/zephyrproject-rtos/zephyr/issues/21700) - [Coverity CID :206606] Out-of-bounds access in tests/bluetooth/uuid/src/main.c
- [GitHub #21699](https://github.com/zephyrproject-rtos/zephyr/issues/21699) - [Coverity CID :206608] Dereference null return value in tests/net/icmpv4/src/main.c
- [GitHub #21695](https://github.com/zephyrproject-rtos/zephyr/issues/21695) - Documentation issues on v1.14-branch block backport
- [GitHub #21681](https://github.com/zephyrproject-rtos/zephyr/issues/21681) - nucleo\_g431rb / STM32G4: Flashing works only once
- [GitHub #21679](https://github.com/zephyrproject-rtos/zephyr/issues/21679) - SPI broken on stm32f412 on master
- [GitHub #21676](https://github.com/zephyrproject-rtos/zephyr/issues/21676) - [Coverity CID :206389] Logically dead code in subsys/testsuite/ztest/src/ztest.c
- [GitHub #21674](https://github.com/zephyrproject-rtos/zephyr/issues/21674) - [Coverity CID :206392] Side effect in assertion in tests/kernel/timer/starve/src/main.c
- [GitHub #21673](https://github.com/zephyrproject-rtos/zephyr/issues/21673) - [Coverity CID :206393] Unintentional integer overflow in drivers/sensor/ms5607/ms5607.c
- [GitHub #21672](https://github.com/zephyrproject-rtos/zephyr/issues/21672) - [Coverity CID :206394] Logically dead code in subsys/testsuite/ztest/src/ztest.c
- [GitHub #21660](https://github.com/zephyrproject-rtos/zephyr/issues/21660) - Sample projects do not build for Nucleo WB55RG
- [GitHub #21659](https://github.com/zephyrproject-rtos/zephyr/issues/21659) - at86rf2xx radio driver not (reliably) sending ACKs
- [GitHub #21650](https://github.com/zephyrproject-rtos/zephyr/issues/21650) - \_TEXT\_SECTION\_NAME\_2 on ARM Cortex-R
- [GitHub #21637](https://github.com/zephyrproject-rtos/zephyr/issues/21637) - sanitycheck failed issue in parallel running.
- [GitHub #21629](https://github.com/zephyrproject-rtos/zephyr/issues/21629) - error with ‘west update’ on Windows 10
- [GitHub #21623](https://github.com/zephyrproject-rtos/zephyr/issues/21623) - DT: accept standard syntax for phandle in chosen node
- [GitHub #21618](https://github.com/zephyrproject-rtos/zephyr/issues/21618) - CI failing to complete tests
- [GitHub #21617](https://github.com/zephyrproject-rtos/zephyr/issues/21617) - Allow per module prj.conf
- [GitHub #21614](https://github.com/zephyrproject-rtos/zephyr/issues/21614) - host toolchain for x86 fails on empty CMAKE\_C\_FLAGS
- [GitHub #21607](https://github.com/zephyrproject-rtos/zephyr/issues/21607) - BME680 Sensor is not building
- [GitHub #21601](https://github.com/zephyrproject-rtos/zephyr/issues/21601) - ‘!radio\_is\_ready()’ failed
- [GitHub #21599](https://github.com/zephyrproject-rtos/zephyr/issues/21599) - CONFIG\_HEAP\_MEM\_POOL\_SIZE and k\_malloc, k\_free not working in nrf51\_pca10028
- [GitHub #21597](https://github.com/zephyrproject-rtos/zephyr/issues/21597) - sht3xd build error on olimexino\_stm32
- [GitHub #21591](https://github.com/zephyrproject-rtos/zephyr/issues/21591) - Timeout error for the Microchip board during Sanitycheck
- [GitHub #21586](https://github.com/zephyrproject-rtos/zephyr/issues/21586) - Bluetooth Mesh fail to transmit messages after some time on nRF52840
- [GitHub #21581](https://github.com/zephyrproject-rtos/zephyr/issues/21581) - GNU ARM Embedded link broken in Getting Started
- [GitHub #21571](https://github.com/zephyrproject-rtos/zephyr/issues/21571) - CONFIG\_BT\_CENTRAL doesnot work fine with nrf51\_pca10028
- [GitHub #21570](https://github.com/zephyrproject-rtos/zephyr/issues/21570) - how to select usb mps for SAME70 board
- [GitHub #21568](https://github.com/zephyrproject-rtos/zephyr/issues/21568) - mps2\_an385:tests/kernel/tickless/tickless\_concept/kernel.tickless.concept fail
- [GitHub #21552](https://github.com/zephyrproject-rtos/zephyr/issues/21552) - Constant disconnects while attempting BT LE multi-central application.
- [GitHub #21551](https://github.com/zephyrproject-rtos/zephyr/issues/21551) - gpio: xec: GPIO Interrupt is not triggered for range GPIO240\_276
- [GitHub #21546](https://github.com/zephyrproject-rtos/zephyr/issues/21546) - SPI broken for STM32L1
- [GitHub #21536](https://github.com/zephyrproject-rtos/zephyr/issues/21536) - tests/subsys/fs/fat\_fs\_api fails on native\_posix\_64
- [GitHub #21532](https://github.com/zephyrproject-rtos/zephyr/issues/21532) - can not build the image ,No targets specified and no makefile found
- [GitHub #21514](https://github.com/zephyrproject-rtos/zephyr/issues/21514) - Logging - strange behaviour with RTT on nRF53
- [GitHub #21510](https://github.com/zephyrproject-rtos/zephyr/issues/21510) - re-v
- [GitHub #21493](https://github.com/zephyrproject-rtos/zephyr/issues/21493) - System tick is not running
- [GitHub #21483](https://github.com/zephyrproject-rtos/zephyr/issues/21483) - sanitycheck messages in CI are not informative anymore
- [GitHub #21475](https://github.com/zephyrproject-rtos/zephyr/issues/21475) - sanitycheck: hardware map generation unexpected exit during the first attempt
- [GitHub #21466](https://github.com/zephyrproject-rtos/zephyr/issues/21466) - doc: extract\_content.py not copying images in a table
- [GitHub #21450](https://github.com/zephyrproject-rtos/zephyr/issues/21450) - sample.net.cloud.google\_iot\_mqtt test is failing for frdm\_k64f
- [GitHub #21448](https://github.com/zephyrproject-rtos/zephyr/issues/21448) - nrf52840 errata\_98 / 89 mixup
- [GitHub #21443](https://github.com/zephyrproject-rtos/zephyr/issues/21443) - “HCI\_USB” sample doesn’t compile with “nucleo\_wb55rg” board
- [GitHub #21438](https://github.com/zephyrproject-rtos/zephyr/issues/21438) - sanitycheck reports “FAILED: N/A” for failed or hung tests
- [GitHub #21432](https://github.com/zephyrproject-rtos/zephyr/issues/21432) - watchdog subsystem has no system calls
- [GitHub #21431](https://github.com/zephyrproject-rtos/zephyr/issues/21431) - missing async uart.h system calls
- [GitHub #21429](https://github.com/zephyrproject-rtos/zephyr/issues/21429) - Impossible to override syscalls
- [GitHub #21426](https://github.com/zephyrproject-rtos/zephyr/issues/21426) - civetweb triggers an error on Windows with Git 2.24
- [GitHub #21422](https://github.com/zephyrproject-rtos/zephyr/issues/21422) - Added nucleo-f767zi board support and would like to share
- [GitHub #21419](https://github.com/zephyrproject-rtos/zephyr/issues/21419) - RFC: API Change: usb: Make users call usb\_enable. Provide global status callback.
- [GitHub #21418](https://github.com/zephyrproject-rtos/zephyr/issues/21418) - Crash when suspending system
- [GitHub #21410](https://github.com/zephyrproject-rtos/zephyr/issues/21410) - bt\_ctlr\_hci: Tx Buffer Overflow on LL/CON/MAS/BV-04-C, LL/CON/SLA/BV-05-C & LL/CON/SLA/BV-06-C
- [GitHub #21409](https://github.com/zephyrproject-rtos/zephyr/issues/21409) - sanitycheck: cmd.exe colorized output
- [GitHub #21385](https://github.com/zephyrproject-rtos/zephyr/issues/21385) - board frdm\_kl25z build passed, but can’t flash
- [GitHub #21384](https://github.com/zephyrproject-rtos/zephyr/issues/21384) - RFC: API Change: PWM: add support for inverted PWM signals
- [GitHub #21379](https://github.com/zephyrproject-rtos/zephyr/issues/21379) - Bluetooth: Mesh: Node Reset Not Clear Bind Key Information
- [GitHub #21375](https://github.com/zephyrproject-rtos/zephyr/issues/21375) - GATT: gatt\_write\_ccc\_rsp with error (0x0e) removes always beginning from subscriptions head
- [GitHub #21365](https://github.com/zephyrproject-rtos/zephyr/issues/21365) - implicit casts in API headers must be replaced for C++ support
- [GitHub #21351](https://github.com/zephyrproject-rtos/zephyr/issues/21351) - tests/drivers/counter/counter\_basic\_api failed on mimxrt1050\_evk board.
- [GitHub #21341](https://github.com/zephyrproject-rtos/zephyr/issues/21341) - conditions required for safe call of kernel operations from interrupts
- [GitHub #21339](https://github.com/zephyrproject-rtos/zephyr/issues/21339) - Expired IPv6 router causes an infinite loop
- [GitHub #21335](https://github.com/zephyrproject-rtos/zephyr/issues/21335) - net: TCP: Socket echo server does not accept incoming connections when TLS is enabled
- [GitHub #21328](https://github.com/zephyrproject-rtos/zephyr/issues/21328) - Apparent network context leak with offloading driver (u-blox Sara r4)
- [GitHub #21325](https://github.com/zephyrproject-rtos/zephyr/issues/21325) - Where should the Digital-Input, Output, ADC driver be added?
- [GitHub #21321](https://github.com/zephyrproject-rtos/zephyr/issues/21321) - error update for project civetweb
- [GitHub #21318](https://github.com/zephyrproject-rtos/zephyr/issues/21318) - CONFIG\_SYS\_POWER\_MANAGEMENT Makes Build Fail for nRF5340 and nRF9160
- [GitHub #21317](https://github.com/zephyrproject-rtos/zephyr/issues/21317) - intermittent SMP crashes on x86\_64
- [GitHub #21306](https://github.com/zephyrproject-rtos/zephyr/issues/21306) - ARC: syscall register save/restore needs backport to 1.14
- [GitHub #21301](https://github.com/zephyrproject-rtos/zephyr/issues/21301) - Coverage report generated for qemu\_x86 board is incomplete
- [GitHub #21300](https://github.com/zephyrproject-rtos/zephyr/issues/21300) - pyocd flash failing on bbc\_microbit
- [GitHub #21299](https://github.com/zephyrproject-rtos/zephyr/issues/21299) - bluetooth: Controller does not release buffer on central side after peripheral reset
- [GitHub #21290](https://github.com/zephyrproject-rtos/zephyr/issues/21290) - Compiler warnings in flash.h: invalid conversion from ‘const void\*’ to ‘const flash\_driver\_api\*’
- [GitHub #21281](https://github.com/zephyrproject-rtos/zephyr/issues/21281) - logging: msg\_free may erroneously call log\_free
- [GitHub #21278](https://github.com/zephyrproject-rtos/zephyr/issues/21278) - How to use pwm in nrf52832 for rgb led
- [GitHub #21275](https://github.com/zephyrproject-rtos/zephyr/issues/21275) - kl2x soc fixup is missing I2C\_1 labels
- [GitHub #21257](https://github.com/zephyrproject-rtos/zephyr/issues/21257) - tests/net/net\_pkt failed on mimxrt1050\_evk board.
- [GitHub #21240](https://github.com/zephyrproject-rtos/zephyr/issues/21240) - Error west flash
- [GitHub #21229](https://github.com/zephyrproject-rtos/zephyr/issues/21229) - cc1plus: warning: ‘-Werror=’ argument ‘-Werror=implicit-int’ is not valid for C++
- [GitHub #21202](https://github.com/zephyrproject-rtos/zephyr/issues/21202) - Required upgrade of HAL
- [GitHub #21186](https://github.com/zephyrproject-rtos/zephyr/issues/21186) - Gatt discover callback gives invalid pointer to primary and secondary service UUID.
- [GitHub #21185](https://github.com/zephyrproject-rtos/zephyr/issues/21185) - zero-latency IRQ behavior is not documented?
- [GitHub #21181](https://github.com/zephyrproject-rtos/zephyr/issues/21181) - devicetree should support making properties with defaults required
- [GitHub #21177](https://github.com/zephyrproject-rtos/zephyr/issues/21177) - Long ATT MTU reports wrong length field in write callback.
- [GitHub #21171](https://github.com/zephyrproject-rtos/zephyr/issues/21171) - Module Request: Optiga Trust X
- [GitHub #21167](https://github.com/zephyrproject-rtos/zephyr/issues/21167) - libraries.libc.newlib test fails
- [GitHub #21165](https://github.com/zephyrproject-rtos/zephyr/issues/21165) - Bluetooth: Mesh: Friend Clear message from a Friend node
- [GitHub #21162](https://github.com/zephyrproject-rtos/zephyr/issues/21162) - Sanitycheck corrupted test case names in test-report.xml files
- [GitHub #21161](https://github.com/zephyrproject-rtos/zephyr/issues/21161) - question: openthread with other boards
- [GitHub #21148](https://github.com/zephyrproject-rtos/zephyr/issues/21148) - nrf51: uart\_1 does not compile
- [GitHub #21139](https://github.com/zephyrproject-rtos/zephyr/issues/21139) - west: runners: blackmagicprobe: Keyboard Interrupt shouldn’t kill the process
- [GitHub #21131](https://github.com/zephyrproject-rtos/zephyr/issues/21131) - Bluetooth: host: Subscriptions not removed upon unpair
- [GitHub #21126](https://github.com/zephyrproject-rtos/zephyr/issues/21126) - drivers: spi\_nrfx\_spim: Incorrect handling of extended SPIM configuration
- [GitHub #21123](https://github.com/zephyrproject-rtos/zephyr/issues/21123) - sanitycheck halt some test cases with parallel running.
- [GitHub #21121](https://github.com/zephyrproject-rtos/zephyr/issues/21121) - netusb: RNDIS host support
- [GitHub #21115](https://github.com/zephyrproject-rtos/zephyr/issues/21115) - Request a new repository for the Xtensa HAL
- [GitHub #21105](https://github.com/zephyrproject-rtos/zephyr/issues/21105) - Bluetooth API called before finished initialization.
- [GitHub #21103](https://github.com/zephyrproject-rtos/zephyr/issues/21103) - Bluetooth: host: Reduce overhead of GATT subscriptions
- [GitHub #21099](https://github.com/zephyrproject-rtos/zephyr/issues/21099) - echo server qemu\_x86 e1000 cannot generate coverage reports
- [GitHub #21095](https://github.com/zephyrproject-rtos/zephyr/issues/21095) - [Coverity CID :206086] Out-of-bounds access in drivers/timer/cortex\_m\_systick.c
- [GitHub #21094](https://github.com/zephyrproject-rtos/zephyr/issues/21094) - native\_posix doesn’t call main function that’s defined in C++
- [GitHub #21082](https://github.com/zephyrproject-rtos/zephyr/issues/21082) - tests/kernel/timer/timer\_api failing on several nRF5x SoCs
- [GitHub #21074](https://github.com/zephyrproject-rtos/zephyr/issues/21074) - Enhance 802.1Qav documentation
- [GitHub #21058](https://github.com/zephyrproject-rtos/zephyr/issues/21058) - BLE: Enable/Disable Automatic sending of Connection Parameter update request on Timeout.
- [GitHub #21057](https://github.com/zephyrproject-rtos/zephyr/issues/21057) - BLE: No Valid Parameter check in send\_conn\_le\_param\_update()
- [GitHub #21045](https://github.com/zephyrproject-rtos/zephyr/issues/21045) - log\_backend.h missing include for UTIL\_CAT in LOG\_BACKEND\_DEFINE macro
- [GitHub #21036](https://github.com/zephyrproject-rtos/zephyr/issues/21036) - Add SMP function similar to bt\_conn\_get\_info
- [GitHub #21025](https://github.com/zephyrproject-rtos/zephyr/issues/21025) - sam\_e70\_xplained reboots after 35secs
- [GitHub #20981](https://github.com/zephyrproject-rtos/zephyr/issues/20981) - mempool: MPU fault
- [GitHub #20974](https://github.com/zephyrproject-rtos/zephyr/issues/20974) - file resources exceeded with sanitycheck
- [GitHub #20953](https://github.com/zephyrproject-rtos/zephyr/issues/20953) - usb: nrf: usb on reel board becomes unavailable if USB cable is not connected at first
- [GitHub #20927](https://github.com/zephyrproject-rtos/zephyr/issues/20927) - ztest\_1cpu\_user\_unit\_test() doesn’t work
- [GitHub #20915](https://github.com/zephyrproject-rtos/zephyr/issues/20915) - doc: Kconfig section in board\_porting.rst should be moved or removed
- [GitHub #20904](https://github.com/zephyrproject-rtos/zephyr/issues/20904) - kernel.timer.tickless is failed due to missing TEST\_USERSPACE flag
- [GitHub #20886](https://github.com/zephyrproject-rtos/zephyr/issues/20886) - [Coverity CID :205826] Memory - corruptions in tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_utils.c
- [GitHub #20885](https://github.com/zephyrproject-rtos/zephyr/issues/20885) - [Coverity CID :205819] Memory - corruptions in tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_utils.c
- [GitHub #20884](https://github.com/zephyrproject-rtos/zephyr/issues/20884) - [Coverity CID :205799] Memory - corruptions in tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_utils.c
- [GitHub #20877](https://github.com/zephyrproject-rtos/zephyr/issues/20877) - [Coverity CID :205823] Null pointer dereferences in tests/kernel/fifo/fifo\_timeout/src/main.c
- [GitHub #20802](https://github.com/zephyrproject-rtos/zephyr/issues/20802) - reschedule not done after mutex unlock
- [GitHub #20770](https://github.com/zephyrproject-rtos/zephyr/issues/20770) - irq locking in logging backend can cause missing interrupts
- [GitHub #20755](https://github.com/zephyrproject-rtos/zephyr/issues/20755) - mcuboot: add as module and verify functionality
- [GitHub #20749](https://github.com/zephyrproject-rtos/zephyr/issues/20749) - samples:sample.net.dns\_resolve.mdns:frdmk64f ipv4dns handler has not result
- [GitHub #20748](https://github.com/zephyrproject-rtos/zephyr/issues/20748) - build warnings on lpcxpresso54114\_m0/m4 board
- [GitHub #20746](https://github.com/zephyrproject-rtos/zephyr/issues/20746) - Bluetooth: Mesh: Friend node Adding another Friend Update
- [GitHub #20724](https://github.com/zephyrproject-rtos/zephyr/issues/20724) - Packed pointer warning in LL Controller
- [GitHub #20698](https://github.com/zephyrproject-rtos/zephyr/issues/20698) - Bluetooth: host: Skip pre-scan done by bt\_conn\_create\_le if not needed
- [GitHub #20697](https://github.com/zephyrproject-rtos/zephyr/issues/20697) - Confusing warning during cmake
- [GitHub #20673](https://github.com/zephyrproject-rtos/zephyr/issues/20673) - guiconfig not working properly?
- [GitHub #20640](https://github.com/zephyrproject-rtos/zephyr/issues/20640) - Bluetooth: l2cap do not recover when faced with long packets and run out of buffers
- [GitHub #20629](https://github.com/zephyrproject-rtos/zephyr/issues/20629) - when CONFIG\_BT\_SETTINGS is enabled, stack stores id in flash memory each power up of device (call to bt\_enable)
- [GitHub #20618](https://github.com/zephyrproject-rtos/zephyr/issues/20618) - Can unicast address be relayed when send message over gatt proxy?
- [GitHub #20576](https://github.com/zephyrproject-rtos/zephyr/issues/20576) - DTS overlay files must include full path name
- [GitHub #20561](https://github.com/zephyrproject-rtos/zephyr/issues/20561) - Crypto API: Separate IV from ciphertext based on struct cipher\_ctx::flags
- [GitHub #20535](https://github.com/zephyrproject-rtos/zephyr/issues/20535) - [Coverity CID :205619]Null pointer dereferences in /tests/net/ieee802154/fragment/src/main.c
- [GitHub #20497](https://github.com/zephyrproject-rtos/zephyr/issues/20497) - [Coverity CID :205638]Integer handling issues in /drivers/pwm/pwm\_mchp\_xec.c
- [GitHub #20490](https://github.com/zephyrproject-rtos/zephyr/issues/20490) - [Coverity CID :205651]Uninitialized variables in /drivers/dma/dma\_stm32.c
- [GitHub #20484](https://github.com/zephyrproject-rtos/zephyr/issues/20484) - Tests/kernel/gen\_isr\_table failing when enabling WDT driver
- [GitHub #20426](https://github.com/zephyrproject-rtos/zephyr/issues/20426) - sensors: grove temperature and light drivers out of date
- [GitHub #20414](https://github.com/zephyrproject-rtos/zephyr/issues/20414) - nRF51 issues with the split link layer
- [GitHub #20411](https://github.com/zephyrproject-rtos/zephyr/issues/20411) - samples: lis3mdl trigger not working with x\_nucleo\_iks01a1
- [GitHub #20388](https://github.com/zephyrproject-rtos/zephyr/issues/20388) - Allow for runtime reconfiguration of SPI master / slave
- [GitHub #20355](https://github.com/zephyrproject-rtos/zephyr/issues/20355) - west build for zephyr/samples/net/sockets/echo\_server/ on qemu\_xtensa target outputs elf with panic
- [GitHub #20315](https://github.com/zephyrproject-rtos/zephyr/issues/20315) - zperf TCP uploader fails
- [GitHub #20286](https://github.com/zephyrproject-rtos/zephyr/issues/20286) - Problem building for ESP32
- [GitHub #20278](https://github.com/zephyrproject-rtos/zephyr/issues/20278) - Something is wrong when trying ST7789V sample
- [GitHub #20264](https://github.com/zephyrproject-rtos/zephyr/issues/20264) - Bluetooth: Delay advertising events instead of dropping them on collision
- [GitHub #20256](https://github.com/zephyrproject-rtos/zephyr/issues/20256) - settings subsystem sample
- [GitHub #20217](https://github.com/zephyrproject-rtos/zephyr/issues/20217) - Extend qemu\_cortex\_r5 test coverage
- [GitHub #20172](https://github.com/zephyrproject-rtos/zephyr/issues/20172) - devicetree support for compound elements
- [GitHub #20161](https://github.com/zephyrproject-rtos/zephyr/issues/20161) - Facing issue to setup zephyr on ubuntu
- [GitHub #20153](https://github.com/zephyrproject-rtos/zephyr/issues/20153) - BLE small throughput
- [GitHub #20140](https://github.com/zephyrproject-rtos/zephyr/issues/20140) - CMake: syscall macro’s are not generated for out of tree DTS\_ROOT
- [GitHub #20125](https://github.com/zephyrproject-rtos/zephyr/issues/20125) - Add system call to enter low power mode and reduce latency for deep sleep entry
- [GitHub #20026](https://github.com/zephyrproject-rtos/zephyr/issues/20026) - sanitycheck corrupts stty in some cases
- [GitHub #20017](https://github.com/zephyrproject-rtos/zephyr/issues/20017) - Convert GPIO users to new GPIO API
- [GitHub #19982](https://github.com/zephyrproject-rtos/zephyr/issues/19982) - Periodically wake up log process thread consume more power
- [GitHub #19922](https://github.com/zephyrproject-rtos/zephyr/issues/19922) - Linear time to give L2CAP credits
- [GitHub #19869](https://github.com/zephyrproject-rtos/zephyr/issues/19869) - Implement tickless capability for xlnx\_psttc\_timer
- [GitHub #19761](https://github.com/zephyrproject-rtos/zephyr/issues/19761) - tests/net/ieee802154/fragment failed on reel board.
- [GitHub #19737](https://github.com/zephyrproject-rtos/zephyr/issues/19737) - No Function In Zephyr For Reading BLE Channel Map?
- [GitHub #19666](https://github.com/zephyrproject-rtos/zephyr/issues/19666) - remove kernel/include and `arch/*/include` from default include path
- [GitHub #19643](https://github.com/zephyrproject-rtos/zephyr/issues/19643) - samples/boards/arc\_secure\_services fails on nsim\_sem
- [GitHub #19545](https://github.com/zephyrproject-rtos/zephyr/issues/19545) - usb: obtain configuration descriptor’s bmAttributes and bMaxPower from DT
- [GitHub #19540](https://github.com/zephyrproject-rtos/zephyr/issues/19540) - Allow running and testing network samples in automatic way
- [GitHub #19492](https://github.com/zephyrproject-rtos/zephyr/issues/19492) - sanitycheck: unreliable/inconsistent catch of ASSERTION FAILED
- [GitHub #19488](https://github.com/zephyrproject-rtos/zephyr/issues/19488) - Reference and sample codes to get started with the friendship feature in ble mesh
- [GitHub #19473](https://github.com/zephyrproject-rtos/zephyr/issues/19473) - Missing NULL parameter check in k\_pipe\_get
- [GitHub #19361](https://github.com/zephyrproject-rtos/zephyr/issues/19361) - BLE Scan fails to start when running in parallel with BLE mesh
- [GitHub #19342](https://github.com/zephyrproject-rtos/zephyr/issues/19342) - Bluetooth: Mesh: Persistent storage of Virtual Addresses
- [GitHub #19245](https://github.com/zephyrproject-rtos/zephyr/issues/19245) - Logging: Assert with LOG\_IMMEDIATE
- [GitHub #19100](https://github.com/zephyrproject-rtos/zephyr/issues/19100) - LwM2M sample with DTLS: does not connect
- [GitHub #19053](https://github.com/zephyrproject-rtos/zephyr/issues/19053) - 2.1 Release Checklist
- [GitHub #18962](https://github.com/zephyrproject-rtos/zephyr/issues/18962) - [Coverity CID :203909]Memory - corruptions in /subsys/mgmt/smp\_shell.c
- [GitHub #18867](https://github.com/zephyrproject-rtos/zephyr/issues/18867) - zsock\_poll() unnecessarily wait when querying for ZSOCK\_POLLOUT
- [GitHub #18852](https://github.com/zephyrproject-rtos/zephyr/issues/18852) - west flash fails for cc1352r\_launchxl
- [GitHub #18635](https://github.com/zephyrproject-rtos/zephyr/issues/18635) - isr4 repeatedly gets triggered after test passes in tests/kernel/gen\_isr\_table
- [GitHub #18583](https://github.com/zephyrproject-rtos/zephyr/issues/18583) - hci\_usb: NRF52840 connecting addtional peripheral fails
- [GitHub #18551](https://github.com/zephyrproject-rtos/zephyr/issues/18551) - address-of-temporary idiom not allowed in C++
- [GitHub #18530](https://github.com/zephyrproject-rtos/zephyr/issues/18530) - Convert GPIO drivers to new GPIO API
- [GitHub #18483](https://github.com/zephyrproject-rtos/zephyr/issues/18483) - Bluetooth: length variable inconsistency in keys.c
- [GitHub #18452](https://github.com/zephyrproject-rtos/zephyr/issues/18452) - [Coverity CID :203463]Memory - corruptions in /tests/lib/ringbuffer/src/main.c
- [GitHub #18447](https://github.com/zephyrproject-rtos/zephyr/issues/18447) - [Coverity CID :203400]Integer handling issues in /tests/lib/fdtable/src/main.c
- [GitHub #18410](https://github.com/zephyrproject-rtos/zephyr/issues/18410) - [Coverity CID :203448]Memory - corruptions in /subsys/net/lib/lwm2m/ipso\_onoff\_switch.c
- [GitHub #18378](https://github.com/zephyrproject-rtos/zephyr/issues/18378) - [Coverity CID :203537]Error handling issues in /samples/subsys/nvs/src/main.c
- [GitHub #18280](https://github.com/zephyrproject-rtos/zephyr/issues/18280) - tests/drivers/adc/adc\_api fails on frdmkl25z
- [GitHub #18173](https://github.com/zephyrproject-rtos/zephyr/issues/18173) - ARM: Core Stack Improvements/Bug fixes for 2.1 release
- [GitHub #18169](https://github.com/zephyrproject-rtos/zephyr/issues/18169) - dts: bindings: inconsistent file names and base.yaml include of general device controllers
- [GitHub #18137](https://github.com/zephyrproject-rtos/zephyr/issues/18137) - Add section on IRQ generation to doc/guides/dts/index.rst
- [GitHub #17852](https://github.com/zephyrproject-rtos/zephyr/issues/17852) - Cmsis\_rtos\_v2\_apis test failed on iotdk board.
- [GitHub #17838](https://github.com/zephyrproject-rtos/zephyr/issues/17838) - state DEVICE\_PM\_LOW\_POWER\_STATE of Device Power Management
- [GitHub #17787](https://github.com/zephyrproject-rtos/zephyr/issues/17787) - openocd unable to flash hello\_world to cc26x2r1\_launchxl
- [GitHub #17731](https://github.com/zephyrproject-rtos/zephyr/issues/17731) - Dynamically set TX power of BLE Radio
- [GitHub #17689](https://github.com/zephyrproject-rtos/zephyr/issues/17689) - On missing sensor, Init hangs
- [GitHub #17543](https://github.com/zephyrproject-rtos/zephyr/issues/17543) - dtc version 1.4.5 with ubuntu 18.04 and zephyr sdk-0.10.1
- [GitHub #17310](https://github.com/zephyrproject-rtos/zephyr/issues/17310) - boards: shields: use Kconfig.defconfig system for shields
- [GitHub #17309](https://github.com/zephyrproject-rtos/zephyr/issues/17309) - enhancements to device tree generation
- [GitHub #17102](https://github.com/zephyrproject-rtos/zephyr/issues/17102) - RFC: rework GPIO interrupt configuration
- [GitHub #16935](https://github.com/zephyrproject-rtos/zephyr/issues/16935) - Zephyr doc website: Delay search in /boards to the end of the search.
- [GitHub #16851](https://github.com/zephyrproject-rtos/zephyr/issues/16851) - west flash error on zephyr v1.14.99
- [GitHub #16735](https://github.com/zephyrproject-rtos/zephyr/issues/16735) - smp\_svr sample does not discover services
- [GitHub #16545](https://github.com/zephyrproject-rtos/zephyr/issues/16545) - west: diagnose dependency version failures
- [GitHub #16482](https://github.com/zephyrproject-rtos/zephyr/issues/16482) - mcumgr seems to compromise BT security
- [GitHub #16472](https://github.com/zephyrproject-rtos/zephyr/issues/16472) - tinycrypt ecc-dh and ecc-dsa should not select entropy generator
- [GitHub #16329](https://github.com/zephyrproject-rtos/zephyr/issues/16329) - ztest teardown function not called if test function is interrupted
- [GitHub #16239](https://github.com/zephyrproject-rtos/zephyr/issues/16239) - Build: C++ compiler warning ‘-Wold-style-definition’
- [GitHub #16235](https://github.com/zephyrproject-rtos/zephyr/issues/16235) - STM32: Move STM32 Flash driver to CMSIS STM32Cube definitions
- [GitHub #16232](https://github.com/zephyrproject-rtos/zephyr/issues/16232) - STM32: implement pinmux api
- [GitHub #16202](https://github.com/zephyrproject-rtos/zephyr/issues/16202) - Improve help for west build target
- [GitHub #16034](https://github.com/zephyrproject-rtos/zephyr/issues/16034) - Net packet size of 64 bytes doesn’t work.
- [GitHub #16023](https://github.com/zephyrproject-rtos/zephyr/issues/16023) - mcuboot: enabling USB functionality in MCUboot crashes zephyr application in slot0
- [GitHub #16011](https://github.com/zephyrproject-rtos/zephyr/issues/16011) - Increase coverage of tests
- [GitHub #15906](https://github.com/zephyrproject-rtos/zephyr/issues/15906) - WEST ERROR: extension command build was improperly defined
- [GitHub #15841](https://github.com/zephyrproject-rtos/zephyr/issues/15841) - Support AT86RF233
- [GitHub #15729](https://github.com/zephyrproject-rtos/zephyr/issues/15729) - flash: should write\_protection be emulated?
- [GitHub #15657](https://github.com/zephyrproject-rtos/zephyr/issues/15657) - properly define kernel <–> arch APIs
- [GitHub #15611](https://github.com/zephyrproject-rtos/zephyr/issues/15611) - gpio/pinctrl: GPIO and introduce PINCTRL API to support gpio, pinctrl DTS nodes
- [GitHub #15593](https://github.com/zephyrproject-rtos/zephyr/issues/15593) - How to use gdb to view the stack of a thread
- [GitHub #15580](https://github.com/zephyrproject-rtos/zephyr/issues/15580) - SAMD21 Adafruit examples no longer run on boards
- [GitHub #15435](https://github.com/zephyrproject-rtos/zephyr/issues/15435) - device fails to boot when spi max frequency set above 1000000
- [GitHub #15278](https://github.com/zephyrproject-rtos/zephyr/issues/15278) - CANopen Support
- [GitHub #15229](https://github.com/zephyrproject-rtos/zephyr/issues/15229) - network tests have extremely restrictive whitelist
- [GitHub #15171](https://github.com/zephyrproject-rtos/zephyr/issues/15171) - BLE Throughput
- [GitHub #14927](https://github.com/zephyrproject-rtos/zephyr/issues/14927) - checkpatch: not expected behavior for multiple git commit check.
- [GitHub #14922](https://github.com/zephyrproject-rtos/zephyr/issues/14922) - samples/boards/altera\_max10/pio: Error configuring GPIO PORT
- [GitHub #14753](https://github.com/zephyrproject-rtos/zephyr/issues/14753) - nrf52840\_pca10056: Leading spurious 0x00 byte in UART output
- [GitHub #14668](https://github.com/zephyrproject-rtos/zephyr/issues/14668) - net: icmp4: Zephyr strips record route and time stamp options
- [GitHub #14650](https://github.com/zephyrproject-rtos/zephyr/issues/14650) - missing system calls in Counter driver APIs
- [GitHub #14639](https://github.com/zephyrproject-rtos/zephyr/issues/14639) - All tests should be SMP-safe
- [GitHub #14632](https://github.com/zephyrproject-rtos/zephyr/issues/14632) - Default for TLS\_PEER\_VERIFY socket option are set to required, may lead to confusion when running samples against self-signed certs
- [GitHub #14621](https://github.com/zephyrproject-rtos/zephyr/issues/14621) - BLE controller: Add support for Controller(SW deferred)-based Privacy
- [GitHub #14287](https://github.com/zephyrproject-rtos/zephyr/issues/14287) - USB HID Get\_Report and Set\_Report
- [GitHub #14206](https://github.com/zephyrproject-rtos/zephyr/issues/14206) - user mode documentation enhancements
- [GitHub #13991](https://github.com/zephyrproject-rtos/zephyr/issues/13991) - net: Spurious driver errors due to feeding packets into IP stack when it’s not fully initialized (assumed reason)
- [GitHub #13943](https://github.com/zephyrproject-rtos/zephyr/issues/13943) - net: QEMU Ethernet drivers are flaky (seemingly after “net\_buf” refactor)
- [GitHub #13941](https://github.com/zephyrproject-rtos/zephyr/issues/13941) - Alternatives for OpenThread settings
- [GitHub #13894](https://github.com/zephyrproject-rtos/zephyr/issues/13894) - stm32f429i\_disc1: Add DTS for USB controller
- [GitHub #13403](https://github.com/zephyrproject-rtos/zephyr/issues/13403) - USBD event and composite-device handling
- [GitHub #13232](https://github.com/zephyrproject-rtos/zephyr/issues/13232) - native\_posix doc: Add mention of virtual USB
- [GitHub #13151](https://github.com/zephyrproject-rtos/zephyr/issues/13151) - Update documentation on linking Zephyr within a flash partition
- [GitHub #12968](https://github.com/zephyrproject-rtos/zephyr/issues/12968) - dfu/mcuboot: solution for Set pending: don’t crash when image slot corrupt
- [GitHub #12860](https://github.com/zephyrproject-rtos/zephyr/issues/12860) - No test builds these files
- [GitHub #12814](https://github.com/zephyrproject-rtos/zephyr/issues/12814) - TCP connet Net Shell function seems to not working when using NET\_SOCKETS\_OFFLOAD
- [GitHub #12635](https://github.com/zephyrproject-rtos/zephyr/issues/12635) - tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_utils.c fail with Assertion failure on nrf52840
- [GitHub #12553](https://github.com/zephyrproject-rtos/zephyr/issues/12553) - List of tests that keep failing sporadically
- [GitHub #12537](https://github.com/zephyrproject-rtos/zephyr/issues/12537) - potential over-use of k\_spinlock
- [GitHub #12490](https://github.com/zephyrproject-rtos/zephyr/issues/12490) - Produced ELF does not follow the linux ELF spec
- [GitHub #12359](https://github.com/zephyrproject-rtos/zephyr/issues/12359) - Default address selection for IPv6 should follow RFC 6724
- [GitHub #12331](https://github.com/zephyrproject-rtos/zephyr/issues/12331) - Proposal to improve the settings subsystem
- [GitHub #12134](https://github.com/zephyrproject-rtos/zephyr/issues/12134) - I cannot see a Zephyr way to change the clock frequency at runtime
- [GitHub #12130](https://github.com/zephyrproject-rtos/zephyr/issues/12130) - Is zephyr targeting high-end phone or pc doing open ended computation on the roadmap?
- [GitHub #12027](https://github.com/zephyrproject-rtos/zephyr/issues/12027) - Make icount work for real on x86\_64
- [GitHub #11751](https://github.com/zephyrproject-rtos/zephyr/issues/11751) - Rework exception & fatal error handling framework
- [GitHub #11519](https://github.com/zephyrproject-rtos/zephyr/issues/11519) - Add at least build test for cc1200
- [GitHub #11490](https://github.com/zephyrproject-rtos/zephyr/issues/11490) - setup\_ipv6() treats event enums as bitmasks
- [GitHub #11296](https://github.com/zephyrproject-rtos/zephyr/issues/11296) - Possible ways to implement clock synchronisation over BLE
- [GitHub #11213](https://github.com/zephyrproject-rtos/zephyr/issues/11213) - NFFS: Handle unexpected Power Off
- [GitHub #11172](https://github.com/zephyrproject-rtos/zephyr/issues/11172) - ARM Cortex A Architecture support - ARMv8-A
- [GitHub #10996](https://github.com/zephyrproject-rtos/zephyr/issues/10996) - Add device tree support for usb controllers on x86
- [GitHub #10821](https://github.com/zephyrproject-rtos/zephyr/issues/10821) - ELCE: DT, Kconfig, EDTS path forward
- [GitHub #10534](https://github.com/zephyrproject-rtos/zephyr/issues/10534) - Can we get rid of zephyr-env.sh?
- [GitHub #10423](https://github.com/zephyrproject-rtos/zephyr/issues/10423) - log\_core.h error on pointer-to-int-cast on 64bit system
- [GitHub #10339](https://github.com/zephyrproject-rtos/zephyr/issues/10339) - gpio: Cleanup flags
- [GitHub #10305](https://github.com/zephyrproject-rtos/zephyr/issues/10305) - RFC: Add pin mask for gpio\_port\_xxx
- [GitHub #9947](https://github.com/zephyrproject-rtos/zephyr/issues/9947) - CMake build architecture documentation
- [GitHub #9904](https://github.com/zephyrproject-rtos/zephyr/issues/9904) - System timer handling with low-frequency timers
- [GitHub #9873](https://github.com/zephyrproject-rtos/zephyr/issues/9873) - External flash driver for the MX25Rxx
- [GitHub #9748](https://github.com/zephyrproject-rtos/zephyr/issues/9748) - NFFS issue after many writes by btsettings
- [GitHub #9506](https://github.com/zephyrproject-rtos/zephyr/issues/9506) - Ztest becomes unresponsive while running SMP tests
- [GitHub #9349](https://github.com/zephyrproject-rtos/zephyr/issues/9349) - Support IPv6 privacy extension RFC 4941
- [GitHub #9333](https://github.com/zephyrproject-rtos/zephyr/issues/9333) - Support for STM32 L1-series
- [GitHub #9330](https://github.com/zephyrproject-rtos/zephyr/issues/9330) - network: clean up / implement supervisor to manage net services
- [GitHub #9194](https://github.com/zephyrproject-rtos/zephyr/issues/9194) - generated syscall header files don’t have ifndef protection
- [GitHub #8833](https://github.com/zephyrproject-rtos/zephyr/issues/8833) - OpenThread: Minimal Thread Device (MTD) option is not building
- [GitHub #8539](https://github.com/zephyrproject-rtos/zephyr/issues/8539) - Categorize Kconfig options in documentation
- [GitHub #8262](https://github.com/zephyrproject-rtos/zephyr/issues/8262) - [Bluetooth] MPU FAULT on sdu\_recv
- [GitHub #8242](https://github.com/zephyrproject-rtos/zephyr/issues/8242) - File system (littlefs & FAT) examples
- [GitHub #8236](https://github.com/zephyrproject-rtos/zephyr/issues/8236) - DTS Debugging is difficult
- [GitHub #7305](https://github.com/zephyrproject-rtos/zephyr/issues/7305) - CMake improvements to modularize gperf targets
- [GitHub #6866](https://github.com/zephyrproject-rtos/zephyr/issues/6866) - build: requirements: No module named yaml and elftools
- [GitHub #6562](https://github.com/zephyrproject-rtos/zephyr/issues/6562) - Question: Is QP™ Real-Time Frameworks/RTOS or libev supported in Zephyr? Or any plan?
- [GitHub #6521](https://github.com/zephyrproject-rtos/zephyr/issues/6521) - Scheduler needs spinlock-based synchronization
- [GitHub #6496](https://github.com/zephyrproject-rtos/zephyr/issues/6496) - Question: Is dynamical module loader supported in Zephyr? Or any plan?
- [GitHub #6389](https://github.com/zephyrproject-rtos/zephyr/issues/6389) - OpenThread: otPlatRandomGetTrue() implementation is not up to spec, may lead to security issues
- [GitHub #6327](https://github.com/zephyrproject-rtos/zephyr/issues/6327) - doc: GPIO\_INT config option dependencies aren’t clear
- [GitHub #6293](https://github.com/zephyrproject-rtos/zephyr/issues/6293) - Refining Zephyr’s Device Driver Model
- [GitHub #6157](https://github.com/zephyrproject-rtos/zephyr/issues/6157) - SMP lacks low-power idle
- [GitHub #6084](https://github.com/zephyrproject-rtos/zephyr/issues/6084) - api: pinmux/gpio: It isn’t possible to set pins as input and output simultaneously
- [GitHub #5943](https://github.com/zephyrproject-rtos/zephyr/issues/5943) - OT: utilsFlashWrite does not take into account the write-block-size
- [GitHub #5695](https://github.com/zephyrproject-rtos/zephyr/issues/5695) - C++ Support doesn’t work
- [GitHub #5436](https://github.com/zephyrproject-rtos/zephyr/issues/5436) - Add LoRa Radio Support
- [GitHub #5027](https://github.com/zephyrproject-rtos/zephyr/issues/5027) - Enhance Testing and Test Coverage
- [GitHub #4973](https://github.com/zephyrproject-rtos/zephyr/issues/4973) - Provide Linux-style ERR\_PTR/PTR\_ERR/IS\_ERR macros
- [GitHub #4951](https://github.com/zephyrproject-rtos/zephyr/issues/4951) - Prevent full rebuilds on Kconfig changes
- [GitHub #4917](https://github.com/zephyrproject-rtos/zephyr/issues/4917) - Reintroduce generic “outputexports” target after CMake migration
- [GitHub #4830](https://github.com/zephyrproject-rtos/zephyr/issues/4830) - device tree: generate pinmux
- [GitHub #3943](https://github.com/zephyrproject-rtos/zephyr/issues/3943) - x86: scope SMAP support in Zephyr
- [GitHub #3866](https://github.com/zephyrproject-rtos/zephyr/issues/3866) - To optimize the layout of the meta data of mem\_slab & mem\_pool
- [GitHub #3810](https://github.com/zephyrproject-rtos/zephyr/issues/3810) - application/kernel rodata split
- [GitHub #3717](https://github.com/zephyrproject-rtos/zephyr/issues/3717) - purge linker scripts of macro-based meta-language
- [GitHub #3701](https://github.com/zephyrproject-rtos/zephyr/issues/3701) - xtensa: scope MPU enabling
- [GitHub #3636](https://github.com/zephyrproject-rtos/zephyr/issues/3636) - Define region data structures exposed by linker script
- [GitHub #3490](https://github.com/zephyrproject-rtos/zephyr/issues/3490) - Move stm32 boards dts file to linux dts naming rules
- [GitHub #3488](https://github.com/zephyrproject-rtos/zephyr/issues/3488) - Dissociate board names from device tree file names
- [GitHub #3469](https://github.com/zephyrproject-rtos/zephyr/issues/3469) - Unify flash and code configuration across targets
- [GitHub #3429](https://github.com/zephyrproject-rtos/zephyr/issues/3429) - Add TSL2560 ambient light sensor driver
- [GitHub #3428](https://github.com/zephyrproject-rtos/zephyr/issues/3428) - Add HTU21D humidity sensor driver
- [GitHub #3427](https://github.com/zephyrproject-rtos/zephyr/issues/3427) - Add MPL3115A2 pressure sensor driver
- [GitHub #3397](https://github.com/zephyrproject-rtos/zephyr/issues/3397) - LLDP: Implement local MIB support for optional TLVs
- [GitHub #3276](https://github.com/zephyrproject-rtos/zephyr/issues/3276) - Dynamic Frequency Scaling
- [GitHub #3156](https://github.com/zephyrproject-rtos/zephyr/issues/3156) - xtensa: Support C++
- [GitHub #3098](https://github.com/zephyrproject-rtos/zephyr/issues/3098) - extend tests/kernel/arm\_irq\_vector\_table to other platforms
- [GitHub #3044](https://github.com/zephyrproject-rtos/zephyr/issues/3044) - How to create a Zephyr ROM library
- [GitHub #2925](https://github.com/zephyrproject-rtos/zephyr/issues/2925) - cross-platform support for interrupt tables/code in RAM or ROM
- [GitHub #2814](https://github.com/zephyrproject-rtos/zephyr/issues/2814) - Add proper support for running Zephyr without a system clock
- [GitHub #2807](https://github.com/zephyrproject-rtos/zephyr/issues/2807) - remove sprintf() and it’s brethen
- [GitHub #2664](https://github.com/zephyrproject-rtos/zephyr/issues/2664) - Running SanityCheck in Windows
- [GitHub #2338](https://github.com/zephyrproject-rtos/zephyr/issues/2338) - ICMPv6 “Packet Too Big” support
- [GitHub #2307](https://github.com/zephyrproject-rtos/zephyr/issues/2307) - DHCPv6
- [GitHub #1903](https://github.com/zephyrproject-rtos/zephyr/issues/1903) - Wi-Fi Host Stack
- [GitHub #1897](https://github.com/zephyrproject-rtos/zephyr/issues/1897) - Thread over BLE
- [GitHub #1583](https://github.com/zephyrproject-rtos/zephyr/issues/1583) - NFFS requires 1-byte unaligned accesses to flash
- [GitHub #1511](https://github.com/zephyrproject-rtos/zephyr/issues/1511) - qemu\_nios2 should use the GHRD design
- [GitHub #1468](https://github.com/zephyrproject-rtos/zephyr/issues/1468) - Move NATS support from sample to a library + API
- [GitHub #1205](https://github.com/zephyrproject-rtos/zephyr/issues/1205) - C++ usage
