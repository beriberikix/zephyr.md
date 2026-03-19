---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/release-notes-2.7.html
original_path: releases/release-notes-2.7.html
---

# Zephyr 2.7.0

We are pleased to announce the release of Zephyr RTOS version 2.7.0 (LTS2).

Major enhancements since v2.6.0 include:

- Bluetooth Audio, Direction Finding, and Mesh improvements
- Support for Bluetooth Advertisement PDU Chaining
- Added support for armclang / armlinker toolchain
- Added support for MWDT C / C++ toolchain
- Update to CMSIS v5.8.0 (Core v5.5.0, DSP v1.9.0)
- Support for M-Profile Vector Extensions (MVE) on ARMv8.1-M
- Improved thread safety for Newlib and C++ on SMP-capable systems
- IEEE 802.15.4 Software Address Filtering
- New Action-based Power Management API
- USB Device Framework now includes all Chapter 9 defines and structures
- Generic System Controller (`syscon`) driver and emulator
- Linker Support for Tightly-Coupled Memory in RISC-V
- Additional Blocking API calls for LoRa
- Support for extended PCI / PCIe capabilities, improved MIS-X support
- Added Support for Service Type Enumeration (STE) with mDNS / DNS Service Discovery
- Added Zephyr Thread Awareness for OpenOCD to West
- EEPROM now can be emulated in flash
- Added both Ethernet MDIO and Ethernet generic PHY drivers

Additional Major enhancements since v1.14.0 (LTS1) include:

- The kernel now supports both 32- and 64-bit architectures
- We added support for SOCKS5 proxy
- Introduced support for 6LoCAN, a 6Lo adaption layer for Controller Area Networks
- We added support for Point-to-Point Protocol (PPP)
- We added support for UpdateHub, an end-to-end solution for over-the-air device updates
- We added support for ARM Cortex-R Architecture
- Normalized APIs across all architectures
- Expanded support for ARMv6-M architecture
- Added support for numerous new boards and shields
- Added numerous new drivers and sensors
- Added BLE support on Vega platform
- Memory size improvements to Bluetooth host stack
- We added initial support for 64-bit ARMv8-A architecture
- CANopen protocol support through 3rd party CANopenNode stack
- LoRa support was added along with the SX1276 LoRa modem driver
- A new Zephyr CMake package has been introduced
- A new Devicetree API which provides access to virtually all DT nodes and properties
- The kernel timeout API has been overhauled
- A new k\_heap/sys\_heap allocator, with improved performance
- Zephyr now integrates with the TF-M (Trusted Firmware M) PSA-compliant framework
- The Bluetooth Low Energy Host now supports LE Advertising Extensions
- The CMSIS-DSP library is now included and integrated
- Introduced initial support for virtual memory management
- Added Bluetooth host support for periodic advertisement and isochronous channels.
- Added a new TCP stack which improves network protocol testability
- Introduced a new toolchain abstraction with initial support for GCC and LLVM/Clang
- Moved to using C99 integer types and deprecate Zephyr integer types
- Introduced support for the SPARC architecture and the LEON implementation
- Added Thread Local Storage (TLS) support
- Added support for per thread runtime statistics
- Added support for building with LLVM on X86
- Added new synchronization mechanisms using Condition Variables
- Add support for demand paging, initial support on X86
- Logging subsystem overhauled
- Added support for 64-bit ARCv3
- Split ARM32 and ARM64, ARM64 is now a top-level architecture
- Added initial support for Arm v8.1-m and Cortex-M55
- Removed legacy TCP stack support which was deprecated in 2.4
- Tracing subsystem overhaul / added support for Percepio Tracealyzer
- Device runtime power management (PM) completely overhauled
- Automatic SPDX SBOM generation has been added to West
- Added an example standalone Zephyr application

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

- CVE-2021-3510: [Zephyr project bug tracker GHSA-289f-7mw3-2qf4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-289f-7mw3-2qf4).

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## API Changes

Deprecated in this release

- `DT_ENUM_TOKEN` and `DT_ENUM_UPPER_TOKEN`,
  were deprecated in favor of utilizing
  [`DT_STRING_TOKEN`](../doxygen/html/group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54) and [`DT_STRING_UPPER_TOKEN`](../doxygen/html/group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)
- `BT_CONN_ROLE_MASTER` and `BT_CONN_ROLE_SLAVE`
  have been deprecated in favor of
  `BT_CONN_ROLE_CENTRAL` and `BT_CONN_ROLE_PERIPHERAL`
- [`BT_LE_SCAN_OPT_FILTER_WHITELIST`](../doxygen/html/group__bt__gap.md#ga33e84f4ccbf4d0aa2527e9fe1086e252)
  has been deprecated in favor of
  `BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST`
- The following whitelist functions have been deprecated:
  `bt_le_whitelist_add()`
  `bt_le_whitelist_rem()`
  `bt_le_whitelist_clear()`
  in favor of
  [`bt_le_filter_accept_list_add()`](../doxygen/html/group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)
  [`bt_le_filter_accept_list_remove()`](../doxygen/html/group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)
  [`bt_le_filter_accept_list_clear()`](../doxygen/html/group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)

Modified in this release

- The following Bluetooth macros and structures in `hci.h` have been
  modified to align with the inclusive naming in the v5.3 specification:

  - `BT_LE_FEAT_BIT_SLAVE_FEAT_REQ` is now `BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG`
  - `BT_LE_FEAT_BIT_CIS_MASTER` is now `BT_LE_FEAT_BIT_CIS_CENTRAL`
  - `BT_LE_FEAT_BIT_CIS_SLAVE` is now `BT_LE_FEAT_BIT_CIS_PERIPHERAL`
  - `BT_FEAT_LE_SLAVE_FEATURE_XCHG` is now `BT_FEAT_LE_PER_INIT_FEAT_XCHG`
  - `BT_FEAT_LE_CIS_MASTER` is now `BT_FEAT_LE_CIS_CENTRAL`
  - `BT_FEAT_LE_CIS_SLAVE` is now `BT_FEAT_LE_CIS_PERIPHERAL`
  - `BT_LE_STATES_SLAVE_CONN_ADV` is now `BT_LE_STATES_PER_CONN_ADV`
  - `BT_HCI_OP_LE_READ_WL_SIZE` is now `BT_HCI_OP_LE_READ_FAL_SIZE`
  - `bt_hci_rp_le_read_wl_size` is now `bt_hci_rp_le_read_fal_size`
  - `bt_hci_rp_le_read_wl_size::wl_size` is now `bt_hci_rp_le_read_fal_size::fal_size`
  - `BT_HCI_OP_LE_CLEAR_WL` is now `BT_HCI_OP_LE_CLEAR_FAL`
  - `BT_HCI_OP_LE_ADD_DEV_TO_WL` is now `BT_HCI_OP_LE_REM_DEV_FROM_FAL`
  - `bt_hci_cp_le_add_dev_to_wl` is now `bt_hci_cp_le_add_dev_to_fal`
  - `BT_HCI_OP_LE_REM_DEV_FROM_WL` is now `BT_HCI_OP_LE_REM_DEV_FROM_FAL`
  - `bt_hci_cp_le_rem_dev_from_wl` is now `bt_hci_cp_le_rem_dev_from_fal`
  - `BT_HCI_ROLE_MASTER` is now `BT_HCI_ROLE_CENTRAL`
  - `BT_HCI_ROLE_SLAVE` is now `BT_HCI_ROLE_PERIPHERAL`
  - `BT_EVT_MASK_CL_SLAVE_BC_RX` is now `BT_EVT_MASK_CL_PER_BC_RX`
  - `BT_EVT_MASK_CL_SLAVE_BC_TIMEOUT` is now `BT_EVT_MASK_CL_PER_BC_TIMEOUT`
  - `BT_EVT_MASK_SLAVE_PAGE_RSP_TIMEOUT` is now `BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT`
  - `BT_EVT_MASK_CL_SLAVE_BC_CH_MAP_CHANGE` is now `BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE`
  - `m_*` structure members are now `c_*`
  - `s_*` structure members are now `p_*`
- The `CONFIG_BT_PERIPHERAL_PREF_SLAVE_LATENCY` Kconfig option is now
  [`CONFIG_BT_PERIPHERAL_PREF_LATENCY`](../kconfig.md#CONFIG_BT_PERIPHERAL_PREF_LATENCY "CONFIG_BT_PERIPHERAL_PREF_LATENCY")
- The `CONFIG_BT_CTLR_SLAVE_FEAT_REQ_SUPPORT` Kconfig option is now
  `CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`
- The `CONFIG_BT_CTLR_SLAVE_FEAT_REQ` Kconfig option is now
  [`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG`](../kconfig.md#CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG "CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG")

### Changes in this release

Removed APIs in this release

- Removed support for the deprecated `DEVICE_INIT` and `DEVICE_AND_API_INIT` macros.
- Removed support for the deprecated `BUILD_ASSERT_MSG` macro.
- Removed support for the deprecated `GET_ARG1`, `GET_ARG2` and `GET_ARGS_LESS_1` macros.
- Removed support for the deprecated Kconfig `PRINTK64` option.
- Removed support for the deprecated `bt_set_id_addr` function.
- Removed support for the Kconfig `USB` option. Option `USB_DEVICE_STACK`
  is sufficient to enable USB device support.
- Removed `CONFIG_OPENTHREAD_COPROCESSOR_SPINEL_ON_UART_ACM` and
  `CONFIG_OPENTHREAD_COPROCESSOR_SPINEL_ON_UART_DEV_NAME` Kconfig options
  in favor of chosen node `zephyr,ot-uart`.
- Removed `CONFIG_BT_UART_ON_DEV_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,bt-uart`.
- Removed `CONFIG_BT_MONITOR_ON_DEV_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,bt-mon-uart`.
- Removed `CONFIG_MODEM_GSM_UART_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,gsm-ppp`.
- Removed `CONFIG_UART_MCUMGR_ON_DEV_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,uart-mcumgr`.
- Removed `CONFIG_UART_CONSOLE_ON_DEV_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,console`.
- Removed `CONFIG_UART_SHELL_ON_DEV_NAME` Kconfig option
  in favor of direct use of chosen node `zephyr,shell-uart`.

---

### Stable API changes in this release

- Bluetooth

  - Added `multiple` to the [`bt_gatt_read_params`](../doxygen/html/structbt__gatt__read__params.md) - this
    structure contains two members: `handles`, which was moved from
    [`bt_gatt_read_params`](../doxygen/html/structbt__gatt__read__params.md), and `variable`.
- Networking

  - Added IPv4 address support to the multicast group join/leave monitor. The
    address parameter passed to the callback function was therefore changed from
    `in6_addr` to `net_addr` type.

## Kernel

## Architectures

- ARC

  - Add SMP support to ARCv3 HS6x
  - Add MWDT C library support
  - Add basic C++ support with MWDT toolchain
  - Add MPUv3 and MPUv6 support
  - Remove dead PM code from ARC core interrupt controller driver
  - Add updating arc connect debug mask dynamically
- ARM

  - AARCH32

    > - Updated CMSIS version to 5.8.0
    > - Added support for FPU in QEMU for Cortex-M, allowing to build and execute
    >   tests in CI with FPU and FPU\_SHARING options enabled.
    > - Added MPU support for Cortex-R
  - AARCH64
- RISC-V

  - Added support to RISC-V CPU devicetree compatible bindings
  - Added support to link with ITCM & DTCM sections
- x86

## Bluetooth

- Updated all APIs and internal implementation to be conformant with the new
  inclusive terminology in version 5.3 of the Bluetooth Core Specification
- Audio

  - Added the Microphone Input Control Service and client.
  - Changed the connected isochronous API to use a group-based opaque struct
  - Split the configuration options into connected and broadcast groups
  - Added support for a new sent callback to be notified when an SDU has been
    transmitted
- Direction Finding

  - Added configurability for conditional CTE RX support
  - Added support for CTE periodic advertising chain transmissions
- Host

  - Added support for setting more than 251 bytes of advertising data
  - Added new callbacks on ATT MTU update
  - Added a new call to retrieve the handle of an advertising set
  - Fixed key overwrite algorithm when working with multiple connections
  - Added configuration support for GATT security re-establishment
  - Added support for writing a long device name
  - OTS: Added object name write capability
- Mesh

  - Added return value for opcode callback
  - Added support for OOB Public Key in the provisionee role
  - Added a new API to manually store pending RPL entries
  - Added support for application access to mesh messages
  - Refactored the Mesh Model Extensions
- Bluetooth LE split software Controller

  - Added support for advertising PDU chaining, implementing advertising trains
    for Direction Finding
  - Added support for adding or removing the ACAD field in Common Extended
    Header Format to support BIGInfo
  - Refactored the legacy, extended and periodic advertising time reservation
    slot calculations
  - Implemented CSA#2 in Extended Advertising and Broadcast ISO sub-events
  - Added support for Extended Active Scanning
  - Added support for advertising on the S2 and S8 coding schemes
  - Added support for the Periodic Advertising channel map update indication
- HCI Driver

  - Removed all `CONFIG_BT_*_ON_DEV_NAME` Kconfig options, use Devicetree
    instead

## Boards & SoC Support

- Added support for these SoC series:

  - Added STM32U5 basic SoC support
- Removed support for these SoC series:
- Made these changes in other SoC series:

  - Added Atmel SAM0 pinctrl support
  - Added Atmel SAM4L USBC device controller
  - Added Atmel GMAC support for MDIO driver
  - Added Atmel GMAC support to use generic PHY driver
  - Added Atmel SAM counter (TC) Driver
  - Added Atmel SAM DAC (DACC) driver
  - Enabled Atmel SAM `clock-frequency` support from devicetree
  - Free Atmel SAM TRACESWO pin when unused
  - Enabled Cypress PSoC-6 Cortex-M4 support
  - Added low power support to STM32L0, STM32G0 and STM32WL series
  - STM32: Enabled ART Flash accelerator by default when available (F2, F4, F7, H7, L5)
  - STM32: Added Kconfig option to enable STM32Cube asserts (CONFIG\_USE\_STM32\_ASSERT)
  - NXP FRDM-K82F: Added arduino\_i2c and arduino\_spi aliases
  - NXP i.MX RT series: Added support for flash controller with XIP
  - NXP i.MX RT series: Added TRNG support
  - NXP i.MX RT1170: Added LPSPI driver support
  - NXP i.MX RT1170: Added ADC driver support
  - NXP i.MX RT1170: Enabled Segger RTT/SystemView
  - NXP i.MX RT1170: Added MCUX FlexCan support
  - NXP i.MX RT1064: Added watchdog driver support
  - NXP i.MX RT1064: Added DMA driver support
  - NXP i.MX RT600: Added arduino serial port
  - NXP i.MX RT600: Add mcuboot flash partitions
  - NXP i.MX RT600: Added counter support
  - NXP i.MX RT600: Added PWM support
  - NXP i.MX RT600: Added disk driver support
  - NXP i.MX RT600: Added USB driver support
  - NXP i.MX RT600: Added LPADC driver support
  - NXP i.MX RT600: Added CTimer Counter support
  - NXP KE1xF: Added SoC Power Management support
  - NXP LPC55s69: Added USB driver support
  - NXP LPC55s69: Added ctimer driver support
  - NXP LPC55s69: Added I2S driver support
- Changes for ARC boards:

  - Implement ‘run’ command for SMP nSIM simulation board
  - Enable upstream verification on QEMU ARCv3 HS6x board (qemu\_arc\_hs6x)
  - Implement creg GPIO driver and add it to hsdk and em\_starterkit boards
- Changes for ARM boards:

  - Added SPI support on Arduino standard SPI when possible
- Added support for these ARM boards:

  - Dragino NBSN95 NB-IoT Sensor Node
  - Seeedstudio LoRa-E5 Dev Board
  - ST B\_U585I\_IOT02A Discovery kit
  - ST Nucleo F446ZE
  - ST Nucleo U575ZI Q
  - ST STM32H735G Discovery
  - PJRC Teensy 4 Board
- Added support for these ARM64 boards:
- Removed support for these ARM boards:
- Removed support for these X86 boards:
- Made these changes in other boards:

  - arduino\_due: Added support for TC driver
  - atsame54\_xpro: Added support for PHY driver
  - sam4l\_ek: Added support for TC driver
  - sam4e\_xpro: Added support for PHY driver
  - sam4e\_xpro: Added support for TC driver
  - sam4s\_xplained: Added support for TC driver
  - sam\_e70\_xplained: Added support for DACC driver
  - sam\_e70\_xplained: Added support for PHY driver
  - sam\_e70\_xplained: Added support for TC driver
  - sam\_v71\_xult: Added support for DACC driver
  - sam\_v71\_xult: Added support for PHY driver
  - sam\_v71\_xult: Added support for TC driver
  - sam\_v71\_xult: Enable pwm on LED0
  - cy8ckit\_062\_ble: Added arduino’s nexus map
- Added support for these following shields:

  - 4.2inch epaper display (GDEW042T2)
  - X-NUCLEO-EEPRMA2 EEPROM memory expansion board

## Drivers and Sensors

- ADC

  - Added STM32WL ADC driver
  - STM32: Added support for oversampling
  - Added driver for Microchip MEC172x
- Audio

  - Added DMIC driver for nRF PDM peripherals
- Bluetooth
- CAN

  - Renesas R-Car driver added
- Clock Control
- Console
- Counter

  - Add Atmel SAM counter (TC) Driver
  - Added STM32WL RTC counter driver
- Crypto

  - STM23: Add support for SOCs with AES hardware block (STM32G0, STM32L5 and STM32WL)
- DAC

  - Added Atmel SAM DAC (DACC) driver
  - Added support for Microchip MCP4725
  - Added support for STM32F3 series
- Disk

  - Added SDMMC support on STM32L4+
  - STM32 SDMMC now supports SDIO enabled devices
  - Added USDHC support for i.MX RT685
- Display

  - Added support for ST7735R
- DMA

  - Added Atmel SAM XDMAC reload support
  - Added support on STM32F3, STM32G0, STM32H7 and STM32L5
  - STM32: Reviewed bindings definitions, “st,stm32-dma-v2bis” introduced.
- EEPROM

  - Added support for EEPROM emulated in flash.
- Entropy

  - Added support for STM32F2, STM32G0, STM32WB and STM32WL
- ESPI

  - Added support for Microchip eSPI SAF
- Ethernet

  - Added Atmel SAM/SAM0 GMAC devicetree support
  - Added Atmel SAM/SAM0 MDIO driver
  - Added MDIO driver
  - Added generic PHY driver
- Flash

  - Added STM32F2, STM32L5 and STM32WL Flash driver support
  - STM32: Max erase time parameter was moved to device tree
  - Added quad SPI support for STM32F4
- GPIO
- Hardware Info
- I2C
- I2S

  - Added Atmel SAM I2S driver support to XDMAC reload
  - Added driver for nRF I2S peripherals
- IEEE 802.15.4
- IPM

  - STM32: Add HSEM based IPM driver for STM32H7 series
- Interrupt Controller
- LED
- LoRa

  - lora\_send now blocks until the transmission is complete. lora\_send\_async
    can be used for the previous, non-blocking behaviour.
  - Enabled support for STM32WL series
- MEMC

  - Added STM32F4 support
- Modem

  - Added gsm\_ppp devicetree support
- PCI/PCIe

  - Fixed an issue that MSI-X was used even though it is not available.
  - Improved MBAR retrieval for MSI-X.
  - Added ability to retrieve extended PCI/PCIe capabilities.
- Pinmux

  - Added Atmel SAM0 pinctrl support
  - STM32: Deprecated definitions like ‘STM32F2\_PINMUX\_FUNC\_PA0\_UART4\_TX’
    are now removed.
- PWM

  - Property “st,prescaler” of binding “st,stm32-pwm” now defaults to “0”.
  - Added driver for ITE IT8XXX2 series
  - Added driver for NXP LPC devices
  - Added driver for Telink B91
- Sensor

  - Refactored various drivers to use `_dt_spec`.
  - Refactored various drivers to support multiple instances.
  - Enhanced TI HDC20XX driver to support DRDY/INT pin.
  - Updated temperature conversion formula in TI HDC20XX driver.
  - Enhanced MS5607 pressure sensor driver to support I2C.
  - Fixed temperature compensation in MS5607 pressure sensor driver.
  - Refactored ST LIS2DW12 driver to move range, power, and trigger
    configuration from Kconfig to dts.
  - Enhanced TI BQ274XX fuel gauge driver to support power management.
  - Aligned ST sensor drivers to use STMEMC HAL I/F v2.00.
  - Added Sensirion SGP40 multipixel gas sensor driver.
  - Added Sensirion SHTCX humidity sensor driver.
  - Added Sensirion SHT4X temperature and humidity sensor driver.
  - Added SiLabs SI7270 hall effect magnetic position and temperature sensor
    driver.
  - Added ST I3G4250D gyroscope driver.
  - Added TI INA219 and INA23X current/power monitor drivers.
  - Added TI LM75 and LM77 temperature sensor drivers.
  - Added TI HDC20XX humidity and temperature sensor driver.
- Serial

  - Added kconfig to disable runtime re-configuration of UART
    to reduce footprint if so desired.
  - Added ESP32-C3 polling only UART driver.
  - Added ESP32-S2 polling only UART driver.
  - Added Microchip XEC UART driver.
- SPI
- Timer
- USB

  - Added Atmel SAM4L USBC device controller driver
  - Added support for NXP LPC USB controller
  - Adapted drivers use new USB framework header
- Watchdog

  - Added STM32L5 watchdog support
- WiFi

## Networking

- 802.15.4 L2:

  - Fixed a bug, where the net\_pkt structure contained invalid LL address
    pointers after being processed by 802.15.4 L2.
  - Added an optional destination address filtering in the 802.15.4 L2.
- CoAP:

  - Added `user_data` field to the [`coap_packet`](../doxygen/html/structcoap__packet.md) structure.
  - Fixed processing of out-of-order notifications.
  - Fixed [`coap_packet_get_payload()`](../doxygen/html/group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c) function.
  - Converted CoAP test suite to ztest API.
  - Improved [`coap_packet_get_payload()`](../doxygen/html/group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c) function to minimize number
    of RNG calls.
  - Fixed retransmissions in the `coap_server` sample.
  - Fixed observer removal in the `coap_server` sample (on notification
    timeout).
- DHCPv4:

  - Fixed a bug, where DHPCv4 library removed statically configured gateway
    before obtaining a new one from the server.
- DNS:

  - Fixed a bug, where the same IP address was used to populate the result
    address info entries, when multiple IP addresses were obtained from the
    server.
- DNS-SD:

  - Added Service Type Enumeration support (`_services._dns_sd._udp.local`)
- HTTP:

  - Switched the library to use `zsock_*` API, to improve compatibility with
    various POSIX configurations.
  - Fixed a bug, where `HTTP_DATA_FINAL` notification was triggered even for
    intermediate response fragments.
- IPv6:

  - Multiple IPv6 fixes, addressing failures in IPv6Ready compliance tests.
- LwM2M:

  - Added support for notification timeout reporting to the application.
  - Fixed a bug, where a multi instance resource with only one active instance
    was incorrectly encoded on reads.
  - Fixed a bug, where notifications were generated on changes to non-readable
    resources.
  - Added mutex protection for the state variable of the `lwm2m_rd_client`
    module.
  - Removed LWM2M\_RES\_TYPE\_U64 type, as it’s not possible to encode it properly
    for large values.
  - Fixed a bug, where large unsigned integers were incorrectly encoded in TLV.
  - Multiple fixes for FLOAT type processing in the LwM2M engine and encoders.
  - Fix a bug, where IPSO Push Button counter resource was not triggering
    notification on incrementation.
  - Fixed a bug, where Register failures were reported as success to the
    application.
- Misc:

  - Added RX/TX timeout on a socket in `big_http_download` sample.
  - Introduced [`net_pkt_remove_tail()`](../doxygen/html/group__net__pkt.md#gab657c80669733a4afefaf1be6310107e) function.
    Added IEEE 802.15.4 security-related flags to the [`net_pkt`](../doxygen/html/structnet__pkt.md)
    structure.
  - Added bridging support to the Ethernet L2.
  - Fixed a bug in mDNS, where an incorrect address type could be set as a
    response destination.
  - Added an option to suppress ICMP destination unreachable errors.
  - Fixed possible assertion in `net nbr` shell command.
  - Major refactoring of the TFTP library.
- MQTT:

  - Added an option to register a custom transport type.
  - Fixed a bug in [`mqtt_abort()`](../doxygen/html/group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd), where the function could return without
    releasing a lock.
- OpenThread:

  - Update OpenThread module up to commit `9ea34d1e2053b6b2a80e1d46b65a6aee99fc504a`.
    Added several new Kconfig options to align with new OpenThread
    configurations.
  - Added OpenThread API mutex protection during initialization.
  - Converted OpenThread thread to a dedicated work queue.
  - Implemented missing `otPlatAssertFail()` platform function.
  - Fixed a bug, where NONE level OpenThread logs were not processed.
  - Added possibility to disable CSL sampling, when used.
  - Fixed a potential bug, where invalid error code could be returned by the
    platform radio layer to OpenThread.
  - Reworked UART configuration in the OpenThread Coprocessor sample.
- Socket:

  - Added microsecond accuracy in [`zsock_select()`](../doxygen/html/group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10) function.
  - Reworked [`zsock_select()`](../doxygen/html/group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10) into a syscall.
  - Fixed a bug, where [`poll()`](../doxygen/html/group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29) events were not signalled correctly
    for socketpair sockets.
  - Fixed a bug, where socket mutex could be used after being initialized by a
    new owner after being deallocated in [`zsock_close()`](../doxygen/html/group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349).
  - Fixed a possible assert after enabling CAN sockets.
  - Fixed IPPROTO\_RAW usage in packet socket implementation.
- TCP:

  - Fixed a bug, where `unacked_len` could be set to a negative value.
  - Fixed possible assertion failure in `tcp_send_data()`.
  - Fixed a bug, where [FIN, PSH, ACK] was not handled properly in
    TCP\_FIN\_WAIT\_2 state.
- TLS:

  - Reworked TLS sockets to use secure random generator from Zephyr.
  - Fixed busy looping during DTLS handshake with offloaded sockets.
  - Fixed busy looping during TLS/DTLS handshake on non blocking sockets.
  - Reset mbed TLS session on timed out DTLS handshake, to allow a retry without
    closing a socket.
  - Fixed TLS/DTLS [`sendmsg()`](../doxygen/html/group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8) implementation for larger payloads.
  - Fixed TLS/DTLS sockets `POLLHUP` notification.
- WebSocket:

  - Fixed [`poll()`](../doxygen/html/group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29) implementation for WebSocket, which did not work
    correctly with offloaded sockets.
  - Fixed [`ioctl()`](../doxygen/html/ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6) implementation for WebSocket, which did not work
    correctly with offloaded sockets.

## USB

- Added new header file where all defines and structures from Chapter 9
  (USB Device Framework) should be included.
- Revised configuration of USB device support.
  Removed Kconfig option `CONFIG_USB` and introduced Kconfig option
  `CONFIG_USB_DEVICE_DRIVER` to enable USB device controller drivers,
  which is selected when option `CONFIG_USB_DEVICE_STACK` is enabled.
- Enhanced verification of the control request in device stack, classes, and samples.
- Added support to store alternate interface setting.
- Added `zephyr_udc0` nodelabel to all boards with USB support to allow
  generic USB device support samples to be build.
- Reworked descriptors, config, and data definitions macros in CDC ACM class.
- Changed CDC ACM UART implementation to get configuration from devicetree.
  With this change, many `CONFIG_*_ON_DEV_NAME` options were removed and
  applications revised. See [CDC ACM](../connectivity/usb/device/usb_device.md#usb-device-cdc-acm) for more information.

## Build and Infrastructure

- Devicetree API

  - New “for-each” macros which work like existing APIs, but take variable
    numbers of arguments: [`DT_FOREACH_CHILD_VARGS`](../doxygen/html/group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de),
    [`DT_FOREACH_CHILD_STATUS_OKAY_VARGS`](../doxygen/html/group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3),
    [`DT_FOREACH_PROP_ELEM_VARGS`](../doxygen/html/group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607),
    [`DT_INST_FOREACH_CHILD_VARGS`](../doxygen/html/group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651),
    [`DT_INST_FOREACH_STATUS_OKAY_VARGS`](../doxygen/html/group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38),
    [`DT_INST_FOREACH_PROP_ELEM_VARGS`](../doxygen/html/group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)
  - Other new “for-each” macros: [`DT_FOREACH_STATUS_OKAY`](../doxygen/html/group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8),
    [`DT_FOREACH_STATUS_OKAY_VARGS`](../doxygen/html/group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)
  - New macros for converting strings to C tokens: [`DT_STRING_TOKEN`](../doxygen/html/group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54),
    [`DT_STRING_UPPER_TOKEN`](../doxygen/html/group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)
  - New [Pinctrl (pin control)](../build/dts/api/api.md#devicetree-pinctrl-api) helper macros
- Devicetree tooling

  - Errors are now generated when invalid YAML files are discovered while
    searching for bindings. See [Where bindings are located](../build/dts/bindings-intro.md#dt-where-bindings-are-located) for
    information on the search path.
  - File names ending in `.yml` are now considered YAML files when searching
    for bindings.
  - Errors are now generated if invalid node names are used. For example, the
    node name `node?` now generates an error message ending in `node?: Bad
    character '?' in node name`. The valid node names are documented in
    “2.2.2 Node Names” of the Devicetree specification v0.3.
  - Warnings are now generated if a [compatible property](../build/dts/intro-syntax-structure.md#dt-important-props) in the `vendor,device` format uses an unknown
    vendor prefix. This warning does not apply to the root node.

    Known vendor prefixes are defined in
    `dts/bindings/vendor-prefixes.txt` files, which may appear in any
    directory in [DTS\_ROOT](../develop/application/index.md#dts-root).

    These may be upgraded to errors using the edtlib Python APIs; Zephyr’s CI
    now generates such errors.
- Devicetree bindings

  - Various bindings had incorrect vendor prefixes in their [compatible](../build/dts/intro-syntax-structure.md#dt-important-props) properties; the following changes were made to fix
    these.

    | Old compatible | New compatible |
    | --- | --- |
    | `nios,i2c` | [`altr,nios2-i2c`](../build/dts/api/bindings/i2c/altr%2Cnios2-i2c.md#std-dtcompatible-altr-nios2-i2c) |
    | `cadence,tensilica-xtensa-lx4` | [`cdns,tensilica-xtensa-lx4`](../build/dts/api/bindings/cpu/cdns%2Ctensilica-xtensa-lx4.md#std-dtcompatible-cdns-tensilica-xtensa-lx4) |
    | `cadence,tensilica-xtensa-lx6` | [`cdns,tensilica-xtensa-lx6`](../build/dts/api/bindings/cpu/cdns%2Ctensilica-xtensa-lx6.md#std-dtcompatible-cdns-tensilica-xtensa-lx6) |
    | `colorway,lpd8803` | [`greeled,lpd8803`](../build/dts/api/bindings/led_strip/greeled%2Clpd8803.md#std-dtcompatible-greeled-lpd8803) |
    | `colorway,lpd8806` | [`greeled,lpd8806`](../build/dts/api/bindings/led_strip/greeled%2Clpd8806.md#std-dtcompatible-greeled-lpd8806) |
    | `grove,light` | [`seeed,grove-light`](../build/dts/api/bindings/sensor/seeed%2Cgrove-light.md#std-dtcompatible-seeed-grove-light) |
    | `grove,temperature` | [`seeed,grove-temperature`](../build/dts/api/bindings/sensor/seeed%2Cgrove-temperature.md#std-dtcompatible-seeed-grove-temperature) |
    | `max,max30101` | [`maxim,max30101`](../build/dts/api/bindings/sensor/maxim%2Cmax30101.md#std-dtcompatible-maxim-max30101) |
    | `ublox,sara-r4` | [`u-blox,sara-r4`](../build/dts/api/bindings/modem/u-blox%2Csara-r4.md#std-dtcompatible-u-blox-sara-r4) |
    | `xtensa,core-intc` | [`cdns,xtensa-core-intc`](../build/dts/api/bindings/interrupt-controller/cdns%2Cxtensa-core-intc.md#std-dtcompatible-cdns-xtensa-core-intc) |
    | `vexriscv,intc0` | `vexriscv-intc0` |

    Out of tree users of these bindings will need to update their
    devicetrees.

    You can support multiple versions of Zephyr with one devicetree by
    including both the old and new values in your nodes’ compatible properties,
    like this example for the LPD8803:

    ```text
    my-led-strip@0 {
            compatible = "colorway,lpd8803", "greeled,lpd8803";
            ...
    };
    ```
  - Other new bindings in alphabetical order: [`andestech,atcgpio100`](../build/dts/api/bindings/gpio/andestech%2Catcgpio100.md#std-dtcompatible-andestech-atcgpio100),
    [`arm,gic-v3-its`](../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3-its.md#std-dtcompatible-arm-gic-v3-its), [`atmel,sam0-gmac`](../build/dts/api/bindings/ethernet/atmel%2Csam0-gmac.md#std-dtcompatible-atmel-sam0-gmac),
    [`atmel,sam0-pinctrl`](../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl), [`atmel,sam-dac`](../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac),
    [`atmel,sam-mdio`](../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio), [`atmel,sam-usbc`](../build/dts/api/bindings/usb/atmel%2Csam-usbc.md#std-dtcompatible-atmel-sam-usbc),
    [`cdns,tensilica-xtensa-lx7`](../build/dts/api/bindings/cpu/cdns%2Ctensilica-xtensa-lx7.md#std-dtcompatible-cdns-tensilica-xtensa-lx7),
    `espressif,esp32c3-uart`,
    [`espressif,esp32-intc`](../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc),
    `espressif,esp32s2-uart`, [`ethernet-phy`](../build/dts/api/bindings/ethernet/ethernet-phy.md#std-dtcompatible-ethernet-phy),
    [`fcs,fxl6408`](../build/dts/api/bindings/gpio/fcs%2Cfxl6408.md#std-dtcompatible-fcs-fxl6408), [`ilitek,ili9341`](../build/dts/api/bindings/display/ilitek%2Cili9341.md#std-dtcompatible-ilitek-ili9341),
    [`ite,it8xxx2-bbram`](../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-bbram.md#std-dtcompatible-ite-it8xxx2-bbram), `ite,it8xxx2-kscan`,
    `ite,it8xxx2-pinctrl-conf`, [`ite,it8xxx2-pwm`](../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwm.md#std-dtcompatible-ite-it8xxx2-pwm),
    [`ite,it8xxx2-pwmprs`](../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwmprs.md#std-dtcompatible-ite-it8xxx2-pwmprs), [`ite,it8xxx2-watchdog`](../build/dts/api/bindings/watchdog/ite%2Cit8xxx2-watchdog.md#std-dtcompatible-ite-it8xxx2-watchdog),
    [`lm75`](../build/dts/api/bindings/sensor/lm75.md#std-dtcompatible-lm75), [`lm77`](../build/dts/api/bindings/sensor/lm77.md#std-dtcompatible-lm77), [`meas,ms5607`](../build/dts/api/compatibles/meas%2Cms5607.md#std-dtcompatible-meas-ms5607),
    [`microchip,ksz8863`](../build/dts/api/bindings/dsa/microchip%2Cksz8863.md#std-dtcompatible-microchip-ksz8863), [`microchip,mcp7940n`](../build/dts/api/bindings/rtc/microchip%2Cmcp7940n.md#std-dtcompatible-microchip-mcp7940n),
    `microchip,xec-adc-v2`, [`microchip,xec-ecia`](../build/dts/api/bindings/interrupt-controller/microchip%2Cxec-ecia.md#std-dtcompatible-microchip-xec-ecia),
    [`microchip,xec-ecia-girq`](../build/dts/api/bindings/interrupt-controller/microchip%2Cxec-ecia-girq.md#std-dtcompatible-microchip-xec-ecia-girq),
    [`microchip,xec-gpio-v2`](../build/dts/api/bindings/gpio/microchip%2Cxec-gpio-v2.md#std-dtcompatible-microchip-xec-gpio-v2),
    [`microchip,xec-i2c-v2`](../build/dts/api/bindings/i2c/microchip%2Cxec-i2c-v2.md#std-dtcompatible-microchip-xec-i2c-v2), [`microchip,xec-pcr`](../build/dts/api/bindings/clock/microchip%2Cxec-pcr.md#std-dtcompatible-microchip-xec-pcr),
    [`microchip,xec-uart`](../build/dts/api/bindings/serial/microchip%2Cxec-uart.md#std-dtcompatible-microchip-xec-uart), [`nuvoton,npcx-bbram`](../build/dts/api/bindings/memory-controllers/nuvoton%2Cnpcx-bbram.md#std-dtcompatible-nuvoton-npcx-bbram),
    [`nuvoton,npcx-booter-variant`](../build/dts/api/bindings/misc/nuvoton%2Cnpcx-booter-variant.md#std-dtcompatible-nuvoton-npcx-booter-variant),
    [`nuvoton,npcx-ps2-channel`](../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-channel.md#std-dtcompatible-nuvoton-npcx-ps2-channel),
    [`nuvoton,npcx-ps2-ctrl`](../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-ctrl.md#std-dtcompatible-nuvoton-npcx-ps2-ctrl), [`nuvoton,npcx-soc-id`](../build/dts/api/bindings/misc/nuvoton%2Cnpcx-soc-id.md#std-dtcompatible-nuvoton-npcx-soc-id),
    [`nxp,imx-ccm-rev2`](../build/dts/api/bindings/clock/nxp%2Cimx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2), [`nxp,lpc-ctimer`](../build/dts/api/bindings/timer/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer),
    [`nxp,lpc-uid`](../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid), `nxp,mcux-usbd`,
    [`nxp,sctimer-pwm`](../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm), [`ovti,ov2640`](../build/dts/api/bindings/video/ovti%2Cov2640.md#std-dtcompatible-ovti-ov2640),
    [`renesas,rcar-can`](../build/dts/api/bindings/can/renesas%2Crcar-can.md#std-dtcompatible-renesas-rcar-can), [`renesas,rcar-i2c`](../build/dts/api/bindings/i2c/renesas%2Crcar-i2c.md#std-dtcompatible-renesas-rcar-i2c),
    `reserved-memory`, `riscv,sifive-e24`,
    [`sensirion,sgp40`](../build/dts/api/bindings/sensor/sensirion%2Csgp40.md#std-dtcompatible-sensirion-sgp40), [`sensirion,sht4x`](../build/dts/api/bindings/sensor/sensirion%2Csht4x.md#std-dtcompatible-sensirion-sht4x),
    [`sensirion,shtcx`](../build/dts/api/bindings/sensor/sensirion%2Cshtcx.md#std-dtcompatible-sensirion-shtcx), [`silabs,si7055`](../build/dts/api/bindings/sensor/silabs%2Csi7055.md#std-dtcompatible-silabs-si7055),
    [`silabs,si7210`](../build/dts/api/bindings/sensor/silabs%2Csi7210.md#std-dtcompatible-silabs-si7210), [`snps,creg-gpio`](../build/dts/api/bindings/gpio/snps%2Ccreg-gpio.md#std-dtcompatible-snps-creg-gpio),
    [`st,i3g4250d`](../build/dts/api/bindings/sensor/st%2Ci3g4250d.md#std-dtcompatible-st-i3g4250d), [`st,stm32-aes`](../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes),
    [`st,stm32-dma`](../build/dts/api/bindings/dma/st%2Cstm32-dma.md#std-dtcompatible-st-stm32-dma), [`st,stm32-dma-v2bis`](../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis),
    [`st,stm32-hsem-mailbox`](../build/dts/api/bindings/ipm/st%2Cstm32-hsem-mailbox.md#std-dtcompatible-st-stm32-hsem-mailbox), [`st,stm32-nv-flash`](../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash),
    [`st,stm32-spi-subghz`](../build/dts/api/bindings/spi/st%2Cstm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz),
    `st,stm32u5-flash-controller`,
    [`st,stm32u5-msi-clock`](../build/dts/api/bindings/clock/st%2Cstm32u5-msi-clock.md#std-dtcompatible-st-stm32u5-msi-clock), [`st,stm32u5-pll-clock`](../build/dts/api/bindings/clock/st%2Cstm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock),
    [`st,stm32u5-rcc`](../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc), [`st,stm32wl-hse-clock`](../build/dts/api/bindings/clock/st%2Cstm32wl-hse-clock.md#std-dtcompatible-st-stm32wl-hse-clock),
    [`st,stm32wl-subghz-radio`](../build/dts/api/bindings/lora/st%2Cstm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio), [`st,stmpe1600`](../build/dts/api/bindings/gpio/st%2Cstmpe1600.md#std-dtcompatible-st-stmpe1600),
    [`syscon`](../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon), [`telink,b91`](../build/dts/api/bindings/cpu/telink%2Cb91.md#std-dtcompatible-telink-b91),
    [`telink,b91-flash-controller`](../build/dts/api/bindings/flash_controller/telink%2Cb91-flash-controller.md#std-dtcompatible-telink-b91-flash-controller),
    [`telink,b91-gpio`](../build/dts/api/bindings/gpio/telink%2Cb91-gpio.md#std-dtcompatible-telink-b91-gpio), [`telink,b91-i2c`](../build/dts/api/bindings/i2c/telink%2Cb91-i2c.md#std-dtcompatible-telink-b91-i2c),
    `telink,b91-pinmux`, [`telink,b91-power`](../build/dts/api/bindings/power/telink%2Cb91-power.md#std-dtcompatible-telink-b91-power),
    [`telink,b91-pwm`](../build/dts/api/bindings/pwm/telink%2Cb91-pwm.md#std-dtcompatible-telink-b91-pwm), [`telink,b91-spi`](../build/dts/api/bindings/spi/telink%2Cb91-spi.md#std-dtcompatible-telink-b91-spi),
    [`telink,b91-trng`](../build/dts/api/bindings/rng/telink%2Cb91-trng.md#std-dtcompatible-telink-b91-trng), [`telink,b91-uart`](../build/dts/api/bindings/serial/telink%2Cb91-uart.md#std-dtcompatible-telink-b91-uart),
    [`telink,b91-zb`](../build/dts/api/bindings/ieee802154/telink%2Cb91-zb.md#std-dtcompatible-telink-b91-zb), [`ti,hdc2010`](../build/dts/api/bindings/sensor/ti%2Chdc2010.md#std-dtcompatible-ti-hdc2010),
    [`ti,hdc2021`](../build/dts/api/bindings/sensor/ti%2Chdc2021.md#std-dtcompatible-ti-hdc2021), [`ti,hdc2022`](../build/dts/api/bindings/sensor/ti%2Chdc2022.md#std-dtcompatible-ti-hdc2022),
    [`ti,hdc2080`](../build/dts/api/bindings/sensor/ti%2Chdc2080.md#std-dtcompatible-ti-hdc2080), [`ti,hdc20xx`](../build/dts/api/bindings/sensor/ti%2Chdc20xx.md#std-dtcompatible-ti-hdc20xx),
    [`ti,ina219`](../build/dts/api/bindings/sensor/ti%2Cina219.md#std-dtcompatible-ti-ina219), `ti,ina23x`,
    [`ti,tca9538`](../build/dts/api/bindings/gpio/ti%2Ctca9538.md#std-dtcompatible-ti-tca9538), [`ti,tca9546a`](../build/dts/api/bindings/i2c/ti%2Ctca9546a.md#std-dtcompatible-ti-tca9546a),
    [`ti,tlc59108`](../build/dts/api/bindings/led/ti%2Ctlc59108.md#std-dtcompatible-ti-tlc59108),
    [`xlnx,gem`](../build/dts/api/bindings/ethernet/xlnx%2Cgem.md#std-dtcompatible-xlnx-gem), [`zephyr,bbram-emul`](../build/dts/api/bindings/memory-controllers/zephyr%2Cbbram-emul.md#std-dtcompatible-zephyr-bbram-emul),
    [`zephyr,cdc-acm-uart`](../build/dts/api/bindings/serial/zephyr%2Ccdc-acm-uart.md#std-dtcompatible-zephyr-cdc-acm-uart), `zephyr,gsm-ppp`,
    [`zephyr,native-posix-udc`](../build/dts/api/bindings/usb/zephyr%2Cnative-posix-udc.md#std-dtcompatible-zephyr-native-posix-udc)
- West (extensions)

  > - openocd runner: Zephyr thread awareness is now available in GDB by default
  >   for application builds with [`CONFIG_DEBUG_THREAD_INFO`](../kconfig.md#CONFIG_DEBUG_THREAD_INFO "CONFIG_DEBUG_THREAD_INFO") set to `y`
  >   in [Configuration System (Kconfig)](../build/kconfig/index.md#kconfig). This applies to `west debug`, `west debugserver`,
  >   and `west attach`. OpenOCD version later than 0.11.0 must be installed
  >   on the host system.

## Libraries / Subsystems

- Disk
- Management
- CMSIS subsystem
- Power management

  - The APIs to set/clear/check if devices are busy from a power management
    perspective have been moved to the PM subsystem. Their naming and signature
    has also been adjusted to follow common conventions. Below you can find the
    equivalence list.

    - `device_busy_set` -> `pm_device_busy_set`
    - `device_busy_clear` -> `pm_device_busy_clear`
    - `device_busy_check` -> `pm_device_is_busy`
    - `device_any_busy_check` -> `pm_device_is_any_busy`
  - The device power management callback (`pm_device_control_callback_t`) has
    been largely simplified to work based on *actions*, resulting in simpler and
    more natural implementations. This principle is also used by other OSes like
    the Linux Kernel. As a result, the callback argument list has been reduced
    to the device instance and an action (e.g. `PM_DEVICE_ACTION_RESUME`).
    Other improvements include specification of error codes, removal of some
    unused/unclear states, or guarantees such as avoid calling a device for
    suspend/resume if it is already at the right state. All these changes
    together have allowed simplifying multiple device power management callback
    implementations.
  - Introduced a new API to allow devices capable of wake up the system
    register themselves was wake up sources. This permits applications to
    select the most appropriate way to wake up the system when it is
    suspended. Devices marked as wake up source are not suspended by the kernel
    when the system is idle. It is possible to declare a device wake up capable
    direct in devicetree like this example:

    ```text
    &gpio0 {
            compatible = "zephyr,gpio-emul";
            gpio-controller;
            wakeup-source;
    };
    ```

    - Removed `PM_DEVICE_STATE_FORCE_SUSPEND` device power state.because it
      is an action and not a state.
    - Removed `PM_DEVICE_STATE_RESUMING` and `PM_DEVICE_STATE_SUSPENDING`.
      They were transitional states and only used in device runtime. Now the
      subsystem is using device flag to keep track of a transition.
    - Implement constraint API as weak symbols so applications or platform
      can override them. Platforms can have their own way to
      set/release constraints in their drivers that are not part of
      Zephyr code base.
- Logging
- MODBUS

  - Changed server handler to copy Transaction and Protocol Identifiers
    to response header.
- Random

  - xoroshiro128+ PRNG deprecated in favor of xoshiro128++
- Shell
- Storage
- Task Watchdog
- Tracing
- Debug
- OS

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## Trusted Firmware-m

- Renamed psa\_level\_1 sample to psa\_crypto. Extended the use of the PSA Cryptography
  1.0 API in the sample code to demonstrate additional crypto functionality.
- Added a new sample to showcase the PSA Protecter Storage service.

## Documentation

- Kconfig options need to be referenced using the `:kconfig:option:` Sphinx role.
  Previous to this change, `:option:` was used for this purpose.
- Doxygen alias `@config{}` has been deprecated in favor of `@kconfig{}`.

## Tests and Samples

## Issue Related Items

These GitHub issues were addressed since the previous 2.6.0 tagged
release:

- [GitHub #39443](https://github.com/zephyrproject-rtos/zephyr/issues/39443) - Be more inclusive
- [GitHub #39419](https://github.com/zephyrproject-rtos/zephyr/issues/39419) - STM32WL55 not found st/wl/stm32wl55jcix-pinctrl.dtsi
- [GitHub #39413](https://github.com/zephyrproject-rtos/zephyr/issues/39413) - warnings when using newlibc and threads
- [GitHub #39409](https://github.com/zephyrproject-rtos/zephyr/issues/39409) - runners: canopen: program download fails with slow flash access and/or congested CAN nets
- [GitHub #39389](https://github.com/zephyrproject-rtos/zephyr/issues/39389) - http\_get, big\_http\_download samples fails to build
- [GitHub #39388](https://github.com/zephyrproject-rtos/zephyr/issues/39388) - GSM Modem sample fails to build
- [GitHub #39378](https://github.com/zephyrproject-rtos/zephyr/issues/39378) - Garbage IQ Data Reports are generated if some check in hci\_df\_prepare\_connectionless\_iq\_report fails
- [GitHub #39294](https://github.com/zephyrproject-rtos/zephyr/issues/39294) - noticing stm32 clock domain naming changes
- [GitHub #39291](https://github.com/zephyrproject-rtos/zephyr/issues/39291) - Bluetooth: Periodic advertising
- [GitHub #39284](https://github.com/zephyrproject-rtos/zephyr/issues/39284) - mdns + dns\_sd: fix regression that breaks ptr queries
- [GitHub #39281](https://github.com/zephyrproject-rtos/zephyr/issues/39281) - Undefined references to k\_thread\_abort related tracing routines
- [GitHub #39270](https://github.com/zephyrproject-rtos/zephyr/issues/39270) - example-application CI build fails
- [GitHub #39263](https://github.com/zephyrproject-rtos/zephyr/issues/39263) - Bluetooth: controller: DF: wrong handling of max\_cte\_count
- [GitHub #39260](https://github.com/zephyrproject-rtos/zephyr/issues/39260) - [backport v2.7-branch] backport of #38292 failed
- [GitHub #39240](https://github.com/zephyrproject-rtos/zephyr/issues/39240) - ARC Kconfig allows so select IRQ configuration which isn’t supported in SW
- [GitHub #39206](https://github.com/zephyrproject-rtos/zephyr/issues/39206) - lwm2m: send\_attempts field does not seem to be used?
- [GitHub #39205](https://github.com/zephyrproject-rtos/zephyr/issues/39205) - drivers: wifi: esp\_at: cannot connect to open (unsecure) WiFi networks
- [GitHub #39195](https://github.com/zephyrproject-rtos/zephyr/issues/39195) - USB: netusb: example echo\_server not working as expected
- [GitHub #39190](https://github.com/zephyrproject-rtos/zephyr/issues/39190) - tests/subsys/logging/log\_core\_additional/logging.add.log2 fails
- [GitHub #39188](https://github.com/zephyrproject-rtos/zephyr/issues/39188) - tests/bluetooth/mesh/bluetooth.mesh.ext\_adv fails
- [GitHub #39185](https://github.com/zephyrproject-rtos/zephyr/issues/39185) - tests/subsys/logging/log\_core\_additional/logging.add.user fails on several platforms
- [GitHub #39180](https://github.com/zephyrproject-rtos/zephyr/issues/39180) - samples/subsys/mgmt/osdp/peripheral\_device & samples/subsys/mgmt/osdp/control\_panel fail to build
- [GitHub #39170](https://github.com/zephyrproject-rtos/zephyr/issues/39170) - Can not run correctly on NXP MIMXRT1061 CVL5A.
- [GitHub #39135](https://github.com/zephyrproject-rtos/zephyr/issues/39135) - samples/compression/lz4 build failed (lz4.h: No such file or directory)
- [GitHub #39132](https://github.com/zephyrproject-rtos/zephyr/issues/39132) - subsys/net/ip/tcp2: Missing feature to decrease Receive Window size sent in the ACK messge
- [GitHub #39123](https://github.com/zephyrproject-rtos/zephyr/issues/39123) - ztest: Broken on NRF52840 Platform
- [GitHub #39115](https://github.com/zephyrproject-rtos/zephyr/issues/39115) - sensor: fdc2x1x: warnings and compilation errors when PM\_DEVICE is used
- [GitHub #39086](https://github.com/zephyrproject-rtos/zephyr/issues/39086) - CMake warning during build - depracated roule CMP0079
- [GitHub #39085](https://github.com/zephyrproject-rtos/zephyr/issues/39085) - Ordering of device\_map() breaks PCIe config space mapping on ARM64
- [GitHub #39075](https://github.com/zephyrproject-rtos/zephyr/issues/39075) - IPv6 address not set on loopback interface
- [GitHub #39051](https://github.com/zephyrproject-rtos/zephyr/issues/39051) - Zephyr was unable to find the toolchain. Is the environment misconfigured?
- [GitHub #39036](https://github.com/zephyrproject-rtos/zephyr/issues/39036) - Multicast packet forwarding not working for the coap\_server sample and Openthread
- [GitHub #39022](https://github.com/zephyrproject-rtos/zephyr/issues/39022) - [backport v2.7-branch] backport of #38834 failed
- [GitHub #39011](https://github.com/zephyrproject-rtos/zephyr/issues/39011) - Bluetooth: Mesh: Model extensions walk stops before last model
- [GitHub #39009](https://github.com/zephyrproject-rtos/zephyr/issues/39009) - Nordic PWM causing lock up due to infinte loop
- [GitHub #39008](https://github.com/zephyrproject-rtos/zephyr/issues/39008) - tests: logging.add.user: build failure on STM32H7 targets
- [GitHub #38999](https://github.com/zephyrproject-rtos/zephyr/issues/38999) - [backport v2.7-branch] backport of #38407 failed
- [GitHub #38996](https://github.com/zephyrproject-rtos/zephyr/issues/38996) - There is no way to leave a ipv6 multicast group
- [GitHub #38994](https://github.com/zephyrproject-rtos/zephyr/issues/38994) - ARP: Replies are sent to multicast MAC address rather than senders MAC address.
- [GitHub #38970](https://github.com/zephyrproject-rtos/zephyr/issues/38970) - LWM2M Client Sample with DTLS enabled fail to connect
- [GitHub #38966](https://github.com/zephyrproject-rtos/zephyr/issues/38966) - Please add STM32F412VX
- [GitHub #38961](https://github.com/zephyrproject-rtos/zephyr/issues/38961) - tests: kernel: sched: schedule\_api: instable on disco\_l475\_iot1
- [GitHub #38959](https://github.com/zephyrproject-rtos/zephyr/issues/38959) - ITE RISCV I2C driver returning positive values for error instead of negative values
- [GitHub #38943](https://github.com/zephyrproject-rtos/zephyr/issues/38943) - west: update hal\_espressif failure
- [GitHub #38938](https://github.com/zephyrproject-rtos/zephyr/issues/38938) - Bluetooth tester application should be able return L2CAP ECFC credits on demand
- [GitHub #38930](https://github.com/zephyrproject-rtos/zephyr/issues/38930) - Low Power mode not functional on nucleo\_l073rz
- [GitHub #38924](https://github.com/zephyrproject-rtos/zephyr/issues/38924) - twister: cmake: Misleading error in Twister when sdk-zephyr 0.13.1 not used
- [GitHub #38904](https://github.com/zephyrproject-rtos/zephyr/issues/38904) - [backport v2.7-branch] backport of #38860 failed
- [GitHub #38902](https://github.com/zephyrproject-rtos/zephyr/issues/38902) - i2c\_nrfx\_twim: Error 0x0BAE0002 if sensor is set in trigger mode and reset with nrf device
- [GitHub #38899](https://github.com/zephyrproject-rtos/zephyr/issues/38899) - There is no valid date setting function in the RTC driver of the LL Library of STM32
- [GitHub #38893](https://github.com/zephyrproject-rtos/zephyr/issues/38893) - g0b1re + spi\_flash\_at45 + flash\_shell: First write always fails with `CONFIG_PM_DEVICE`
- [GitHub #38886](https://github.com/zephyrproject-rtos/zephyr/issues/38886) - devicetree/memory.h probably should not exist as-is
- [GitHub #38877](https://github.com/zephyrproject-rtos/zephyr/issues/38877) - Running the zephyr elf natively on an arm a53 machine (ThunderX2) with KVM emulation
- [GitHub #38870](https://github.com/zephyrproject-rtos/zephyr/issues/38870) - stm32f1: Button callback not fired
- [GitHub #38853](https://github.com/zephyrproject-rtos/zephyr/issues/38853) - Bluetooth: host: bt\_unpair failed because function [bt\_conn\_set\_state] wont work as expected
- [GitHub #38849](https://github.com/zephyrproject-rtos/zephyr/issues/38849) - drivers: i2c: nrf: i2c error with burst write
- [GitHub #38829](https://github.com/zephyrproject-rtos/zephyr/issues/38829) - net\_buf issue leads to unwanted elem free
- [GitHub #38826](https://github.com/zephyrproject-rtos/zephyr/issues/38826) - tests/lib/cmsis\_dsp: malloc failed on 128K SRAM targets
- [GitHub #38818](https://github.com/zephyrproject-rtos/zephyr/issues/38818) - driver display display\_st7789v.c build error
- [GitHub #38815](https://github.com/zephyrproject-rtos/zephyr/issues/38815) - kernel/mem\_domain: Remove dead case in check\_add\_partition()
- [GitHub #38807](https://github.com/zephyrproject-rtos/zephyr/issues/38807) - stm32: Missing header in power.c files
- [GitHub #38804](https://github.com/zephyrproject-rtos/zephyr/issues/38804) - testskernelthreadsthread\_stack test fail with ARC
- [GitHub #38799](https://github.com/zephyrproject-rtos/zephyr/issues/38799) - BLE central\_ht only receives 7 notifications
- [GitHub #38796](https://github.com/zephyrproject-rtos/zephyr/issues/38796) - Failure building the zephyrtestssubsyscpplibcxx project
- [GitHub #38791](https://github.com/zephyrproject-rtos/zephyr/issues/38791) - Example code\_relocation not compiling.
- [GitHub #38790](https://github.com/zephyrproject-rtos/zephyr/issues/38790) - SD FatFS Sample Build Failure
- [GitHub #38784](https://github.com/zephyrproject-rtos/zephyr/issues/38784) - stm32: pm: Debug mode not functional on G0
- [GitHub #38782](https://github.com/zephyrproject-rtos/zephyr/issues/38782) - CONFIG\_BT\_CTLR\_DATA\_LENGTH\_MAX=250 causes pairing compatibility issues with many devices
- [GitHub #38769](https://github.com/zephyrproject-rtos/zephyr/issues/38769) - mqtt: the size of a mqtt payload is limited
- [GitHub #38765](https://github.com/zephyrproject-rtos/zephyr/issues/38765) - samples: create an OLED example
- [GitHub #38764](https://github.com/zephyrproject-rtos/zephyr/issues/38764) - CBPRINTF\_FP\_SUPPORT does not work after NEWLIB\_LIBC enabled
- [GitHub #38761](https://github.com/zephyrproject-rtos/zephyr/issues/38761) - Does zephyr\_library\_property defines -DTRUE in command-line?
- [GitHub #38756](https://github.com/zephyrproject-rtos/zephyr/issues/38756) - Twister: missing testcases with error in report
- [GitHub #38745](https://github.com/zephyrproject-rtos/zephyr/issues/38745) - Bluetooth when configured for extended advertising does not limit advertisement packet size if a non-extended avertisement is used
- [GitHub #38737](https://github.com/zephyrproject-rtos/zephyr/issues/38737) - drivers: syscon: missing implementation
- [GitHub #38735](https://github.com/zephyrproject-rtos/zephyr/issues/38735) - nucleo\_wb55rg: Flash space left to M0 binary is not sufficient anymore
- [GitHub #38731](https://github.com/zephyrproject-rtos/zephyr/issues/38731) - test-ci: ptp\_clock\_test : test failure on frdm\_k64f platform
- [GitHub #38727](https://github.com/zephyrproject-rtos/zephyr/issues/38727) - [RFC] Add hal\_gigadevice to support GigaDevice SoC Vendor
- [GitHub #38716](https://github.com/zephyrproject-rtos/zephyr/issues/38716) - modem: HL7800: does not work with IPv6
- [GitHub #38702](https://github.com/zephyrproject-rtos/zephyr/issues/38702) - Coap server not properly removing observers
- [GitHub #38701](https://github.com/zephyrproject-rtos/zephyr/issues/38701) - Observable resource of coap server seems to not support a restart of an observer
- [GitHub #38700](https://github.com/zephyrproject-rtos/zephyr/issues/38700) - Observable resource of coap server seems to not support 2 observers simultaneously
- [GitHub #38698](https://github.com/zephyrproject-rtos/zephyr/issues/38698) - stm32f4\_disco: Socket CAN sample not working
- [GitHub #38697](https://github.com/zephyrproject-rtos/zephyr/issues/38697) - The coap\_server sample is missing the actual send in the retransmit routine
- [GitHub #38694](https://github.com/zephyrproject-rtos/zephyr/issues/38694) - Disabling NET\_CONFIG\_AUTO\_INIT does not require calling net\_config\_init() manually in application as mentioned in Zephyr Network Configuration Library documentation
- [GitHub #38692](https://github.com/zephyrproject-rtos/zephyr/issues/38692) - samples/tfm\_integration: Compilation fails (“unexpected keyword argument ‘rom\_fixed’”)
- [GitHub #38691](https://github.com/zephyrproject-rtos/zephyr/issues/38691) - MPU fault with mcumgr bluetooth FOTA started whilst existing FOTA is in progress
- [GitHub #38690](https://github.com/zephyrproject-rtos/zephyr/issues/38690) - Wrong initialisation priority on different display drivers (eg. ST7735r) cause exception when using lvgl.
- [GitHub #38688](https://github.com/zephyrproject-rtos/zephyr/issues/38688) - bt\_gatt\_unsubscribe does not remove subscription from internal list/returning BT\_GATT\_ITER\_STOP causes bt\_gatt\_subscribe to return -ENOMEM / -12
- [GitHub #38675](https://github.com/zephyrproject-rtos/zephyr/issues/38675) - DTS binding create devicetree\_unfixed.h build error at v2.7.0
- [GitHub #38673](https://github.com/zephyrproject-rtos/zephyr/issues/38673) - DNS-SD library does not support `_services._dns-sd._udp.local` meta-query for service enumeration
- [GitHub #38668](https://github.com/zephyrproject-rtos/zephyr/issues/38668) - ESP32‘s I2S
- [GitHub #38667](https://github.com/zephyrproject-rtos/zephyr/issues/38667) - ST LSM6DSO polling mode does not work on nRF52dk\_nrf52832
- [GitHub #38655](https://github.com/zephyrproject-rtos/zephyr/issues/38655) - Failing Tests for Regulator API
- [GitHub #38653](https://github.com/zephyrproject-rtos/zephyr/issues/38653) - drivers: modem: gsm\_ppp: Add support for Quectel modems
- [GitHub #38646](https://github.com/zephyrproject-rtos/zephyr/issues/38646) - SIMD Rounding bug while running Assembly addps instruction on Zephyr
- [GitHub #38641](https://github.com/zephyrproject-rtos/zephyr/issues/38641) - Arm v8-M ‘\_ns’ renaming was applied inconsistently
- [GitHub #38635](https://github.com/zephyrproject-rtos/zephyr/issues/38635) - USDHC driver broken on RT10XX after 387e6a676f86c00d1f9ef018e4b2480e0bcad3c8 commit
- [GitHub #38622](https://github.com/zephyrproject-rtos/zephyr/issues/38622) - subsys/usb: CONFIG\_USB\_DEVICE\_STACK resulted in 10kb increase in firmware size
- [GitHub #38621](https://github.com/zephyrproject-rtos/zephyr/issues/38621) - Drivers: spi: stm32: Transceive lock forever
- [GitHub #38620](https://github.com/zephyrproject-rtos/zephyr/issues/38620) - STM32 uart driver prevent system to go to deep sleep
- [GitHub #38617](https://github.com/zephyrproject-rtos/zephyr/issues/38617) - HL7800 PSM not working as intended
- [GitHub #38613](https://github.com/zephyrproject-rtos/zephyr/issues/38613) - BLE connection parameters updated with inconsistent values
- [GitHub #38612](https://github.com/zephyrproject-rtos/zephyr/issues/38612) - Fault with assertions enabled prevents detailed output because of ISR() assertion check in shell function
- [GitHub #38602](https://github.com/zephyrproject-rtos/zephyr/issues/38602) - modem gsm
- [GitHub #38601](https://github.com/zephyrproject-rtos/zephyr/issues/38601) - nucleo\_f103rb: samples/posix/eventfd/ failed since “retargetable locking” addition
- [GitHub #38593](https://github.com/zephyrproject-rtos/zephyr/issues/38593) - using RTT console to print along with newlib C library in Zephyr
- [GitHub #38591](https://github.com/zephyrproject-rtos/zephyr/issues/38591) - nucleo\_f091rc: Linking issue since “align \_\_data\_ram/rom\_start/end linker” (65a2de84a9d5c535167951bf1cf610c4f7967ea5)
- [GitHub #38586](https://github.com/zephyrproject-rtos/zephyr/issues/38586) - olimexino\_stm32: “no DEVICE\_HANDLE\_ENDS inserted” builld issue (samples/subsys/usb/audio/headphones\_microphone)
- [GitHub #38581](https://github.com/zephyrproject-rtos/zephyr/issues/38581) - tests-ci : kernel: scheduler: multiq test failed
- [GitHub #38582](https://github.com/zephyrproject-rtos/zephyr/issues/38582) - tests-ci : kernel: scheduler: test failed
- [GitHub #38578](https://github.com/zephyrproject-rtos/zephyr/issues/38578) - STM32L0X ADC hangs
- [GitHub #38572](https://github.com/zephyrproject-rtos/zephyr/issues/38572) - Builds with macOS SDK are failing
- [GitHub #38571](https://github.com/zephyrproject-rtos/zephyr/issues/38571) - bug: drivers: ethernet: build as static library breaks frdm\_k64f gptp sample application
- [GitHub #38563](https://github.com/zephyrproject-rtos/zephyr/issues/38563) - ISO broadcast cannot send with callback if CONFIG\_BT\_CONN=n
- [GitHub #38560](https://github.com/zephyrproject-rtos/zephyr/issues/38560) - log v2 with 64-bit integers and threads causes invalid 64-bit value output
- [GitHub #38559](https://github.com/zephyrproject-rtos/zephyr/issues/38559) - Shell log backend may hang on qemu\_x86\_64
- [GitHub #38558](https://github.com/zephyrproject-rtos/zephyr/issues/38558) - CMake warning: CMP0079
- [GitHub #38554](https://github.com/zephyrproject-rtos/zephyr/issues/38554) - tests-ci : kernel: scheduler: test failed
- [GitHub #38552](https://github.com/zephyrproject-rtos/zephyr/issues/38552) - stm32: g0b1: garbage output in log and suspected hard fault when configuring modem
- [GitHub #38536](https://github.com/zephyrproject-rtos/zephyr/issues/38536) - samples: tests: display: Sample for display.ft800 causes end in timeout
- [GitHub #38535](https://github.com/zephyrproject-rtos/zephyr/issues/38535) - drivers: modem: bg9x: Kconfig values compiled into `autoconf.h` even if it isn’t being used
- [GitHub #38534](https://github.com/zephyrproject-rtos/zephyr/issues/38534) - lwm2m: add api to inspect observation state of resource/object
- [GitHub #38532](https://github.com/zephyrproject-rtos/zephyr/issues/38532) - samples: audio: tests: Twister fails on samples/drivers/audio/dmic
- [GitHub #38527](https://github.com/zephyrproject-rtos/zephyr/issues/38527) - lwm2m: re-register instead of removing observer on COAP reset answer to notification
- [GitHub #38520](https://github.com/zephyrproject-rtos/zephyr/issues/38520) - Bluetooth:Host:Scan: “bt\_le\_per\_adv\_list\_add” function doesn’t work
- [GitHub #38519](https://github.com/zephyrproject-rtos/zephyr/issues/38519) - stm32: g0b1re: Log/Shell subsys with serial uart buggy after #38432
- [GitHub #38516](https://github.com/zephyrproject-rtos/zephyr/issues/38516) - subsys: net: ip: packet\_socket: always returning of NET\_CONTINUE caused access to unreferred pkt and causing a crash/segmentation fault
- [GitHub #38514](https://github.com/zephyrproject-rtos/zephyr/issues/38514) - mqtt azure sample failing with net\_tcp “is waiting on connect semaphore”
- [GitHub #38512](https://github.com/zephyrproject-rtos/zephyr/issues/38512) - stm32f7: CAN: STM32F645VE CAN signal seems upside down.
- [GitHub #38500](https://github.com/zephyrproject-rtos/zephyr/issues/38500) - tests/kernel/device/kernel.device.pm fails to build on TI platforms
- [GitHub #38498](https://github.com/zephyrproject-rtos/zephyr/issues/38498) - net: ipv6: nbr\_lock not initialized with CONFIG\_NET\_IPV6\_ND=n
- [GitHub #38480](https://github.com/zephyrproject-rtos/zephyr/issues/38480) - Improve samples documentation
- [GitHub #38479](https://github.com/zephyrproject-rtos/zephyr/issues/38479) - “west flash” command exiting with error
- [GitHub #38477](https://github.com/zephyrproject-rtos/zephyr/issues/38477) - json: JSON Library Orphaned, Request to Become a Maintainer
- [GitHub #38474](https://github.com/zephyrproject-rtos/zephyr/issues/38474) - command exited with status 63: nrfjprog –ids
- [GitHub #38463](https://github.com/zephyrproject-rtos/zephyr/issues/38463) - check\_compliance gives very many Kconfig warnings
- [GitHub #38452](https://github.com/zephyrproject-rtos/zephyr/issues/38452) - Some STM32 series require CONFIG\_PM\_DEVICE if CONFIG\_PM=y
- [GitHub #38442](https://github.com/zephyrproject-rtos/zephyr/issues/38442) - test-ci: can: twr\_ke18f: all can driver test fails with BUS Fault
- [GitHub #38438](https://github.com/zephyrproject-rtos/zephyr/issues/38438) - test-ci: test\_flash\_map:twr\_ke18f: test failure
- [GitHub #38437](https://github.com/zephyrproject-rtos/zephyr/issues/38437) - stm32: g0b1re: Serial UART timing issue after MCU entered deep sleep
- [GitHub #38433](https://github.com/zephyrproject-rtos/zephyr/issues/38433) - gpio\_pin\_set not working on STM32 with CONFIG\_PM\_DEVICE\_RUNTIME
- [GitHub #38428](https://github.com/zephyrproject-rtos/zephyr/issues/38428) - http\_client response callback always reports final\_data == HTTP\_DATA\_FINAL
- [GitHub #38427](https://github.com/zephyrproject-rtos/zephyr/issues/38427) - mimxrt1050\_evk and mimxrt1020\_evk boards fail to boot some sample applications
- [GitHub #38421](https://github.com/zephyrproject-rtos/zephyr/issues/38421) - HardFault regression detected on Cortex-M0+ following Cortex-R introduction
- [GitHub #38418](https://github.com/zephyrproject-rtos/zephyr/issues/38418) - twister: Remove toolchain-depandat filter for native\_posix
- [GitHub #38417](https://github.com/zephyrproject-rtos/zephyr/issues/38417) - Add support for WeAct-F401CC board
- [GitHub #38414](https://github.com/zephyrproject-rtos/zephyr/issues/38414) - Build of http client fails if CONFIG\_POSIX\_API=y
- [GitHub #38405](https://github.com/zephyrproject-rtos/zephyr/issues/38405) - samples/philosophers/sample.kernel.philosopher.stacks fails on xtensa
- [GitHub #38403](https://github.com/zephyrproject-rtos/zephyr/issues/38403) - Cleanup `No SOURCES given to Zephyr library` warnings
- [GitHub #38402](https://github.com/zephyrproject-rtos/zephyr/issues/38402) - module: MCUboot module missing fixes available upstream
- [GitHub #38401](https://github.com/zephyrproject-rtos/zephyr/issues/38401) - Builds fail due to a proxy error by launchpadlibrarian
- [GitHub #38400](https://github.com/zephyrproject-rtos/zephyr/issues/38400) - mec15xxevb\_assy6853: arm\_ramfunc and arm\_sw\_vector\_relay tests timeout after the build
- [GitHub #38398](https://github.com/zephyrproject-rtos/zephyr/issues/38398) - DT\_N\_INST error for TMP116 sample
- [GitHub #38396](https://github.com/zephyrproject-rtos/zephyr/issues/38396) - RISC-V privilege SoC initialisation code skips the \_\_reset vector
- [GitHub #38382](https://github.com/zephyrproject-rtos/zephyr/issues/38382) - stm32 uart finishes Tx before going to PM
- [GitHub #38365](https://github.com/zephyrproject-rtos/zephyr/issues/38365) - drivers: gsm\_ppp: gsm\_ppp\_stop fails to lock tx\_sem after some time
- [GitHub #38362](https://github.com/zephyrproject-rtos/zephyr/issues/38362) - soc: ti cc13x2-cc26x2: PM standby + radio interaction regression
- [GitHub #38354](https://github.com/zephyrproject-rtos/zephyr/issues/38354) - stm32: stm32f10x JTAG realated gpio repmap didn’t works
- [GitHub #38351](https://github.com/zephyrproject-rtos/zephyr/issues/38351) - Custom radio protocol
- [GitHub #38349](https://github.com/zephyrproject-rtos/zephyr/issues/38349) - XCC compilation fails on Intel cAVS platforms
- [GitHub #38348](https://github.com/zephyrproject-rtos/zephyr/issues/38348) - Bluetooth: Switch to inclusive terminology from the 5.3 specification
- [GitHub #38340](https://github.com/zephyrproject-rtos/zephyr/issues/38340) - Bluetooth:DirectionFinding: Disabling the MPU causes some compilation errors
- [GitHub #38332](https://github.com/zephyrproject-rtos/zephyr/issues/38332) - stm32g0: power hooks should be define as weak
- [GitHub #38323](https://github.com/zephyrproject-rtos/zephyr/issues/38323) - Can not generate code coverage report by running samples/subsys/tracing
- [GitHub #38316](https://github.com/zephyrproject-rtos/zephyr/issues/38316) - Synchronize multiple DF TX devices in the DF Connectionless RX Example “Periodic Advertising list”
- [GitHub #38309](https://github.com/zephyrproject-rtos/zephyr/issues/38309) - ARC context switch to interrupted thread busted with CONFIG\_ARC\_FIRQ=y and CONFIG\_NUM\_IRQ\_PRIO\_LEVELS=1
- [GitHub #38303](https://github.com/zephyrproject-rtos/zephyr/issues/38303) - The current BabbleSim tests build system based on bash scripts hides warnings
- [GitHub #38290](https://github.com/zephyrproject-rtos/zephyr/issues/38290) - net\_buf\_add\_mem() hard-faults when adding buffer from external SDRAM
- [GitHub #38279](https://github.com/zephyrproject-rtos/zephyr/issues/38279) - Bluetooth: Controller: assert LL\_ASSERT(!radio\_is\_ready()) in lll\_conn.c
- [GitHub #38277](https://github.com/zephyrproject-rtos/zephyr/issues/38277) - soc: stm32h7: Fails to boot with LDO power supply, if soc has SMPS support.
- [GitHub #38276](https://github.com/zephyrproject-rtos/zephyr/issues/38276) - LwM2M: RD Client: Wrong state if registration fails
- [GitHub #38273](https://github.com/zephyrproject-rtos/zephyr/issues/38273) - Support UART4 on STM32F303Xe
- [GitHub #38272](https://github.com/zephyrproject-rtos/zephyr/issues/38272) - “west flash” stopped working
- [GitHub #38271](https://github.com/zephyrproject-rtos/zephyr/issues/38271) - Expose emulator\_get\_binding function
- [GitHub #38264](https://github.com/zephyrproject-rtos/zephyr/issues/38264) - Modbus over RS485 on samd21g18a re-gpios turning on 1 byte too early
- [GitHub #38259](https://github.com/zephyrproject-rtos/zephyr/issues/38259) - subsys/shell: `[JJ` escape codes in logs after disabling colors
- [GitHub #38258](https://github.com/zephyrproject-rtos/zephyr/issues/38258) - newlib: first malloc call may fail on Xtensa depending on image size
- [GitHub #38246](https://github.com/zephyrproject-rtos/zephyr/issues/38246) - samples: drivers: flash\_shell: fails on arduino\_due due to compilation issue
- [GitHub #38245](https://github.com/zephyrproject-rtos/zephyr/issues/38245) - board: bl654\_usb project: samples/basic/blinky does not blink LED
- [GitHub #38240](https://github.com/zephyrproject-rtos/zephyr/issues/38240) - Connected ISO does not disconnect gracefully
- [GitHub #38237](https://github.com/zephyrproject-rtos/zephyr/issues/38237) - [backport v2.6-branch] backport of #37479 failed
- [GitHub #38235](https://github.com/zephyrproject-rtos/zephyr/issues/38235) - Please add stm32h723Xe.dtsi to dts/arm/st/h7/
- [GitHub #38234](https://github.com/zephyrproject-rtos/zephyr/issues/38234) - Newlib retargetable lock init fails on qemu\_xtensa
- [GitHub #38233](https://github.com/zephyrproject-rtos/zephyr/issues/38233) - Build newlib function read() and write() failed when enable userspace
- [GitHub #38219](https://github.com/zephyrproject-rtos/zephyr/issues/38219) - kernel: Z\_MEM\_SLAB\_INITIALIZER MACRO not compatible with C++
- [GitHub #38216](https://github.com/zephyrproject-rtos/zephyr/issues/38216) - nxp\_adsp\_imx8 fails to build a number of tests
- [GitHub #38214](https://github.com/zephyrproject-rtos/zephyr/issues/38214) - xtensa builds fail in CI due to running out of ram to link
- [GitHub #38207](https://github.com/zephyrproject-rtos/zephyr/issues/38207) - Use of unaligned noinit data hangs qemu\_arc\_hs
- [GitHub #38202](https://github.com/zephyrproject-rtos/zephyr/issues/38202) - mbedtls and littlefs on a STM32L4
- [GitHub #38197](https://github.com/zephyrproject-rtos/zephyr/issues/38197) - Invalid NULL check for `iso` in bt\_iso\_connected
- [GitHub #38196](https://github.com/zephyrproject-rtos/zephyr/issues/38196) - net nbr command might crash
- [GitHub #38191](https://github.com/zephyrproject-rtos/zephyr/issues/38191) - Unable to connect multiple MQTT clients
- [GitHub #38186](https://github.com/zephyrproject-rtos/zephyr/issues/38186) - i.MX RT10xx boards fail to initialize when Ethernet is enabled
- [GitHub #38181](https://github.com/zephyrproject-rtos/zephyr/issues/38181) - tests/drivers/uart/uart\_basic\_api/drivers.uart.cdc\_acm fails to build
- [GitHub #38177](https://github.com/zephyrproject-rtos/zephyr/issues/38177) - LORA Module crashes SHT3XD sensor.
- [GitHub #38173](https://github.com/zephyrproject-rtos/zephyr/issues/38173) - STM32WB: Low power modes entry blocked by C2 when CONFIG\_BLE=n
- [GitHub #38172](https://github.com/zephyrproject-rtos/zephyr/issues/38172) - modem\_context\_sprint\_ip\_addr returns pointer to stack array
- [GitHub #38170](https://github.com/zephyrproject-rtos/zephyr/issues/38170) - Shell argument in second position containing a question mark is ignored
- [GitHub #38168](https://github.com/zephyrproject-rtos/zephyr/issues/38168) - aarch32: flags value collision between base IRQ layer and GIC interrupt controller driver
- [GitHub #38162](https://github.com/zephyrproject-rtos/zephyr/issues/38162) - Upgrade to 2.6 GPIO device\_get\_binding(“GPIO\_0”) now returns null
- [GitHub #38154](https://github.com/zephyrproject-rtos/zephyr/issues/38154) - Error building example i2c\_fujitsu\_fram
- [GitHub #38153](https://github.com/zephyrproject-rtos/zephyr/issues/38153) - Zephyr Native POSIX select() implementation too frequent wakeup on pure timeout based use
- [GitHub #38145](https://github.com/zephyrproject-rtos/zephyr/issues/38145) - [backport v2.6-branch] backport of #37787 failed
- [GitHub #38144](https://github.com/zephyrproject-rtos/zephyr/issues/38144) - [backport v2.6-branch] backport of #37787 failed
- [GitHub #38141](https://github.com/zephyrproject-rtos/zephyr/issues/38141) - Wrong output from printk() with CONFIG\_CBPRINTF\_NANO=y
- [GitHub #38138](https://github.com/zephyrproject-rtos/zephyr/issues/38138) - [Coverity CID: 239554] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_msg2.h (Generated Code)
- [GitHub #38137](https://github.com/zephyrproject-rtos/zephyr/issues/38137) - [Coverity CID: 239555] Unchecked return value in subsys/mgmt/hawkbit/hawkbit.c
- [GitHub #38136](https://github.com/zephyrproject-rtos/zephyr/issues/38136) - [Coverity CID: 239557] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #38135](https://github.com/zephyrproject-rtos/zephyr/issues/38135) - [Coverity CID: 239560] Out-of-bounds access in subsys/modbus/modbus\_core.c
- [GitHub #38134](https://github.com/zephyrproject-rtos/zephyr/issues/38134) - [Coverity CID: 239563] Logically dead code in subsys/bluetooth/host/id.c
- [GitHub #38133](https://github.com/zephyrproject-rtos/zephyr/issues/38133) - [Coverity CID: 239564] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll.c
- [GitHub #38132](https://github.com/zephyrproject-rtos/zephyr/issues/38132) - [Coverity CID: 239565] Unchecked return value in drivers/sensor/adxl372/adxl372\_trigger.c
- [GitHub #38131](https://github.com/zephyrproject-rtos/zephyr/issues/38131) - [Coverity CID: 239568] Out-of-bounds access in subsys/modbus/modbus\_core.c
- [GitHub #38130](https://github.com/zephyrproject-rtos/zephyr/issues/38130) - [Coverity CID: 239569] Out-of-bounds access in subsys/bluetooth/host/id.c
- [GitHub #38129](https://github.com/zephyrproject-rtos/zephyr/issues/38129) - [Coverity CID: 239572] Out-of-bounds read in /zephyr/include/generated/syscalls/kernel.h (Generated Code)
- [GitHub #38127](https://github.com/zephyrproject-rtos/zephyr/issues/38127) - [Coverity CID: 239579] Logically dead code in drivers/flash/nrf\_qspi\_nor.c
- [GitHub #38126](https://github.com/zephyrproject-rtos/zephyr/issues/38126) - [Coverity CID: 239581] Out-of-bounds access in subsys/modbus/modbus\_core.c
- [GitHub #38125](https://github.com/zephyrproject-rtos/zephyr/issues/38125) - [Coverity CID: 239582] Unchecked return value in drivers/display/ssd1306.c
- [GitHub #38124](https://github.com/zephyrproject-rtos/zephyr/issues/38124) - [Coverity CID: 239583] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll.c
- [GitHub #38123](https://github.com/zephyrproject-rtos/zephyr/issues/38123) - [Coverity CID: 239584] Improper use of negative value in subsys/logging/log\_msg2.c
- [GitHub #38122](https://github.com/zephyrproject-rtos/zephyr/issues/38122) - [Coverity CID: 239585] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll.c
- [GitHub #38121](https://github.com/zephyrproject-rtos/zephyr/issues/38121) - [Coverity CID: 239586] Side effect in assertion in subsys/bluetooth/controller/ll\_sw/nordic/lll/lll.c
- [GitHub #38120](https://github.com/zephyrproject-rtos/zephyr/issues/38120) - [Coverity CID: 239588] Unchecked return value in subsys/bluetooth/host/id.c
- [GitHub #38119](https://github.com/zephyrproject-rtos/zephyr/issues/38119) - [Coverity CID: 239592] Dereference before null check in subsys/ipc/rpmsg\_multi\_instance/rpmsg\_multi\_instance.c
- [GitHub #38118](https://github.com/zephyrproject-rtos/zephyr/issues/38118) - [Coverity CID: 239597] Explicit null dereferenced in tests/net/context/src/main.c
- [GitHub #38117](https://github.com/zephyrproject-rtos/zephyr/issues/38117) - [Coverity CID: 239598] Unchecked return value in drivers/sensor/adxl362/adxl362\_trigger.c
- [GitHub #38116](https://github.com/zephyrproject-rtos/zephyr/issues/38116) - [Coverity CID: 239601] Untrusted loop bound in subsys/bluetooth/host/sdp.c
- [GitHub #38115](https://github.com/zephyrproject-rtos/zephyr/issues/38115) - [Coverity CID: 239605] Logically dead code in drivers/flash/nrf\_qspi\_nor.c
- [GitHub #38114](https://github.com/zephyrproject-rtos/zephyr/issues/38114) - [Coverity CID: 239607] Missing break in switch in subsys/usb/class/dfu/usb\_dfu.c
- [GitHub #38113](https://github.com/zephyrproject-rtos/zephyr/issues/38113) - [Coverity CID: 239609] Out-of-bounds access in subsys/random/rand32\_ctr\_drbg.c
- [GitHub #38112](https://github.com/zephyrproject-rtos/zephyr/issues/38112) - [Coverity CID: 239612] Out-of-bounds read in /zephyr/include/generated/syscalls/log\_ctrl.h (Generated Code)
- [GitHub #38111](https://github.com/zephyrproject-rtos/zephyr/issues/38111) - [Coverity CID: 239615] Out-of-bounds access in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #38110](https://github.com/zephyrproject-rtos/zephyr/issues/38110) - [Coverity CID: 239619] Out-of-bounds access in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #38109](https://github.com/zephyrproject-rtos/zephyr/issues/38109) - [Coverity CID: 239623] Out-of-bounds access in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #38108](https://github.com/zephyrproject-rtos/zephyr/issues/38108) - nxp: usb driver build failure due to d92d1f162af3ba24963f1026fc0a304f1a44d1f3
- [GitHub #38104](https://github.com/zephyrproject-rtos/zephyr/issues/38104) - kheap buffer own section attribute causing memory overflow in ESP32
- [GitHub #38101](https://github.com/zephyrproject-rtos/zephyr/issues/38101) - bt\_le\_adv\_update\_data() assertion fail
- [GitHub #38093](https://github.com/zephyrproject-rtos/zephyr/issues/38093) - preempt\_cnt not reset in each test case in tests/lib/ringbuffer/libraries.data\_structures
- [GitHub #38090](https://github.com/zephyrproject-rtos/zephyr/issues/38090) - LPS22HH: int32\_t overflow in pressure calculations
- [GitHub #38082](https://github.com/zephyrproject-rtos/zephyr/issues/38082) - Hawkbit (http request) and MQTT can’t seem to work together
- [GitHub #38078](https://github.com/zephyrproject-rtos/zephyr/issues/38078) - RT6XX I2S test fails after d92d1f162af3ba24963f1026fc0a304f1a44d1f3
- [GitHub #38069](https://github.com/zephyrproject-rtos/zephyr/issues/38069) - stm32h747i\_disco M4 not working following merge of 9fa5437447712eece9c88e728ac05ac10fb01c4a
- [GitHub #38065](https://github.com/zephyrproject-rtos/zephyr/issues/38065) - Bluetooth: Direction Finding: Compiler warning when included in other header files
- [GitHub #38059](https://github.com/zephyrproject-rtos/zephyr/issues/38059) - automount configuration in nrf52840dk\_nrf52840.overlay causes error: mount point already exists!! in subsys/fs/littlefs sample
- [GitHub #38054](https://github.com/zephyrproject-rtos/zephyr/issues/38054) - Bluetooth: host: Local Host terminated but send host number of completed Packed
- [GitHub #38047](https://github.com/zephyrproject-rtos/zephyr/issues/38047) - twister: The –board-root parameter doesn’t appear to work
- [GitHub #38046](https://github.com/zephyrproject-rtos/zephyr/issues/38046) - twister: The –device-serial only works at 115200 baud
- [GitHub #38044](https://github.com/zephyrproject-rtos/zephyr/issues/38044) - tests: newlib: Scenarios from tests/lib/newlib/thread\_safety fail on nrf9160dk\_nrf9160\_ns
- [GitHub #38031](https://github.com/zephyrproject-rtos/zephyr/issues/38031) - STM32WB - Problem with data reception on LPUART when PM and LPTIM are enabled
- [GitHub #38026](https://github.com/zephyrproject-rtos/zephyr/issues/38026) - boards: bl654\_usb: does not support samples/bluetooth/hci\_uart
- [GitHub #38022](https://github.com/zephyrproject-rtos/zephyr/issues/38022) - thread: k\_float\_enable() API can’t build on x86\_64 platforms, fix that API and macro documentation
- [GitHub #38019](https://github.com/zephyrproject-rtos/zephyr/issues/38019) - nsim\_sem\_mpu\_stack\_guard board can’t run
- [GitHub #38017](https://github.com/zephyrproject-rtos/zephyr/issues/38017) - [Coverity CID: 237063] Untrusted value as argument in tests/net/lib/coap/src/main.c
- [GitHub #38016](https://github.com/zephyrproject-rtos/zephyr/issues/38016) - [Coverity CID: 238375] Uninitialized pointer read in subsys/bluetooth/mesh/shell.c
- [GitHub #38015](https://github.com/zephyrproject-rtos/zephyr/issues/38015) - [Coverity CID: 237072] Uninitialized pointer read in subsys/bluetooth/controller/ll\_sw/ull\_adv\_aux.c
- [GitHub #38014](https://github.com/zephyrproject-rtos/zephyr/issues/38014) - [Coverity CID: 237071] Unexpected control flow in subsys/bluetooth/host/keys.c
- [GitHub #38013](https://github.com/zephyrproject-rtos/zephyr/issues/38013) - [Coverity CID: 237070] Unchecked return value in subsys/bluetooth/shell/gatt.c
- [GitHub #38012](https://github.com/zephyrproject-rtos/zephyr/issues/38012) - [Coverity CID: 236654] Unchecked return value in subsys/bluetooth/host/gatt.c
- [GitHub #38011](https://github.com/zephyrproject-rtos/zephyr/issues/38011) - [Coverity CID: 236653] Unchecked return value in drivers/sensor/bmi160/bmi160\_trigger.c
- [GitHub #38010](https://github.com/zephyrproject-rtos/zephyr/issues/38010) - [Coverity CID: 236652] Unchecked return value in drivers/sensor/fxas21002/fxas21002\_trigger.c
- [GitHub #38009](https://github.com/zephyrproject-rtos/zephyr/issues/38009) - [Coverity CID: 236651] Unchecked return value in drivers/sensor/bmg160/bmg160\_trigger.c
- [GitHub #38008](https://github.com/zephyrproject-rtos/zephyr/issues/38008) - [Coverity CID: 236650] Unchecked return value in drivers/sensor/fxos8700/fxos8700\_trigger.c
- [GitHub #38007](https://github.com/zephyrproject-rtos/zephyr/issues/38007) - [Coverity CID: 236649] Unchecked return value in drivers/sensor/adt7420/adt7420\_trigger.c
- [GitHub #38006](https://github.com/zephyrproject-rtos/zephyr/issues/38006) - [Coverity CID: 236648] Unchecked return value in drivers/sensor/sx9500/sx9500\_trigger.c
- [GitHub #38005](https://github.com/zephyrproject-rtos/zephyr/issues/38005) - [Coverity CID: 236647] Unchecked return value in drivers/sensor/bmp388/bmp388\_trigger.c
- [GitHub #38004](https://github.com/zephyrproject-rtos/zephyr/issues/38004) - [Coverity CID: 238360] Result is not floating-point in drivers/sensor/sgp40/sgp40.c
- [GitHub #38003](https://github.com/zephyrproject-rtos/zephyr/issues/38003) - [Coverity CID: 238343] Result is not floating-point in drivers/sensor/sgp40/sgp40.c
- [GitHub #38002](https://github.com/zephyrproject-rtos/zephyr/issues/38002) - [Coverity CID: 237060] Out-of-bounds access in subsys/bluetooth/host/gatt.c
- [GitHub #38001](https://github.com/zephyrproject-rtos/zephyr/issues/38001) - [Coverity CID: 238371] Negative array index read in tests/lib/cbprintf\_package/src/test.inc
- [GitHub #38000](https://github.com/zephyrproject-rtos/zephyr/issues/38000) - [Coverity CID: 238347] Negative array index read in tests/lib/cbprintf\_package/src/test.inc
- [GitHub #37999](https://github.com/zephyrproject-rtos/zephyr/issues/37999) - [Coverity CID: 238383] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37998](https://github.com/zephyrproject-rtos/zephyr/issues/37998) - [Coverity CID: 238381] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37997](https://github.com/zephyrproject-rtos/zephyr/issues/37997) - [Coverity CID: 238380] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37996](https://github.com/zephyrproject-rtos/zephyr/issues/37996) - [Coverity CID: 238379] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37995](https://github.com/zephyrproject-rtos/zephyr/issues/37995) - [Coverity CID: 238378] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37994](https://github.com/zephyrproject-rtos/zephyr/issues/37994) - [Coverity CID: 238377] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37993](https://github.com/zephyrproject-rtos/zephyr/issues/37993) - [Coverity CID: 238376] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37992](https://github.com/zephyrproject-rtos/zephyr/issues/37992) - [Coverity CID: 238374] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37991](https://github.com/zephyrproject-rtos/zephyr/issues/37991) - [Coverity CID: 238373] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37990](https://github.com/zephyrproject-rtos/zephyr/issues/37990) - [Coverity CID: 238372] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37989](https://github.com/zephyrproject-rtos/zephyr/issues/37989) - [Coverity CID: 238370] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37988](https://github.com/zephyrproject-rtos/zephyr/issues/37988) - [Coverity CID: 238369] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37987](https://github.com/zephyrproject-rtos/zephyr/issues/37987) - [Coverity CID: 238368] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37986](https://github.com/zephyrproject-rtos/zephyr/issues/37986) - [Coverity CID: 238367] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37985](https://github.com/zephyrproject-rtos/zephyr/issues/37985) - [Coverity CID: 238366] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37984](https://github.com/zephyrproject-rtos/zephyr/issues/37984) - [Coverity CID: 238364] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37983](https://github.com/zephyrproject-rtos/zephyr/issues/37983) - [Coverity CID: 238363] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37982](https://github.com/zephyrproject-rtos/zephyr/issues/37982) - [Coverity CID: 238362] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37981](https://github.com/zephyrproject-rtos/zephyr/issues/37981) - [Coverity CID: 238361] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37980](https://github.com/zephyrproject-rtos/zephyr/issues/37980) - [Coverity CID: 238359] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37979](https://github.com/zephyrproject-rtos/zephyr/issues/37979) - [Coverity CID: 238358] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37978](https://github.com/zephyrproject-rtos/zephyr/issues/37978) - [Coverity CID: 238357] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37977](https://github.com/zephyrproject-rtos/zephyr/issues/37977) - [Coverity CID: 238356] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37976](https://github.com/zephyrproject-rtos/zephyr/issues/37976) - [Coverity CID: 238355] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37975](https://github.com/zephyrproject-rtos/zephyr/issues/37975) - [Coverity CID: 238354] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37974](https://github.com/zephyrproject-rtos/zephyr/issues/37974) - [Coverity CID: 238353] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37973](https://github.com/zephyrproject-rtos/zephyr/issues/37973) - [Coverity CID: 238352] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37972](https://github.com/zephyrproject-rtos/zephyr/issues/37972) - [Coverity CID: 238351] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37971](https://github.com/zephyrproject-rtos/zephyr/issues/37971) - [Coverity CID: 238350] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37970](https://github.com/zephyrproject-rtos/zephyr/issues/37970) - [Coverity CID: 238349] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37969](https://github.com/zephyrproject-rtos/zephyr/issues/37969) - [Coverity CID: 238348] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37968](https://github.com/zephyrproject-rtos/zephyr/issues/37968) - [Coverity CID: 238346] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37967](https://github.com/zephyrproject-rtos/zephyr/issues/37967) - [Coverity CID: 238345] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37966](https://github.com/zephyrproject-rtos/zephyr/issues/37966) - [Coverity CID: 238344] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37965](https://github.com/zephyrproject-rtos/zephyr/issues/37965) - [Coverity CID: 238342] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37964](https://github.com/zephyrproject-rtos/zephyr/issues/37964) - [Coverity CID: 238341] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37963](https://github.com/zephyrproject-rtos/zephyr/issues/37963) - [Coverity CID: 238340] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37962](https://github.com/zephyrproject-rtos/zephyr/issues/37962) - [Coverity CID: 238339] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37961](https://github.com/zephyrproject-rtos/zephyr/issues/37961) - [Coverity CID: 238337] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37960](https://github.com/zephyrproject-rtos/zephyr/issues/37960) - [Coverity CID: 238336] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37959](https://github.com/zephyrproject-rtos/zephyr/issues/37959) - [Coverity CID: 238335] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37958](https://github.com/zephyrproject-rtos/zephyr/issues/37958) - [Coverity CID: 238334] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37957](https://github.com/zephyrproject-rtos/zephyr/issues/37957) - [Coverity CID: 238333] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37956](https://github.com/zephyrproject-rtos/zephyr/issues/37956) - [Coverity CID: 238332] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37955](https://github.com/zephyrproject-rtos/zephyr/issues/37955) - [Coverity CID: 238331] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37954](https://github.com/zephyrproject-rtos/zephyr/issues/37954) - [Coverity CID: 238330] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37953](https://github.com/zephyrproject-rtos/zephyr/issues/37953) - [Coverity CID: 238328] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37952](https://github.com/zephyrproject-rtos/zephyr/issues/37952) - [Coverity CID: 238327] Logically dead code in tests/bluetooth/tester/src/mesh.c
- [GitHub #37951](https://github.com/zephyrproject-rtos/zephyr/issues/37951) - [Coverity CID: 238365] Logical vs. bitwise operator in drivers/i2s/i2s\_nrfx.c
- [GitHub #37950](https://github.com/zephyrproject-rtos/zephyr/issues/37950) - [Coverity CID: 237067] Division or modulo by zero in tests/benchmarks/latency\_measure/src/heap\_malloc\_free.c
- [GitHub #37949](https://github.com/zephyrproject-rtos/zephyr/issues/37949) - [Coverity CID: 238382] Dereference before null check in subsys/bluetooth/mesh/cfg\_cli.c
- [GitHub #37948](https://github.com/zephyrproject-rtos/zephyr/issues/37948) - [Coverity CID: 238338] Dereference before null check in subsys/bluetooth/mesh/cfg\_cli.c
- [GitHub #37947](https://github.com/zephyrproject-rtos/zephyr/issues/37947) - [Coverity CID: 237069] Dereference before null check in subsys/bluetooth/host/att.c
- [GitHub #37946](https://github.com/zephyrproject-rtos/zephyr/issues/37946) - [Coverity CID: 237066] Calling risky function in tests/lib/c\_lib/src/main.c
- [GitHub #37945](https://github.com/zephyrproject-rtos/zephyr/issues/37945) - [Coverity CID: 237064] Calling risky function in tests/lib/c\_lib/src/main.c
- [GitHub #37944](https://github.com/zephyrproject-rtos/zephyr/issues/37944) - [Coverity CID: 237062] Calling risky function in tests/lib/c\_lib/src/main.c
- [GitHub #37940](https://github.com/zephyrproject-rtos/zephyr/issues/37940) - Unconsistent UART ASYNC API
- [GitHub #37927](https://github.com/zephyrproject-rtos/zephyr/issues/37927) - tests-ci: net-lib: test/net/lib : build missing drivers\_\_net and application has no console output
- [GitHub #37916](https://github.com/zephyrproject-rtos/zephyr/issues/37916) - [Coverity CID :219656] Uninitialized scalar variable in file /tests/kernel/threads/thread\_stack/src/main.c
- [GitHub #37915](https://github.com/zephyrproject-rtos/zephyr/issues/37915) - led\_pwm driver not generating correct linker symbol
- [GitHub #37896](https://github.com/zephyrproject-rtos/zephyr/issues/37896) - samples: bluetooth: mesh: build failed for native posix
- [GitHub #37876](https://github.com/zephyrproject-rtos/zephyr/issues/37876) - Execution of twister in makefile environment
- [GitHub #37865](https://github.com/zephyrproject-rtos/zephyr/issues/37865) - nRF Battery measurement issue
- [GitHub #37861](https://github.com/zephyrproject-rtos/zephyr/issues/37861) - tests/lib/ringbuffer failed on ARC boards
- [GitHub #37856](https://github.com/zephyrproject-rtos/zephyr/issues/37856) - tests: arm: uninitialized FPSCR
- [GitHub #37852](https://github.com/zephyrproject-rtos/zephyr/issues/37852) - RISC-V machine timer time-keeping question
- [GitHub #37850](https://github.com/zephyrproject-rtos/zephyr/issues/37850) - Provide macros for switching off Zephyr kernel version
- [GitHub #37842](https://github.com/zephyrproject-rtos/zephyr/issues/37842) - TCP2 statemachine gets stuck in TCP\_FIN\_WAIT\_2 state
- [GitHub #37839](https://github.com/zephyrproject-rtos/zephyr/issues/37839) - SX1272 LoRa driver is broken and fails to build
- [GitHub #37838](https://github.com/zephyrproject-rtos/zephyr/issues/37838) - cmake 3.20 not supported (yet) by recent Ubuntu
- [GitHub #37830](https://github.com/zephyrproject-rtos/zephyr/issues/37830) - intel\_adsp\_cavs15: run queue testcases failed on ADSP
- [GitHub #37827](https://github.com/zephyrproject-rtos/zephyr/issues/37827) - stm32h747i\_disco M4 not working, if use large size(>1KB) global array
- [GitHub #37821](https://github.com/zephyrproject-rtos/zephyr/issues/37821) - pm: `pm_device_request` incorrectly returns errors
- [GitHub #37797](https://github.com/zephyrproject-rtos/zephyr/issues/37797) - Merge vendor-prefixes.txt from all modules with build.settings.dts\_root in zephyr/module.yml
- [GitHub #37790](https://github.com/zephyrproject-rtos/zephyr/issues/37790) - Bluetooth: host: Confusion about periodic advertising interval
- [GitHub #37786](https://github.com/zephyrproject-rtos/zephyr/issues/37786) - Example for tca9546a multiplexor driver
- [GitHub #37784](https://github.com/zephyrproject-rtos/zephyr/issues/37784) - MPU6050 accel and gyro values swapped
- [GitHub #37781](https://github.com/zephyrproject-rtos/zephyr/issues/37781) - nucleo\_l496zg lpuart1 driver not working
- [GitHub #37779](https://github.com/zephyrproject-rtos/zephyr/issues/37779) - adc sam0 interrupt mapping, RESRDY maps to second interrupt in samd5x.dtsi
- [GitHub #37772](https://github.com/zephyrproject-rtos/zephyr/issues/37772) - samples: subsys: usb: mass: Use &flash0 storage\_partition for USB mass storage
- [GitHub #37768](https://github.com/zephyrproject-rtos/zephyr/issues/37768) - tests/lib/ringbuffer/libraries.data\_structures fails to build on number of platforms due to CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC=100000
- [GitHub #37765](https://github.com/zephyrproject-rtos/zephyr/issues/37765) - cmake: multiple `No SOURCES given to Zephyr library:` warnings
- [GitHub #37746](https://github.com/zephyrproject-rtos/zephyr/issues/37746) - qemu\_x86\_64 fails samples/hello\_world/sample.basic.helloworld.uefi in CI
- [GitHub #37735](https://github.com/zephyrproject-rtos/zephyr/issues/37735) - Unsigned types are incorrectly serialized when TLV format is used in LWM2M response
- [GitHub #37734](https://github.com/zephyrproject-rtos/zephyr/issues/37734) - xtensa xcc build spi\_nor.c fail
- [GitHub #37720](https://github.com/zephyrproject-rtos/zephyr/issues/37720) - net: dtls: received close\_notify alerts are not properly handled by DTLS client sockets
- [GitHub #37718](https://github.com/zephyrproject-rtos/zephyr/issues/37718) - Incompatible (u)intptr\_t type and PRIxPTR definitions
- [GitHub #37709](https://github.com/zephyrproject-rtos/zephyr/issues/37709) - x86 PCIe ECAM does not work as expected
- [GitHub #37701](https://github.com/zephyrproject-rtos/zephyr/issues/37701) - stm32: conflicts with uart serial DMA
- [GitHub #37696](https://github.com/zephyrproject-rtos/zephyr/issues/37696) - Modbus TCP: wrong transaction id in response
- [GitHub #37694](https://github.com/zephyrproject-rtos/zephyr/issues/37694) - Update CMSIS-DSP version to 1.9.0 (CMSIS 5.8.0)
- [GitHub #37693](https://github.com/zephyrproject-rtos/zephyr/issues/37693) - Update CMSIS-Core version to 5.5.0 (CMSIS 5.8.0)
- [GitHub #37691](https://github.com/zephyrproject-rtos/zephyr/issues/37691) - samples/subsys/canbus/isotp/sample.subsys.canbus.isotp fails to build on mimxrt1170\_evk\_cm7
- [GitHub #37687](https://github.com/zephyrproject-rtos/zephyr/issues/37687) - Support MVE on ARMv8.1-M
- [GitHub #37684](https://github.com/zephyrproject-rtos/zephyr/issues/37684) - Add State Machine Framework to Zephyr
- [GitHub #37676](https://github.com/zephyrproject-rtos/zephyr/issues/37676) - tests/kernel/device/kernel.device.pm (and tests/subsys/pm/power\_mgmt/subsys.pm.device\_pm) fails to build on mec172xevb\_assy6906 & mec1501modular\_assy6885
- [GitHub #37675](https://github.com/zephyrproject-rtos/zephyr/issues/37675) - tests/kernel/device/kernel.device.pm fails on bt510/bt6x0
- [GitHub #37672](https://github.com/zephyrproject-rtos/zephyr/issues/37672) - Board qemu\_x86 is no longer working with shell
- [GitHub #37665](https://github.com/zephyrproject-rtos/zephyr/issues/37665) - File system: wrong type for ssize\_t in fs.h for CONFIG\_ARCH\_POSIX
- [GitHub #37660](https://github.com/zephyrproject-rtos/zephyr/issues/37660) - Changing zephyr,console requires a clean build
- [GitHub #37658](https://github.com/zephyrproject-rtos/zephyr/issues/37658) - samples: boards/stm32/backup\_sram : needs backup sram enabled in DT to properly display memory region
- [GitHub #37652](https://github.com/zephyrproject-rtos/zephyr/issues/37652) - bluetooth: tests/bluetooth/bsim\_bt/bsim\_test\_advx reported success but still reported failed.
- [GitHub #37637](https://github.com/zephyrproject-rtos/zephyr/issues/37637) - Infinite configuring loop for samplesdriversled\_ws2812 sample
- [GitHub #37619](https://github.com/zephyrproject-rtos/zephyr/issues/37619) - RT6xx TRNG reports error on first request after reset
- [GitHub #37611](https://github.com/zephyrproject-rtos/zephyr/issues/37611) - Bluetooth: host: Implement L2CAP ecred reconfiguration request as initiator
- [GitHub #37610](https://github.com/zephyrproject-rtos/zephyr/issues/37610) - subsys/mgmt/hawkbit: Unable to parse json if the payload is split into 2 packets
- [GitHub #37600](https://github.com/zephyrproject-rtos/zephyr/issues/37600) - Invalidate TLB after ptables swap
- [GitHub #37597](https://github.com/zephyrproject-rtos/zephyr/issues/37597) - samples: bluetooth: scan\_adv
- [GitHub #37586](https://github.com/zephyrproject-rtos/zephyr/issues/37586) - get\_maintainer.py is broken
- [GitHub #37581](https://github.com/zephyrproject-rtos/zephyr/issues/37581) - Bluetooth: controller: radio: Change CTE configuration method
- [GitHub #37579](https://github.com/zephyrproject-rtos/zephyr/issues/37579) - PWM: Issue compiling project when CONFIG\_PWM and CONFIG\_PWM\_SAM is used with SAME70
- [GitHub #37571](https://github.com/zephyrproject-rtos/zephyr/issues/37571) - Bluetooth: Extended advertising assertion
- [GitHub #37556](https://github.com/zephyrproject-rtos/zephyr/issues/37556) - Schedule or timeline of LE audio in zephyr
- [GitHub #37547](https://github.com/zephyrproject-rtos/zephyr/issues/37547) - Bluetooth: Direction Finding: Channel index of received CTE packet is incorrect
- [GitHub #37544](https://github.com/zephyrproject-rtos/zephyr/issues/37544) - Change partition name using .overlay
- [GitHub #37543](https://github.com/zephyrproject-rtos/zephyr/issues/37543) - Using STM32Cube HAL function results in linker error
- [GitHub #37536](https://github.com/zephyrproject-rtos/zephyr/issues/37536) - \_pm\_devices() skips the very first device in the list and suspend() is not called.
- [GitHub #37530](https://github.com/zephyrproject-rtos/zephyr/issues/37530) - arc smp build failed with mwdt toolchain.
- [GitHub #37527](https://github.com/zephyrproject-rtos/zephyr/issues/37527) - Replace mqtt-azure example with azure-sdk-for-c
- [GitHub #37526](https://github.com/zephyrproject-rtos/zephyr/issues/37526) - ehl\_crb: edac tests are failing
- [GitHub #37520](https://github.com/zephyrproject-rtos/zephyr/issues/37520) - Is zephyr can run syscall or extrenal program
- [GitHub #37519](https://github.com/zephyrproject-rtos/zephyr/issues/37519) - friend.c:unseg\_app\_sdu\_decrypt causes assert: net\_buf\_simple\_tailfroom(buf) >= len when payload + opcode is 10 or 11 bytes long
- [GitHub #37515](https://github.com/zephyrproject-rtos/zephyr/issues/37515) - drivers: flash\_sam: Random failures when writing large amount of data to flash
- [GitHub #37502](https://github.com/zephyrproject-rtos/zephyr/issues/37502) - OPENTHREAD\_CUSTOM\_PARAMETERS does not seem to work
- [GitHub #37495](https://github.com/zephyrproject-rtos/zephyr/issues/37495) - mcuboot: Booting an image flashed on top of a Hawkbit updated ones results in hard fault
- [GitHub #37491](https://github.com/zephyrproject-rtos/zephyr/issues/37491) - wrong documentation format on DMA peripheral API reference
- [GitHub #37482](https://github.com/zephyrproject-rtos/zephyr/issues/37482) - ‘cmd.exe’ is not recognized as an internal or external command, operable program or batch file.
- [GitHub #37475](https://github.com/zephyrproject-rtos/zephyr/issues/37475) - twister: wrong test statuses in json report
- [GitHub #37472](https://github.com/zephyrproject-rtos/zephyr/issues/37472) - Corrupted timeout on poll for offloaded sockets
- [GitHub #37467](https://github.com/zephyrproject-rtos/zephyr/issues/37467) - Bluetooth: host: Incorrect advertiser timeout handling when using Limited Discoverable flag
- [GitHub #37465](https://github.com/zephyrproject-rtos/zephyr/issues/37465) - samples/bluetooth/iso\_receive fails on nrf5340dk target
- [GitHub #37462](https://github.com/zephyrproject-rtos/zephyr/issues/37462) - Bluetooth: Advertising becomes scannable even if BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD is set
- [GitHub #37461](https://github.com/zephyrproject-rtos/zephyr/issues/37461) - Schedule of LE audio in zephyr
- [GitHub #37460](https://github.com/zephyrproject-rtos/zephyr/issues/37460) - tests/kernel/sched/schedule\_api/kernel.scheduler and tests/kernel/fifo/fifo\_timeout/kernel.fifo.timeout failed on nsim\_hs\_smp board
- [GitHub #37456](https://github.com/zephyrproject-rtos/zephyr/issues/37456) - script: Unaccounted size in ram/rom reports
- [GitHub #37454](https://github.com/zephyrproject-rtos/zephyr/issues/37454) - Sensor driver: sht4x, sgp40, invalid include path
- [GitHub #37446](https://github.com/zephyrproject-rtos/zephyr/issues/37446) - Sensor driver: ST LPS22HH undeclared functions and variables
- [GitHub #37444](https://github.com/zephyrproject-rtos/zephyr/issues/37444) - MSI-X: wrong register referenced in map\_msix\_table()
- [GitHub #37441](https://github.com/zephyrproject-rtos/zephyr/issues/37441) - Native POSIX Flash Storage Does not Support Multiple Instances
- [GitHub #37436](https://github.com/zephyrproject-rtos/zephyr/issues/37436) - Delayed startup due to printing over not ready console
- [GitHub #37412](https://github.com/zephyrproject-rtos/zephyr/issues/37412) - IQ samples are not correct during the “reference period” of CTE signal
- [GitHub #37409](https://github.com/zephyrproject-rtos/zephyr/issues/37409) - Allow dual controller on usb
- [GitHub #37406](https://github.com/zephyrproject-rtos/zephyr/issues/37406) - ISO disconnect complete event doesn’t reach the application
- [GitHub #37400](https://github.com/zephyrproject-rtos/zephyr/issues/37400) - esp32 build
- [GitHub #37396](https://github.com/zephyrproject-rtos/zephyr/issues/37396) - DHCP issue with events not triggering on network with microsoft windows DHCP server
- [GitHub #37395](https://github.com/zephyrproject-rtos/zephyr/issues/37395) - stm32h747i\_disco board M4 core not working
- [GitHub #37391](https://github.com/zephyrproject-rtos/zephyr/issues/37391) - Bluetooth: 4 Bits of IQ Samples Are Removed (Direction Finding Based on CTE)
- [GitHub #37386](https://github.com/zephyrproject-rtos/zephyr/issues/37386) - bt\_vcs\_register() enhancement for setting default volume and step
- [GitHub #37379](https://github.com/zephyrproject-rtos/zephyr/issues/37379) - drivers: adc for stm32h7 depends on the version for oversampling
- [GitHub #37376](https://github.com/zephyrproject-rtos/zephyr/issues/37376) - samples/subsys/usb/dfu/sample.usb.dfu fails on teensy41/teensy40
- [GitHub #37375](https://github.com/zephyrproject-rtos/zephyr/issues/37375) - tests/drivers/adc/adc\_api/drivers.adc fails to build on nucleo\_h753zi
- [GitHub #37371](https://github.com/zephyrproject-rtos/zephyr/issues/37371) - logging.log2\_api\_deferred\_64b\_timestamp tests fails running on several qemu platforms
- [GitHub #37367](https://github.com/zephyrproject-rtos/zephyr/issues/37367) - Bluetooth: Host: Support setting long advertising data
- [GitHub #37365](https://github.com/zephyrproject-rtos/zephyr/issues/37365) - STM32 :DTCM: incorrect buffer size utilization
- [GitHub #37346](https://github.com/zephyrproject-rtos/zephyr/issues/37346) - STM32WL LoRa increased the current in “suspend\_to\_idle” state
- [GitHub #37338](https://github.com/zephyrproject-rtos/zephyr/issues/37338) - west flash to teensy 41 fail, use blinky with west build
- [GitHub #37332](https://github.com/zephyrproject-rtos/zephyr/issues/37332) - Increased power consumption for STM32WB55 with enabled PM and Bluetooth
- [GitHub #37327](https://github.com/zephyrproject-rtos/zephyr/issues/37327) - subsys/mgmt/hawkbit: hawkbit run can interrupt a running instance
- [GitHub #37319](https://github.com/zephyrproject-rtos/zephyr/issues/37319) - West 0.11.0 fails in Zephyr doc build under other manifest repo & renamed Zephyr fork
- [GitHub #37309](https://github.com/zephyrproject-rtos/zephyr/issues/37309) - ARC: add MPU v6 (and others) support
- [GitHub #37307](https://github.com/zephyrproject-rtos/zephyr/issues/37307) - Use XOSHIRO random number generator on NXP i.MX RT platform
- [GitHub #37306](https://github.com/zephyrproject-rtos/zephyr/issues/37306) - revert commit with bogus commit message
- [GitHub #37305](https://github.com/zephyrproject-rtos/zephyr/issues/37305) - Bluetooth Direction Finding Support of “AoA RX 1us”
- [GitHub #37304](https://github.com/zephyrproject-rtos/zephyr/issues/37304) - k\_timer\_status\_sync can lock forever on qemu\_x86\_64
- [GitHub #37303](https://github.com/zephyrproject-rtos/zephyr/issues/37303) - tests: drivers: i2s: drivers.i2s.speed scenario fails on nrf platforms
- [GitHub #37294](https://github.com/zephyrproject-rtos/zephyr/issues/37294) - RTT logs not found with default west debug invocation on jlink runner
- [GitHub #37293](https://github.com/zephyrproject-rtos/zephyr/issues/37293) - Native POSIX MAC addresses are not random and are duplicate between multiple instances
- [GitHub #37272](https://github.com/zephyrproject-rtos/zephyr/issues/37272) - subsys/mgmt/hawkbit: Falsely determine that an update is installed successfully
- [GitHub #37270](https://github.com/zephyrproject-rtos/zephyr/issues/37270) - stm32l4 System Power Management issue
- [GitHub #37264](https://github.com/zephyrproject-rtos/zephyr/issues/37264) - tests-ci : can: isotp: implemmentation test report FATAL ERROR when do not connect can loopback test pins
- [GitHub #37265](https://github.com/zephyrproject-rtos/zephyr/issues/37265) - tests-ci : kernel: scheduler: multiq test failed
- [GitHub #37266](https://github.com/zephyrproject-rtos/zephyr/issues/37266) - tests-ci : kernel: memory\_protection: userspace test Timeout
- [GitHub #37267](https://github.com/zephyrproject-rtos/zephyr/issues/37267) - tests-ci : kernel: threads: apis test Timeout
- [GitHub #37263](https://github.com/zephyrproject-rtos/zephyr/issues/37263) - lib: timeutil: conversion becomes less accurate as time progresses
- [GitHub #37260](https://github.com/zephyrproject-rtos/zephyr/issues/37260) - STM32WL does not support HSE as RCC source and HSEDiv
- [GitHub #37258](https://github.com/zephyrproject-rtos/zephyr/issues/37258) - symmetric multiprocessing failed in user mode
- [GitHub #37254](https://github.com/zephyrproject-rtos/zephyr/issues/37254) - Run Coverity / Generate GitHub Issues
- [GitHub #37253](https://github.com/zephyrproject-rtos/zephyr/issues/37253) - west flash is failed with openocd for on macOS
- [GitHub #37236](https://github.com/zephyrproject-rtos/zephyr/issues/37236) - ESP32 will not start when CONFIG\_ASSERT=y is enabled
- [GitHub #37231](https://github.com/zephyrproject-rtos/zephyr/issues/37231) - BME280 faulty measurement after power cycle
- [GitHub #37228](https://github.com/zephyrproject-rtos/zephyr/issues/37228) - Bluetooth SMP does not complete pairing
- [GitHub #37226](https://github.com/zephyrproject-rtos/zephyr/issues/37226) - PM: soc: Leftover in conversion of PM hooks to \_\_weak
- [GitHub #37225](https://github.com/zephyrproject-rtos/zephyr/issues/37225) - subsys/mgmt/hawkbit & sample: Bugs/improvements
- [GitHub #37222](https://github.com/zephyrproject-rtos/zephyr/issues/37222) - k\_queue data corruption, override user data after reserved heading word
- [GitHub #37221](https://github.com/zephyrproject-rtos/zephyr/issues/37221) - nRF5340: SPIM4 invalid clock frequency selection
- [GitHub #37213](https://github.com/zephyrproject-rtos/zephyr/issues/37213) - ESP32: can’t write to SD card over SPI (CRC error)
- [GitHub #37207](https://github.com/zephyrproject-rtos/zephyr/issues/37207) - drivers: serial: convert uart\_altera\_jtag\_hal to use devicetree
- [GitHub #37206](https://github.com/zephyrproject-rtos/zephyr/issues/37206) - counter: stm32: Missing implementation of set\_top\_value
- [GitHub #37205](https://github.com/zephyrproject-rtos/zephyr/issues/37205) - openocd: Configure thread awareness by default
- [GitHub #37202](https://github.com/zephyrproject-rtos/zephyr/issues/37202) - esp32c3 build error
- [GitHub #37189](https://github.com/zephyrproject-rtos/zephyr/issues/37189) - Bug “Key ‘name’, ‘cmake-ext’ and ‘kconfig-ext’ were not defined” when build a zephyr application
- [GitHub #37188](https://github.com/zephyrproject-rtos/zephyr/issues/37188) - Get an error of “Illegal load of EXC\_RETURN into PC” when print log in IO interrupt callback
- [GitHub #37182](https://github.com/zephyrproject-rtos/zephyr/issues/37182) - cmsis\_v1 osSignalWait doesn’t clear the signals properly when any signal mask is set
- [GitHub #37180](https://github.com/zephyrproject-rtos/zephyr/issues/37180) - Led driver PCA9633 does nok take chip out from sleep
- [GitHub #37175](https://github.com/zephyrproject-rtos/zephyr/issues/37175) - nucleo-f756zg: rtos aware debugging not working
- [GitHub #37174](https://github.com/zephyrproject-rtos/zephyr/issues/37174) - Zephyr’s .git directory is 409 MiB, can it be squashed?
- [GitHub #37173](https://github.com/zephyrproject-rtos/zephyr/issues/37173) - drivers: clock\_control: stm32: AHB prescaler usable for almost all stm32 series
- [GitHub #37170](https://github.com/zephyrproject-rtos/zephyr/issues/37170) - LwM2M lwm2m\_rd\_client\_stop() not working when called during bootstrapping/registration
- [GitHub #37160](https://github.com/zephyrproject-rtos/zephyr/issues/37160) - [Moved] Bootloader should provide the version of zephyr, mcuboot and a user defined version to the application
- [GitHub #37159](https://github.com/zephyrproject-rtos/zephyr/issues/37159) - osThreadTerminate does not decrease the instances counter
- [GitHub #37153](https://github.com/zephyrproject-rtos/zephyr/issues/37153) - USB serial number is not unique for STM32 devices
- [GitHub #37145](https://github.com/zephyrproject-rtos/zephyr/issues/37145) - sys: ring\_buffer: ring\_buf\_peek() and ring\_buf\_size\_get()
- [GitHub #37140](https://github.com/zephyrproject-rtos/zephyr/issues/37140) - Twister: Cmake error wrongly counted in the report
- [GitHub #37135](https://github.com/zephyrproject-rtos/zephyr/issues/37135) - Extend the HWINFO API to provide variable length unique ID
- [GitHub #37134](https://github.com/zephyrproject-rtos/zephyr/issues/37134) - Add support for the Raspberry Pi Compute Module 4
- [GitHub #37132](https://github.com/zephyrproject-rtos/zephyr/issues/37132) - Assert on enabling Socket CAN
- [GitHub #37120](https://github.com/zephyrproject-rtos/zephyr/issues/37120) - Documentation on modules
- [GitHub #37119](https://github.com/zephyrproject-rtos/zephyr/issues/37119) - tests: kernel tests hardfault on nucleo\_l073rz
- [GitHub #37115](https://github.com/zephyrproject-rtos/zephyr/issues/37115) - tests/bluetooth/shell fails to builds on a lot of platforms
- [GitHub #37109](https://github.com/zephyrproject-rtos/zephyr/issues/37109) - Zephyr POSIX layer uses swapping with an interrupt lock held
- [GitHub #37105](https://github.com/zephyrproject-rtos/zephyr/issues/37105) - mcumgr: BUS FAULT when starting dfu with mcumgr CLI
- [GitHub #37104](https://github.com/zephyrproject-rtos/zephyr/issues/37104) - tests-ci : kernel: scheduler: multiq test failed
- [GitHub #37075](https://github.com/zephyrproject-rtos/zephyr/issues/37075) - PlatformIO: i cannot use the Wifi Shield ESP8266 to build the sample wifi project with the Nucleo F429ZI
- [GitHub #37070](https://github.com/zephyrproject-rtos/zephyr/issues/37070) - NXP mcux ADC16 reading 65535
- [GitHub #37057](https://github.com/zephyrproject-rtos/zephyr/issues/37057) - PWM-blinky for Silabs MCU
- [GitHub #37038](https://github.com/zephyrproject-rtos/zephyr/issues/37038) - stm32f4 - DMA tx interrupt doesn’t trigger
- [GitHub #37032](https://github.com/zephyrproject-rtos/zephyr/issues/37032) - document: API reference missing: In clock of zephyr document
- [GitHub #37029](https://github.com/zephyrproject-rtos/zephyr/issues/37029) - drivers: sensor: sensor\_value\_to\_double requieres non const sensor\_value pointer
- [GitHub #37028](https://github.com/zephyrproject-rtos/zephyr/issues/37028) - ipv6 multicast addresses vanish after iface down/up sequence
- [GitHub #37024](https://github.com/zephyrproject-rtos/zephyr/issues/37024) - Compile error if we only use VCS without VOCS and AICS
- [GitHub #37023](https://github.com/zephyrproject-rtos/zephyr/issues/37023) - zephyr\_prebuilt.elf and zephyr.elf has inconsistent symbol address in RISC-V platform
- [GitHub #37007](https://github.com/zephyrproject-rtos/zephyr/issues/37007) - Problem with out of tree driver
- [GitHub #37006](https://github.com/zephyrproject-rtos/zephyr/issues/37006) - tests: kernel: mem\_protect: stack\_random: enable qemu\_riscv32
- [GitHub #36998](https://github.com/zephyrproject-rtos/zephyr/issues/36998) - TF-M: does not allow PSA Connect to proceed with IRQs locked
- [GitHub #36990](https://github.com/zephyrproject-rtos/zephyr/issues/36990) - Memory misalignment ARM Cortex-M33
- [GitHub #36971](https://github.com/zephyrproject-rtos/zephyr/issues/36971) - ESP32: wifi station sample does not get IP address by DHCP4
- [GitHub #36967](https://github.com/zephyrproject-rtos/zephyr/issues/36967) - Bluetooth: public API to query controller public address
- [GitHub #36959](https://github.com/zephyrproject-rtos/zephyr/issues/36959) - Direction Finding - CTE transmitted in connectionless mode has wrong length
- [GitHub #36953](https://github.com/zephyrproject-rtos/zephyr/issues/36953) - <err> lorawan: MlmeConfirm failed : Tx timeout
- [GitHub #36948](https://github.com/zephyrproject-rtos/zephyr/issues/36948) - Cluttering of logs on USB Console in Zephyr when CDC Shell is enabled
- [GitHub #36947](https://github.com/zephyrproject-rtos/zephyr/issues/36947) - Tensorflow: Dedicated tflite-micro repository
- [GitHub #36929](https://github.com/zephyrproject-rtos/zephyr/issues/36929) - Failure to build OpenThread LwM2M client on nrf52840dk
- [GitHub #36928](https://github.com/zephyrproject-rtos/zephyr/issues/36928) - Disconnecting ISO mid-send giver error in hci\_num\_completed\_packets
- [GitHub #36927](https://github.com/zephyrproject-rtos/zephyr/issues/36927) - LWM2M: Writing to Write-Only resource causes notification
- [GitHub #36926](https://github.com/zephyrproject-rtos/zephyr/issues/36926) - samples/boards/nrf/system\_off wouldn’t compile on Particle Xenon board
- [GitHub #36924](https://github.com/zephyrproject-rtos/zephyr/issues/36924) - embARC Machine Learning Inference Library from Synopsys
- [GitHub #36917](https://github.com/zephyrproject-rtos/zephyr/issues/36917) - Runtime device PM is broken on STM32
- [GitHub #36909](https://github.com/zephyrproject-rtos/zephyr/issues/36909) - Shell log` commands crash the system if CONFIG\_SHELL\_LOG\_BACKEND is not defined
- [GitHub #36896](https://github.com/zephyrproject-rtos/zephyr/issues/36896) - tests: net: select: still failing occasionally due to FUZZ
- [GitHub #36891](https://github.com/zephyrproject-rtos/zephyr/issues/36891) - Significant TCP perfomance regression
- [GitHub #36889](https://github.com/zephyrproject-rtos/zephyr/issues/36889) - string.h / strcasestr() + strtok()
- [GitHub #36885](https://github.com/zephyrproject-rtos/zephyr/issues/36885) - Update ISO API to better support TWS
- [GitHub #36882](https://github.com/zephyrproject-rtos/zephyr/issues/36882) - MCUMGR: fs upload fail for first time file upload
- [GitHub #36873](https://github.com/zephyrproject-rtos/zephyr/issues/36873) - USB AUDIO Byte alignment issues
- [GitHub #36869](https://github.com/zephyrproject-rtos/zephyr/issues/36869) - Direction Finding Connectionless porting to nrf52811
- [GitHub #36866](https://github.com/zephyrproject-rtos/zephyr/issues/36866) - CONFIG\_NO\_OPTIMIZATIONS=y MPU fault on Zephyr 2.6
- [GitHub #36865](https://github.com/zephyrproject-rtos/zephyr/issues/36865) - k\_work\_q seems to check uninitialized flag on start
- [GitHub #36859](https://github.com/zephyrproject-rtos/zephyr/issues/36859) - Possible Advertising PDU Corruption if bt\_enable called in SYS\_INIT function
- [GitHub #36858](https://github.com/zephyrproject-rtos/zephyr/issues/36858) - Static object constructors execute twice on the NATIVE\_POSIX target
- [GitHub #36857](https://github.com/zephyrproject-rtos/zephyr/issues/36857) - i2c\_samd0.c burst write not compatible with ssd1306.c
- [GitHub #36851](https://github.com/zephyrproject-rtos/zephyr/issues/36851) - FS logging backend assumes littlefs
- [GitHub #36823](https://github.com/zephyrproject-rtos/zephyr/issues/36823) - Build excludes paths to standard C++ headers when using GNUARMEMB toolchain variant
- [GitHub #36819](https://github.com/zephyrproject-rtos/zephyr/issues/36819) - qemu\_leon3 samples/subsys/portability/cmsis\_rtos\_v2 samples failing
- [GitHub #36814](https://github.com/zephyrproject-rtos/zephyr/issues/36814) - Wrong format type for uint32\_t
- [GitHub #36811](https://github.com/zephyrproject-rtos/zephyr/issues/36811) - Clarify `Z_` APIs naming conventions and intended scope
- [GitHub #36802](https://github.com/zephyrproject-rtos/zephyr/issues/36802) - MCUboot doesn’t work with encrypted images on external flash
- [GitHub #36796](https://github.com/zephyrproject-rtos/zephyr/issues/36796) - Build failure: samples/net/civetweb/http\_server using target stm32h735g\_disco
- [GitHub #36794](https://github.com/zephyrproject-rtos/zephyr/issues/36794) - Build failure: tests/drivers/adc using stm32l562e\_dk
- [GitHub #36790](https://github.com/zephyrproject-rtos/zephyr/issues/36790) - sys: ring\_buffer: correct space calculation when tail is less than head
- [GitHub #36789](https://github.com/zephyrproject-rtos/zephyr/issues/36789) - [ESP32] samples blinky / gpio / custom board
- [GitHub #36783](https://github.com/zephyrproject-rtos/zephyr/issues/36783) - drivers: modem: hl7800 gpio init failed with interrupt flags
- [GitHub #36782](https://github.com/zephyrproject-rtos/zephyr/issues/36782) - drivers: serial: nrfx: Enforced pull-ups on RXD and CTS conflict on many custom boards
- [GitHub #36781](https://github.com/zephyrproject-rtos/zephyr/issues/36781) - source\_periph incorrectly set in dma\_stm32
- [GitHub #36778](https://github.com/zephyrproject-rtos/zephyr/issues/36778) - firmware update using mcumgr displays information for only slot 0 and not slot 1.
- [GitHub #36770](https://github.com/zephyrproject-rtos/zephyr/issues/36770) - doc：Missing description for deadline scheduling
- [GitHub #36769](https://github.com/zephyrproject-rtos/zephyr/issues/36769) - Zephyr assumes Interrupt Line config space register is RW, while ACRN hardwired it to 0.
- [GitHub #36767](https://github.com/zephyrproject-rtos/zephyr/issues/36767) - tests-ci :arch.arm.irq\_advanced\_features.arm\_irq\_target\_state : test failed
- [GitHub #36768](https://github.com/zephyrproject-rtos/zephyr/issues/36768) - tests-ci :coredump.logging\_backend : test failed
- [GitHub #36765](https://github.com/zephyrproject-rtos/zephyr/issues/36765) - [PCI] ACRN sets Interrupt Line config space register to 0 and ReadOnly.
- [GitHub #36764](https://github.com/zephyrproject-rtos/zephyr/issues/36764) - Bluetooth Require paired after disconnected work with iphone
- [GitHub #36755](https://github.com/zephyrproject-rtos/zephyr/issues/36755) - NTP client faults module when it fails
- [GitHub #36748](https://github.com/zephyrproject-rtos/zephyr/issues/36748) - Zephyr IP Stack Leaks when using PROMISCUOUS socket along with POSIX sockets based implementation.
- [GitHub #36747](https://github.com/zephyrproject-rtos/zephyr/issues/36747) - Adding Board Support for STEVAL-STWINKT1B
- [GitHub #36745](https://github.com/zephyrproject-rtos/zephyr/issues/36745) - Zephyr IP Stack Limited to 1514 bytes on the wire - no ICMPs beyond this limit
- [GitHub #36739](https://github.com/zephyrproject-rtos/zephyr/issues/36739) - coap\_packet\_get\_payload() returns the wrong size
- [GitHub #36737](https://github.com/zephyrproject-rtos/zephyr/issues/36737) - Cortex M23: “swap\_helper.S:223: Error: invalid offset, value too big (0x0000009C)”
- [GitHub #36736](https://github.com/zephyrproject-rtos/zephyr/issues/36736) - kernel: SMP global lock (and therefore irq\_lock) works incorrectly on SMP platforms
- [GitHub #36718](https://github.com/zephyrproject-rtos/zephyr/issues/36718) - st\_ble\_sensor sample references wrong attribute
- [GitHub #36716](https://github.com/zephyrproject-rtos/zephyr/issues/36716) - zephyr - ADC - ATSAMD21G18A
- [GitHub #36713](https://github.com/zephyrproject-rtos/zephyr/issues/36713) - nrf5 ieee802154 driver does not compile and breaks CI
- [GitHub #36711](https://github.com/zephyrproject-rtos/zephyr/issues/36711) - Enable “template repository” for zephyrproject-rtos/example-application
- [GitHub #36696](https://github.com/zephyrproject-rtos/zephyr/issues/36696) - Json on native\_posix\_64 board
- [GitHub #36695](https://github.com/zephyrproject-rtos/zephyr/issues/36695) - net: ieee802154: cc13xx\_26xx: Sub-GHz RF power saving
- [GitHub #36692](https://github.com/zephyrproject-rtos/zephyr/issues/36692) - Release Notes for 2.6.0 not useful (BLE API changes)
- [GitHub #36679](https://github.com/zephyrproject-rtos/zephyr/issues/36679) - Bluetooth - notifications not sending (bonded, CONFIG\_BT\_MAX\_CONN=4, after disconnection then reconnection)
- [GitHub #36678](https://github.com/zephyrproject-rtos/zephyr/issues/36678) - Zephyr Throws Exception for Shell “log status” command when Telnet is shell backend and log is UART backend
- [GitHub #36668](https://github.com/zephyrproject-rtos/zephyr/issues/36668) - LittleFS example overwrite falsh memory
- [GitHub #36667](https://github.com/zephyrproject-rtos/zephyr/issues/36667) - logger: Filesystem backend doesn’t work except for first time boot
- [GitHub #36665](https://github.com/zephyrproject-rtos/zephyr/issues/36665) - l2cap cids mixed up in request
- [GitHub #36661](https://github.com/zephyrproject-rtos/zephyr/issues/36661) - xtensa xcc does not support “-Warray-bounds”
- [GitHub #36659](https://github.com/zephyrproject-rtos/zephyr/issues/36659) - samples/net/sockets small bugs
- [GitHub #36655](https://github.com/zephyrproject-rtos/zephyr/issues/36655) - twister: sometimes the twister fails because the error `configparser.NoSectionError: No section: 'manifest'`
- [GitHub #36652](https://github.com/zephyrproject-rtos/zephyr/issues/36652) - deadlock in pthread implementation on SMP platforms
- [GitHub #36646](https://github.com/zephyrproject-rtos/zephyr/issues/36646) - sample.shell.shell\_module.minimal\_rtt fails to build on mimxrt1170\_evk\_cm4/mimxrt1170\_evk\_cm7
- [GitHub #36644](https://github.com/zephyrproject-rtos/zephyr/issues/36644) - Toolchain C++ headers can be included when libstdc++ is not selected
- [GitHub #36631](https://github.com/zephyrproject-rtos/zephyr/issues/36631) - Turn on GPIO from DTS
- [GitHub #36625](https://github.com/zephyrproject-rtos/zephyr/issues/36625) - compilation fails while building samples/net/openthread/coprocessor for Arduino nano 33 ble
- [GitHub #36613](https://github.com/zephyrproject-rtos/zephyr/issues/36613) - LoRaWAN - Provide method to register a callback for received data
- [GitHub #36609](https://github.com/zephyrproject-rtos/zephyr/issues/36609) - could not mount fatfs on efm32pg\_stk3402a
- [GitHub #36608](https://github.com/zephyrproject-rtos/zephyr/issues/36608) - Unable to compile USB console example with uart\_mux
- [GitHub #36606](https://github.com/zephyrproject-rtos/zephyr/issues/36606) - Regression in udp socket performance from zephyr v2.3.0 to v2.6.0
- [GitHub #36600](https://github.com/zephyrproject-rtos/zephyr/issues/36600) - Bluetooth: Peripheral: Bond issue when using secure connection
- [GitHub #36598](https://github.com/zephyrproject-rtos/zephyr/issues/36598) - Lora driver TX done wait/synchronous call
- [GitHub #36593](https://github.com/zephyrproject-rtos/zephyr/issues/36593) - Failing IPv6 Ready compliance (RFC 2460)
- [GitHub #36590](https://github.com/zephyrproject-rtos/zephyr/issues/36590) - NVS sector size above 65535 not supported
- [GitHub #36578](https://github.com/zephyrproject-rtos/zephyr/issues/36578) - net: ip: Assertion fails when tcp\_send\_data() with zero length packet
- [GitHub #36575](https://github.com/zephyrproject-rtos/zephyr/issues/36575) - Modbus RTU Client on ESP32
- [GitHub #36572](https://github.com/zephyrproject-rtos/zephyr/issues/36572) - kernel: Negative mutex lock\_count value
- [GitHub #36570](https://github.com/zephyrproject-rtos/zephyr/issues/36570) - Use a custom role for Kconfig configuration options
- [GitHub #36569](https://github.com/zephyrproject-rtos/zephyr/issues/36569) - ‘.. only:’ is not working as expected in documentation
- [GitHub #36568](https://github.com/zephyrproject-rtos/zephyr/issues/36568) - net: lib: sockets: Assertion fails when zsock\_close()
- [GitHub #36565](https://github.com/zephyrproject-rtos/zephyr/issues/36565) - ehl\_crb: Only boot banner is printed but not the test related details for multiple tests due to PR #36191 is not backported to v2.6.0 release
- [GitHub #36553](https://github.com/zephyrproject-rtos/zephyr/issues/36553) - LoRaWAN Sample: join accept but “Join failed”
- [GitHub #36552](https://github.com/zephyrproject-rtos/zephyr/issues/36552) - Bluetooth v2.6.0 connectable advertising leak/loss
- [GitHub #36540](https://github.com/zephyrproject-rtos/zephyr/issues/36540) - LoRaWAN otaa.app\_key belongs to mib\_req.Param.AppKey
- [GitHub #36524](https://github.com/zephyrproject-rtos/zephyr/issues/36524) - HSE clock doesn’t initialize and blinky doesn’t run on custom board when moving from zephyr v2.3.0 to v2.6.0
- [GitHub #36520](https://github.com/zephyrproject-rtos/zephyr/issues/36520) - tests/kernel/timer/timer\_api/kernel.timer.tickless fails to build on npcx9m6f\_evb
- [GitHub #36500](https://github.com/zephyrproject-rtos/zephyr/issues/36500) - espressif: cannot install toolchain on Darwin-arm64
- [GitHub #36496](https://github.com/zephyrproject-rtos/zephyr/issues/36496) - bluetooth: only the first Extended Advertising Report with data status “incomplete, more data to come” is issued
- [GitHub #36495](https://github.com/zephyrproject-rtos/zephyr/issues/36495) - dtc generates missing #address-cells in interrupt provider warning
- [GitHub #36486](https://github.com/zephyrproject-rtos/zephyr/issues/36486) - LOG2 - self referential macro
- [GitHub #36467](https://github.com/zephyrproject-rtos/zephyr/issues/36467) - runner mdb-hw not work with arc hsdk board
- [GitHub #36466](https://github.com/zephyrproject-rtos/zephyr/issues/36466) - tests/kernel/mem\_protect/mem\_protect failed with arcmwdt toolchain
- [GitHub #36465](https://github.com/zephyrproject-rtos/zephyr/issues/36465) - samples/compression/lz4 failed with arcmwdt toolchian
- [GitHub #36462](https://github.com/zephyrproject-rtos/zephyr/issues/36462) - [bluetooth stack][limited\_discoverable\_advertising timeout] Some problems about the lim\_adv\_timeout
- [GitHub #36448](https://github.com/zephyrproject-rtos/zephyr/issues/36448) - samples: subsys: fs: fat\_fs: adafruit\_2\_8\_tft\_touch\_v2: buildkite compilation failed when no i2c defined
- [GitHub #36447](https://github.com/zephyrproject-rtos/zephyr/issues/36447) - net: socket: socketpair: Poll call resetting all events
- [GitHub #36435](https://github.com/zephyrproject-rtos/zephyr/issues/36435) - RFC: API Change: Mesh: Add return value for opcode callback
- [GitHub #36427](https://github.com/zephyrproject-rtos/zephyr/issues/36427) - test: kernel.common.nano32: zephyr-v2.6.0-286-g46029914a7ac: mimxrt1060\_evk: test fails
- [GitHub #36419](https://github.com/zephyrproject-rtos/zephyr/issues/36419) - test-ci: net.ethernet\_mgmt: zephyr-v2.6.0-286-g46029914a7ac: frdm\_k64f: test fails
- [GitHub #36418](https://github.com/zephyrproject-rtos/zephyr/issues/36418) - test-ci: net.socket.tls: zephyr-v2.6.0-286-g46029914a7ac: frdm\_k64f: test fail
- [GitHub #36417](https://github.com/zephyrproject-rtos/zephyr/issues/36417) - tests-ci :coredump.logging\_backend : zephyr-v2.6.0-286-g46029914a7ac: lpcxpresso55s28: test failed
- [GitHub #36416](https://github.com/zephyrproject-rtos/zephyr/issues/36416) - tests-ci :arch.arm.irq\_advanced\_features.arm\_irq\_target\_state : zephyr-v2.6.0-286-g46029914a7ac: lpcxpresso55s28: test failed
- [GitHub #36414](https://github.com/zephyrproject-rtos/zephyr/issues/36414) - ESP32 with samples/net/wifi gives: net\_if: There is no network interface to work with!
- [GitHub #36412](https://github.com/zephyrproject-rtos/zephyr/issues/36412) - Blinky on ESP32: Unsupported board: led0 devicetree alias is not defined”
- [GitHub #36410](https://github.com/zephyrproject-rtos/zephyr/issues/36410) - board: cc1352r\_sensortag: add dts entry for hdc2080
- [GitHub #36408](https://github.com/zephyrproject-rtos/zephyr/issues/36408) - ARM\_MPU on boards `stm32_min_dev_*` without MPU enabled
- [GitHub #36398](https://github.com/zephyrproject-rtos/zephyr/issues/36398) - [Video API] Erroneous function pointer validation
- [GitHub #36390](https://github.com/zephyrproject-rtos/zephyr/issues/36390) - net: ip: Negative TCP unacked\_len value
- [GitHub #36388](https://github.com/zephyrproject-rtos/zephyr/issues/36388) - ARM: Architecture Level user guide
- [GitHub #36382](https://github.com/zephyrproject-rtos/zephyr/issues/36382) - segfault when hardware isn’t emulated
- [GitHub #36381](https://github.com/zephyrproject-rtos/zephyr/issues/36381) - Bluetooth ASSERTION FAIL [evdone] Zephyr v2.6.0
- [GitHub #36380](https://github.com/zephyrproject-rtos/zephyr/issues/36380) - missing auto-dependency on CONFIG\_EMUL
- [GitHub #36357](https://github.com/zephyrproject-rtos/zephyr/issues/36357) - tests: samples: watchdog: sample.subsys.task\_wdt fails on nrf platforms
- [GitHub #36356](https://github.com/zephyrproject-rtos/zephyr/issues/36356) - Network fails to transmit STM32H747DISC0 board zephyr v2.6.0
- [GitHub #36351](https://github.com/zephyrproject-rtos/zephyr/issues/36351) - nRF: we do not always guarantee that SystemInit is inlined
- [GitHub #36347](https://github.com/zephyrproject-rtos/zephyr/issues/36347) - Zephyr Wifi IoT device - whats a good board to start with?
- [GitHub #36344](https://github.com/zephyrproject-rtos/zephyr/issues/36344) - Zephyr 2.6.0 st\_ble\_sensor sample is broken when compiled for nucleo\_wb55rg
- [GitHub #36339](https://github.com/zephyrproject-rtos/zephyr/issues/36339) - samples/subsys/logging/dictionary doesn’t build under MS Windows environment
- [GitHub #36329](https://github.com/zephyrproject-rtos/zephyr/issues/36329) - Support for CC3120 WiFi module
- [GitHub #36324](https://github.com/zephyrproject-rtos/zephyr/issues/36324) - add project groups to upsteam west manifest
- [GitHub #36323](https://github.com/zephyrproject-rtos/zephyr/issues/36323) - Don’t set TFM\_CMAKE\_BUILD\_TYPE\_DEBUG by default on LPC55S69-NS if DEBUG\_OPTIMIZATIONS
- [GitHub #36319](https://github.com/zephyrproject-rtos/zephyr/issues/36319) - Help: Asking for Help Tips page gets 404 error
- [GitHub #36318](https://github.com/zephyrproject-rtos/zephyr/issues/36318) - [Coverity CID: 236600] Unused value in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36317](https://github.com/zephyrproject-rtos/zephyr/issues/36317) - [Coverity CID: 236599] Unused value in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36316](https://github.com/zephyrproject-rtos/zephyr/issues/36316) - [Coverity CID: 236597] Unused value in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36315](https://github.com/zephyrproject-rtos/zephyr/issues/36315) - [Coverity CID: 236604] Untrusted value as argument in subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #36314](https://github.com/zephyrproject-rtos/zephyr/issues/36314) - [Coverity CID: 236610] Uninitialized pointer read in subsys/bluetooth/mesh/proxy.c
- [GitHub #36313](https://github.com/zephyrproject-rtos/zephyr/issues/36313) - [Coverity CID: 236602] Unchecked return value in drivers/modem/gsm\_ppp.c
- [GitHub #36312](https://github.com/zephyrproject-rtos/zephyr/issues/36312) - [Coverity CID: 236608] Out-of-bounds access in subsys/bluetooth/audio/mics\_client.c
- [GitHub #36311](https://github.com/zephyrproject-rtos/zephyr/issues/36311) - [Coverity CID: 236598] Out-of-bounds access in subsys/bluetooth/audio/mics\_client.c
- [GitHub #36310](https://github.com/zephyrproject-rtos/zephyr/issues/36310) - [Coverity CID: 236607] Missing break in switch in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36309](https://github.com/zephyrproject-rtos/zephyr/issues/36309) - [Coverity CID: 236606] Missing break in switch in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36308](https://github.com/zephyrproject-rtos/zephyr/issues/36308) - [Coverity CID: 236601] Missing break in switch in drivers/ieee802154/ieee802154\_nrf5.c
- [GitHub #36307](https://github.com/zephyrproject-rtos/zephyr/issues/36307) - [Coverity CID: 236605] Logically dead code in subsys/bluetooth/audio/mics.c
- [GitHub #36306](https://github.com/zephyrproject-rtos/zephyr/issues/36306) - [Coverity CID: 236596] Logically dead code in subsys/bluetooth/audio/mics.c
- [GitHub #36305](https://github.com/zephyrproject-rtos/zephyr/issues/36305) - [Coverity CID: 236595] Logically dead code in samples/drivers/eeprom/src/main.c
- [GitHub #36304](https://github.com/zephyrproject-rtos/zephyr/issues/36304) - [Coverity CID: 236609] Explicit null dereferenced in subsys/bluetooth/audio/mics\_client.c
- [GitHub #36303](https://github.com/zephyrproject-rtos/zephyr/issues/36303) - [Coverity CID: 236603] Dereference after null check in subsys/bluetooth/audio/vcs\_client.c
- [GitHub #36301](https://github.com/zephyrproject-rtos/zephyr/issues/36301) - soc: cypress: Port Zephyr to Cypress CYW43907
- [GitHub #36298](https://github.com/zephyrproject-rtos/zephyr/issues/36298) - TF-M integration: add a brief user guide
- [GitHub #36291](https://github.com/zephyrproject-rtos/zephyr/issues/36291) - ADC and math library functions use for stm32l496
- [GitHub #36289](https://github.com/zephyrproject-rtos/zephyr/issues/36289) - eswifi gets a deadlock on b\_l4s5i\_iot01a target
- [GitHub #36282](https://github.com/zephyrproject-rtos/zephyr/issues/36282) - Overwrite mode for RTT logging
- [GitHub #36278](https://github.com/zephyrproject-rtos/zephyr/issues/36278) - ARM: Cortex-M: SysTick priority is not initialized if the SysTick is not used
- [GitHub #36276](https://github.com/zephyrproject-rtos/zephyr/issues/36276) - NULL pointer access in check\_used\_port()
- [GitHub #36270](https://github.com/zephyrproject-rtos/zephyr/issues/36270) - TF-M: introduce uniformity in Non-Secure target names
- [GitHub #36267](https://github.com/zephyrproject-rtos/zephyr/issues/36267) - net: ieee802154: software address filtering
- [GitHub #36263](https://github.com/zephyrproject-rtos/zephyr/issues/36263) - up\_squared: kernel.memory\_protection.mem\_map.x86\_64 failed.
- [GitHub #36256](https://github.com/zephyrproject-rtos/zephyr/issues/36256) - SPI4 & 3 MISO not working on nRF5340
- [GitHub #36255](https://github.com/zephyrproject-rtos/zephyr/issues/36255) - tests/subsys/logging/log\_core failed on hsdk board
- [GitHub #36254](https://github.com/zephyrproject-rtos/zephyr/issues/36254) - Zephyr shell subsystem not work with ARC hardware boards.
- [GitHub #36250](https://github.com/zephyrproject-rtos/zephyr/issues/36250) - tests/subsys/cpp/cxx - doesn’t compile on native\_posix when CONFIG\_EXCEPTIONS=y
- [GitHub #36247](https://github.com/zephyrproject-rtos/zephyr/issues/36247) - samples: usb: testusb: Problems with using with cdc-acm
- [GitHub #36242](https://github.com/zephyrproject-rtos/zephyr/issues/36242) - Zephyr Upstream + sdk-nrf BLE NUS SHELL LOG/CBPRINTF build problem.
- [GitHub #36238](https://github.com/zephyrproject-rtos/zephyr/issues/36238) - net\_if.c: possible mutex deadlock
- [GitHub #36237](https://github.com/zephyrproject-rtos/zephyr/issues/36237) - fs\_open returns 0 on existing file with FS\_O\_CREATE | FS\_O\_WRITE
- [GitHub #36197](https://github.com/zephyrproject-rtos/zephyr/issues/36197) - BOSSA flashing on Arduino Nano 33 BLE (NRF52840)
- [GitHub #36185](https://github.com/zephyrproject-rtos/zephyr/issues/36185) - CMP0116 related warnings
- [GitHub #36172](https://github.com/zephyrproject-rtos/zephyr/issues/36172) - net: ieee802154: LL src/dst address is lost from received net\_pkt (when using 6LO)
- [GitHub #36163](https://github.com/zephyrproject-rtos/zephyr/issues/36163) - nvs no longer supports the use of id=0xffff
- [GitHub #36131](https://github.com/zephyrproject-rtos/zephyr/issues/36131) - Occasionally unable to scan for extended advertisements when connected
- [GitHub #36117](https://github.com/zephyrproject-rtos/zephyr/issues/36117) - toolchain: The added abstraction for llvm, breaks builds with off-tree llvm based toolchains
- [GitHub #36107](https://github.com/zephyrproject-rtos/zephyr/issues/36107) - ehl\_crb: Multiple tests are failing and board is not booting up.
- [GitHub #36101](https://github.com/zephyrproject-rtos/zephyr/issues/36101) - tfm related build rebuild even if nothing changes
- [GitHub #36100](https://github.com/zephyrproject-rtos/zephyr/issues/36100) - pb\_gatt buf\_send does not call callback
- [GitHub #36095](https://github.com/zephyrproject-rtos/zephyr/issues/36095) - drivers: pwm: sam: compilation failure for sam\_v71b\_xult
- [GitHub #36094](https://github.com/zephyrproject-rtos/zephyr/issues/36094) - BLE wrong connections intervals on multible connections
- [GitHub #36093](https://github.com/zephyrproject-rtos/zephyr/issues/36093) - Fix dt\_compat\_enabled\_with\_label behavior (or usage)
- [GitHub #36089](https://github.com/zephyrproject-rtos/zephyr/issues/36089) - intel\_adsp\_cavs25: support more than 2 DSP cores
- [GitHub #36088](https://github.com/zephyrproject-rtos/zephyr/issues/36088) - intel\_adsp\_cavs25: secondary boot fails in arch\_start\_cpu()
- [GitHub #36084](https://github.com/zephyrproject-rtos/zephyr/issues/36084) - Arduino Nano 33 BLE: USB gets disconnected after flashing
- [GitHub #36078](https://github.com/zephyrproject-rtos/zephyr/issues/36078) - coredump.logging\_backend: lpcxpresso55s28: test failure assertion fail
- [GitHub #36077](https://github.com/zephyrproject-rtos/zephyr/issues/36077) - net: lib: coap: Impossible to get socket info from incoming packet
- [GitHub #36075](https://github.com/zephyrproject-rtos/zephyr/issues/36075) - drivers: can: stm32fd: can2 does not work
- [GitHub #36074](https://github.com/zephyrproject-rtos/zephyr/issues/36074) - LoRaWAN: sx126x: infinite loop on CRC error
- [GitHub #36061](https://github.com/zephyrproject-rtos/zephyr/issues/36061) - Undefined reference to `z_priq_rb_lessthan(rbnode*, rbnode*)` when using k\_timer\_start in cpp file.
- [GitHub #36057](https://github.com/zephyrproject-rtos/zephyr/issues/36057) - Zephyr Shell Console and Logging Targeting Isolated Different Device Interfaces
- [GitHub #36048](https://github.com/zephyrproject-rtos/zephyr/issues/36048) - Cannot establish ISO CIS connection properly after ACL disconnected several times
- [GitHub #36038](https://github.com/zephyrproject-rtos/zephyr/issues/36038) - iotdk: the testcase samples/modules/nanopb can’t build
- [GitHub #36037](https://github.com/zephyrproject-rtos/zephyr/issues/36037) - bt\_init returning success when Bluetooth initialization does not get finalized.
- [GitHub #36035](https://github.com/zephyrproject-rtos/zephyr/issues/36035) - struct devices should be allocated in ROM, not RAM
- [GitHub #36033](https://github.com/zephyrproject-rtos/zephyr/issues/36033) - Mere warnings slow down incremental documentation build from seconds to minutes
- [GitHub #36030](https://github.com/zephyrproject-rtos/zephyr/issues/36030) - West warnings (and others?) are ignored when building documentation
- [GitHub #36028](https://github.com/zephyrproject-rtos/zephyr/issues/36028) - More Description in Example Documentation
- [GitHub #36026](https://github.com/zephyrproject-rtos/zephyr/issues/36026) - wolfssl / wolfcrypt
- [GitHub #36022](https://github.com/zephyrproject-rtos/zephyr/issues/36022) - Wrong channel index in connectionless IQ samples report
- [GitHub #36014](https://github.com/zephyrproject-rtos/zephyr/issues/36014) - stm32g050: Missing closing parenthesis for soc prototype
- [GitHub #36013](https://github.com/zephyrproject-rtos/zephyr/issues/36013) - arm: qemu: run cmsis-dsp tests on the qemu target with FPU
- [GitHub #35999](https://github.com/zephyrproject-rtos/zephyr/issues/35999) - Unexpected Bluetooth disconnection and removal of bond
- [GitHub #35992](https://github.com/zephyrproject-rtos/zephyr/issues/35992) - stm32f303k8 device tree missing DACs
- [GitHub #35986](https://github.com/zephyrproject-rtos/zephyr/issues/35986) - POSIX: multiple definition of posix\_types
- [GitHub #35983](https://github.com/zephyrproject-rtos/zephyr/issues/35983) - [backport v1.14-branch] backport of #35935 failed
- [GitHub #35978](https://github.com/zephyrproject-rtos/zephyr/issues/35978) - ESP32 SPI send data hangup
- [GitHub #35972](https://github.com/zephyrproject-rtos/zephyr/issues/35972) - C++ exceptions do not work when building with GNU Arm Embedded
- [GitHub #35971](https://github.com/zephyrproject-rtos/zephyr/issues/35971) - ehl\_crb: test\_nop is failing under tests/kernel/common/
- [GitHub #35970](https://github.com/zephyrproject-rtos/zephyr/issues/35970) - up\_squared: samples/boards/up\_squared/gpio\_counter/ is failing
- [GitHub #35964](https://github.com/zephyrproject-rtos/zephyr/issues/35964) - shell\_uart hangs when putting UART into PM\_LOW\_POWER\_STATE / PM\_DEVICE\_STATE\_LOW\_POWER
- [GitHub #35962](https://github.com/zephyrproject-rtos/zephyr/issues/35962) - drivers using deprecated Kconfigs
- [GitHub #35955](https://github.com/zephyrproject-rtos/zephyr/issues/35955) - Bluetooth: Controller: Regression in connection setup
- [GitHub #35949](https://github.com/zephyrproject-rtos/zephyr/issues/35949) - can: mcan: sjw-data devicetree configuration is not written correctly
- [GitHub #35945](https://github.com/zephyrproject-rtos/zephyr/issues/35945) - SPI4 on nRF5340 not working when using k\_sleep() in main
- [GitHub #35941](https://github.com/zephyrproject-rtos/zephyr/issues/35941) - subsys: tracing: sysview: No SEGGER\_SYSVIEW.h in path
- [GitHub #35939](https://github.com/zephyrproject-rtos/zephyr/issues/35939) - enc424j600 driver unusable/broken on stm32l552
- [GitHub #35931](https://github.com/zephyrproject-rtos/zephyr/issues/35931) - Bluetooth: controller: Assertion in ull\_master.c
- [GitHub #35930](https://github.com/zephyrproject-rtos/zephyr/issues/35930) - nRF Dongle as BLE Central Unstable Connectivity at Long-ish Range
- [GitHub #35926](https://github.com/zephyrproject-rtos/zephyr/issues/35926) - Shell tab-completion with more than two levels of nested dynamic commands fails
- [GitHub #35916](https://github.com/zephyrproject-rtos/zephyr/issues/35916) - drivers: TI cc13xx\_cc26xx: build error when PM is enabled (serial, entropy, spi, i2c modules)
- [GitHub #35908](https://github.com/zephyrproject-rtos/zephyr/issues/35908) - Stopping DHCP with network interface goes down leaves networking state in a broken state
- [GitHub #35897](https://github.com/zephyrproject-rtos/zephyr/issues/35897) - Bluetooth: PTS Tester on native posix
- [GitHub #35890](https://github.com/zephyrproject-rtos/zephyr/issues/35890) - Build system ignores explicit ZephyrBuildConfiguration\_ROOT variable
- [GitHub #35880](https://github.com/zephyrproject-rtos/zephyr/issues/35880) - PSA tests run indefinitely when CONFIG\_TFM\_IPC=y
- [GitHub #35870](https://github.com/zephyrproject-rtos/zephyr/issues/35870) - Build failure with gcc 11.x on native\_posix
- [GitHub #35857](https://github.com/zephyrproject-rtos/zephyr/issues/35857) - intel\_adsp\_cavs15: run msgq testcases failed on ADSP
- [GitHub #35856](https://github.com/zephyrproject-rtos/zephyr/issues/35856) - intel\_adsp\_cavs15: run semaphore testcases failed on ADSP
- [GitHub #35850](https://github.com/zephyrproject-rtos/zephyr/issues/35850) - the sample kernel/metairq\_dispatch fails on nucleo\_g474re
- [GitHub #35835](https://github.com/zephyrproject-rtos/zephyr/issues/35835) - ADC support for STM32l496\_disco board
- [GitHub #35809](https://github.com/zephyrproject-rtos/zephyr/issues/35809) - sample: USB audio samples are not working on STM32
- [GitHub #35793](https://github.com/zephyrproject-rtos/zephyr/issues/35793) - kernel.scheduler.multiq: Failed since #35276 (“cooperative scheduling only” special cases removal)
- [GitHub #35789](https://github.com/zephyrproject-rtos/zephyr/issues/35789) - sockets\_tls: receiving data on offloaded socket before handshake causes pollin | pollerr and failed recvfrom (SARA-R4)
- [GitHub #35721](https://github.com/zephyrproject-rtos/zephyr/issues/35721) - Atmel sam0 Async and/or DMA may not work
- [GitHub #35720](https://github.com/zephyrproject-rtos/zephyr/issues/35720) - tests:kernel timer fails on test\_sleep\_abs with TICKLESS\_KERNEL and PM on nucleo\_wb55rg
- [GitHub #35718](https://github.com/zephyrproject-rtos/zephyr/issues/35718) - Excessive error messages from filesystem interface
- [GitHub #35711](https://github.com/zephyrproject-rtos/zephyr/issues/35711) - net: sockets: dtls: handshake not reset as it ought to be
- [GitHub #35707](https://github.com/zephyrproject-rtos/zephyr/issues/35707) - AssertionError: zephyr/tests/kernel/common test case is failing with gcc-11 (Yocto)
- [GitHub #35703](https://github.com/zephyrproject-rtos/zephyr/issues/35703) - posix\_apis: fails at test\_posix\_realtime for mimxrt1024\_evk
- [GitHub #35681](https://github.com/zephyrproject-rtos/zephyr/issues/35681) - Unable to get output for samples/subsys/logging/logger and samples/philosophers
- [GitHub #35668](https://github.com/zephyrproject-rtos/zephyr/issues/35668) - The channel selection of auxiliary advertisments in extended advertisments
- [GitHub #35663](https://github.com/zephyrproject-rtos/zephyr/issues/35663) - STM32H7: Support memory protection unit(MPU) to enable shared memory
- [GitHub #35658](https://github.com/zephyrproject-rtos/zephyr/issues/35658) - arch.interrupt.arm.irq\_vector\_table.arm\_irq\_vector\_table: MPU FAULT Halting system for mximxrt685\_evk\_cm33
- [GitHub #35656](https://github.com/zephyrproject-rtos/zephyr/issues/35656) - arch.interrupt.arm.arm\_interrupt: hangs on mimxrt685\_evk\_cm33
- [GitHub #35581](https://github.com/zephyrproject-rtos/zephyr/issues/35581) - stm32 SPI problems with DMA and INTR set-up
- [GitHub #35550](https://github.com/zephyrproject-rtos/zephyr/issues/35550) - nRF91: DPS310 I2C driver not working
- [GitHub #35532](https://github.com/zephyrproject-rtos/zephyr/issues/35532) - SSL Handshake error with modified http(s) client example
- [GitHub #35529](https://github.com/zephyrproject-rtos/zephyr/issues/35529) - STM32: STM32H7 ADC calibration must be performed on startup
- [GitHub #35429](https://github.com/zephyrproject-rtos/zephyr/issues/35429) - subsys: settings: Encryption
- [GitHub #35377](https://github.com/zephyrproject-rtos/zephyr/issues/35377) - add creg\_gpio driver for ARC HSDK board
- [GitHub #35354](https://github.com/zephyrproject-rtos/zephyr/issues/35354) - Adding support for measurement of Ultraviolet(UV) Light.
- [GitHub #35293](https://github.com/zephyrproject-rtos/zephyr/issues/35293) - Sporadic boot failure
- [GitHub #35256](https://github.com/zephyrproject-rtos/zephyr/issues/35256) - DOC: DATA PASSING TABLE MISSING THE OBJECT QUEUES
- [GitHub #35250](https://github.com/zephyrproject-rtos/zephyr/issues/35250) - Twister is not reading the serial line output completely
- [GitHub #35244](https://github.com/zephyrproject-rtos/zephyr/issues/35244) - twister: build failure for native\_posix with GNU binutils 2.35
- [GitHub #35238](https://github.com/zephyrproject-rtos/zephyr/issues/35238) - ieee802.15.4 support for stm32wb55
- [GitHub #35229](https://github.com/zephyrproject-rtos/zephyr/issues/35229) - twister log mixing between tests
- [GitHub #35190](https://github.com/zephyrproject-rtos/zephyr/issues/35190) - echo\_server sample non-functional rails all CPUs on native\_posix\_64 board build
- [GitHub #35055](https://github.com/zephyrproject-rtos/zephyr/issues/35055) - STM32L432KC Nucleo Reference board SWD problem after programming with Zephyr
- [GitHub #34917](https://github.com/zephyrproject-rtos/zephyr/issues/34917) - arch.interrupt.arm| arch.interrupt.extra\_exception\_info: lpcxpresso55s28 series: test failure
- [GitHub #34913](https://github.com/zephyrproject-rtos/zephyr/issues/34913) - ModuleNotFoundError: No module named ‘elftools’
- [GitHub #34879](https://github.com/zephyrproject-rtos/zephyr/issues/34879) - mec15xxevb\_assy6853: 2 GPIO test failures
- [GitHub #34855](https://github.com/zephyrproject-rtos/zephyr/issues/34855) - FANSTEL BT840X
- [GitHub #34832](https://github.com/zephyrproject-rtos/zephyr/issues/34832) - Coding Guideline - MISRA rule 14.4 not applied properly
- [GitHub #34829](https://github.com/zephyrproject-rtos/zephyr/issues/34829) - Bluetooth: ISO: Don’t attempt to remove the ISO data path of a disconnected ISO channel
- [GitHub #34767](https://github.com/zephyrproject-rtos/zephyr/issues/34767) - C++ support on ESP boards
- [GitHub #34760](https://github.com/zephyrproject-rtos/zephyr/issues/34760) - Hawkbit not downloading large files
- [GitHub #34659](https://github.com/zephyrproject-rtos/zephyr/issues/34659) - Bluetooth: HCI cmd response timeout
- [GitHub #34571](https://github.com/zephyrproject-rtos/zephyr/issues/34571) - Twister mark successfully passed tests as failed
- [GitHub #34557](https://github.com/zephyrproject-rtos/zephyr/issues/34557) - upgrade fatfs to 0.14b
- [GitHub #34554](https://github.com/zephyrproject-rtos/zephyr/issues/34554) - Settings FS: Duplicate finding is extremely slow when dealing with larger number of settings entries
- [GitHub #34544](https://github.com/zephyrproject-rtos/zephyr/issues/34544) - lib: gui: lvgl: buffer overflow bug on misconfiguration
- [GitHub #34543](https://github.com/zephyrproject-rtos/zephyr/issues/34543) - STM32F1 failed to compile with CONFIG\_UART\_ASYNC\_API
- [GitHub #34392](https://github.com/zephyrproject-rtos/zephyr/issues/34392) - [backport v2.5-branch] backport of #34237 failed
- [GitHub #34391](https://github.com/zephyrproject-rtos/zephyr/issues/34391) - [backport v1.14-branch] backport of #34237 failed
- [GitHub #34390](https://github.com/zephyrproject-rtos/zephyr/issues/34390) - i2s: bitrate is wrongly configured on STM32
- [GitHub #34372](https://github.com/zephyrproject-rtos/zephyr/issues/34372) - CPU Lockups when using own Log Backend
- [GitHub #34354](https://github.com/zephyrproject-rtos/zephyr/issues/34354) - Please investigate adding DMA support to STM32 I2C!
- [GitHub #34324](https://github.com/zephyrproject-rtos/zephyr/issues/34324) - RTT is not working on STM32
- [GitHub #34315](https://github.com/zephyrproject-rtos/zephyr/issues/34315) - BMI270 configuration file sending to I2C seems to be not handling the last part of the configuration properly.
- [GitHub #34305](https://github.com/zephyrproject-rtos/zephyr/issues/34305) - Shell [modem send] command causes shell to hang after about 10 seconds, Sara R4 - Particle Boron
- [GitHub #34282](https://github.com/zephyrproject-rtos/zephyr/issues/34282) - HAL Module Request: hal\_telink
- [GitHub #34273](https://github.com/zephyrproject-rtos/zephyr/issues/34273) - mqtt\_publisher: Unable to connect properly on EC21 modem with bg9x driver
- [GitHub #34269](https://github.com/zephyrproject-rtos/zephyr/issues/34269) - LOG\_MODE\_MINIMAL BUILD error
- [GitHub #34268](https://github.com/zephyrproject-rtos/zephyr/issues/34268) - Bluetooth: Mesh: Sample is stuck in init process on disco\_l475\_iot
- [GitHub #34259](https://github.com/zephyrproject-rtos/zephyr/issues/34259) - Problem running code with memory domain
- [GitHub #34239](https://github.com/zephyrproject-rtos/zephyr/issues/34239) - Call settings\_save\_one in the system work queue, which will cause real-time performance degradation.
- [GitHub #34236](https://github.com/zephyrproject-rtos/zephyr/issues/34236) - External source code integration request: Raspberry Pi Pico SDK
- [GitHub #34231](https://github.com/zephyrproject-rtos/zephyr/issues/34231) - uzlib (decompression library)
- [GitHub #34226](https://github.com/zephyrproject-rtos/zephyr/issues/34226) - Compile error when building civetweb http\_server sample for posix\_native
- [GitHub #34222](https://github.com/zephyrproject-rtos/zephyr/issues/34222) - Commit related to null pointer exception detection causing UART issues
- [GitHub #34218](https://github.com/zephyrproject-rtos/zephyr/issues/34218) - Civetweb server crashing when trying to access invalid resource
- [GitHub #34204](https://github.com/zephyrproject-rtos/zephyr/issues/34204) - nvs\_write: Bad documented return value.
- [GitHub #34192](https://github.com/zephyrproject-rtos/zephyr/issues/34192) - Sensor BME680: Add support for SPI operation
- [GitHub #34134](https://github.com/zephyrproject-rtos/zephyr/issues/34134) - USB do not works if bootloader badly use the device before
- [GitHub #34131](https://github.com/zephyrproject-rtos/zephyr/issues/34131) - TFTP client ignores incoming data packets
- [GitHub #34121](https://github.com/zephyrproject-rtos/zephyr/issues/34121) - Unable to generate pdf according to the documentation steps on windows
- [GitHub #34105](https://github.com/zephyrproject-rtos/zephyr/issues/34105) - Convert tests/kernel/workq to new kwork API
- [GitHub #34049](https://github.com/zephyrproject-rtos/zephyr/issues/34049) - Nordic nrf9160 switching between drivers and peripherals
- [GitHub #34015](https://github.com/zephyrproject-rtos/zephyr/issues/34015) - cfb sample “Device not found” for esp32 when SSD1306 is enabled
- [GitHub #33994](https://github.com/zephyrproject-rtos/zephyr/issues/33994) - kscan\_ft5336 doesn’t provide proper up/down information when polling, and hogs resources in interrupt mode
- [GitHub #33960](https://github.com/zephyrproject-rtos/zephyr/issues/33960) - Zephyr for Briey SoC
- [GitHub #33937](https://github.com/zephyrproject-rtos/zephyr/issues/33937) - [backport v1.14-branch] backport of #26712 failed
- [GitHub #33932](https://github.com/zephyrproject-rtos/zephyr/issues/33932) - [backport v1.14-branch] backport of #26083 failed
- [GitHub #33910](https://github.com/zephyrproject-rtos/zephyr/issues/33910) - sam\_v71\_xult -> I2C\_1 hang during scanning i2c devices
- [GitHub #33901](https://github.com/zephyrproject-rtos/zephyr/issues/33901) - tests: interrupt: irq\_enable() and irq\_disable() do not work with direct and regular interrupt on x86
- [GitHub #33895](https://github.com/zephyrproject-rtos/zephyr/issues/33895) - Device tree: STM32L412 and STM32L422 are missing nodes
- [GitHub #33883](https://github.com/zephyrproject-rtos/zephyr/issues/33883) - [backport v2.5-branch] backport of #33340 failed
- [GitHub #33876](https://github.com/zephyrproject-rtos/zephyr/issues/33876) - Lora sender sample build error for esp32
- [GitHub #33873](https://github.com/zephyrproject-rtos/zephyr/issues/33873) - arm\_arch\_timer: Too many clock announcements with CONFIG\_TICKLESS\_KERNEL=n on SMP
- [GitHub #33862](https://github.com/zephyrproject-rtos/zephyr/issues/33862) - [backport v2.5-branch] backport of #33771 failed
- [GitHub #33753](https://github.com/zephyrproject-rtos/zephyr/issues/33753) - LVGL output doesn’t match the LVGL TFT simulator for gauge widget
- [GitHub #33652](https://github.com/zephyrproject-rtos/zephyr/issues/33652) - Monitoring the BLE connection
- [GitHub #33573](https://github.com/zephyrproject-rtos/zephyr/issues/33573) - JSON\_OBJ\_DESCR\_ARRAY\_ARRAY is dangerously broken
- [GitHub #33554](https://github.com/zephyrproject-rtos/zephyr/issues/33554) - Request to add OM13056 board (LPC1500 family or specifically SoC LPC1519) support to Zephyr
- [GitHub #33544](https://github.com/zephyrproject-rtos/zephyr/issues/33544) - ehl\_crb: portability.posix.common.posix\_realtime failed.
- [GitHub #33485](https://github.com/zephyrproject-rtos/zephyr/issues/33485) - Issue with DMA transfers outside of the Zephyr DMA driver on STM32F767
- [GitHub #33483](https://github.com/zephyrproject-rtos/zephyr/issues/33483) - TIMESLICE and PM interaction and expected behavior
- [GitHub #33449](https://github.com/zephyrproject-rtos/zephyr/issues/33449) - Remove deprecated items in 2.7
- [GitHub #33440](https://github.com/zephyrproject-rtos/zephyr/issues/33440) - lsm6dso sensor driver not working on nRF5340
- [GitHub #33435](https://github.com/zephyrproject-rtos/zephyr/issues/33435) - armclang / armlinker
- [GitHub #33337](https://github.com/zephyrproject-rtos/zephyr/issues/33337) - twister: Find and fix all “dead” samples/tests
- [GitHub #33275](https://github.com/zephyrproject-rtos/zephyr/issues/33275) - ehl\_crb: samples/subsys/shell/shell\_module does not work
- [GitHub #33265](https://github.com/zephyrproject-rtos/zephyr/issues/33265) - Power Management Overhaul
- [GitHub #33192](https://github.com/zephyrproject-rtos/zephyr/issues/33192) - LoRaWAN - Application fails to start if module is not powered
- [GitHub #33113](https://github.com/zephyrproject-rtos/zephyr/issues/33113) - Improve code coverage for new feature or code change in kernel
- [GitHub #33104](https://github.com/zephyrproject-rtos/zephyr/issues/33104) - Updating Zephyr to fix Work Queue Problems
- [GitHub #33099](https://github.com/zephyrproject-rtos/zephyr/issues/33099) - ppp: termination packet not sent
- [GitHub #33052](https://github.com/zephyrproject-rtos/zephyr/issues/33052) - [Coverity CID :219624] Untrusted loop bound in subsys/bluetooth/host/sdp.c
- [GitHub #33041](https://github.com/zephyrproject-rtos/zephyr/issues/33041) - [Coverity CID :219645] Untrusted loop bound in subsys/bluetooth/host/sdp.c
- [GitHub #33016](https://github.com/zephyrproject-rtos/zephyr/issues/33016) - spi\_nor: CONFIG\_SPI\_NOR\_SFDP\_RUNTIME leaves flash in Standby after spi\_nor\_configure()
- [GitHub #33015](https://github.com/zephyrproject-rtos/zephyr/issues/33015) - spi\_nor driver: SPI\_NOR\_IDLE\_IN\_DPD breaks SPI\_NOR\_SFDP\_RUNTIME
- [GitHub #32997](https://github.com/zephyrproject-rtos/zephyr/issues/32997) - Improve documentation search experience
- [GitHub #32990](https://github.com/zephyrproject-rtos/zephyr/issues/32990) - FS/littlefs: it is possible to write to already deleted file
- [GitHub #32984](https://github.com/zephyrproject-rtos/zephyr/issues/32984) - West: openocd runner: Don’t let debug mode on by default
- [GitHub #32875](https://github.com/zephyrproject-rtos/zephyr/issues/32875) - Benchmarking Zephyr vs. RIOT-OS
- [GitHub #32836](https://github.com/zephyrproject-rtos/zephyr/issues/32836) - Remaining integration failures on intel\_adsp\_cavs15
- [GitHub #32822](https://github.com/zephyrproject-rtos/zephyr/issues/32822) - Code doesn’t compile after changing the PWM pin on example “blinky\_pwm” on NRF52
- [GitHub #32803](https://github.com/zephyrproject-rtos/zephyr/issues/32803) - Extend mcux uart drivers to support async API
- [GitHub #32789](https://github.com/zephyrproject-rtos/zephyr/issues/32789) - USB DFU support w/o MPU support
- [GitHub #32733](https://github.com/zephyrproject-rtos/zephyr/issues/32733) - RS-485 support
- [GitHub #32669](https://github.com/zephyrproject-rtos/zephyr/issues/32669) - [Bluetooth] sample code for Periodic Advertising Sync Transfer
- [GitHub #32603](https://github.com/zephyrproject-rtos/zephyr/issues/32603) - acrn\_ehl\_crb: test case of arch.interrupt.prevent\_interruption failed
- [GitHub #32564](https://github.com/zephyrproject-rtos/zephyr/issues/32564) - net\_buf reference count not protected
- [GitHub #32545](https://github.com/zephyrproject-rtos/zephyr/issues/32545) - It seems that CONFIG\_IMG\_MGMT\_VERBOSE\_ERR does not work
- [GitHub #32531](https://github.com/zephyrproject-rtos/zephyr/issues/32531) - get\_maintainer.py cannot parse MAINTAINERS.yml
- [GitHub #32293](https://github.com/zephyrproject-rtos/zephyr/issues/32293) - Zephyr 2.6 Release Checklist
- [GitHub #32289](https://github.com/zephyrproject-rtos/zephyr/issues/32289) - USDHC: Fails after reset
- [GitHub #32282](https://github.com/zephyrproject-rtos/zephyr/issues/32282) - x86 ACPI images are much too large
- [GitHub #32261](https://github.com/zephyrproject-rtos/zephyr/issues/32261) - problem with CONFIG\_STACK\_SENTINEL
- [GitHub #32133](https://github.com/zephyrproject-rtos/zephyr/issues/32133) - Current atomics are subtly broken on AArch64 due to memory ordering
- [GitHub #32111](https://github.com/zephyrproject-rtos/zephyr/issues/32111) - Zephyr build fail with LLVM on Windows
- [GitHub #32035](https://github.com/zephyrproject-rtos/zephyr/issues/32035) - Bluetooth: application notification when MTU updated
- [GitHub #31993](https://github.com/zephyrproject-rtos/zephyr/issues/31993) - Add west extension to parse yml file
- [GitHub #31985](https://github.com/zephyrproject-rtos/zephyr/issues/31985) - riscv: Long execution time when TICKLESS\_KERNEL=y
- [GitHub #31943](https://github.com/zephyrproject-rtos/zephyr/issues/31943) - drivers: flash: stm32: harmonization of flash erase implementation across STM32 series
- [GitHub #31739](https://github.com/zephyrproject-rtos/zephyr/issues/31739) - Convert CoAP unit tests to use ztest API
- [GitHub #31593](https://github.com/zephyrproject-rtos/zephyr/issues/31593) - civetweb hangs when there are no free filedescriptors
- [GitHub #31499](https://github.com/zephyrproject-rtos/zephyr/issues/31499) - lwm2m : Add visibility into observer notification success/fail
- [GitHub #31475](https://github.com/zephyrproject-rtos/zephyr/issues/31475) - TCP keepalive
- [GitHub #31473](https://github.com/zephyrproject-rtos/zephyr/issues/31473) - Failed phy request not retried and may prevent DLE procedure during auto-initiation
- [GitHub #31447](https://github.com/zephyrproject-rtos/zephyr/issues/31447) - MQTT idling gets disconnected when using TCP2
- [GitHub #31290](https://github.com/zephyrproject-rtos/zephyr/issues/31290) - dts: arm: st: standardize pwm default property st,prescaler to 0
- [GitHub #31253](https://github.com/zephyrproject-rtos/zephyr/issues/31253) - lis3dh driver support is confusing
- [GitHub #31162](https://github.com/zephyrproject-rtos/zephyr/issues/31162) - Mapping between existing and new system power management states
- [GitHub #31107](https://github.com/zephyrproject-rtos/zephyr/issues/31107) - libc: minimal: add qsort routine
- [GitHub #31043](https://github.com/zephyrproject-rtos/zephyr/issues/31043) - Infinite loop in modem cmd\_handler\_process
- [GitHub #30921](https://github.com/zephyrproject-rtos/zephyr/issues/30921) - west flash failed with an open ocd error
- [GitHub #30861](https://github.com/zephyrproject-rtos/zephyr/issues/30861) - drivers: uart: increase timeout precision in uart\_rx\_enable
- [GitHub #30635](https://github.com/zephyrproject-rtos/zephyr/issues/30635) - cpu\_stats: Change from printk to `LOG_*`
- [GitHub #30429](https://github.com/zephyrproject-rtos/zephyr/issues/30429) - Thread Border Router with NRC/RCP sample and nrf52840dk not starting
- [GitHub #30367](https://github.com/zephyrproject-rtos/zephyr/issues/30367) - TCP2 does not send our MSS to peer
- [GitHub #30245](https://github.com/zephyrproject-rtos/zephyr/issues/30245) - Bluetooth: controller: event scheduling pipeline preemption by short schedule
- [GitHub #30244](https://github.com/zephyrproject-rtos/zephyr/issues/30244) - Bluetooth: controller: Extended scan window time reservation prevents auxiliary channel reception
- [GitHub #30243](https://github.com/zephyrproject-rtos/zephyr/issues/30243) - Bluetooth: controller: IRK resolution in extended scanning breaks auxiliary PDU reception
- [GitHub #30236](https://github.com/zephyrproject-rtos/zephyr/issues/30236) - Main thread sometimes looping forever before user application is reached when using UDP and IPv6 on Nucleo F767ZI
- [GitHub #30209](https://github.com/zephyrproject-rtos/zephyr/issues/30209) - TCP2 : How to add MSS option on sending [SYN, ACK] to client?
- [GitHub #30066](https://github.com/zephyrproject-rtos/zephyr/issues/30066) - CI test build with RAM overflow
- [GitHub #30026](https://github.com/zephyrproject-rtos/zephyr/issues/30026) - Can not make multiple BLE IPSP connection to the same host
- [GitHub #29545](https://github.com/zephyrproject-rtos/zephyr/issues/29545) - samples: tfm\_integration: tfm\_ipc: No module named ‘cryptography.hazmat.primitives.asymmetric.ed25519’
- [GitHub #29535](https://github.com/zephyrproject-rtos/zephyr/issues/29535) - riscv: stack objects are mis-aligned
- [GitHub #29520](https://github.com/zephyrproject-rtos/zephyr/issues/29520) - make k\_current\_get() work without a system call
- [GitHub #29397](https://github.com/zephyrproject-rtos/zephyr/issues/29397) - Build all tests of module mcuboot
- [GitHub #28872](https://github.com/zephyrproject-rtos/zephyr/issues/28872) - Support ESP32 as Bluetooth controller
- [GitHub #28819](https://github.com/zephyrproject-rtos/zephyr/issues/28819) - memory order and consistency promises for Zephyr atomic API?
- [GitHub #28729](https://github.com/zephyrproject-rtos/zephyr/issues/28729) - ARM: Core Stack Improvements/Bug fixes for 2.6 release
- [GitHub #28716](https://github.com/zephyrproject-rtos/zephyr/issues/28716) - 2.5 Release Checklist
- [GitHub #28312](https://github.com/zephyrproject-rtos/zephyr/issues/28312) - Add option to enable ART Accelerator on STM32 FLASH controller
- [GitHub #27992](https://github.com/zephyrproject-rtos/zephyr/issues/27992) - stm32f7: usb: Bursting HID Get and Set report requests leads to unresponding Control endpoint.
- [GitHub #27525](https://github.com/zephyrproject-rtos/zephyr/issues/27525) - Including STM32Cube’s USB PD support to Zephyr
- [GitHub #27415](https://github.com/zephyrproject-rtos/zephyr/issues/27415) - Decide if we keep a single thread support (CONFIG\_MULTITHREADING=n) in Zephyr
- [GitHub #27176](https://github.com/zephyrproject-rtos/zephyr/issues/27176) - [v1.14] Restore socket descriptor permission management
- [GitHub #27015](https://github.com/zephyrproject-rtos/zephyr/issues/27015) - Add custom transport support for MQTT
- [GitHub #26981](https://github.com/zephyrproject-rtos/zephyr/issues/26981) - Problem with PPP + GSM MUX with SIMCOM7600E
- [GitHub #26585](https://github.com/zephyrproject-rtos/zephyr/issues/26585) - IPv4 multicast datagrams can’t be received for mimxrt1064\_evk board (missing ethernet API)
- [GitHub #26256](https://github.com/zephyrproject-rtos/zephyr/issues/26256) - NRF51822 BLE Micro module: hangs on k\_msleep() (RTC counter not working)
- [GitHub #26136](https://github.com/zephyrproject-rtos/zephyr/issues/26136) - CMake Error in Windows Environment
- [GitHub #26051](https://github.com/zephyrproject-rtos/zephyr/issues/26051) - shell: uart: Allow a change in the shell initalisation to let routing it through USB UART
- [GitHub #25832](https://github.com/zephyrproject-rtos/zephyr/issues/25832) - [test][kernel][lpcxpresso55s69\_ns] kernel cases meet ESF could not be retrieved successfully
- [GitHub #25182](https://github.com/zephyrproject-rtos/zephyr/issues/25182) - Raspberry Pi 4B Support
- [GitHub #25015](https://github.com/zephyrproject-rtos/zephyr/issues/25015) - Bluetooth Isochronous Channels Support
- [GitHub #24854](https://github.com/zephyrproject-rtos/zephyr/issues/24854) - docs: Using third-party libraries not well documented in Memory partitions docs
- [GitHub #24733](https://github.com/zephyrproject-rtos/zephyr/issues/24733) - Misconfigured environment
- [GitHub #24200](https://github.com/zephyrproject-rtos/zephyr/issues/24200) - USB GET\_INTERFACE response always 0, even when an alternate setting is used
- [GitHub #24051](https://github.com/zephyrproject-rtos/zephyr/issues/24051) - double to sensor\_val
- [GitHub #23745](https://github.com/zephyrproject-rtos/zephyr/issues/23745) - Align PS/2 handlers with the handlers found in other drivers
- [GitHub #23723](https://github.com/zephyrproject-rtos/zephyr/issues/23723) - Poor sinf/cosf performance compared to the Segger math libraries
- [GitHub #23349](https://github.com/zephyrproject-rtos/zephyr/issues/23349) - Question: How to add external soc, board, DTS, drivers and libs?
- [GitHub #22731](https://github.com/zephyrproject-rtos/zephyr/issues/22731) - Improve docker CI documentation
- [GitHub #22705](https://github.com/zephyrproject-rtos/zephyr/issues/22705) - Implement counter driver for lpcxpresso55s69
- [GitHub #22702](https://github.com/zephyrproject-rtos/zephyr/issues/22702) - Implement I2S driver for lpcxpresso55s69
- [GitHub #22455](https://github.com/zephyrproject-rtos/zephyr/issues/22455) - How to assign USB endpoint address manually in stm32f4\_disco for CDC ACM class driver
- [GitHub #22210](https://github.com/zephyrproject-rtos/zephyr/issues/22210) - Bluetooth - bt\_gatt\_get\_value\_attr\_by\_uuid
- [GitHub #22131](https://github.com/zephyrproject-rtos/zephyr/issues/22131) - ARM Cortex\_R: CONFIG\_USERSPACE: external interrupts are disabled during system calls
- [GitHub #21869](https://github.com/zephyrproject-rtos/zephyr/issues/21869) - IPv6 neighbors get added too eagerly
- [GitHub #21648](https://github.com/zephyrproject-rtos/zephyr/issues/21648) - improve documentation on meta-IRQ threads
- [GitHub #21519](https://github.com/zephyrproject-rtos/zephyr/issues/21519) - RFC: libc: thread-safe newlib
- [GitHub #21339](https://github.com/zephyrproject-rtos/zephyr/issues/21339) - Expired IPv6 router causes an infinite loop
- [GitHub #21293](https://github.com/zephyrproject-rtos/zephyr/issues/21293) - adding timeout the I2C read/write functions for the stm32 port
- [GitHub #21205](https://github.com/zephyrproject-rtos/zephyr/issues/21205) - get\_device\_list only available if power management invoked
- [GitHub #21167](https://github.com/zephyrproject-rtos/zephyr/issues/21167) - libraries.libc.newlib test fails
- [GitHub #20576](https://github.com/zephyrproject-rtos/zephyr/issues/20576) - DTS overlay files must include full path name
- [GitHub #20409](https://github.com/zephyrproject-rtos/zephyr/issues/20409) - USB: Create webusb shell
- [GitHub #20236](https://github.com/zephyrproject-rtos/zephyr/issues/20236) - usb: api: Cleanup of current inclusion path for USB
- [GitHub #20171](https://github.com/zephyrproject-rtos/zephyr/issues/20171) - support external spi nor flash on mimxrt1060-evk
- [GitHub #19882](https://github.com/zephyrproject-rtos/zephyr/issues/19882) - Add support for multiple channel sampling to STM32 ADC driver
- [GitHub #19328](https://github.com/zephyrproject-rtos/zephyr/issues/19328) - Logger could block in thread at certain log message pool usage
- [GitHub #18960](https://github.com/zephyrproject-rtos/zephyr/issues/18960) - [Coverity CID :203908]Error handling issues in /lib/libc/newlib/libc-hooks.c
- [GitHub #18896](https://github.com/zephyrproject-rtos/zephyr/issues/18896) - Concurrent Multi-Protocol Support NRF52840
- [GitHub #18850](https://github.com/zephyrproject-rtos/zephyr/issues/18850) - Bluetooth: controller: Advertiser following directed advertiser will have corrupt data
- [GitHub #18386](https://github.com/zephyrproject-rtos/zephyr/issues/18386) - [Coverity CID :203443]Memory - corruptions in /subsys/bluetooth/host/rfcomm.c
- [GitHub #18351](https://github.com/zephyrproject-rtos/zephyr/issues/18351) - logging: 32 bit float values don’t work.
- [GitHub #18316](https://github.com/zephyrproject-rtos/zephyr/issues/18316) - Support for unregistering bt\_conn callbacks
- [GitHub #18042](https://github.com/zephyrproject-rtos/zephyr/issues/18042) - Only corporate members can join the slack channel
- [GitHub #17748](https://github.com/zephyrproject-rtos/zephyr/issues/17748) - stm32: clock-control: Remove usage of SystemCoreClock
- [GitHub #17692](https://github.com/zephyrproject-rtos/zephyr/issues/17692) - Proper way for joining a multicast group (NRF52840/OpenThread)
- [GitHub #17375](https://github.com/zephyrproject-rtos/zephyr/issues/17375) - Add VREF, TEMPSENSOR, VBAT internal channels to the stm32 adc driver
- [GitHub #17021](https://github.com/zephyrproject-rtos/zephyr/issues/17021) - revise concurrency control in kernel/userspace.c
- [GitHub #16761](https://github.com/zephyrproject-rtos/zephyr/issues/16761) - nrf52840 usb driver with openthread
- [GitHub #16671](https://github.com/zephyrproject-rtos/zephyr/issues/16671) - ideas for future of the settings
- [GitHub #16231](https://github.com/zephyrproject-rtos/zephyr/issues/16231) - Add CONFIG\_UART\_DYNAMIC\_SETTINGS option
- [GitHub #15841](https://github.com/zephyrproject-rtos/zephyr/issues/15841) - Support AT86RF233
- [GitHub #15793](https://github.com/zephyrproject-rtos/zephyr/issues/15793) - Unable to load binaries into iotdk
- [GitHub #15676](https://github.com/zephyrproject-rtos/zephyr/issues/15676) - Support instrumentation for time spent in various power states
- [GitHub #15555](https://github.com/zephyrproject-rtos/zephyr/issues/15555) - Counter Docs Missing Callback Context Note
- [GitHub #14308](https://github.com/zephyrproject-rtos/zephyr/issues/14308) - Better integration between system and device power modes.
- [GitHub #12405](https://github.com/zephyrproject-rtos/zephyr/issues/12405) - add test to catch issues fixed in PR #12384
- [GitHub #11773](https://github.com/zephyrproject-rtos/zephyr/issues/11773) - Add Bluetooth support for Silicon Labs EFR32MG12
- [GitHub #11702](https://github.com/zephyrproject-rtos/zephyr/issues/11702) - Add support for nrfx i2s driver
- [GitHub #11519](https://github.com/zephyrproject-rtos/zephyr/issues/11519) - Add at least build test for cc1200
- [GitHub #11193](https://github.com/zephyrproject-rtos/zephyr/issues/11193) - ARM V8M Trusted Execution Environments and Zephyr
- [GitHub #11028](https://github.com/zephyrproject-rtos/zephyr/issues/11028) - CONFIG\_LOAPIC\_SPURIOUS\_VECTOR not being tested
- [GitHub #11000](https://github.com/zephyrproject-rtos/zephyr/issues/11000) - USB 2.0 high-speed support in Zephyr
- [GitHub #10930](https://github.com/zephyrproject-rtos/zephyr/issues/10930) - Extending string formatting function
- [GitHub #10676](https://github.com/zephyrproject-rtos/zephyr/issues/10676) - Feature Required: DFU over Thread network
- [GitHub #10378](https://github.com/zephyrproject-rtos/zephyr/issues/10378) - watchdog: Limitation with the current watchdog API for Nordic devices
- [GitHub #10324](https://github.com/zephyrproject-rtos/zephyr/issues/10324) - Publish PDF with the release doc build
- [GitHub #10198](https://github.com/zephyrproject-rtos/zephyr/issues/10198) - Add support for FRDM-STBC-AGM01 sensor shield
- [GitHub #8876](https://github.com/zephyrproject-rtos/zephyr/issues/8876) - Adapt net/l2/ieee802154 subsystem to new shell subsystem
- [GitHub #8275](https://github.com/zephyrproject-rtos/zephyr/issues/8275) - when zephyr can support popular IDE develop?
- [GitHub #7001](https://github.com/zephyrproject-rtos/zephyr/issues/7001) - ST Sensors: Driver factorization
- [GitHub #6777](https://github.com/zephyrproject-rtos/zephyr/issues/6777) - Add copyright handling to contributing doc
- [GitHub #6657](https://github.com/zephyrproject-rtos/zephyr/issues/6657) - Question: Is Bluetooth avrcp supported in Zephyr? Or any plan?
- [GitHub #6493](https://github.com/zephyrproject-rtos/zephyr/issues/6493) - need APIs for ranged random number generation
- [GitHub #6450](https://github.com/zephyrproject-rtos/zephyr/issues/6450) - Several devices of same type on same bus - how to address?
- [GitHub #6117](https://github.com/zephyrproject-rtos/zephyr/issues/6117) - Make sanitycheck aware of DTS and HW support
- [GitHub #4911](https://github.com/zephyrproject-rtos/zephyr/issues/4911) - Filesystem support for qemu
- [GitHub #1392](https://github.com/zephyrproject-rtos/zephyr/issues/1392) - No module named ‘elftools’
- [GitHub #3886](https://github.com/zephyrproject-rtos/zephyr/issues/3886) - Add mutual authentication to net/crypto examples
- [GitHub #3885](https://github.com/zephyrproject-rtos/zephyr/issues/3885) - Add real entropy to crypto-based net samples
- [GitHub #3884](https://github.com/zephyrproject-rtos/zephyr/issues/3884) - Improve the TLS and DTLS examples to use best practices on security
- [GitHub #3879](https://github.com/zephyrproject-rtos/zephyr/issues/3879) - k\_thread\_abort vs k\_thread->fn\_abort()
- [GitHub #3677](https://github.com/zephyrproject-rtos/zephyr/issues/3677) - Implement HCI Zephyr extensions
- [GitHub #3199](https://github.com/zephyrproject-rtos/zephyr/issues/3199) - xtensa: simplify linker scripts
- [GitHub #2811](https://github.com/zephyrproject-rtos/zephyr/issues/2811) - Investigate having timeout code track tick deadlines instead of deltas
- [GitHub #2619](https://github.com/zephyrproject-rtos/zephyr/issues/2619) - Define APIs for hashing/ Message Authentication
- [GitHub #2248](https://github.com/zephyrproject-rtos/zephyr/issues/2248) - Split LE Controller: style fixes
