---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/release-notes-2.4.html
original_path: releases/release-notes-2.4.html
---

# Zephyr 2.4.0

We are pleased to announce the release of Zephyr RTOS version 2.4.0.

Major enhancements with this release include:

- Introduced initial support for virtual memory management.
- Added Bluetooth host support for periodic advertisement and isochronous
  channels.
- Enabled the new TCP stack, TCP2, by default. This stack was introduced in
  Zephyr v2.1.0 to improve network protocol testability with open source tools.
- Introduced a new toolchain abstraction with initial implementations for GCC
  and LLVM/Clang, and groundwork for future support of commercial toolchains.
- Moved to using C99 integer types and deprecate Zephyr integer types. The
  Zephyr types can be enabled by Kconfig DEPRECATED\_ZEPHYR\_INT\_TYPES option.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

- CVE-2020-10060: UpdateHub Might Dereference An Uninitialized Pointer
- CVE-2020-10064: Improper Input Frame Validation in ieee802154 Processing
- CVE-2020-10066: Incorrect Error Handling in Bluetooth HCI core
- CVE-2020-10072: all threads can access all socket file descriptors
- CVE-2020-13598: FS: Buffer Overflow when enabling Long File Names in FAT\_FS and calling fs\_stat
- CVE-2020-13599: Security problem with settings and littlefs
- CVE-2020-13601: Under embargo until 2020/11/18
- CVE-2020-13602: Remote Denial of Service in LwM2M do\_write\_op\_tlv

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## API Changes

- Moved to using C99 integer types and deprecate Zephyr integer types. The
  Zephyr types can be enabled by Kconfig DEPRECATED\_ZEPHYR\_INT\_TYPES option.
- The `<sys/util.h>` header has been promoted to a documented API with
  [experimental stability](../develop/api/api_lifecycle.md#api-lifecycle). See [Utilities](../kernel/util/index.md#util-api) for an API
  reference.
- The [`wdt_feed()`](../doxygen/html/group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe) function will now return `-EAGAIN` if
  issuing a feed would stall the caller. Application code may need to
  ignore this diagnostic result or initiate another feed operation
  later.
- `<drivers/uart.h>` has seen its callbacks normalized.
  [`uart_callback_t`](../doxygen/html/group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) and [`uart_irq_callback_user_data_t`](../doxygen/html/group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
  had their signature changed to add a struct device pointer as first parameter.
  `uart_irq_callback_t` has been removed. [`uart_callback_set()`](../doxygen/html/group__uart__async.md#gad33e627ed8729409b14e92453e53459c),
  [`uart_irq_callback_user_data_set()`](../doxygen/html/group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0) and [`uart_irq_callback_set()`](../doxygen/html/group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)
  user code have been modified accordingly.
- `<drivers/dma.h>` has seen its callback normalized. It had its signature
  changed to add a struct device pointer as first parameter. Such callback
  signature has been generalized through the addition of dma\_callback\_t.
  ‘callback\_arg’ argument has been renamed to ‘user\_data. All user code have
  been modified accordingly.
- `<drivers/ipm.h>` has seen its callback normalized.
  [`ipm_callback_t`](../doxygen/html/group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) had its signature changed to add a struct device
  pointer as first parameter. [`ipm_register_callback()`](../doxygen/html/group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b) user code have
  been modified accordingly. The context argument has been renamed to user\_data
  and all drivers have been modified against it as well.
- The [`fs_open()`](../doxygen/html/group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b) function now accepts open flags that are passed as
  a third parameter.
  All custom file system front-ends require change to the implementation
  of `open` callback to accept the new parameter.
  To maintain original behaviour within user code, two argument invocations
  should be converted to pass a third argument `FS_O_CREATE | FS_O_RDWR`.
- The struct device got 3 attributes renamed: `config_info` to `config`,
  `driver_api` to `api` and finally `driver_data` to `data`.
  This renaming was done to get rid of legacy names, for which the reasons
  do no longer apply.
- All device instances got a const qualifier. So this applies to all APIs
  manipulating `struct device *` (ADC, GPIO, I2C, …). In order to avoid
  const qualifier loss on ISRs, all ISRs now take a `const *void` as a
  parameter as well.
- The `_gatt_` and `_GATT_` infixes have been removed for the HRS, DIS
  and BAS APIs and the Kconfig options.
- `<include/bluetooth/gatt.h>` callback `bt_gatt_attr_func_t()` used by
  [`bt_gatt_foreach_attr()`](../doxygen/html/group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a) and [`bt_gatt_foreach_attr_type()`](../doxygen/html/group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10) has
  been changed to always pass the original pointer of attributes along with its
  resolved handle.
- Established the unrestricted alignment of flash reads for all drivers.

### Deprecated in this release

- The full set of `k_mem_pool` and `sys_mem_pool` APIs
  are considered deprecated as of this release. The replacements are
  the `k_heap` and `sys_heap` APIs. These APIs are not tagged with
  `__deprecated` in the 2.4 release, but will be in 2.5. They will be
  removed completely in Zephyr 2.6 LTS. The set of APIs now deprecated is as
  follows:

  - `k_mbox_data_block_get()`
  - `k_pipe_block_put()`
  - `K_MEM_POOL_DEFINE()`
  - `k_mem_pool_alloc()`
  - `k_mem_pool_free()`
  - `k_mem_pool_free_id()`
  - `SYS_MEM_POOL_DEFINE()`
  - `sys_mem_pool_init()`
  - `sys_mem_pool_alloc()`
  - `sys_mem_pool_free()`
  - `sys_mem_pool_try_expand_inplace()`
- The Kconfig option `CONFIG_MULTITHREADING` to disable multi-threading was
  deprecated due to lack of maintainership. This means that single-threaded
  mode with the scheduler disabled is deprecated; normal multi-threaded mode is
  still fully supported.

### Removed APIs in this release

- Other

  - The deprecated `MACRO_MAP` macro has been removed from the
    [Utilities](../kernel/util/index.md#util-api). Use `FOR_EACH` instead.
  - The CONFIG\_NET\_IF\_USERSPACE\_ACCESS is removed as it is no longer needed.
- Build system

  - The set of `*_if_kconfig()` CMake functions have been removed. Use
    `_ifdef(CONFIG_ ...)` instead.

### Stable API changes in this release

- USB

  - HID class callbacks now takes a parameter `const struct device*` which
    is the HID device for which callback was called.
- Bluetooth

  - The `_gatt_` infix has been removed from all GATT service APIs.
- Bluetooth HCI Driver

  - bt\_hci\_evt\_is\_prio() removed, use bt\_hci\_evt\_get\_flags() instead when
    CONFIG\_BT\_RECV\_IS\_RX\_THREAD is defined and call bt\_recv and bt\_recv\_prio
    when their flag is set, otherwise always call bt\_recv().

## Kernel

- Initial support for virtual memory management

  - API definitions in `include/sys/mem_manage.h`.
  - Supporting architectures will implement `arch_mem_map()` and enable
    `CONFIG_MMU`.
  - The kernel is linked at its physical memory location in RAM.
  - The size of the address space is controlled via `CONFIG_KERNEL_VM_SIZE`
    with memory mapping calls allocating virtual memory growing downward
    from the address space limit towards the system RAM mappings.
  - This infrastructure is still under heavy development.
- Device memory mapped I/O APIs

  - Namedspaced as DEVICE\_MMIO and specified in a new
    `include/sys/device_mmio.h` header.
  - This is added to facilitate the specification and the storage location of
    device driver memory-mapped I/O regions based on system configuration.

    - Maintained entirely in ROM for most systems.
    - Maintained in RAM with hooks to memory-mapping APIs for MMU or PCI-E
      systems.
- Updates for Memory Domain APIs

  - All threads now are always a member of a memory domain. A new
    memory domain `k_mem_domain_default` introduced for initial threads
    like the main thread.
  - The `k_mem_domain_destroy()` and `k_mem_domain_remove_thread()` APIs
    are now deprecated and will be removed in a future release.
  - Header definitions moved to `include/app_memory/mem_domain.h`.
- Thread stack specification improvements

  - Introduced a parallel set of `K_KERNEL_STACK_*` APIs for specifying
    thread stacks that will never host user threads. This will conserve memory
    as ancillary data structures (such as privilege mode elevation stacks) will
    not need to be created, and certain alignment requirements are less strict.
  - Internal interfaces to the architecture code have been simplified. All
    thread stack macros are now centrally defined, with arches declaring
    support macros to indicate the alignment of the stack pointer, the
    stack buffer base address, and the stack buffer size.

## Architectures

- ARC

  - Added ARC MetaWare toolchain support
  - General arch improvements for stacks & memory domains
  - API improvements for cache flush and cache invalidate
  - Debugging help: show all registers on exception
  - Fix for fast irq (one register bank configuration)
  - Fix for undefined shift behavior (CID 211523)
- ARM

  - AARCH32

    - Added support for ARM Cortex-M1 architecture.
    - Implemented the timing API in Cortex-M architecture using the Data
      Watchpoint and Trace (DWT) unit.
    - The interrupt vector relaying feature support was extended to Cortex-M
      Mainline architecture variants.
    - Cortex-M fault handling implementation was enhanced by adding an option to
      generate and supply the full register state to the kernel fatal error
      handling mechanism.
    - Fixed Cortex-M boot sequence for single-threaded applications
      (CONFIG\_MULTITHREADING=n).
    - Added thread safety to Non-Secure entry function calls in ARMv8-M
      architecture.
    - Fixed stack randomization for main thread.
    - Fixed exception vector table alignment in Cortex-M architecture
    - Increased test coverage in QEMU for ARMv6-M architecture variant.
    - Removed the implementation of arch\_mem\_domain\_\* APIs for Cortex-M
  - AARCH64

    - Re-implemented thread context-switch to use the \_arch\_switch() API
- POSIX
- RISC-V
- x86

  - x86 MMU paging support has been overhauled to meet CONFIG\_MMU requirements.

    - `arch_mem_map()` is implemented.
    - Restored support for 32-bit non-PAE paging. PAE use is now controlled
      via the `CONFIG_X86_PAE` option
    - Initial kernel page tables are now created at build time.
    - Page tables are no longer strictly identity-mapped
  - Added `zefi` infrastructure for packaging the 64-bit Zephyr kernel into
    an EFI application.
  - Added a GDB stub implementation that works over serial for x86 32-bit.

## Boards & SoC Support

- Added support for these SoC series:

  - ARM Cortex-M1/M3 DesignStart FPGA
  - Atmel SAM4L
  - Nordic nRF52805
  - NXP i.MX RT685, i.MX8M Mini, and LPC11U6x
  - ARC QEMU support for EM and HS family
- Made these changes in other SoC series:

  - STM32L4/STM32WB: Added support for Low Power Mode.
  - STM32H7/STM32WB/STM32MP1: Added Dual Core concurrent register access
    protection using HSEM.
  - Increased cpu frequency for ARC nsim\_hs\_smp.
- Changes for ARC boards:

  - ARC QEMU boards for ARC EM and HS
  - ARC MetaWare toolchain support, including mdb runner for various ARC boards
  - gcov coverage support for ARC QEMU
  - New nSIM configuration, corresponding to em7d\_v22 EMSK board
  - Enabled SMP on HSDK board, including dual core and quad core configurations.
  - Switched from legacy ARC-nSIM UART to ns16550 UART model and driver.
  - Fixed EMSDP secure config for emsdp\_em7d\_esp.
- Added support for these ARM boards:

  - Adafruit ItsyBitsy M4 Express
  - Arduino Nano 33 IOT
  - ARM Cortex-M1/M3 DesignStart FPGA reference designs running on the Digilent
    Arty A7 development board
  - Atmel SAM4L-EK board
  - Circuit Dojo nRF9160 Feather
  - EOS S3 Quick Feather
  - Laird Connectivity Pinnacle 100 Modem Development board (pinnacle\_100\_dvk)
  - nRF21540 DK (nrf21540dk\_nrf52840)
  - nRF52805 emulation on nRF52 DK (nrf52dk\_nrf52805)
  - nRF5340 DK
  - Nuvoton npcx7m6fb and pfm m487 boards
  - NXP i.MX RT685 EVK, i.MX8M Mini EVK, LPCXpresso LPC11U68
  - OLIMEX-STM32-H103
  - Ruuvitag board
  - Seagate FaZe board
  - Seeeduino XIAO
  - Serpente board
  - Silicon Labs BRD4180A (a.k.a. SLWRB4180A) Mighty Gecko Radio Board
  - ST B\_L4S5I\_IOT01A Discovery kit
  - ST NUCLEO-H745ZI-Q
  - Waveshare Open103Z
  - WeAct Studio Black Pill V2.0
- Made these changes in other boards:

  - b\_l072z\_lrwan1: Added flash, LoRa, USB, EEPROM, RNG
  - nRF boards: enabled HW Stack Protection by default on boards maintained by Nordic
  - nucleo\_l552ze\_q: Added non secure target and TFM support
  - STM32 boards: Enabled MPU on all boards with at least 64K flash
  - lpcxpresso55s69: Added TFM support
- Added support for these following shields:

  - Adafruit WINC1500 Wifi
  - ARM Ltd. V2C-DAPLink for DesignStart FPGA
  - Atmel AT86RF2XX Transceivers
  - Buydisplay 2.8” TFT Touch Shield with Arduino adapter
  - DAC80508 Evaluation Module

## Drivers and Sensors

- ADC

  - Added chip select flags to SPI ADC drivers.
- Audio

  - N/A
- Bluetooth

  - L2CAP RX MTU is now controlled by CONFIG\_BT\_L2CAP\_RX\_MTU when
    CONFIG\_BT\_ACL\_FLOW\_CONTROL is disabled, previously this was controlled
    by CONFIG\_BT\_RX\_BUF\_LEN. If CONFIG\_BT\_RX\_BUF\_LEN has been changed from its
    default value then CONFIG\_BT\_L2CAP\_RX\_MTU should be set to
    CONFIG\_BT\_RX\_BUF\_LEN - 8.
- CAN

  - Added chip select flags to SPI CAN drivers.
  - Fixed MCP2515 driver to wait to reset.
- Clock Control

  - STM32: Various changes including Flash latency wait states computation,
    configuration option additions for H7 series, and fixes on F0/F3 PREDIV1
    support
  - Added LPC11U6X driver.
- Console

  - Added IPM driver.
- Counter

  - STM32: Added support on F0/F2 series.
  - Added MCUX PIT counter driver for Kinetis K6x and K8x SoCs.
- Crypto

  - N/A
- DAC

  - STM32: Added support for F0/F2/G4/L1 series.
- Debug

  - N/A
- Display

  - Enhanced SSD16XX driver to support loading WS from OTP.
  - Added chip select flags to SPI display drivers.
- DMA

  - STM32: Number of changes including k\_malloc removal, driver priority init
    increase, get\_status API addition and various cleanups.
  - Added MCUX EDMA driver for i.MX RT and Kinetis K6x SoCs.
  - Added MCUX LPC driver for LPC and i.MX RT6xx SoCs.
- EEPROM

  - Added driver supporting the on-chip EEPROM found on NXP LPC11U6X MCUs.
  - Fixed at2x cs gpio flags extraction from DT.
- Entropy

  - STM32: Added support for ISR mode. Added support on F7/H7/L0 series.
- ESPI

  - Enhanced XEC driver to support KBC status operations, ACPI\_EC1 interface,
    and slaves with long initializations.
  - Fixed XEC driver frequency override during IO selection.
- Ethernet

  - Added VLAN support to Intel e1000 driver.
  - Added Ethernet support to stm32h7 based boards (with IT based TX).
  - Moved stm32 driver to device tree configuration.
  - Added support for setting fixed configuration and read from device tree
    for ENET ETH interface and PHY in mcux driver.
  - Added support for device that do not use SMI for PHY setup in mcux driver.
  - Added support for multiport gPTP in native\_posix driver. This allows gPTP
    bridging testing.
  - Fixed MAC registers in enc28j60 driver to the latest Microchip reference manual.
- Flash

  - The driver selected by `CONFIG_SPI_FLASH_W25QXXDV` has been
    removed as it is unmaintained and all its functionality is available
    through `CONFIG_SPI_NOR`. Out of tree uses should convert to the
    supported driver using the `jedec,spi-nor` compatible.
  - Enhanced nRF QSPI NOR flash driver (nrf\_qspi\_nor) so it supports unaligned read offset, read length and buffer offset.
  - Added SFDP support in spi\_nor driver.
  - Fixed regression in nRF flash driver (soc\_flash\_nrf) with [`CONFIG_BT_CTLR_LOW_LAT`](../kconfig.md#CONFIG_BT_CTLR_LOW_LAT "CONFIG_BT_CTLR_LOW_LAT") option.
  - Introduced NRF radio scheduler interface in nRF flash driver (soc\_flash\_nrf).
  - STM32: Factorized support for F0/F1/F3. Added L0 support. Various fixes.
- GPIO

  - Added driver for the Xilinx AXI GPIO IP.
  - Added LPC11U6X driver.
- Hardware Info

  - Added Atmel SAM4L driver.
- I2C

  - Introduced new driver for NXP LPC11U6x SoCs. See
    [`CONFIG_I2C_LPC11U6X`](../kconfig.md#CONFIG_I2C_LPC11U6X "CONFIG_I2C_LPC11U6X").
  - Introduced new driver for emulated I2C devices, where I2C operations
    are forwarded to a module that emulates responses from hardware.
    This enables testing without hardware and allows unusual conditions
    to be synthesized to test driver behavior. See
    [`CONFIG_I2C_EMUL`](../kconfig.md#CONFIG_I2C_EMUL "CONFIG_I2C_EMUL").
  - STM32: V1: Reset i2c device on read/write error.
  - STM32: V2: Added dts configurable Timing option.
  - Fixed MCUX LPI2C driver transfer status after NACK.
- I2S

  - Added LiteX controller driver.
- IEEE 802.15.4

  - Allow user to disable auto-start of IEEE 802.15.4 network interface.
    By default the IEEE 802.15.4 network interface is automatically started.
  - Added support for setting TX power in rf2xx driver.
  - Added Nordic 802.15.4 multiprotocol support, see [`CONFIG_NRF_802154_MULTIPROTOCOL_SUPPORT`](../kconfig.md#CONFIG_NRF_802154_MULTIPROTOCOL_SUPPORT "CONFIG_NRF_802154_MULTIPROTOCOL_SUPPORT").
  - Added Kconfig [`CONFIG_IEEE802154_VENDOR_OUI_ENABLE`](../kconfig.md#CONFIG_IEEE802154_VENDOR_OUI_ENABLE "CONFIG_IEEE802154_VENDOR_OUI_ENABLE") option for defining OUI.
- Interrupt Controller

  - Enhanced GICV3 driver to support SGI API.
  - Added NPCX MIWU driver.
- IPM

  - Added Intel ADSP driver.
- Keyboard Scan

  - Enhanced FT5336 driver to support additional part number variants.
- LED

  - Added TI LP503X controller driver.
  - Introduced led\_set\_color, let\_get\_info, and channel-dedicated syscalls
  - Added shell support.
- LED Strip

  - Enhanced APA102 driver to support SPI chip select.
- LoRa

  - Made various enhancements and fixes in SX1276 driver.
- Modem

  - Added option to query the IMSI and ICCID from the SIM.
  - Added support for offloaded Sierra Wireless HL7800 modem.
- PECI

  - N/A
- Pinmux

  - Added LPC11U6X driver.
  - Added NPCX driver.
- PS/2

  - N/A
- PWM

  - STM32: Refactored using Cube LL API.
  - Added SAM9 TCC based driver.
- Sensor

  - Added API function `sensor_attr_get()` for getting a sensor’s
    attribute.
  - Added support for wsen-itds accelerometer sensor.
  - Added chip select flags to SPI sensor drivers.
  - Added IIS2DH accelerometer driver.
  - Added MAX17055 fuel-gauge sensor driver.
  - Added SI7055 temperature sensor driver.
  - Enhanced FXOS8700 driver to support magnetic vector magnitude function.
  - Added SM351LT magnetoresistive sensor driver.
  - Added VCNL4040 proximity and light sensor driver.
  - Refactored LIS2DH and LSM6DSL drivers to support multiple instances.
- Serial

  - Added driver for the Xilinx UART Lite IP.
  - Added NXP IUART driver for i.MX8M Mini.
  - Implemented uart\_config\_get API in MCUX UART driver.
  - Added LPC11U6X driver.
- SPI

  - The SPI driver subsystem has been updated to use the flags specified
    in the cs-gpios devicetree properties rather than the
    SPI\_CS\_ACTIVE\_LOW/HIGH configuration options. Devicetree files that
    specify 0 for this field will probably need to be updated to specify
    GPIO\_ACTIVE\_LOW. SPI\_CS\_ACTIVE\_LOW/HIGH are still used for chip
    selects that are not specified by a cs-gpios property.
  - Added driver for the Xilinx AXI Quad SPI IP.
  - STM32: Various fixes around DMA mode.
  - Extended MCUX Flexcomm driver to support slave mode.
  - Added optional delays to MCUX DSPI and LPSPI drivers.
- Timer

  - N/A
- USB

  - The usb\_enable() function, which, for some samples, was invoked
    automatically on system boot up, now needs to be explicitly called
    by the application in order to enable the USB subsystem. If your
    application relies on any of the following Kconfig options, then
    it shall also enable the USB subsystem:

    - [`CONFIG_USB_DEVICE_NETWORK_ECM`](../kconfig.md#CONFIG_USB_DEVICE_NETWORK_ECM "CONFIG_USB_DEVICE_NETWORK_ECM")
    - [`CONFIG_USB_DEVICE_NETWORK_EEM`](../kconfig.md#CONFIG_USB_DEVICE_NETWORK_EEM "CONFIG_USB_DEVICE_NETWORK_EEM")
    - [`CONFIG_USB_DEVICE_NETWORK_RNDIS`](../kconfig.md#CONFIG_USB_DEVICE_NETWORK_RNDIS "CONFIG_USB_DEVICE_NETWORK_RNDIS")
    - [`CONFIG_TRACING_BACKEND_USB`](../kconfig.md#CONFIG_TRACING_BACKEND_USB "CONFIG_TRACING_BACKEND_USB")
    - `CONFIG_USB_UART_CONSOLE`
  - USB device support has got its own work queue
    which is used by CDC ACM class by default.
  - CDC ACM Class was slightly reworked.
  - Suspend and resume support in CDC ACM and HID classes
    has been corrected.
  - Atmel SAM0 USB device driver (usb\_dc\_sam0) was revised.
    All drivers now use common macros for getting indexes and direction
    from an endpoint.
- Video

  - N/A
- Watchdog

  - Added MCUX WWDT driver for LPC SoCs.
  - Enhanced Gecko driver to support Gecko Series 2 SoC.
- WiFi

  - Added IPv6 support to Simplelink driver.
  - Added DNS offloading support to eswifi driver.
  - Fixed esp driver offload protocol parsing.
  - Fixed esp driver GPIO reset control logic.
  - Fixed eswifi driver offloading packet parsing.

## Networking

- The new TCP stack is enabled by default. The legacy TCP stack is not yet
  removed and can be used if needed.
- The network interface is made a kernel object. This allows better access
  control handling when usermode is enabled.
- The kernel stacks are used in network related threads to save memory when
  usermode is enabled.
- Network statistics collection can be enabled in key points of the network
  stack. This can be used to get information where time is spent in RX or TX.
- The BSD socket sendmsg() can now be used with AF\_PACKET type sockets.
- Added support for enabling OpenThread reference device.
- Added support for enabling MQTT persistent sessions.
- Added “net tcp recv” command to net shell to enable TCP RX in manual testing.
- Added ObjLnk resource type support to LWM2M.
- Added userspace support to MQTT publisher, echo-server and echo-client
  sample applications.
- Added support to rejecting received and unsupported PPP options.
- Added support for select() when using socket offloading.
- Added support for IPv6 multicast packet routing.
- Added support to SOCK\_DGRAM type sockets for AF\_PACKET family.
- Added support for using TLS sockets when using socket offloading.
- Added additional checks in IPv6 to ensure that multicasts are only passed to the
  upper layer if the originating interface actually joined the destination
  multicast group.
- Allow user to specify TCP port number in HTTP request.
- Allow application to initialize the network config library instead of network
  stack calling initialization at startup. This enables better control of
  network resources but requires application to call net\_config\_init\_app()
  manually.
- Allow using wildcards in CoAP resource path description.
- Allow user to specify used network interface in net-shell ping command.
- Allow user to select a custom mbedtls library in OpenThread.
- Removed dependency to [`CONFIG_NET_SOCKETS_POSIX_NAMES`](../kconfig.md#CONFIG_NET_SOCKETS_POSIX_NAMES "CONFIG_NET_SOCKETS_POSIX_NAMES") from offloaded
  WiFi device drivers.
- Print more gPTP status information in gptp net shell.
- Fixed the network traffic class statistics collection.
- Fixed WiFi shell when doing a scan.
- Fixed IPv6 routes when nexthop is link local address of the connected peer.
- Fixed IPv6 Router Solicitation message handling.
- Fixed BSD socket lib and set errno to EBADF if socket descriptor is invalid.
- Fixed received DNS packet parsing.
- Fixed DNS resolving by ignoring incoming queries while we are resolving a name.
- Fixed CoAP zero length option parsing.
- Fixed gPTP port numbering to start from 1.
- Fixed gPTP BMCA priority vector calculation.
- Fixed multiple interface bound socket recv() for AF\_PACKET sockets.
- Fixed PPP Term-Req and Term-Ack packet length when sending them.
- Fixed PPP ipv6cp and ipcp Configure-Rej handling.
- Fixed PPP option parsing and negotiation handling.
- Fixed PPP ipcp option handling when the protocol goes down.
- Fixed PPP ipv6cp and ipcp network address removal when connection goes down.
- Added support to rejecting received and unsupported PPP options.
- Added initial support for PAP authentication in PPP.
- Fixed a race PPP when ppp\_fsm\_open() was called in CLOSED state.
- Fixed LWM2M FOTA socket closing.
- Fixed LWM2M block transfer retransmissions.
- Fixed LWM2M opaque data transfer in block mode.
- Fixed LWM2M Security and Server object instance matching.
- Fixed LWM2M updating lifetime on Register Update event.
- Fixed MQTT double CONNACK event notification on server reject.

## Bluetooth

- Host

  - Added basic support for Isochronous Channels (also known as LE Audio).
  - Added support for Periodic Advertising (both Advertising and Scanning
    procedures).
  - The application can now specify preferences for the PHY update procedure PHY
    choices.
  - A new “bond\_deleted” callback has been introduced.
  - Added a new callback for GATT (un)subscription.
  - Added support for the application to provide subscription information to the
    stack prior to reconnection (`bt_gatt_resubscribe`).
  - The application can now request for the CCC descriptor to be discovered
    automatically by the stack when subscribing to a characteristic.
  - Fixed a regression introduced in 2.3 along the EATT feature, where the ATT
    throughput could not reach the expected values.
  - Fixed a deadlock in the RX thread that was observed multiple times in
    scenarios involving high throughput and a sudden disconnection.
  - Fixed a race condition upon advertising resume.
  - The GATT notify multiple feature is now disabled by default.
  - The advertiser can now be requested to restart even when a connection
    object is not available.
  - The L2CAP security level will now be elevated automatically when a
    connection is rejected for security reasons.
  - When LE Secure Connections are the only option enabled, the security level
    will now be elevated to Level 4 automatically.
  - Fixed CCC restoring when using settings lazy loading.
  - Fixed recombination of ACL L2CAP PDUs when the header itself is split across
    multiple HCI ACL packets.
  - GATT no longer assumes the position of the CCC descriptor and instead
    discovers it.
  - Multiple additional fixes.
- Mesh

  - Added support for storage of model data in a key-value fashion.
  - Added support for a network loopback.
  - Multiple qualification-related fixes.
- BLE split software Controller

  - The advanced scheduling algorithms that were supported in the legacy
    Controller have been ported to the split one.
  - Preliminary support for Advertising Extensions, restricted to
    non-connectable advertising for now.
  - Very early support for Periodic Advertising. This should be considered an
    early experimental draft at this stage.
  - Added full support for the Nordic nRF5340 IC, not just the engineering
    sample.
  - Added support for the Nordic nRF52805 IC.
  - Several fixes to scheduling and window calculation, some of which had an
    impact in the cooperation between the flash driver and the Controller.
  - Fixed an null pointer dereference in the ticker code.
- HCI Driver

  - A new BT\_QUIRK\_NO\_AUTO\_DLE has been added for Controllers that do not follow
    the recommendation of auto-initating the data length update procedure. This
    is in fact the case of the split software Controller.

## Build and Infrastructure

- Improved support for additional toolchains:

  - Better toolchain abstractions.
  - Support for the ARC MetaWare toolchain.
- Devicetree

  - Added new devicetree macros that provide a default value if the property
    or cell accessor doesn’t contain the requested data.
  - Added support for inferring bindings for `/zephyr,user` devicetree node
    to allow applications an easy way to specify application specific
    devicetree properties without having a binding.
- Support for multiple SOC and ARCH roots.
  The [SOC\_ROOT](../develop/application/index.md#application) and `ARCH_ROOT` variables used to specify
  support files for out of tree SoCs and architectures now accept multiple
  paths, separated by semicolons. As a result, the `SOC_DIR` Kconfig variable
  is no longer supported.

  Uses like `source $(SOC_DIR)/<path>` must be changed to
  `rsource <relative>/<path>` or similar.
- BOARD, SOC, DTS, and ARCH roots can now be specified in each module’s
  `zephyr/module.yml` file; see [Build settings](../develop/modules.md#modules-build-settings).

## Libraries / Subsystems

- Disk
- Management

  - MCUmgr

    - Moved mcumgr into its own directory.
    - UDP port switched to using kernel stack.
    - smp: added missing socket close in error path.
  - Added support for Open Supervised Device Protocol (OSDP), see [`CONFIG_OSDP`](../kconfig.md#CONFIG_OSDP "CONFIG_OSDP").
  - updatehub

    - Added download block check.
    - Added support to flash integrity check using SHA-256 algorithm.
    - Moved updatehub from lib to subsys/mgmt directory.
    - Fixed out-of-bounds access and add flash\_img\_init return value check.
    - Fixed getaddrinfo resource leak.
- Settings

  - If a setting read is attempted from a channel that doesn’t support reading return an error rather than faulting.
  - Disallow modifying the content of a static subtree name.
- Random
- POSIX subsystem
- Power management
- Logging

  - Fixed immediate logging with multiple backends.
  - Switched logging thread to use kernel stack.
  - Allow users to disable all shell backends at one using [`CONFIG_SHELL_LOG_BACKEND`](../kconfig.md#CONFIG_SHELL_LOG_BACKEND "CONFIG_SHELL_LOG_BACKEND").
  - Added Spinel protocol logging backend.
  - Fixed timestamp calculation when using NEWLIB.
- LVGL

  - Library has been updated to the new major release v7.0.2.
  - It is important to note that v7 introduces multiple API changes and new
    configuration settings, so applications developed on v6 or previous versions
    will likely require some porting work. Refer to [LVGL 7 Release notes](https://github.com/lvgl/lvgl/releases/tag/v7.0.0) for more information.
  - LVGL Kconfig option names have been aligned with LVGL. All LVGL
    configuration options `LV_[A-Z0-9_]` have a matching Zephyr Kconfig
    option named as `CONFIG_LVGL_[A-Z0-9_]`.
  - LVGL Kconfig constants have been aligned with upstream suggested defaults.
    If your application relies on any of the following Kconfig defaults consider
    checking if the new values are good or they need to be adjusted:

    - `CONFIG_LVGL_HOR_RES_MAX`
    - `CONFIG_LVGL_VER_RES_MAX`
    - `CONFIG_LVGL_DPI`
    - `CONFIG_LVGL_DISP_DEF_REFR_PERIOD`
    - `CONFIG_LVGL_INDEV_DEF_READ_PERIOD`
    - `CONFIG_LVGL_INDEV_DEF_DRAG_THROW`
    - `CONFIG_LVGL_TXT_LINE_BREAK_LONG_LEN`
    - `CONFIG_LVGL_CHART_AXIS_TICK_LABEL_MAX_LEN`
  - Note that ROM usage is significantly higher on v7 for minimal
    configurations. This is in part due to new features such as the new drawing
    system. LVGL maintainers are currently investigating ways for reducing the
    library footprint when some options are not enabled, so you should wait for
    future releases if higher ROM usage is a concern for your application.
- Shell

  - Switched to use kernel stacks.
  - Fixed select command.
  - Fixed prompting dynamic commands.
  - Change behavior when more than `CONFIG_SHELL_ARGC_MAX` arguments are
    passed. Before 2.3 extra arguments were joined to the last argument.
    In 2.3 extra arguments caused a fault. Now the shell will report that
    the command cannot be processed.
- Storage

  - Added flash SHA-256 integrity check.
- Tracing

  - Tracing backed API now checks if init function exists prio to calling it.
- Debug

  - Core Dump

    - Added the ability to do core dump when fatal error is encountered.
      This allows dumping the CPU registers and memory content for offline
      debugging.
    - Cortex-M, x86, and x86-64 are supported in this release.
    - A data output backend utilizing the logging subsystem is introduced
      in this release.

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Documentation

## Tests and Samples

> - nvs: Do full chip erase when flashing.
> - nrf: onoff\_level\_lighting\_vnd\_app: Fixed build with mcumgr.
> - drivers: flash\_shell: new commands write\_unaligned and write\_pattern.
> - bluetooth: hci\_spi: Fixed cmd\_hdr and acl\_hdr usage.
> - Removed zephyr nfc sample.
> - drivers: Fixed uninitialized spi\_cfg in spi\_fujitsu\_fram sample.
> - Updated configuration for extended advertising in Bluetooth hci\_uart and hci\_rpmsg examples.

## Issue Related Items

These GitHub issues were addressed since the previous 2.3.0 tagged
release:

- [GitHub #28665](https://github.com/zephyrproject-rtos/zephyr/issues/28665) - boards b\_l4s5i\_iot01a: invertion of user LEDS polarity
- [GitHub #28659](https://github.com/zephyrproject-rtos/zephyr/issues/28659) - [Coverity CID :214346] Out-of-bounds access in subsys/net/ip/tcp2.c
- [GitHub #28654](https://github.com/zephyrproject-rtos/zephyr/issues/28654) - [lwm2m stm32F429] No registration with server possible
- [GitHub #28653](https://github.com/zephyrproject-rtos/zephyr/issues/28653) - Bluetooth: Mesh: TX Power Dynamic Control
- [GitHub #28639](https://github.com/zephyrproject-rtos/zephyr/issues/28639) - tests: kernel: sleep: is failing for nRF51
- [GitHub #28638](https://github.com/zephyrproject-rtos/zephyr/issues/28638) - bq274xx sample unable to build
- [GitHub #28635](https://github.com/zephyrproject-rtos/zephyr/issues/28635) - nrf: qspi: devicetree opcode properties are ignored
- [GitHub #28628](https://github.com/zephyrproject-rtos/zephyr/issues/28628) - samples/tfm\_integration/tfm\_ipc: regression on nucleo\_l552\_ze
- [GitHub #28627](https://github.com/zephyrproject-rtos/zephyr/issues/28627) - tests: kernel: fatal: exception: stack\_sentinel test is failing for nRF platforms
- [GitHub #28625](https://github.com/zephyrproject-rtos/zephyr/issues/28625) - tests: net: tcp2: llegal use of the EPSR
- [GitHub #28621](https://github.com/zephyrproject-rtos/zephyr/issues/28621) - tests: kernel: mem\_protect: syscalls: wrong FAULTY\_ADDRESS for nucleo\_l073rz
- [GitHub #28605](https://github.com/zephyrproject-rtos/zephyr/issues/28605) - Build failure - (64-bit platforms) acrn/bcm958402m2\_a72/native\_posix\_64/… on a number of sanitycheck tests w/TCP2
- [GitHub #28604](https://github.com/zephyrproject-rtos/zephyr/issues/28604) - mcumgr smp\_svr sample not working over shell or serial transport
- [GitHub #28603](https://github.com/zephyrproject-rtos/zephyr/issues/28603) - tests: kernel: timer: timer\_api: Failed on nucleo\_l073rz
- [GitHub #28602](https://github.com/zephyrproject-rtos/zephyr/issues/28602) - TCP2:frdm\_k64f/mimxrt1064\_evk tests/net/tcp2 regression failure in RC2
- [GitHub #28577](https://github.com/zephyrproject-rtos/zephyr/issues/28577) - possible bug / regression in new TCP stack
- [GitHub #28571](https://github.com/zephyrproject-rtos/zephyr/issues/28571) - Erroneous call to ull\_disable\_mark in ull\_adv::disable()
- [GitHub #28565](https://github.com/zephyrproject-rtos/zephyr/issues/28565) - sensor: lsm6dsl: incompatible pointer type (warning)
- [GitHub #28559](https://github.com/zephyrproject-rtos/zephyr/issues/28559) - Unable to extend the flash sync API part of the BLE Controller
- [GitHub #28552](https://github.com/zephyrproject-rtos/zephyr/issues/28552) - up\_squared: samples/portability/cmsis\_rtos\_v1/philosophers/ failed.
- [GitHub #28549](https://github.com/zephyrproject-rtos/zephyr/issues/28549) - up\_squared: tests/kernel/threads/thread\_apis/ failed
- [GitHub #28548](https://github.com/zephyrproject-rtos/zephyr/issues/28548) - up\_squared: tests/arch/x86/pagetables/ failed.
- [GitHub #28547](https://github.com/zephyrproject-rtos/zephyr/issues/28547) - up\_squared: tests/subsys/debug/coredump failed.
- [GitHub #28540](https://github.com/zephyrproject-rtos/zephyr/issues/28540) - littlefs: MPU FAULT and failed to run
- [GitHub #28538](https://github.com/zephyrproject-rtos/zephyr/issues/28538) - Atmel SAM4L have two pinctrl with wrong map
- [GitHub #28492](https://github.com/zephyrproject-rtos/zephyr/issues/28492) - Could not build Zephyr application for swervolf\_nexys board in simulation
- [GitHub #28480](https://github.com/zephyrproject-rtos/zephyr/issues/28480) - `tests/lib/devicetree/legacy_api/libraries.devicetree.legacy` fails to build on pinnacle\_100\_dvk
- [GitHub #28471](https://github.com/zephyrproject-rtos/zephyr/issues/28471) - Central not working properly on nRF5340-DK
- [GitHub #28465](https://github.com/zephyrproject-rtos/zephyr/issues/28465) - Building OpenThread NCP: build system has concurrency issue
- [GitHub #28460](https://github.com/zephyrproject-rtos/zephyr/issues/28460) - Generated ExternalProject include directories
- [GitHub #28453](https://github.com/zephyrproject-rtos/zephyr/issues/28453) - qemu 5.1 hangs on a number tests on x86\_64
- [GitHub #28443](https://github.com/zephyrproject-rtos/zephyr/issues/28443) - drivers: sensor: hts221 compilation issue linked to DT property drdy\_gpios
- [GitHub #28434](https://github.com/zephyrproject-rtos/zephyr/issues/28434) - Shell Tab Completion Candidates results in segmentation fault
- [GitHub #28414](https://github.com/zephyrproject-rtos/zephyr/issues/28414) - kernel/timeout: next\_timeout() is returning negative number of ticks
- [GitHub #28413](https://github.com/zephyrproject-rtos/zephyr/issues/28413) - [Coverity CID :214280] Unintentional integer overflow in tests/posix/common/src/nanosleep.c
- [GitHub #28412](https://github.com/zephyrproject-rtos/zephyr/issues/28412) - [Coverity CID :214279] ‘Constant’ variable guards dead code in tests/drivers/clock\_control/nrf\_lf\_clock\_start/src/main.c
- [GitHub #28411](https://github.com/zephyrproject-rtos/zephyr/issues/28411) - [Coverity CID :214281] Unchecked return value in subsys/mgmt/osdp/src/osdp.c
- [GitHub #28397](https://github.com/zephyrproject-rtos/zephyr/issues/28397) - gcc 10.x compile warning/error for array subscript is outside the bounds in cmsis\_rtos\_v2/thread.c
- [GitHub #28394](https://github.com/zephyrproject-rtos/zephyr/issues/28394) - nanosleep test failed on ARC series targets
- [GitHub #28390](https://github.com/zephyrproject-rtos/zephyr/issues/28390) - drivers: sensor: lsm6dsl compilation issue when sensor defined in board (I2C) and in test (SPI)
- [GitHub #28385](https://github.com/zephyrproject-rtos/zephyr/issues/28385) - drivers.clock.nrf\_lf\_clock\_start\_xtal\_no\_wait.wait\_in\_thread fails on nrf9160dk\_nrf9160
- [GitHub #28384](https://github.com/zephyrproject-rtos/zephyr/issues/28384) - Bluetooth: L2CAP: Bad CoC SDU segment handling
- [GitHub #28380](https://github.com/zephyrproject-rtos/zephyr/issues/28380) - drivers: peci: xec: Cannot recover PECI bus after PECI transfer fails
- [GitHub #28375](https://github.com/zephyrproject-rtos/zephyr/issues/28375) - gcc 10.x compile warning/error for array subscript 0 is outside the bounds in tests/bluetooth/tester/src/gap.c
- [GitHub #28371](https://github.com/zephyrproject-rtos/zephyr/issues/28371) - gcc 10.x compile warning/error for array subscript 0 is outside the bounds in subsys/bluetooth/mesh/prov.c
- [GitHub #28361](https://github.com/zephyrproject-rtos/zephyr/issues/28361) - USB audio samples fails if ASSERT=y
- [GitHub #28360](https://github.com/zephyrproject-rtos/zephyr/issues/28360) - drivers: nrf\_802154: SWI IRQ priority is not read correctly
- [GitHub #28347](https://github.com/zephyrproject-rtos/zephyr/issues/28347) - Possible use-after-free of rx\_msg->tx\_block in kernel/mailbox.c
- [GitHub #28344](https://github.com/zephyrproject-rtos/zephyr/issues/28344) - cdc\_acm sample with CONFIG\_NO\_OPTIMIZATIONS=y crashes on nrf52840 dev board
- [GitHub #28343](https://github.com/zephyrproject-rtos/zephyr/issues/28343) - Bluetooth peripheral sample auto disconnects “ST B\_L4S5I\_IOT01A Discovery kit”
- [GitHub #28341](https://github.com/zephyrproject-rtos/zephyr/issues/28341) - No SRAM available to link echo\_server for atsamr21 with ieee802154.overlay
- [GitHub #28337](https://github.com/zephyrproject-rtos/zephyr/issues/28337) - Cannot flash Atmel boards using west
- [GitHub #28332](https://github.com/zephyrproject-rtos/zephyr/issues/28332) - What is the airspeed velocity of an unladen swallow running Zephyr?
- [GitHub #28331](https://github.com/zephyrproject-rtos/zephyr/issues/28331) - Shell on CDC ACM UART stopped working after PR #24873
- [GitHub #28326](https://github.com/zephyrproject-rtos/zephyr/issues/28326) - Sample boards nrf mesh onoff not working
- [GitHub #28325](https://github.com/zephyrproject-rtos/zephyr/issues/28325) - bluetooth: null pointer dereference for non-connectable extended advertising
- [GitHub #28324](https://github.com/zephyrproject-rtos/zephyr/issues/28324) - GATT notifications aren’t working for CUD characteristics
- [GitHub #28319](https://github.com/zephyrproject-rtos/zephyr/issues/28319) - tests: kernel: context: fails because timer expiration is shorter than excepted
- [GitHub #28317](https://github.com/zephyrproject-rtos/zephyr/issues/28317) - Asymmetric nrfx spi\_transceive tx/rx lengths outputs error
- [GitHub #28307](https://github.com/zephyrproject-rtos/zephyr/issues/28307) - Can’t build bootloader/mcuboot while `CONF_FILE` contains multiple files.
- [GitHub #28305](https://github.com/zephyrproject-rtos/zephyr/issues/28305) - Device not found (SX1276 with nRF52840)
- [GitHub #28303](https://github.com/zephyrproject-rtos/zephyr/issues/28303) - nucleo\_l4r5zi uses wrong pinmux setting
- [GitHub #28295](https://github.com/zephyrproject-rtos/zephyr/issues/28295) - kernel.common: lpcxpresso55s16\_ns test failure
- [GitHub #28294](https://github.com/zephyrproject-rtos/zephyr/issues/28294) - arch.interrupt.gen\_isr\_table.arm\_mainline: lpcxpresso55s16\_ns failed
- [GitHub #28289](https://github.com/zephyrproject-rtos/zephyr/issues/28289) - tests: arch: arm: arm\_sw\_vector\_relay: fails on nucleo\_f091rc
- [GitHub #28283](https://github.com/zephyrproject-rtos/zephyr/issues/28283) - LWM2M: Invalid ACK when server is using message ID 0
- [GitHub #28282](https://github.com/zephyrproject-rtos/zephyr/issues/28282) - Slave host auto-initiate stalls if master does not support extended reject indications, and procedure collision occurs
- [GitHub #28280](https://github.com/zephyrproject-rtos/zephyr/issues/28280) - tests/kernel/tickless/tickless\_concept: disco\_l475\_iot1 build issue
- [GitHub #28275](https://github.com/zephyrproject-rtos/zephyr/issues/28275) - drivers: bluetooth: hci\_spi: hci driver is init before spi causing an error on device\_get\_binding
- [GitHub #28270](https://github.com/zephyrproject-rtos/zephyr/issues/28270) - Errors in the HL7800.c file
- [GitHub #28267](https://github.com/zephyrproject-rtos/zephyr/issues/28267) - up\_squared(acrn):running tests/kernel/workq/work\_queue\_api/ failed
- [GitHub #28266](https://github.com/zephyrproject-rtos/zephyr/issues/28266) - up\_squared(acrn):running tests/kernel/sched/schedule\_api/ failed
- [GitHub #28265](https://github.com/zephyrproject-rtos/zephyr/issues/28265) - up\_squared(acrn):running tests/kernel/timer/timer\_api/ failed
- [GitHub #28264](https://github.com/zephyrproject-rtos/zephyr/issues/28264) - up\_squared(acrn):running tests/kernel/timer/timer\_monotonic/ failed
- [GitHub #28262](https://github.com/zephyrproject-rtos/zephyr/issues/28262) - up\_squared(acrn):running tests/kernel/tickless/tickless\_concept/ failed
- [GitHub #28261](https://github.com/zephyrproject-rtos/zephyr/issues/28261) - up\_squared(acrn):running tests/kernel/common/ failed
- [GitHub #28260](https://github.com/zephyrproject-rtos/zephyr/issues/28260) - up\_squared(acrn):running tests/portability/cmsis\_rtos\_v2/ failed
- [GitHub #28259](https://github.com/zephyrproject-rtos/zephyr/issues/28259) - up\_squared(acrn):running tests/subsys/debug/coredump/ failed
- [GitHub #28258](https://github.com/zephyrproject-rtos/zephyr/issues/28258) - up\_squared(acrn):running tests/drivers/counter/counter\_cmos/ failed
- [GitHub #28256](https://github.com/zephyrproject-rtos/zephyr/issues/28256) - mimxrt1050\_evk: running samples/subsys/fs/fat\_fs/ failed
- [GitHub #28255](https://github.com/zephyrproject-rtos/zephyr/issues/28255) - mimxrt1050\_evk:running samples/drivers/display/ failed
- [GitHub #28251](https://github.com/zephyrproject-rtos/zephyr/issues/28251) - Tests of the cmsis\_dsp library fails on nrf52840dk\_nrf52840 platform
- [GitHub #28248](https://github.com/zephyrproject-rtos/zephyr/issues/28248) - bt\_gatt\_notify() causes “unable to alllocate TX buffer”
- [GitHub #28240](https://github.com/zephyrproject-rtos/zephyr/issues/28240) - nordic spim: does not work with SPI-SDHC infrastructure
- [GitHub #28234](https://github.com/zephyrproject-rtos/zephyr/issues/28234) - ipv6: multicast group: wrong filtering
- [GitHub #28230](https://github.com/zephyrproject-rtos/zephyr/issues/28230) - “make zephyr\_generated\_headers” produces incorrect result (SHELL:”) after recent cmake refactor
- [GitHub #28229](https://github.com/zephyrproject-rtos/zephyr/issues/28229) - Possible NULL dereference in subsys/net/ip/net\_context.c.
- [GitHub #28223](https://github.com/zephyrproject-rtos/zephyr/issues/28223) - LEDs in the board nRF52840dk\_nRF52840 dont work with Lora
- [GitHub #28218](https://github.com/zephyrproject-rtos/zephyr/issues/28218) - Possible NULL dereference in subsys/logging/log\_msg.c.
- [GitHub #28216](https://github.com/zephyrproject-rtos/zephyr/issues/28216) - socket: send fails instead of blocking when there are no more net buffers
- [GitHub #28211](https://github.com/zephyrproject-rtos/zephyr/issues/28211) - “High” current drawn when ussing RTT log back-end with CONFIG\_LOG\_IMMEDIATE and CONFIG\_LOG\_BACKEND\_RTT\_MODE\_DROP
- [GitHub #28206](https://github.com/zephyrproject-rtos/zephyr/issues/28206) - mimxrt685\_cm33: many cases has no console output seems hangs in kernel init.
- [GitHub #28205](https://github.com/zephyrproject-rtos/zephyr/issues/28205) - kernel.timer.tickless: frdmk64f failure
- [GitHub #28203](https://github.com/zephyrproject-rtos/zephyr/issues/28203) - Cannot flash TI boards using west
- [GitHub #28202](https://github.com/zephyrproject-rtos/zephyr/issues/28202) - Adafruit TFT touch shield cap touch flipped sides left-to-right
- [GitHub #28197](https://github.com/zephyrproject-rtos/zephyr/issues/28197) - samples/net/sockets/echo\_client/sample.net.sockets.echo\_client.nrf\_openthread fails to build
- [GitHub #28196](https://github.com/zephyrproject-rtos/zephyr/issues/28196) - samples/boards/intel\_s1000\_crb/audio/sample.board.intel\_s1000\_crb.audio Fails to build
- [GitHub #28193](https://github.com/zephyrproject-rtos/zephyr/issues/28193) - include/drivers/flash: API stands mistakenly unrestricted alignment of writes.
- [GitHub #28185](https://github.com/zephyrproject-rtos/zephyr/issues/28185) - Problem using SX1276 with nRF52840dk
- [GitHub #28184](https://github.com/zephyrproject-rtos/zephyr/issues/28184) - tests: drivers: spi: spi\_loopback: fails on board nucleo\_wb55rg
- [GitHub #28181](https://github.com/zephyrproject-rtos/zephyr/issues/28181) - MQTT not working with MOSQUITTO broker:
- [GitHub #28174](https://github.com/zephyrproject-rtos/zephyr/issues/28174) - [Coverity CID :214213] Improper use of negative value in tests/net/socket/af\_packet/src/main.c
- [GitHub #28173](https://github.com/zephyrproject-rtos/zephyr/issues/28173) - [Coverity CID :214210] Side effect in assertion in tests/arch/arm/arm\_interrupt/src/arm\_interrupt.c
- [GitHub #28172](https://github.com/zephyrproject-rtos/zephyr/issues/28172) - [Coverity CID :214227] Resource leak in subsys/mgmt/hawkbit/hawkbit.c
- [GitHub #28171](https://github.com/zephyrproject-rtos/zephyr/issues/28171) - [Coverity CID :214224] Unsigned compared against 0 in subsys/storage/flash\_map/flash\_map.c
- [GitHub #28169](https://github.com/zephyrproject-rtos/zephyr/issues/28169) - [Coverity CID :214220] Explicit null dereferenced in subsys/mgmt/hawkbit/hawkbit.c
- [GitHub #28167](https://github.com/zephyrproject-rtos/zephyr/issues/28167) - [Coverity CID :214209] Dereference after null check in subsys/mgmt/osdp/src/osdp.c
- [GitHub #28166](https://github.com/zephyrproject-rtos/zephyr/issues/28166) - [Coverity CID :214211] Unused value in drivers/entropy/entropy\_stm32.c
- [GitHub #28165](https://github.com/zephyrproject-rtos/zephyr/issues/28165) - [Coverity CID :214215] Out-of-bounds access in subsys/mgmt/mcumgr/smp\_shell.c
- [GitHub #28164](https://github.com/zephyrproject-rtos/zephyr/issues/28164) - [Coverity CID :214225] Buffer not null terminated in subsys/net/lib/lwm2m/ipso\_generic\_sensor.c
- [GitHub #28163](https://github.com/zephyrproject-rtos/zephyr/issues/28163) - [Coverity CID :214223] Untrusted value as argument in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #28162](https://github.com/zephyrproject-rtos/zephyr/issues/28162) - [Coverity CID :214221] Untrusted value as argument in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #28161](https://github.com/zephyrproject-rtos/zephyr/issues/28161) - [Coverity CID :214219] Uninitialized scalar variable in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #28160](https://github.com/zephyrproject-rtos/zephyr/issues/28160) - [Coverity CID :214212] Negative array index read in subsys/net/lib/dns/resolve.c
- [GitHub #28157](https://github.com/zephyrproject-rtos/zephyr/issues/28157) - benchmark.data\_structures fails(bus error) on mimxrt1020/60/64/frdmk64f platform
- [GitHub #28156](https://github.com/zephyrproject-rtos/zephyr/issues/28156) - twr\_kv58f220m: libraries.cmsis\_dsp.transform.cf64 test fails
- [GitHub #28154](https://github.com/zephyrproject-rtos/zephyr/issues/28154) - reel\_board:running samples/subsys/usb/console/ failed
- [GitHub #28153](https://github.com/zephyrproject-rtos/zephyr/issues/28153) - reel\_board: running samples/subsys/shell/fs/ failed
- [GitHub #28152](https://github.com/zephyrproject-rtos/zephyr/issues/28152) - frdm\_k64f: running samples/subsys/canbus/canopen/ failed
- [GitHub #28151](https://github.com/zephyrproject-rtos/zephyr/issues/28151) - gPTP should allow user setting of priority1 and priority2 fields used in BMCA
- [GitHub #28150](https://github.com/zephyrproject-rtos/zephyr/issues/28150) - mec15xxevb\_assy6853:running samples/boards/mec15xxevb\_assy6853/power\_management/ failed
- [GitHub #28149](https://github.com/zephyrproject-rtos/zephyr/issues/28149) - mec15xxevb\_assy6853:running samples/drivers/ps2/ failed
- [GitHub #28148](https://github.com/zephyrproject-rtos/zephyr/issues/28148) - mec15xxevb\_assy6853:running samples/drivers/espi/ failed
- [GitHub #28146](https://github.com/zephyrproject-rtos/zephyr/issues/28146) - mec15xxevb\_assy6853:running samples/drivers/kscan/ failed
- [GitHub #28145](https://github.com/zephyrproject-rtos/zephyr/issues/28145) - nRF52840 Dongle cannot scan LE Coded PHY devices
- [GitHub #28139](https://github.com/zephyrproject-rtos/zephyr/issues/28139) - tests: benchmarks: data\_structure\_perf: rbtree\_perf: uninitialized root struct
- [GitHub #28138](https://github.com/zephyrproject-rtos/zephyr/issues/28138) - No more able to flash board on windows
- [GitHub #28134](https://github.com/zephyrproject-rtos/zephyr/issues/28134) - mcuboot: specifying -DCONF\_FILE results in failure
- [GitHub #28133](https://github.com/zephyrproject-rtos/zephyr/issues/28133) - using nrf52dk\_nrf52832 with serial disabled
- [GitHub #28131](https://github.com/zephyrproject-rtos/zephyr/issues/28131) - Crash while serving large files via HTTP with TCP2
- [GitHub #28118](https://github.com/zephyrproject-rtos/zephyr/issues/28118) - timers strange rounding errors
- [GitHub #28114](https://github.com/zephyrproject-rtos/zephyr/issues/28114) - subsys: OSDP forces SERIAL=y
- [GitHub #28112](https://github.com/zephyrproject-rtos/zephyr/issues/28112) - timer/scheduler problem (STM32F407)
- [GitHub #28108](https://github.com/zephyrproject-rtos/zephyr/issues/28108) - EEPROM shell MPU Fault when performing a write command with more than 9 bytes
- [GitHub #28104](https://github.com/zephyrproject-rtos/zephyr/issues/28104) - sanitycheck overloaded by tests/subsys/logging/log\_immediate with large -j values
- [GitHub #28099](https://github.com/zephyrproject-rtos/zephyr/issues/28099) - subsys: power: device implicit depends on CONFIG\_SYS\_POWER\_MANAGEMENT
- [GitHub #28097](https://github.com/zephyrproject-rtos/zephyr/issues/28097) - cmake: fails to filter options for target language
- [GitHub #28095](https://github.com/zephyrproject-rtos/zephyr/issues/28095) - Doc: Getting Started Guide: reel board blinky gif is outdated
- [GitHub #28092](https://github.com/zephyrproject-rtos/zephyr/issues/28092) - Make SPI speed of SDHC card configurable
- [GitHub #28090](https://github.com/zephyrproject-rtos/zephyr/issues/28090) - bluetooth: build error with extended advertising
- [GitHub #28083](https://github.com/zephyrproject-rtos/zephyr/issues/28083) - Align MWDT and LD linker scripts
- [GitHub #28069](https://github.com/zephyrproject-rtos/zephyr/issues/28069) - eswifi: build failure
- [GitHub #28068](https://github.com/zephyrproject-rtos/zephyr/issues/28068) - Crash in USB device when turning HFXO off
- [GitHub #28061](https://github.com/zephyrproject-rtos/zephyr/issues/28061) - nrf52840 can’t boot up after power plug in,unless it was connected to JLINKRTTVIEWER with a JTAG
- [GitHub #28059](https://github.com/zephyrproject-rtos/zephyr/issues/28059) - sample for sensor lps22hh is not filtered out for bare nrf52dk\_nrf52832
- [GitHub #28057](https://github.com/zephyrproject-rtos/zephyr/issues/28057) - TCP2: client side receives EOF before all pending data is fed into it
- [GitHub #28053](https://github.com/zephyrproject-rtos/zephyr/issues/28053) - Eclipse broken build ability
- [GitHub #28052](https://github.com/zephyrproject-rtos/zephyr/issues/28052) - metairq\_dispatch sample fails on nrf platforms
- [GitHub #28049](https://github.com/zephyrproject-rtos/zephyr/issues/28049) - nucleo\_wb55rg: test/spi/spi\_loopback build failure
- [GitHub #28045](https://github.com/zephyrproject-rtos/zephyr/issues/28045) - [mimxrt1050\_evk] uart\_fifo\_fill only send 1 byte
- [GitHub #28040](https://github.com/zephyrproject-rtos/zephyr/issues/28040) - sanitycheck reports test timeouts as “exited with 2”
- [GitHub #28036](https://github.com/zephyrproject-rtos/zephyr/issues/28036) - samples/drivers/flash\_shell/sample.drivers.flash.shell fails to build on nucleo\_wb55rg
- [GitHub #28033](https://github.com/zephyrproject-rtos/zephyr/issues/28033) - rand32\_ctr\_drbg.c fails to build
- [GitHub #28032](https://github.com/zephyrproject-rtos/zephyr/issues/28032) - eth\_enc424j600 fails to build
- [GitHub #28031](https://github.com/zephyrproject-rtos/zephyr/issues/28031) - samples/subsys/mgmt/mcumgr/smp\_svr/sample.mcumg.smp\_svr.bt fails to build
- [GitHub #28020](https://github.com/zephyrproject-rtos/zephyr/issues/28020) - call k\_malloc or k\_mem\_slab\_alloc allowed or not
- [GitHub #28017](https://github.com/zephyrproject-rtos/zephyr/issues/28017) - tests/bluetooth/init/bluetooth.init.test\_controller\_dbg\_ll\_sw\_split fails to build on a few boards
- [GitHub #28016](https://github.com/zephyrproject-rtos/zephyr/issues/28016) - tests/boards/intel\_s1000\_crb/main/boards.s1000\_crb.main fails to build
- [GitHub #28013](https://github.com/zephyrproject-rtos/zephyr/issues/28013) - tests/misc/test\_build/buildsystem.kconfig.utf8\_in\_values fails on faze
- [GitHub #28012](https://github.com/zephyrproject-rtos/zephyr/issues/28012) - tests/net/lib/mqtt\_subscriber/net.mqtt.subscriber fails to build on cc3220sf\_launchxl
- [GitHub #28006](https://github.com/zephyrproject-rtos/zephyr/issues/28006) - Module: mbedtls broken following driver instances const-ification
- [GitHub #28003](https://github.com/zephyrproject-rtos/zephyr/issues/28003) - Module: segger broken following driver instances const-ification
- [GitHub #28000](https://github.com/zephyrproject-rtos/zephyr/issues/28000) - sam\_e70\_xplained:Test cases run failed at tests/net/lib/dns\_packet/.
- [GitHub #27985](https://github.com/zephyrproject-rtos/zephyr/issues/27985) - change in device initialization behavior
- [GitHub #27982](https://github.com/zephyrproject-rtos/zephyr/issues/27982) - TCP2: Apparent issues with client-side connections (hangs when server (apparently) closes connection).
- [GitHub #27964](https://github.com/zephyrproject-rtos/zephyr/issues/27964) - usb: Standard requests are not filtered.
- [GitHub #27963](https://github.com/zephyrproject-rtos/zephyr/issues/27963) - tests: net: socket: af\_packet: failed on nucleo\_f746zg
- [GitHub #27958](https://github.com/zephyrproject-rtos/zephyr/issues/27958) - USB: GET\_STATUS(Device) is improperly handled
- [GitHub #27943](https://github.com/zephyrproject-rtos/zephyr/issues/27943) - tests/kernel/sched/schedule\_api fails on nsim\_hs\_smp
- [GitHub #27935](https://github.com/zephyrproject-rtos/zephyr/issues/27935) - hci\_uart not acknowledging data correctly / losing packets
- [GitHub #27934](https://github.com/zephyrproject-rtos/zephyr/issues/27934) - Tests ignore custom board config overlays
- [GitHub #27931](https://github.com/zephyrproject-rtos/zephyr/issues/27931) - Address resolving when eswifi is used causes MPU FAULT
- [GitHub #27929](https://github.com/zephyrproject-rtos/zephyr/issues/27929) - Address resolving when eswifi is used causes MPU FAULT
- [GitHub #27928](https://github.com/zephyrproject-rtos/zephyr/issues/27928) - Settings api hangs
- [GitHub #27921](https://github.com/zephyrproject-rtos/zephyr/issues/27921) - Bluetooth: Dynamic TX power is overwritten every procedure
- [GitHub #27915](https://github.com/zephyrproject-rtos/zephyr/issues/27915) - Samples:LoRa send;sx126x with NRF52840dk ,no data from SPI miso
- [GitHub #27887](https://github.com/zephyrproject-rtos/zephyr/issues/27887) - Event counter may get out of sync when multiple events collide in ticker
- [GitHub #27880](https://github.com/zephyrproject-rtos/zephyr/issues/27880) - build errors for some samples/ on lpcxpresso55s69\_cpu1
- [GitHub #27876](https://github.com/zephyrproject-rtos/zephyr/issues/27876) - TCP2: Apparent issues with server-side connections (>1 connection doesn’t work properly)
- [GitHub #27874](https://github.com/zephyrproject-rtos/zephyr/issues/27874) - Nordic timer failures with synchronized periodic timers
- [GitHub #27867](https://github.com/zephyrproject-rtos/zephyr/issues/27867) - up\_squared: couldn’t get test result from serial of each test.
- [GitHub #27855](https://github.com/zephyrproject-rtos/zephyr/issues/27855) - i2c bitbanging on nrf52840
- [GitHub #27849](https://github.com/zephyrproject-rtos/zephyr/issues/27849) - tests: lib: cmsis\_dsp: transform: malloc out of memory
- [GitHub #27847](https://github.com/zephyrproject-rtos/zephyr/issues/27847) - tests/lib/sprintf fails on native\_posix\_64
- [GitHub #27843](https://github.com/zephyrproject-rtos/zephyr/issues/27843) - spi\_nor.c: Wrong buffers for rx\_set
- [GitHub #27838](https://github.com/zephyrproject-rtos/zephyr/issues/27838) - [Coverity CID :212961] Side effect in assertion in tests/kernel/threads/thread\_apis/src/test\_threads\_cancel\_abort.c
- [GitHub #27837](https://github.com/zephyrproject-rtos/zephyr/issues/27837) - [Coverity CID :212956] Out-of-bounds access in tests/kernel/mem\_protect/mem\_map/src/main.c
- [GitHub #27836](https://github.com/zephyrproject-rtos/zephyr/issues/27836) - [Coverity CID :212960] Logically dead code in samples/net/sockets/echo\_client/src/echo-client.c
- [GitHub #27835](https://github.com/zephyrproject-rtos/zephyr/issues/27835) - [Coverity CID :212962] Macro compares unsigned to 0 in include/sys/mem\_manage.h
- [GitHub #27834](https://github.com/zephyrproject-rtos/zephyr/issues/27834) - [Coverity CID :212959] Macro compares unsigned to 0 in include/sys/mem\_manage.h
- [GitHub #27833](https://github.com/zephyrproject-rtos/zephyr/issues/27833) - [Coverity CID :212958] Out-of-bounds access in arch/x86/core/x86\_mmu.c
- [GitHub #27832](https://github.com/zephyrproject-rtos/zephyr/issues/27832) - [Coverity CID :212957] Out-of-bounds access in arch/x86/core/x86\_mmu.c
- [GitHub #27821](https://github.com/zephyrproject-rtos/zephyr/issues/27821) - frdm\_k64f:running test cases /tests/subsys/power/power\_mgmt/ error
- [GitHub #27820](https://github.com/zephyrproject-rtos/zephyr/issues/27820) - reel\_board:running failed in tests/drivers/gpio/gpio\_api\_1pin/
- [GitHub #27813](https://github.com/zephyrproject-rtos/zephyr/issues/27813) - samples without sample.yaml
- [GitHub #27811](https://github.com/zephyrproject-rtos/zephyr/issues/27811) - intermittent failure of tests/net/socket/select on qemu\_x86
- [GitHub #27803](https://github.com/zephyrproject-rtos/zephyr/issues/27803) - samples: update to support new devicetree flag defaults
- [GitHub #27792](https://github.com/zephyrproject-rtos/zephyr/issues/27792) - Default clock settings for STM32F7 violates operating conditions
- [GitHub #27791](https://github.com/zephyrproject-rtos/zephyr/issues/27791) - DT\_DRV\_COMPAT in spi\_flash\_w25qxxdv.c named incorrectly
- [GitHub #27785](https://github.com/zephyrproject-rtos/zephyr/issues/27785) - memory domain arch implementation not correct with respect to SMP on ARC
- [GitHub #27783](https://github.com/zephyrproject-rtos/zephyr/issues/27783) - Add support for mbedTLS Server Name Indication (SNI) at configuration
- [GitHub #27771](https://github.com/zephyrproject-rtos/zephyr/issues/27771) - iotdk: cpu\_stats function doesn’t work as expected
- [GitHub #27768](https://github.com/zephyrproject-rtos/zephyr/issues/27768) - Usage fault when running with CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #27765](https://github.com/zephyrproject-rtos/zephyr/issues/27765) - Sanitycheck: non-existing test case shows up in .xml file.
- [GitHub #27753](https://github.com/zephyrproject-rtos/zephyr/issues/27753) - drivers: sensor: lis2dh: compilation issue struct lis2dh\_config’ has no member named ‘spi\_conf’
- [GitHub #27745](https://github.com/zephyrproject-rtos/zephyr/issues/27745) - Zephyr with host stack and hci driver only ?
- [GitHub #27738](https://github.com/zephyrproject-rtos/zephyr/issues/27738) - em\_starterkit\_7d sanitycheck test failure on testskernelmem\_protectsyscalls test
- [GitHub #27734](https://github.com/zephyrproject-rtos/zephyr/issues/27734) - vl53l0x driver gives wrong offset calibration value
- [GitHub #27727](https://github.com/zephyrproject-rtos/zephyr/issues/27727) - mcumgr serial interface does not work with CDC\_ACM UART
- [GitHub #27721](https://github.com/zephyrproject-rtos/zephyr/issues/27721) - Concurrent file descriptor allocations may return the same descriptor
- [GitHub #27718](https://github.com/zephyrproject-rtos/zephyr/issues/27718) - Updatehub might dereference an uninitialized pointer
- [GitHub #27712](https://github.com/zephyrproject-rtos/zephyr/issues/27712) - warnings when compiling smp\_svr with newlibc on 2.3.0
- [GitHub #27706](https://github.com/zephyrproject-rtos/zephyr/issues/27706) - Cannot debug specific files
- [GitHub #27693](https://github.com/zephyrproject-rtos/zephyr/issues/27693) - Crash on ARM when BT LE scan response packet too big
- [GitHub #27648](https://github.com/zephyrproject-rtos/zephyr/issues/27648) - [Coverity CID :212430] Unchecked return value in tests/kernel/msgq/msgq\_api/src/test\_msgq\_contexts.c
- [GitHub #27647](https://github.com/zephyrproject-rtos/zephyr/issues/27647) - [Coverity CID :212429] Negative array index write in tests/subsys/fs/fs\_api/src/test\_fs\_dir\_file.c
- [GitHub #27646](https://github.com/zephyrproject-rtos/zephyr/issues/27646) - [Coverity CID :212428] Unchecked return value in tests/kernel/msgq/msgq\_api/src/test\_msgq\_contexts.c
- [GitHub #27645](https://github.com/zephyrproject-rtos/zephyr/issues/27645) - [Coverity CID :212424] Unchecked return value in tests/kernel/msgq/msgq\_api/src/test\_msgq\_contexts.c
- [GitHub #27644](https://github.com/zephyrproject-rtos/zephyr/issues/27644) - [Coverity CID :212141] Improper use of negative value in tests/lib/fdtable/src/main.c
- [GitHub #27643](https://github.com/zephyrproject-rtos/zephyr/issues/27643) - [Coverity CID :212427] Invalid type in argument to printf format specifier in samples/drivers/jesd216/src/main.c
- [GitHub #27642](https://github.com/zephyrproject-rtos/zephyr/issues/27642) - [Coverity CID :212143] Unused value in samples/drivers/flash\_shell/src/main.c
- [GitHub #27641](https://github.com/zephyrproject-rtos/zephyr/issues/27641) - [Coverity CID :212142] Unused value in samples/drivers/flash\_shell/src/main.c
- [GitHub #27640](https://github.com/zephyrproject-rtos/zephyr/issues/27640) - [Coverity CID :212426] Unrecoverable parse warning in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27639](https://github.com/zephyrproject-rtos/zephyr/issues/27639) - [Coverity CID :212425] Out-of-bounds access in drivers/ethernet/eth\_mcux.c
- [GitHub #27637](https://github.com/zephyrproject-rtos/zephyr/issues/27637) - Bluetooth: controller: Possible corruption in AD data
- [GitHub #27636](https://github.com/zephyrproject-rtos/zephyr/issues/27636) - sensor: shell float output broken w/ CONFIG\_NEWLIB\_LIBC=y
- [GitHub #27634](https://github.com/zephyrproject-rtos/zephyr/issues/27634) - wifi simple\_link driver build error
- [GitHub #27613](https://github.com/zephyrproject-rtos/zephyr/issues/27613) - CONFIG\_ASSERT not working on nrf5340dk\_nrf5340\_cpunet in hci\_rpmsg sample
- [GitHub #27612](https://github.com/zephyrproject-rtos/zephyr/issues/27612) - RFC: API Change: usb: Device argument to USB HID ops
- [GitHub #27610](https://github.com/zephyrproject-rtos/zephyr/issues/27610) - UART\_ERROR\_FRAMING
- [GitHub #27600](https://github.com/zephyrproject-rtos/zephyr/issues/27600) - JSON Api refuse to decode null value
- [GitHub #27599](https://github.com/zephyrproject-rtos/zephyr/issues/27599) - bluetooth shell deadlock on USB shell UART
- [GitHub #27597](https://github.com/zephyrproject-rtos/zephyr/issues/27597) - build system fails to propagate devicetree change to Kconfig
- [GitHub #27592](https://github.com/zephyrproject-rtos/zephyr/issues/27592) - threads without name show up as junk names in SystemView
- [GitHub #27587](https://github.com/zephyrproject-rtos/zephyr/issues/27587) - New socket close() implementation broke build of platforms using socket offloading
- [GitHub #27582](https://github.com/zephyrproject-rtos/zephyr/issues/27582) - BT Identity address is overwritten when using extended advertising
- [GitHub #27580](https://github.com/zephyrproject-rtos/zephyr/issues/27580) - west install error
- [GitHub #27576](https://github.com/zephyrproject-rtos/zephyr/issues/27576) - sample.drivers.sample.drivers.peci failed to run
- [GitHub #27574](https://github.com/zephyrproject-rtos/zephyr/issues/27574) - mec15xxevb\_assy6853:arch.arm.arch.arm.no.multithreading failed to run
- [GitHub #27572](https://github.com/zephyrproject-rtos/zephyr/issues/27572) - mec15xxevb\_assy6853:crypto.tinycrypt.hmac\_prng.hmac\_prng failed to build,
- [GitHub #27571](https://github.com/zephyrproject-rtos/zephyr/issues/27571) - up\_squared:tests/portability/cmsis\_rtos\_v2/thread\_api failed
- [GitHub #27569](https://github.com/zephyrproject-rtos/zephyr/issues/27569) - mimxrt1050\_evk:samples.usb.cdc-acm-composite failed
- [GitHub #27566](https://github.com/zephyrproject-rtos/zephyr/issues/27566) - nRF52832: MCUBoot cannot read signed SMP Server Sample binary
- [GitHub #27560](https://github.com/zephyrproject-rtos/zephyr/issues/27560) - APIs for dynamically creating thread stacks
- [GitHub #27558](https://github.com/zephyrproject-rtos/zephyr/issues/27558) - “west update” only certain vendor
- [GitHub #27548](https://github.com/zephyrproject-rtos/zephyr/issues/27548) - CMake and west doesn’t accept multiple overlay files during build
- [GitHub #27547](https://github.com/zephyrproject-rtos/zephyr/issues/27547) - samples/boards/reel\_board/mesh\_badge fails booting with error in i2c\_nrfx\_twim
- [GitHub #27544](https://github.com/zephyrproject-rtos/zephyr/issues/27544) - TrustZone: NSC\_ALIGN gets redefined
- [GitHub #27533](https://github.com/zephyrproject-rtos/zephyr/issues/27533) - kernel crashes with small CONFIG\_TIMESLICE\_SIZE
- [GitHub #27531](https://github.com/zephyrproject-rtos/zephyr/issues/27531) - Zephyr testing via emulators
- [GitHub #27529](https://github.com/zephyrproject-rtos/zephyr/issues/27529) - sanitycheck: incorrect correct calculation of total\_skipped when –subset is set:
- [GitHub #27526](https://github.com/zephyrproject-rtos/zephyr/issues/27526) - poll(2) returning -1 errno ENOMEM
- [GitHub #27523](https://github.com/zephyrproject-rtos/zephyr/issues/27523) - [RFC] drivers: display: Implementing driver for sharp memory display
- [GitHub #27522](https://github.com/zephyrproject-rtos/zephyr/issues/27522) - shell: Output can get corrupted when printing from thread before command completes
- [GitHub #27511](https://github.com/zephyrproject-rtos/zephyr/issues/27511) - coverage: qemu platforms: sanitycheck generates many `unexpected eof` failures when enable coverage
- [GitHub #27505](https://github.com/zephyrproject-rtos/zephyr/issues/27505) - spi: mchp: Unintended data is transmitted when tx and rx operations are performed simultaneously
- [GitHub #27503](https://github.com/zephyrproject-rtos/zephyr/issues/27503) - testcases under zephyr/tests/application\_development take a very long time to dump coverage data
- [GitHub #27495](https://github.com/zephyrproject-rtos/zephyr/issues/27495) - Include full register state in ARM Cortex M Exception Stack Frame (ESF)
- [GitHub #27488](https://github.com/zephyrproject-rtos/zephyr/issues/27488) - Bluetooth Mesh samples don’t build
- [GitHub #27482](https://github.com/zephyrproject-rtos/zephyr/issues/27482) - Bluetooth stops responding when calling k\_delayed\_work\_submit. v2.3.0
- [GitHub #27473](https://github.com/zephyrproject-rtos/zephyr/issues/27473) - RT1050/60/64-evk board user LED does not work
- [GitHub #27465](https://github.com/zephyrproject-rtos/zephyr/issues/27465) - How recursively build boards on Zephyr?
- [GitHub #27464](https://github.com/zephyrproject-rtos/zephyr/issues/27464) - LOG\_BACKEND\_NET does not work for certain application/ip configurations
- [GitHub #27463](https://github.com/zephyrproject-rtos/zephyr/issues/27463) - Cannot build samples/net/sockets/echo for cc3220sf\_launchxl
- [GitHub #27448](https://github.com/zephyrproject-rtos/zephyr/issues/27448) - fatal error: device\_imx.h: No such file or directory
- [GitHub #27446](https://github.com/zephyrproject-rtos/zephyr/issues/27446) - Unable to flash cc1352r (no xds) with openocd in Zephyr SDK
- [GitHub #27444](https://github.com/zephyrproject-rtos/zephyr/issues/27444) - spi sdhc CS signal not working
- [GitHub #27434](https://github.com/zephyrproject-rtos/zephyr/issues/27434) - Bluetooth: L2CAP: buffer use after free
- [GitHub #27428](https://github.com/zephyrproject-rtos/zephyr/issues/27428) - Cannot compile network logging backend with IPv6-only
- [GitHub #27421](https://github.com/zephyrproject-rtos/zephyr/issues/27421) - libraries.cmsis\_dsp.matrix.binary\_q15: buffer allocation failure on twr\_kv58f220m
- [GitHub #27420](https://github.com/zephyrproject-rtos/zephyr/issues/27420) - drivers.uart: config test failure on uart\_mcux.c (was twr\_kv58f220m platform)
- [GitHub #27414](https://github.com/zephyrproject-rtos/zephyr/issues/27414) - Bluetooth: Controller: First advertisement does not preempt continuous scanner
- [GitHub #27404](https://github.com/zephyrproject-rtos/zephyr/issues/27404) - IS\_ENABLED not working with C++ (was: Is DT\_INST\_FOREACH\_STATUS\_OKAY broken on v2.3?)
- [GitHub #27403](https://github.com/zephyrproject-rtos/zephyr/issues/27403) - uart\_fifo\_read can only read one character
- [GitHub #27399](https://github.com/zephyrproject-rtos/zephyr/issues/27399) - [RFC] API change - Switch all struct device to constant
- [GitHub #27397](https://github.com/zephyrproject-rtos/zephyr/issues/27397) - [RFC] API change - Device structure attribute renaming
- [GitHub #27396](https://github.com/zephyrproject-rtos/zephyr/issues/27396) - samples/subsys/logging/logger timeout when sanitycheck enable coverage, it needs a filter
- [GitHub #27392](https://github.com/zephyrproject-rtos/zephyr/issues/27392) - tests/kernel/device/kernel.device.pm fails to build on cc1352r1\_launchxl
- [GitHub #27380](https://github.com/zephyrproject-rtos/zephyr/issues/27380) - Cannot use mcuboot with i.MXRT1060 due to a problem with the vector table address
- [GitHub #27379](https://github.com/zephyrproject-rtos/zephyr/issues/27379) - Macro Z\_ARC\_MPU\_SIZE\_ALIGN seems to be missing
- [GitHub #27377](https://github.com/zephyrproject-rtos/zephyr/issues/27377) - up\_squared(acrn):samples/philosophers/ caused the acrn platform crashed.
- [GitHub #27375](https://github.com/zephyrproject-rtos/zephyr/issues/27375) - “west zephyr-export” dumps stack if cmake is not installed
- [GitHub #27373](https://github.com/zephyrproject-rtos/zephyr/issues/27373) - CivetWeb Support for STM32H7 Series
- [GitHub #27370](https://github.com/zephyrproject-rtos/zephyr/issues/27370) - Constant asserts from nrf5 clock calibration
- [GitHub #27366](https://github.com/zephyrproject-rtos/zephyr/issues/27366) - tests: net: regression on many tests
- [GitHub #27363](https://github.com/zephyrproject-rtos/zephyr/issues/27363) - mec15xxevb\_assy6853:kernel.device.pm failed
- [GitHub #27362](https://github.com/zephyrproject-rtos/zephyr/issues/27362) - cannot move to 1M baud rate in bt\_shell
- [GitHub #27353](https://github.com/zephyrproject-rtos/zephyr/issues/27353) - west flash ignores –bin-file parameter and uses hex file when nrfjprog is used internally
- [GitHub #27348](https://github.com/zephyrproject-rtos/zephyr/issues/27348) - When using CONFIG\_NVS it triggers BUS FAULT during startup on “nucleo\_wb55rg” board
- [GitHub #27340](https://github.com/zephyrproject-rtos/zephyr/issues/27340) - <wrn> bt\_driver: Discarding event 0x3e
- [GitHub #27339](https://github.com/zephyrproject-rtos/zephyr/issues/27339) - up\_squared: Zephyr does not boot via grub anymore
- [GitHub #27338](https://github.com/zephyrproject-rtos/zephyr/issues/27338) - Bluetooth: host: GATT service request is not able to trigger the authentication procedure while in SC only mode
- [GitHub #27331](https://github.com/zephyrproject-rtos/zephyr/issues/27331) - Fails to upload over BLE using Zephyr with SMP Server Sample
- [GitHub #27330](https://github.com/zephyrproject-rtos/zephyr/issues/27330) - include in prj.conf
- [GitHub #27329](https://github.com/zephyrproject-rtos/zephyr/issues/27329) - [Coverity CID :211587] Unchecked return value in tests/drivers/clock\_control/clock\_control\_api/src/test\_clock\_control.c
- [GitHub #27328](https://github.com/zephyrproject-rtos/zephyr/issues/27328) - [Coverity CID :211586] Resource leak in tests/posix/fs/src/test\_fs\_open\_flags.c
- [GitHub #27327](https://github.com/zephyrproject-rtos/zephyr/issues/27327) - [Coverity CID :211585] Argument cannot be negative in tests/posix/fs/src/test\_fs\_open\_flags.c
- [GitHub #27326](https://github.com/zephyrproject-rtos/zephyr/issues/27326) - [Coverity CID :211584] Logically dead code in drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #27325](https://github.com/zephyrproject-rtos/zephyr/issues/27325) - [Coverity CID :211583] Unchecked return value in drivers/wifi/eswifi/eswifi\_socket.c
- [GitHub #27324](https://github.com/zephyrproject-rtos/zephyr/issues/27324) - [Coverity CID :211572] Out-of-bounds read in soc/xtensa/sample\_controller/include/\_soc\_inthandlers.h
- [GitHub #27323](https://github.com/zephyrproject-rtos/zephyr/issues/27323) - [Coverity CID :211551] Out-of-bounds read in soc/xtensa/sample\_controller/include/\_soc\_inthandlers.h
- [GitHub #27322](https://github.com/zephyrproject-rtos/zephyr/issues/27322) - [Coverity CID :211546] Out-of-bounds read in soc/xtensa/sample\_controller/include/\_soc\_inthandlers.h
- [GitHub #27321](https://github.com/zephyrproject-rtos/zephyr/issues/27321) - [Coverity CID :211539] Out-of-bounds read in soc/xtensa/sample\_controller/include/\_soc\_inthandlers.h
- [GitHub #27320](https://github.com/zephyrproject-rtos/zephyr/issues/27320) - [Coverity CID :211537] Out-of-bounds read in soc/xtensa/sample\_controller/include/\_soc\_inthandlers.h
- [GitHub #27319](https://github.com/zephyrproject-rtos/zephyr/issues/27319) - [Coverity CID :211523] Bad bit shift operation in arch/arc/core/mpu/arc\_mpu\_v2\_internal.h
- [GitHub #27318](https://github.com/zephyrproject-rtos/zephyr/issues/27318) - Decouple TLS socket from net\_context
- [GitHub #27303](https://github.com/zephyrproject-rtos/zephyr/issues/27303) - RFC: downgrade i2c eeprom\_slave driver to test
- [GitHub #27293](https://github.com/zephyrproject-rtos/zephyr/issues/27293) - Test nrf52840dk\_nrf52840 tests/net/socket/net\_mgmt/net.socket.mgmt build failure
- [GitHub #27288](https://github.com/zephyrproject-rtos/zephyr/issues/27288) - linker relocation feature fails for out of tree projects
- [GitHub #27282](https://github.com/zephyrproject-rtos/zephyr/issues/27282) - Drivers in app folder
- [GitHub #27280](https://github.com/zephyrproject-rtos/zephyr/issues/27280) - drivers: bluetooth: hci: spi: CS DT config not working because CS gpio\_dt\_flags are not set in the spi\_cs\_config struct
- [GitHub #27268](https://github.com/zephyrproject-rtos/zephyr/issues/27268) - usb: mcux RT1060 EVK - when using on-chip memory, USB fails
- [GitHub #27266](https://github.com/zephyrproject-rtos/zephyr/issues/27266) - samples: bluetooth: hci\_spi: Invalid cmd\_hdr and acl\_hdr usage
- [GitHub #27249](https://github.com/zephyrproject-rtos/zephyr/issues/27249) - Is there any development plan for supporting RPL stack ？
- [GitHub #27239](https://github.com/zephyrproject-rtos/zephyr/issues/27239) - samples/subsys/canbus/isotp/sample.subsys.canbus.isotp fails on FRDM-K64F
- [GitHub #27238](https://github.com/zephyrproject-rtos/zephyr/issues/27238) - tests/net/socket/af\_packet fails on FRDM-K64F
- [GitHub #27237](https://github.com/zephyrproject-rtos/zephyr/issues/27237) - Out\_of\_tree example broken
- [GitHub #27227](https://github.com/zephyrproject-rtos/zephyr/issues/27227) - shell crashes on qemu\_x86 board upon the Tab button press
- [GitHub #27220](https://github.com/zephyrproject-rtos/zephyr/issues/27220) - Bluetooth: L2CAP: l2cap\_change\_security() not considering bt\_conn::sec\_level when handling BT\_L2CAP\_LE\_ERR\_AUTHENTICATION
- [GitHub #27219](https://github.com/zephyrproject-rtos/zephyr/issues/27219) - thousands of lines of log spam in buildkite output
- [GitHub #27212](https://github.com/zephyrproject-rtos/zephyr/issues/27212) - drivers: clock\_control: stm32h7 cannot choose system frequency higher than 400MHz
- [GitHub #27211](https://github.com/zephyrproject-rtos/zephyr/issues/27211) - sanitycheck: add option to only build/run on emulated targets
- [GitHub #27205](https://github.com/zephyrproject-rtos/zephyr/issues/27205) - tests/kernel/timer/timer\_api test fails on twr\_ke18f
- [GitHub #27202](https://github.com/zephyrproject-rtos/zephyr/issues/27202) - tests/kernel/threads/thread\_apis failure on lpcxpresso55s16\_ns
- [GitHub #27181](https://github.com/zephyrproject-rtos/zephyr/issues/27181) - New drivers out of device tree
- [GitHub #27177](https://github.com/zephyrproject-rtos/zephyr/issues/27177) - Unable to build samples/bluetooth/st\_ble\_sensor for steval\_fcu001v1 board
- [GitHub #27173](https://github.com/zephyrproject-rtos/zephyr/issues/27173) - [v2.1] Unable to build Zephyr 2.1 for Upsquared board running ACRN
- [GitHub #27172](https://github.com/zephyrproject-rtos/zephyr/issues/27172) - shell: logging: CONFIG\_SHELL\_LOG\_BACKEND is forced if CONFIG\_LOG is chosen
- [GitHub #27166](https://github.com/zephyrproject-rtos/zephyr/issues/27166) - tests/kernel/sched/schedule\_api need add ram limitaion as some platform not support
- [GitHub #27164](https://github.com/zephyrproject-rtos/zephyr/issues/27164) - tests/lib/mem\_alloc failed on up\_squared board.
- [GitHub #27162](https://github.com/zephyrproject-rtos/zephyr/issues/27162) - reel\_board:tests/net/ieee802154/l2 failed.
- [GitHub #27161](https://github.com/zephyrproject-rtos/zephyr/issues/27161) - shell: shell\_start() and shell\_stop() can cause deadlock
- [GitHub #27154](https://github.com/zephyrproject-rtos/zephyr/issues/27154) - bt\_conn\_le\_param\_update doesn’t return an error when setting the timeout >30sec, stops device from sleeping on nrf52840
- [GitHub #27151](https://github.com/zephyrproject-rtos/zephyr/issues/27151) - sanitycheck: samples: net: echo\_server: Doesn’t run all configurations from atmel\_rf2xx shield
- [GitHub #27150](https://github.com/zephyrproject-rtos/zephyr/issues/27150) - [Coverity CID :211513] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #27149](https://github.com/zephyrproject-rtos/zephyr/issues/27149) - [Coverity CID :211508] Unchecked return value in tests/kernel/mem\_protect/futex/src/main.c
- [GitHub #27148](https://github.com/zephyrproject-rtos/zephyr/issues/27148) - [Coverity CID :211506] Operands don’t affect result in tests/drivers/clock\_control/nrf\_onoff\_and\_bt/src/main.c
- [GitHub #27147](https://github.com/zephyrproject-rtos/zephyr/issues/27147) - [Coverity CID :211505] Operands don’t affect result in tests/drivers/clock\_control/nrf\_onoff\_and\_bt/src/main.c
- [GitHub #27145](https://github.com/zephyrproject-rtos/zephyr/issues/27145) - [Coverity CID :211511] Dereference after null check in subsys/net/ip/net\_if.c
- [GitHub #27144](https://github.com/zephyrproject-rtos/zephyr/issues/27144) - [Coverity CID :211501] Explicit null dereferenced in subsys/net/ip/tcp2.c
- [GitHub #27143](https://github.com/zephyrproject-rtos/zephyr/issues/27143) - [Coverity CID :211512] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27142](https://github.com/zephyrproject-rtos/zephyr/issues/27142) - [Coverity CID :211509] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27141](https://github.com/zephyrproject-rtos/zephyr/issues/27141) - [Coverity CID :211507] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27140](https://github.com/zephyrproject-rtos/zephyr/issues/27140) - [Coverity CID :211504] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27139](https://github.com/zephyrproject-rtos/zephyr/issues/27139) - [Coverity CID :211503] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27138](https://github.com/zephyrproject-rtos/zephyr/issues/27138) - [Coverity CID :211502] Out-of-bounds read in drivers/wifi/eswifi/eswifi\_socket\_offload.c
- [GitHub #27130](https://github.com/zephyrproject-rtos/zephyr/issues/27130) - samples/drivers/spi\_flash has no README
- [GitHub #27120](https://github.com/zephyrproject-rtos/zephyr/issues/27120) - exception happened when running CI
- [GitHub #27118](https://github.com/zephyrproject-rtos/zephyr/issues/27118) - Bluetooth: HCI: Missing implementation of hci\_driver.h functions
- [GitHub #27112](https://github.com/zephyrproject-rtos/zephyr/issues/27112) - [v2.3.0] mcumgr fs download crashes
- [GitHub #27090](https://github.com/zephyrproject-rtos/zephyr/issues/27090) - LE Coded PHY scanning on nRF9160DK fails
- [GitHub #27081](https://github.com/zephyrproject-rtos/zephyr/issues/27081) - missing `python3-devel` dependency (was python3-psutil)
- [GitHub #27080](https://github.com/zephyrproject-rtos/zephyr/issues/27080) - uarte\_instance\_init() in NRF UARTE driver does not disable UART prior to setting PSEL pin values
- [GitHub #27079](https://github.com/zephyrproject-rtos/zephyr/issues/27079) - espi: driver: mchp: eSPI driver indicates flash channel is ready to eSPI host even before the channel negotiation takes place
- [GitHub #27078](https://github.com/zephyrproject-rtos/zephyr/issues/27078) - drivers: espi: mchp: Cannot perform multiple transactions over eSPI OOB channel
- [GitHub #27074](https://github.com/zephyrproject-rtos/zephyr/issues/27074) - doc: coding\_guidelines: broken links to MISRA-C example suite
- [GitHub #27071](https://github.com/zephyrproject-rtos/zephyr/issues/27071) - USB: CDC-ACM uart console hijacks usb\_enable call preventing user applications from registering callbacks
- [GitHub #27057](https://github.com/zephyrproject-rtos/zephyr/issues/27057) - NUCLEO-H745ZI-Q add cortex-m4 ethernet support
- [GitHub #27056](https://github.com/zephyrproject-rtos/zephyr/issues/27056) - Local header found before system header of same name
- [GitHub #27055](https://github.com/zephyrproject-rtos/zephyr/issues/27055) - BlueZ with ESP32 boards supported or not?
- [GitHub #27037](https://github.com/zephyrproject-rtos/zephyr/issues/27037) - No network interface found when running wifi sample
- [GitHub #27010](https://github.com/zephyrproject-rtos/zephyr/issues/27010) - net: ieee802154: wrong header generation
- [GitHub #27003](https://github.com/zephyrproject-rtos/zephyr/issues/27003) - CMakeLists.txt newline check is too strict
- [GitHub #27002](https://github.com/zephyrproject-rtos/zephyr/issues/27002) - checkpatch.pl incorrect ERROR:POINTER\_LOCATION
- [GitHub #26998](https://github.com/zephyrproject-rtos/zephyr/issues/26998) - [Coverity CID :211479] Unchecked return value in tests/kernel/mutex/mutex\_api/src/test\_mutex\_apis.c
- [GitHub #26997](https://github.com/zephyrproject-rtos/zephyr/issues/26997) - [Coverity CID :211474] Unchecked return value in tests/kernel/mutex/mutex\_api/src/test\_mutex\_apis.c
- [GitHub #26996](https://github.com/zephyrproject-rtos/zephyr/issues/26996) - [Coverity CID :211340] Side effect in assertion in tests/kernel/smp/src/main.c
- [GitHub #26995](https://github.com/zephyrproject-rtos/zephyr/issues/26995) - [Coverity CID :211478] Logically dead code in samples/net/sockets/big\_http\_download/src/big\_http\_download.c
- [GitHub #26994](https://github.com/zephyrproject-rtos/zephyr/issues/26994) - [Coverity CID :210616] Resource leak in lib/updatehub/updatehub.c
- [GitHub #26993](https://github.com/zephyrproject-rtos/zephyr/issues/26993) - [Coverity CID :210593] Out-of-bounds access in lib/updatehub/updatehub.c
- [GitHub #26992](https://github.com/zephyrproject-rtos/zephyr/issues/26992) - [Coverity CID :210547] Unchecked return value in lib/updatehub/updatehub.c
- [GitHub #26991](https://github.com/zephyrproject-rtos/zephyr/issues/26991) - [Coverity CID :210072] Resource leak in subsys/mgmt/smp\_udp.c
- [GitHub #26990](https://github.com/zephyrproject-rtos/zephyr/issues/26990) - i2c transfers are timing out with SSD1306 display
- [GitHub #26989](https://github.com/zephyrproject-rtos/zephyr/issues/26989) - [Coverity CID :211477] Unchecked return value in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #26988](https://github.com/zephyrproject-rtos/zephyr/issues/26988) - [Coverity CID :211473] Unchecked return value in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #26986](https://github.com/zephyrproject-rtos/zephyr/issues/26986) - [Coverity CID :211480] Printf arg count mismatch in arch/x86/zefi/zefi.c
- [GitHub #26985](https://github.com/zephyrproject-rtos/zephyr/issues/26985) - [Coverity CID :211476] Extra argument to printf format specifier in arch/x86/zefi/zefi.c
- [GitHub #26984](https://github.com/zephyrproject-rtos/zephyr/issues/26984) - sys/device\_mmio.h API design should accept generic DT node identifiers
- [GitHub #26983](https://github.com/zephyrproject-rtos/zephyr/issues/26983) - MPU FAULT in nRF52840-DK
- [GitHub #26981](https://github.com/zephyrproject-rtos/zephyr/issues/26981) - Problem with PPP + GSM MUX with SIMCOM7600E
- [GitHub #26970](https://github.com/zephyrproject-rtos/zephyr/issues/26970) - usb: overflow of USB transfers leads to clogging
- [GitHub #26966](https://github.com/zephyrproject-rtos/zephyr/issues/26966) - Example OTA-DFU for Android/IOS app
- [GitHub #26961](https://github.com/zephyrproject-rtos/zephyr/issues/26961) - occasional sanitycheck failures in samples/subsys/settings
- [GitHub #26954](https://github.com/zephyrproject-rtos/zephyr/issues/26954) - devicetree: warning: braces around scalar initializer
- [GitHub #26953](https://github.com/zephyrproject-rtos/zephyr/issues/26953) - settings: ISO C++ forbids converting a string constant to ‘char\*’
- [GitHub #26948](https://github.com/zephyrproject-rtos/zephyr/issues/26948) - cmake failure when using ZEPHYR\_MODULES without west
- [GitHub #26941](https://github.com/zephyrproject-rtos/zephyr/issues/26941) - Meta-IRQ documentation references
- [GitHub #26939](https://github.com/zephyrproject-rtos/zephyr/issues/26939) - MCUMGR - smp shell server sends responses to wrong port
- [GitHub #26937](https://github.com/zephyrproject-rtos/zephyr/issues/26937) - Kconfig choice Warning
- [GitHub #26924](https://github.com/zephyrproject-rtos/zephyr/issues/26924) - Bluetooth: Mesh: no space to store ccc cfg
- [GitHub #26923](https://github.com/zephyrproject-rtos/zephyr/issues/26923) - [RFC] API change - Normalize DMA, IPM and UART callbacks signatures including the caller’s device pointer.
- [GitHub #26919](https://github.com/zephyrproject-rtos/zephyr/issues/26919) - ipv6: promiscuous mode: packet flood over 802.15.4 adapter
- [GitHub #26914](https://github.com/zephyrproject-rtos/zephyr/issues/26914) - gen\_kobject\_list.py dosn’t generate correct gperf info for ARC MetaWare toolchain
- [GitHub #26910](https://github.com/zephyrproject-rtos/zephyr/issues/26910) - sanitycheck always treats warnings as errors
- [GitHub #26900](https://github.com/zephyrproject-rtos/zephyr/issues/26900) - Bluetooth: host: bt\_conn\_recv() assumes ACL data is >= 2 bytes
- [GitHub #26896](https://github.com/zephyrproject-rtos/zephyr/issues/26896) - STM32: mcu goes to sleep inadvertently when using PM.
- [GitHub #26868](https://github.com/zephyrproject-rtos/zephyr/issues/26868) - qemu\_x86\_64 icount support with SMP
- [GitHub #26862](https://github.com/zephyrproject-rtos/zephyr/issues/26862) - Bluetooth: GATT: CCC is not properly stored
- [GitHub #26848](https://github.com/zephyrproject-rtos/zephyr/issues/26848) - kernel: undefined reference with –no-gc-sections
- [GitHub #26833](https://github.com/zephyrproject-rtos/zephyr/issues/26833) - RFC: subsys: fs: Support file open flags to fs and POSIX API
- [GitHub #26832](https://github.com/zephyrproject-rtos/zephyr/issues/26832) - [mcux\_counter\_rtc][frdm\_k82f] counter\_basic\_api hangs
- [GitHub #26828](https://github.com/zephyrproject-rtos/zephyr/issues/26828) - Build Error - Network communication between Zephyr app on QEMU and Host OS
- [GitHub #26826](https://github.com/zephyrproject-rtos/zephyr/issues/26826) - i2c\_nrfx\_twi\_transfer hangs when SDA/SCL are set to pins 0,1
- [GitHub #26818](https://github.com/zephyrproject-rtos/zephyr/issues/26818) - drivers: uart\_console.c: usb\_enable() broken
- [GitHub #26814](https://github.com/zephyrproject-rtos/zephyr/issues/26814) - net\_ipv6\_send\_rs behaviour doesn’t comply with RFC4291
- [GitHub #26812](https://github.com/zephyrproject-rtos/zephyr/issues/26812) - NXP: tests/drivers/dma/loop\_transfer fails on FRDM-K64F
- [GitHub #26807](https://github.com/zephyrproject-rtos/zephyr/issues/26807) - Bluetooth HCI USB sample is not working
- [GitHub #26805](https://github.com/zephyrproject-rtos/zephyr/issues/26805) - test: drivers: i2c: i2c\_slave\_api:
- [GitHub #26804](https://github.com/zephyrproject-rtos/zephyr/issues/26804) - Bluetooth mesh repeated provision/gatt bearer connection crash
- [GitHub #26803](https://github.com/zephyrproject-rtos/zephyr/issues/26803) - Cortex-M7 Thumb-2 Instructions Alignment
- [GitHub #26801](https://github.com/zephyrproject-rtos/zephyr/issues/26801) - UART API has ifdefs around API functions
- [GitHub #26796](https://github.com/zephyrproject-rtos/zephyr/issues/26796) - Interrupts on Cortex-M do not work with CONFIG\_MULTITHREADING=n
- [GitHub #26793](https://github.com/zephyrproject-rtos/zephyr/issues/26793) - kernel: work: triggers immediately with longer timeouts
- [GitHub #26788](https://github.com/zephyrproject-rtos/zephyr/issues/26788) - cmake build system works wrong with cmake version 3.15.5
- [GitHub #26782](https://github.com/zephyrproject-rtos/zephyr/issues/26782) - boards: mchp: mec15xxevb\_assy6853: Cannot set gpios as alternate function when enabling multiple instances of a driver
- [GitHub #26769](https://github.com/zephyrproject-rtos/zephyr/issues/26769) - “west flash -r openocd –serial <serial\_num>” ignores serial\_num and flashes wrong board
- [GitHub #26766](https://github.com/zephyrproject-rtos/zephyr/issues/26766) - Build failure on nucleo\_wb55rg for tests/kernel/profiling/profiling\_api/kernel.common.profiling
- [GitHub #26764](https://github.com/zephyrproject-rtos/zephyr/issues/26764) - Build failure on intel\_s1000\_crb for samples/drivers/flash\_shell/sample.drivers.flash.shell
- [GitHub #26759](https://github.com/zephyrproject-rtos/zephyr/issues/26759) - Build error - Nothing found at GNUARMEMB\_TOOLCHAIN\_PATH
- [GitHub #26758](https://github.com/zephyrproject-rtos/zephyr/issues/26758) - Missing documentation of report targets (ram/rom report, puncover)
- [GitHub #26746](https://github.com/zephyrproject-rtos/zephyr/issues/26746) - Change sanitycheck to used pickled EDT
- [GitHub #26731](https://github.com/zephyrproject-rtos/zephyr/issues/26731) - Single channel selection - Bluetooth - Zephyr
- [GitHub #26729](https://github.com/zephyrproject-rtos/zephyr/issues/26729) - FCB flash\_area\_write fails on nRF52840DK when using mx25r64 storage
- [GitHub #26725](https://github.com/zephyrproject-rtos/zephyr/issues/26725) - USB suspend-resume process is not properly handled
- [GitHub #26723](https://github.com/zephyrproject-rtos/zephyr/issues/26723) - NULL handler in work queue entry can be called resulting in silent reboot
- [GitHub #26720](https://github.com/zephyrproject-rtos/zephyr/issues/26720) - lib: sockets: getaddrinfo don’t work without newlib C on ARM
- [GitHub #26717](https://github.com/zephyrproject-rtos/zephyr/issues/26717) - Big HTTP Download - Upgrade
- [GitHub #26708](https://github.com/zephyrproject-rtos/zephyr/issues/26708) - RFC: API Change: watchdog: wdt\_feed error codes
- [GitHub #26701](https://github.com/zephyrproject-rtos/zephyr/issues/26701) - Invalid handling of large cycle count in rtc timer
- [GitHub #26700](https://github.com/zephyrproject-rtos/zephyr/issues/26700) - waveshare\_open103z board can’t build tests/mem\_protect
- [GitHub #26695](https://github.com/zephyrproject-rtos/zephyr/issues/26695) - net: TCP2: connect() returns 0 without waiting for handshake completion
- [GitHub #26689](https://github.com/zephyrproject-rtos/zephyr/issues/26689) - Couldn’t get test result from serial on up\_squared board.
- [GitHub #26685](https://github.com/zephyrproject-rtos/zephyr/issues/26685) - sanitycheck “–only-failed” is broken
- [GitHub #26683](https://github.com/zephyrproject-rtos/zephyr/issues/26683) - Transition from non-secure to kernel causes “Stacking error”
- [GitHub #26679](https://github.com/zephyrproject-rtos/zephyr/issues/26679) - sanitycheck passes tests if the emulator exits unexpectedly
- [GitHub #26676](https://github.com/zephyrproject-rtos/zephyr/issues/26676) - MDB runner is not capturing real board’s output
- [GitHub #26665](https://github.com/zephyrproject-rtos/zephyr/issues/26665) - Implement reset for ARC development boards
- [GitHub #26664](https://github.com/zephyrproject-rtos/zephyr/issues/26664) - frdm\_kw41z: tests/drivers/pwm/pwm\_api fails in test\_pwm\_cycle()
- [GitHub #26663](https://github.com/zephyrproject-rtos/zephyr/issues/26663) - sanitycheck reports failing tests with em\_starterkit\_em7d\_v22 board
- [GitHub #26651](https://github.com/zephyrproject-rtos/zephyr/issues/26651) - Updatehub: frdm\_k64f resets in a loop
- [GitHub #26647](https://github.com/zephyrproject-rtos/zephyr/issues/26647) - build generates unaligned function reference in v2.3
- [GitHub #26643](https://github.com/zephyrproject-rtos/zephyr/issues/26643) - Nucleo board Slow Code execution at power up - need to always reset
- [GitHub #26628](https://github.com/zephyrproject-rtos/zephyr/issues/26628) - Couldn’t find Definition for CTE transmit and enable command for Connectionless AoA/AoD implementation in Zephyr
- [GitHub #26627](https://github.com/zephyrproject-rtos/zephyr/issues/26627) - tests/benchmarks/sys\_kernel failed on up\_squared.
- [GitHub #26626](https://github.com/zephyrproject-rtos/zephyr/issues/26626) - tests/portability/cmsis\_rtos\_v1 failed on reel\_board.
- [GitHub #26625](https://github.com/zephyrproject-rtos/zephyr/issues/26625) - tests/net/utils failed on multiple arm platforms.
- [GitHub #26624](https://github.com/zephyrproject-rtos/zephyr/issues/26624) - Noridc52840 hci\_usb bug on linux when “ discoverable on “ by bluetoothctl
- [GitHub #26621](https://github.com/zephyrproject-rtos/zephyr/issues/26621) - System can’t recover after assertion failed in kernel/mem\_domain.c
- [GitHub #26619](https://github.com/zephyrproject-rtos/zephyr/issues/26619) - tests/unit/rbtree fails
- [GitHub #26617](https://github.com/zephyrproject-rtos/zephyr/issues/26617) - devicetree: sam0 gclk
- [GitHub #26607](https://github.com/zephyrproject-rtos/zephyr/issues/26607) - STM32F0 nucleo PWM output not working
- [GitHub #26602](https://github.com/zephyrproject-rtos/zephyr/issues/26602) - GH Action: Automate removal of tag “Waiting for response”
- [GitHub #26600](https://github.com/zephyrproject-rtos/zephyr/issues/26600) - net.util test is broken on MPU-enabled ARM platforms
- [GitHub #26596](https://github.com/zephyrproject-rtos/zephyr/issues/26596) - west: rimage support in `west sign` poorly documented
- [GitHub #26595](https://github.com/zephyrproject-rtos/zephyr/issues/26595) - tests/kernel/obj\_tracing thread counting issue with 1.14 branch.
- [GitHub #26587](https://github.com/zephyrproject-rtos/zephyr/issues/26587) - DT\_CALL\_WITH\_ARG macro missing
- [GitHub #26586](https://github.com/zephyrproject-rtos/zephyr/issues/26586) - K\_TIMER\_DEFINE macro causing build error
- [GitHub #26582](https://github.com/zephyrproject-rtos/zephyr/issues/26582) - What happened to DT\_HAS\_NODE macro?
- [GitHub #26575](https://github.com/zephyrproject-rtos/zephyr/issues/26575) - devicetree: need save/restore support for devicetree data
- [GitHub #26568](https://github.com/zephyrproject-rtos/zephyr/issues/26568) - tests: net: socket: af\_packet: is ethernet cable now mandatory to run this test ?
- [GitHub #26555](https://github.com/zephyrproject-rtos/zephyr/issues/26555) - uart: uart\_nrfx\_uarte: async init does not cleanup previous sync rx
- [GitHub #26551](https://github.com/zephyrproject-rtos/zephyr/issues/26551) - sam0 devicetree failing to compile
- [GitHub #26536](https://github.com/zephyrproject-rtos/zephyr/issues/26536) - The CONFIG\_BT\_L2CAP\_RX\_MTU setting is not reflected correctly in the build
- [GitHub #26529](https://github.com/zephyrproject-rtos/zephyr/issues/26529) - How to support Nordic ble5.0 on Android 7.0？
- [GitHub #26527](https://github.com/zephyrproject-rtos/zephyr/issues/26527) - mimxrt1050\_evk:Couldn’t flash image by using west flash command.
- [GitHub #26524](https://github.com/zephyrproject-rtos/zephyr/issues/26524) - Problem with hci\_uart and L2CAP CoC connections
- [GitHub #26519](https://github.com/zephyrproject-rtos/zephyr/issues/26519) - samples: net: sockets: dumb\_http\_server: instabllity on nucleo\_f767zi
- [GitHub #26518](https://github.com/zephyrproject-rtos/zephyr/issues/26518) - NRF temperature sensor driver race condition
- [GitHub #26509](https://github.com/zephyrproject-rtos/zephyr/issues/26509) - net\_l2\_ppp.ppp\_link\_terminated: SARA U201 modem
- [GitHub #26508](https://github.com/zephyrproject-rtos/zephyr/issues/26508) - CI: simulated BT tests not run if BT tests are changed
- [GitHub #26506](https://github.com/zephyrproject-rtos/zephyr/issues/26506) - how does hci\_usb (hci\_usb fw : ncsv1.3.0zephyrsamplesbluetoothhci\_usb) set mac and send/receive files ?
- [GitHub #26505](https://github.com/zephyrproject-rtos/zephyr/issues/26505) - An example of using the microphone in Thingy 52
- [GitHub #26499](https://github.com/zephyrproject-rtos/zephyr/issues/26499) - usermode: random: backport random syscall
- [GitHub #26476](https://github.com/zephyrproject-rtos/zephyr/issues/26476) - ARM Cortex-A: architecture timer continuously firing in tick-less mode
- [GitHub #26467](https://github.com/zephyrproject-rtos/zephyr/issues/26467) - Bluetooth: Race-condition on persistent connectable advertiser
- [GitHub #26466](https://github.com/zephyrproject-rtos/zephyr/issues/26466) - Bluetooth: host: Do auto-postponement of advertising also when application requests advertising
- [GitHub #26455](https://github.com/zephyrproject-rtos/zephyr/issues/26455) - bme280 connect to rt1020\_evk
- [GitHub #26450](https://github.com/zephyrproject-rtos/zephyr/issues/26450) - Bad disconnect reason when client connects with wrong address type
- [GitHub #26438](https://github.com/zephyrproject-rtos/zephyr/issues/26438) - Bluetooth: Reconnection to paired/bonded peripheral fails
- [GitHub #26435](https://github.com/zephyrproject-rtos/zephyr/issues/26435) - Suspicious source code with subsys/random/random32\_entropy\_device: seg fault risk
- [GitHub #26434](https://github.com/zephyrproject-rtos/zephyr/issues/26434) - nrf9160 uart\_tx can return -ENOTSUP, which is not documented behavior
- [GitHub #26428](https://github.com/zephyrproject-rtos/zephyr/issues/26428) - LPSPI support for i.MX RT106x
- [GitHub #26427](https://github.com/zephyrproject-rtos/zephyr/issues/26427) - Linker problems with zephyr-sdk-0.11.2: undefined reference to ‘gettimeofday’
- [GitHub #26424](https://github.com/zephyrproject-rtos/zephyr/issues/26424) - master west.yml references pull in hal\_stm32
- [GitHub #26419](https://github.com/zephyrproject-rtos/zephyr/issues/26419) - Cannot request update when writing to external flash
- [GitHub #26415](https://github.com/zephyrproject-rtos/zephyr/issues/26415) - CONFIG\_FS\_LOG\_LEVEL\_OFF option doesn’t work with LittleFS
- [GitHub #26413](https://github.com/zephyrproject-rtos/zephyr/issues/26413) - disco\_l475\_iot1: flash storage corruption caused by partition overlap
- [GitHub #26410](https://github.com/zephyrproject-rtos/zephyr/issues/26410) - RFC: soc: Initial Nuvoton NPCX port
- [GitHub #26407](https://github.com/zephyrproject-rtos/zephyr/issues/26407) - fs: nvs: Incorrect handling of corrupt ate’s in nvs\_gc
- [GitHub #26406](https://github.com/zephyrproject-rtos/zephyr/issues/26406) - On x86, the main stack overflows when CONFIG\_NET\_IPV6 and CONFIG\_DEBUG are enabled
- [GitHub #26403](https://github.com/zephyrproject-rtos/zephyr/issues/26403) - Compile Error when trying to build samples/synchronization
- [GitHub #26397](https://github.com/zephyrproject-rtos/zephyr/issues/26397) - storage: flash\_map: Only works on limited compatibles
- [GitHub #26391](https://github.com/zephyrproject-rtos/zephyr/issues/26391) - stm32f746g: sample subsys/usb/hid-cdc does not work
- [GitHub #26377](https://github.com/zephyrproject-rtos/zephyr/issues/26377) - Problems getting I2C to work on NXP i.MX RT1020 EVK
- [GitHub #26372](https://github.com/zephyrproject-rtos/zephyr/issues/26372) - qspi driver does not work if multithreading is disabled
- [GitHub #26369](https://github.com/zephyrproject-rtos/zephyr/issues/26369) - C++ compilation warning for Z\_TIMEOUT\_TICKS
- [GitHub #26363](https://github.com/zephyrproject-rtos/zephyr/issues/26363) - samples: subsys: canbus: canopen: objdict: CO\_OD.h is not normally made.
- [GitHub #26362](https://github.com/zephyrproject-rtos/zephyr/issues/26362) - arc gdb failed to load core dump file
- [GitHub #26361](https://github.com/zephyrproject-rtos/zephyr/issues/26361) - [Coverity CID :211051] Explicit null dereferenced in tests/lib/ringbuffer/src/main.c
- [GitHub #26360](https://github.com/zephyrproject-rtos/zephyr/issues/26360) - [Coverity CID :211048] Side effect in assertion in tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #26359](https://github.com/zephyrproject-rtos/zephyr/issues/26359) - [Coverity CID :211047] Dereference null return value in tests/net/ipv6/src/main.c
- [GitHub #26358](https://github.com/zephyrproject-rtos/zephyr/issues/26358) - [Coverity CID :211044] Unchecked return value in tests/subsys/settings/fcb\_init/src/settings\_test\_fcb\_init.c
- [GitHub #26357](https://github.com/zephyrproject-rtos/zephyr/issues/26357) - [Coverity CID :211046] Unchecked return value in boards/posix/native\_posix/timer\_model.c
- [GitHub #26356](https://github.com/zephyrproject-rtos/zephyr/issues/26356) - [Coverity CID :211043] Logical vs. bitwise operator in subsys/net/lib/lwm2m/lwm2m\_rw\_oma\_tlv.c
- [GitHub #26355](https://github.com/zephyrproject-rtos/zephyr/issues/26355) - [Coverity CID :211045] Macro compares unsigned to 0 in kernel/timeout.c
- [GitHub #26354](https://github.com/zephyrproject-rtos/zephyr/issues/26354) - [Coverity CID :211040] Macro compares unsigned to 0 in kernel/timeout.c
- [GitHub #26353](https://github.com/zephyrproject-rtos/zephyr/issues/26353) - [Coverity CID :211039] Out-of-bounds access in drivers/gpio/gpio\_nrfx.c
- [GitHub #26352](https://github.com/zephyrproject-rtos/zephyr/issues/26352) - [Coverity CID :211049] Macro compares unsigned to 0 in arch/x86/core/x86\_mmu.c
- [GitHub #26343](https://github.com/zephyrproject-rtos/zephyr/issues/26343) - Gatt Bearer Issue
- [GitHub #26337](https://github.com/zephyrproject-rtos/zephyr/issues/26337) - BT scan: filter duplicates yields duplicates
- [GitHub #26333](https://github.com/zephyrproject-rtos/zephyr/issues/26333) - Bluetooth: Split LL: Cannot store Bluetooth keys
- [GitHub #26313](https://github.com/zephyrproject-rtos/zephyr/issues/26313) - nucleo\_h745zi\_q\_m7 pwm device tree bug
- [GitHub #26303](https://github.com/zephyrproject-rtos/zephyr/issues/26303) - Bluetooth: Windows 10 cannot reconnect on direct advertising from Zephyr
- [GitHub #26302](https://github.com/zephyrproject-rtos/zephyr/issues/26302) - Test gen\_isr\_tables from ./tests/kernel/gen\_isr\_table/ fails on nrf9160dk\_nrf9160
- [GitHub #26296](https://github.com/zephyrproject-rtos/zephyr/issues/26296) - Store logs in persistent storage (ext. flash, SD card)
- [GitHub #26295](https://github.com/zephyrproject-rtos/zephyr/issues/26295) - Enable persistent storage (ext flash/SD card) as logger backend
- [GitHub #26294](https://github.com/zephyrproject-rtos/zephyr/issues/26294) - Test suite output is hard to read
- [GitHub #26291](https://github.com/zephyrproject-rtos/zephyr/issues/26291) - canopen: error when CAN\_MCP2515\_MAX\_FILTER > 8
- [GitHub #26290](https://github.com/zephyrproject-rtos/zephyr/issues/26290) - gfhgf
- [GitHub #26284](https://github.com/zephyrproject-rtos/zephyr/issues/26284) - device.h doxygen
- [GitHub #26281](https://github.com/zephyrproject-rtos/zephyr/issues/26281) - Question: Does NRF52840-DK support both OpenThread and BLE at the same time
- [GitHub #26280](https://github.com/zephyrproject-rtos/zephyr/issues/26280) - test\_kernel\_systicks from tests/portability/cmsis\_rtos\_v1 fails on nrf platforms
- [GitHub #26279](https://github.com/zephyrproject-rtos/zephyr/issues/26279) - littlefs: Unable to erase external flash.
- [GitHub #26278](https://github.com/zephyrproject-rtos/zephyr/issues/26278) - [v2.2] bt\_att: Unhandled ATT code 0x1d
- [GitHub #26271](https://github.com/zephyrproject-rtos/zephyr/issues/26271) - k\_sleep/k\_msleep ends too early on UP\_squared board
- [GitHub #26267](https://github.com/zephyrproject-rtos/zephyr/issues/26267) - drivers: SPI: CS output type not honored
- [GitHub #26266](https://github.com/zephyrproject-rtos/zephyr/issues/26266) - Cast and shift operator priority issue may lead to wrong memory size result in fat\_fs example
- [GitHub #26265](https://github.com/zephyrproject-rtos/zephyr/issues/26265) - Zephyr os bluetooth peripheral example indication. When i flash code to my board custom configuration for indication will shown and after i click button for indication it device will disconnect from phone. My board is nrf52832.
- [GitHub #26264](https://github.com/zephyrproject-rtos/zephyr/issues/26264) - tests/benchmarks/latency\_measure failed on up\_squared board.
- [GitHub #26263](https://github.com/zephyrproject-rtos/zephyr/issues/26263) - reel\_board:tests/posix/common failed.
- [GitHub #26259](https://github.com/zephyrproject-rtos/zephyr/issues/26259) - Add AT86RF233 REB Xplained Pro Extension shield
- [GitHub #26256](https://github.com/zephyrproject-rtos/zephyr/issues/26256) - NRF51822 BLE Micro module: hangs on k\_msleep() (RTC counter not working)
- [GitHub #26255](https://github.com/zephyrproject-rtos/zephyr/issues/26255) - k\_uptime\_ticks() returns pointer instead of value
- [GitHub #26252](https://github.com/zephyrproject-rtos/zephyr/issues/26252) - bluetooth: controller: Cannot receive long packets
- [GitHub #26248](https://github.com/zephyrproject-rtos/zephyr/issues/26248) - A timer with 24-hour timeout fires immediately
- [GitHub #26242](https://github.com/zephyrproject-rtos/zephyr/issues/26242) - qemu\_x86 and qemu\_cortex\_m3 time handling broken with CONFIG\_QEMU\_ICOUNT
- [GitHub #26235](https://github.com/zephyrproject-rtos/zephyr/issues/26235) - multi vlan support networking
- [GitHub #26234](https://github.com/zephyrproject-rtos/zephyr/issues/26234) - Question: how can a NRF52840-DK’s clock be set to 64MHz
- [GitHub #26232](https://github.com/zephyrproject-rtos/zephyr/issues/26232) - Segger Embedded Studio doesn’t find the right python
- [GitHub #26220](https://github.com/zephyrproject-rtos/zephyr/issues/26220) - OpenThread L2 does not implement `enable` API function
- [GitHub #26209](https://github.com/zephyrproject-rtos/zephyr/issues/26209) - sanitycheck tries to run random *samples*, without being asked for
- [GitHub #26200](https://github.com/zephyrproject-rtos/zephyr/issues/26200) - BT\_LE\_ADV\_OPT\_EXT\_ADV causes bt\_le\_adv\_start to return -22
- [GitHub #26197](https://github.com/zephyrproject-rtos/zephyr/issues/26197) - tracking provenance of utility code
- [GitHub #26185](https://github.com/zephyrproject-rtos/zephyr/issues/26185) - Sample posix:eventfd fails on all platforms
- [GitHub #26177](https://github.com/zephyrproject-rtos/zephyr/issues/26177) - Bluetooth: Mesh: Friend node unexpected un-reference buffer
- [GitHub #26174](https://github.com/zephyrproject-rtos/zephyr/issues/26174) - Add STM32H7 Series Ethernet Driver Support
- [GitHub #26172](https://github.com/zephyrproject-rtos/zephyr/issues/26172) - Zephyr Master/Slave not conforming with Core Spec. 5.2 connection policies
- [GitHub #26169](https://github.com/zephyrproject-rtos/zephyr/issues/26169) - Enable -O0 for only one \*.c file
- [GitHub #26168](https://github.com/zephyrproject-rtos/zephyr/issues/26168) - arch-level memory-mapping interface
- [GitHub #26167](https://github.com/zephyrproject-rtos/zephyr/issues/26167) - Extend the sensor API with function for getting the value of a sensor attribute
- [GitHub #26165](https://github.com/zephyrproject-rtos/zephyr/issues/26165) - Clock not initialized in LPC Flexcomm UART driver
- [GitHub #26150](https://github.com/zephyrproject-rtos/zephyr/issues/26150) - storage/stream: flash\_img\_bytes\_written() might returns more than number of payload bytes written.
- [GitHub #26149](https://github.com/zephyrproject-rtos/zephyr/issues/26149) - building native\_posix against musl-libc
- [GitHub #26139](https://github.com/zephyrproject-rtos/zephyr/issues/26139) - west: nrfjprog and jlink runner leave SW-DP registers in enabled state
- [GitHub #26136](https://github.com/zephyrproject-rtos/zephyr/issues/26136) - CMake Error in Windows Environment
- [GitHub #26131](https://github.com/zephyrproject-rtos/zephyr/issues/26131) - nrf52840\_mdk: add support for nrf stock bootloader
- [GitHub #26119](https://github.com/zephyrproject-rtos/zephyr/issues/26119) - Compilation error when enabling MPU on STM32 L0 boards
- [GitHub #26112](https://github.com/zephyrproject-rtos/zephyr/issues/26112) - bug: cmake loops when passing overlay file with left slashes in file path
- [GitHub #26107](https://github.com/zephyrproject-rtos/zephyr/issues/26107) - driver MMIO virtual address space mapping
- [GitHub #26106](https://github.com/zephyrproject-rtos/zephyr/issues/26106) - mcumgr: smp\_bt: wrong notify MTU calculation with CONFIG\_BT\_GATT\_NOTIFY\_MULTIPLE
- [GitHub #26105](https://github.com/zephyrproject-rtos/zephyr/issues/26105) - Test kernel.memory\_protection.stack\_random fails on nrf52dk\_nrf52832
- [GitHub #26104](https://github.com/zephyrproject-rtos/zephyr/issues/26104) - Asynchronous input via UART
- [GitHub #26096](https://github.com/zephyrproject-rtos/zephyr/issues/26096) - cmake finds a DTC from Zephyr-SDK version, it tries to execute it, and it fails
- [GitHub #26095](https://github.com/zephyrproject-rtos/zephyr/issues/26095) - Requirements.txt pip version conflict
- [GitHub #26080](https://github.com/zephyrproject-rtos/zephyr/issues/26080) - gPTP time sync fails if having more than one port
- [GitHub #26076](https://github.com/zephyrproject-rtos/zephyr/issues/26076) - bug: cortex-m0: vector table base address is set to zero when soc has control over where to put vector table.
- [GitHub #26071](https://github.com/zephyrproject-rtos/zephyr/issues/26071) - Bluetooth: host: ATT sent callback lost
- [GitHub #26070](https://github.com/zephyrproject-rtos/zephyr/issues/26070) - Bluetooth: ATT request not processed
- [GitHub #26065](https://github.com/zephyrproject-rtos/zephyr/issues/26065) - sanitycheck reports failing tests with timeout as passing
- [GitHub #26064](https://github.com/zephyrproject-rtos/zephyr/issues/26064) - tests/kernel/timer/timer\_api failed on mec15xxevb\_assy6853 board.
- [GitHub #26059](https://github.com/zephyrproject-rtos/zephyr/issues/26059) - Potentially incorrect interrupt handling in nRF SoC .dtsi for GPIO
- [GitHub #26049](https://github.com/zephyrproject-rtos/zephyr/issues/26049) - False multiple define of irq with IRQ\_CONNECT
- [GitHub #26039](https://github.com/zephyrproject-rtos/zephyr/issues/26039) - tests: kernel: timer: timer\_api: regression on STM32 boards
- [GitHub #26038](https://github.com/zephyrproject-rtos/zephyr/issues/26038) - build zephyr with llvm fail
- [GitHub #26037](https://github.com/zephyrproject-rtos/zephyr/issues/26037) - RFC: API Change: Bluetooth Mesh
- [GitHub #26034](https://github.com/zephyrproject-rtos/zephyr/issues/26034) - menuconfig target aborts when Kconfig warnings are present
- [GitHub #26033](https://github.com/zephyrproject-rtos/zephyr/issues/26033) - NET\_SOCKETS\_OFFLOAD conflicts with POSIX\_API
- [GitHub #26030](https://github.com/zephyrproject-rtos/zephyr/issues/26030) - RV32M1\_RI5CY: tests/kernel/threads/thread\_apis and thread\_init fails
- [GitHub #26021](https://github.com/zephyrproject-rtos/zephyr/issues/26021) - Problems compiling for Measuring Time
- [GitHub #26017](https://github.com/zephyrproject-rtos/zephyr/issues/26017) - Build error in shell with gcc 10.1 (tests/drivers/uart/uart\_basic\_api)
- [GitHub #25991](https://github.com/zephyrproject-rtos/zephyr/issues/25991) - [net][net.socket.select][imx-rt series] test fails (k\_uptime\_get\_32() - tstamp <= FUZZ is false)
- [GitHub #25990](https://github.com/zephyrproject-rtos/zephyr/issues/25990) - tests/net/socket/select failed on sam\_e70\_xplained board.
- [GitHub #25989](https://github.com/zephyrproject-rtos/zephyr/issues/25989) - STM32\_LPTIM\_TIMER wrongly depends on DEVICE\_POWER\_MANAGEMENT
- [GitHub #25988](https://github.com/zephyrproject-rtos/zephyr/issues/25988) - [Coverity CID :210687] Argument cannot be negative in tests/net/socket/socketpair/src/test\_socketpair\_happy\_path.c
- [GitHub #25987](https://github.com/zephyrproject-rtos/zephyr/issues/25987) - [Coverity CID :210685] Pointless string comparison in tests/lib/devicetree/legacy\_api/src/main.c
- [GitHub #25986](https://github.com/zephyrproject-rtos/zephyr/issues/25986) - [Coverity CID :210684] Explicit null dereferenced in tests/kernel/mbox/mbox\_api/src/test\_mbox\_api.c
- [GitHub #25985](https://github.com/zephyrproject-rtos/zephyr/issues/25985) - [Coverity CID :210683] Pointless string comparison in tests/lib/devicetree/legacy\_api/src/main.c
- [GitHub #25984](https://github.com/zephyrproject-rtos/zephyr/issues/25984) - [Coverity CID :210686] Unchecked return value in lib/os/mempool.c
- [GitHub #25983](https://github.com/zephyrproject-rtos/zephyr/issues/25983) - [Coverity CID :210682] Unchecked return value in lib/os/mempool.c
- [GitHub #25982](https://github.com/zephyrproject-rtos/zephyr/issues/25982) - [Coverity CID :210020] Explicit null dereferenced in drivers/usb/device/usb\_dc\_mcux\_ehci.c
- [GitHub #25981](https://github.com/zephyrproject-rtos/zephyr/issues/25981) - Support storing mcuboot images on serial flash accessed through Nordic QSPI
- [GitHub #25979](https://github.com/zephyrproject-rtos/zephyr/issues/25979) - Need root LICENSE files in hal\_stm32 module
- [GitHub #25965](https://github.com/zephyrproject-rtos/zephyr/issues/25965) - hci\_uart not responding at higher baudrates on NRF52810
- [GitHub #25964](https://github.com/zephyrproject-rtos/zephyr/issues/25964) - Bluetooth: <err> bt\_att: ATT Timeout
- [GitHub #25958](https://github.com/zephyrproject-rtos/zephyr/issues/25958) - Concept Overview for improving support for serial flash devices via SPI and QSPI
- [GitHub #25956](https://github.com/zephyrproject-rtos/zephyr/issues/25956) - Including header files from modules into app
- [GitHub #25952](https://github.com/zephyrproject-rtos/zephyr/issues/25952) - STM32 LPTIM driver doesn’t restart counter after sleeping K\_TICKS\_FOREVER
- [GitHub #25945](https://github.com/zephyrproject-rtos/zephyr/issues/25945) - devicetree: support generating symbols for -gpios properties w/o compatible
- [GitHub #25942](https://github.com/zephyrproject-rtos/zephyr/issues/25942) - Bluetooth: Scanning + Non-connectable advertising broken on nRF5340
- [GitHub #25926](https://github.com/zephyrproject-rtos/zephyr/issues/25926) - k\_cycle\_get\_32() returns 0 in native\_posix
- [GitHub #25920](https://github.com/zephyrproject-rtos/zephyr/issues/25920) - Compilation error when CONFIG\_BOOTLOADER\_MCUBOOT=y specified
- [GitHub #25919](https://github.com/zephyrproject-rtos/zephyr/issues/25919) - dhcpv4 or rx ethernet packets not working on nucleo\_f429zi
- [GitHub #25892](https://github.com/zephyrproject-rtos/zephyr/issues/25892) - arc emsdp board work wrong with emsdp\_em7d\_esp config
- [GitHub #25869](https://github.com/zephyrproject-rtos/zephyr/issues/25869) - 2.3: Missing release notes
- [GitHub #25865](https://github.com/zephyrproject-rtos/zephyr/issues/25865) - Device Tree Memory Layout
- [GitHub #25859](https://github.com/zephyrproject-rtos/zephyr/issues/25859) - mesh example not working with switched off dcdc?
- [GitHub #25853](https://github.com/zephyrproject-rtos/zephyr/issues/25853) - modem\_ublox\_sara\_r4: Cannot connect to UDP remote
- [GitHub #25833](https://github.com/zephyrproject-rtos/zephyr/issues/25833) - [lpcxpresso55s69\_cpu1] no applications and build guide, hello world can not build
- [GitHub #25827](https://github.com/zephyrproject-rtos/zephyr/issues/25827) - Devicetree: add accessors with defaults
- [GitHub #25794](https://github.com/zephyrproject-rtos/zephyr/issues/25794) - [Coverity CID :210554] Uninitialized scalar variable in tests/net/iface/src/main.c
- [GitHub #25792](https://github.com/zephyrproject-rtos/zephyr/issues/25792) - [Coverity CID :210552] Resource leak in tests/net/pm/src/main.c
- [GitHub #25790](https://github.com/zephyrproject-rtos/zephyr/issues/25790) - [Coverity CID :210594] Dereference after null check in subsys/testsuite/ztest/src/ztest\_mock.c
- [GitHub #25786](https://github.com/zephyrproject-rtos/zephyr/issues/25786) - [Coverity CID :210558] Dereference before null check in drivers/sensor/sensor\_shell.c
- [GitHub #25784](https://github.com/zephyrproject-rtos/zephyr/issues/25784) - [Coverity CID :210546] Dereference after null check in tests/net/promiscuous/src/main.c
- [GitHub #25783](https://github.com/zephyrproject-rtos/zephyr/issues/25783) - [Coverity CID :210051] Dereference after null check in subsys/net/ip/tcp2.c
- [GitHub #25782](https://github.com/zephyrproject-rtos/zephyr/issues/25782) - [Coverity CID :210035] Dereference before null check in drivers/sensor/bq274xx/bq274xx.c
- [GitHub #25781](https://github.com/zephyrproject-rtos/zephyr/issues/25781) - [Coverity CID :210031] Dereference before null check in drivers/modem/gsm\_ppp.c
- [GitHub #25778](https://github.com/zephyrproject-rtos/zephyr/issues/25778) - [Coverity CID :210604] Out-of-bounds access in tests/kernel/mem\_protect/protection/src/main.c
- [GitHub #25777](https://github.com/zephyrproject-rtos/zephyr/issues/25777) - [Coverity CID :210589] Out-of-bounds access in tests/kernel/mem\_protect/protection/src/main.c
- [GitHub #25776](https://github.com/zephyrproject-rtos/zephyr/issues/25776) - [Coverity CID :210573] Out-of-bounds access in tests/kernel/mem\_protect/userspace/src/main.c
- [GitHub #25750](https://github.com/zephyrproject-rtos/zephyr/issues/25750) - [Coverity CID :210066] Unintentional integer overflow in include/sys/time\_units.h
- [GitHub #25749](https://github.com/zephyrproject-rtos/zephyr/issues/25749) - [Coverity CID :210033] Unintentional integer overflow in drivers/sensor/mpr/mpr.c
- [GitHub #25748](https://github.com/zephyrproject-rtos/zephyr/issues/25748) - [Coverity CID :210606] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #25747](https://github.com/zephyrproject-rtos/zephyr/issues/25747) - [Coverity CID :210596] Assign instead of compare in subsys/logging/log\_output\_syst.c
- [GitHub #25746](https://github.com/zephyrproject-rtos/zephyr/issues/25746) - [Coverity CID :210584] Assign instead of compare in subsys/logging/log\_output\_syst.c
- [GitHub #25745](https://github.com/zephyrproject-rtos/zephyr/issues/25745) - [Coverity CID :210052] Side effect in assertion in tests/kernel/fpu\_sharing/generic/src/pi.c
- [GitHub #25744](https://github.com/zephyrproject-rtos/zephyr/issues/25744) - [Coverity CID :210045] Side effect in assertion in tests/kernel/fpu\_sharing/generic/src/pi.c
- [GitHub #25743](https://github.com/zephyrproject-rtos/zephyr/issues/25743) - [Coverity CID :209944] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #25742](https://github.com/zephyrproject-rtos/zephyr/issues/25742) - [Coverity CID :209943] Pointless string comparison in tests/lib/devicetree/src/main.c
- [GitHub #25741](https://github.com/zephyrproject-rtos/zephyr/issues/25741) - [Coverity CID :210618] Unchecked return value in drivers/wifi/esp/esp.c
- [GitHub #25740](https://github.com/zephyrproject-rtos/zephyr/issues/25740) - [Coverity CID :210617] Argument cannot be negative in tests/net/pm/src/main.c
- [GitHub #25739](https://github.com/zephyrproject-rtos/zephyr/issues/25739) - [Coverity CID :210610] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #25738](https://github.com/zephyrproject-rtos/zephyr/issues/25738) - [Coverity CID :210602] Unchecked return value in tests/drivers/uart/uart\_basic\_api/src/test\_uart\_fifo.c
- [GitHub #25735](https://github.com/zephyrproject-rtos/zephyr/issues/25735) - [Coverity CID :210582] Unchecked return value in tests/net/socket/getaddrinfo/src/main.c
- [GitHub #25734](https://github.com/zephyrproject-rtos/zephyr/issues/25734) - [Coverity CID :210580] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #25733](https://github.com/zephyrproject-rtos/zephyr/issues/25733) - [Coverity CID :210575] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #25732](https://github.com/zephyrproject-rtos/zephyr/issues/25732) - [Coverity CID :210570] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #25729](https://github.com/zephyrproject-rtos/zephyr/issues/25729) - [Coverity CID :210056] Unchecked return value in subsys/net/ip/tcp2.c
- [GitHub #25728](https://github.com/zephyrproject-rtos/zephyr/issues/25728) - [Coverity CID :210050] Unchecked return value in tests/subsys/settings/littlefs/src/settings\_setup\_littlefs.c
- [GitHub #25726](https://github.com/zephyrproject-rtos/zephyr/issues/25726) - [Coverity CID :210598] Missing break in switch in subsys/net/l2/ieee802154/ieee802154\_frame.c
- [GitHub #25725](https://github.com/zephyrproject-rtos/zephyr/issues/25725) - [Coverity CID :210578] Structurally dead code in kernel/mem\_domain.c
- [GitHub #25724](https://github.com/zephyrproject-rtos/zephyr/issues/25724) - [Coverity CID :210566] Missing break in switch in subsys/net/l2/ieee802154/ieee802154\_frame.c
- [GitHub #25723](https://github.com/zephyrproject-rtos/zephyr/issues/25723) - [Coverity CID :210559] Unsigned compared against 0 in subsys/net/ip/tcp2.c
- [GitHub #25722](https://github.com/zephyrproject-rtos/zephyr/issues/25722) - [Coverity CID :210058] Logically dead code in samples/net/sockets/big\_http\_download/src/big\_http\_download.c
- [GitHub #25721](https://github.com/zephyrproject-rtos/zephyr/issues/25721) - [Coverity CID :209945] Logically dead code in tests/net/tcp2/src/main.c
- [GitHub #25720](https://github.com/zephyrproject-rtos/zephyr/issues/25720) - [Coverity CID :210073] Arguments in wrong order in drivers/modem/wncm14a2a.c
- [GitHub #25713](https://github.com/zephyrproject-rtos/zephyr/issues/25713) - Miss shift i2c slave address in i2c\_sifive
- [GitHub #25710](https://github.com/zephyrproject-rtos/zephyr/issues/25710) - FS: Buffer Overflow when enabling Long File Names in FAT\_FS and calling fs\_stat
- [GitHub #25704](https://github.com/zephyrproject-rtos/zephyr/issues/25704) - lib: updatehub: Corrupted updated when receiving CoAP duplicate packages
- [GitHub #25693](https://github.com/zephyrproject-rtos/zephyr/issues/25693) - ESP WiFi MPU Fault causes zephyr fatal error
- [GitHub #25682](https://github.com/zephyrproject-rtos/zephyr/issues/25682) - [v2.2] Shell freezes with cout printf, prink on float
- [GitHub #25678](https://github.com/zephyrproject-rtos/zephyr/issues/25678) - enhance k\_mutex to be ISR safe
- [GitHub #25672](https://github.com/zephyrproject-rtos/zephyr/issues/25672) - Bluetooth: Mesh: scan\_start fails with synchronous bt\_enable
- [GitHub #25664](https://github.com/zephyrproject-rtos/zephyr/issues/25664) - nRF Boards: unify static partition size for Bootloader
- [GitHub #25658](https://github.com/zephyrproject-rtos/zephyr/issues/25658) - Issue to run sample on nucleo\_g474re
- [GitHub #25652](https://github.com/zephyrproject-rtos/zephyr/issues/25652) - smp\_svr fails for nrf5340
- [GitHub #25645](https://github.com/zephyrproject-rtos/zephyr/issues/25645) - USB RNDIS driver can’t work with Windows 10 (10.0.18363)
- [GitHub #25601](https://github.com/zephyrproject-rtos/zephyr/issues/25601) - UART input does not work on mps2\_an{385,521}
- [GitHub #25599](https://github.com/zephyrproject-rtos/zephyr/issues/25599) - scanf() not functional with newlib out of the box
- [GitHub #25566](https://github.com/zephyrproject-rtos/zephyr/issues/25566) - LSPI of NXP i.MX RT Other interrupts treated as transfer completion
- [GitHub #25554](https://github.com/zephyrproject-rtos/zephyr/issues/25554) - lib: posix: nanosleep
- [GitHub #25501](https://github.com/zephyrproject-rtos/zephyr/issues/25501) - shields: mikroe\_eth\_click config should be made conditional
- [GitHub #25499](https://github.com/zephyrproject-rtos/zephyr/issues/25499) - Out of tree board: No sources given to target
- [GitHub #25474](https://github.com/zephyrproject-rtos/zephyr/issues/25474) - ipv6 client-server between ble’s failed
- [GitHub #25458](https://github.com/zephyrproject-rtos/zephyr/issues/25458) - Multiple issues with timing benchmark
- [GitHub #25453](https://github.com/zephyrproject-rtos/zephyr/issues/25453) - tests/posix/common fails on nucleo\_wb55rg
- [GitHub #25444](https://github.com/zephyrproject-rtos/zephyr/issues/25444) - No IPv6 routes from BLE IPSP node (NRF52840DK)
- [GitHub #25398](https://github.com/zephyrproject-rtos/zephyr/issues/25398) - UpSquared Grub build docs don’t work on Ubuntu 20.04
- [GitHub #25358](https://github.com/zephyrproject-rtos/zephyr/issues/25358) - net: config: application starts with 3s delay when CONFIG\_NET\_CONFIG\_SETTINGS=y
- [GitHub #25328](https://github.com/zephyrproject-rtos/zephyr/issues/25328) - mesh\_demo is failing
- [GitHub #25327](https://github.com/zephyrproject-rtos/zephyr/issues/25327) - Move to C99 integer types and deprecate zephyr specific types
- [GitHub #25317](https://github.com/zephyrproject-rtos/zephyr/issues/25317) - RFC: Unstable API Change: uart\_async: Call UART\_RX\_RDY event after rx\_disable()
- [GitHub #25312](https://github.com/zephyrproject-rtos/zephyr/issues/25312) - samples:mimxrt1010\_evk:samples/net/openthread/ncp: build error
- [GitHub #25311](https://github.com/zephyrproject-rtos/zephyr/issues/25311) - samples:frdmkw64f:bluetooth/peripheral\_hr| peripheral\_ht: could not get ADC device
- [GitHub #25308](https://github.com/zephyrproject-rtos/zephyr/issues/25308) - I2C simulation in native\_posix
- [GitHub #25299](https://github.com/zephyrproject-rtos/zephyr/issues/25299) - SYSTICK: Inconsistency between dts status and Kconfig
- [GitHub #25295](https://github.com/zephyrproject-rtos/zephyr/issues/25295) - sanitycheck: race when running sanitycheck on native\_posix producing false negatives.
- [GitHub #25294](https://github.com/zephyrproject-rtos/zephyr/issues/25294) - Nordic mcuboot + smp\_svr + QSPI smp\_shell incompatibility
- [GitHub #25293](https://github.com/zephyrproject-rtos/zephyr/issues/25293) - Add USB Device Support to STM32411E-DISCO
- [GitHub #25283](https://github.com/zephyrproject-rtos/zephyr/issues/25283) - sam0: watchdog: Times out twice as fast as expected
- [GitHub #25268](https://github.com/zephyrproject-rtos/zephyr/issues/25268) - sanitycheck doesn’t report native\_posix failures properly
- [GitHub #25258](https://github.com/zephyrproject-rtos/zephyr/issues/25258) - drivers: i2c\_nios2: device config\_info content mutated
- [GitHub #25257](https://github.com/zephyrproject-rtos/zephyr/issues/25257) - drivers: audio: dma\_nios2\_msgdma: device config\_info content mutated
- [GitHub #25256](https://github.com/zephyrproject-rtos/zephyr/issues/25256) - drivers: audio: tlv320dac310x: device config\_info content mutated
- [GitHub #25255](https://github.com/zephyrproject-rtos/zephyr/issues/25255) - drivers: i2c: gecko: device config\_info content mutated
- [GitHub #25231](https://github.com/zephyrproject-rtos/zephyr/issues/25231) - net.offload test fails on atsame54\_xpro
- [GitHub #25229](https://github.com/zephyrproject-rtos/zephyr/issues/25229) - net.neighbour test fails on atsame54\_xpro
- [GitHub #25228](https://github.com/zephyrproject-rtos/zephyr/issues/25228) - net.util test fails on atsame54\_xpro
- [GitHub #25227](https://github.com/zephyrproject-rtos/zephyr/issues/25227) - net.icmpv6 test fails on atsame54\_xpro
- [GitHub #25226](https://github.com/zephyrproject-rtos/zephyr/issues/25226) - net.vlan test fails on atsame54\_xpro
- [GitHub #25215](https://github.com/zephyrproject-rtos/zephyr/issues/25215) - enable modules to append to $DTS\_ROOT
- [GitHub #25189](https://github.com/zephyrproject-rtos/zephyr/issues/25189) - Wrong flash size set in the XIP boot header for NXP imxrt SoCs
- [GitHub #25171](https://github.com/zephyrproject-rtos/zephyr/issues/25171) - Can only run the flash\_simulator test once on native\_posix
- [GitHub #25165](https://github.com/zephyrproject-rtos/zephyr/issues/25165) - LE Coded Phy code rate switch [s2/s8]
- [GitHub #25156](https://github.com/zephyrproject-rtos/zephyr/issues/25156) - Unable to use –use-elf option in ‘west flash’ to correctly flash the .elf file
- [GitHub #25148](https://github.com/zephyrproject-rtos/zephyr/issues/25148) - tests: gpio: Add check to validate initial values of gpio output
- [GitHub #25140](https://github.com/zephyrproject-rtos/zephyr/issues/25140) - Unable to obtain dhcp lease
- [GitHub #25104](https://github.com/zephyrproject-rtos/zephyr/issues/25104) - whitelist in {sample,testcase}.yaml precludes a test from being run with sanitycheck
- [GitHub #25101](https://github.com/zephyrproject-rtos/zephyr/issues/25101) - driver: gpio: mchp: GPIO initialization value doesn’t get reflected when using new flags
- [GitHub #25098](https://github.com/zephyrproject-rtos/zephyr/issues/25098) - MCUX I2C bus errors leave state machine in busy state
- [GitHub #25076](https://github.com/zephyrproject-rtos/zephyr/issues/25076) - Remove potential I2C deadlock on NRFX implementation
- [GitHub #25063](https://github.com/zephyrproject-rtos/zephyr/issues/25063) - USB Console + USB CDC\_ACM co-existing
- [GitHub #25051](https://github.com/zephyrproject-rtos/zephyr/issues/25051) - tests/drivers/gpio/gpio\_api\_1pin failed on reel\_board.
- [GitHub #25022](https://github.com/zephyrproject-rtos/zephyr/issues/25022) - hsdk:There is no case’s information in serial log for ARC(R) HS Development Kit after one case was been flashed into the board.
- [GitHub #25021](https://github.com/zephyrproject-rtos/zephyr/issues/25021) - Problems getting open62541 to run on Zephyr
- [GitHub #24960](https://github.com/zephyrproject-rtos/zephyr/issues/24960) - The example “blinky” didn’t work on MIMXRT1050-EVK
- [GitHub #24939](https://github.com/zephyrproject-rtos/zephyr/issues/24939) - LSPI of NXP i.MX RT timing delay issue
- [GitHub #24918](https://github.com/zephyrproject-rtos/zephyr/issues/24918) - Segger RTT using j-link doesn’t work on NXP i.MX RT
- [GitHub #24916](https://github.com/zephyrproject-rtos/zephyr/issues/24916) - echo\_client sample return: Cannot connect to TCP remote (IPv6): 60 (frdm\_k64f <–> native\_posix)
- [GitHub #24910](https://github.com/zephyrproject-rtos/zephyr/issues/24910) - kernel: stack sentinel crashes
- [GitHub #24859](https://github.com/zephyrproject-rtos/zephyr/issues/24859) - os: Add memory partition overlap assert check is not made for x86 boards
- [GitHub #24844](https://github.com/zephyrproject-rtos/zephyr/issues/24844) - Setting esp-idf path to match Espressif’s documentation
- [GitHub #24770](https://github.com/zephyrproject-rtos/zephyr/issues/24770) - Low throughput with the zperf sample using stm32f746g\_disco
- [GitHub #24767](https://github.com/zephyrproject-rtos/zephyr/issues/24767) - Ethernet support for STM32H747
- [GitHub #24750](https://github.com/zephyrproject-rtos/zephyr/issues/24750) - need API to get list of succeed initialization device or add initialization status flag in struct device
- [GitHub #24747](https://github.com/zephyrproject-rtos/zephyr/issues/24747) - tests/lib/heap fails on ARC nsim\_sem nsim\_em
- [GitHub #24745](https://github.com/zephyrproject-rtos/zephyr/issues/24745) - Mitigate changes in peripheral enable state after Kconfig replaced by DT status
- [GitHub #24730](https://github.com/zephyrproject-rtos/zephyr/issues/24730) - C standard library <time.h> functions and structures not available when using POSIX API
- [GitHub #24703](https://github.com/zephyrproject-rtos/zephyr/issues/24703) - hal\_nuvoton: Add new module for Nuvoton numicro M480 HAL layer
- [GitHub #24700](https://github.com/zephyrproject-rtos/zephyr/issues/24700) - mimxrt1050\_evk:tests/drivers/kscan/kscan\_api failed.
- [GitHub #24632](https://github.com/zephyrproject-rtos/zephyr/issues/24632) - Devices vs. drivers
- [GitHub #24627](https://github.com/zephyrproject-rtos/zephyr/issues/24627) - tests/subsys/usb/device fails on SAM E54
- [GitHub #24625](https://github.com/zephyrproject-rtos/zephyr/issues/24625) - lib: drivers: clock: rtc: rtc api to maintain calendar time through reboot
- [GitHub #24619](https://github.com/zephyrproject-rtos/zephyr/issues/24619) - CONFIG\_USERSPACE=y CONFIG\_XIP=n causes .bin space to be wasted
- [GitHub #24546](https://github.com/zephyrproject-rtos/zephyr/issues/24546) - Implement MDB runner for ARC
- [GitHub #24499](https://github.com/zephyrproject-rtos/zephyr/issues/24499) - devicetree: node name for SPI buses should be ‘spi’ warning
- [GitHub #24429](https://github.com/zephyrproject-rtos/zephyr/issues/24429) - LPC55S69 flash faults when reading unwritten areas
- [GitHub #24372](https://github.com/zephyrproject-rtos/zephyr/issues/24372) - Json: array of objects is not properly handled
- [GitHub #24318](https://github.com/zephyrproject-rtos/zephyr/issues/24318) - Postpone driver initialization
- [GitHub #24301](https://github.com/zephyrproject-rtos/zephyr/issues/24301) - Support for multi core STM32 H75/H77 boards
- [GitHub #24300](https://github.com/zephyrproject-rtos/zephyr/issues/24300) - tests/net/trickle failed on frdm\_k64f and sam\_e70\_xplained with v1.14 branch.
- [GitHub #24293](https://github.com/zephyrproject-rtos/zephyr/issues/24293) - subsys: shell: bug: shell\_fprintf() before shell\_enable() causes shell deadlock
- [GitHub #24233](https://github.com/zephyrproject-rtos/zephyr/issues/24233) - adxl362\_trigger.c adxl362\_init\_interrupt function :const struct adxl362\_config \*cfg not found gpio\_cs\_port
- [GitHub #24224](https://github.com/zephyrproject-rtos/zephyr/issues/24224) - Possible uninitialized variable in zephyrsubsyslogginglog\_msg.c
- [GitHub #24221](https://github.com/zephyrproject-rtos/zephyr/issues/24221) - Do not run cron workflow on forks
- [GitHub #24217](https://github.com/zephyrproject-rtos/zephyr/issues/24217) - Shell: provide mechanism to call any command while in select command
- [GitHub #24191](https://github.com/zephyrproject-rtos/zephyr/issues/24191) - obj\_tracing: Local IPC variables are not removed from obj tracing list after function return
- [GitHub #24147](https://github.com/zephyrproject-rtos/zephyr/issues/24147) - nrf5340 pdk: BOARDS\_ENABLE\_CPUNET does not allow proper NET MCU configuration
- [GitHub #24134](https://github.com/zephyrproject-rtos/zephyr/issues/24134) - [NXP i.MX RT Flash]: evkmimxrt1020 does not boot with a new flash chip
- [GitHub #24133](https://github.com/zephyrproject-rtos/zephyr/issues/24133) - Question: Context save/restore after deep sleep using device driver
- [GitHub #24111](https://github.com/zephyrproject-rtos/zephyr/issues/24111) - drivers: flash: littlefs: add sync to flash API & update LittleFS to use it
- [GitHub #24092](https://github.com/zephyrproject-rtos/zephyr/issues/24092) - Unable to change recv() buffer size in frdm\_k64f board.
- [GitHub #24076](https://github.com/zephyrproject-rtos/zephyr/issues/24076) - [v1.14] UARTE high current consumption on NRF
- [GitHub #24030](https://github.com/zephyrproject-rtos/zephyr/issues/24030) - [Coverity CID :209379] Unchecked return value in tests/kernel/mem\_protect/sys\_sem/src/main.c
- [GitHub #24029](https://github.com/zephyrproject-rtos/zephyr/issues/24029) - [Coverity CID :209380] Unchecked return value in tests/kernel/poll/src/test\_poll.c
- [GitHub #24028](https://github.com/zephyrproject-rtos/zephyr/issues/24028) - [Coverity CID :209381] Unrecoverable parse warning in include/bluetooth/bluetooth.h
- [GitHub #23961](https://github.com/zephyrproject-rtos/zephyr/issues/23961) - CCC does not get cleared when CONFIG\_BT\_KEYS\_OVERWRITE\_OLDEST is enabled
- [GitHub #23949](https://github.com/zephyrproject-rtos/zephyr/issues/23949) - Question: Is there any example for BR/EDR profile/protocols (like A2DP, AVDTP, RFCOMM)?
- [GitHub #23887](https://github.com/zephyrproject-rtos/zephyr/issues/23887) - drivers: modem: question: Should modem stack include headers to put into zephyr/include?
- [GitHub #23886](https://github.com/zephyrproject-rtos/zephyr/issues/23886) - drivers: modem\_socket: Question: socket ID appears to be the same for all sockets
- [GitHub #23873](https://github.com/zephyrproject-rtos/zephyr/issues/23873) - GNA subsystem does not provide any system calls
- [GitHub #23825](https://github.com/zephyrproject-rtos/zephyr/issues/23825) - edtlib.py fails to find bindings when DTS\_ROOT is a relative path
- [GitHub #23808](https://github.com/zephyrproject-rtos/zephyr/issues/23808) - ARM bus fault with code coverage
- [GitHub #23802](https://github.com/zephyrproject-rtos/zephyr/issues/23802) - up\_squared(acrn):tests/kernel/timer/timer\_api/ failed.
- [GitHub #23801](https://github.com/zephyrproject-rtos/zephyr/issues/23801) - up\_squared(acrn):tests/kernel/sched/schedule\_api failed.
- [GitHub #23800](https://github.com/zephyrproject-rtos/zephyr/issues/23800) - tests/drivers/counter/counter\_cmos failed on up\_squared platform
- [GitHub #23775](https://github.com/zephyrproject-rtos/zephyr/issues/23775) - k\_poll() documentation is wrong or unclear
- [GitHub #23713](https://github.com/zephyrproject-rtos/zephyr/issues/23713) - CMake integration with libmetal errors-out with the bleeding edge CMake release
- [GitHub #23702](https://github.com/zephyrproject-rtos/zephyr/issues/23702) - STACK\_POINTER\_RANDOM is not working on ARM for the main thread
- [GitHub #23672](https://github.com/zephyrproject-rtos/zephyr/issues/23672) - dts: sam0: question: Is it possible to clean up samd.dtsi devicetree warning?
- [GitHub #23629](https://github.com/zephyrproject-rtos/zephyr/issues/23629) - support inverted PWM on STM32
- [GitHub #23599](https://github.com/zephyrproject-rtos/zephyr/issues/23599) - zephyr/samples/application\_development/code\_relocation execution stop at z\_arm\_bus\_fault
- [GitHub #23578](https://github.com/zephyrproject-rtos/zephyr/issues/23578) - [Coverity CID :208922] Uninitialized pointer read in tests/posix/common/src/pthread.c
- [GitHub #23574](https://github.com/zephyrproject-rtos/zephyr/issues/23574) - [Coverity CID :208926] Side effect in assertion in tests/kernel/interrupt/src/nested\_irq.c
- [GitHub #23546](https://github.com/zephyrproject-rtos/zephyr/issues/23546) - Kconfig: default value not assigned when inheriting Kconfig values in range
- [GitHub #23514](https://github.com/zephyrproject-rtos/zephyr/issues/23514) - Allocate executable memory for ESP32
- [GitHub #23474](https://github.com/zephyrproject-rtos/zephyr/issues/23474) - tests/subsys/usb/device failed on reel\_board.
- [GitHub #23443](https://github.com/zephyrproject-rtos/zephyr/issues/23443) - esp32 needs i2c\_transfer call to turn on the display
- [GitHub #23423](https://github.com/zephyrproject-rtos/zephyr/issues/23423) - Mitigation in case system [created] threads hang/non-responsive
- [GitHub #23419](https://github.com/zephyrproject-rtos/zephyr/issues/23419) - posix: clock: No thread safety clock\_[get/set]time
- [GitHub #23366](https://github.com/zephyrproject-rtos/zephyr/issues/23366) - ARM: Core Stack Improvements/Bug fixes for 2.3 release
- [GitHub #23364](https://github.com/zephyrproject-rtos/zephyr/issues/23364) - Bluetooth: bt\_recv deadlock on supervision timeout with pending GATT Write Commands
- [GitHub #23349](https://github.com/zephyrproject-rtos/zephyr/issues/23349) - Question: How to add external soc, board, DTS, drivers and libs?
- [GitHub #23322](https://github.com/zephyrproject-rtos/zephyr/issues/23322) - flash, spi-nor: Configuration of jedec spi nor flash device driver
- [GitHub #23319](https://github.com/zephyrproject-rtos/zephyr/issues/23319) - hci interface stopped working after few hours/days
- [GitHub #23248](https://github.com/zephyrproject-rtos/zephyr/issues/23248) - Add secure version of strcpy
- [GitHub #23246](https://github.com/zephyrproject-rtos/zephyr/issues/23246) - net: tx\_bufs are not freed when NET\_TCP\_BACKLOG\_SIZE is too high
- [GitHub #23243](https://github.com/zephyrproject-rtos/zephyr/issues/23243) - test/kernel/gen\_isr\_table fails in v2.2.0-rc3 on lpcxpresso54114\_m4 board
- [GitHub #23215](https://github.com/zephyrproject-rtos/zephyr/issues/23215) - fujitsu FRAM read error on stm32\_olimexino
- [GitHub #23211](https://github.com/zephyrproject-rtos/zephyr/issues/23211) - need a proper arch\_system\_halt() for x86\_64
- [GitHub #23178](https://github.com/zephyrproject-rtos/zephyr/issues/23178) - usb: endpoint buffer leak upon SET\_CONFIGURATION, SET\_INTERFACE
- [GitHub #23177](https://github.com/zephyrproject-rtos/zephyr/issues/23177) - Bluetooth: Mesh: Access structure member with a possible NULL pointer
- [GitHub #23149](https://github.com/zephyrproject-rtos/zephyr/issues/23149) - [v1.14] sam\_e70\_xplained:tests/drivers/watchdog/wdt\_basic\_api failed with v1.14 branch.
- [GitHub #23139](https://github.com/zephyrproject-rtos/zephyr/issues/23139) - USB Mass storage - Unexpected USB restart from host
- [GitHub #23138](https://github.com/zephyrproject-rtos/zephyr/issues/23138) - Codegen for an C structure that stores pinmux definitions
- [GitHub #23134](https://github.com/zephyrproject-rtos/zephyr/issues/23134) - BT: Host: Notification dropped instead of truncated if bigger than ATT\_MTU-3
- [GitHub #23111](https://github.com/zephyrproject-rtos/zephyr/issues/23111) - drivers:usb:device:sam0: Descriptor tables are filled with zeros in attach()
- [GitHub #23052](https://github.com/zephyrproject-rtos/zephyr/issues/23052) - nrf52840\_pca10056: Spurious RTS pulse and incorrect line level with hardware flow control disabled
- [GitHub #23040](https://github.com/zephyrproject-rtos/zephyr/issues/23040) - samples: net/wifi: net ping shell causes USAGE FAULT once wifi is connected
- [GitHub #23039](https://github.com/zephyrproject-rtos/zephyr/issues/23039) - SystemView does not work with C++ enabled
- [GitHub #22996](https://github.com/zephyrproject-rtos/zephyr/issues/22996) - scripts/footprint/size\_report doesn’t work on qemu\_x86\_64
- [GitHub #22980](https://github.com/zephyrproject-rtos/zephyr/issues/22980) - bluetooth: logging: Build assertion prevents immediate logging when using legacy LL
- [GitHub #22975](https://github.com/zephyrproject-rtos/zephyr/issues/22975) - tests/kernel/gen\_isr\_table: filtered in CI only for Cortex-M Mainline
- [GitHub #22974](https://github.com/zephyrproject-rtos/zephyr/issues/22974) - Add cancel function to onoff service
- [GitHub #22955](https://github.com/zephyrproject-rtos/zephyr/issues/22955) - tests/kernel/interrupt fails intermittently on qemu\_cortex\_m0
- [GitHub #22906](https://github.com/zephyrproject-rtos/zephyr/issues/22906) - Slow read/write speed of microSD card via SPI and FatFS
- [GitHub #22892](https://github.com/zephyrproject-rtos/zephyr/issues/22892) - Kconfig warning when serial disable on PCA10059
- [GitHub #22873](https://github.com/zephyrproject-rtos/zephyr/issues/22873) - Bluetooth: RSSI Read command can be configured out even when mandatory
- [GitHub #22872](https://github.com/zephyrproject-rtos/zephyr/issues/22872) - Hello world application for mps2\_an521 board when build as a secure/non-secure with Trusted Firmware is crashing on qemu
- [GitHub #22865](https://github.com/zephyrproject-rtos/zephyr/issues/22865) - drivers: enc28j60: sample: dumb\_http\_server: TX failed errors
- [GitHub #22758](https://github.com/zephyrproject-rtos/zephyr/issues/22758) - RFC: Require system clock stability on startup
- [GitHub #22751](https://github.com/zephyrproject-rtos/zephyr/issues/22751) - STM32F407 I2C driver hangs
- [GitHub #22722](https://github.com/zephyrproject-rtos/zephyr/issues/22722) - posix: redefinition of symbols while porting zeromq to zephyr
- [GitHub #22704](https://github.com/zephyrproject-rtos/zephyr/issues/22704) - Implement watchdog driver for lpcxpresso55s69
- [GitHub #22637](https://github.com/zephyrproject-rtos/zephyr/issues/22637) - 2.3 Release Checklist
- [GitHub #22594](https://github.com/zephyrproject-rtos/zephyr/issues/22594) - NXP S32K144 MCU support
- [GitHub #22562](https://github.com/zephyrproject-rtos/zephyr/issues/22562) - West: Allow configuring `west sign` similar to west runners
- [GitHub #22466](https://github.com/zephyrproject-rtos/zephyr/issues/22466) - Add hx711 sensor
- [GitHub #22391](https://github.com/zephyrproject-rtos/zephyr/issues/22391) - Resuming from suspend should check device usage count in device idle PM
- [GitHub #22344](https://github.com/zephyrproject-rtos/zephyr/issues/22344) - convert espi sample to devicetree
- [GitHub #22340](https://github.com/zephyrproject-rtos/zephyr/issues/22340) - Security problem with settings and littlefs
- [GitHub #22322](https://github.com/zephyrproject-rtos/zephyr/issues/22322) - Clang linking error
- [GitHub #22301](https://github.com/zephyrproject-rtos/zephyr/issues/22301) - k\_msgq\_put() semantics definition
- [GitHub #22151](https://github.com/zephyrproject-rtos/zephyr/issues/22151) - hal\_nordic: nrfx: doxygen: Reference to missing nrfx/templates
- [GitHub #22145](https://github.com/zephyrproject-rtos/zephyr/issues/22145) - RISCV arch\_irq\_connect\_dynamic() broken with PLIC interrupts
- [GitHub #22144](https://github.com/zephyrproject-rtos/zephyr/issues/22144) - arch: arm64: interrupt test is failing
- [GitHub #22140](https://github.com/zephyrproject-rtos/zephyr/issues/22140) - Exiting deep sleep without button help; nrf52832
- [GitHub #22091](https://github.com/zephyrproject-rtos/zephyr/issues/22091) - Blink-Led example doesn’t build on Nucleo\_L476RG, STM32F4\_DISCOVERY, Nucleo\_F302R8, Nucleo\_F401RE
- [GitHub #22077](https://github.com/zephyrproject-rtos/zephyr/issues/22077) - W25Q32fv supported in spi\_flash examples ?
- [GitHub #22063](https://github.com/zephyrproject-rtos/zephyr/issues/22063) - fs/NVS: NVS is not compatible with flash memories which have 0x00 as erased
- [GitHub #22060](https://github.com/zephyrproject-rtos/zephyr/issues/22060) - Build fails with gcc-arm-none-eabi-9-2019-q4-major
- [GitHub #21994](https://github.com/zephyrproject-rtos/zephyr/issues/21994) - Bluetooth: controller: split: Fix procedure complete event generation
- [GitHub #21848](https://github.com/zephyrproject-rtos/zephyr/issues/21848) - sanitycheck duplicate tests Testing/Ztest
- [GitHub #21843](https://github.com/zephyrproject-rtos/zephyr/issues/21843) - CONFIG\_INIT\_STACKS issue on x86\_64
- [GitHub #21819](https://github.com/zephyrproject-rtos/zephyr/issues/21819) - Shell fails when dynamic command has empty subcommand
- [GitHub #21801](https://github.com/zephyrproject-rtos/zephyr/issues/21801) - Logger sample’s performance estimates are incorrect
- [GitHub #21798](https://github.com/zephyrproject-rtos/zephyr/issues/21798) - Bluetooth: host: Allow GATT client to restore subscription info without resubscribing
- [GitHub #21772](https://github.com/zephyrproject-rtos/zephyr/issues/21772) - Adding I2C devices to device tree with the same address on different busses generates excessive warnings.
- [GitHub #21762](https://github.com/zephyrproject-rtos/zephyr/issues/21762) - [v1.14] stm32: k\_sleep() actual sleep times are different than its input
- [GitHub #21754](https://github.com/zephyrproject-rtos/zephyr/issues/21754) - Arduino Due shell does not accept input (UART0)
- [GitHub #21725](https://github.com/zephyrproject-rtos/zephyr/issues/21725) - device power management by device
- [GitHub #21711](https://github.com/zephyrproject-rtos/zephyr/issues/21711) - sam0 i2c slave
- [GitHub #21708](https://github.com/zephyrproject-rtos/zephyr/issues/21708) - Multiple partitions for LittleFS
- [GitHub #21707](https://github.com/zephyrproject-rtos/zephyr/issues/21707) - Timing violation for all sensor drivers
- [GitHub #21670](https://github.com/zephyrproject-rtos/zephyr/issues/21670) - Keep device structures in ROM
- [GitHub #21635](https://github.com/zephyrproject-rtos/zephyr/issues/21635) - sht3xd error -5 on olimexino\_stm32
- [GitHub #21616](https://github.com/zephyrproject-rtos/zephyr/issues/21616) - LWM2M: unable to get plain text from incoming message
- [GitHub #21611](https://github.com/zephyrproject-rtos/zephyr/issues/21611) - IS25LP032D-JNLE Flash support
- [GitHub #21554](https://github.com/zephyrproject-rtos/zephyr/issues/21554) - ldscript:datas section is not properly aligned in ROM
- [GitHub #21549](https://github.com/zephyrproject-rtos/zephyr/issues/21549) - i2c\_sam0 interrupt latency is excessive
- [GitHub #21511](https://github.com/zephyrproject-rtos/zephyr/issues/21511) - re-visit k\_thread\_abort wrt SMP
- [GitHub #21498](https://github.com/zephyrproject-rtos/zephyr/issues/21498) - Zephyr Peripheral not responding to Terminate command from central
- [GitHub #21455](https://github.com/zephyrproject-rtos/zephyr/issues/21455) - driver: subsys: sdhc: USAGE FAULT trace and no cs control
- [GitHub #21452](https://github.com/zephyrproject-rtos/zephyr/issues/21452) - drivers: ethernet: unify the initiaization
- [GitHub #21445](https://github.com/zephyrproject-rtos/zephyr/issues/21445) - drivers/i2c: add I2C slave support for nrfx
- [GitHub #21436](https://github.com/zephyrproject-rtos/zephyr/issues/21436) - refactor and augment CPU cache management APIs
- [GitHub #21399](https://github.com/zephyrproject-rtos/zephyr/issues/21399) - NUCLEO-H745ZI-Q Support
- [GitHub #21378](https://github.com/zephyrproject-rtos/zephyr/issues/21378) - The program cannot be downloaded to nrf52840, only to pca10056
- [GitHub #21240](https://github.com/zephyrproject-rtos/zephyr/issues/21240) - Error west flash
- [GitHub #21234](https://github.com/zephyrproject-rtos/zephyr/issues/21234) - drivers: usb\_dc\_sam0: usb detach and reattach does not work
- [GitHub #21233](https://github.com/zephyrproject-rtos/zephyr/issues/21233) - i2c\_sam0 driver does not execute a STOP condition
- [GitHub #21232](https://github.com/zephyrproject-rtos/zephyr/issues/21232) - i2c\_sam0 LOWTOUT is not functional
- [GitHub #21229](https://github.com/zephyrproject-rtos/zephyr/issues/21229) - cc1plus: warning: ‘-Werror=’ argument ‘-Werror=implicit-int’ is not valid for C++
- [GitHub #21187](https://github.com/zephyrproject-rtos/zephyr/issues/21187) - Can not ping or run http server via ethernet when gPTP is enabled
- [GitHub #21114](https://github.com/zephyrproject-rtos/zephyr/issues/21114) - Invalid interaction between the RTC and the I2C drivers for the sam0
- [GitHub #21111](https://github.com/zephyrproject-rtos/zephyr/issues/21111) - Reschedule points are currently undocumented
- [GitHub #21092](https://github.com/zephyrproject-rtos/zephyr/issues/21092) - i2c-sam0 sleeps waiting for interrupt
- [GitHub #21053](https://github.com/zephyrproject-rtos/zephyr/issues/21053) - net: 6lo: Use context 0 as default when CID-bit is not set
- [GitHub #21016](https://github.com/zephyrproject-rtos/zephyr/issues/21016) - Unexpected ethernet network traffic after power up
- [GitHub #20987](https://github.com/zephyrproject-rtos/zephyr/issues/20987) - Console showing frequent usb warnings: <wrn> usb\_device: Failed to write endpoint buffer 0x82
- [GitHub #20978](https://github.com/zephyrproject-rtos/zephyr/issues/20978) - Add bond\_deleted callback
- [GitHub #20870](https://github.com/zephyrproject-rtos/zephyr/issues/20870) - [Coverity CID :205816] Control flow issues in subsys/settings/src/settings\_file.c
- [GitHub #20844](https://github.com/zephyrproject-rtos/zephyr/issues/20844) - [Coverity CID :205781] Integer handling issues in lib/os/printk.c
- [GitHub #20806](https://github.com/zephyrproject-rtos/zephyr/issues/20806) - nrf: clock control: clock control on/off routines are refcounted
- [GitHub #20780](https://github.com/zephyrproject-rtos/zephyr/issues/20780) - Feature Request: Half-duplex UART shell backend
- [GitHub #20750](https://github.com/zephyrproject-rtos/zephyr/issues/20750) - shell: shell\_execute\_cmd introduce new line
- [GitHub #20734](https://github.com/zephyrproject-rtos/zephyr/issues/20734) - Are cooperative threads cooperative in SMP?
- [GitHub #20729](https://github.com/zephyrproject-rtos/zephyr/issues/20729) - Coverage reporting hangs for C++ tests on X86 qemu
- [GitHub #20712](https://github.com/zephyrproject-rtos/zephyr/issues/20712) - nRF clock\_control\_on() is nonblocking
- [GitHub #20693](https://github.com/zephyrproject-rtos/zephyr/issues/20693) - tests: watchdog: test\_wdt\_callback\_1() implementation vs API specification
- [GitHub #20687](https://github.com/zephyrproject-rtos/zephyr/issues/20687) - Clarification: How to enable on-board nor-flash following the board porting guide?
- [GitHub #20671](https://github.com/zephyrproject-rtos/zephyr/issues/20671) - ARC: remove scheduler code from arch layer
- [GitHub #20663](https://github.com/zephyrproject-rtos/zephyr/issues/20663) - kernel objects are being included always, regardless of usage
- [GitHub #20595](https://github.com/zephyrproject-rtos/zephyr/issues/20595) - tests/arch/arm/arm\_thread\_swap failed on frdm\_k64f board.
- [GitHub #20589](https://github.com/zephyrproject-rtos/zephyr/issues/20589) - RV32M1 SPI loopback needs DEBUG\_OPTIMIZATIONS
- [GitHub #20541](https://github.com/zephyrproject-rtos/zephyr/issues/20541) - [Coverity CID :205639]Security best practices violations in /tests/subsys/settings/functional/src/settings\_basic\_test.c
- [GitHub #20520](https://github.com/zephyrproject-rtos/zephyr/issues/20520) - [Coverity CID :205652]Memory - corruptions in /tests/crypto/tinycrypt/src/ecc\_dsa.c
- [GitHub #20519](https://github.com/zephyrproject-rtos/zephyr/issues/20519) - [Coverity CID :205616]Memory - corruptions in /tests/crypto/tinycrypt/src/ecc\_dsa.c
- [GitHub #20517](https://github.com/zephyrproject-rtos/zephyr/issues/20517) - [Coverity CID :205640]Control flow issues in /subsys/testsuite/ztest/src/ztest.c
- [GitHub #20516](https://github.com/zephyrproject-rtos/zephyr/issues/20516) - [Coverity CID :205609]Control flow issues in /subsys/testsuite/ztest/src/ztest.c
- [GitHub #20500](https://github.com/zephyrproject-rtos/zephyr/issues/20500) - [Coverity CID :205629]Control flow issues in /drivers/timer/cc13x2\_cc26x2\_rtc\_timer.c
- [GitHub #20418](https://github.com/zephyrproject-rtos/zephyr/issues/20418) - CONFIG\_HEAP\_MEM\_POOL\_SIZE should not be limited
- [GitHub #20297](https://github.com/zephyrproject-rtos/zephyr/issues/20297) - Bluetooth: can’t close bt\_driver log output
- [GitHub #20012](https://github.com/zephyrproject-rtos/zephyr/issues/20012) - Support peripheral deallocation at runtime
- [GitHub #19824](https://github.com/zephyrproject-rtos/zephyr/issues/19824) - Build sample net app for ACRN (nuc i7dnhe)
- [GitHub #19739](https://github.com/zephyrproject-rtos/zephyr/issues/19739) - stty: standard input: Inappropriate ioctl for device
- [GitHub #19701](https://github.com/zephyrproject-rtos/zephyr/issues/19701) - mem\_pool\_threadsafe sporadic failures impacting CI
- [GitHub #19684](https://github.com/zephyrproject-rtos/zephyr/issues/19684) - doc: [message\_queues.rst] unclear about data\_item structure type
- [GitHub #19670](https://github.com/zephyrproject-rtos/zephyr/issues/19670) - samples/drivers/spi\_fujitsu\_fram crashs due to uninitialized variables
- [GitHub #19661](https://github.com/zephyrproject-rtos/zephyr/issues/19661) - missing files in xtensa/xt-sim doc
- [GitHub #19550](https://github.com/zephyrproject-rtos/zephyr/issues/19550) - drivers/pcie: `pcie_get_mbar()` should return a `void *` not `u32_t`
- [GitHub #19483](https://github.com/zephyrproject-rtos/zephyr/issues/19483) - Add support for Open Supervised Device Protocol (OSDP)
- [GitHub #19414](https://github.com/zephyrproject-rtos/zephyr/issues/19414) - UART and prf not working
- [GitHub #19376](https://github.com/zephyrproject-rtos/zephyr/issues/19376) - Build on a ARM host
- [GitHub #19348](https://github.com/zephyrproject-rtos/zephyr/issues/19348) - net: TCP/IPv6 set of fragmented packets causes Zephyr QEMU to double free
- [GitHub #19063](https://github.com/zephyrproject-rtos/zephyr/issues/19063) - can we increase qemu\_riscv32/64 RAM sizes
- [GitHub #18960](https://github.com/zephyrproject-rtos/zephyr/issues/18960) - [Coverity CID :203908]Error handling issues in /lib/libc/newlib/libc-hooks.c
- [GitHub #18843](https://github.com/zephyrproject-rtos/zephyr/issues/18843) - Usage Fault with CONFIG\_NO\_OPTIMIZATIONS even on samples/hello\_world
- [GitHub #18815](https://github.com/zephyrproject-rtos/zephyr/issues/18815) - UART API documentation
- [GitHub #18629](https://github.com/zephyrproject-rtos/zephyr/issues/18629) - Some tests fail to reach test\_main() on cc1352r1\_launchxl
- [GitHub #18570](https://github.com/zephyrproject-rtos/zephyr/issues/18570) - Dynamic interrupt does not work with multi-level interrupts
- [GitHub #18345](https://github.com/zephyrproject-rtos/zephyr/issues/18345) - Is there a way to get the bytes that shell receives?
- [GitHub #18157](https://github.com/zephyrproject-rtos/zephyr/issues/18157) - adding an offset to the zephyr code via dts overlay breaks linking + the image size changes
- [GitHub #18045](https://github.com/zephyrproject-rtos/zephyr/issues/18045) - BT Host: Advertising Extensions - Periodic Advertisement
- [GitHub #17814](https://github.com/zephyrproject-rtos/zephyr/issues/17814) - Zephyr support for NXP i.MX8M SoC
- [GitHub #17688](https://github.com/zephyrproject-rtos/zephyr/issues/17688) - Unable to Read data from SCC811
- [GitHub #17624](https://github.com/zephyrproject-rtos/zephyr/issues/17624) - SRAM size configurations aren’t always consistent
- [GitHub #17372](https://github.com/zephyrproject-rtos/zephyr/issues/17372) - sanitycheck does not parse extra\_args with spaces correctly
- [GitHub #16968](https://github.com/zephyrproject-rtos/zephyr/issues/16968) - silabs/gecko/emlib/src/em\_gpio.c:111:35: warning: ?: using integer constants in boolean context [-Werror=int-in-bool-context]
- [GitHub #16886](https://github.com/zephyrproject-rtos/zephyr/issues/16886) - Bluetooth Mesh: Receive segmented message multiple times
- [GitHub #16809](https://github.com/zephyrproject-rtos/zephyr/issues/16809) - TCP2 integration
- [GitHub #16790](https://github.com/zephyrproject-rtos/zephyr/issues/16790) - adxl362 sample isn’t build by sanitycheck
- [GitHub #16661](https://github.com/zephyrproject-rtos/zephyr/issues/16661) - Symmetric multiprocessing (SMP) for ARC HS cores
- [GitHub #16638](https://github.com/zephyrproject-rtos/zephyr/issues/16638) - Filesystem API is missing fs\_open() flags
- [GitHub #16439](https://github.com/zephyrproject-rtos/zephyr/issues/16439) - flash: unify read alignment requirements
- [GitHub #16387](https://github.com/zephyrproject-rtos/zephyr/issues/16387) - STM32wb55 bluetooth samples fail
- [GitHub #16363](https://github.com/zephyrproject-rtos/zephyr/issues/16363) - Error building x\_nucleo\_iks01a1 sample on nucleo\_wb55rg after activating I2C Bus
- [GitHub #16210](https://github.com/zephyrproject-rtos/zephyr/issues/16210) - ARM: initialization sequence might be not using all of interrupt stack
- [GitHub #16031](https://github.com/zephyrproject-rtos/zephyr/issues/16031) - Toolchain abstraction
- [GitHub #15968](https://github.com/zephyrproject-rtos/zephyr/issues/15968) - rom\_report very imprecise
- [GitHub #15845](https://github.com/zephyrproject-rtos/zephyr/issues/15845) - \_RESET\_VECTOR different from 0x00 gives invalid .elf size on nios2
- [GitHub #15286](https://github.com/zephyrproject-rtos/zephyr/issues/15286) - HF clock’s m16src\_grd and BLE stack
- [GitHub #15246](https://github.com/zephyrproject-rtos/zephyr/issues/15246) - doc: confusion about dtc version
- [GitHub #14591](https://github.com/zephyrproject-rtos/zephyr/issues/14591) - Infineon Tricore architecture support
- [GitHub #14587](https://github.com/zephyrproject-rtos/zephyr/issues/14587) - IPv6 support in cc3220sf\_launchxl
- [GitHub #14520](https://github.com/zephyrproject-rtos/zephyr/issues/14520) - invalid locking in shell
- [GitHub #14302](https://github.com/zephyrproject-rtos/zephyr/issues/14302) - USB MSC fails USB3CV tests
- [GitHub #14269](https://github.com/zephyrproject-rtos/zephyr/issues/14269) - Enforce usage of K\_THREAD\_STACK\_SIZEOF macro in k\_thread\_create()
- [GitHub #14173](https://github.com/zephyrproject-rtos/zephyr/issues/14173) - Configure QEMU to run independent of the host clock
- [GitHub #13819](https://github.com/zephyrproject-rtos/zephyr/issues/13819) - mimxrt10xx: Wrong I2C transfer status
- [GitHub #13813](https://github.com/zephyrproject-rtos/zephyr/issues/13813) - Test suite mslab\_threadsafe fails randomly
- [GitHub #13737](https://github.com/zephyrproject-rtos/zephyr/issues/13737) - Where can I find tutorial to make my own device driver for a device under I2C bus?
- [GitHub #13651](https://github.com/zephyrproject-rtos/zephyr/issues/13651) - ARC does not set thread->stack\_info correctly
- [GitHub #13637](https://github.com/zephyrproject-rtos/zephyr/issues/13637) - Introduce supervisor-only stack declaration macros
- [GitHub #13276](https://github.com/zephyrproject-rtos/zephyr/issues/13276) - Do we need to update fatfs
- [GitHub #12987](https://github.com/zephyrproject-rtos/zephyr/issues/12987) - Fix workaround of using ‘mmio-sram’ compat for system memory (DRAM) in DTS
- [GitHub #12935](https://github.com/zephyrproject-rtos/zephyr/issues/12935) - Zephyr usurps “STRINGIFY” define
- [GitHub #12705](https://github.com/zephyrproject-rtos/zephyr/issues/12705) - Implement select() call for socket offloading and SimpleLink driver
- [GitHub #12025](https://github.com/zephyrproject-rtos/zephyr/issues/12025) - OS Pwr Manager doesn’t put nrf52 into LPS\_1
- [GitHub #11976](https://github.com/zephyrproject-rtos/zephyr/issues/11976) - APIs that support a callback should provide both the device pointer and a generic pointer
- [GitHub #11974](https://github.com/zephyrproject-rtos/zephyr/issues/11974) - rework eeprom driver to clearly indicate it is a test stub
- [GitHub #11908](https://github.com/zephyrproject-rtos/zephyr/issues/11908) - Power Manager does not handle K\_FOREVER properly
- [GitHub #11890](https://github.com/zephyrproject-rtos/zephyr/issues/11890) - Reimplement getaddrinfo() to call SlNetUtil\_getaddrinfo() in new SimpleLink SDK v 2.30+
- [GitHub #10628](https://github.com/zephyrproject-rtos/zephyr/issues/10628) - tests/kernel/common and tests/posix/fs crash on ESP32
- [GitHub #10436](https://github.com/zephyrproject-rtos/zephyr/issues/10436) - Mess with ssize\_t, off\_t definitions
- [GitHub #9893](https://github.com/zephyrproject-rtos/zephyr/issues/9893) - MISRA C Review switch statement usage
- [GitHub #9808](https://github.com/zephyrproject-rtos/zephyr/issues/9808) - remove single thread support
- [GitHub #9596](https://github.com/zephyrproject-rtos/zephyr/issues/9596) - tests/subsys/logging/log\_core fails on ESP32 with no console output
- [GitHub #8469](https://github.com/zephyrproject-rtos/zephyr/issues/8469) - Zephyr types incompatibilities (e.g. u32\_t vs uint32\_t)
- [GitHub #8364](https://github.com/zephyrproject-rtos/zephyr/issues/8364) - mcumgr: unable to properly read big files
- [GitHub #8360](https://github.com/zephyrproject-rtos/zephyr/issues/8360) - CI should enforce that extract\_dts\_includes.py does not trigger warnings
- [GitHub #8262](https://github.com/zephyrproject-rtos/zephyr/issues/8262) - [Bluetooth] MPU FAULT on sdu\_recv
- [GitHub #8257](https://github.com/zephyrproject-rtos/zephyr/issues/8257) - Unify TICKLESS\_IDLE & TICKLESS\_KERNEL
- [GitHub #7951](https://github.com/zephyrproject-rtos/zephyr/issues/7951) - doc: naming convention for requirements ids
- [GitHub #7385](https://github.com/zephyrproject-rtos/zephyr/issues/7385) - i2c\_esp32 can write past checked buffer length
- [GitHub #6783](https://github.com/zephyrproject-rtos/zephyr/issues/6783) - Clean up wiki.zephyrproject.org content
- [GitHub #6184](https://github.com/zephyrproject-rtos/zephyr/issues/6184) - drivers: ISR-friendly driver APIs
- [GitHub #5934](https://github.com/zephyrproject-rtos/zephyr/issues/5934) - esp32: Output frequency is different from that configured on I2C and PWM drivers
- [GitHub #5443](https://github.com/zephyrproject-rtos/zephyr/issues/5443) - Deprecate # CONFIG`\_ is not set
- [GitHub #4404](https://github.com/zephyrproject-rtos/zephyr/issues/4404) - Align k\_poll with waiters
- [GitHub #3423](https://github.com/zephyrproject-rtos/zephyr/issues/3423) - Optimize MCUX shim drivers to reduce memory footprint
- [GitHub #3180](https://github.com/zephyrproject-rtos/zephyr/issues/3180) - implement direct interrupts on ARC
- [GitHub #3165](https://github.com/zephyrproject-rtos/zephyr/issues/3165) - xtensa: switch to clang-based frontend
- [GitHub #3066](https://github.com/zephyrproject-rtos/zephyr/issues/3066) - Improve Multi Core support
- [GitHub #2955](https://github.com/zephyrproject-rtos/zephyr/issues/2955) - Use interrupt-driven TX in hci\_uart sample
