---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/release-notes-2.3.html
original_path: releases/release-notes-2.3.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Zephyr 2.3.0

We are pleased to announce the release of Zephyr RTOS version 2.3.0.

Major enhancements with this release include:

- A new Zephyr CMake package has been introduced, reducing the need for
  environment variables
- A new Devicetree API, based on hierarchical macros, has been introduced. This
  new API allows the C code to access virtually all nodes and properties in a
  clean, organized fashion
- The kernel timeout API has been overhauled to be flexible and configurable,
  with future support for features like 64-bit and absolute timeouts in mind
- A new k\_heap/sys\_heap heap allocator has been introduced, with much better
  performance than the existing k\_mem\_pool/sys\_mem\_pool
- Zephyr now integrates with the TF-M (Trusted Firmware M) PSA-compliant
  framework
- The Bluetooth Low Energy Host now supports LE Advertising Extensions
- The CMSIS-DSP library is now included and integrated

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

- CVE-2020-10022: UpdateHub Module Copies a Variable-Sized Hash String
  into a fixed-size array.
- CVE-2020-10059: UpdateHub Module Explicitly Disables TLS
  Verification
- CVE-2020-10061: Improper handling of the full-buffer case in the
  Zephyr Bluetooth implementation can result in memory corruption.
- CVE-2020-10062: Packet length decoding error in MQTT
- CVE-2020-10063: Remote Denial of Service in CoAP Option Parsing Due
  To Integer Overflow
- CVE-2020-10068: In the Zephyr project Bluetooth subsystem, certain
  duplicate and back-to-back packets can cause incorrect behavior,
  resulting in a denial of service.
- CVE-2020-10069: An unchecked parameter in bluetooth data can result
  in an assertion failure, or division by zero, resulting in a denial
  of service attack.
- CVE-2020-10070: MQTT buffer overflow on receive buffer
- CVE-2020-10071: Insufficient publish message length validation in MQTT

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

A single high-priority bug is currently open:

- [GitHub #23364](https://github.com/zephyrproject-rtos/zephyr/issues/23364) - Bluetooth: bt\_recv deadlock on supervision timeout with
  pending GATT Write Commands

## API Changes

- HWINFO

  - The identifier data structure for hwinfo drivers is clarified. Drivers are
    responsible for ensuring that the identifier data structure is a sequence
    of bytes. The returned ID value is not supposed to be interpreted based on
    vendor-specific assumptions of byte order and should express the identifier
    as a raw byte sequence.
    The changes have an impact on users that use the hwinfo API to identify
    their devices.
    The sam0 driver byte swaps each 32 bit word of the 128 bit identifier to
    big endian.
    The nordic driver byte swaps the entire 64 bit word to big endian.
- I2C

  - Added a new API for recovering an I2C bus from situations where the I2C
    master and one or more I2C slaves are out of synchronization (e.g. if the
    I2C master was reset in the middle of an I2C transaction or if a noise
    pulse was induced on the SCL line).

### Deprecated in this release

- Kernel

  - k\_uptime\_delta\_32(), use k\_uptime\_delta()
  - Timeout values

    - All timeout values are now encapsulated k\_timeout\_t opaque structure when
      passing them to the kernel. If you want to revert to the previous s32\_t
      type for the timeout parameter, please enable
      CONFIG\_LEGACY\_TIMEOUT\_API
- Bluetooth

  - BT\_LE\_SCAN\_FILTER\_DUPLICATE, use BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE instead
  - BT\_LE\_SCAN\_FILTER\_WHITELIST, use BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST instead
  - bt\_le\_scan\_param::filter\_dup, use bt\_le\_scan\_param::options instead
  - bt\_conn\_create\_le(), use bt\_conn\_le\_create() instead
  - bt\_conn\_create\_auto\_le(), use bt\_conn\_le\_create\_auto() instead
  - bt\_conn\_create\_slave\_le(), use bt\_le\_adv\_start() instead with
    bt\_le\_adv\_param::peer set to the remote peers address.
  - BT\_LE\_ADV\_\* macros, use BT\_GAP\_ADV\_\* enums instead
- Boards

  - nrf51\_pca10028 has been renamed to nrf51dk\_nrf51422
  - nrf51\_pca10031 has been renamed to nrf51dongle\_nrf51422
  - nrf52810\_pca10040 has been renamed to nrf52dk\_nrf52810
  - nrf52\_pca10040 has been renamed to nrf52dk\_nrf52832
  - nrf52833\_pca10100 has been renamed to nrf52833dk\_nrf52833
  - nrf52811\_pca10056 has been renamed to nrf52840dk\_nrf52811
  - nrf52840\_pca10056 has been renamed to nrf52840dk\_nrf52840
  - nrf52840\_pca10059 has been renamed to nrf52840dongle\_nrf52840
  - nrf9160\_pca10090 has been renamed to nrf9160dk\_nrf9160
  - nrf52840\_pca10090 has been renamed to nrf9160dk\_nrf52840
  - nrf52\_pca20020 has been renamed to thingy52\_nrf52832
  - nrf5340\_dk\_nrf5340 has been renamed to nrf5340pdk\_nrf5340
  - efr32\_slwstk6061a has been renamed to efr32\_radio\_brd4250b
- Devicetree

  - The C macros generated from the devicetree in previous releases are now
    deprecated in favor of a new `<devicetree.h>` API.
  - See [Devicetree access from C/C++](../build/dts/api-usage.md#dt-from-c) for a high-level guide to the new API, and
    [Devicetree API](../build/dts/api/api.md#devicetree-api) for an API reference.
  - Use of the legacy macros now requires explicitly enabling
    `CONFIG_LEGACY_DEVICETREE_MACROS`. See [the Zephyr v2.3 legacy devicetree
    macro page](https://docs.zephyrproject.org/2.3.0/guides/dts/legacy-macros.html#dt-legacy-macros) for more information, including a link to a migration guide to
    the new API.

- Other

  - `MACRO_MAP` has been deprecated. Use `FOR_EACH` instead.
  - `BUILD_ASSERT_MSG` has been deprecated. Use `BUILD_ASSERT` instead.

### Removed APIs in this release

- The `INLINE` macro in `util.h` has been removed.
- `STACK_ANALYZE`, `stack_analyze` and `stack_unused_space_get` have been
  removed.

### Stable API changes in this release

- Bluetooth Mesh

  - The net\_idx parameter has been removed from the Health Client model
    APIs since it can be derived (by the stack) from the app\_idx parameter
- Networking

  - The NET\_DEVICE\_INIT(), NET\_DEVICE\_INIT\_INSTANCE(), NET\_DEVICE\_OFFLOAD\_INIT()
    and ETH\_NET\_DEVICE\_INIT() macros changed and take a device power management
    function pointer parameter. If networking PM is not implemented for the
    specific network device, the device\_pm\_control\_nop value can be used.
- Video

  - The video\_dequeue() API call now takes a k\_timeout\_t for the timeout
    parameter. This reverts to s32\_t if CONFIG\_LEGACY\_TIMEOUT\_API is enabled.
- Floating Point Services

  - FLOAT and FP\_SHARING Kconfig options have been renamed to FPU and FPU\_SHARING,
    respectively.

## Kernel

- A new general purpose memory allocator, sys\_heap/k\_heap, has been added
  to Zephyr with more conventional API/behavior, better space
  efficiency and higher performance than the pre-existing mem\_pool.
  The older mem\_pool APIs are, by default, wrappers around this new
  heap backend and will be deprecated in an upcoming release. The
  original implementation remains available for this release via
  disabling CONFIG\_MEM\_POOL\_HEAP\_BACKEND.
- The timeout arguments to all kernel calls are now a “k\_timeout\_t”
  type instead of a 32 bit millisecond count. These can be
  initialized in arbitrary time units (ns/us/ms, ticks), be
  interpreted relative to either current time or system start, and be
  expressed in 64 bit quantities. This involves a minor change to the
  API, so the original API is still available in a completely
  source-compatible way via CONFIG\_LEGACY\_TIMEOUT\_API.
- Simplified dummy thread implementation and properly name idle threads
- Centralized new thread priority check
- Refactored device structures and introduced struct init\_entry which is
  a generic init end-point. SYS\_INIT() generates only a struct init\_entry via
  calling INIT\_ENTRY\_DEFINE(). Also removed struct deviceconfig leaving
  struct device to own everything now.

## Architectures

- ARC:

  - Changed to automatic generation of privilege stack for ARC MPU V2 to
    avoid the potential waste of memory When USERSPACE is configured
  - Enhanced runtime programming for the MPU v3 by making the gap-filling
    of kernel memory a user-configurable feature
  - Refactored the thread switch code in epilogue of irq and exception
  - Refactored the assembly codes for better maintenance
  - Fixed the behavior of ARC timer driver
  - Fixed the behavior of ARC SMP
  - Fixed the wrong configurations of ARC boards in Kconfig and DTS
- ARM:

  - CMSIS has been moved out of the main tree and now resides in its
    own standalone module repository
  - Updated CMSIS version to 5.7.0
  - Added CMSIS-DSP library integration
  - Added semihosting console support
  - Cleanups and improvements to the Cortex-M exception vector table
  - Fixed the behavior of Cortex-M spurious IRQ handler
  - Fixed parsing of Cortex-M MemManage Stacking Errors
  - Fixed the arch\_cpu\_idle() implementation for Cortex-M and Cortex-R
  - Renamed Cortex-R architecture port to cortex\_a\_r in preparation for the
    AArch32 Cortex-A architecture port
  - Added processor exception handling and reporting framework for Cortex-R
  - Added nested interrupt support on AArch32 Cortex-R and AArch64 Cortex-A
  - Refactored Cortex-R interrupt system to remove fake multi-level interrupt
    controller abstraction scheme
- POSIX:

  - Added support for building on ARM hosts
- RISC-V:

  - Added support for hard floating point for RISC-V
  - Added march and mabi options to Kconfig
  - Fixed compilation warning for platforms without PLIC
- x86:

  - Instrumented code for timing information
  - Added ability for SoC to add MMU regions
  - x86 FPU sharing symbols renamed
  - early\_serial: extended to support MMIO UART

## Boards & SoC Support

- Added support for these SoC series:

  - Broadcom Viper BCM58402
  - Infineon XMC4500 SoC
  - Nordic nRF52820 SoC
  - NXP LPC55S16 SoC
  - SiLabs EFR32BG13P SoC
  - STM32L5 series of Ultra-low-power MCUs
- Added support for these ARM boards:

  - 96Boards AeroCore 2
  - Adafruit Feather nRF52840 Express
  - Adafruit Feather STM32F405 Express
  - Black STM32 F407VE Development Board
  - Black STM32 F407ZG Pro Development Board
  - Broadcom BCM958402M2
  - EFR32 BRD4104A (SLWRB4104A)
  - Infineon XMC45-RELAX-KIT
  - nRF52820 emulation on nRF52833 DK
  - nrf9160 INNBLUE21
  - nrf9160 INNBLUE22
  - NXP LPCXpresso55S16
  - SEGGER IP Switch Board
  - ST Nucleo H743ZI
  - ST Nucleo F303RE
  - ST Nucleo L552ZE-Q
- Made these changes in other boards

  - `up_squared` now defaults to the x86\_64 architecture
  - `intel_s1000` now supports SMP
- Added support for these following shields:

  - Espressif ESP-8266 Module
  - MikroElektronika ADC Click
  - MikroElectronica Eth Click
  - ST X-NUCLEO-IKS02A1: MEMS Inertial and Environmental Multi sensor shield

## Drivers and Sensors

- ADC

  - Added support for STM32G4, STM32L1 and STM32H7 series
  - Enabled internal voltage reference source on stm32
  - Added Microchip MCP320x driver
- Audio

  - N/A
- Bluetooth

  - Added an RX thread on stm32wb hci wrapper
  - Improved BLE support for rv32m1\_vega:

    - Added Resolvable Private Address support
    - Enabled power saving support
    - Added 2 Mbps PHY support
    - Enabled controller-based privacy
- CAN

  - Converted can-primary alias to zephyr,can-primary chosen property
  - Converted loopback driver to use a thread to send frames
- Clock Control

  - Enabled MSI range config in PLL mode on stm32
  - Fixed AHB clock computation based on core on stm32h7
- Console

  - Fixed USB initialization
  - Added semihosting console
- Counter

  - Added support on stm32h7 and stm32l0
  - Fixed alarm tick count on stm32
  - Added Maxim DS3231 driver
  - Added NXP Kinetis LPTMR driver
- Crypto

  - Added driver for nRF ECB
  - Added CAP\_NO\_IV\_PREFIX capability to stm32 driver
- DAC

  - Added stm32l0 series support
  - Added DAC shell
  - Added NXP Kinetis DAC and DAC32 drivers
- Debug

  - N/A
- Display

  - Added power management support to st7789v driver
  - Reworked controller memory initialization in ssd16xx driver
  - Updated st7789v driver to set x-offset and y-offset properties properly
- DMA

  - Enabled use of DMAMUX on stm32l4+ and stm32wb
  - Various fixes on stm32 dma management
- EEPROM

  - N/A
- Entropy

  - Removed Kconfig HAS\_DTS\_ENTROPY
  - Implemented ISR specific get entropy call in gecko driver
- ESPI

  - Various fixes in Microchip driver
- Ethernet

  - Added SAM E54 max queue count referencing
  - Added SAM0 family support to gmac driver
  - Added sam4e support to queue in gmac
  - Added network power management support to mcux
  - Added VLAN support to enc28j60
  - Added VLAN support to stm32
  - Added Ethernet cable link status support to gmac
  - Added support for i.MXRT1060 family to mcux
  - Added support for getting manual MAC address from devicetree
  - Added support for enabling random MAC address from devicetree
  - Various fixes to setup and cache handling in gmac
  - Fixed how unique MAC address is determined in mcux
  - Fixed Ethernet cable link detection in gecko
  - Fixed stm32 when receiving data during initialization
- Flash

  - Added logs on stm32
  - Fixed wrong bank erasing on stm32g4
  - Various fixes in nrf\_qspi\_nor driver
  - Added driver for AT456 compatible SPI flash chips
  - Enabled support for SAMV71
- GPIO

  - Added mcp23s17 driver
  - Added STM32L5 support to stm32 driver
  - Added interrupt support to sx1509b driver
  - Fixed interrupt handling in sifive, intel\_apl, mchp\_xec, mcux\_igpio driver
  - Various fixes in intel\_apl driver
  - Added MCP23S17 driver
  - Fixed port 1 interrupts in mcux lpc driver
- Hardware Info

  - Fixed ESP32 implementation
  - Updated byte order in all drivers
- I2C

  - Added support to stm32h7
  - Added write/read and bus recovery commands to shell
  - Added bus recovery function to gpio bitbang driver
  - Fixed fast and fast+ mode bus speeds in several drivers
  - Added mcux flexcomm driver
- I2S

  - Added I2S master DMA support and clock output to stm32 driver
  - Enabled SAMV71
- IEEE 802.15.4

  - Added Decawave DW1000 driver
  - Added “no auto start” option and local MAC address support to rf2xx
  - Added support for Frame Pending Bit (FPB) handling in nrf5
  - Added CSMA CA transmit capability to nrf5
  - Added PAN coordinator mode support to nrf5
  - Added support for promiscuous mode to nrf5
  - Added support for energy scan function to nrf5
  - Fixed RX timestamp handling in nrf5
  - Various fixes to rf2xx
- Interrupt Controller

  - Fixed PLIC register space
  - Added support for STM32L5 series
  - Added GIC V3 driver
  - Fixed ICFGRn access and config in GIC driver
  - Optimized the arc v2 interrupt unit driver
- IPM

  - Added CAVS DSP Intra-DSP Communication (IDC) driver
- Keyboard Scan

  - Added interrupt support to the ft5336 touch controller driver
  - Added SDL mouse driver
- LED

  - N/A
- LED Strip

  - N/A
- LoRa

  - Added a LoRa shell
  - Replaced counter driver usage with k\_timer calls
  - Various fixes in sx1276 driver
- Modem

  - Added support for GSM 07.10 muxing protocol to generic GSM modem
  - Added support for modem commands that do not have a line ending
  - Added automatic detection of ublox-sara-r4 modem type
  - Added automatic setting of APN for ublox-sara-r4
  - Added sendmsg() support to ublox-sara-r4
  - Fixed UDP socket closing in ublox-sara-r4
  - Fixed RSSI calculation for Sara U201
  - Fixed TCP context release and RX socket src/dst port assignment in wncm14a2a
  - Changed PPP driver connection to generic GSM modem
- PECI

  - Added Microchip XEC driver
- Pinmux

  - Fixed compilation errors in rv32m1\_vega pinmux
- PS/2

  - Tuned PS2 driver to support several mice brands
- PWM

  - Added support to stm32h7
  - Enhanced mcux ftm driver to configure pwm in ticks and allow configuring the clock prescaler
  - Added mcux tpm driver
  - Fixed nrfx driver to wait until PWM is stopped before restarting it
- Sensor

  - Added support for Analog Devices ADXL345 3-axis I2C accelerometer
  - Added Infineon DPS310 driver
  - Fixed temperature conversion in SI7006 driver
  - Added Honeywell MPR driver
  - Added BQ27421 driver
  - Added weighted average filter to NXP Kinetis temperature driver
  - Enabled single shot mode in ENS210 driver
  - Added forced sampling mode to BME280 driver
  - Added IIS2MDC magnetometer driver
  - Added IIS2DLPC accelerometer driver
  - Added ISM330DHCX IMU driver
  - Added MEC tachometer driver
  - Fixed I2C and SPI bus communication in LIS2DH driver
- Serial

  - Added uart\_mux driver that is used in GSM 07.10 muxing protocol
  - Added support for parity setting from dts on stm32
  - Added support for stm32l5
  - Various fixes in ns16550 driver
  - Added XMC driver
  - Added interrupt and runtime configuration support to Xilinx driver
  - Fixed interrupt support in sifive driver
  - Enhanced nrfx driver TX only mode support
  - Added SAMV71 support to sam driver
- SPI

  - Added support for DMA client on stm32
  - Increased clock frequency in mcux flexcomm driver
  - Added power management support to cc13xx\_cc26xx driver
- Timer

  - Various fixes in stm32\_lptim driver
  - Removed RTC1 dependency from nrf driver
  - Various fixes in arcv2\_timer0 driver
  - Fixed TICKLESS=n processing in nrf\_rtc and stm32\_lptim drivers
  - Added CAVS DSP wall clock timer driver
  - Implemented tickless support in xlnx\_psttc\_timer driver
- USB

  - Added experimental USB Audio implementation.
  - Added support to stm32wb
  - Fixed PMA leak at reset on stm32
  - Various fixes in usb\_dc\_nrfx driver
  - Refactored usb\_dc\_mcux\_ehci driver
- Video

  - Added dedicated video init priority
  - Various fixes in sw\_generator and mcux\_csi
  - Fixed video buffer alignment
- Watchdog

  - Added support on stm32g0
  - Disabled iwdg at boot on stm32
- WiFi

  - Added scan completion indication to eswifi
  - Added support to ESP8266 and ESP32

## Networking

- Converted networking to use new k\_timeout\_t infrastructure
- Enhanced new TCP stack support
- Added minimal support for TFTP client (RFC 1350)
- Added support for network device driver power management
- Added support for socketpair() BSD socket API
- Added support for QEMU user networking (SLIRP)
- Added support to disable automatic network attachment in OpenThread
- Added support for Frame Pending Bit handling in OpenThread
- Added support for RX frame handling in OpenThread
- Added support for TX started notification in OpenThread
- Added support for HW CSMA CA in OpenThread
- Added support for promiscuous mode in OpenThread
- Added support for reading OPAQUE resources with OMA TLV in LWM2M
- Added config to enable PAN coordinator mode in IEEE 802.15.4
- Added config to enable promiscuous mode in IEEE 802.15.4
- Added support for subscribe in Azure cloud sample
- Added support for queue mode in lwm2m\_client sample
- Added support to allow change of the QEMU Ethernet interface name
- Added support for PPP IPCP to negotiate used DNS servers
- Added support for setting hostname in DHCPv4 request
- Fixed binding AF\_PACKET socket type multiple times
- Fixed LLDPDU data in sent LLDP packets
- Fixed and enhance Google IoT sample application documentation
- Fixed MQTT cloud sample when polling incoming messages
- Fixed LWM2M socket error handling, and pending and reply handling during start
- Fixed LWM2M retransmission logic
- Fixed LWM2M Cell ID resource initialization
- Fixed COAP pending and reply handling
- Fixed wpan\_serial sample application and enable USB during initialization
- Fixed HTTP client payload issue on HTTP upload
- Fixed MQTT Websocket incoming data handling and accept packets only in RX
- Fixed MQTT Publish message length validation
- Fixed IEEE 802.15.4 received frame length validation
- IEEE 802.15.4: avoided ACK processing when not needed
- IEEE 802.15.4: Now allows energy detection scan unconditionally

## Bluetooth

- Host:

  - Support for LE Advertising Extensions has been added.
  - The Host is now 5.2 compliant, with support for EATT, L2CAP ECRED mode and
    all new GATT PDUs.
  - New application-controlled data length and PHY update APIs.
  - Legacy OOB pairing support has been added.
  - Multiple improvements to OOB data access and pairing.
  - The Host now uses the new thread analyzer functionality.
  - Multiple bug fixes and improvements
- BLE split software Controller:

  - The Controller is now 5.2 compliant.
  - A new HCI USB H4 driver has been added, which can interact with BlueZ’s
    counterpart Host driver.
  - PHY support is now configurable.
  - Only control procedures supported by the peer are now used.
  - The Nordic nRF52820 IC is now supported
  - OpenISA/RV32M1:

    - 2 Mbps PHY support.
    - Radio deep sleep mode support.
    - Controller-based privacy support.
- BLE legacy software Controller:

  - The legacy Controller has been removed from the tree.

## Build and Infrastructure

- Zephyr CMake package

  - The Zephyr main repository now includes a Zephyr CMake package.
    This allows for registering Zephyr in the CMake user package registry and
    allows for easier integration into Zephyr applications, by using the CMake
    function, `find_package(Zephyr ...)`.
    Registering the Zephyr CMake package in the CMake user package registry
    removes the need for setting of `ZEPHYR_BASE`, sourcing `zephyr-env.sh`,
    or running `zephyr-env.cmd`.
  - A new `west` extension command, `west zephyr-export` is introduced for easy
    registration of Zephyr CMake package in the CMake user package registry.
  - Zephyr Build Configuration CMake package hook.
    Zephyr offers the possibility of configuring the Zephyr build system through
    a Zephyr Build Configuration package. A single Zephyr workspace
    `ZephyrBuildConfig.cmake` will be loaded if present in the Zephyr
    workspace. This allows users to configure the Zephyr build system on a per
    workspace setup, as an alternative to using a `.zephyrrc` system wide file.
- Devicetree

  - A new [Devicetree API](../build/dts/api/api.md#devicetree-api) was added. This API is not generated, but is
    still included via `<devicetree.h>`.

    See [the Zephyr v2.3 legacy devicetree macro page](https://docs.zephyrproject.org/2.3.0/guides/dts/legacy-macros.html#dt-legacy-macros) for more information,
    including a link to a migration guide to the new API.

    The [Devicetree HOWTOs](../build/dts/howtos.md#dt-howtos) page has been extended for the new API, and a new
    [Devicetree access from C/C++](../build/dts/api-usage.md#dt-from-c) API usage guide was also added.

## Libraries / Subsystems

- Disk

  - Add stm32 sdmmc disk access driver, supports stm32f7 and stm32l4
- Random

  - Removed the `rand32_timestamp` driver.
- POSIX subsystem:

  - socketpair() function implemented.
  - eventfd() function (Linux-like extension) implemented.
- Power management:

  - Add system and device power management support on TI CC13x2/CC26x2.

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Documentation

- New API overview page added.
- Reference pages have been cleaned up and organized.
- The Devicetree documentation has been expanded significally.
- The project roles have been overhauled in the Contribution Guidelines pages.
- The documentation on driver-specific APIs has been simplified.
- Documentation for new APIs, boards and samples.

## Tests and Samples

- Added samples for USB Audio Class.
- Added sample for using POSIX read()/write() with network sockets.

## Issue Related Items

These GitHub issues were addressed since the previous 2.2.0 tagged
release:

- [GitHub #25991](https://github.com/zephyrproject-rtos/zephyr/issues/25991) - [net][net.socket.select][imx-rt series] test fails (k\_uptime\_get\_32() - tstamp <= FUZZ is false)
- [GitHub #25990](https://github.com/zephyrproject-rtos/zephyr/issues/25990) - tests/net/socket/select failed on sam\_e70\_xplained board.
- [GitHub #25960](https://github.com/zephyrproject-rtos/zephyr/issues/25960) - tests/net/socket/socketpair failed on mimxrt1050\_evk and sam\_e70\_xplained.
- [GitHub #25948](https://github.com/zephyrproject-rtos/zephyr/issues/25948) - Function i2c\_transfer stops execution for I2C\_SAM0
- [GitHub #25944](https://github.com/zephyrproject-rtos/zephyr/issues/25944) - driver: timer: stm32\_lptim: Extra ticks count
- [GitHub #25926](https://github.com/zephyrproject-rtos/zephyr/issues/25926) - k\_cycle\_get\_32() returns 0 in native\_posix
- [GitHub #25925](https://github.com/zephyrproject-rtos/zephyr/issues/25925) - tests: net: socket: socketpair: fails due to empty message header name
- [GitHub #25920](https://github.com/zephyrproject-rtos/zephyr/issues/25920) - Compilation error when CONFIG\_BOOTLOADER\_MCUBOOT=y specified
- [GitHub #25904](https://github.com/zephyrproject-rtos/zephyr/issues/25904) - kernel: k\_queue\_get return NULL before timeout
- [GitHub #25901](https://github.com/zephyrproject-rtos/zephyr/issues/25901) - timer: nrf\_rtc\_timer: Subtraction underflow causing 8 minute time skips
- [GitHub #25895](https://github.com/zephyrproject-rtos/zephyr/issues/25895) - driver: timer: stm32\_lptim: backup domain is reset
- [GitHub #25893](https://github.com/zephyrproject-rtos/zephyr/issues/25893) - Application syscalls in usermode gives bus fault with stacking error
- [GitHub #25887](https://github.com/zephyrproject-rtos/zephyr/issues/25887) - legacy timeout API does not work as expected
- [GitHub #25880](https://github.com/zephyrproject-rtos/zephyr/issues/25880) - stm32wb: Unable to use BLE and USB host simultaneously.
- [GitHub #25870](https://github.com/zephyrproject-rtos/zephyr/issues/25870) - tests/kernel/timer/timer\_api fails conversion tests with large offset
- [GitHub #25863](https://github.com/zephyrproject-rtos/zephyr/issues/25863) - Where is the definition of SystemInit()?
- [GitHub #25859](https://github.com/zephyrproject-rtos/zephyr/issues/25859) - mesh example not working with switched off dcdc?
- [GitHub #25847](https://github.com/zephyrproject-rtos/zephyr/issues/25847) - Problems using math functions and double.
- [GitHub #25824](https://github.com/zephyrproject-rtos/zephyr/issues/25824) - Unpacked bt\_l2cap\_le\_conn\_rsp struct is causing corrupt L2CAP connection request responses on some platforms
- [GitHub #25820](https://github.com/zephyrproject-rtos/zephyr/issues/25820) - kernel: k\_timer\_start(timer, K\_FOREVER, K\_NO\_WAIT) expires immediately
- [GitHub #25811](https://github.com/zephyrproject-rtos/zephyr/issues/25811) - K22F USB Console/Shell
- [GitHub #25797](https://github.com/zephyrproject-rtos/zephyr/issues/25797) - [Coverity CID :210607] Uninitialized scalar variable in tests/net/socket/socketpair/src/test\_socketpair\_happy\_path.c
- [GitHub #25796](https://github.com/zephyrproject-rtos/zephyr/issues/25796) - [Coverity CID :210579] Uninitialized scalar variable in tests/net/socket/socketpair/src/test\_socketpair\_happy\_path.c
- [GitHub #25795](https://github.com/zephyrproject-rtos/zephyr/issues/25795) - [Coverity CID :210564] Uninitialized scalar variable in tests/lib/cmsis\_dsp/distance/src/u32.c
- [GitHub #25793](https://github.com/zephyrproject-rtos/zephyr/issues/25793) - [Coverity CID :210561] Resource leak in tests/net/socket/socketpair/src/test\_socketpair\_unsupported\_calls.c
- [GitHub #25791](https://github.com/zephyrproject-rtos/zephyr/issues/25791) - [Coverity CID :210614] Explicit null dereferenced in tests/lib/cmsis\_dsp/distance/src/f32.c
- [GitHub #25789](https://github.com/zephyrproject-rtos/zephyr/issues/25789) - [Coverity CID :210586] Explicit null dereferenced in tests/lib/cmsis\_dsp/distance/src/f32.c
- [GitHub #25788](https://github.com/zephyrproject-rtos/zephyr/issues/25788) - [Coverity CID :210581] Dereference before null check in subsys/net/lib/sockets/socketpair.c
- [GitHub #25787](https://github.com/zephyrproject-rtos/zephyr/issues/25787) - [Coverity CID :210571] Explicit null dereferenced in tests/subsys/openthread/radio\_test.c
- [GitHub #25785](https://github.com/zephyrproject-rtos/zephyr/issues/25785) - [Coverity CID :210549] Explicit null dereferenced in tests/subsys/openthread/radio\_test.c
- [GitHub #25780](https://github.com/zephyrproject-rtos/zephyr/issues/25780) - [Coverity CID :210612] Negative array index read in samples/net/sockets/socketpair/src/socketpair\_example.c
- [GitHub #25779](https://github.com/zephyrproject-rtos/zephyr/issues/25779) - [Coverity CID :209942] Pointer to local outside scope in subsys/net/ip/tcp2.c
- [GitHub #25774](https://github.com/zephyrproject-rtos/zephyr/issues/25774) - [Coverity CID :210615] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25773](https://github.com/zephyrproject-rtos/zephyr/issues/25773) - [Coverity CID :210613] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25772](https://github.com/zephyrproject-rtos/zephyr/issues/25772) - [Coverity CID :210609] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25771](https://github.com/zephyrproject-rtos/zephyr/issues/25771) - [Coverity CID :210608] Incompatible cast in tests/lib/cmsis\_dsp/fastmath/src/f32.c
- [GitHub #25770](https://github.com/zephyrproject-rtos/zephyr/issues/25770) - [Coverity CID :210605] Incompatible cast in tests/lib/cmsis\_dsp/filtering/src/misc\_f32.c
- [GitHub #25769](https://github.com/zephyrproject-rtos/zephyr/issues/25769) - [Coverity CID :210603] Incompatible cast in tests/lib/cmsis\_dsp/filtering/src/misc\_f32.c
- [GitHub #25768](https://github.com/zephyrproject-rtos/zephyr/issues/25768) - [Coverity CID :210601] Incompatible cast in tests/lib/cmsis\_dsp/fastmath/src/f32.c
- [GitHub #25767](https://github.com/zephyrproject-rtos/zephyr/issues/25767) - [Coverity CID :210600] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25766](https://github.com/zephyrproject-rtos/zephyr/issues/25766) - [Coverity CID :210592] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25765](https://github.com/zephyrproject-rtos/zephyr/issues/25765) - [Coverity CID :210591] Incompatible cast in tests/lib/cmsis\_dsp/filtering/src/misc\_f32.c
- [GitHub #25764](https://github.com/zephyrproject-rtos/zephyr/issues/25764) - [Coverity CID :210590] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25763](https://github.com/zephyrproject-rtos/zephyr/issues/25763) - [Coverity CID :210577] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25762](https://github.com/zephyrproject-rtos/zephyr/issues/25762) - [Coverity CID :210576] Incompatible cast in tests/lib/cmsis\_dsp/filtering/src/misc\_f32.c
- [GitHub #25761](https://github.com/zephyrproject-rtos/zephyr/issues/25761) - [Coverity CID :210574] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25760](https://github.com/zephyrproject-rtos/zephyr/issues/25760) - [Coverity CID :210572] Incompatible cast in tests/lib/cmsis\_dsp/distance/src/f32.c
- [GitHub #25759](https://github.com/zephyrproject-rtos/zephyr/issues/25759) - [Coverity CID :210569] Incompatible cast in tests/lib/cmsis\_dsp/bayes/src/f32.c
- [GitHub #25758](https://github.com/zephyrproject-rtos/zephyr/issues/25758) - [Coverity CID :210567] Incompatible cast in tests/lib/cmsis\_dsp/fastmath/src/f32.c
- [GitHub #25757](https://github.com/zephyrproject-rtos/zephyr/issues/25757) - [Coverity CID :210565] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25756](https://github.com/zephyrproject-rtos/zephyr/issues/25756) - [Coverity CID :210563] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25755](https://github.com/zephyrproject-rtos/zephyr/issues/25755) - [Coverity CID :210560] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25754](https://github.com/zephyrproject-rtos/zephyr/issues/25754) - [Coverity CID :210556] Incompatible cast in tests/lib/cmsis\_dsp/matrix/src/unary\_f64.c
- [GitHub #25753](https://github.com/zephyrproject-rtos/zephyr/issues/25753) - [Coverity CID :210555] Incompatible cast in tests/lib/cmsis\_dsp/support/src/barycenter\_f32.c
- [GitHub #25752](https://github.com/zephyrproject-rtos/zephyr/issues/25752) - [Coverity CID :210551] Incompatible cast in tests/lib/cmsis\_dsp/matrix/src/unary\_f32.c
- [GitHub #25751](https://github.com/zephyrproject-rtos/zephyr/issues/25751) - [Coverity CID :210545] Incompatible cast in tests/benchmarks/cmsis\_dsp/basicmath/src/f32.c
- [GitHub #25737](https://github.com/zephyrproject-rtos/zephyr/issues/25737) - [Coverity CID :210585] Unchecked return value in samples/net/sockets/socketpair/src/socketpair\_example.c
- [GitHub #25736](https://github.com/zephyrproject-rtos/zephyr/issues/25736) - [Coverity CID :210583] Unchecked return value from library in samples/net/sockets/socketpair/src/socketpair\_example.c
- [GitHub #25731](https://github.com/zephyrproject-rtos/zephyr/issues/25731) - [Coverity CID :210568] Argument cannot be negative in tests/net/socket/socketpair/src/test\_socketpair\_happy\_path.c
- [GitHub #25730](https://github.com/zephyrproject-rtos/zephyr/issues/25730) - [Coverity CID :210553] Unchecked return value in tests/drivers/gpio/gpio\_basic\_api/src/test\_deprecated.c
- [GitHub #25727](https://github.com/zephyrproject-rtos/zephyr/issues/25727) - [Coverity CID :210611] Logically dead code in subsys/net/lib/sockets/socketpair.c
- [GitHub #25702](https://github.com/zephyrproject-rtos/zephyr/issues/25702) - BSD socket sendmsg() did not verify params in usermode
- [GitHub #25701](https://github.com/zephyrproject-rtos/zephyr/issues/25701) - MPU FAULT in nvs test on nrf52840dk\_nrf52840
- [GitHub #25698](https://github.com/zephyrproject-rtos/zephyr/issues/25698) - IPv6 prefix could be added multiple times to prefix timer list
- [GitHub #25697](https://github.com/zephyrproject-rtos/zephyr/issues/25697) - Example of Thread creation in documentation does not compile
- [GitHub #25694](https://github.com/zephyrproject-rtos/zephyr/issues/25694) - IPv6 RA prefix option invalid length
- [GitHub #25673](https://github.com/zephyrproject-rtos/zephyr/issues/25673) - Unable to use SPI1 when enabled without SPI0 on cc13xx/cc26xx
- [GitHub #25670](https://github.com/zephyrproject-rtos/zephyr/issues/25670) - Possible Null pointer dereferences in /subsys/logging/log\_msg.c
- [GitHub #25666](https://github.com/zephyrproject-rtos/zephyr/issues/25666) - tests: kernel: mem\_protect: syscalls: test\_string\_nlen fails
- [GitHub #25656](https://github.com/zephyrproject-rtos/zephyr/issues/25656) - shields: Can’t use multiple shields anymore
- [GitHub #25635](https://github.com/zephyrproject-rtos/zephyr/issues/25635) - ARM: TLS pointer may not be set correctly
- [GitHub #25621](https://github.com/zephyrproject-rtos/zephyr/issues/25621) - ESWiFi does not populate info about remote when invoking callback
- [GitHub #25614](https://github.com/zephyrproject-rtos/zephyr/issues/25614) - fix longstanding error in pthread\_attr\_t definition
- [GitHub #25613](https://github.com/zephyrproject-rtos/zephyr/issues/25613) - USB: CDC adds set line coding callback
- [GitHub #25612](https://github.com/zephyrproject-rtos/zephyr/issues/25612) - ARM: Cortex-M: CPU is not reporting Explicit MemManage Stacking Errors correctly
- [GitHub #25597](https://github.com/zephyrproject-rtos/zephyr/issues/25597) - west sign fails to find header size or padding
- [GitHub #25585](https://github.com/zephyrproject-rtos/zephyr/issues/25585) - QEMU special key handling is broken on qemu\_cortex\_a53
- [GitHub #25578](https://github.com/zephyrproject-rtos/zephyr/issues/25578) - nrf: clock control: nrf5340: using CLOCK\_CONTROL\_NRF\_K32SRC\_RC results in build failure
- [GitHub #25568](https://github.com/zephyrproject-rtos/zephyr/issues/25568) - nrf: clock\_control: Fatal error during initialization
- [GitHub #25561](https://github.com/zephyrproject-rtos/zephyr/issues/25561) - bluetooth: GATT lockup on split packets
- [GitHub #25555](https://github.com/zephyrproject-rtos/zephyr/issues/25555) - Unable to connect to Thread network (NRF52840DK)
- [GitHub #25527](https://github.com/zephyrproject-rtos/zephyr/issues/25527) - sample and writeup for socketpair
- [GitHub #25526](https://github.com/zephyrproject-rtos/zephyr/issues/25526) - Sanity Check Fails:
- [GitHub #25522](https://github.com/zephyrproject-rtos/zephyr/issues/25522) - settings: FCB back-end does not try to add record after the last compression attempt.
- [GitHub #25519](https://github.com/zephyrproject-rtos/zephyr/issues/25519) - wrong debug function cause kinds of building error
- [GitHub #25511](https://github.com/zephyrproject-rtos/zephyr/issues/25511) - arc em\_starterkit\_em11d failed in tests/kernel/timer/timer\_api
- [GitHub #25510](https://github.com/zephyrproject-rtos/zephyr/issues/25510) - arc EMSDP failed in tests/kernel/gen\_isr\_table
- [GitHub #25509](https://github.com/zephyrproject-rtos/zephyr/issues/25509) - OpenThread SED set link mode fail
- [GitHub #25493](https://github.com/zephyrproject-rtos/zephyr/issues/25493) - devicetree: nRF5340 application core DTSI is missing cryptocell node
- [GitHub #25489](https://github.com/zephyrproject-rtos/zephyr/issues/25489) - drivers: modem\_cmd\_handler: uninitialized variable used
- [GitHub #25483](https://github.com/zephyrproject-rtos/zephyr/issues/25483) - Bluetooth: controller: split: feature exchange not conform V5.0 core spec
- [GitHub #25480](https://github.com/zephyrproject-rtos/zephyr/issues/25480) - Unconditional source of shield configs can mess up configuration
- [GitHub #25478](https://github.com/zephyrproject-rtos/zephyr/issues/25478) - settings\_runtime\_set() not populating bt/cf
- [GitHub #25477](https://github.com/zephyrproject-rtos/zephyr/issues/25477) - dts: arm: Incorrect GIC interrupt spec order for AArch64 SoCs
- [GitHub #25471](https://github.com/zephyrproject-rtos/zephyr/issues/25471) - disco\_l475\_iot1 don’t write last small block
- [GitHub #25469](https://github.com/zephyrproject-rtos/zephyr/issues/25469) - Fix devicetree documentation for new API
- [GitHub #25468](https://github.com/zephyrproject-rtos/zephyr/issues/25468) - FRDM\_K82F DTS missing information for ADC-0
- [GitHub #25452](https://github.com/zephyrproject-rtos/zephyr/issues/25452) - Some USB samples targeting stm32 are malfunctioning
- [GitHub #25448](https://github.com/zephyrproject-rtos/zephyr/issues/25448) - serial: uart\_nrfx\_uarte: poll & async TX infinite hang
- [GitHub #25447](https://github.com/zephyrproject-rtos/zephyr/issues/25447) - cf\_set() returns 0 when no cfg is available
- [GitHub #25442](https://github.com/zephyrproject-rtos/zephyr/issues/25442) - Does Zephyr support USB host mode ?
- [GitHub #25437](https://github.com/zephyrproject-rtos/zephyr/issues/25437) - tests/lib/heap: sanitycheck timeout on STM32 boards
- [GitHub #25433](https://github.com/zephyrproject-rtos/zephyr/issues/25433) - Add vendor specific class custom usb device sample
- [GitHub #25427](https://github.com/zephyrproject-rtos/zephyr/issues/25427) - STM32 Ethernet driver build failure with CONFIG\_ASSERT=1
- [GitHub #25408](https://github.com/zephyrproject-rtos/zephyr/issues/25408) - STM32 Ethernet Driver: Fix driver crash caused by RX IRQ trigger
- [GitHub #25390](https://github.com/zephyrproject-rtos/zephyr/issues/25390) - driver: timer: arm arch timer PPI configuration to be taken from dt
- [GitHub #25386](https://github.com/zephyrproject-rtos/zephyr/issues/25386) - boards: shields: esp\_8266: There isn’t CI tests enabled
- [GitHub #25379](https://github.com/zephyrproject-rtos/zephyr/issues/25379) - Bluetooth mesh example not working
- [GitHub #25378](https://github.com/zephyrproject-rtos/zephyr/issues/25378) - Installation problems
- [GitHub #25369](https://github.com/zephyrproject-rtos/zephyr/issues/25369) - tests/drivers/gpio/gpio\_basic\_api: test\_gpio\_deprecated step fails on STM32 boards
- [GitHub #25366](https://github.com/zephyrproject-rtos/zephyr/issues/25366) - tests/drivers/counter/counter\_basic\_api: instable test status on STM32 boards
- [GitHub #25363](https://github.com/zephyrproject-rtos/zephyr/issues/25363) - tests/drivers/counter/counter\_basic\_api: Assertion failed on STM32 boards
- [GitHub #25354](https://github.com/zephyrproject-rtos/zephyr/issues/25354) - Fails to compile when SYS\_PM\_DIRECT\_FORCE\_MODE is true
- [GitHub #25351](https://github.com/zephyrproject-rtos/zephyr/issues/25351) - test:mimxrt1050\_evk:tests/subsys/usb/bos/: run failure
- [GitHub #25350](https://github.com/zephyrproject-rtos/zephyr/issues/25350) - Bluetooth: controller: Data transmission delayed by slave latency
- [GitHub #25349](https://github.com/zephyrproject-rtos/zephyr/issues/25349) - The b\_l072z\_lrwan1 board (STM32L0) doesn’t support flashing of firmware larger than bank 0
- [GitHub #25348](https://github.com/zephyrproject-rtos/zephyr/issues/25348) - test:mimxrt10xx\_evk:tests/kernel/mem\_protect/stackprot: get unexpected Stacking error
- [GitHub #25346](https://github.com/zephyrproject-rtos/zephyr/issues/25346) - Timestamp in LOG jumps 00:08:32
- [GitHub #25337](https://github.com/zephyrproject-rtos/zephyr/issues/25337) - LED pins always configured as PWM outputs
- [GitHub #25334](https://github.com/zephyrproject-rtos/zephyr/issues/25334) - SPI won’t build on microbit with I2C
- [GitHub #25332](https://github.com/zephyrproject-rtos/zephyr/issues/25332) - lib: updatehub: Don’t build after conversion from DT\_FLASH\_AREA to FLASH\_AREA macros
- [GitHub #25331](https://github.com/zephyrproject-rtos/zephyr/issues/25331) - test\_timer\_remaining() fails with assertion in timer\_api test
- [GitHub #25319](https://github.com/zephyrproject-rtos/zephyr/issues/25319) - MMU and USERSPACE not working on upsquared
- [GitHub #25312](https://github.com/zephyrproject-rtos/zephyr/issues/25312) - samples:mimxrt1010\_evk:samples/net/openthread/ncp: build error
- [GitHub #25289](https://github.com/zephyrproject-rtos/zephyr/issues/25289) - mcuboot incompatible with Nordic QSPI flash driver
- [GitHub #25287](https://github.com/zephyrproject-rtos/zephyr/issues/25287) - test/benchmarks/latency\_measure fails on nucleo\_f429zi and nucleo\_f207zg
- [GitHub #25284](https://github.com/zephyrproject-rtos/zephyr/issues/25284) - spi: stm32: dma\_client: Cannot use RX only configuration
- [GitHub #25276](https://github.com/zephyrproject-rtos/zephyr/issues/25276) - OpenThread not work after upgrade to latest version
- [GitHub #25272](https://github.com/zephyrproject-rtos/zephyr/issues/25272) - tests/drivers/gpio/gpio\_basic\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #25270](https://github.com/zephyrproject-rtos/zephyr/issues/25270) - fix userspace permissions in socketpair tests
- [GitHub #25263](https://github.com/zephyrproject-rtos/zephyr/issues/25263) - Can anyone tell me how can i use external qspi flash “mx25r64”(custom board with nrf52840 soc) for mcuboot slot1 and i’m using zephyr 2.2.0
- [GitHub #25260](https://github.com/zephyrproject-rtos/zephyr/issues/25260) - drivers: uart\_ns16550: device config\_info content mutated
- [GitHub #25251](https://github.com/zephyrproject-rtos/zephyr/issues/25251) - Post DT API migration review
- [GitHub #25247](https://github.com/zephyrproject-rtos/zephyr/issues/25247) - const qualifier lost on some device config\_info casts
- [GitHub #25246](https://github.com/zephyrproject-rtos/zephyr/issues/25246) - SHELL\_DEFAULT\_TERMINAL\_WIDTH should be configurable in Kconfig
- [GitHub #25241](https://github.com/zephyrproject-rtos/zephyr/issues/25241) - tests.drivers.spi\_loopback stm32wb55x fails transferring multiple buffers with dma
- [GitHub #25240](https://github.com/zephyrproject-rtos/zephyr/issues/25240) - Building usb audio sample hangs the pre-processor
- [GitHub #25234](https://github.com/zephyrproject-rtos/zephyr/issues/25234) - kernel.timer.tickless test fails on atsamd21\_xpro
- [GitHub #25233](https://github.com/zephyrproject-rtos/zephyr/issues/25233) - bad logic in test\_busy\_wait of tests/kernel/context
- [GitHub #25232](https://github.com/zephyrproject-rtos/zephyr/issues/25232) - driver: wifi: esp\_offload.c: Missing new timeout API conversion
- [GitHub #25230](https://github.com/zephyrproject-rtos/zephyr/issues/25230) - Lib: UpdateHub: Missing new timeout API conversion
- [GitHub #25224](https://github.com/zephyrproject-rtos/zephyr/issues/25224) - benchmark.kernel.latency test fails on atsame54\_xpro
- [GitHub #25221](https://github.com/zephyrproject-rtos/zephyr/issues/25221) - arch.arm.irq\_advanced\_features test fails on atsamd21\_xpro
- [GitHub #25216](https://github.com/zephyrproject-rtos/zephyr/issues/25216) - cc13xx and cc26xx handler for IRQ invoked multiple times
- [GitHub #25210](https://github.com/zephyrproject-rtos/zephyr/issues/25210) - CI seems to be stuck for my pull request
- [GitHub #25204](https://github.com/zephyrproject-rtos/zephyr/issues/25204) - soc: apollo\_lake: Disabling I2C support is not possible
- [GitHub #25200](https://github.com/zephyrproject-rtos/zephyr/issues/25200) - Build error in Sample App for OpenThread NCP
- [GitHub #25196](https://github.com/zephyrproject-rtos/zephyr/issues/25196) - tests: portability: cmsis\_rtos\_v2: hangs on nRF52, 53 and 91 nRF platforms
- [GitHub #25194](https://github.com/zephyrproject-rtos/zephyr/issues/25194) - tests: kernel: context: seems to be failing on Nordic platforms
- [GitHub #25191](https://github.com/zephyrproject-rtos/zephyr/issues/25191) - tests/drivers/console: drivers.console.semihost can’t work
- [GitHub #25190](https://github.com/zephyrproject-rtos/zephyr/issues/25190) - West - init/update module SHA with –depth = 1
- [GitHub #25185](https://github.com/zephyrproject-rtos/zephyr/issues/25185) - Adding CONFIG\_BT\_SETTINGS creates errors on bt\_hci\_core & bt\_gatt
- [GitHub #25184](https://github.com/zephyrproject-rtos/zephyr/issues/25184) - lldp: lldp\_send includes bug
- [GitHub #25183](https://github.com/zephyrproject-rtos/zephyr/issues/25183) - west build error after while “getting started” on ESP32
- [GitHub #25180](https://github.com/zephyrproject-rtos/zephyr/issues/25180) - tests: drivers/i2s/i2s\_api: Build failed on 96b\_argonkey
- [GitHub #25179](https://github.com/zephyrproject-rtos/zephyr/issues/25179) - tests/kernel/timer/timer\_api failed on iotdk board.
- [GitHub #25178](https://github.com/zephyrproject-rtos/zephyr/issues/25178) - tests/kernel/sched/schedule\_api failed on iotdk board.
- [GitHub #25177](https://github.com/zephyrproject-rtos/zephyr/issues/25177) - tests/drivers/counter/maxim\_ds3231\_api failed on frdm\_k64f.
- [GitHub #25176](https://github.com/zephyrproject-rtos/zephyr/issues/25176) - tests/kernel/context failed on multiple platforms.
- [GitHub #25174](https://github.com/zephyrproject-rtos/zephyr/issues/25174) - qemu test failures when running sanitycheck
- [GitHub #25169](https://github.com/zephyrproject-rtos/zephyr/issues/25169) - soc/arm/infineon\_xmc/4xxx/soc.h not found
- [GitHub #25161](https://github.com/zephyrproject-rtos/zephyr/issues/25161) - samples/cfb/display flickers with SSD1306
- [GitHub #25141](https://github.com/zephyrproject-rtos/zephyr/issues/25141) - Cannot use C++ on APPLICATION level initialization
- [GitHub #25140](https://github.com/zephyrproject-rtos/zephyr/issues/25140) - Unable to obtain dhcp lease
- [GitHub #25139](https://github.com/zephyrproject-rtos/zephyr/issues/25139) - USB HID mouse sample high input delay
- [GitHub #25130](https://github.com/zephyrproject-rtos/zephyr/issues/25130) - Bluetooth: controller: Incorrect version information
- [GitHub #25128](https://github.com/zephyrproject-rtos/zephyr/issues/25128) - Missing `python3-dev` dependency
- [GitHub #25123](https://github.com/zephyrproject-rtos/zephyr/issues/25123) - DAC is not described in soc of STM32L4xx series
- [GitHub #25109](https://github.com/zephyrproject-rtos/zephyr/issues/25109) - Flash tests fail on posix
- [GitHub #25101](https://github.com/zephyrproject-rtos/zephyr/issues/25101) - driver: gpio: mchp: GPIO initialization value doesn’t get reflected when using new flags
- [GitHub #25091](https://github.com/zephyrproject-rtos/zephyr/issues/25091) - drivers: eSPI: Incorrect handling of OOB registers leads to report wrong OOB packet len
- [GitHub #25084](https://github.com/zephyrproject-rtos/zephyr/issues/25084) - LLDP: missing net\_pkt\_set\_lldp in lldp\_send
- [GitHub #25083](https://github.com/zephyrproject-rtos/zephyr/issues/25083) - Networking samples are not able to connect with the TCP under qemu\_x86 after 9b055ec
- [GitHub #25067](https://github.com/zephyrproject-rtos/zephyr/issues/25067) - Insufficient ticker nodes for vendor implementations
- [GitHub #25057](https://github.com/zephyrproject-rtos/zephyr/issues/25057) - errors when running sanitycheck with tests/subsys/storage/stream/stream\_flash
- [GitHub #25036](https://github.com/zephyrproject-rtos/zephyr/issues/25036) - kernel: pipe: read\_avail / write\_avail syscalls
- [GitHub #25032](https://github.com/zephyrproject-rtos/zephyr/issues/25032) - build failure on lpcxpresso55s16\_ns
- [GitHub #25017](https://github.com/zephyrproject-rtos/zephyr/issues/25017) - [CI] m2gl025\_miv in Shippable CI systematically fails some tests
- [GitHub #25016](https://github.com/zephyrproject-rtos/zephyr/issues/25016) - BT\_LE\_ADV\_NCONN\_NAME doesn’t actually advertise name
- [GitHub #25015](https://github.com/zephyrproject-rtos/zephyr/issues/25015) - Bluetooth Isochronous Channels Support
- [GitHub #25012](https://github.com/zephyrproject-rtos/zephyr/issues/25012) - checkpatch.pl doesn’t match the vendor string properly
- [GitHub #25010](https://github.com/zephyrproject-rtos/zephyr/issues/25010) - disco\_l475\_iot1 don’t confirm MCUBoot slot-1 image
- [GitHub #24978](https://github.com/zephyrproject-rtos/zephyr/issues/24978) - RFC: use compatible name for prefix for device-specific API
- [GitHub #24970](https://github.com/zephyrproject-rtos/zephyr/issues/24970) - ieee802154 l2: no length check in frame validation
- [GitHub #24965](https://github.com/zephyrproject-rtos/zephyr/issues/24965) - RF2XX radio driver does automatic retransmission and OpenThread as well
- [GitHub #24963](https://github.com/zephyrproject-rtos/zephyr/issues/24963) - Slower OpenThread PSKc calculation
- [GitHub #24943](https://github.com/zephyrproject-rtos/zephyr/issues/24943) - Add a harness property to boards in sanitycheck’s hardware\_map
- [GitHub #24928](https://github.com/zephyrproject-rtos/zephyr/issues/24928) - Running Zephyr Bot tests on local machine
- [GitHub #24927](https://github.com/zephyrproject-rtos/zephyr/issues/24927) - stm32: Fix docs boards for doc generation
- [GitHub #24926](https://github.com/zephyrproject-rtos/zephyr/issues/24926) - Remove all uses of CONFIG\_LEGACY\_TIMEOUT\_API from the tree before 2.3
- [GitHub #24915](https://github.com/zephyrproject-rtos/zephyr/issues/24915) - accelerometer example no longer works for microbit
- [GitHub #24911](https://github.com/zephyrproject-rtos/zephyr/issues/24911) - arch: arm: aarch32: When CPU\_HAS\_FPU for Cortex-R5 is selected, prep\_c.c uses undefined symbols
- [GitHub #24909](https://github.com/zephyrproject-rtos/zephyr/issues/24909) - `find_package` goes into an infinite loop on windows
- [GitHub #24903](https://github.com/zephyrproject-rtos/zephyr/issues/24903) - Python detection when building documentation fails
- [GitHub #24889](https://github.com/zephyrproject-rtos/zephyr/issues/24889) - stm32f469i discovery board and samples/display/lvgl fails
- [GitHub #24869](https://github.com/zephyrproject-rtos/zephyr/issues/24869) - qemu\_x86: with icount enabled, crash in test\_syscall\_torture
- [GitHub #24853](https://github.com/zephyrproject-rtos/zephyr/issues/24853) - os: Precise data bus error with updatehub
- [GitHub #24842](https://github.com/zephyrproject-rtos/zephyr/issues/24842) - Support Building on Aarch64
- [GitHub #24840](https://github.com/zephyrproject-rtos/zephyr/issues/24840) - Unable to connect to OpenThread network after upgrade
- [GitHub #24805](https://github.com/zephyrproject-rtos/zephyr/issues/24805) - On x86, misalligned SSE accesses can occur when multithreading is enabled
- [GitHub #24784](https://github.com/zephyrproject-rtos/zephyr/issues/24784) - nRF: Busy wait clock is skewed vs. timer clock
- [GitHub #24773](https://github.com/zephyrproject-rtos/zephyr/issues/24773) - devicetree: allow generation of properties that don’t have a binding
- [GitHub #24751](https://github.com/zephyrproject-rtos/zephyr/issues/24751) - What is purpose of the CONFIG\_ADC\_X
- [GitHub #24744](https://github.com/zephyrproject-rtos/zephyr/issues/24744) - k\_thread\_join() taking a very long time on qemu\_cortex\_m3
- [GitHub #24733](https://github.com/zephyrproject-rtos/zephyr/issues/24733) - Misconfigured environment
- [GitHub #24727](https://github.com/zephyrproject-rtos/zephyr/issues/24727) - Unable allocate buffer to send mesh message
- [GitHub #24722](https://github.com/zephyrproject-rtos/zephyr/issues/24722) - OnePlus 7T & peripheral\_hr on NRF52 conn failure
- [GitHub #24720](https://github.com/zephyrproject-rtos/zephyr/issues/24720) - Build failure on intel\_s1000\_crb board for test case:” tests/kernel/smp”
- [GitHub #24718](https://github.com/zephyrproject-rtos/zephyr/issues/24718) - adc: stm32g4: Fix ADC instances naming
- [GitHub #24713](https://github.com/zephyrproject-rtos/zephyr/issues/24713) - ztest\_test\_fail() doesn’t always work
- [GitHub #24706](https://github.com/zephyrproject-rtos/zephyr/issues/24706) - mcumgr: fail to upgrade nRF target using nRF Connect
- [GitHub #24702](https://github.com/zephyrproject-rtos/zephyr/issues/24702) - tests/drivers/counter/counter\_basic\_api failed on frdm\_k64f board.
- [GitHub #24701](https://github.com/zephyrproject-rtos/zephyr/issues/24701) - tests/lib/cmsis\_dsp/transform failed on frdm\_k64f board.
- [GitHub #24695](https://github.com/zephyrproject-rtos/zephyr/issues/24695) - Board IP Can Not Be Set Manually
- [GitHub #24692](https://github.com/zephyrproject-rtos/zephyr/issues/24692) - FindPython3 has unexpected behavior on Windows
- [GitHub #24674](https://github.com/zephyrproject-rtos/zephyr/issues/24674) - Cannot generate code coverage report for unit tests using sanitycheck
- [GitHub #24665](https://github.com/zephyrproject-rtos/zephyr/issues/24665) - z\_cstart memory corruption (ARM CortexM)
- [GitHub #24661](https://github.com/zephyrproject-rtos/zephyr/issues/24661) - sanitycheck incorrect judgement with tests/drivers/gpio/gpio\_basic\_api.
- [GitHub #24660](https://github.com/zephyrproject-rtos/zephyr/issues/24660) - tests/benchmarks/sys\_kernel failed on nrf platforms
- [GitHub #24659](https://github.com/zephyrproject-rtos/zephyr/issues/24659) - tests/portability/cmsis\_rtos\_v2 failed on reel\_board.
- [GitHub #24653](https://github.com/zephyrproject-rtos/zephyr/issues/24653) - device\_pm: clarify and document usage
- [GitHub #24646](https://github.com/zephyrproject-rtos/zephyr/issues/24646) - Bluetooth: hci\_uart broken on master
- [GitHub #24645](https://github.com/zephyrproject-rtos/zephyr/issues/24645) - naming consistency for kernel object initializer macros
- [GitHub #24642](https://github.com/zephyrproject-rtos/zephyr/issues/24642) - kernel: pipe: simple test fails for pipe write / read of 3 bytes
- [GitHub #24641](https://github.com/zephyrproject-rtos/zephyr/issues/24641) - inconsistent timer behavior on native platforms
- [GitHub #24635](https://github.com/zephyrproject-rtos/zephyr/issues/24635) - tests/counter/counter\_basic\_api fails on mps2\_an385
- [GitHub #24634](https://github.com/zephyrproject-rtos/zephyr/issues/24634) - Invalid pin reported in gpio callback
- [GitHub #24626](https://github.com/zephyrproject-rtos/zephyr/issues/24626) - USB re-connection fails on SAM E70
- [GitHub #24612](https://github.com/zephyrproject-rtos/zephyr/issues/24612) - mimxrt1020\_evk: total freeze
- [GitHub #24601](https://github.com/zephyrproject-rtos/zephyr/issues/24601) - Bluetooth: Mesh: Config Client’s net\_key\_status pulls two key indexes, should pull one.
- [GitHub #24585](https://github.com/zephyrproject-rtos/zephyr/issues/24585) - How to read/write an big(>16K) file in littlefs shell sample on native posix board?
- [GitHub #24579](https://github.com/zephyrproject-rtos/zephyr/issues/24579) - Couldn’t get test results from device serial on mimxrt1050\_evk board.
- [GitHub #24576](https://github.com/zephyrproject-rtos/zephyr/issues/24576) - scripts/subfolder\_list.py: Support long paths
- [GitHub #24571](https://github.com/zephyrproject-rtos/zephyr/issues/24571) - #include <new> is not available
- [GitHub #24564](https://github.com/zephyrproject-rtos/zephyr/issues/24564) - NRF51822 BLE ~400uA idle current consumption
- [GitHub #24554](https://github.com/zephyrproject-rtos/zephyr/issues/24554) - hal\_infineon: Add new module for Infineon XMC HAL layer
- [GitHub #24553](https://github.com/zephyrproject-rtos/zephyr/issues/24553) - samples/subsys/shell/fs/ fail on native posix board
- [GitHub #24539](https://github.com/zephyrproject-rtos/zephyr/issues/24539) - How to complete userspace support for driver-specific API
- [GitHub #24534](https://github.com/zephyrproject-rtos/zephyr/issues/24534) - arch\_mem\_domain\_max\_partitions\_get() returns equal number for all architectures
- [GitHub #24533](https://github.com/zephyrproject-rtos/zephyr/issues/24533) - devicetree: are some defines missing from the bindings?
- [GitHub #24509](https://github.com/zephyrproject-rtos/zephyr/issues/24509) - Ethernet Sample Echo Failed in Nucleo\_f429zi - bisected
- [GitHub #24505](https://github.com/zephyrproject-rtos/zephyr/issues/24505) - Bluetooth: Mesh: Configuration Client: Add support for Model Subscription Get
- [GitHub #24500](https://github.com/zephyrproject-rtos/zephyr/issues/24500) - Failed to run the sample “Native Posix Ethernet”
- [GitHub #24497](https://github.com/zephyrproject-rtos/zephyr/issues/24497) - frdm\_k64f fatal error while using flash and TLS features together
- [GitHub #24490](https://github.com/zephyrproject-rtos/zephyr/issues/24490) - SPI-NOR driver not found in spi\_flash sample
- [GitHub #24485](https://github.com/zephyrproject-rtos/zephyr/issues/24485) - kernel: pipe: should return if >= min\_xfer bytes transferred and timeout is K\_FOREVER
- [GitHub #24484](https://github.com/zephyrproject-rtos/zephyr/issues/24484) - The file system shell example failed to build
- [GitHub #24479](https://github.com/zephyrproject-rtos/zephyr/issues/24479) - nrf-uarte problems with uart\_irq\_tx\_disable() in handler
- [GitHub #24464](https://github.com/zephyrproject-rtos/zephyr/issues/24464) - drivers: espi: XEC: Incorrect eSPI channel status handling leading to missed interrupts and callbacks
- [GitHub #24462](https://github.com/zephyrproject-rtos/zephyr/issues/24462) - File not truncated to actual size after calling fs\_close
- [GitHub #24457](https://github.com/zephyrproject-rtos/zephyr/issues/24457) - Common Trace Format - Failed to produce correct trace output
- [GitHub #24442](https://github.com/zephyrproject-rtos/zephyr/issues/24442) - samples/subsys/mgmt/mcumgr/smp\_svr: should enable BT and FS for nrf52 boards
- [GitHub #24439](https://github.com/zephyrproject-rtos/zephyr/issues/24439) - LPCXpresso55S69\_ns target : build failed
- [GitHub #24437](https://github.com/zephyrproject-rtos/zephyr/issues/24437) - smp\_svr samle doesn’t build for any target
- [GitHub #24431](https://github.com/zephyrproject-rtos/zephyr/issues/24431) - http\_client assumes request payload is non-binary
- [GitHub #24426](https://github.com/zephyrproject-rtos/zephyr/issues/24426) - syscall for pipe(2)
- [GitHub #24409](https://github.com/zephyrproject-rtos/zephyr/issues/24409) - When the delay parameter of k\_delayed\_work\_submit is K\_FOREVER, the system will crash
- [GitHub #24399](https://github.com/zephyrproject-rtos/zephyr/issues/24399) - drivers: sam0\_rtc\_timer: DT\_INST changes have broken this driver
- [GitHub #24390](https://github.com/zephyrproject-rtos/zephyr/issues/24390) - nsim\_sem\_normal target is broken
- [GitHub #24382](https://github.com/zephyrproject-rtos/zephyr/issues/24382) - disco\_l475\_iot1 not working with samples/net/wifi
- [GitHub #24376](https://github.com/zephyrproject-rtos/zephyr/issues/24376) - SPI (test) is not working for LPCXpresso54114
- [GitHub #24373](https://github.com/zephyrproject-rtos/zephyr/issues/24373) - NULL-pointer dereferencing in GATT when master connection fails
- [GitHub #24369](https://github.com/zephyrproject-rtos/zephyr/issues/24369) - tests/drivers/counter/counter\_basic\_api failure on nRF51-DK
- [GitHub #24366](https://github.com/zephyrproject-rtos/zephyr/issues/24366) - syscall for socketpair(2)
- [GitHub #24363](https://github.com/zephyrproject-rtos/zephyr/issues/24363) - nsim\_hs\_smp target doesn’t work at all
- [GitHub #24359](https://github.com/zephyrproject-rtos/zephyr/issues/24359) - k\_heap / sys\_heap needs overview documentation
- [GitHub #24357](https://github.com/zephyrproject-rtos/zephyr/issues/24357) - NVS sample on STM32F4 fails even if the dts definition is correct
- [GitHub #24356](https://github.com/zephyrproject-rtos/zephyr/issues/24356) - MCUboot (and other users of DT\_FLASH\_DEV\_NAME) broken with current zephyr master
- [GitHub #24355](https://github.com/zephyrproject-rtos/zephyr/issues/24355) - tests/drivers/uart/uart\_basic\_api configure and config\_get fail because not implemented
- [GitHub #24353](https://github.com/zephyrproject-rtos/zephyr/issues/24353) - minnowboard hangs during boot of samples/hello\_world
- [GitHub #24347](https://github.com/zephyrproject-rtos/zephyr/issues/24347) - Application Cortex M Systick driver broken by merge of #24012
- [GitHub #24340](https://github.com/zephyrproject-rtos/zephyr/issues/24340) - #24308 Broke python3 interpreter selection
- [GitHub #24339](https://github.com/zephyrproject-rtos/zephyr/issues/24339) - arm\_gic\_irq\_set\_priority - temporary variable overflow
- [GitHub #24325](https://github.com/zephyrproject-rtos/zephyr/issues/24325) - broken link in MinnowBoard documentation
- [GitHub #24324](https://github.com/zephyrproject-rtos/zephyr/issues/24324) - ST Nucleo F767ZI Ethernet Auto Negotiation problem
- [GitHub #24322](https://github.com/zephyrproject-rtos/zephyr/issues/24322) - IRQ\_CONNECT and IRQ\_DIRECT\_CONNECT throw compile error with CONFIG\_CPLUSPLUS
- [GitHub #24311](https://github.com/zephyrproject-rtos/zephyr/issues/24311) - LPN not receiving any message from Friend node after LPN device reset
- [GitHub #24306](https://github.com/zephyrproject-rtos/zephyr/issues/24306) - How to set up native posix board to allow connections to the Internet?
- [GitHub #24304](https://github.com/zephyrproject-rtos/zephyr/issues/24304) - Application crash #nrf52840 #ble
- [GitHub #24299](https://github.com/zephyrproject-rtos/zephyr/issues/24299) - tests/subsys/storage/flash\_map failed on frdm\_k64f board.
- [GitHub #24294](https://github.com/zephyrproject-rtos/zephyr/issues/24294) - Problem using TMP116 sensor with platformio
- [GitHub #24291](https://github.com/zephyrproject-rtos/zephyr/issues/24291) - The button interrupt enters the spurious handler
- [GitHub #24283](https://github.com/zephyrproject-rtos/zephyr/issues/24283) - os: Illegal use of the EPSR-disco\_l475\_iot1
- [GitHub #24282](https://github.com/zephyrproject-rtos/zephyr/issues/24282) - echo\_client sample return: Cannot connect to TCP remote (IPv6): 110
- [GitHub #24278](https://github.com/zephyrproject-rtos/zephyr/issues/24278) - Function of “ull\_conn\_done” in “ull\_conn.c”
- [GitHub #24277](https://github.com/zephyrproject-rtos/zephyr/issues/24277) - tests/kernel/workq/critical times out on ARC
- [GitHub #24276](https://github.com/zephyrproject-rtos/zephyr/issues/24276) - tests/kernel/context hangs on ARC in test\_kernel\_cpu\_idle
- [GitHub #24275](https://github.com/zephyrproject-rtos/zephyr/issues/24275) - tests/kernel/mem\_protect/syscalls fails on ARC in test\_syscall\_torture
- [GitHub #24252](https://github.com/zephyrproject-rtos/zephyr/issues/24252) - Python detection macro in cmake fails to detect highest installed version
- [GitHub #24243](https://github.com/zephyrproject-rtos/zephyr/issues/24243) - MCUBoot not working on disco\_l475\_iot1
- [GitHub #24241](https://github.com/zephyrproject-rtos/zephyr/issues/24241) - Build error when using MCHP ACPI HAL macros
- [GitHub #24237](https://github.com/zephyrproject-rtos/zephyr/issues/24237) - Fail to pass samples/subsys/nvs
- [GitHub #24227](https://github.com/zephyrproject-rtos/zephyr/issues/24227) - build hello\_world sample failed for ESP32 board.
- [GitHub #24226](https://github.com/zephyrproject-rtos/zephyr/issues/24226) - [master]Bluetooth: samples/bluetooth/central\_hr can’t connect with samples/bluetooth/peripheral\_hr
- [GitHub #24216](https://github.com/zephyrproject-rtos/zephyr/issues/24216) - Shell: Allow selecting command without subcommands
- [GitHub #24215](https://github.com/zephyrproject-rtos/zephyr/issues/24215) - Couldn’t flash image into up\_squared using misc.py script.
- [GitHub #24212](https://github.com/zephyrproject-rtos/zephyr/issues/24212) - lib: updatehub: Improve memory footprint
- [GitHub #24207](https://github.com/zephyrproject-rtos/zephyr/issues/24207) - tests/subsys/fs/fcb fails on nRF52840-DK
- [GitHub #24197](https://github.com/zephyrproject-rtos/zephyr/issues/24197) - Reduce snprintf and snprintk footprint
- [GitHub #24195](https://github.com/zephyrproject-rtos/zephyr/issues/24195) - question regarding c++
- [GitHub #24194](https://github.com/zephyrproject-rtos/zephyr/issues/24194) - Bluetooth: Mesh: Unknown message received by the node
- [GitHub #24193](https://github.com/zephyrproject-rtos/zephyr/issues/24193) - Issue with launching examples on custom board (after succesfull build)
- [GitHub #24187](https://github.com/zephyrproject-rtos/zephyr/issues/24187) - Remove the BLE Legacy Controller from the tree
- [GitHub #24183](https://github.com/zephyrproject-rtos/zephyr/issues/24183) - [v2.2] Bluetooth: controller: split: Regression slave latency during connection update
- [GitHub #24181](https://github.com/zephyrproject-rtos/zephyr/issues/24181) - Snprintk used at many place while dummy build if CONFIG\_PRINTK is undef
- [GitHub #24180](https://github.com/zephyrproject-rtos/zephyr/issues/24180) - Parameter deprecation causes scanner malfunction on big-endian systems
- [GitHub #24178](https://github.com/zephyrproject-rtos/zephyr/issues/24178) - CI: extra\_args from sanitycheck `*.yaml` do not propagate to cmake
- [GitHub #24176](https://github.com/zephyrproject-rtos/zephyr/issues/24176) - Where can I read PDR (packet delivery ratio)? Or number of TX/ACK packets?
- [GitHub #24162](https://github.com/zephyrproject-rtos/zephyr/issues/24162) - eSPI KConfig overrides espi\_config API channel selection in eSPI driver
- [GitHub #24158](https://github.com/zephyrproject-rtos/zephyr/issues/24158) - gap in support for deprecated Nordic board names
- [GitHub #24156](https://github.com/zephyrproject-rtos/zephyr/issues/24156) - MQTT Websocket transport interprets all received data as MQTT messages
- [GitHub #24145](https://github.com/zephyrproject-rtos/zephyr/issues/24145) - File system shell example mount littleFS issue on nrf52840\_pca10056
- [GitHub #24144](https://github.com/zephyrproject-rtos/zephyr/issues/24144) - deadlock potential in nrf\_qspi\_nor
- [GitHub #24136](https://github.com/zephyrproject-rtos/zephyr/issues/24136) - tests/benchmarks/latency\_measure failed on mec15xxevb\_assy6853 board.
- [GitHub #24122](https://github.com/zephyrproject-rtos/zephyr/issues/24122) - [nrf\_qspi\_nor] LittleFS file system fails to mount if LFS rcache buffer is not word aligned
- [GitHub #24108](https://github.com/zephyrproject-rtos/zephyr/issues/24108) - https GET request is failed for big file download.
- [GitHub #24104](https://github.com/zephyrproject-rtos/zephyr/issues/24104) - west sign usage help is missing key information
- [GitHub #24103](https://github.com/zephyrproject-rtos/zephyr/issues/24103) - USB Serial Number reverses bytes in hw identifier
- [GitHub #24101](https://github.com/zephyrproject-rtos/zephyr/issues/24101) - Bluetooth: Mesh: Transport Segment send failed lead to seg\_tx un-free
- [GitHub #24098](https://github.com/zephyrproject-rtos/zephyr/issues/24098) - drivers: flash: flash\_stm32: usage fault
- [GitHub #24089](https://github.com/zephyrproject-rtos/zephyr/issues/24089) - Zephyr/Openthread/MBEDTLS heap size/usage
- [GitHub #24086](https://github.com/zephyrproject-rtos/zephyr/issues/24086) - Bluetooth: SMP: Existing bond deleted on pairing failure
- [GitHub #24081](https://github.com/zephyrproject-rtos/zephyr/issues/24081) - le\_adv\_ext\_report is not generating an HCI event
- [GitHub #24072](https://github.com/zephyrproject-rtos/zephyr/issues/24072) - tests/kernel/timer/timer\_api failed on nucleo\_stm32l152re board
- [GitHub #24068](https://github.com/zephyrproject-rtos/zephyr/issues/24068) - UART driver for sifive does not compile when configuring PORT\_1
- [GitHub #24067](https://github.com/zephyrproject-rtos/zephyr/issues/24067) - cross-platform inconsistency in I2C bus speeds
- [GitHub #24055](https://github.com/zephyrproject-rtos/zephyr/issues/24055) - Add support for openocd on stm32g0 and stm32g4 targets
- [GitHub #24041](https://github.com/zephyrproject-rtos/zephyr/issues/24041) - [Coverity CID :209368] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24040](https://github.com/zephyrproject-rtos/zephyr/issues/24040) - [Coverity CID :209369] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24039](https://github.com/zephyrproject-rtos/zephyr/issues/24039) - [Coverity CID :209370] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24038](https://github.com/zephyrproject-rtos/zephyr/issues/24038) - [Coverity CID :209371] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24037](https://github.com/zephyrproject-rtos/zephyr/issues/24037) - [Coverity CID :209372] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24036](https://github.com/zephyrproject-rtos/zephyr/issues/24036) - [Coverity CID :209373] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24035](https://github.com/zephyrproject-rtos/zephyr/issues/24035) - [Coverity CID :209374] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24034](https://github.com/zephyrproject-rtos/zephyr/issues/24034) - [Coverity CID :209375] Side effect in assertion in tests/kernel/interrupt/src/prevent\_irq.c
- [GitHub #24033](https://github.com/zephyrproject-rtos/zephyr/issues/24033) - [Coverity CID :209376] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24032](https://github.com/zephyrproject-rtos/zephyr/issues/24032) - [Coverity CID :209377] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24031](https://github.com/zephyrproject-rtos/zephyr/issues/24031) - [Coverity CID :209378] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24027](https://github.com/zephyrproject-rtos/zephyr/issues/24027) - [Coverity CID :209382] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24026](https://github.com/zephyrproject-rtos/zephyr/issues/24026) - [Coverity CID :209383] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #24016](https://github.com/zephyrproject-rtos/zephyr/issues/24016) - Fully support DTS on nrf entropy driver
- [GitHub #24014](https://github.com/zephyrproject-rtos/zephyr/issues/24014) - Bluetooth: Mesh: Friend node not cache for lpn which receiveing unknown app\_idx
- [GitHub #24009](https://github.com/zephyrproject-rtos/zephyr/issues/24009) - Bluetooth: Mesh: Friend node not cache ALL\_Node Address or different app\_idx
- [GitHub #24008](https://github.com/zephyrproject-rtos/zephyr/issues/24008) - Build failure on intel\_s1000\_crb board.
- [GitHub #24003](https://github.com/zephyrproject-rtos/zephyr/issues/24003) - Couldn’t generated code coverage report using sanitycheck
- [GitHub #24001](https://github.com/zephyrproject-rtos/zephyr/issues/24001) - tests/kernel/timer/timer\_api failed on reel\_board and mec15xxevb\_assy6853.
- [GitHub #23998](https://github.com/zephyrproject-rtos/zephyr/issues/23998) - Infinite Reboot loop in Constructor C++
- [GitHub #23997](https://github.com/zephyrproject-rtos/zephyr/issues/23997) - flash sector erase fails on stm32l475
- [GitHub #23989](https://github.com/zephyrproject-rtos/zephyr/issues/23989) - Switching among different PHY Modes
- [GitHub #23986](https://github.com/zephyrproject-rtos/zephyr/issues/23986) - Possible use of uninitialized variable in subsys/net/ip/utils.c
- [GitHub #23980](https://github.com/zephyrproject-rtos/zephyr/issues/23980) - Nordic USB driver: last fragment sometimes dropped for OUT control endpoint
- [GitHub #23961](https://github.com/zephyrproject-rtos/zephyr/issues/23961) - CCC does not get cleared when CONFIG\_BT\_KEYS\_OVERWRITE\_OLDEST is enabled
- [GitHub #23953](https://github.com/zephyrproject-rtos/zephyr/issues/23953) - Question: How is pdata.tsize initialized in zephyr/subsys/usb/usb\_transfer.c?
- [GitHub #23947](https://github.com/zephyrproject-rtos/zephyr/issues/23947) - soc: arm: atmel: sam4e: Enable FPU
- [GitHub #23946](https://github.com/zephyrproject-rtos/zephyr/issues/23946) - ARM soft FP ABI support is broken
- [GitHub #23945](https://github.com/zephyrproject-rtos/zephyr/issues/23945) - west flash don’t flash right signed file when system build both hex and bin files
- [GitHub #23930](https://github.com/zephyrproject-rtos/zephyr/issues/23930) - Question: Cortex-M7 revision r0p1 errata
- [GitHub #23928](https://github.com/zephyrproject-rtos/zephyr/issues/23928) - Flash device FLASH\_CTRL not found
- [GitHub #23922](https://github.com/zephyrproject-rtos/zephyr/issues/23922) - cmake 3.17 dev warning from FindPythonInterp.cmake
- [GitHub #23919](https://github.com/zephyrproject-rtos/zephyr/issues/23919) - sanitycheck samples/drivers/entropy/sample.drivers.entropy fails
- [GitHub #23907](https://github.com/zephyrproject-rtos/zephyr/issues/23907) - Shell overdo argument parsing in some cases
- [GitHub #23897](https://github.com/zephyrproject-rtos/zephyr/issues/23897) - Typo in linker.ld for NXP i.MX RT
- [GitHub #23893](https://github.com/zephyrproject-rtos/zephyr/issues/23893) - server to client ble coms: two characteristics with notifications failing to notify the right characteristics at the client
- [GitHub #23877](https://github.com/zephyrproject-rtos/zephyr/issues/23877) - syscall use of output buffers may be unsafe in some situations
- [GitHub #23872](https://github.com/zephyrproject-rtos/zephyr/issues/23872) - cmake find\_package(ZephyrUnittest…) doesn’t work
- [GitHub #23866](https://github.com/zephyrproject-rtos/zephyr/issues/23866) - sample hci\_usb fails with zephyr 2.2.0 (worked with zephyr 2.1.0)
- [GitHub #23865](https://github.com/zephyrproject-rtos/zephyr/issues/23865) - nrf52840 and pyocd cannot program at addresses above 512k
- [GitHub #23853](https://github.com/zephyrproject-rtos/zephyr/issues/23853) - samples/boards/nrf/battery does not build
- [GitHub #23850](https://github.com/zephyrproject-rtos/zephyr/issues/23850) - Template with C linkage in util.h:52
- [GitHub #23824](https://github.com/zephyrproject-rtos/zephyr/issues/23824) - ARM Cortex-M7 MPU setting
- [GitHub #23805](https://github.com/zephyrproject-rtos/zephyr/issues/23805) - Bluetooth: controller: Switching to non conn adv fails for Mesh LPN
- [GitHub #23803](https://github.com/zephyrproject-rtos/zephyr/issues/23803) - nrf52840 ble error
- [GitHub #23800](https://github.com/zephyrproject-rtos/zephyr/issues/23800) - tests/drivers/counter/counter\_cmos failed on up\_squared platform
- [GitHub #23799](https://github.com/zephyrproject-rtos/zephyr/issues/23799) - tests/subsys/logging/log\_immediate failed on reel\_board
- [GitHub #23777](https://github.com/zephyrproject-rtos/zephyr/issues/23777) - Problem with applying overlay for custom board in blinky example
- [GitHub #23763](https://github.com/zephyrproject-rtos/zephyr/issues/23763) - net: sockets: Wrong binding when connecting to ll address
- [GitHub #23762](https://github.com/zephyrproject-rtos/zephyr/issues/23762) - stm32: Revert nucleo\_l152re to work at full speed
- [GitHub #23750](https://github.com/zephyrproject-rtos/zephyr/issues/23750) - eSPI API needs to be updated since it’s passing parameters by value
- [GitHub #23718](https://github.com/zephyrproject-rtos/zephyr/issues/23718) - Getting started with zephyr OS
- [GitHub #23712](https://github.com/zephyrproject-rtos/zephyr/issues/23712) - Error in mounting the SD card
- [GitHub #23703](https://github.com/zephyrproject-rtos/zephyr/issues/23703) - Openthread on Zephyr cannot get On-Mesh Prefix address
- [GitHub #23694](https://github.com/zephyrproject-rtos/zephyr/issues/23694) - TEMP\_KINETIS is forced enabled on frdm\_k64f if SENSORS is enabled. But ADC is missing
- [GitHub #23692](https://github.com/zephyrproject-rtos/zephyr/issues/23692) - drivers: ublox-sara-r4: Add support for pin polarity
- [GitHub #23678](https://github.com/zephyrproject-rtos/zephyr/issues/23678) - drivers/flash: stm32: Error in device name
- [GitHub #23677](https://github.com/zephyrproject-rtos/zephyr/issues/23677) - SPI slave driver doesn’t work correctly on STM32F746ZG; needs spi-fifo to be enabled in DT
- [GitHub #23674](https://github.com/zephyrproject-rtos/zephyr/issues/23674) - Openthread stop working after “Update OpenThread revision #23632”
- [GitHub #23673](https://github.com/zephyrproject-rtos/zephyr/issues/23673) - spi-nor driver fails to check for support of 32 KiBy block erase
- [GitHub #23669](https://github.com/zephyrproject-rtos/zephyr/issues/23669) - ipv4 rx fragments: is zephyr support?
- [GitHub #23662](https://github.com/zephyrproject-rtos/zephyr/issues/23662) - Building blinky sample program goes wrong
- [GitHub #23637](https://github.com/zephyrproject-rtos/zephyr/issues/23637) - Wrong channel computation in stm32 pwm driver
- [GitHub #23624](https://github.com/zephyrproject-rtos/zephyr/issues/23624) - posix: clock: clock\_gettime fault on userspace with CLOCK\_REALTIME
- [GitHub #23623](https://github.com/zephyrproject-rtos/zephyr/issues/23623) - stm32 can2 not work properly
- [GitHub #23622](https://github.com/zephyrproject-rtos/zephyr/issues/23622) - litex\_vexriscv: k\_busy\_wait() never returns if called with interrupts locked
- [GitHub #23618](https://github.com/zephyrproject-rtos/zephyr/issues/23618) - cmake: Export compile\_commands.json for all generated code
- [GitHub #23617](https://github.com/zephyrproject-rtos/zephyr/issues/23617) - kernel: k\_cpu\_idle/atomic\_idle() not tested for tick-less kernel
- [GitHub #23611](https://github.com/zephyrproject-rtos/zephyr/issues/23611) - Add QuickLogic EOS S3 HAL west module
- [GitHub #23600](https://github.com/zephyrproject-rtos/zephyr/issues/23600) - Differences in cycles between k\_busy\_wait and k\_sleep
- [GitHub #23595](https://github.com/zephyrproject-rtos/zephyr/issues/23595) - RF2XX driver Openthread ACK handling
- [GitHub #23593](https://github.com/zephyrproject-rtos/zephyr/issues/23593) - Nested interrupt test is broken for RISC-V
- [GitHub #23588](https://github.com/zephyrproject-rtos/zephyr/issues/23588) - [Coverity CID :208912] Dereference after null check in tests/net/icmpv4/src/main.c
- [GitHub #23587](https://github.com/zephyrproject-rtos/zephyr/issues/23587) - [Coverity CID :208913] Resource leak in tests/net/socket/af\_packet/src/main.c
- [GitHub #23586](https://github.com/zephyrproject-rtos/zephyr/issues/23586) - [Coverity CID :208914] Self assignment in drivers/peci/peci\_mchp\_xec.c
- [GitHub #23585](https://github.com/zephyrproject-rtos/zephyr/issues/23585) - [Coverity CID :208915] Out-of-bounds access in tests/net/icmpv4/src/main.c
- [GitHub #23584](https://github.com/zephyrproject-rtos/zephyr/issues/23584) - [Coverity CID :208916] Out-of-bounds read in drivers/sensor/adxl345/adxl345.c
- [GitHub #23583](https://github.com/zephyrproject-rtos/zephyr/issues/23583) - [Coverity CID :208917] Dereference after null check in tests/net/icmpv4/src/main.c
- [GitHub #23582](https://github.com/zephyrproject-rtos/zephyr/issues/23582) - [Coverity CID :208918] Side effect in assertion in tests/arch/arm/arm\_interrupt/src/arm\_interrupt.c
- [GitHub #23581](https://github.com/zephyrproject-rtos/zephyr/issues/23581) - [Coverity CID :208919] Out-of-bounds read in drivers/sensor/adxl345/adxl345.c
- [GitHub #23580](https://github.com/zephyrproject-rtos/zephyr/issues/23580) - [Coverity CID :208920] Resource leak in tests/net/socket/af\_packet/src/main.c
- [GitHub #23579](https://github.com/zephyrproject-rtos/zephyr/issues/23579) - [Coverity CID :208921] Improper use of negative value in tests/net/socket/af\_packet/src/main.c
- [GitHub #23577](https://github.com/zephyrproject-rtos/zephyr/issues/23577) - [Coverity CID :208923] Out-of-bounds read in drivers/sensor/adxl345/adxl345.c
- [GitHub #23576](https://github.com/zephyrproject-rtos/zephyr/issues/23576) - [Coverity CID :208924] Dereference after null check in tests/net/icmpv4/src/main.c
- [GitHub #23575](https://github.com/zephyrproject-rtos/zephyr/issues/23575) - [Coverity CID :208925] Unsigned compared against 0 in samples/drivers/espi/src/main.c
- [GitHub #23573](https://github.com/zephyrproject-rtos/zephyr/issues/23573) - [Coverity CID :208927] Dereference after null check in tests/net/icmpv4/src/main.c
- [GitHub #23571](https://github.com/zephyrproject-rtos/zephyr/issues/23571) - drivers: timer: nrf52: Question: Does nRF52840 errata 179 affect nrf\_rtc\_timer driver?
- [GitHub #23562](https://github.com/zephyrproject-rtos/zephyr/issues/23562) - build warnings when updating to master from 2.2.0
- [GitHub #23555](https://github.com/zephyrproject-rtos/zephyr/issues/23555) - STM32 SDMMC disk access driver (based on stm32 cube HAL)
- [GitHub #23544](https://github.com/zephyrproject-rtos/zephyr/issues/23544) - tests/kernel/mem\_protect/syscalls failed on iotdk board.
- [GitHub #23541](https://github.com/zephyrproject-rtos/zephyr/issues/23541) - xilinx\_zynqmp: k\_busy\_wait() never returns if called with interrupts locked
- [GitHub #23539](https://github.com/zephyrproject-rtos/zephyr/issues/23539) - west flash –runner jlink returns KeyError: ‘jlink’
- [GitHub #23529](https://github.com/zephyrproject-rtos/zephyr/issues/23529) - Convert STM32 drivers to new DT macros
- [GitHub #23528](https://github.com/zephyrproject-rtos/zephyr/issues/23528) - k64f dts flash0/storage\_partition 8KiB -> 64KiB
- [GitHub #23507](https://github.com/zephyrproject-rtos/zephyr/issues/23507) - samples/subsys/shell/shell\_module doesn’t work on qemu\_x86\_64
- [GitHub #23504](https://github.com/zephyrproject-rtos/zephyr/issues/23504) - Build system dependency issue with syscalls
- [GitHub #23496](https://github.com/zephyrproject-rtos/zephyr/issues/23496) - Issue building & flashing a hello world project on nRF52840
- [GitHub #23494](https://github.com/zephyrproject-rtos/zephyr/issues/23494) - Bluetooth: LL/PAC/SLA/BV-01-C fails if Slave-initiated Feature Exchange is disabled
- [GitHub #23485](https://github.com/zephyrproject-rtos/zephyr/issues/23485) - BT: host: Service Change indication sent regardless of whether it is needed or not.
- [GitHub #23482](https://github.com/zephyrproject-rtos/zephyr/issues/23482) - 2M PHY + DLE and timing calculations on an encrypted link are wrong
- [GitHub #23476](https://github.com/zephyrproject-rtos/zephyr/issues/23476) - tests/kernel/interrupt failed on ARC
- [GitHub #23475](https://github.com/zephyrproject-rtos/zephyr/issues/23475) - tests/kernel/gen\_isr\_table failed on iotdk board.
- [GitHub #23473](https://github.com/zephyrproject-rtos/zephyr/issues/23473) - tests/posix/common failed on multiple ARM platforms.
- [GitHub #23468](https://github.com/zephyrproject-rtos/zephyr/issues/23468) - bluetooth: host: Runtime HCI\_LE\_Create\_Connection timeout
- [GitHub #23467](https://github.com/zephyrproject-rtos/zephyr/issues/23467) - Import from linux to zephyr?
- [GitHub #23459](https://github.com/zephyrproject-rtos/zephyr/issues/23459) - tests: drivers: uart: config api has extra dependency in test 2
- [GitHub #23444](https://github.com/zephyrproject-rtos/zephyr/issues/23444) - drivers: hwinfo: shell command “hwinfo devid” output ignores endianness
- [GitHub #23441](https://github.com/zephyrproject-rtos/zephyr/issues/23441) - RFC: API change: Add I2C bus recovery API
- [GitHub #23438](https://github.com/zephyrproject-rtos/zephyr/issues/23438) - Cannot reset Bluetooth mesh device
- [GitHub #23435](https://github.com/zephyrproject-rtos/zephyr/issues/23435) - Missing documentation for macros in util.h
- [GitHub #23432](https://github.com/zephyrproject-rtos/zephyr/issues/23432) - Add PECI subsystem user space handlers
- [GitHub #23425](https://github.com/zephyrproject-rtos/zephyr/issues/23425) - Remote opencd
- [GitHub #23420](https://github.com/zephyrproject-rtos/zephyr/issues/23420) - PPP management don’t build
- [GitHub #23418](https://github.com/zephyrproject-rtos/zephyr/issues/23418) - Building hello\_world failed
- [GitHub #23415](https://github.com/zephyrproject-rtos/zephyr/issues/23415) - gen\_defines does not resolve symbol values for devicetree.conf
- [GitHub #23414](https://github.com/zephyrproject-rtos/zephyr/issues/23414) - tests/benchmarks/timing\_info failed on mec15xxevb\_assy6853 board.
- [GitHub #23395](https://github.com/zephyrproject-rtos/zephyr/issues/23395) - UART Console input does not work on SiFive HiFive1 on echo sample app
- [GitHub #23387](https://github.com/zephyrproject-rtos/zephyr/issues/23387) - [Question] Why does not zephyr use a toolchain file with cmake as -DCMAKE\_TOOLCHAIN\_FILE=.. ?
- [GitHub #23386](https://github.com/zephyrproject-rtos/zephyr/issues/23386) - SAM GMAC should support PHY link status detection
- [GitHub #23373](https://github.com/zephyrproject-rtos/zephyr/issues/23373) - ARM: Move CMSIS out of main tree
- [GitHub #23372](https://github.com/zephyrproject-rtos/zephyr/issues/23372) - arm: aarch32: spurious IRQ handler calling z\_arm\_reserved with wrong arguments’ list
- [GitHub #23360](https://github.com/zephyrproject-rtos/zephyr/issues/23360) - Possible NULL dereference in zephyr/arch/arm/include/aarch32/cortex\_m/exc.h
- [GitHub #23353](https://github.com/zephyrproject-rtos/zephyr/issues/23353) - nrf51\_ble400.dts i2c pins inverted
- [GitHub #23346](https://github.com/zephyrproject-rtos/zephyr/issues/23346) - bl65x\_dvk boards do not reset after flashing
- [GitHub #23339](https://github.com/zephyrproject-rtos/zephyr/issues/23339) - tests/kernel/sched/schedule\_api failed on mps2\_an385 with v1.14 branch.
- [GitHub #23337](https://github.com/zephyrproject-rtos/zephyr/issues/23337) - USB DFU device + Composite Device with ACM Serial - Windows Fails
- [GitHub #23324](https://github.com/zephyrproject-rtos/zephyr/issues/23324) - TinyCBOR is not linked to application files unless CONFIG\_MCUMGR is selected
- [GitHub #23311](https://github.com/zephyrproject-rtos/zephyr/issues/23311) - Sanitycheck flash error on frdm\_k64f board.
- [GitHub #23309](https://github.com/zephyrproject-rtos/zephyr/issues/23309) - Sanitycheck generated incorrect acrn.xml on acrn platform
- [GitHub #23299](https://github.com/zephyrproject-rtos/zephyr/issues/23299) - Some bugs or dead codes cased by possible NULL pointers
- [GitHub #23295](https://github.com/zephyrproject-rtos/zephyr/issues/23295) - [Coverity CID :208676] Overlapping buffer in memory copy in subsys/usb/class/mass\_storage.c
- [GitHub #23294](https://github.com/zephyrproject-rtos/zephyr/issues/23294) - [Coverity CID :208677] Unchecked return value in drivers/sensor/lis3mdl/lis3mdl\_trigger.c
- [GitHub #23284](https://github.com/zephyrproject-rtos/zephyr/issues/23284) - driver: ethernet: Add support for a second Ethernet controller in the MCUX driver
- [GitHub #23280](https://github.com/zephyrproject-rtos/zephyr/issues/23280) - Bluetooth: hci\_usb fails to connect to two devices with slow advertising interval
- [GitHub #23278](https://github.com/zephyrproject-rtos/zephyr/issues/23278) - uart\_basic\_api test fails for SAM family devices
- [GitHub #23274](https://github.com/zephyrproject-rtos/zephyr/issues/23274) - power: subsystem: Application hangs when logging is enabled after entering deep sleep
- [GitHub #23247](https://github.com/zephyrproject-rtos/zephyr/issues/23247) - Bluetooth LE: Add feature to allow profiles to change ADV data at RPA updates
- [GitHub #23246](https://github.com/zephyrproject-rtos/zephyr/issues/23246) - net: tx\_bufs are not freed when NET\_TCP\_BACKLOG\_SIZE is too high
- [GitHub #23226](https://github.com/zephyrproject-rtos/zephyr/issues/23226) - Bluetooth: host: Peer not resolved when host resolving is used
- [GitHub #23225](https://github.com/zephyrproject-rtos/zephyr/issues/23225) - Bluetooth: Quality of service: Adaptive channel map
- [GitHub #23222](https://github.com/zephyrproject-rtos/zephyr/issues/23222) - Bluetooth: host: Unable to pair when privacy feature is disabled by application
- [GitHub #23207](https://github.com/zephyrproject-rtos/zephyr/issues/23207) - tests/kernel/mem\_pool/mem\_pool\_concept failed on mec15xxevb\_assy6853 board.
- [GitHub #23193](https://github.com/zephyrproject-rtos/zephyr/issues/23193) - Allow overriding get\_mac() function in ieee802154 drivers
- [GitHub #23187](https://github.com/zephyrproject-rtos/zephyr/issues/23187) - nrf\_rtc\_timer.c timseout setting mistake.
- [GitHub #23184](https://github.com/zephyrproject-rtos/zephyr/issues/23184) - mqtt\_connect fails with return -2
- [GitHub #23156](https://github.com/zephyrproject-rtos/zephyr/issues/23156) - App determines if Bluetooth host link request is allowed
- [GitHub #23153](https://github.com/zephyrproject-rtos/zephyr/issues/23153) - Binding AF\_PACKET socket second time will fail with multiple network interfaces
- [GitHub #23133](https://github.com/zephyrproject-rtos/zephyr/issues/23133) - boards: adafruit\_feather\_m0: don’t throw compiler warnings on using custom sercom config
- [GitHub #23117](https://github.com/zephyrproject-rtos/zephyr/issues/23117) - Unable to flash hello\_world w/XDS-110 & OpenOCD
- [GitHub #23107](https://github.com/zephyrproject-rtos/zephyr/issues/23107) - Convert SAM SoC drivers to DT\_INST
- [GitHub #23106](https://github.com/zephyrproject-rtos/zephyr/issues/23106) - timer\_api intermittent failures on Nordic nRF
- [GitHub #23070](https://github.com/zephyrproject-rtos/zephyr/issues/23070) - Bluetooth: controller: Fix ticker implementation to avoid catch up
- [GitHub #23026](https://github.com/zephyrproject-rtos/zephyr/issues/23026) - missing ISR locking in UART driver?
- [GitHub #23001](https://github.com/zephyrproject-rtos/zephyr/issues/23001) - Implement SAM E5X GMAC support
- [GitHub #22997](https://github.com/zephyrproject-rtos/zephyr/issues/22997) - Add GMAC device tree definition
- [GitHub #22964](https://github.com/zephyrproject-rtos/zephyr/issues/22964) - Define a consistent naming convention for device tree defines
- [GitHub #22948](https://github.com/zephyrproject-rtos/zephyr/issues/22948) - sanitycheck –build-only followed by –test-only fails
- [GitHub #22911](https://github.com/zephyrproject-rtos/zephyr/issues/22911) - [Coverity CID :208407] Unsigned compared against 0 in drivers/modem/modem\_pin.c
- [GitHub #22910](https://github.com/zephyrproject-rtos/zephyr/issues/22910) - [Coverity CID :208408] Unsigned compared against 0 in drivers/modem/modem\_pin.c
- [GitHub #22909](https://github.com/zephyrproject-rtos/zephyr/issues/22909) - [Coverity CID :208409] Unchecked return value in tests/drivers/gpio/gpio\_basic\_api/src/test\_deprecated.c
- [GitHub #22908](https://github.com/zephyrproject-rtos/zephyr/issues/22908) - [Coverity CID :208410] Unsigned compared against 0 in drivers/modem/modem\_pin.c
- [GitHub #22907](https://github.com/zephyrproject-rtos/zephyr/issues/22907) - si7006 temperature conversion offset missing
- [GitHub #22903](https://github.com/zephyrproject-rtos/zephyr/issues/22903) - mcuboot/samples/zephyr (make test-good-rsa) doesn’t work
- [GitHub #22887](https://github.com/zephyrproject-rtos/zephyr/issues/22887) - Atomic operations on pointers
- [GitHub #22860](https://github.com/zephyrproject-rtos/zephyr/issues/22860) - Highly accurate synchronized clock distribution for BLE mesh network
- [GitHub #22780](https://github.com/zephyrproject-rtos/zephyr/issues/22780) - Sanitycheck hardware map integration caused some tests failure.
- [GitHub #22777](https://github.com/zephyrproject-rtos/zephyr/issues/22777) - Sanitycheck hardware map integration failed with some tests timeout.
- [GitHub #22745](https://github.com/zephyrproject-rtos/zephyr/issues/22745) - schedule\_api fails with slice testing on frdmkw41z board on v2.2.0\_rc1
- [GitHub #22738](https://github.com/zephyrproject-rtos/zephyr/issues/22738) - crashes in tests/kernel/mem\_protect/userspace case pass\_noperms\_object on x86\_64
- [GitHub #22732](https://github.com/zephyrproject-rtos/zephyr/issues/22732) - IPv6 address and prefix timeout failures
- [GitHub #22701](https://github.com/zephyrproject-rtos/zephyr/issues/22701) - Implement I2C driver for lpcxpresso55s69
- [GitHub #22679](https://github.com/zephyrproject-rtos/zephyr/issues/22679) - MQTT publish causes unnecessary TCP segmentation
- [GitHub #22670](https://github.com/zephyrproject-rtos/zephyr/issues/22670) - Implement GIC-based ARM interrupt tests
- [GitHub #22643](https://github.com/zephyrproject-rtos/zephyr/issues/22643) - [Coverity CID :208206] Unsigned compared against 0 in samples/sensor/fxos8700-hid/src/main.c
- [GitHub #22625](https://github.com/zephyrproject-rtos/zephyr/issues/22625) - tests/subsys/canbus/isotp/conformance fails on frdm\_k64f and twr\_ke18f boards
- [GitHub #22622](https://github.com/zephyrproject-rtos/zephyr/issues/22622) - tests/drivers/gpio/gpio\_basic\_api failed on multiple ARM platforms
- [GitHub #22561](https://github.com/zephyrproject-rtos/zephyr/issues/22561) - tests/kernel/mem\_protect/syscalls fails test\_string\_nlen on nsim\_sem
- [GitHub #22555](https://github.com/zephyrproject-rtos/zephyr/issues/22555) - Add support to device tree generation support for DT\_NODELABEL\_<node-label>\_<FOO> generation
- [GitHub #22554](https://github.com/zephyrproject-rtos/zephyr/issues/22554) - Add support to device tree generation support for DT\_PATH\_<path>\_<FOO> generation
- [GitHub #22541](https://github.com/zephyrproject-rtos/zephyr/issues/22541) - hal\_nordic: nrf\_glue.h change mapped assert function
- [GitHub #22521](https://github.com/zephyrproject-rtos/zephyr/issues/22521) - intermittent crash in tests/portability/cmsis\_rtos\_v2 on qemu\_x86
- [GitHub #22502](https://github.com/zephyrproject-rtos/zephyr/issues/22502) - USB transfer warnings
- [GitHub #22452](https://github.com/zephyrproject-rtos/zephyr/issues/22452) - not driver found in can bus samples for olimexino\_stm32
- [GitHub #22441](https://github.com/zephyrproject-rtos/zephyr/issues/22441) - [Coverity CID :207967] Invalid type in argument to printf format specifier in samples/drivers/spi\_flash/src/main.c
- [GitHub #22431](https://github.com/zephyrproject-rtos/zephyr/issues/22431) - [Coverity CID :207984] Sizeof not portable in drivers/counter/counter\_handlers.c
- [GitHub #22429](https://github.com/zephyrproject-rtos/zephyr/issues/22429) - [Coverity CID :207989] Dereference after null check in drivers/sensor/sensor\_shell.c
- [GitHub #22421](https://github.com/zephyrproject-rtos/zephyr/issues/22421) - mbed TLS: Inconsistent Kconfig option names
- [GitHub #22356](https://github.com/zephyrproject-rtos/zephyr/issues/22356) - An application hook for early init
- [GitHub #22348](https://github.com/zephyrproject-rtos/zephyr/issues/22348) - LIS2DH SPI Support
- [GitHub #22270](https://github.com/zephyrproject-rtos/zephyr/issues/22270) - wrong total of testcases when sanitycheck is run with a single test
- [GitHub #22264](https://github.com/zephyrproject-rtos/zephyr/issues/22264) - drivers: serial: nrf\_uart & nrf\_uarte infinite hang
- [GitHub #22222](https://github.com/zephyrproject-rtos/zephyr/issues/22222) - Enabling OpenThread SLAAC
- [GitHub #22158](https://github.com/zephyrproject-rtos/zephyr/issues/22158) - flash\_img: support arbitrary flash devices
- [GitHub #22083](https://github.com/zephyrproject-rtos/zephyr/issues/22083) - stm32: spi: Infinite loop of RXNE bit check
- [GitHub #22078](https://github.com/zephyrproject-rtos/zephyr/issues/22078) - stm32: Shell module sample doesn’t work on nucleo\_l152re
- [GitHub #22034](https://github.com/zephyrproject-rtos/zephyr/issues/22034) - Add support for USB device on STM32L1 series
- [GitHub #21984](https://github.com/zephyrproject-rtos/zephyr/issues/21984) - i2c\_4 not working on stm32f746g\_disco
- [GitHub #21955](https://github.com/zephyrproject-rtos/zephyr/issues/21955) - usb: tests/subsys/usb/device fails on all NXP RT boards
- [GitHub #21932](https://github.com/zephyrproject-rtos/zephyr/issues/21932) - Current consumption on nrf52\_pca10040, power\_mgr sample
- [GitHub #21917](https://github.com/zephyrproject-rtos/zephyr/issues/21917) - cmake error with CONFIG\_COUNTER and CONFIG\_BT both enabled (nrf52 board)
- [GitHub #21899](https://github.com/zephyrproject-rtos/zephyr/issues/21899) - STM32F769I-DISCO > microSD + FatFS > failed in “samples/subsys/fs/fat\_fs” > CMD0 and 0x01
- [GitHub #21877](https://github.com/zephyrproject-rtos/zephyr/issues/21877) - tests/drivers/uart/uart\_async\_api fails on qemu\_cortex\_m0
- [GitHub #21833](https://github.com/zephyrproject-rtos/zephyr/issues/21833) - SRAM not sufficient when building BT Mesh developer guide build on BBC Micro-bit
- [GitHub #21820](https://github.com/zephyrproject-rtos/zephyr/issues/21820) - docs: “Crypto Cipher” API isn’t available in the docs
- [GitHub #21755](https://github.com/zephyrproject-rtos/zephyr/issues/21755) - tests/drivers/adc/adc\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #21706](https://github.com/zephyrproject-rtos/zephyr/issues/21706) - Link to releases in README.rst give a 404 error
- [GitHub #21701](https://github.com/zephyrproject-rtos/zephyr/issues/21701) - [Coverity CID :206600] Logically dead code in drivers/crypto/crypto\_mtls\_shim.c
- [GitHub #21677](https://github.com/zephyrproject-rtos/zephyr/issues/21677) - [Coverity CID :206388] Unrecoverable parse warning in subsys/cpp/cpp\_new.cpp
- [GitHub #21675](https://github.com/zephyrproject-rtos/zephyr/issues/21675) - [Coverity CID :206390] Unrecoverable parse warning in subsys/cpp/cpp\_new.cpp
- [GitHub #21514](https://github.com/zephyrproject-rtos/zephyr/issues/21514) - Logging - strange behaviour with RTT on nRF53
- [GitHub #21513](https://github.com/zephyrproject-rtos/zephyr/issues/21513) - NULL parameter checks in Zephyr APIs
- [GitHub #21500](https://github.com/zephyrproject-rtos/zephyr/issues/21500) - RFC: k\_thread\_join()
- [GitHub #21469](https://github.com/zephyrproject-rtos/zephyr/issues/21469) - ARC SMP is mostly untested in sanitycheck
- [GitHub #21455](https://github.com/zephyrproject-rtos/zephyr/issues/21455) - driver: subsys: sdhc: USAGE FAULT trace and no cs control
- [GitHub #21441](https://github.com/zephyrproject-rtos/zephyr/issues/21441) - Add UART5 on B-port to H7 pinmux
- [GitHub #21426](https://github.com/zephyrproject-rtos/zephyr/issues/21426) - civetweb triggers an error on Windows with Git 2.24
- [GitHub #21390](https://github.com/zephyrproject-rtos/zephyr/issues/21390) - BLE Incomplete Connect results in subsquent encryption failures
- [GitHub #21372](https://github.com/zephyrproject-rtos/zephyr/issues/21372) - cc26x2r1\_launchxl build passed, but can’t flash
- [GitHub #21369](https://github.com/zephyrproject-rtos/zephyr/issues/21369) - devicetree: clearly define constraints on identifier/property name conflicts
- [GitHub #21321](https://github.com/zephyrproject-rtos/zephyr/issues/21321) - error update for project civetweb
- [GitHub #21305](https://github.com/zephyrproject-rtos/zephyr/issues/21305) - New Kernel Timeout API
- [GitHub #21253](https://github.com/zephyrproject-rtos/zephyr/issues/21253) - 2.2 Release Checklist
- [GitHub #21201](https://github.com/zephyrproject-rtos/zephyr/issues/21201) - ARM: Core Stack Improvements/Bug fixes for 2.2 release
- [GitHub #21200](https://github.com/zephyrproject-rtos/zephyr/issues/21200) - Replace IWDG\_STM32\_START\_AT\_BOOT by WDT\_DISABLE\_AT\_BOOT
- [GitHub #21158](https://github.com/zephyrproject-rtos/zephyr/issues/21158) - Giving Semaphore Limit+1 can cause limit+1 takes
- [GitHub #21156](https://github.com/zephyrproject-rtos/zephyr/issues/21156) - Interrupts do not work on UP Squared board
- [GitHub #21107](https://github.com/zephyrproject-rtos/zephyr/issues/21107) - LL\_ASSERT and ‘Imprecise data bus error’ in LL Controller
- [GitHub #21093](https://github.com/zephyrproject-rtos/zephyr/issues/21093) - put sys\_trace\_isr\_enter/sys\_trace\_isr\_exit to user care about ISR instead of every ISR
- [GitHub #21088](https://github.com/zephyrproject-rtos/zephyr/issues/21088) - Bluetooth: Mesh: Send Model Message shouldn’t require explicit NetKey Index
- [GitHub #21068](https://github.com/zephyrproject-rtos/zephyr/issues/21068) - Conflicting documentation for device initialization
- [GitHub #20993](https://github.com/zephyrproject-rtos/zephyr/issues/20993) - spinlock APIs need documentation
- [GitHub #20991](https://github.com/zephyrproject-rtos/zephyr/issues/20991) - test\_timer\_duration\_period fails with stm32 lptimer
- [GitHub #20945](https://github.com/zephyrproject-rtos/zephyr/issues/20945) - samples/synchronization fails on nsim\_hs\_smp and nsim\_sem\_normal
- [GitHub #20876](https://github.com/zephyrproject-rtos/zephyr/issues/20876) - [Coverity CID :205820] Memory - corruptions in tests/crypto/tinycrypt/src/cmac\_mode.c
- [GitHub #20875](https://github.com/zephyrproject-rtos/zephyr/issues/20875) - [Coverity CID :205840] Memory - corruptions in tests/benchmarks/mbedtls/src/benchmark.c
- [GitHub #20874](https://github.com/zephyrproject-rtos/zephyr/issues/20874) - [Coverity CID :205805] Memory - corruptions in tests/benchmarks/mbedtls/src/benchmark.c
- [GitHub #20873](https://github.com/zephyrproject-rtos/zephyr/issues/20873) - [Coverity CID :205782] Memory - corruptions in tests/benchmarks/mbedtls/src/benchmark.c
- [GitHub #20835](https://github.com/zephyrproject-rtos/zephyr/issues/20835) - [Coverity CID :205797] Control flow issues in drivers/flash/spi\_nor.c
- [GitHub #20825](https://github.com/zephyrproject-rtos/zephyr/issues/20825) - stm32: dma: enable dma with peripheral using DMAMUX
- [GitHub #20699](https://github.com/zephyrproject-rtos/zephyr/issues/20699) - Each board should have a list of Kconfig options supported
- [GitHub #20632](https://github.com/zephyrproject-rtos/zephyr/issues/20632) - call to bt\_gatt\_hids\_init influences execution time of work queue
- [GitHub #20604](https://github.com/zephyrproject-rtos/zephyr/issues/20604) - log will be discarded before logging\_thread scheduled once
- [GitHub #20585](https://github.com/zephyrproject-rtos/zephyr/issues/20585) - z\_clock\_announce starvation with timeslicing active
- [GitHub #20492](https://github.com/zephyrproject-rtos/zephyr/issues/20492) - [Coverity CID :205653]Control flow issues in /drivers/dma/dma\_stm32\_v1.c
- [GitHub #20491](https://github.com/zephyrproject-rtos/zephyr/issues/20491) - [Coverity CID :205644]Control flow issues in /drivers/dma/dma\_stm32\_v1.c
- [GitHub #20348](https://github.com/zephyrproject-rtos/zephyr/issues/20348) - Convert remaining entropy to Devicetree
- [GitHub #20330](https://github.com/zephyrproject-rtos/zephyr/issues/20330) - devicetree Arduino bindings do not support identification of bus controllers
- [GitHub #20301](https://github.com/zephyrproject-rtos/zephyr/issues/20301) - tests/drivers/watchdog/wdt\_basic\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #20259](https://github.com/zephyrproject-rtos/zephyr/issues/20259) - Bluetooth: Mesh: Network management
- [GitHub #20137](https://github.com/zephyrproject-rtos/zephyr/issues/20137) - posix: undefined reference with –no-gc-sections
- [GitHub #20136](https://github.com/zephyrproject-rtos/zephyr/issues/20136) - kernel: undefined reference with –no-gc-sections
- [GitHub #20068](https://github.com/zephyrproject-rtos/zephyr/issues/20068) - Application doesn’t start when SHELL-UART is enabled and UART is not connected on STM32F0
- [GitHub #19869](https://github.com/zephyrproject-rtos/zephyr/issues/19869) - Implement tickless capability for xlnx\_psttc\_timer
- [GitHub #19852](https://github.com/zephyrproject-rtos/zephyr/issues/19852) - Add support for GPIO AF remap on STM32F1XX
- [GitHub #19837](https://github.com/zephyrproject-rtos/zephyr/issues/19837) - SS register is 0 when taking exceptions on qemu\_x86\_long
- [GitHub #19813](https://github.com/zephyrproject-rtos/zephyr/issues/19813) - tests/crypto/rand32 failed on sam\_e70 board on v1.14 branch.
- [GitHub #19763](https://github.com/zephyrproject-rtos/zephyr/issues/19763) - tests/subsys/usb/device/ failed on mimxrt1050\_evk board.
- [GitHub #19614](https://github.com/zephyrproject-rtos/zephyr/issues/19614) - Make zephyr\_library out of hal\_stm32 and hal\_st
- [GitHub #19550](https://github.com/zephyrproject-rtos/zephyr/issues/19550) - drivers/pcie: `pcie_get_mbar()` should return a `void *` not `u32_t`
- [GitHub #19487](https://github.com/zephyrproject-rtos/zephyr/issues/19487) - tests/kernel/fifo/fifo\_usage GPF crash on qemu\_x86\_long
- [GitHub #19456](https://github.com/zephyrproject-rtos/zephyr/issues/19456) - arch/x86: make use of z\_bss\_zero() and z\_data\_copy()
- [GitHub #19353](https://github.com/zephyrproject-rtos/zephyr/issues/19353) - arch/x86: QEMU doesn’t appear to support x2APIC
- [GitHub #19307](https://github.com/zephyrproject-rtos/zephyr/issues/19307) - \_interrupt\_stack is defined in the kernel, but declared in arch headers
- [GitHub #19285](https://github.com/zephyrproject-rtos/zephyr/issues/19285) - devicetree: fixed non-alias reference to specific nodes
- [GitHub #19235](https://github.com/zephyrproject-rtos/zephyr/issues/19235) - move drivers/timer/apic\_timer.c to devicetree
- [GitHub #19219](https://github.com/zephyrproject-rtos/zephyr/issues/19219) - drivers/i2c/i2c\_dw.c is not 64-bit clean
- [GitHub #19144](https://github.com/zephyrproject-rtos/zephyr/issues/19144) - arch/x86: CONFIG\_BOOT\_TIME\_MEASUREMENT broken
- [GitHub #19075](https://github.com/zephyrproject-rtos/zephyr/issues/19075) - k\_delayed\_work\_submit() does not handle long delays correctly
- [GitHub #19067](https://github.com/zephyrproject-rtos/zephyr/issues/19067) - non-overlapping MPU gap-filling needs to be optional
- [GitHub #19038](https://github.com/zephyrproject-rtos/zephyr/issues/19038) - [zephyr branch 1.14 and master -stm32-netusb]:errors when i view RNDIS Device‘s properties on Windows 10
- [GitHub #18956](https://github.com/zephyrproject-rtos/zephyr/issues/18956) - memory protection for x86 dependent on XIP
- [GitHub #18940](https://github.com/zephyrproject-rtos/zephyr/issues/18940) - Counter External Trigger
- [GitHub #18808](https://github.com/zephyrproject-rtos/zephyr/issues/18808) - Docs for gpmrb board incorrectly refer to up\_squared board
- [GitHub #18787](https://github.com/zephyrproject-rtos/zephyr/issues/18787) - arch/x86: retire loapic\_timer.c driver in favor of new apic\_timer.c
- [GitHub #18657](https://github.com/zephyrproject-rtos/zephyr/issues/18657) - drivers/timer/hpet.c should use devicetree, not CONFIG\_\* for MMIO/IRQ data
- [GitHub #18614](https://github.com/zephyrproject-rtos/zephyr/issues/18614) - same70 hsmci interface
- [GitHub #18568](https://github.com/zephyrproject-rtos/zephyr/issues/18568) - Support for Particle Photon
- [GitHub #18435](https://github.com/zephyrproject-rtos/zephyr/issues/18435) - [Coverity CID :203481]API usage errors in /tests/crypto/tinycrypt/src/test\_ecc\_utils.c
- [GitHub #18425](https://github.com/zephyrproject-rtos/zephyr/issues/18425) - [Coverity CID :203498]Memory - corruptions in /tests/application\_development/gen\_inc\_file/src/main.c
- [GitHub #18422](https://github.com/zephyrproject-rtos/zephyr/issues/18422) - [Coverity CID :203415]Memory - illegal accesses in /subsys/shell/shell\_telnet.c
- [GitHub #18389](https://github.com/zephyrproject-rtos/zephyr/issues/18389) - [Coverity CID :203396]Null pointer dereferences in /subsys/bluetooth/mesh/access.c
- [GitHub #18386](https://github.com/zephyrproject-rtos/zephyr/issues/18386) - [Coverity CID :203443]Memory - corruptions in /subsys/bluetooth/host/rfcomm.c
- [GitHub #18263](https://github.com/zephyrproject-rtos/zephyr/issues/18263) - flash sector erase fails on stm32f412
- [GitHub #18207](https://github.com/zephyrproject-rtos/zephyr/issues/18207) - tests/bluetooth/hci\_prop\_evt fails with code coverage enabled in qemu\_x86
- [GitHub #18124](https://github.com/zephyrproject-rtos/zephyr/issues/18124) - synchronization example fails to build for SMP platforms
- [GitHub #18118](https://github.com/zephyrproject-rtos/zephyr/issues/18118) - samples/subsys/console doesn’t work with qemu\_riscv32
- [GitHub #18106](https://github.com/zephyrproject-rtos/zephyr/issues/18106) - Only 1 NET\_SOCKET\_OFFLOAD driver can be used
- [GitHub #18085](https://github.com/zephyrproject-rtos/zephyr/issues/18085) - I2C log level ignored
- [GitHub #18050](https://github.com/zephyrproject-rtos/zephyr/issues/18050) - BT Host - Advertisement extensions support
- [GitHub #18047](https://github.com/zephyrproject-rtos/zephyr/issues/18047) - BT Host: Advertising Extensions - Advertiser
- [GitHub #18046](https://github.com/zephyrproject-rtos/zephyr/issues/18046) - BT Host: Advertising Extensions - Scanner
- [GitHub #18044](https://github.com/zephyrproject-rtos/zephyr/issues/18044) - BT Host: Advertising Extensions - Periodic Advertisement Synchronisation (Rx)
- [GitHub #18042](https://github.com/zephyrproject-rtos/zephyr/issues/18042) - Only corporate members can join the slack channel
- [GitHub #17892](https://github.com/zephyrproject-rtos/zephyr/issues/17892) - arch/x86: clean up segmentation.h
- [GitHub #17888](https://github.com/zephyrproject-rtos/zephyr/issues/17888) - arch/x86: remove IAMCU ABI support
- [GitHub #17775](https://github.com/zephyrproject-rtos/zephyr/issues/17775) - Microchip XEC rtos timer should be using values coming from DTS
- [GitHub #17755](https://github.com/zephyrproject-rtos/zephyr/issues/17755) - ARC privilege mode stacks waste memory due to alignment requirements
- [GitHub #17735](https://github.com/zephyrproject-rtos/zephyr/issues/17735) - abolish Z\_OOPS() in system call handlers
- [GitHub #17543](https://github.com/zephyrproject-rtos/zephyr/issues/17543) - dtc version 1.4.5 with ubuntu 18.04 and zephyr sdk-0.10.1
- [GitHub #17508](https://github.com/zephyrproject-rtos/zephyr/issues/17508) - RFC: Change/deprecation in display API
- [GitHub #17443](https://github.com/zephyrproject-rtos/zephyr/issues/17443) - Kconfig: move arch-specific stack sizes to arch trees?
- [GitHub #17430](https://github.com/zephyrproject-rtos/zephyr/issues/17430) - arch/x86: drivers/interrupt\_controller/system\_apic.c improperly classifies IRQs
- [GitHub #17415](https://github.com/zephyrproject-rtos/zephyr/issues/17415) - Settings Module - settings\_line\_val\_read() returning -EINVAL instead of 0 for deleted setting entries
- [GitHub #17361](https://github.com/zephyrproject-rtos/zephyr/issues/17361) - \_THREAD\_QUEUED overlaps with x86 \_EXC\_ACTIVE in k\_thread.thread\_state
- [GitHub #17324](https://github.com/zephyrproject-rtos/zephyr/issues/17324) - failing bluetooth tests with code coverage enabled in qemu\_x86
- [GitHub #17323](https://github.com/zephyrproject-rtos/zephyr/issues/17323) - failing network tests with code coverage enabled in qemu\_x86
- [GitHub #17240](https://github.com/zephyrproject-rtos/zephyr/issues/17240) - add arc support in Zephyr’s openthread
- [GitHub #17234](https://github.com/zephyrproject-rtos/zephyr/issues/17234) - CONFIG\_KERNEL\_ENTRY appears to be superfluous
- [GitHub #17166](https://github.com/zephyrproject-rtos/zephyr/issues/17166) - arch/x86: eliminate support for CONFIG\_REALMODE
- [GitHub #17135](https://github.com/zephyrproject-rtos/zephyr/issues/17135) - Cannot flash LWM2M example for ESP32
- [GitHub #17133](https://github.com/zephyrproject-rtos/zephyr/issues/17133) - arch/x86: x2APIC EOI should be inline
- [GitHub #17104](https://github.com/zephyrproject-rtos/zephyr/issues/17104) - arch/x86: fix -march flag for Apollo Lake
- [GitHub #17064](https://github.com/zephyrproject-rtos/zephyr/issues/17064) - drivers/serial/uart\_ns16550: CMD\_SET\_DLF should be removed
- [GitHub #16988](https://github.com/zephyrproject-rtos/zephyr/issues/16988) - Packet isn’t received by server during stepping
- [GitHub #16902](https://github.com/zephyrproject-rtos/zephyr/issues/16902) - CMSIS v2 emulation assumes ticks == milliseconds
- [GitHub #16886](https://github.com/zephyrproject-rtos/zephyr/issues/16886) - Bluetooth Mesh: Receive segmented message multiple times
- [GitHub #16721](https://github.com/zephyrproject-rtos/zephyr/issues/16721) - PCIe build warnings from devicetree
- [GitHub #16720](https://github.com/zephyrproject-rtos/zephyr/issues/16720) - drivers/loapic\_timer.c is buggy, needs cleanup
- [GitHub #16649](https://github.com/zephyrproject-rtos/zephyr/issues/16649) - z\_init\_timeout() ignores fn parameter
- [GitHub #16587](https://github.com/zephyrproject-rtos/zephyr/issues/16587) - build failures with gcc 9.x
- [GitHub #16436](https://github.com/zephyrproject-rtos/zephyr/issues/16436) - Organize generated include files
- [GitHub #16385](https://github.com/zephyrproject-rtos/zephyr/issues/16385) - watch dog timer causes the reboot on SAME70 board
- [GitHub #16330](https://github.com/zephyrproject-rtos/zephyr/issues/16330) - LPCXpresso55S69 secure/non-secure configuration
- [GitHub #16196](https://github.com/zephyrproject-rtos/zephyr/issues/16196) - display\_mcux\_elcdif driver full support frame buffer features
- [GitHub #16122](https://github.com/zephyrproject-rtos/zephyr/issues/16122) - Detect first block in LWM2M firmware updates.
- [GitHub #16096](https://github.com/zephyrproject-rtos/zephyr/issues/16096) - Sam gmac Ethernet driver should be able to detect the carrier state
- [GitHub #16072](https://github.com/zephyrproject-rtos/zephyr/issues/16072) - boards/up\_squared: k\_sleep() too long with local APIC timer
- [GitHub #15903](https://github.com/zephyrproject-rtos/zephyr/issues/15903) - Documentation missing for SPI and ADC async operations
- [GitHub #15680](https://github.com/zephyrproject-rtos/zephyr/issues/15680) - “backport v1.14 branch” label: update description and doc
- [GitHub #15565](https://github.com/zephyrproject-rtos/zephyr/issues/15565) - undefined references to `sys_rand32_get`
- [GitHub #15504](https://github.com/zephyrproject-rtos/zephyr/issues/15504) - Can I use one custom random static bd\_addr before provision?
- [GitHub #15499](https://github.com/zephyrproject-rtos/zephyr/issues/15499) - gpio\_intel\_apl: gpio\_pin\_read() pin value doesn’t match documentation
- [GitHub #15463](https://github.com/zephyrproject-rtos/zephyr/issues/15463) - soc/x86/apollo\_lake/soc\_gpio.h: leading zeros on decimal constants
- [GitHub #15449](https://github.com/zephyrproject-rtos/zephyr/issues/15449) - tests/net/ieee802154/crypto: Assertion Failure: ds\_test(dev) is false
- [GitHub #15343](https://github.com/zephyrproject-rtos/zephyr/issues/15343) - tests/kernel/interrupt: Assertion Failure in test\_prevent\_interruption
- [GitHub #15304](https://github.com/zephyrproject-rtos/zephyr/issues/15304) - merge gen\_kobject\_list.py and gen\_priv\_stacks.py
- [GitHub #15202](https://github.com/zephyrproject-rtos/zephyr/issues/15202) - tests/benchmarks/timing\_info measurements are suddenly higher than previous values on nrf52\_pca10040
- [GitHub #15181](https://github.com/zephyrproject-rtos/zephyr/issues/15181) - ztest issues
- [GitHub #15177](https://github.com/zephyrproject-rtos/zephyr/issues/15177) - samples/drivers/crypto: CBC and CTR mode not supported
- [GitHub #14972](https://github.com/zephyrproject-rtos/zephyr/issues/14972) - samples: Create README.rst
- [GitHub #14790](https://github.com/zephyrproject-rtos/zephyr/issues/14790) - google\_iot\_mqtt sample does not work with qemu\_x86 out of the box
- [GitHub #14763](https://github.com/zephyrproject-rtos/zephyr/issues/14763) - PCI debug logging cannot work with PCI-enabled NS16550
- [GitHub #14749](https://github.com/zephyrproject-rtos/zephyr/issues/14749) - Verify all samples work as intended
- [GitHub #14647](https://github.com/zephyrproject-rtos/zephyr/issues/14647) - IP: Zephyr replies to broadcast ethernet packets in other subnets on the same wire
- [GitHub #14591](https://github.com/zephyrproject-rtos/zephyr/issues/14591) - Infineon Tricore architecture support
- [GitHub #14540](https://github.com/zephyrproject-rtos/zephyr/issues/14540) - kernel: message queue MACRO not compatible with C++
- [GitHub #14302](https://github.com/zephyrproject-rtos/zephyr/issues/14302) - USB MSC fails USB3CV tests
- [GitHub #14173](https://github.com/zephyrproject-rtos/zephyr/issues/14173) - Configure QEMU to run independent of the host clock
- [GitHub #14122](https://github.com/zephyrproject-rtos/zephyr/issues/14122) - CONFIG\_FLOAT/CONFIG\_FP\_SHARING descriptions are confusing and contradictory
- [GitHub #14099](https://github.com/zephyrproject-rtos/zephyr/issues/14099) - Minnowboard doesn’t build tests/kernel/xip/
- [GitHub #13963](https://github.com/zephyrproject-rtos/zephyr/issues/13963) - up\_squared: evaluate removal of SBL-related special configurations
- [GitHub #13821](https://github.com/zephyrproject-rtos/zephyr/issues/13821) - tests/kernel/sched/schedule\_api: Assertion failed for test\_slice\_scheduling
- [GitHub #13783](https://github.com/zephyrproject-rtos/zephyr/issues/13783) - tests/kernel/mem\_protect/stackprot failure in frdm\_k64f due to limited privilege stack size
- [GitHub #13569](https://github.com/zephyrproject-rtos/zephyr/issues/13569) - ZTEST: Add optional float/double comparison support
- [GitHub #13468](https://github.com/zephyrproject-rtos/zephyr/issues/13468) - tests/drivers/watchdog/wdt\_basic\_api/testcase.yaml: Various version of “Waiting to restart MCU”
- [GitHub #13353](https://github.com/zephyrproject-rtos/zephyr/issues/13353) - z\_timeout\_remaining should subtract z\_clock\_elapsed
- [GitHub #12872](https://github.com/zephyrproject-rtos/zephyr/issues/12872) - Update uart api tests with configure/configure\_get apis
- [GitHub #12775](https://github.com/zephyrproject-rtos/zephyr/issues/12775) - USB audio isochronous endpoints
- [GitHub #12553](https://github.com/zephyrproject-rtos/zephyr/issues/12553) - List of tests that keep failing sporadically
- [GitHub #12478](https://github.com/zephyrproject-rtos/zephyr/issues/12478) - tests/drivers/ipm/peripheral.mailbox failing sporadically on qemu\_x86\_64 (timeout)
- [GitHub #12440](https://github.com/zephyrproject-rtos/zephyr/issues/12440) - Device discovery of direct advertising devices is not working
- [GitHub #12385](https://github.com/zephyrproject-rtos/zephyr/issues/12385) - Support touch button
- [GitHub #12264](https://github.com/zephyrproject-rtos/zephyr/issues/12264) - kernel: poll: outdated check for expired timeout
- [GitHub #11998](https://github.com/zephyrproject-rtos/zephyr/issues/11998) - intermittent failures in tests/kernel/common: test\_timeout\_order: (poll\_events[ii].state not equal to K\_POLL\_STATE\_SEM\_AVAILABLE)
- [GitHub #11928](https://github.com/zephyrproject-rtos/zephyr/issues/11928) - nRF UART nrfx drivers (nRF UARTE 0) won’t build
- [GitHub #11916](https://github.com/zephyrproject-rtos/zephyr/issues/11916) - ISR table (\_sw\_isr\_table) generation is fragile and can result in corrupted binaries
- [GitHub #11745](https://github.com/zephyrproject-rtos/zephyr/issues/11745) - logging: never leaves panic mode on fatal thread exception
- [GitHub #11261](https://github.com/zephyrproject-rtos/zephyr/issues/11261) - ARM Cortex-M4 (EFR32FG1P) MCU fails to wake up from sleep within \_sys\_soc\_suspend()
- [GitHub #11149](https://github.com/zephyrproject-rtos/zephyr/issues/11149) - subsys/bluetooth/host/rfcomm.c: Missing unlock
- [GitHub #11016](https://github.com/zephyrproject-rtos/zephyr/issues/11016) - nRF52840-PCA10056/59: Cannot bring up HCI0 when using HCI\_USB sample
- [GitHub #9994](https://github.com/zephyrproject-rtos/zephyr/issues/9994) - irq\_is\_enabled not available on nios2
- [GitHub #9962](https://github.com/zephyrproject-rtos/zephyr/issues/9962) - Migrate sensor drivers to device tree
- [GitHub #9953](https://github.com/zephyrproject-rtos/zephyr/issues/9953) - wrong behavior in pthread\_barrier\_wait()
- [GitHub #9741](https://github.com/zephyrproject-rtos/zephyr/issues/9741) - tests/kernel/spinlock:kernel.multiprocessing.spinlock\_bounce crashing on ESP32
- [GitHub #9711](https://github.com/zephyrproject-rtos/zephyr/issues/9711) - RFC: Zephyr should provide a unique id interface
- [GitHub #9608](https://github.com/zephyrproject-rtos/zephyr/issues/9608) - Bluetooth: different transaction collision
- [GitHub #9566](https://github.com/zephyrproject-rtos/zephyr/issues/9566) - Unclear definition of CONFIG\_IS\_BOOTLOADER
- [GitHub #8139](https://github.com/zephyrproject-rtos/zephyr/issues/8139) - Driver for BMA400 accelerometer
- [GitHub #7868](https://github.com/zephyrproject-rtos/zephyr/issues/7868) - Support non-recursive single-toolchain multi-image builds
- [GitHub #7564](https://github.com/zephyrproject-rtos/zephyr/issues/7564) - dtc: define list of acceptable warnings (and silent them with –warning -no<warnign-name> option)
- [GitHub #6648](https://github.com/zephyrproject-rtos/zephyr/issues/6648) - Trusted Execution Framework: practical use-cases (high-level overview)
- [GitHub #6015](https://github.com/zephyrproject-rtos/zephyr/issues/6015) - PWM on 32bit arch can get 0 pulse\_cycle because of 64bit calculation
- [GitHub #5857](https://github.com/zephyrproject-rtos/zephyr/issues/5857) - net: TCP retransmit queue implementation is broken
- [GitHub #5408](https://github.com/zephyrproject-rtos/zephyr/issues/5408) - Improve docs & samples on device tree overlay
- [GitHub #4985](https://github.com/zephyrproject-rtos/zephyr/issues/4985) - TEE support for ARMv8-M
- [GitHub #4911](https://github.com/zephyrproject-rtos/zephyr/issues/4911) - Filesystem support for qemu
- [GitHub #4832](https://github.com/zephyrproject-rtos/zephyr/issues/4832) - disco\_l475\_iot1: Provide 802.15.4 Sub-GHz
- [GitHub #4475](https://github.com/zephyrproject-rtos/zephyr/issues/4475) - Add support for Rigado BMD-3XX-EVAL boards
- [GitHub #4412](https://github.com/zephyrproject-rtos/zephyr/issues/4412) - Replace STM32 USB driver with DWC
- [GitHub #4326](https://github.com/zephyrproject-rtos/zephyr/issues/4326) - Port Zephyr to Cypress PSoC 6 MCU’s
- [GitHub #3909](https://github.com/zephyrproject-rtos/zephyr/issues/3909) - Add Atmel SAM QDEC Driver
- [GitHub #3730](https://github.com/zephyrproject-rtos/zephyr/issues/3730) - ESP32: DAC Driver support
- [GitHub #3729](https://github.com/zephyrproject-rtos/zephyr/issues/3729) - ESP32 ADC Driver Support
- [GitHub #3727](https://github.com/zephyrproject-rtos/zephyr/issues/3727) - ESP32: SPI Driver Support
- [GitHub #3726](https://github.com/zephyrproject-rtos/zephyr/issues/3726) - ESP32: DMA Driver Support
- [GitHub #3694](https://github.com/zephyrproject-rtos/zephyr/issues/3694) - i2c: Drivers are not thread safe
- [GitHub #3668](https://github.com/zephyrproject-rtos/zephyr/issues/3668) - timeslice reset is not tested for interrupt-induced swaps
- [GitHub #3564](https://github.com/zephyrproject-rtos/zephyr/issues/3564) - Requires more UART samples for STM32 Nucleo/similar boards
- [GitHub #3285](https://github.com/zephyrproject-rtos/zephyr/issues/3285) - Allow taking advantage of HW-based AES block cipher
- [GitHub #3232](https://github.com/zephyrproject-rtos/zephyr/issues/3232) - Add ksdk dma shim driver
- [GitHub #3076](https://github.com/zephyrproject-rtos/zephyr/issues/3076) - Add support for DAC (Digital to Analog Converter) drivers
- [GitHub #2585](https://github.com/zephyrproject-rtos/zephyr/issues/2585) - Support for LE legacy out-of-band pairing
- [GitHub #2566](https://github.com/zephyrproject-rtos/zephyr/issues/2566) - Create a tool for finding out stack sizes automatically.
- [GitHub #1900](https://github.com/zephyrproject-rtos/zephyr/issues/1900) - Framework for Trusted Execution Environment
- [GitHub #1894](https://github.com/zephyrproject-rtos/zephyr/issues/1894) - Secure Key Storage
- [GitHub #1333](https://github.com/zephyrproject-rtos/zephyr/issues/1333) - Provide build number in include/generated/version.h
