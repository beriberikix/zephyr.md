---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/release-notes-2.5.html
original_path: releases/release-notes-2.5.html
---

# Zephyr 2.5.0

We are pleased to announce the release of Zephyr RTOS version 2.5.0.

Major enhancements with this release include:

- Introduced support for the SPARC processor architecture and the LEON
  processor implementation.
- Added Thread Local Storage (TLS) support
- Added support for per thread runtime statistics
- Added support for building with LLVM on X86
- Added new synchronization mechanisms using Condition Variables
- Add support for demand paging, initial support on X86.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following CVEs are addressed by this release:

- CVE-2021-3323: Under embargo until 2021-04-14
- CVE-2021-3321: Under embargo until 2021-04-14
- CVE-2021-3320: Under embargo until 2021-04-14

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Known issues

You can check all currently known issues by listing them using the GitHub
interface and listing all issues with the [bug label](https://github.com/zephyrproject-rtos/zephyr/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## API Changes

- Removed SETTINGS\_USE\_BASE64 support as its been deprecated for more than
  two releases.
- The [`lwm2m_rd_client_start()`](../doxygen/html/group__lwm2m__api.md#ga9dfd46b8a535b1f28e644dc18f57fd79) function now accepts an additional
  `flags` parameter, which allows to configure current LwM2M client session,
  for instance enable bootstrap procedure in the current session.
- LwM2M execute now supports arguments. The execute callback
  [`lwm2m_engine_execute_cb_t`](../doxygen/html/group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) is extended with an `args` parameter
  which points to the CoAP payload that comprises the arguments, and an
  `args_len` parameter to indicate the length of the `args` data.
- Changed vcnl4040 dts binding default for property ‘proximity-trigger’.
  Changed the default to match the HW POR state for this property.
- The [`clock_control_async_on()`](../doxygen/html/group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf) function will now take `callback` and
  `user_data` as arguments instead of structure which contained list node,
  callback and user data.
- The [`mqtt_keepalive_time_left()`](../doxygen/html/group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b) function now returns -1 if keep alive
  messages are disabled by setting `CONFIG_MQTT_KEEPALIVE` to 0.
- The `CONFIG_LEGACY_TIMEOUT_API` mode has been removed. All kernel
  timeout usage must use the new-style k\_timeout\_t type and not the
  legacy/deprecated millisecond counts.
- The [`coap_pending_init()`](../doxygen/html/group__coap.md#ga868f792abf555f01c28caa5413d9e84c) function now accepts an additional `retries`
  parameter, allowing to specify the maximum retransmission count of the
  confirmable message.
- The `CONFIG_BT_CTLR_CODED_PHY` is now disabled by default for builds
  combining both Bluetooth host and controller.
- The [`coap_packet_append_payload()`](../doxygen/html/group__coap.md#gadcd3a93a702a2a0b428f39b71dd67954) function will now take a pointer to a
  constant buffer as the `payload` argument instead of a pointer to a writable
  buffer.
- The [`coap_packet_init()`](../doxygen/html/group__coap.md#ga90e6aab174f8977f0a3b5fbe1a20297c) function will now take a pointer to a constant
  buffer as the `token` argument instead of a pointer to a writable buffer.
- A new [Regulators](../hardware/peripherals/regulators.md#regulator-api) API has been added to support controlling power
  sources. Regulators can also be associated with devicetree nodes, allowing
  drivers to ensure the device they access has been powered up. For simple
  GPIO-only regulators a devicetree property `supply-gpios` is defined as a
  standard way to identify the control signal in nodes that support power
  control.
- `fs_tile_t` objects must now be initialized by calling
  [`fs_file_t_init()`](../doxygen/html/group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564) before their first use.
- `fs_dir_t` objects must now be initialized by calling
  [`fs_dir_t_init()`](../doxygen/html/group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3) before their first use.

### Deprecated in this release

- Nordic nRF5340 PDK board deprecated and planned to be removed in 2.6.0.
- ARM Musca-A board and SoC support deprecated and planned to be removed in 2.6.0.
- DEVICE\_INIT was deprecated in favor of utilizing DEVICE\_DEFINE directly.
- DEVICE\_AND\_API\_INIT was deprecated in favor of DEVICE\_DT\_INST\_DEFINE and
  DEVICE\_DEFINE.
- Bluetooth

  - Deprecated the `bt_set_id_addr()` function, use [`bt_id_create()`](../doxygen/html/group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)
    before calling [`bt_enable()`](../doxygen/html/group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b) instead. When `CONFIG_PRIVACY` is
    enabled a valid IRK has to be supplied by the application for this case.

### Removed APIs in this release

- Bluetooth

  - The deprecated BT\_LE\_SCAN\_FILTER\_DUPLICATE define has been removed,
    use BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE instead.
  - The deprecated BT\_LE\_SCAN\_FILTER\_WHITELIST define has been removed,
    use BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST instead.
  - The deprecated bt\_le\_scan\_param::filter\_dup argument has been removed,
    use bt\_le\_scan\_param::options instead.
  - The deprecated bt\_conn\_create\_le() function has been removed,
    use bt\_conn\_le\_create() instead.
  - The deprecated bt\_conn\_create\_auto\_le() function has been removed,
    use bt\_conn\_le\_create\_auto() instead.
  - The deprecated bt\_conn\_create\_slave\_le() function has been removed,
    use bt\_le\_adv\_start() instead with bt\_le\_adv\_param::peer set to the remote
    peers address.
  - The deprecated BT\_LE\_ADV\_\* macros have been removed,
    use the BT\_GAP\_ADV\_\* enums instead.
  - The deprecated bt\_conn\_security function has been removed,
    use bt\_conn\_set\_security instead.
  - The deprecated BT\_SECURITY\_\* defines NONE, LOW, MEDIUM, HIGH, FIPS have been
    removed, use the L0, L1, L2, L3, L4 defines instead.
  - The deprecated BT\_HCI\_ERR\_AUTHENTICATION\_FAIL define has been removed,
    use BT\_HCI\_ERR\_AUTH\_FAIL instead.
- Kernel

  - The deprecated k\_mem\_pool API has been removed entirely (for the
    past release it was backed by a k\_heap, but maintained a
    compatible API). Now all instantiated heaps must be
    sys\_heap/k\_heaps. Note that the new-style heap is a general
    purpose allocator and does not make the same promises about block
    alignment/splitting. Applications with such requirements should
    look at porting their logic, or perhaps at the k\_mem\_slab utility.

### Stable API changes in this release

## Kernel

- Added support for per thread runtime statistics
- Added new synchronization mechanisms using Condition Variables
- Thread Local Storage (TLS)

  - Introduced thread local storage support for the following architectures:

    - ARC
    - Arm Cortex-M
    - Arm Cortex-R
    - AArch64
    - RISC-V
    - Sparc
    - x86 and x86\_64
    - Xtensa
  - This allows variables declared with `__thread` keyword to be allocated
    on a per-thread basis, and every thread has its own copy of these
    variables.
  - Enable via [`CONFIG_THREAD_LOCAL_STORAGE`](../kconfig.md#CONFIG_THREAD_LOCAL_STORAGE "CONFIG_THREAD_LOCAL_STORAGE").
  - `errno` can be stored inside TLS if [`CONFIG_ERRNO_IN_TLS`](../kconfig.md#CONFIG_ERRNO_IN_TLS "CONFIG_ERRNO_IN_TLS")
    is enabled (together with [`CONFIG_ERRNO`](../kconfig.md#CONFIG_ERRNO "CONFIG_ERRNO")). This allow user
    threads to access the value of `errno` without making a system call.
- Memory Management

  - Added page frame management for physical memory to keep track of
    the status of each page frame.
  - Added [`k_mem_map()`](../doxygen/html/group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb) which allows applications to increase
    the data space available via anonymous memory mappings.
  - Added [`k_mem_free_get()`](../doxygen/html/group__kernel__memory__management.md#gabb315b4994193147e9f51b0c3268bfcd) which returns the amount of
    physical anonymous memory remaining.
  - Paging structure must now be pre-allocated so that there is no need
    to do memory allocations when mapping memory. Because of this,
    [`arch_mem_map()`](../doxygen/html/group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94) may no longer fail.
- Demand Paging

  - Introduced the framework for demand paging and infrastructure for
    custom eviction algorithms and implementation of backing stores.
  - Currently the whole kernel is pinned and remaining physical memory
    can be used for paging.

## Architectures

- ARC

  - Fixed execution on ARC HS with one interrupt bank and fast interrupts (FIRQ)
    enabled
  - Hardened SMP support
  - Improved mdb west runner to support simulation on SMP nSIM-based
    configurations
  - Improved mdb west runner to support nSIM-based configurations execution
    on real HW (FPGA-based)
  - Added documentation page with Zephyr support status on ARC processor
  - Added coverage support for nSIM-based configurations
  - Switched to upstream OpenOCD for ARC
  - Various minor fixes/improvements for ARC MWDT toolchain infrastructure
- ARM

  - AARCH32

    - Introduced the functionality for chain-loadable Zephyr
      firmware images to force the initialization of internal
      architecture state during early system boot (Cortex-M).
    - Changed the default Floating Point Services mode to
      Shared FP registers mode.
    - Enhanced Cortex-M Shared FP register mode by implementing
      dynamic lazy FP register stacking in threads.
    - Added preliminary support for Cortex-R7 variant.
    - Fixed inline assembly code in Cortex-M system calls.
    - Enhanced and fixed Cortex-M TCS support.
    - Enabled interrupts before switching to main in single-thread
      Cortex-M builds (CONFIG\_MULTITHREADING=n).
    - Fixed vector table relocation in non-XIP Cortex-M builds.
    - Fixed exception exit routine for fatal error exceptions in
      Cortex-R.
    - Fixed interrupt nesting in ARMv7-R architecture.
  - AARCH64

    - Fixed registers printing on error and beautified crash dump output
    - Removed CONFIG\_SWITCH\_TO\_EL1 symbol. By default the execution now drops
      to EL1 at boot
    - Deprecated booting from EL2
    - Improved assembly code and errors catching in EL3 and EL1 during the
      start routine
    - Enabled support for EL0 in the page tables
    - Fixed vector table alignment
    - Introduced support to boot Zephyr in NS mode
    - Fixed alignment fault in z\_bss\_zero
    - Added PSCI driver
    - Added ability to generate image header
    - Improved MMU code and driver
- RISC-V

  - Added support for PMP (Physical Memory Protection).
    Integrate PMP in Zephyr allow to support userspace (with shared
    memory) and stack guard features.
- SPARC

  - Added support for the SPARC architecture, compatible with the SPARC V8
    specification and the SPARC ABI.
  - FPU is supported in both shared and unshared FP register mode.
- x86

  - Enabled soft float support for Zephyr SDK
  - `CONFIG_X86_MMU_PAGE_POOL_PAGES` is removed as paging structure
    must now be pre-allocated.
  - Mapping of physical memory has changed:

    - This allows a smaller virtual address space thus requiring a smaller
      paging structure.
    - Only the kernel image is mapped when [`CONFIG_ACPI`](../kconfig.md#CONFIG_ACPI "CONFIG_ACPI") is not enabled.
    - When [`CONFIG_ACPI`](../kconfig.md#CONFIG_ACPI "CONFIG_ACPI") is enabled, the previous behavior to map
      all physical memory is retained as platforms with ACPI are usually not
      memory constrained and can accommodate bigger paging structure.
  - Page fault handler has been extended to support demand paging.

## Boards & SoC Support

- Added support for these SoC series:

  - Cypress PSoC-63
  - Intel Elkhart Lake
- Made these changes in other SoC series:
- Changes for ARC boards:

  - Added icount support for ARC QEMU boards
  - Added MWDT compiler options for HSDK board
  - Added missing taps into JTAG chain for the dual-core configuration of the
    HSDK board
- Added support for these ARM boards:

  - Cypress CY8CKIT\_062\_BLE board
- Added support for these x86 boards:

  - Elkhart Lake CRB board
  - ACRN configuration on Elkhart Lake CRB board
  - Slim Bootloader configuration on Elkhart Lake CRB board
- Added support for these SPARC boards:

  - GR716-MINI LEON3FT microcontroller development board
  - Generic LEON3 board configuration for GRLIB FPGA reference designs
  - SPARC QEMU for emulating LEON3 processors and running kernel tests
- Added support for these NXP boards:

  - LPCXpresso55S28
  - MIMXRT1024-EVK
- Added support for these STM32 boards and SoCs :

  - Cortex-M Trace Reference Board V1.2 (SEGGER TRB STM32F407)
  - MikroE Clicker 2 for STM32
  - STM32F103RCT6 Mini
  - ST Nucleo F303K8
  - ST Nucleo F410RB
  - ST Nucleo H723ZG
  - ST Nucleo L011K4
  - ST Nucleo L031K6
  - ST Nucleo L433RC-P
  - ST STM32L562E-DK Discovery
  - STM32F105xx and STM32F103xG SoC variants
  - STM32G070xx SoC variants
  - STM32G474xB/C SoC variants
  - STM32L071xx SoC variants
  - STM32L151xC and STM32L152xC SoC variants
- Made these global changes in STM32 boards and SoC series:

  - Pin control configuration is now done through devicetree and existing
    macros to configure pins in pinmux.c files are tagged as deprecated.
    The new pin settings are provided thanks to .dtsi files distributed in
    hal\_stm32 module.
  - Generic LL headers, also distributed in hal\_stm32 module, are now available
    to abstract series references in drivers.
  - Hardware stack protection is now default on all boards with enabled MPU
    (SRAM > 64K ), excluding F0/G0/L0 series.
  - West flash STM32CubeProgrammer runner was added as a new option for STM32
    boards flashing (to be installed separately).
- Made these changes in other boards:

  - CY8CKIT\_062\_WIFI\_BT\_M0: was renamed to CY8CKIT\_062\_WIFI\_BT.
  - CY8CKIT\_062\_WIFI\_BT\_M4: was moved into CY8CKIT\_062\_WIFI\_BT.
  - CY8CKIT\_062\_WIFI\_BT: Now M0+/M4 are at same common board.
  - nRF5340 DK: Selected TF-M as the default Secure Processing Element
    (SPE) when building Zephyr for the non-secure domain.
  - SAM4E\_XPRO: Added support to SAM-BA ROM bootloader.
  - SAM4S\_XPLAINED: Added support to SAM-BA ROM bootloader.
  - Extended LPCXpresso55S69 to support dual-core.
  - Enhanced MIMXRT1064-EVK to support QSPI flash storage and LittleFS.
  - Updated MIMXRT685-EVK to increase the core clock frequency.
  - Updated NXP i.MX RT, Kinetis, and LPC boards to enable hardware stack
    protection by default.
  - Fixed Segger RTT and SystemView support on NXP i.MX RT boards.
  - Demand paging is turned on by default for `qemu_x86_tiny`.
  - Updated zefi.py to use cross-compiler while building Zephyr.
  - Enabled code coverage report for `qemu_x86_64`.
  - Removed support for legacy APIC timer driver.
  - Added common memory linker for x86 SoCs.
  - Enabled configuration to reserve the first megabyte in x86 SoCs.
- Added support for these following shields:

  - Inventek es-WIFI shield
  - Sharp memory display generic shield

## Drivers and Sensors

- ADC

  - Added support for ADC on STM32G0 Series.
  - Introduced the `adc_sequence_options::user_data` field.
- CAN

  - We reworked the configuration API.
    A user can now specify the timing manually (define prop segment,
    phase segment1, phase segment2, and prescaler) or use a newly introduced
    algorithm to calculate optimal timing values from a bitrate and sample point.
    The bitrate and sample point can be specified in the devicetree too.
    It is possible to change the timing values at runtime now.
  - We reworked the zcan\_frame struct due to undefined behavior.
    The std\_id (11-bit) and ext\_id (29-bit) are merged to a single id
    field (29-bit). The union of both IDs was removed.
  - We made the CANbus API CAN-FD compatible.
    The zcan\_frame data-field can have a size of >8 bytes now.
    A flag was introduced to mark a zcan\_frame as CAN-FD frame.
    A flag was introduced that enables a bitrate switch in CAN-FD frames.
    The configuration API supports an additional timing parameter for the CAN-FD
    data-phase.
  - drivers are converted to use the new DEVICE\_DT\_\* macros.
- Clock Control

  - Added NXP LPC driver.
- DAC

  - STM32: Enabled support for G0 and H7 series.
  - Added TI DACx3608 driver.
- DMA

  - kmalloc was removed from STM32 DMAMUX driver initialization.
- EEPROM

  - Marked the EEPROM API as stable.
  - Added support for AT24Cxx devices.
- Ethernet

  - Added support for Distributed Switch Architecture (DSA) devices.
    Currently only ip\_k66f board supports DSA.
  - Added support for w5500 Ethernet controller.
  - Reworked the NXP MCUX driver to use DT\_INST\_FOREACH.
- Flash

  - CONFIG\_NORDIC\_QSPI\_NOR\_QE\_BIT has been removed. The
    quad-enable-requirements devicetree property should be used instead.
  - MPU\_ALLOW\_FLASH\_WRITE is now default on STM32 boards when MPU is enabled.
  - Add driver for STM32H7 and STM32L1 SoC series.
  - Add QSPI NOR Flash controller support for STM32 family.
  - Added NXP LPC legacy flash driver.
  - Added NXP FlexSPI flash driver for i.MX RT SoCs.
  - Added support for nRF53 Series SoCs in the nRF QSPI NOR flash driver
    (nrf\_qspi\_nor).
- GPIO

  - Added Cypress PSoC-6 driver.
  - Added Atmel SAM4L driver.
- Hardware Info

  - Added Cypress PSoC-6 driver.
- I2C

  - Added driver support for lmx6x, it8xxx2, and npcx7 platforms.
  - Added Atmel SAM4L TWIM driver.
  - Added I2C slave support in the microchip i2c driver.
  - Reversed 2.4 decision to downgrade I2C eeprom slave driver to a
    test. It’s a driver again.
- I2S
- IEEE 802.15.4

  - nRF:

    - Added IEEE 802.15.4 support for nRF5340.
    - Added support for failed rx notification.
  - cc13xx/cc26xx:

    - Added multi-protocol radio support.
    - Added sub-ghz support.
    - Added raw mode support.
- Interrupt Controller

  - Added Cypress PSoC-6 Cortex-M0+ interrupt multiplexer driver.
- memc

  - Added FMC/SDRAM memory controller for STM32 family
- Modem

  - Improved RX with HW flow control in modem interface API.
  - Improved reading from interface in command handler.
  - Fixed race condition when waiting on cmd reply.
  - Added support for Quectel bg95 modem.
  - Constified modem command structures to reduce RAM usage.
  - hl7800:

    - Fixed buffer handling issues.
    - Fixed setting DNS address.
    - Fixed file open in fw update.
    - Fixed cases where socket would not close.
  - sara-r4:

    - Added sanity timeout for @ prompt.
    - Fixed redundant wait after sendto.
    - Improved offload\_sendmsg() support.
    - Added Kconfig to configure RSSI work.
    - Added direct CMD to catch @ when sending data.
    - Sanitize send\_socket\_data() semaphore handling.
  - bg96:

    - Fixed UDP packet management.
  - GSM:

    - Added start/stop API support so that application can turn off
      the GSM/PPP modem if needed to save power.
    - Avoid wrapping each byte in muxing headers in PPP.
    - Added support to remove PPP IPv4 ipcp address on network down.
- PECI
- Pinmux

  - STM32 pinmux driver has been reworked to allow pin configuration using
    devicetree definitions. The previous C macros are now deprecated.
- PWM

  - Added support for generating PWM signal based on RTC in the pwm\_nrf5\_sw
    driver.
  - Added optional API for capturing the PWM pulse width and period.
  - Added PWM capture driver for the NXP Kinetis Pulse Width Timer (PWT).
  - Removed the DesignWare and PCA9685 controller drivers.
- Sensor

  - Fixed current conversion to milliamps in the MAX17055 driver.
  - Added multi-instance support to the FXOS8700, IIS2DLPC, and IIS2ICLX
    drivers.
  - Added Invensense ICM42605 driver.
  - Added NXP MCUX ACMP driver.
  - Fixed gyro units in the FXAS21002 driver.
  - Fixed pressure and temperature registers in the DPS310 driver.
  - Added I2C support to the BMI160 driver.
  - Added IIS2ICLX driver.
  - Aligned ST sensor drivers to stmemsc HAL i/f v1.03.
  - Fixed temperature units in the IIS2MDC driver.
  - Added emulator for Bosch BMI160 accelerometer.
  - Added device power management support to the LIS2MDL driver.
- Serial

  - Added ASYNC API support on STM32 family.
- SPI

  - Enhanced NXP MCUX Flexcomm driver to support DMA.
- Timer
- USB

  - Reworked nrfx driver to use mem\_slab for event elements and
    and static memory for OUT endpoints.
  - Fixed ZLP handling for nrfx driver.
  - Added support for USB Device mode on STM32F105xx parts.
- Video
- Watchdog

  - Added NXP i.MX RT driver.
- WiFi

  - eswifi:

    - Added uart bus interface. This enables all Inventek modules with
      IWIN AT Commands firmware.
  - esp:

    - Fixed thread-safety access on esp\_socket operations.
    - Fixed scheduling each RX packet on separate work thread.
    - Fixed initializing socket work structures only once.
    - Reworked +IPD and +CIPRECVDATA handling.
    - Stopped locking scheduler when sending data.
    - Added DHCP/Static IP Support.
    - Added support using DNS servers.
    - Enhanced CWMODE support.
    - Added support for configuring hostname.
    - Added support for power-gpios to enable ESP module.
    - Added support 32-bit length in +IPD.
    - Added support for reconfiguring UART baudrate after initial communication.
    - Improved packet allocation failure handling by closing stream sockets.

## Networking

- CoAP:

  - Fixed discovery response formatting according to RFC6690.
  - Randomized initial ACK timeout.
  - Reworked pending retransmission logic.
  - Fixed long options encoding.
- DHCPv4:

  - Added start/bound/stop network management events for DHCPv4.
  - Fixed timeout scheduling with multiple network interfaces.
  - Fixed timeout on entry to bound state.
  - Fixed invalid timeout on send failure.
  - Fixed bounds checking in timeout.
  - Fixed endian issue.
  - Added randomization to message interval.
  - Limited message interval to a maximum of 64 seconds.
- DNS:

  - Added resolving literal IP addresses even when DNS is disabled.
  - Added support for DNS Service Discovery (dns-sd).
  - Fixed getaddrinfo() to respect socket type hints.
- HTTP:

  - Added chunked encoding body support to HTTP client API.
- IPv6:

  - Tweaked IPv6 DAD and RS timeout handling.
  - Fixed multiple endian issues.
  - Fixed unaligned access to IPv6 address.
- LwM2M:

  - Added dimension discovery support.
  - Implemented bootstrap discovery.
  - Fixed message find based on pending/reply.
  - Reworked bootstrap DELETE operation.
  - Added path generation macro.
  - Added a way to notify the application on network error.
  - Added a callback to notify socket errors to applications.
  - Send Registration Update on lifetime changes.
  - Fixed PULL FW update in case of URI parse errors.
  - Fixed separate response handling.
  - Start notify sequence numbers on 0.
  - Enhanced packing of TLV integers more efficiently.
  - Improved token generation.
  - Fixed the bootstrap to be optional.
- Misc:

  - Allow user to select pre-emptive or co-operative RX/TX threads.
  - Refactored RX and TX thread priorities.
  - Only start the network logging backend if the autostarting is enabled.
  - Added support for simultaneous UDP/TCP and raw sockets in applications.
  - Enabled solicit node multicast group registration for Bluetooth IPSP
    connections.
  - Added net\_buf\_remove API to manipulate data at the end of network buffers.
  - Added checks to syslog-net that ensure immediate logging mode is not set as
    the network logging is not compatible with it.
  - Implemented SO\_RCVTIMEO socket receive timeout option.
  - Added support to update unique hostname on link address changes.
  - Added locking to IPv6, CAN and packet socket bind calls.
  - Added network management events monitor support.
- MQTT:

  - Reset client state before notifying application with MQTT\_EVT\_DISCONNECT event.
- OpenThread:

  - Added support for RCP (Radio Co-Processor) mode.
  - Made radio workqueue stack size configurable.
  - Added joining thread multicast addresses which are added to Zephyr.
  - Added SRP Kconfig options.
  - Enabled CSL and TREL config options.
  - Added option to enable software CSMA backoff.
  - Added support to configure platform info.
  - Added Kconfigs to change values in Zephyr.
  - Removed unused defines from platform configuration.
- Samples:

  - Added TagoIO IoT Cloud HTTP post sample.
  - Fixed the return code in MQTT Docker tests.
  - Added support to allow DHCPv4 or manually set addresses in zperf sample.
  - Use IPv4 instead of IPv6 in coap-server to support Docker based testing.
  - Added connection manager support to dumb\_http\_server\_mt sample.
  - Added support for large file in dumb\_http\_server\_mt sample.
  - Added support for running the gptp sample X seconds to support Docker based testing.
  - Added Docker based testing to http\_client sample.
  - Refractored code structure and reduced RAM usage of civetweb sample.
  - Added suspend/resume shell commands to gsm\_modem sample.
  - Added Docker based testing support to network logging sample.
- TCP:

  - The new TCP stack is enabled by default. Legacy TCP stack is deprecated but
    still available and scheduled for removal in next 2.6 release.
  - Added support to queue received out-of-order TCP data.
  - Added connection termination if the TCP handshake is not finalized.
  - Enhanced received TCP RST packet handling.
  - Fixed TCP connection from Windows 10.
- TLS:

  - Use Maximum Fragment Length (MFL) extension by default.
  - Added ALPN extension option to TLS.
  - Fixed TLS context leak on socket allocation failure.

## Bluetooth

- Host

  - When privacy has been enabled in order to advertise towards a
    privacy-enabled peer the BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA option must now
    be set, same as when privacy has been disabled.
- Mesh

  - The `bt_mesh_cfg_srv` structure has been deprecated in favor of a
    standalone Heartbeat API and Kconfig entries for default state values.
- BLE split software Controller
- HCI Driver

## USB

- USB synchronous transfer

  - Fixed possible deadlock in usb\_transfer\_sync().
  - Check added to prevent starting new transfer if an other transfer is
    already ongoing on same endpoint.
- USB DFU class

  - Made USB DFU class compatible with the target configuration that does not
    have a secondary image slot.
  - Support to use USB DFU within MCUBoot with single application slot mode.
  - Separate PID for DFU mode added to avoid problems caused by the host OS
    caching the remaining descriptors when switching to DFU mode.
  - Added timer for appDETACH state and revised descriptor handling to
    meet specification requirements.
- USB HID class

  - Reworked transfer handling after suspend and resume events.
- Samples

  - Reworked disk and FS configuration in MSC sample. MSC sample can be
    built with none or one of two supported file systems, LittleFS or FATFS.
    Disk subsystem can be flash or RAM based.

## Build and Infrastructure

- Improved support for additional toolchains:
- Devicetree

  - Support for legacy devicetree macros via
    `CONFIG_LEGACY_DEVICETREE_MACROS` was removed. All devicetree-based code
    should be using the new devicetree API introduced in Zephyr 2.3 and
    documented in [Devicetree access from C/C++](../build/dts/api-usage.md#dt-from-c). Information on flash partitions has moved
    to [Flash map](../services/storage/flash_map/flash_map.md#flash-map-api).
  - It is now possible to resolve at build time the device pointer associated
    with a device that is defined in devicetree, via `DEVICE_DT_GET`. See
    [Get a struct device from a devicetree node](../build/dts/howtos.md#dt-get-device).
  - Enhanced support for enumerated property values via new macros:

    - [`DT_ENUM_IDX_OR`](../doxygen/html/group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)
    - `DT_ENUM_TOKEN`
    - `DT_ENUM_UPPER_TOKEN`
  - New hardware specific macros:

    - [`DT_GPIO_CTLR_BY_IDX`](../doxygen/html/group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)
    - [`DT_GPIO_CTLR`](../doxygen/html/group__devicetree-gpio.md#gafbad7d0d7f7fb9338997482c8da0e566)
    - [`DT_MTD_FROM_FIXED_PARTITION`](../doxygen/html/group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)
  - Miscellaneous new node-related macros:

    - [`DT_GPARENT`](../doxygen/html/group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)
    - [`DT_INVALID_NODE`](../doxygen/html/group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)
    - [`DT_NODE_PATH`](../doxygen/html/group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)
    - [`DT_SAME_NODE`](../doxygen/html/group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)
  - Property access macro changes:

    - [`DT_PROP_BY_PHANDLE_IDX_OR`](../doxygen/html/group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b): new macro
    - [`DT_PROP_HAS_IDX`](../doxygen/html/group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c) now expands to a literal 0 or 1, not an
      expression that evaluates to 0 or 1
  - Dependencies between nodes are now exposed via new macros:

    - [`DT_DEP_ORD`](../doxygen/html/group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd), [`DT_INST_DEP_ORD`](../doxygen/html/group__devicetree-dep-ord.md#ga9c5e6f36c6e7a250368177a9f0713f86)
    - [`DT_REQUIRES_DEP_ORDS`](../doxygen/html/group__devicetree-dep-ord.md#ga22dd1b0c89eb5ddfbfdd1e723d44f509), [`DT_INST_REQUIRES_DEP_ORDS`](../doxygen/html/group__devicetree-dep-ord.md#gac7d43a7916bdc8c46fafeee0213e538c)
    - [`DT_SUPPORTS_DEP_ORDS`](../doxygen/html/group__devicetree-dep-ord.md#ga3f559e9a787792685ed08be124b374ae), [`DT_INST_SUPPORTS_DEP_ORDS`](../doxygen/html/group__devicetree-dep-ord.md#ga027cc1361d1e059dde039926980e26fa)
- West

  - Improve bossac runner. It supports now native ROM bootloader for Atmel
    MCUs and extended SAM-BA bootloader like Arduino and Adafruit UF2. The
    devices supported depend on bossac version inside Zephyr SDK or in users
    path. The recommended Zephyr SDK version is 0.12.0 or newer.

## Libraries / Subsystems

- File systems

  - API

    - Added [`fs_file_t_init()`](../doxygen/html/group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564) function for initialization of
      `fs_file_t` objects.
    - Added [`fs_dir_t_init()`](../doxygen/html/group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3) function for initialization of
      `fs_dir_t` objects.
  - `CONFIG_FS_LITTLEFS_FC_MEM_POOL` has been deprecated and
    should be replaced by [`CONFIG_FS_LITTLEFS_FC_HEAP_SIZE`](../kconfig.md#CONFIG_FS_LITTLEFS_FC_HEAP_SIZE "CONFIG_FS_LITTLEFS_FC_HEAP_SIZE").
- Management

  - MCUmgr

    - Added support for flash devices that have non-0xff erase value.
    - Added optional verification, enabled via
      `CONFIG_IMG_MGMT_REJECT_DIRECT_XIP_MISMATCHED_SLOT`, of an uploaded
      Direct-XIP binary, which will reject any binary that is not able to boot
      from base address of offered upload slot.
  - updatehub

    - Added support to Network Manager and interface overlays at UpdateHub
      sample. Ethernet is the default interface configuration and overlays
      can be used to change default configuration
    - Added WIFI overlay
    - Added MODEM overlay
    - Added IEEE 802.15.4 overlay [experimental]
    - Added BLE IPSP overlay as [experimental]
    - Added OpenThread overlay as [experimental].
- Settings
- Random
- POSIX subsystem
- Power management

  - Use a consistent naming convention using **pm\_** namespace.
  - Overhaul power states. New states [`pm_state`](../doxygen/html/group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) are more
    meaningful and ACPI alike.
  - Move residency information and supported power states to devicetree
    and remove related Kconfig options.
  - New power state changes notification API [`pm_notifier`](../doxygen/html/structpm__notifier.md)
  - Cleanup build options.
- LVGL

  - Library has been updated to minor release v7.6.1
- Storage

  - flash\_map: Added API to get the value of an erased byte in the flash\_area,
    see `flash_area_erased_val()`.
- DFU

> - boot: Reworked using MCUBoot’s bootutil\_public library which allow to use
>   API implementation already provided by MCUboot codebase and remove
>   zephyr’s own implementations.

- Crypto

  - mbedTLS updated to 2.16.9

## HALs

- HALs are now moved out of the main tree as external modules and reside in
  their own standalone repositories.

## MCUBoot

- bootloader

  - Added hardening against hardware level fault injection and timing attacks,
    see `CONFIG_BOOT_FIH_PROFILE_HIGH` and similar kconfig options.
  - Introduced Abstract crypto primitives to simplify porting.
  - Added ram-load upgrade mode (not enabled for zephy-rtos yet).
  - Renamed single-image mode to single-slot mode,
    see `CONFIG_SINGLE_APPLICATION_SLOT`.
  - Added patch for turning off cache for Cortex M7 before chain-loading.
  - Fixed bootstrapping in swap-move mode.
  - Fixed issue causing that interrupted swap-move operation might brick device
    if the primary image was padded.
  - Fixed issue causing that HW stack protection catches the chain-loaded
    application during its early initialization.
  - Added reset of Cortex SPLIM registers before boot.
  - Fixesd build issue that occurs if CONF\_FILE contains multiple file paths
    instead of single file path.
  - Added watchdog feed on nRF devices. See `CONFIG_BOOT_WATCHDOG_FEED` option.
  - Removed the flash\_area\_read\_is\_empty() port implementation function.
  - Initialize the ARM core configuration only when selected by the user,
    see `CONFIG_MCUBOOT_CLEANUP_ARM_CORE`.
  - Allow the final data chunk in the image to be unaligned in
    the serial-recovery protocol.
  - Kconfig: allow xip-revert only for xip-mode.
  - ext: tinycrypt: update ctr mode to stream.
  - Use minimal CBPRINTF implementation.
  - Configure logging to LOG\_MINIMAL by default.
  - boot: cleanup NXP MPU configuration before boot.
  - Fix nokogiri<=1.11.0.rc4 vulnerability.
  - bootutil\_public library was extracted as code which is common API for
    MCUboot and the DFU application, see `CONFIG_MCUBOOT_BOOTUTIL_LIB`
- imgtool

  - Print image digest during verify.
  - Add possibility to set confirm flag for hex files as well.
  - Usage of –confirm implies –pad.
  - Fixed ‘custom\_tlvs’ argument handling.
  - Add support for setting fixed ROM address into image header.
  - Fixed verification with protected TLVs.

## Trusted-Firmware-M

- Synchronized Trusted-Firmware-M module to the upstream v1.2.0 release.

## Documentation

## Tests and Samples

> - A sample was added to demonstrate how to use the ADC driver API.
> - Sanitycheck script was renamed to twister

## Issue Related Items

These GitHub issues were addressed since the previous 2.4.0 tagged
release:

- [GitHub #32221](https://github.com/zephyrproject-rtos/zephyr/issues/32221) - Sporadic kernel panics on stm32g4 flash erase/writes
- [GitHub #32203](https://github.com/zephyrproject-rtos/zephyr/issues/32203) - Cannot set static address when using hci\_usb or hci\_uart on nRF5340 attached to Linux Host
- [GitHub #32181](https://github.com/zephyrproject-rtos/zephyr/issues/32181) - samples: tests: Tests from samples/boards/nrf/nrfx fail
- [GitHub #32179](https://github.com/zephyrproject-rtos/zephyr/issues/32179) - samples: tests: Tests from samples/subsys/usb/audio fail
- [GitHub #32112](https://github.com/zephyrproject-rtos/zephyr/issues/32112) - intel\_adsp\_cavs15: a part of testcases run failed with same error
- [GitHub #31819](https://github.com/zephyrproject-rtos/zephyr/issues/31819) - intel\_adsp\_cavs15: signing not correct thus download firmware failed
- [GitHub #31675](https://github.com/zephyrproject-rtos/zephyr/issues/31675) - [Coverity CID :216790] Division or modulo by zero in tests/drivers/can/timing/src/main.c
- [GitHub #31607](https://github.com/zephyrproject-rtos/zephyr/issues/31607) - Bluetooth: host: bt\_conn\_auth\_cb callbacks are not called when pairing to BLE 4.1 central in BT\_SECURITY\_L4 mode.
- [GitHub #28685](https://github.com/zephyrproject-rtos/zephyr/issues/28685) - Bluetooth: Characteristic unsubscribe under indication load results in ATT timeout
- [GitHub #26495](https://github.com/zephyrproject-rtos/zephyr/issues/26495) - Make k\_poll work with KERNEL\_COHERENCE
- [GitHub #21033](https://github.com/zephyrproject-rtos/zephyr/issues/21033) - Read out heap space used and unallocated
- [GitHub #19655](https://github.com/zephyrproject-rtos/zephyr/issues/19655) - Milestones toward generalized representation of timeouts
- [GitHub #12028](https://github.com/zephyrproject-rtos/zephyr/issues/12028) - Enable 16550 UART driver on x86\_64
- [GitHub #32206](https://github.com/zephyrproject-rtos/zephyr/issues/32206) - CMSIS-DSP support seems broken on link
- [GitHub #32194](https://github.com/zephyrproject-rtos/zephyr/issues/32194) - Source files missing specification of SPDX-License-Identifier in comments
- [GitHub #32167](https://github.com/zephyrproject-rtos/zephyr/issues/32167) - Bluetooth: controller: conformance testcase failures
- [GitHub #32153](https://github.com/zephyrproject-rtos/zephyr/issues/32153) - Use of deprecated macro’s in dma\_iproc\_pax\_v1, and dma\_iproc\_pax\_v2
- [GitHub #32152](https://github.com/zephyrproject-rtos/zephyr/issues/32152) - DEVICE\_AND\_API\_INIT and DEVICE\_INIT deprecation marking is not working
- [GitHub #32151](https://github.com/zephyrproject-rtos/zephyr/issues/32151) - Use of deprecated macro’s in icm42605
- [GitHub #32143](https://github.com/zephyrproject-rtos/zephyr/issues/32143) - AArch64 idle loop corrupts IRQ state with CONFIG\_TRACING
- [GitHub #32142](https://github.com/zephyrproject-rtos/zephyr/issues/32142) - dtc: Unrecognized check name “unique\_unit\_address\_if\_enabled”
- [GitHub #32136](https://github.com/zephyrproject-rtos/zephyr/issues/32136) - z\_unpend1\_no\_timeout non-atomic
- [GitHub #32095](https://github.com/zephyrproject-rtos/zephyr/issues/32095) - guiconfig search fails
- [GitHub #32078](https://github.com/zephyrproject-rtos/zephyr/issues/32078) - build error with llvm: samples/subsys/fs/littlefs
- [GitHub #32070](https://github.com/zephyrproject-rtos/zephyr/issues/32070) - How to manage power consumption when working with peripheral\_hr sample on NRF52832
- [GitHub #32067](https://github.com/zephyrproject-rtos/zephyr/issues/32067) - Bluetooth: Mesh: Devkey and addr not stored correctly
- [GitHub #32064](https://github.com/zephyrproject-rtos/zephyr/issues/32064) - Minimal libc malloc() is unprotected
- [GitHub #32059](https://github.com/zephyrproject-rtos/zephyr/issues/32059) - Getting Started - Windows - Toolchain not found
- [GitHub #32048](https://github.com/zephyrproject-rtos/zephyr/issues/32048) - doc: power management: Remove references to previous PM states terminology
- [GitHub #32046](https://github.com/zephyrproject-rtos/zephyr/issues/32046) - LMP90xxx ADC driver fails to initialise more than one instance
- [GitHub #32045](https://github.com/zephyrproject-rtos/zephyr/issues/32045) - boards: Inaccurate values for ram/flash in nrf5340dk\_nrf5340\_cpuapp.yaml
- [GitHub #32040](https://github.com/zephyrproject-rtos/zephyr/issues/32040) - BT\_AUDIO\_UNICAST selection rejected in nightly tests
- [GitHub #32033](https://github.com/zephyrproject-rtos/zephyr/issues/32033) - Bluetooth mesh : LPN doesn’t receive messages from Friend
- [GitHub #32030](https://github.com/zephyrproject-rtos/zephyr/issues/32030) - dma: stm32: remove dump stream info in irq
- [GitHub #32015](https://github.com/zephyrproject-rtos/zephyr/issues/32015) - Thread local storage is broken when adding more thread variables
- [GitHub #32014](https://github.com/zephyrproject-rtos/zephyr/issues/32014) - Is there a sample that uses SAADC (analog to digital converter)?
- [GitHub #32007](https://github.com/zephyrproject-rtos/zephyr/issues/32007) - Wrong clock value at USART1 in STM32F2 dtsi file
- [GitHub #32005](https://github.com/zephyrproject-rtos/zephyr/issues/32005) - stm32: async uart tests fail
- [GitHub #32002](https://github.com/zephyrproject-rtos/zephyr/issues/32002) - Cannot build encrypted images on Zephyr
- [GitHub #31996](https://github.com/zephyrproject-rtos/zephyr/issues/31996) - tests/bluetooth/init/bluetooth.init.test\_ctlr\_peripheral\_iso fails to build on a few platforms
- [GitHub #31994](https://github.com/zephyrproject-rtos/zephyr/issues/31994) - drivers: flash: stm32h7: fix int/long int warnings
- [GitHub #31989](https://github.com/zephyrproject-rtos/zephyr/issues/31989) - nrfx\_uarte serial driver does not go to low power mode after setting off state
- [GitHub #31976](https://github.com/zephyrproject-rtos/zephyr/issues/31976) - dma: loop\_transfer issue on nucleo\_wb55rg
- [GitHub #31973](https://github.com/zephyrproject-rtos/zephyr/issues/31973) - Stm32 uart async driver changes offset after callback
- [GitHub #31952](https://github.com/zephyrproject-rtos/zephyr/issues/31952) - Linking fails with latest master on ARM64 platform
- [GitHub #31948](https://github.com/zephyrproject-rtos/zephyr/issues/31948) - tests: drivers: spi: spi\_loopback: became skipped whereas it used to be run
- [GitHub #31947](https://github.com/zephyrproject-rtos/zephyr/issues/31947) - Cleanup devicetree warnings generated by dtc
- [GitHub #31946](https://github.com/zephyrproject-rtos/zephyr/issues/31946) - arm,arm-timer dts compatible should be arm,armv8-timer
- [GitHub #31944](https://github.com/zephyrproject-rtos/zephyr/issues/31944) - flashing not working with openocd runner
- [GitHub #31938](https://github.com/zephyrproject-rtos/zephyr/issues/31938) - Invalid SPDX license identifier used in file
- [GitHub #31937](https://github.com/zephyrproject-rtos/zephyr/issues/31937) - sample.bluetooth.peripheral\_hr\_rv32m1\_vega\_ri5cy does not build
- [GitHub #31930](https://github.com/zephyrproject-rtos/zephyr/issues/31930) - uart\_nrfx\_uarte: `CONFIG_UART_ASYNC_API` with `CONFIG_PM_DEVICE` breaks
- [GitHub #31928](https://github.com/zephyrproject-rtos/zephyr/issues/31928) - usb loopback not work on nrf52840
- [GitHub #31924](https://github.com/zephyrproject-rtos/zephyr/issues/31924) - IVSHMEM with ACRN not working
- [GitHub #31921](https://github.com/zephyrproject-rtos/zephyr/issues/31921) - west flash not working with pyocd
- [GitHub #31920](https://github.com/zephyrproject-rtos/zephyr/issues/31920) - BME280: Use of deprecated `CONFIG_DEVICE_POWER_MANAGEMENT`
- [GitHub #31911](https://github.com/zephyrproject-rtos/zephyr/issues/31911) - Bluetooth: Mesh: Network buffer overflow on too long proxy messages
- [GitHub #31907](https://github.com/zephyrproject-rtos/zephyr/issues/31907) - settings: Unhandled error in NVS backend
- [GitHub #31905](https://github.com/zephyrproject-rtos/zephyr/issues/31905) - Question : Friend & Low power node with nRF52840
- [GitHub #31876](https://github.com/zephyrproject-rtos/zephyr/issues/31876) - west signing seems to be broken on windows
- [GitHub #31867](https://github.com/zephyrproject-rtos/zephyr/issues/31867) - samples/scheduler/metairq\_dispatc failed on iotdk boards
- [GitHub #31858](https://github.com/zephyrproject-rtos/zephyr/issues/31858) - xtensa crt1.S hard coding
- [GitHub #31853](https://github.com/zephyrproject-rtos/zephyr/issues/31853) - Devicetree API - Getting GPIO details from pin
- [GitHub #31847](https://github.com/zephyrproject-rtos/zephyr/issues/31847) - BT ISO channel. error value set, but not returned.
- [GitHub #31836](https://github.com/zephyrproject-rtos/zephyr/issues/31836) - Correct values of \_msg\_len arg in BT\_MESH\_MODEL\_PUB\_DEFINE macro
- [GitHub #31835](https://github.com/zephyrproject-rtos/zephyr/issues/31835) - Type conflict (uint32\_t) vs. (uint32\_t:7) leads to overflow (276 vs. 20)
- [GitHub #31822](https://github.com/zephyrproject-rtos/zephyr/issues/31822) - tests: drivers: timer: Test drivers.timer.nrf\_rtc\_timer.stress fails on nrf52 platforms
- [GitHub #31817](https://github.com/zephyrproject-rtos/zephyr/issues/31817) - mec15xxevb\_assy6853: tests/boards/mec15xxevb\_assy6853/i2c\_api/ failed
- [GitHub #31807](https://github.com/zephyrproject-rtos/zephyr/issues/31807) - USB DFU Broken for STM32L4
- [GitHub #31800](https://github.com/zephyrproject-rtos/zephyr/issues/31800) - west build; west build –board=qemu\_x86 fails with “unknown BOARD”
- [GitHub #31797](https://github.com/zephyrproject-rtos/zephyr/issues/31797) - need 2.5 release notes on switch to k\_heap from mem\_pool
- [GitHub #31791](https://github.com/zephyrproject-rtos/zephyr/issues/31791) - samples: hello-world: extra slash in path
- [GitHub #31789](https://github.com/zephyrproject-rtos/zephyr/issues/31789) - samples/scheduler/metairq\_dispatch: Regression after 30916 (sched: timeout: Do not miss slice timeouts)
- [GitHub #31782](https://github.com/zephyrproject-rtos/zephyr/issues/31782) - adc: test and sample failed on STM32
- [GitHub #31778](https://github.com/zephyrproject-rtos/zephyr/issues/31778) - Calling k\_sem\_give causes MPU Fault on nRF52833
- [GitHub #31769](https://github.com/zephyrproject-rtos/zephyr/issues/31769) - Twister: AttributeError: ‘NoneType’ object has no attribute ‘serial\_pty’
- [GitHub #31767](https://github.com/zephyrproject-rtos/zephyr/issues/31767) - twister: rename variable p
- [GitHub #31749](https://github.com/zephyrproject-rtos/zephyr/issues/31749) - fs: fs\_opendir can corrupt fs\_dir\_t object given via zdp parameter
- [GitHub #31741](https://github.com/zephyrproject-rtos/zephyr/issues/31741) - tests:subsys\_canbus\_isotp: mimxrt1060 meet recv timeout
- [GitHub #31735](https://github.com/zephyrproject-rtos/zephyr/issues/31735) - intel\_adsp\_cavs15: use twister to run kernel testcases has no output
- [GitHub #31733](https://github.com/zephyrproject-rtos/zephyr/issues/31733) - Unable to build socket can with frdm\_k64f
- [GitHub #31729](https://github.com/zephyrproject-rtos/zephyr/issues/31729) - test: build fatal related testcase failed on qemu\_cortex\_m0 and run failed on qemu\_nios2
- [GitHub #31727](https://github.com/zephyrproject-rtos/zephyr/issues/31727) - system\_off fails to go into soft\_off (deep sleep) state on cc1352r1\_launchxl
- [GitHub #31726](https://github.com/zephyrproject-rtos/zephyr/issues/31726) - RISC-V MIV SoC clock rate is specified 100x too slow
- [GitHub #31721](https://github.com/zephyrproject-rtos/zephyr/issues/31721) - tests: nrf: posix: portability.posix.common.tls.newlib fails on nrf9160dk\_nrf9160
- [GitHub #31704](https://github.com/zephyrproject-rtos/zephyr/issues/31704) - tests/bluetooth/init/bluetooth.init.test\_ctlr\_tiny Fails to build on nrf52dk\_nrf52832
- [GitHub #31696](https://github.com/zephyrproject-rtos/zephyr/issues/31696) - UP² Celeron version (not the Atom one) has no console
- [GitHub #31693](https://github.com/zephyrproject-rtos/zephyr/issues/31693) - Bluetooth: controller: Compilation error when Encryption support is disabled
- [GitHub #31684](https://github.com/zephyrproject-rtos/zephyr/issues/31684) - intel\_adsp\_cavs15: Cannot download firmware of kernel testcases
- [GitHub #31681](https://github.com/zephyrproject-rtos/zephyr/issues/31681) - [Coverity CID :216796] Uninitialized scalar variable in tests/subsys/power/power\_mgmt/src/main.c
- [GitHub #31680](https://github.com/zephyrproject-rtos/zephyr/issues/31680) - [Coverity CID :216795] Unchecked return value in tests/kernel/msgq/msgq\_api/src/test\_msgq\_contexts.c
- [GitHub #31679](https://github.com/zephyrproject-rtos/zephyr/issues/31679) - [Coverity CID :216794] Pointless string comparison in tests/lib/devicetree/api/src/main.c
- [GitHub #31678](https://github.com/zephyrproject-rtos/zephyr/issues/31678) - [Coverity CID :216793] Division or modulo by zero in tests/ztest/error\_hook/src/main.c
- [GitHub #31677](https://github.com/zephyrproject-rtos/zephyr/issues/31677) - [Coverity CID :216792] Out-of-bounds access in tests/net/lib/dns\_addremove/src/main.c
- [GitHub #31676](https://github.com/zephyrproject-rtos/zephyr/issues/31676) - [Coverity CID :216791] Side effect in assertion in tests/lib/p4workq/src/main.c
- [GitHub #31674](https://github.com/zephyrproject-rtos/zephyr/issues/31674) - [Coverity CID :216788] Explicit null dereferenced in tests/ztest/error\_hook/src/main.c
- [GitHub #31673](https://github.com/zephyrproject-rtos/zephyr/issues/31673) - [Coverity CID :216787] Wrong sizeof argument in tests/kernel/mem\_heap/mheap\_api\_concept/src/test\_mheap\_api.c
- [GitHub #31672](https://github.com/zephyrproject-rtos/zephyr/issues/31672) - [Coverity CID :216786] Side effect in assertion in tests/kernel/threads/thread\_apis/src/test\_threads\_cancel\_abort.c
- [GitHub #31671](https://github.com/zephyrproject-rtos/zephyr/issues/31671) - [Coverity CID :216785] Side effect in assertion in tests/lib/p4workq/src/main.c
- [GitHub #31670](https://github.com/zephyrproject-rtos/zephyr/issues/31670) - [Coverity CID :216783] Side effect in assertion in tests/lib/p4workq/src/main.c
- [GitHub #31669](https://github.com/zephyrproject-rtos/zephyr/issues/31669) - [Coverity CID :215715] Unchecked return value in tests/subsys/fs/littlefs/src/testfs\_mount\_flags.c
- [GitHub #31668](https://github.com/zephyrproject-rtos/zephyr/issues/31668) - [Coverity CID :215714] Unchecked return value in tests/subsys/fs/fs\_api/src/test\_fs\_mount\_flags.c
- [GitHub #31667](https://github.com/zephyrproject-rtos/zephyr/issues/31667) - [Coverity CID :215395] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31666](https://github.com/zephyrproject-rtos/zephyr/issues/31666) - [Coverity CID :215394] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31665](https://github.com/zephyrproject-rtos/zephyr/issues/31665) - [Coverity CID :215393] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31664](https://github.com/zephyrproject-rtos/zephyr/issues/31664) - [Coverity CID :215390] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31663](https://github.com/zephyrproject-rtos/zephyr/issues/31663) - [Coverity CID :215389] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31662](https://github.com/zephyrproject-rtos/zephyr/issues/31662) - [Coverity CID :215388] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31661](https://github.com/zephyrproject-rtos/zephyr/issues/31661) - [Coverity CID :215387] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31660](https://github.com/zephyrproject-rtos/zephyr/issues/31660) - [Coverity CID :215385] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31659](https://github.com/zephyrproject-rtos/zephyr/issues/31659) - [Coverity CID :215384] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31658](https://github.com/zephyrproject-rtos/zephyr/issues/31658) - [Coverity CID :215383] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31657](https://github.com/zephyrproject-rtos/zephyr/issues/31657) - [Coverity CID :215382] Operands don’t affect result in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31656](https://github.com/zephyrproject-rtos/zephyr/issues/31656) - [Coverity CID :215380] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31655](https://github.com/zephyrproject-rtos/zephyr/issues/31655) - [Coverity CID :215378] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31654](https://github.com/zephyrproject-rtos/zephyr/issues/31654) - [Coverity CID :215377] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31653](https://github.com/zephyrproject-rtos/zephyr/issues/31653) - [Coverity CID :215375] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31652](https://github.com/zephyrproject-rtos/zephyr/issues/31652) - [Coverity CID :215374] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31651](https://github.com/zephyrproject-rtos/zephyr/issues/31651) - [Coverity CID :215371] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31650](https://github.com/zephyrproject-rtos/zephyr/issues/31650) - [Coverity CID :215370] Argument cannot be negative in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31649](https://github.com/zephyrproject-rtos/zephyr/issues/31649) - [Coverity CID :215369] Out-of-bounds access in tests/net/lib/dns\_sd/src/main.c
- [GitHub #31648](https://github.com/zephyrproject-rtos/zephyr/issues/31648) - [Coverity CID :216800] Operands don’t affect result in lib/os/heap.c
- [GitHub #31647](https://github.com/zephyrproject-rtos/zephyr/issues/31647) - [Coverity CID :216789] Wrong sizeof argument in include/kernel.h
- [GitHub #31646](https://github.com/zephyrproject-rtos/zephyr/issues/31646) - [Coverity CID :215712] Assignment of overlapping memory in lib/os/cbprintf\_complete.c
- [GitHub #31645](https://github.com/zephyrproject-rtos/zephyr/issues/31645) - [Coverity CID :215711] Wrong sizeof argument in include/kernel.h
- [GitHub #31644](https://github.com/zephyrproject-rtos/zephyr/issues/31644) - [Coverity CID :216798] Unused value in subsys/net/lib/sockets/socketpair.c
- [GitHub #31643](https://github.com/zephyrproject-rtos/zephyr/issues/31643) - [Coverity CID :215372] Logically dead code in subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #31642](https://github.com/zephyrproject-rtos/zephyr/issues/31642) - [Coverity CID :216784] Uninitialized scalar variable in drivers/can/can\_common.c
- [GitHub #31640](https://github.com/zephyrproject-rtos/zephyr/issues/31640) - mcuboot build is broken
- [GitHub #31631](https://github.com/zephyrproject-rtos/zephyr/issues/31631) - x86: ehl\_crb\_sbl: Booting fails with Slim Bootloader
- [GitHub #31630](https://github.com/zephyrproject-rtos/zephyr/issues/31630) - Incorrect configuration override option for west flash
- [GitHub #31629](https://github.com/zephyrproject-rtos/zephyr/issues/31629) - mcumgr-cli image upload is failing on shell channel after MCUBOOT\_BOOTUTIL library was introduced
- [GitHub #31627](https://github.com/zephyrproject-rtos/zephyr/issues/31627) - tests/subsys/power/power\_mgmt/subsys.power.device\_pm fails to build on nrf5340dk\_nrf5340\_cpunet & nrf5340pdk\_nrf5340\_cpunet
- [GitHub #31616](https://github.com/zephyrproject-rtos/zephyr/issues/31616) - test: ipc: Test from samples/subsys/ipc/rpmsg\_service fails on nrf5340dk\_nrf5340\_cpuapp
- [GitHub #31614](https://github.com/zephyrproject-rtos/zephyr/issues/31614) - drivers: clock\_control: Kconfig.stm32xxx PLL div range for each serie
- [GitHub #31613](https://github.com/zephyrproject-rtos/zephyr/issues/31613) - Undefined reference errors when using External Library with k\_msgq\_\* calls
- [GitHub #31609](https://github.com/zephyrproject-rtos/zephyr/issues/31609) - CoAP discovery response does not follow CoRE link format specification
- [GitHub #31599](https://github.com/zephyrproject-rtos/zephyr/issues/31599) - 64 bit race on timer counter in cavs\_timer
- [GitHub #31584](https://github.com/zephyrproject-rtos/zephyr/issues/31584) - Twister: json reports generation takes too much time
- [GitHub #31582](https://github.com/zephyrproject-rtos/zephyr/issues/31582) - STM32F746ZG: No pwm signal output when running /tests/drivers/pwm/pwm\_api
- [GitHub #31579](https://github.com/zephyrproject-rtos/zephyr/issues/31579) - sam\_e70\_xplained: running tests/subsys/logging/log\_core failed
- [GitHub #31573](https://github.com/zephyrproject-rtos/zephyr/issues/31573) - Wrong log settings in can\_stm32 driver
- [GitHub #31569](https://github.com/zephyrproject-rtos/zephyr/issues/31569) - lora: sx126x: interrupt pin permanently enabled
- [GitHub #31567](https://github.com/zephyrproject-rtos/zephyr/issues/31567) - lora: SX126x modems consume excess power until used for first time
- [GitHub #31566](https://github.com/zephyrproject-rtos/zephyr/issues/31566) - up\_squared: Couldn’t get testcase log from console for all testcases.
- [GitHub #31562](https://github.com/zephyrproject-rtos/zephyr/issues/31562) - unexpected sign-extension in Kconfig linker symbols on 64-bit platforms
- [GitHub #31560](https://github.com/zephyrproject-rtos/zephyr/issues/31560) - Fix incorrect usage of default in dts bindings
- [GitHub #31555](https://github.com/zephyrproject-rtos/zephyr/issues/31555) - tests:drivers\_can\_api: mimxrt1060 can api test meet assert failure
- [GitHub #31551](https://github.com/zephyrproject-rtos/zephyr/issues/31551) - lorawan: setting datarate does not allow sending larger packets
- [GitHub #31549](https://github.com/zephyrproject-rtos/zephyr/issues/31549) - tests/kernel/lifo/lifo\_usage/kernel.lifo.usage fails on m2gl025\_miv
- [GitHub #31546](https://github.com/zephyrproject-rtos/zephyr/issues/31546) - DTS device dependency is shifting memory addresses between builds
- [GitHub #31543](https://github.com/zephyrproject-rtos/zephyr/issues/31543) - Documentation: Spelling
- [GitHub #31531](https://github.com/zephyrproject-rtos/zephyr/issues/31531) - STM32 can driver don’t set prescaler
- [GitHub #31528](https://github.com/zephyrproject-rtos/zephyr/issues/31528) - introduction of demand paging support causing qemu failures on x86\_64, qemu\_x86\_64\_nokpti
- [GitHub #31524](https://github.com/zephyrproject-rtos/zephyr/issues/31524) - littlefs: Too small heap for file cache.
- [GitHub #31517](https://github.com/zephyrproject-rtos/zephyr/issues/31517) - UP² broken (git bisect findings inside)
- [GitHub #31511](https://github.com/zephyrproject-rtos/zephyr/issues/31511) - AArch32 exception exit routine behaves incorrectly on fatal exceptions
- [GitHub #31510](https://github.com/zephyrproject-rtos/zephyr/issues/31510) - Some drivers return invalid z\_timer\_cycle\_get\_32() value
- [GitHub #31508](https://github.com/zephyrproject-rtos/zephyr/issues/31508) - up\_squared: tests/kernel/sched/deadline/ failed.
- [GitHub #31505](https://github.com/zephyrproject-rtos/zephyr/issues/31505) - qemu\_cortex\_m0: Cmake build failure
- [GitHub #31504](https://github.com/zephyrproject-rtos/zephyr/issues/31504) - qemu\_cortex\_m0: Cmake build failure
- [GitHub #31502](https://github.com/zephyrproject-rtos/zephyr/issues/31502) - it8xxx2\_evb should not define TICKLESS\_CAPABLE
- [GitHub #31488](https://github.com/zephyrproject-rtos/zephyr/issues/31488) - build failure w/twister and SDK 0.12.1 related to
- [GitHub #31486](https://github.com/zephyrproject-rtos/zephyr/issues/31486) - make htmldocs-fast not working in development workspace
- [GitHub #31485](https://github.com/zephyrproject-rtos/zephyr/issues/31485) - west flash –runner=jlink should raise error when CONFIG\_BUILD\_OUTPUT\_BIN=n
- [GitHub #31472](https://github.com/zephyrproject-rtos/zephyr/issues/31472) - tests: kernel: poll: timeout with FPU enabled
- [GitHub #31467](https://github.com/zephyrproject-rtos/zephyr/issues/31467) - samples: bluetooth: peripheral\_hids: Pairing fails on the nucleo\_wb55rg board.
- [GitHub #31444](https://github.com/zephyrproject-rtos/zephyr/issues/31444) - Error in include/net/socket\_select.h
- [GitHub #31439](https://github.com/zephyrproject-rtos/zephyr/issues/31439) - nrf5340dk\_nrf5340\_cpunet configuring incomplete
- [GitHub #31436](https://github.com/zephyrproject-rtos/zephyr/issues/31436) - compliance script broken
- [GitHub #31433](https://github.com/zephyrproject-rtos/zephyr/issues/31433) - samples/bluetooth/hci\_pwr\_ctrl stack overflow on nRF52DK\_nRF52832
- [GitHub #31419](https://github.com/zephyrproject-rtos/zephyr/issues/31419) - tests/ztest/error\_hook failed on ARC boards
- [GitHub #31414](https://github.com/zephyrproject-rtos/zephyr/issues/31414) - samples/net/mqtt\_publisher link error: undefined reference to `z_impl_sys_rand32_get`
- [GitHub #31400](https://github.com/zephyrproject-rtos/zephyr/issues/31400) - Extending `zephyr,code-partition` with `zephyr,code-header-size`
- [GitHub #31386](https://github.com/zephyrproject-rtos/zephyr/issues/31386) - sam\_e70b\_xplained: running tests/drivers/watchdog/wdt\_basic\_api/ timeout for v1.14-branch
- [GitHub #31385](https://github.com/zephyrproject-rtos/zephyr/issues/31385) - ARC version of sys\_read32 only reads uint16\_t on Zephyr v2.4
- [GitHub #31379](https://github.com/zephyrproject-rtos/zephyr/issues/31379) - Update CAN-API Documentation
- [GitHub #31370](https://github.com/zephyrproject-rtos/zephyr/issues/31370) - Question about serial communication using virtual COM
- [GitHub #31362](https://github.com/zephyrproject-rtos/zephyr/issues/31362) - kconfiglib.py \_save\_old() may rename /dev/null – replacing /dev/null with a file
- [GitHub #31358](https://github.com/zephyrproject-rtos/zephyr/issues/31358) - `west build` might destroy your repository, as it is defaulting doing pristine.
- [GitHub #31344](https://github.com/zephyrproject-rtos/zephyr/issues/31344) - iotdk: running tests/ztest/error\_hook/ failed
- [GitHub #31343](https://github.com/zephyrproject-rtos/zephyr/issues/31343) - sam\_e70\_xplained: running tests/net/socket/af\_packet/ failed
- [GitHub #31342](https://github.com/zephyrproject-rtos/zephyr/issues/31342) - sam\_e70\_xplained: running tests/net/ptp/clock/ failed
- [GitHub #31340](https://github.com/zephyrproject-rtos/zephyr/issues/31340) - sam\_e70\_xplained: running tests/subsys/logging/log\_core/ failed
- [GitHub #31339](https://github.com/zephyrproject-rtos/zephyr/issues/31339) - nsim\_em: running tests/ztest/error\_hook/ failed
- [GitHub #31338](https://github.com/zephyrproject-rtos/zephyr/issues/31338) - mimxrt1050\_evk: running tests/kernel/fpu\_sharing/float\_disable/ failed
- [GitHub #31333](https://github.com/zephyrproject-rtos/zephyr/issues/31333) - adding a periodic k\_timer causes k\_msleep to never return in tests/kernel/context
- [GitHub #31330](https://github.com/zephyrproject-rtos/zephyr/issues/31330) - Getting started guide outdated: Step 4 - Install a toolchain
- [GitHub #31327](https://github.com/zephyrproject-rtos/zephyr/issues/31327) - ci compliance failures due to intel\_adsp\_cavs25 sample
- [GitHub #31316](https://github.com/zephyrproject-rtos/zephyr/issues/31316) - Issue in UDP management for BG96
- [GitHub #31308](https://github.com/zephyrproject-rtos/zephyr/issues/31308) - Cannot set static address when using hci\_usb or hci\_uart on nRF5340 attached to Linux Host
- [GitHub #31301](https://github.com/zephyrproject-rtos/zephyr/issues/31301) - intel\_adsp\_cavs15: run kernel testcases failed.
- [GitHub #31289](https://github.com/zephyrproject-rtos/zephyr/issues/31289) - Problems building grub2 bootloader for Zephyr
- [GitHub #31285](https://github.com/zephyrproject-rtos/zephyr/issues/31285) - LOG resulting in incorrect output
- [GitHub #31282](https://github.com/zephyrproject-rtos/zephyr/issues/31282) - Kernel: Poll: Code Suspected Logic Problem
- [GitHub #31272](https://github.com/zephyrproject-rtos/zephyr/issues/31272) - CANOpen Sample compilation fails
- [GitHub #31262](https://github.com/zephyrproject-rtos/zephyr/issues/31262) - tests/kernel/threads/tls/kernel.threads.tls.userspace failing
- [GitHub #31259](https://github.com/zephyrproject-rtos/zephyr/issues/31259) - uart.h: Clarification required on uart\_irq\_tx\_ready uart\_irq\_rx\_ready
- [GitHub #31258](https://github.com/zephyrproject-rtos/zephyr/issues/31258) - watch dog (WWDT) timeout calculation for STM32 handles biggest timeout and rollover wrong
- [GitHub #31235](https://github.com/zephyrproject-rtos/zephyr/issues/31235) - Cortex-M: vector table relocation is incorrect with XIP=n
- [GitHub #31234](https://github.com/zephyrproject-rtos/zephyr/issues/31234) - twister: Add choice for tests sorting into subsets
- [GitHub #31226](https://github.com/zephyrproject-rtos/zephyr/issues/31226) - tests/drivers/dma/loop\_transfer does not use ztest
- [GitHub #31219](https://github.com/zephyrproject-rtos/zephyr/issues/31219) - newlib printk float formatting not working
- [GitHub #31207](https://github.com/zephyrproject-rtos/zephyr/issues/31207) - Non-existent event in asynchronous UART API
- [GitHub #31206](https://github.com/zephyrproject-rtos/zephyr/issues/31206) - coap.c : encoding of options with lengths larger than 268 is not proper
- [GitHub #31203](https://github.com/zephyrproject-rtos/zephyr/issues/31203) - fatal error: setjmp.h: No such file or directory
- [GitHub #31194](https://github.com/zephyrproject-rtos/zephyr/issues/31194) - twister: using unsupported fixture without defined harness causes an infinite loop during on-target test execution
- [GitHub #31168](https://github.com/zephyrproject-rtos/zephyr/issues/31168) - Wrong linker option syntax for printf and scanf with float support
- [GitHub #31158](https://github.com/zephyrproject-rtos/zephyr/issues/31158) - Ethernet (ENC424J600) with dumb\_http\_server\_mt demo does not work
- [GitHub #31153](https://github.com/zephyrproject-rtos/zephyr/issues/31153) - twister build of samples/audio/sof/sample.audio.sof fails on most platforms
- [GitHub #31145](https://github.com/zephyrproject-rtos/zephyr/issues/31145) - Litex-vexriscv address misaligned with dumb\_http\_server example
- [GitHub #31143](https://github.com/zephyrproject-rtos/zephyr/issues/31143) - samples: audio: sof: compilation issue, include file not found.
- [GitHub #31137](https://github.com/zephyrproject-rtos/zephyr/issues/31137) - Seems like the rule “.99 tag to signify major work started, minor+1 started “ not used anymore ?
- [GitHub #31134](https://github.com/zephyrproject-rtos/zephyr/issues/31134) - LittleFS: Error Resizing the External QSPI NOR Flash in nRF52840dk
- [GitHub #31114](https://github.com/zephyrproject-rtos/zephyr/issues/31114) - Bluetooth: Which coding (S2 vs S8) is used during advertising on Coded PHY?
- [GitHub #31100](https://github.com/zephyrproject-rtos/zephyr/issues/31100) - Recvfrom not returning -1 if UDP and len is too small for packet.
- [GitHub #31091](https://github.com/zephyrproject-rtos/zephyr/issues/31091) - usb: usb\_transfer\_sync deadlocks on disconnect/cancel transfer
- [GitHub #31086](https://github.com/zephyrproject-rtos/zephyr/issues/31086) - bluetooth: Resume peripheral’s advertising after disconnection when using new bt\_le\_ext\_adv\_\* API
- [GitHub #31085](https://github.com/zephyrproject-rtos/zephyr/issues/31085) - networking / openthread: ipv6 mesh-local all-nodes multicast (ff03::1) packets are dropped by zephyr ipv6 stack
- [GitHub #31079](https://github.com/zephyrproject-rtos/zephyr/issues/31079) - Receiving extended scans on an Adafruit nRF 52840
- [GitHub #31071](https://github.com/zephyrproject-rtos/zephyr/issues/31071) - board: arm: SiliconLabs: add support to development kit efm32pg\_stk3401a
- [GitHub #31069](https://github.com/zephyrproject-rtos/zephyr/issues/31069) - net: buf: remove data from end of buffer
- [GitHub #31067](https://github.com/zephyrproject-rtos/zephyr/issues/31067) - usb: cdc\_acm: compilation error without UART
- [GitHub #31055](https://github.com/zephyrproject-rtos/zephyr/issues/31055) - nordic: west flash no longer supports changing `CONFIG_GPIO_PINRESET` when flashing
- [GitHub #31053](https://github.com/zephyrproject-rtos/zephyr/issues/31053) - LwM2M FOTA pull not working with modem (offloaded socket) driver using UART
- [GitHub #31044](https://github.com/zephyrproject-rtos/zephyr/issues/31044) - sample.bluetooth.peripheral\_hr build fails on rv32m1\_vega\_ri5cy
- [GitHub #31110](https://github.com/zephyrproject-rtos/zephyr/issues/31110) - How can I overwrite west build in command?
- [GitHub #31028](https://github.com/zephyrproject-rtos/zephyr/issues/31028) - Cannot READ\_BIT(RCC->CR, RCC\_CR\_PLL1RDY) on STM32H743 based board
- [GitHub #31027](https://github.com/zephyrproject-rtos/zephyr/issues/31027) - Google tests run twice
- [GitHub #31020](https://github.com/zephyrproject-rtos/zephyr/issues/31020) - CI build failed on intel\_adsp\_cavs18 when submitted a PR
- [GitHub #31019](https://github.com/zephyrproject-rtos/zephyr/issues/31019) - Bluetooth: Mesh: Thread competition leads to failure to open or close the scanning.
- [GitHub #31018](https://github.com/zephyrproject-rtos/zephyr/issues/31018) - up\_squared: tests/kernel/pipe/pipe\_api failed.
- [GitHub #31014](https://github.com/zephyrproject-rtos/zephyr/issues/31014) - Incorrect timing calculation in can\_mcux\_flexcan
- [GitHub #31008](https://github.com/zephyrproject-rtos/zephyr/issues/31008) - error: initializer element is not constant .attr = K\_MEM\_PARTITION\_P\_RX\_U\_RX
- [GitHub #30999](https://github.com/zephyrproject-rtos/zephyr/issues/30999) - updatehub with openthread build update pkg failed
- [GitHub #30997](https://github.com/zephyrproject-rtos/zephyr/issues/30997) - samples: net: sockets: echo\_client: posix tls example
- [GitHub #30989](https://github.com/zephyrproject-rtos/zephyr/issues/30989) - driver : STM32 Ethernet : Pin definition for PH6
- [GitHub #30979](https://github.com/zephyrproject-rtos/zephyr/issues/30979) - up\_squared\_adsp: Twister can not capture testcases log correctly
- [GitHub #30972](https://github.com/zephyrproject-rtos/zephyr/issues/30972) - USB: SET\_ADDRESS logic error
- [GitHub #30964](https://github.com/zephyrproject-rtos/zephyr/issues/30964) - Sleep calls are off on qemu\_x86
- [GitHub #30961](https://github.com/zephyrproject-rtos/zephyr/issues/30961) - esp32 broken by devicetree device updates
- [GitHub #30955](https://github.com/zephyrproject-rtos/zephyr/issues/30955) - Bluetooth: userchan: k\_sem\_take failed with err -11
- [GitHub #30938](https://github.com/zephyrproject-rtos/zephyr/issues/30938) - samples/net/dhcpv4\_client does not work with sam\_e70\_xplained
- [GitHub #30935](https://github.com/zephyrproject-rtos/zephyr/issues/30935) - tests: net: sockets: tcp: add a tls tests
- [GitHub #30921](https://github.com/zephyrproject-rtos/zephyr/issues/30921) - west flash failed with an open ocd error
- [GitHub #30918](https://github.com/zephyrproject-rtos/zephyr/issues/30918) - up\_squared: tests/kernel/mem\_protect/mem\_protect failed.
- [GitHub #30893](https://github.com/zephyrproject-rtos/zephyr/issues/30893) - Remove LEGACY\_TIMEOUT\_API
- [GitHub #30872](https://github.com/zephyrproject-rtos/zephyr/issues/30872) - Convert Intel GNA driver to devicetree
- [GitHub #30871](https://github.com/zephyrproject-rtos/zephyr/issues/30871) - “warning: compound assignment with ‘volatile’-qualified left operand is deprecated” when building with C++20
- [GitHub #30870](https://github.com/zephyrproject-rtos/zephyr/issues/30870) - Convert Intel DMIC to devicetree
- [GitHub #30869](https://github.com/zephyrproject-rtos/zephyr/issues/30869) - Convert designware PWM driver to devicetree
- [GitHub #30862](https://github.com/zephyrproject-rtos/zephyr/issues/30862) - Nordic system timer driver incompatible with LEGACY\_TIMEOUT\_API
- [GitHub #30860](https://github.com/zephyrproject-rtos/zephyr/issues/30860) - legacy timeout ticks mishandled
- [GitHub #30857](https://github.com/zephyrproject-rtos/zephyr/issues/30857) - SDRAM not working on STM32H747I-DISCO
- [GitHub #30850](https://github.com/zephyrproject-rtos/zephyr/issues/30850) - iotdk: couldn’t flash image into iotdk board using west flash.
- [GitHub #30846](https://github.com/zephyrproject-rtos/zephyr/issues/30846) - devicetree: unspecified phandle-array elements cause errors
- [GitHub #30822](https://github.com/zephyrproject-rtos/zephyr/issues/30822) - designator order for field ‘zcan\_filter::rtr’ does not match declaration order in ‘const zcan\_filter’
- [GitHub #30819](https://github.com/zephyrproject-rtos/zephyr/issues/30819) - twister: –generate-hardware-map crashes and deletes map
- [GitHub #30810](https://github.com/zephyrproject-rtos/zephyr/issues/30810) - tests: kernel: kernel.threads.armv8m\_mpu\_stack\_guard fails on nrf9160dk
- [GitHub #30809](https://github.com/zephyrproject-rtos/zephyr/issues/30809) - new testcase is failing after 3f134877 on mec1501modular\_assy6885
- [GitHub #30808](https://github.com/zephyrproject-rtos/zephyr/issues/30808) - Blueooth: Controller Response COMMAND DISALLOWED
- [GitHub #30805](https://github.com/zephyrproject-rtos/zephyr/issues/30805) - Build error at tests/kernel/queue in mec15xxevb\_assy6853(qemu) platform
- [GitHub #30800](https://github.com/zephyrproject-rtos/zephyr/issues/30800) - STM32 usb clock from PLLSAI1
- [GitHub #30792](https://github.com/zephyrproject-rtos/zephyr/issues/30792) - Cannot build network echo\_server for nucleo\_f767zi
- [GitHub #30752](https://github.com/zephyrproject-rtos/zephyr/issues/30752) - ARC: passed tests marked as failed when running sanitycheck on nsim\_\* platforms
- [GitHub #30750](https://github.com/zephyrproject-rtos/zephyr/issues/30750) - Convert i2s\_cavs to devicetree
- [GitHub #30736](https://github.com/zephyrproject-rtos/zephyr/issues/30736) - Deadlock with usb\_transfer\_sync()
- [GitHub #30730](https://github.com/zephyrproject-rtos/zephyr/issues/30730) - tests: nrf: Tests in tests/drivers/timer/nrf\_rtc\_timer are flaky
- [GitHub #30723](https://github.com/zephyrproject-rtos/zephyr/issues/30723) - libc: malloc() returns unaligned pointer, causes CPU exception
- [GitHub #30713](https://github.com/zephyrproject-rtos/zephyr/issues/30713) - doc: “Variable ZEPHYR\_TOOLCHAIN\_VARIANT is not defined”
- [GitHub #30712](https://github.com/zephyrproject-rtos/zephyr/issues/30712) - “make zephyr\_generated\_headers” regressed again - “;” separator for Z\_CFLAGS instead of spaces
- [GitHub #30705](https://github.com/zephyrproject-rtos/zephyr/issues/30705) - STM32 PWM driver generates signal with wrong frequency on STM32G4
- [GitHub #30702](https://github.com/zephyrproject-rtos/zephyr/issues/30702) - Shell module broken on LiteX/VexRiscv after release zephyr-v2.1.0
- [GitHub #30698](https://github.com/zephyrproject-rtos/zephyr/issues/30698) - OpenThread Kconfigs should more closely follow Zephyr Kconfig recommendations
- [GitHub #30688](https://github.com/zephyrproject-rtos/zephyr/issues/30688) - Using openthread based lwm2m\_client cannot ping the external network address unless reset once
- [GitHub #30686](https://github.com/zephyrproject-rtos/zephyr/issues/30686) - getaddrinfo() does not respect socket type
- [GitHub #30685](https://github.com/zephyrproject-rtos/zephyr/issues/30685) - reel\_board: tests/kernel/fatal/exception/ failure
- [GitHub #30683](https://github.com/zephyrproject-rtos/zephyr/issues/30683) - intel\_adsp\_cavs15:running tests/kernel/sched/schedule\_api failed
- [GitHub #30679](https://github.com/zephyrproject-rtos/zephyr/issues/30679) - puncover worst-case stack analysis does not work
- [GitHub #30673](https://github.com/zephyrproject-rtos/zephyr/issues/30673) - cmake: zephyr\_module.cmake included before ZEPHYR\_EXTRA\_MODULES is evaluated
- [GitHub #30663](https://github.com/zephyrproject-rtos/zephyr/issues/30663) - Support for TI’s TMP117 Temperature Sensor.
- [GitHub #30657](https://github.com/zephyrproject-rtos/zephyr/issues/30657) - BT Mesh: Friendship ends if LPN publishes to a VA it is subscribed to
- [GitHub #30651](https://github.com/zephyrproject-rtos/zephyr/issues/30651) - sanitycheck samples/video/capture/sample.video.capture fails to build on mimxrt1064\_evk
- [GitHub #30649](https://github.com/zephyrproject-rtos/zephyr/issues/30649) - Trouble with gpio callback on frdm k64f
- [GitHub #30638](https://github.com/zephyrproject-rtos/zephyr/issues/30638) - nrf pwm broken
- [GitHub #30636](https://github.com/zephyrproject-rtos/zephyr/issues/30636) - TCP stack locks irq’s for too long
- [GitHub #30634](https://github.com/zephyrproject-rtos/zephyr/issues/30634) - frdm\_kw41z: Current master fails compilation in drivers/pwm/pwm\_mcux\_tpm.c
- [GitHub #30624](https://github.com/zephyrproject-rtos/zephyr/issues/30624) - BLE : ATT Timeout occurred during multilink central connection
- [GitHub #30591](https://github.com/zephyrproject-rtos/zephyr/issues/30591) - build RAM usage printout uses prebuilt and not final binary
- [GitHub #30582](https://github.com/zephyrproject-rtos/zephyr/issues/30582) - Doxygen doesn’t catch errors in argument names in callback functions that are @typedef’d
- [GitHub #30574](https://github.com/zephyrproject-rtos/zephyr/issues/30574) - up\_squared: tests/kernel/semaphore/semaphore failed.
- [GitHub #30573](https://github.com/zephyrproject-rtos/zephyr/issues/30573) - up\_squared: slowdown on test execution and timing out on multiple tests
- [GitHub #30566](https://github.com/zephyrproject-rtos/zephyr/issues/30566) - flashing issue with ST Nucleo board H745ZI-Q
- [GitHub #30557](https://github.com/zephyrproject-rtos/zephyr/issues/30557) - i2c slave driver removed
- [GitHub #30554](https://github.com/zephyrproject-rtos/zephyr/issues/30554) - tests/kernel/fatal/exception/sentinel test is failing for various nrf platforms
- [GitHub #30553](https://github.com/zephyrproject-rtos/zephyr/issues/30553) - kconfig.py exits with error when using multiple shields
- [GitHub #30548](https://github.com/zephyrproject-rtos/zephyr/issues/30548) - reel\_board: tests/net/ieee802154/l2/ build failure
- [GitHub #30547](https://github.com/zephyrproject-rtos/zephyr/issues/30547) - reel\_board: tests/net/ieee802154/fragment/ build failure
- [GitHub #30546](https://github.com/zephyrproject-rtos/zephyr/issues/30546) - LwM2M Execute arguments currently not supported
- [GitHub #30541](https://github.com/zephyrproject-rtos/zephyr/issues/30541) - l2m2m: writing to resources with pre\_write callback fails
- [GitHub #30531](https://github.com/zephyrproject-rtos/zephyr/issues/30531) - When using ccache, compiler identity stored in ToolchainCapabilityDatabase is always the same
- [GitHub #30526](https://github.com/zephyrproject-rtos/zephyr/issues/30526) - tests: drivers: timer: Tests from drivers.timer.nrf\_rtc\_timer.basic fail on all nrf platforms
- [GitHub #30517](https://github.com/zephyrproject-rtos/zephyr/issues/30517) - Interrupt nesting is broken on ARMv7-R / LR\_svc corrupted.
- [GitHub #30514](https://github.com/zephyrproject-rtos/zephyr/issues/30514) - reel\_board: tests/benchmarks/sys\_kernel/ fails
- [GitHub #30513](https://github.com/zephyrproject-rtos/zephyr/issues/30513) - reel\_board: tests/benchmarks/latency\_measure/ fails
- [GitHub #30509](https://github.com/zephyrproject-rtos/zephyr/issues/30509) - k\_timer\_remaining\_get returns incorrect value on long timers
- [GitHub #30507](https://github.com/zephyrproject-rtos/zephyr/issues/30507) - nrf52\_bsim fails on some tests after merging 29810
- [GitHub #30488](https://github.com/zephyrproject-rtos/zephyr/issues/30488) - Bluetooth: controller: swi.h should use CONFIG\_SOC\_NRF5340\_CPUNET define
- [GitHub #30486](https://github.com/zephyrproject-rtos/zephyr/issues/30486) - updatehub demo for nrf52840dk
- [GitHub #30483](https://github.com/zephyrproject-rtos/zephyr/issues/30483) - Sanitycheck: When platform is nsim\_hs\_smp, process “west flash” become defunct, the grandchild “cld” process can’t be killed
- [GitHub #30480](https://github.com/zephyrproject-rtos/zephyr/issues/30480) - Bluetooth: Controller: Advertising can only be started 2^16 times
- [GitHub #30477](https://github.com/zephyrproject-rtos/zephyr/issues/30477) - frdm\_k64f: testcase samples/subsys/canbus/canopen/ failed to be ran
- [GitHub #30476](https://github.com/zephyrproject-rtos/zephyr/issues/30476) - frdm\_k64f: testcase samples/net/cloud/tagoio\_http\_post/ failed to be ran
- [GitHub #30475](https://github.com/zephyrproject-rtos/zephyr/issues/30475) - frdm\_k64f: testcase tests/kernel/fatal/exception/ failed to be ran
- [GitHub #30473](https://github.com/zephyrproject-rtos/zephyr/issues/30473) - mimxrt1050\_evk: testcase tests/kernel/fatal/exception/ failed to be ran
- [GitHub #30472](https://github.com/zephyrproject-rtos/zephyr/issues/30472) - sam\_e70\_xplained: the samples/net/civetweb/http\_server/. waits for interface unitl timeout
- [GitHub #30470](https://github.com/zephyrproject-rtos/zephyr/issues/30470) - sam\_e70\_xplained: tesecase tests/subsys/log\_core failed to run
- [GitHub #30468](https://github.com/zephyrproject-rtos/zephyr/issues/30468) - mesh: cfg\_svr.c app\_key\_del passes an incorrect parameter
- [GitHub #30467](https://github.com/zephyrproject-rtos/zephyr/issues/30467) - replace device define macros with devicetree-based macro
- [GitHub #30446](https://github.com/zephyrproject-rtos/zephyr/issues/30446) - fxas21002 gyroscope reading is in deg/s
- [GitHub #30435](https://github.com/zephyrproject-rtos/zephyr/issues/30435) - NRFX\_CLOCK\_EVT\_HFCLKAUDIO\_STARTED not handled in clock\_control\_nrf.c
- [GitHub #30434](https://github.com/zephyrproject-rtos/zephyr/issues/30434) - Memory map executing test case failed when code coverage enabled in x86\_64 platform
- [GitHub #30433](https://github.com/zephyrproject-rtos/zephyr/issues/30433) - zephyr client automatic joiner failed on nRF52840dk
- [GitHub #30432](https://github.com/zephyrproject-rtos/zephyr/issues/30432) - No network interface was found when running socketcan sample
- [GitHub #30426](https://github.com/zephyrproject-rtos/zephyr/issues/30426) - Enforce all checkpatch warnings and move to 100 characters per line
- [GitHub #30423](https://github.com/zephyrproject-rtos/zephyr/issues/30423) - Devicetree: Child node of node on SPI bus itself needs reg property - Bug?
- [GitHub #30418](https://github.com/zephyrproject-rtos/zephyr/issues/30418) - Logging: Using asserts with LOG in high pri ISR context blocks output
- [GitHub #30408](https://github.com/zephyrproject-rtos/zephyr/issues/30408) - tests/kernel/sched/schedule\_api is failing after 0875740 on m2gl025\_miv
- [GitHub #30397](https://github.com/zephyrproject-rtos/zephyr/issues/30397) - tests:latency\_measure is not counting semaphore results on the ARM boards
- [GitHub #30394](https://github.com/zephyrproject-rtos/zephyr/issues/30394) - TLS tests failing with sanitycheck (under load)
- [GitHub #30393](https://github.com/zephyrproject-rtos/zephyr/issues/30393) - kernel.threads.tls.userspace fails with SDK 0.12.0-beta on ARM Cortex-M
- [GitHub #30386](https://github.com/zephyrproject-rtos/zephyr/issues/30386) - Building confirmed images does not work
- [GitHub #30384](https://github.com/zephyrproject-rtos/zephyr/issues/30384) - Scheduler doesn’t activate sleeping threads on native\_posix
- [GitHub #30380](https://github.com/zephyrproject-rtos/zephyr/issues/30380) - Improve the use of CONFIG\_KERNEL\_COHERENCE
- [GitHub #30378](https://github.com/zephyrproject-rtos/zephyr/issues/30378) - Bluetooth: controller: tx buffer overflow error
- [GitHub #30364](https://github.com/zephyrproject-rtos/zephyr/issues/30364) - TCP2 does not implement queing for incoming packets
- [GitHub #30362](https://github.com/zephyrproject-rtos/zephyr/issues/30362) - adc\_read\_async callback parameters are dereferenced pointers, making use of CONTAINER\_OF impossible
- [GitHub #30360](https://github.com/zephyrproject-rtos/zephyr/issues/30360) - reproducible qemu\_x86\_64 SMP failures
- [GitHub #30356](https://github.com/zephyrproject-rtos/zephyr/issues/30356) - DAC header file not included in stm32 soc.h
- [GitHub #30354](https://github.com/zephyrproject-rtos/zephyr/issues/30354) - Regression with ‘local-mac-address’ enet DTS property parsing (on i.MX K6x)
- [GitHub #30349](https://github.com/zephyrproject-rtos/zephyr/issues/30349) - Memory protection unit fault when running socket CAN program
- [GitHub #30344](https://github.com/zephyrproject-rtos/zephyr/issues/30344) - Bluetooth: host: Add support for multiple advertising sets for legacy advertising
- [GitHub #30338](https://github.com/zephyrproject-rtos/zephyr/issues/30338) - BT Mesh LPN max. poll timeout calculated incorrectly
- [GitHub #30330](https://github.com/zephyrproject-rtos/zephyr/issues/30330) - tests/subsys/usb/bos/usb.bos fails with native\_posix and llvm/clang
- [GitHub #30328](https://github.com/zephyrproject-rtos/zephyr/issues/30328) - Openthread build issues with clang/llvm
- [GitHub #30322](https://github.com/zephyrproject-rtos/zephyr/issues/30322) - tests: benchmarks: latency\_measure: timing measurement values are all 0
- [GitHub #30316](https://github.com/zephyrproject-rtos/zephyr/issues/30316) - updatehub with openthread
- [GitHub #30315](https://github.com/zephyrproject-rtos/zephyr/issues/30315) - Build failure: zephyr/include/generated/devicetree\_unfixed.h:627:29: error: ‘DT\_N\_S\_leds\_S\_led\_0\_P\_gpios\_IDX\_0\_PH\_P\_label’ undeclared
- [GitHub #30308](https://github.com/zephyrproject-rtos/zephyr/issues/30308) - Add optional user data field to device structure
- [GitHub #30307](https://github.com/zephyrproject-rtos/zephyr/issues/30307) - up\_squared: tests/kernel/device/ failed.
- [GitHub #30306](https://github.com/zephyrproject-rtos/zephyr/issues/30306) - up\_squared: tests/kernel/mem\_protect/userspace failed.
- [GitHub #30305](https://github.com/zephyrproject-rtos/zephyr/issues/30305) - up\_squared: tests/kernel/mem\_protect/mem\_protect failed.
- [GitHub #30304](https://github.com/zephyrproject-rtos/zephyr/issues/30304) - NRF52832 consumption too high 220uA
- [GitHub #30298](https://github.com/zephyrproject-rtos/zephyr/issues/30298) - regression/change in master: formatting floats and doubles
- [GitHub #30276](https://github.com/zephyrproject-rtos/zephyr/issues/30276) - Sanitycheck: can’t find mdb.pid
- [GitHub #30275](https://github.com/zephyrproject-rtos/zephyr/issues/30275) - up\_squared: tests/kernel/common failed (timeout error)
- [GitHub #30261](https://github.com/zephyrproject-rtos/zephyr/issues/30261) - File no longer at this location
- [GitHub #30257](https://github.com/zephyrproject-rtos/zephyr/issues/30257) - test: kernel: Test kernel.common.stack\_protection\_arm\_fpu\_sharing.fatal fails on nrf52 platforms
- [GitHub #30253](https://github.com/zephyrproject-rtos/zephyr/issues/30253) - tests: kernel: Test kernel.memory\_protection.gap\_filling fails on nrf5340dk\_nrf5340\_cpuapp
- [GitHub #30372](https://github.com/zephyrproject-rtos/zephyr/issues/30372) - WEST Support clean build
- [GitHub #30373](https://github.com/zephyrproject-rtos/zephyr/issues/30373) - out of tree （board soc doc subsystem …)
- [GitHub #30240](https://github.com/zephyrproject-rtos/zephyr/issues/30240) - Bluetooth: Mesh: PTS Test failed in friend node
- [GitHub #30235](https://github.com/zephyrproject-rtos/zephyr/issues/30235) - MbedTLS X509 certificate not parsing
- [GitHub #30232](https://github.com/zephyrproject-rtos/zephyr/issues/30232) - CMake 3.19 doesn’t work with Zephyr (tracking issue w/upstream CMake)
- [GitHub #30230](https://github.com/zephyrproject-rtos/zephyr/issues/30230) - printk and power management incompatibility
- [GitHub #30229](https://github.com/zephyrproject-rtos/zephyr/issues/30229) - BinaryHandler has no pid file
- [GitHub #30224](https://github.com/zephyrproject-rtos/zephyr/issues/30224) - stm32f4\_disco: User button press is inverted
- [GitHub #30222](https://github.com/zephyrproject-rtos/zephyr/issues/30222) - boards: arm: nucleo\_wb55rg: fails to build basic samples
- [GitHub #30219](https://github.com/zephyrproject-rtos/zephyr/issues/30219) - drivers: gpio: gpio\_cc13xx\_cc26xx: Add drive strength configurability
- [GitHub #30213](https://github.com/zephyrproject-rtos/zephyr/issues/30213) - usb: tests: Test usb.device.usb.device.usb\_disable fails on nrf52840dk\_nrf52840
- [GitHub #30211](https://github.com/zephyrproject-rtos/zephyr/issues/30211) - spi nor sfdp runtime: nph offset
- [GitHub #30207](https://github.com/zephyrproject-rtos/zephyr/issues/30207) - Mesh\_demo with a nRF52840 not working
- [GitHub #30205](https://github.com/zephyrproject-rtos/zephyr/issues/30205) - Missing error check of function i2c\_write\_read() and dac\_write\_value()
- [GitHub #30194](https://github.com/zephyrproject-rtos/zephyr/issues/30194) - qemu\_x86 crashes when printing floating point.
- [GitHub #30193](https://github.com/zephyrproject-rtos/zephyr/issues/30193) - reel\_board: running tests/subsys/power/power\_mgmt\_soc failed
- [GitHub #30191](https://github.com/zephyrproject-rtos/zephyr/issues/30191) - Missing checks of return values of settings\_runtime\_set()
- [GitHub #30189](https://github.com/zephyrproject-rtos/zephyr/issues/30189) - Missing error check of function sensor\_trigger\_set()
- [GitHub #30187](https://github.com/zephyrproject-rtos/zephyr/issues/30187) - usb: stm32: MCU fall in deadlock when calling sleep API during USB transfer
- [GitHub #30183](https://github.com/zephyrproject-rtos/zephyr/issues/30183) - undefined reference to `ring_buf_item_put`
- [GitHub #30179](https://github.com/zephyrproject-rtos/zephyr/issues/30179) - out of tree （board soc doc subsystem …）
- [GitHub #30178](https://github.com/zephyrproject-rtos/zephyr/issues/30178) - Is there any plan to support NXP RT600 HIFI4 DSP in the zephyr project?
- [GitHub #30173](https://github.com/zephyrproject-rtos/zephyr/issues/30173) - OpenThread SED cannot join the network after “Update nRF5 ieee802154 driver to v1.9”
- [GitHub #30157](https://github.com/zephyrproject-rtos/zephyr/issues/30157) - SW based BLE Link Layer Random Advertise delay not as expected
- [GitHub #30153](https://github.com/zephyrproject-rtos/zephyr/issues/30153) - BSD recv() can not received huge package(may be 100kB) sustain .
- [GitHub #30148](https://github.com/zephyrproject-rtos/zephyr/issues/30148) - STM32G474: Write to flash Bank 2 address 0x08040000 does not work in 256K flash version
- [GitHub #30141](https://github.com/zephyrproject-rtos/zephyr/issues/30141) - qemu\_x86 unexpected thread behavior
- [GitHub #30137](https://github.com/zephyrproject-rtos/zephyr/issues/30137) - TCP2: Handling of RST flag from server makes poll() call unable to return indefinitely
- [GitHub #30135](https://github.com/zephyrproject-rtos/zephyr/issues/30135) - LWM2M: Firmware URI writing does not work anymore
- [GitHub #30134](https://github.com/zephyrproject-rtos/zephyr/issues/30134) - tests: drivers: uart: Tests from tests/drivers/uart/uart\_mix\_fifo\_poll fails on nrf platforms
- [GitHub #30133](https://github.com/zephyrproject-rtos/zephyr/issues/30133) - sensor: driver: lis2dh interrupt definitions
- [GitHub #30130](https://github.com/zephyrproject-rtos/zephyr/issues/30130) - nrf\_radio\_power\_set() should use bool
- [GitHub #30129](https://github.com/zephyrproject-rtos/zephyr/issues/30129) - TCP2 send test
- [GitHub #30126](https://github.com/zephyrproject-rtos/zephyr/issues/30126) - xtensa-asm2-util.s hard coding
- [GitHub #30120](https://github.com/zephyrproject-rtos/zephyr/issues/30120) - sanitycheck fails for tests/bluetooth/init/bluetooth.init.test\_ctlr\_per\_sync
- [GitHub #30117](https://github.com/zephyrproject-rtos/zephyr/issues/30117) - Cannot compile Zephyr project with standard macros INT8\_C, UINT8\_C, UINT16\_C
- [GitHub #30106](https://github.com/zephyrproject-rtos/zephyr/issues/30106) - Refactor zcan\_frame.
- [GitHub #30100](https://github.com/zephyrproject-rtos/zephyr/issues/30100) - twister test case selection numbers don’t make any sense
- [GitHub #30099](https://github.com/zephyrproject-rtos/zephyr/issues/30099) - sanitycheck –build-only gets stuck
- [GitHub #30098](https://github.com/zephyrproject-rtos/zephyr/issues/30098) - > very few are even tested with CONFIG\_NO\_OPTIMIZATIONS. What is the general consensus about this?
- [GitHub #30094](https://github.com/zephyrproject-rtos/zephyr/issues/30094) - tests: kernel: fpu\_sharing: Tests in tests/kernel/fpu\_sharing fail on nrf platforms
- [GitHub #30075](https://github.com/zephyrproject-rtos/zephyr/issues/30075) - dfu: mcuboot: fail to build with CONFIG\_BOOTLOADER\_MCUBOOT=n and CONFIG\_IMG\_MANAGER=y
- [GitHub #30072](https://github.com/zephyrproject-rtos/zephyr/issues/30072) - tests/net/socket/socketpair appears to mis-use work queue APIs
- [GitHub #30066](https://github.com/zephyrproject-rtos/zephyr/issues/30066) - CI test build with RAM overflow
- [GitHub #30057](https://github.com/zephyrproject-rtos/zephyr/issues/30057) - LLVM built application crash
- [GitHub #30037](https://github.com/zephyrproject-rtos/zephyr/issues/30037) - Documentation: Fix getting started guide for macOS around homebrew install
- [GitHub #30031](https://github.com/zephyrproject-rtos/zephyr/issues/30031) - stm32f4 usb - bulk in endpoint does not work
- [GitHub #30029](https://github.com/zephyrproject-rtos/zephyr/issues/30029) - samples: net: cloud: tagoio\_http\_post: Undefined initialization levels used.
- [GitHub #30028](https://github.com/zephyrproject-rtos/zephyr/issues/30028) - sam\_e70\_xplained: MPU fault with CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #30027](https://github.com/zephyrproject-rtos/zephyr/issues/30027) - sanitycheck failures on `tests/bluetooth/init/bluetooth.init.test_ctlr_peripheral_ext`
- [GitHub #30022](https://github.com/zephyrproject-rtos/zephyr/issues/30022) - The mailbox message.info in the receiver thread is not updated.
- [GitHub #30014](https://github.com/zephyrproject-rtos/zephyr/issues/30014) - STM32F411RE PWM support
- [GitHub #30010](https://github.com/zephyrproject-rtos/zephyr/issues/30010) - util or toolchain: functions for reversing bits
- [GitHub #29999](https://github.com/zephyrproject-rtos/zephyr/issues/29999) - nrf52840 Slave mode is not supported on SPI\_0
- [GitHub #29997](https://github.com/zephyrproject-rtos/zephyr/issues/29997) - format specifies type ‘unsigned short’ but the argument has type ‘int’ error in network stack
- [GitHub #29995](https://github.com/zephyrproject-rtos/zephyr/issues/29995) - Bluetooth: l2cap: L2CAP/LE/REJ/BI-02-C test failure
- [GitHub #29994](https://github.com/zephyrproject-rtos/zephyr/issues/29994) - High bluetooth ISR latency with CONFIG\_BT\_MAX\_CONN=2
- [GitHub #29992](https://github.com/zephyrproject-rtos/zephyr/issues/29992) - dma tests fail with stm32wb55 and stm32l476 nucleo boards
- [GitHub #29991](https://github.com/zephyrproject-rtos/zephyr/issues/29991) - Watchdog Example not working as expected on a Nordic chip
- [GitHub #29977](https://github.com/zephyrproject-rtos/zephyr/issues/29977) - nrf9160: use 32Mhz HFCLK
- [GitHub #29969](https://github.com/zephyrproject-rtos/zephyr/issues/29969) - sanitycheck fails on tests/benchmarks/latency\_measure/benchmark.kernel.latency
- [GitHub #29968](https://github.com/zephyrproject-rtos/zephyr/issues/29968) - sanitycheck fails a number of bluetooth tests on NRF
- [GitHub #29967](https://github.com/zephyrproject-rtos/zephyr/issues/29967) - sanitycheck fails to build samples/bluetooth/peripheral\_hr/sample.bluetooth.peripheral\_hr\_rv32m1\_vega\_ri5cy
- [GitHub #29964](https://github.com/zephyrproject-rtos/zephyr/issues/29964) - net: lwm2m: Correctly Support Bootstrap-Delete Operation
- [GitHub #29963](https://github.com/zephyrproject-rtos/zephyr/issues/29963) - RFC: dfu/boot/mcuboot: consider usage of boootloader/mcuboot code
- [GitHub #29961](https://github.com/zephyrproject-rtos/zephyr/issues/29961) - Add i2c driver tests for microchip evaluation board
- [GitHub #29960](https://github.com/zephyrproject-rtos/zephyr/issues/29960) - Checkpatch compliance errors do not fail CI
- [GitHub #29958](https://github.com/zephyrproject-rtos/zephyr/issues/29958) - mcuboot hangs when CONFIG\_BOOT\_SERIAL\_DETECT\_PORT value not found
- [GitHub #29957](https://github.com/zephyrproject-rtos/zephyr/issues/29957) - BLE Notifications limited to 1 per connection event on Zephyr v2.4.0 Central
- [GitHub #29954](https://github.com/zephyrproject-rtos/zephyr/issues/29954) - intel\_adsp\_cavs18 fails with heap errors on current Zephyr
- [GitHub #29953](https://github.com/zephyrproject-rtos/zephyr/issues/29953) - Add the sofproject as a module
- [GitHub #29951](https://github.com/zephyrproject-rtos/zephyr/issues/29951) - ieee802154: cc13xx\_cc26xx: raw mode support
- [GitHub #29945](https://github.com/zephyrproject-rtos/zephyr/issues/29945) - Missing error check of function sensor\_sample\_fetch() and sensor\_channel\_get()
- [GitHub #29943](https://github.com/zephyrproject-rtos/zephyr/issues/29943) - Missing error check of function isotp\_send()
- [GitHub #29937](https://github.com/zephyrproject-rtos/zephyr/issues/29937) - XCC Build offsets.c ：FAILED
- [GitHub #29936](https://github.com/zephyrproject-rtos/zephyr/issues/29936) - XCC Build isr\_tables.c fail
- [GitHub #29925](https://github.com/zephyrproject-rtos/zephyr/issues/29925) - pinctrl error for disco\_l475\_iot1 board:
- [GitHub #29921](https://github.com/zephyrproject-rtos/zephyr/issues/29921) - USB DFU with nrf52840dk (PCA10056)
- [GitHub #29916](https://github.com/zephyrproject-rtos/zephyr/issues/29916) - ARC: tests fail on nsim\_hs with one register bank
- [GitHub #29913](https://github.com/zephyrproject-rtos/zephyr/issues/29913) - Question : Bluetooth mesh using long range
- [GitHub #29908](https://github.com/zephyrproject-rtos/zephyr/issues/29908) - devicetree: Allow all GPIO flags to be used by devicetree
- [GitHub #29896](https://github.com/zephyrproject-rtos/zephyr/issues/29896) - new documentation build warning
- [GitHub #29891](https://github.com/zephyrproject-rtos/zephyr/issues/29891) - mcumgr image upload (with smp\_svr) does not work over serial/shell on the nrf52840dk
- [GitHub #29884](https://github.com/zephyrproject-rtos/zephyr/issues/29884) - x\_nucleo\_iks01a2 device tree overlay issue with stm32mp157c\_dk2 board
- [GitHub #29883](https://github.com/zephyrproject-rtos/zephyr/issues/29883) - drivers: ieee802154: cc13xx\_cc26xx: use multi-protocol radio patch
- [GitHub #29879](https://github.com/zephyrproject-rtos/zephyr/issues/29879) - samples/net/gptp compile failed on frdm\_k64f board in origin/master (work well in origin/v2.4-branch)
- [GitHub #29877](https://github.com/zephyrproject-rtos/zephyr/issues/29877) - WS2812 SPI LED strip driver produces bad SPI data
- [GitHub #29869](https://github.com/zephyrproject-rtos/zephyr/issues/29869) - Missing error check of function entropy\_get\_entropy()
- [GitHub #29868](https://github.com/zephyrproject-rtos/zephyr/issues/29868) - Bluetooth: Mesh: DST not checked on send
- [GitHub #29858](https://github.com/zephyrproject-rtos/zephyr/issues/29858) - [v1.14, v2.4] Bluetooth: Mesh: RPL cleared on LPN disconnect
- [GitHub #29855](https://github.com/zephyrproject-rtos/zephyr/issues/29855) - Bluetooth: Mesh: TTL max not checked on send
- [GitHub #29853](https://github.com/zephyrproject-rtos/zephyr/issues/29853) - multiple PRs fail doc checks
- [GitHub #29842](https://github.com/zephyrproject-rtos/zephyr/issues/29842) - ‘imgtool’ absent in requirements.txt
- [GitHub #29833](https://github.com/zephyrproject-rtos/zephyr/issues/29833) - Test DT\_INST\_PROP\_HAS\_IDX() inside the macros for multi instances
- [GitHub #29831](https://github.com/zephyrproject-rtos/zephyr/issues/29831) - flash support for stm32h7 SoC
- [GitHub #29829](https://github.com/zephyrproject-rtos/zephyr/issues/29829) - On-PR CI needs to build a subset of tests for a subset of platforms regardless of the scope of the PR changes
- [GitHub #29826](https://github.com/zephyrproject-rtos/zephyr/issues/29826) - SNTP doesn’t work on v2.4.0 on eswifi
- [GitHub #29822](https://github.com/zephyrproject-rtos/zephyr/issues/29822) - Redundant error check of function usb\_set\_config() in subsys/usb/class/usb\_dfu.c
- [GitHub #29809](https://github.com/zephyrproject-rtos/zephyr/issues/29809) - gen\_isr\_tables.py does not check that the IRQ number is in bounds
- [GitHub #29805](https://github.com/zephyrproject-rtos/zephyr/issues/29805) - SimpleLink does not compile (simplelink\_sockets.c)
- [GitHub #29796](https://github.com/zephyrproject-rtos/zephyr/issues/29796) - Zephyr API for writing to flash for STM32G474 doesn’t work as expected
- [GitHub #29793](https://github.com/zephyrproject-rtos/zephyr/issues/29793) - Ninja generated error when setting PCAP option in west
- [GitHub #29791](https://github.com/zephyrproject-rtos/zephyr/issues/29791) - spi stm32 dma: spi
- [GitHub #29790](https://github.com/zephyrproject-rtos/zephyr/issues/29790) - The zephyr-app-commands macro does not honor :generator: option
- [GitHub #29782](https://github.com/zephyrproject-rtos/zephyr/issues/29782) - smp\_svr: Flashing zephyr.signed.bin does not seem to work on nrf52840dk
- [GitHub #29780](https://github.com/zephyrproject-rtos/zephyr/issues/29780) - nRF SDK hci\_usb sample disconnects after 40 seconds with extended connection via coded PHY
- [GitHub #29776](https://github.com/zephyrproject-rtos/zephyr/issues/29776) - Check vector number and pointer to ISR in “\_isr\_wrapper” routine for aarch64
- [GitHub #29775](https://github.com/zephyrproject-rtos/zephyr/issues/29775) - TCP socket stream
- [GitHub #29773](https://github.com/zephyrproject-rtos/zephyr/issues/29773) - sam\_e70\_xplained: running samples/net/sockets/civetweb/ failed
- [GitHub #29772](https://github.com/zephyrproject-rtos/zephyr/issues/29772) - sam\_e70\_xplained:running testcase tests/subsys/logging/log\_core failed
- [GitHub #29771](https://github.com/zephyrproject-rtos/zephyr/issues/29771) - samples: net: sockets: tcp: tcp2 server not accepting with ipv6 bsd sockets
- [GitHub #29769](https://github.com/zephyrproject-rtos/zephyr/issues/29769) - mimxrt1050\_evk: build error at tests/subsys/usb/device/
- [GitHub #29762](https://github.com/zephyrproject-rtos/zephyr/issues/29762) - nRF53 Network core cannot start LFClk when using empty\_app\_core
- [GitHub #29758](https://github.com/zephyrproject-rtos/zephyr/issues/29758) - edtlib not reporting proper matching\_compat for led nodes (and other children nodes)
- [GitHub #29740](https://github.com/zephyrproject-rtos/zephyr/issues/29740) - OTA using Thread
- [GitHub #29737](https://github.com/zephyrproject-rtos/zephyr/issues/29737) - up\_squared: tests/subsys/power/power\_mgmt failed.
- [GitHub #29733](https://github.com/zephyrproject-rtos/zephyr/issues/29733) - SAM0 will wake up with interrupted execution after deep sleep
- [GitHub #29732](https://github.com/zephyrproject-rtos/zephyr/issues/29732) - issue with ST Nucleo H743ZI2
- [GitHub #29730](https://github.com/zephyrproject-rtos/zephyr/issues/29730) - drivers/pcie: In Kernel Mode pcie\_conf\_read crashes when used with newlib
- [GitHub #29722](https://github.com/zephyrproject-rtos/zephyr/issues/29722) - West flash is not able to flash with openocd
- [GitHub #29721](https://github.com/zephyrproject-rtos/zephyr/issues/29721) - drivers/sensor/lsm6dsl: assertion/UB during interrupt handling
- [GitHub #29720](https://github.com/zephyrproject-rtos/zephyr/issues/29720) - samples/display/lvgl/sample.gui.lvgl fails to build on several boards
- [GitHub #29716](https://github.com/zephyrproject-rtos/zephyr/issues/29716) - Dependency between userspace and memory protection features
- [GitHub #29713](https://github.com/zephyrproject-rtos/zephyr/issues/29713) - nRF5340 - duplicate unit-address
- [GitHub #29711](https://github.com/zephyrproject-rtos/zephyr/issues/29711) - Add BSD socket option SO\_RCVTIMEO
- [GitHub #29710](https://github.com/zephyrproject-rtos/zephyr/issues/29710) - drivers: usb\_dc\_mcux\_ehci: driver broken, build error at all USB test and samples
- [GitHub #29707](https://github.com/zephyrproject-rtos/zephyr/issues/29707) - xtensa xt-xcc -Wno-unused-but-set-variable not work
- [GitHub #29706](https://github.com/zephyrproject-rtos/zephyr/issues/29706) - xtensa xt-xcc inline warning
- [GitHub #29705](https://github.com/zephyrproject-rtos/zephyr/issues/29705) - reel\_board: tests/kernel/sched/schedule\_api/ fails on multiple boards
- [GitHub #29704](https://github.com/zephyrproject-rtos/zephyr/issues/29704) - [Coverity CID :215255] Dereference before null check in tests/subsys/fs/fs\_api/src/test\_fs.c
- [GitHub #29703](https://github.com/zephyrproject-rtos/zephyr/issues/29703) - [Coverity CID :215261] Explicit null dereferenced in subsys/emul/emul\_bmi160.c
- [GitHub #29702](https://github.com/zephyrproject-rtos/zephyr/issues/29702) - [Coverity CID :215232] Dereference after null check in subsys/emul/emul\_bmi160.c
- [GitHub #29701](https://github.com/zephyrproject-rtos/zephyr/issues/29701) - [Coverity CID :215226] Logically dead code in soc/xtensa/intel\_adsp/common/bootloader/boot\_loader.c
- [GitHub #29700](https://github.com/zephyrproject-rtos/zephyr/issues/29700) - [Coverity CID :215253] Unintentional integer overflow in drivers/timer/stm32\_lptim\_timer.c
- [GitHub #29699](https://github.com/zephyrproject-rtos/zephyr/issues/29699) - [Coverity CID :215249] Unused value in drivers/modem/ublox-sara-r4.c
- [GitHub #29698](https://github.com/zephyrproject-rtos/zephyr/issues/29698) - [Coverity CID :215248] Dereference after null check in drivers/modem/hl7800.c
- [GitHub #29697](https://github.com/zephyrproject-rtos/zephyr/issues/29697) - [Coverity CID :215243] Unintentional integer overflow in drivers/timer/stm32\_lptim\_timer.c
- [GitHub #29696](https://github.com/zephyrproject-rtos/zephyr/issues/29696) - [Coverity CID :215241] Buffer not null terminated in drivers/modem/hl7800.c
- [GitHub #29695](https://github.com/zephyrproject-rtos/zephyr/issues/29695) - [Coverity CID :215235] Dereference after null check in drivers/modem/hl7800.c
- [GitHub #29694](https://github.com/zephyrproject-rtos/zephyr/issues/29694) - [Coverity CID :215233] Logically dead code in drivers/modem/hl7800.c
- [GitHub #29693](https://github.com/zephyrproject-rtos/zephyr/issues/29693) - [Coverity CID :215224] Parse warning in drivers/modem/hl7800.c
- [GitHub #29692](https://github.com/zephyrproject-rtos/zephyr/issues/29692) - [Coverity CID :215221] Unchecked return value in drivers/regulator/regulator\_fixed.c
- [GitHub #29690](https://github.com/zephyrproject-rtos/zephyr/issues/29690) - NUCLEO-H745ZI-Q + OpenOCD - connect under reset
- [GitHub #29684](https://github.com/zephyrproject-rtos/zephyr/issues/29684) - Can not make multiple BLE IPSP connection to the same host
- [GitHub #29683](https://github.com/zephyrproject-rtos/zephyr/issues/29683) - BLE IPSP sample doesn’t work on raspberry pi 4 with nrf52840\_mdk board
- [GitHub #29681](https://github.com/zephyrproject-rtos/zephyr/issues/29681) - Add NUCLEO-H723ZG board support
- [GitHub #29677](https://github.com/zephyrproject-rtos/zephyr/issues/29677) - stm32h747i\_disco add ethernet support
- [GitHub #29675](https://github.com/zephyrproject-rtos/zephyr/issues/29675) - Remove pinmux dependency on STM32 boards
- [GitHub #29667](https://github.com/zephyrproject-rtos/zephyr/issues/29667) - RTT Tracing is not working using NXP mimxrt1064\_evk
- [GitHub #29657](https://github.com/zephyrproject-rtos/zephyr/issues/29657) - enc28j60 on nRF52840 stalls during enc28j60\_init\_buffers in zephyr 2.4.0
- [GitHub #29654](https://github.com/zephyrproject-rtos/zephyr/issues/29654) - k\_heap APIs have no tests
- [GitHub #29649](https://github.com/zephyrproject-rtos/zephyr/issues/29649) - net: context: add net\_context api to check if a port is bound
- [GitHub #29639](https://github.com/zephyrproject-rtos/zephyr/issues/29639) - Bluetooth: host: Security procedure failure can terminate GATT client request
- [GitHub #29637](https://github.com/zephyrproject-rtos/zephyr/issues/29637) - 5g is microwave and 4LTE is radio or static?
- [GitHub #29636](https://github.com/zephyrproject-rtos/zephyr/issues/29636) - Bluetooth: Controller: Connection Parameter Update indication timeout
- [GitHub #29634](https://github.com/zephyrproject-rtos/zephyr/issues/29634) - Build error: (Bluetooth: Mesh: split prov.c into two separate modules #28457)
- [GitHub #29632](https://github.com/zephyrproject-rtos/zephyr/issues/29632) - GPIO interrupt support for IO expander
- [GitHub #29631](https://github.com/zephyrproject-rtos/zephyr/issues/29631) - kernel: provide aligned variant of k\_heap\_alloc
- [GitHub #29629](https://github.com/zephyrproject-rtos/zephyr/issues/29629) - Creating a k\_thread as runtime instantiated kernel object using k\_malloc causes general protection fault
- [GitHub #29616](https://github.com/zephyrproject-rtos/zephyr/issues/29616) - Lorawan subsystem stack: missing MLE\_JOIN parameter set
- [GitHub #29611](https://github.com/zephyrproject-rtos/zephyr/issues/29611) - usb/class/dfu: void wait\_for\_usb\_dfu() terminates before DFU operation is completed
- [GitHub #29608](https://github.com/zephyrproject-rtos/zephyr/issues/29608) - question: create runtime instantiated kernel objects in kernel mode
- [GitHub #29594](https://github.com/zephyrproject-rtos/zephyr/issues/29594) - x86\_64: RBX being clobbered in the idle thread
- [GitHub #29590](https://github.com/zephyrproject-rtos/zephyr/issues/29590) - ARM: FPU: using Unshared FP Services mode can still result in corrupted floating point registers
- [GitHub #29589](https://github.com/zephyrproject-rtos/zephyr/issues/29589) - Creating a k\_thread and k\_sem as runtime instantiated kernel object causes general protection fault
- [GitHub #29574](https://github.com/zephyrproject-rtos/zephyr/issues/29574) - question: about CONFIG\_NET\_BUF\_POOL\_USAGE
- [GitHub #29567](https://github.com/zephyrproject-rtos/zephyr/issues/29567) - Using openthread based echo\_client and lwm2m\_client cannot ping the external network address
- [GitHub #29549](https://github.com/zephyrproject-rtos/zephyr/issues/29549) - doc: Zephyr module feature `depends` not documented.
- [GitHub #29544](https://github.com/zephyrproject-rtos/zephyr/issues/29544) - Bluetooth: Mesh: Friend node unable relay message for lpn
- [GitHub #29541](https://github.com/zephyrproject-rtos/zephyr/issues/29541) - CONFIG\_THREAD\_LOCAL\_STORAGE=y build fails with ZEPHYR\_TOOLCHAIN\_VARIANT=gnuarmemb
- [GitHub #29538](https://github.com/zephyrproject-rtos/zephyr/issues/29538) - eswifi recvfrom() not properly implemented on disco\_l475\_iot1
- [GitHub #29534](https://github.com/zephyrproject-rtos/zephyr/issues/29534) - reel\_board:running tests/kernel/workq/work\_queue\_api/ failed
- [GitHub #29533](https://github.com/zephyrproject-rtos/zephyr/issues/29533) - mec15xxevb\_assy6853:running testcase tests/kernel/workq/work\_queue\_api/ failed.
- [GitHub #29532](https://github.com/zephyrproject-rtos/zephyr/issues/29532) - mec15xxevb\_assy6853:running testcase tests/portability/cmsis\_rtos\_v2/ failed.
- [GitHub #29530](https://github.com/zephyrproject-rtos/zephyr/issues/29530) - display: nrf52840: adafruit\_2\_8\_tft\_touch\_v2 shield not working with nrf-spim driver
- [GitHub #29519](https://github.com/zephyrproject-rtos/zephyr/issues/29519) - kernel: provide aligned variants for allocators
- [GitHub #29518](https://github.com/zephyrproject-rtos/zephyr/issues/29518) - sleep in qemu to short
- [GitHub #29499](https://github.com/zephyrproject-rtos/zephyr/issues/29499) - x86 thread stack guards persist after thread exit
- [GitHub #29497](https://github.com/zephyrproject-rtos/zephyr/issues/29497) - Warning in CR2
- [GitHub #29491](https://github.com/zephyrproject-rtos/zephyr/issues/29491) - usb: web USB sample fails Chapter9 USB3CV tests.
- [GitHub #29478](https://github.com/zephyrproject-rtos/zephyr/issues/29478) - fs: fs\_open can corrupt fs\_open\_t object given via zfp parameter
- [GitHub #29468](https://github.com/zephyrproject-rtos/zephyr/issues/29468) - usb: ZEPHYR FATAL ERROR when running USB test for Nordic.
- [GitHub #29467](https://github.com/zephyrproject-rtos/zephyr/issues/29467) - nrf\_qspi\_nor.c Incorrect value used for checking start of RAM address space
- [GitHub #29446](https://github.com/zephyrproject-rtos/zephyr/issues/29446) - pwm: stm32: output signal delayed
- [GitHub #29444](https://github.com/zephyrproject-rtos/zephyr/issues/29444) - Network deadlock
- [GitHub #29442](https://github.com/zephyrproject-rtos/zephyr/issues/29442) - build failure w/sanitycheck for samples/bluetooth/hci\_usb\_h4/sample.bluetooth.hci\_usb\_h4
- [GitHub #29440](https://github.com/zephyrproject-rtos/zephyr/issues/29440) - Missing hw-flow-control; in hci\_uart overlay files
- [GitHub #29435](https://github.com/zephyrproject-rtos/zephyr/issues/29435) - SDCard via SD/SDIO/MMC interfaces
- [GitHub #29430](https://github.com/zephyrproject-rtos/zephyr/issues/29430) - up\_squared\_adsp: Sanitycheck can not run test case on Up\_Squared\_ADSP board
- [GitHub #29429](https://github.com/zephyrproject-rtos/zephyr/issues/29429) - net: dns: enable dns service discovery for mdns service
- [GitHub #29418](https://github.com/zephyrproject-rtos/zephyr/issues/29418) - ieee802154: cc13xx\_cc26xx: bug in rf driver library
- [GitHub #29412](https://github.com/zephyrproject-rtos/zephyr/issues/29412) - sanitycheck: skipped tests marked as failed due to the reason SKIPPED (SRAM overflow)
- [GitHub #29398](https://github.com/zephyrproject-rtos/zephyr/issues/29398) - ICMPv6 error sent with incorrect link layer addresses
- [GitHub #29386](https://github.com/zephyrproject-rtos/zephyr/issues/29386) - unexpected behavior when doing syscall with 7 or more arguments
- [GitHub #29382](https://github.com/zephyrproject-rtos/zephyr/issues/29382) - remove memory domain restriction on system RAM for memory partitions on MMU devices
- [GitHub #29376](https://github.com/zephyrproject-rtos/zephyr/issues/29376) - sanitycheck: “TypeError: ‘NoneType’ object is not iterable”
- [GitHub #29373](https://github.com/zephyrproject-rtos/zephyr/issues/29373) - Some altera DTS bindings have the wrong vendor prefix
- [GitHub #29368](https://github.com/zephyrproject-rtos/zephyr/issues/29368) - STM32: non F1 -pinctrl.dtsi generation files: Limit mode to variants
- [GitHub #29367](https://github.com/zephyrproject-rtos/zephyr/issues/29367) - usb: drivers: add USB support for UP squared
- [GitHub #29364](https://github.com/zephyrproject-rtos/zephyr/issues/29364) - cdc\_acm\_composite fails USB3CV test for Nordic platform.
- [GitHub #29363](https://github.com/zephyrproject-rtos/zephyr/issues/29363) - shell: inability to print 64-bit integers with newlib support
- [GitHub #29357](https://github.com/zephyrproject-rtos/zephyr/issues/29357) - RFC: API Change: Bluetooth: Update indication callback parameters
- [GitHub #29347](https://github.com/zephyrproject-rtos/zephyr/issues/29347) - Network deadlock because of mutex locking order
- [GitHub #29346](https://github.com/zephyrproject-rtos/zephyr/issues/29346) - west boards doesn’t display the arcitecture.
- [GitHub #29330](https://github.com/zephyrproject-rtos/zephyr/issues/29330) - mec15xxevb\_assy6853:running samples/boards/mec15xxevb\_assy6853/power\_management Sleep entry latency is higher than expected
- [GitHub #29329](https://github.com/zephyrproject-rtos/zephyr/issues/29329) - tests: kernel.workqueue.api tests fail on multiple platforms
- [GitHub #29328](https://github.com/zephyrproject-rtos/zephyr/issues/29328) - mec15xxevb\_assy6853:running tests/kernel/workq/work\_queue\_api/ failed
- [GitHub #29327](https://github.com/zephyrproject-rtos/zephyr/issues/29327) - mec15xxevb\_assy6853:region `SRAM` overflowed during build
- [GitHub #29319](https://github.com/zephyrproject-rtos/zephyr/issues/29319) - up\_squared: tests/kernel/timer/timer\_api failed.
- [GitHub #29317](https://github.com/zephyrproject-rtos/zephyr/issues/29317) - mimxrt1015: kernel\_threads\_sched: application meet size issue
- [GitHub #29315](https://github.com/zephyrproject-rtos/zephyr/issues/29315) - twr\_kv58f220m: all application build failure
- [GitHub #29312](https://github.com/zephyrproject-rtos/zephyr/issues/29312) - [RFC] [BOSSA] Improve offset parameter
- [GitHub #29310](https://github.com/zephyrproject-rtos/zephyr/issues/29310) - ble central Repeat read and write to three peripherals error USAGE FAULT
- [GitHub #29309](https://github.com/zephyrproject-rtos/zephyr/issues/29309) - ADC1 doesn’t read correctly on STM32F7
- [GitHub #29308](https://github.com/zephyrproject-rtos/zephyr/issues/29308) - GPIO bit banging i2c init before gpio clock init in stm32f401 plantform,cause same gpio can’t work.
- [GitHub #29307](https://github.com/zephyrproject-rtos/zephyr/issues/29307) - samples/bluetooth/mesh-demo unable to send vendor button message
- [GitHub #29300](https://github.com/zephyrproject-rtos/zephyr/issues/29300) - K\_THREAD\_DEFINE() uses const in a wrong way
- [GitHub #29298](https://github.com/zephyrproject-rtos/zephyr/issues/29298) - xlnx\_psttc\_timer driver has an imprecise z\_clock\_set\_timeout() implementation
- [GitHub #29287](https://github.com/zephyrproject-rtos/zephyr/issues/29287) - spi: SPI\_LOCK\_ON does not hold the lock for multiple spi\_transceive until spi\_release
- [GitHub #29284](https://github.com/zephyrproject-rtos/zephyr/issues/29284) - compilation issues for MinnowBoard/ UpSquared on documentation examples
- [GitHub #29283](https://github.com/zephyrproject-rtos/zephyr/issues/29283) - quickfeather not listed in boards
- [GitHub #29274](https://github.com/zephyrproject-rtos/zephyr/issues/29274) - Can’t get Coded PHY type(S2 or S8)
- [GitHub #29272](https://github.com/zephyrproject-rtos/zephyr/issues/29272) - nordic qspi: readoc / writeoc selection may not work
- [GitHub #29263](https://github.com/zephyrproject-rtos/zephyr/issues/29263) - tests/kernel/mem\_protect/obj\_validation fails build on some boards after recent changes
- [GitHub #29261](https://github.com/zephyrproject-rtos/zephyr/issues/29261) - boards: musca\_b1: post build actions with TF-M might not be done in right order
- [GitHub #29259](https://github.com/zephyrproject-rtos/zephyr/issues/29259) - sanitycheck: sanitycheck defines test expected to fail as FAILED
- [GitHub #29258](https://github.com/zephyrproject-rtos/zephyr/issues/29258) - net: Unable to establish TCP connections from Windows hosts
- [GitHub #29257](https://github.com/zephyrproject-rtos/zephyr/issues/29257) - Race condition in k\_queue\_append and k\_queue\_alloc\_append
- [GitHub #29248](https://github.com/zephyrproject-rtos/zephyr/issues/29248) - board: nrf52840\_mdk: support for qspi flash missing
- [GitHub #29244](https://github.com/zephyrproject-rtos/zephyr/issues/29244) - k\_thread\_resume can cause k\_sem\_take with K\_FOREVER to return -EAGAIN and crash
- [GitHub #29239](https://github.com/zephyrproject-rtos/zephyr/issues/29239) - i2c: mcux driver does not prevent simultaneous transactions
- [GitHub #29235](https://github.com/zephyrproject-rtos/zephyr/issues/29235) - Endless build loop after adding pinctrl dtsi
- [GitHub #29223](https://github.com/zephyrproject-rtos/zephyr/issues/29223) - BLE one central connect multiple peripherals
- [GitHub #29220](https://github.com/zephyrproject-rtos/zephyr/issues/29220) - ARC: tickless idle exit code destroy exception status
- [GitHub #29202](https://github.com/zephyrproject-rtos/zephyr/issues/29202) - core kernel depends on minimal libc `z_prf()`
- [GitHub #29195](https://github.com/zephyrproject-rtos/zephyr/issues/29195) - west fails with custom manifest
- [GitHub #29194](https://github.com/zephyrproject-rtos/zephyr/issues/29194) - Sanitycheck block after passing some test
- [GitHub #29183](https://github.com/zephyrproject-rtos/zephyr/issues/29183) - DHCPv4 retransmission interval gets too large
- [GitHub #29175](https://github.com/zephyrproject-rtos/zephyr/issues/29175) - x86 fails all tests if CONFIG\_X86\_KPTI is disabled
- [GitHub #29173](https://github.com/zephyrproject-rtos/zephyr/issues/29173) - uart\_nrfx\_uart fails uart\_async\_api\_test
- [GitHub #29166](https://github.com/zephyrproject-rtos/zephyr/issues/29166) - sanitycheck `--test-only --device-testing --hardware-map` shouldn’t run tests on all boards from `--build-only`
- [GitHub #29165](https://github.com/zephyrproject-rtos/zephyr/issues/29165) - shell\_print doesn’t support anymore %llx when used with newlib
- [GitHub #29164](https://github.com/zephyrproject-rtos/zephyr/issues/29164) - net: accept() doesn’t return an immediately usable descriptor
- [GitHub #29162](https://github.com/zephyrproject-rtos/zephyr/issues/29162) - Data Access Violation when LOG\_\* is called on ISR context
- [GitHub #29155](https://github.com/zephyrproject-rtos/zephyr/issues/29155) - CAN BUS support on Atmel V71
- [GitHub #29150](https://github.com/zephyrproject-rtos/zephyr/issues/29150) - CONFIG\_BT\_SETTINGS\_CCC\_LAZY\_LOADING never loads CCC
- [GitHub #29148](https://github.com/zephyrproject-rtos/zephyr/issues/29148) - MPU: twr\_ke18f: many kernel application fails when allocate dynamic MPU region
- [GitHub #29146](https://github.com/zephyrproject-rtos/zephyr/issues/29146) - canisotp: mimxrt1064\_evk: no DT\_CHOSEN\_ZEPHYR\_CAN\_PRIMARY\_LABEL defined cause tests failure
- [GitHub #29145](https://github.com/zephyrproject-rtos/zephyr/issues/29145) - net: frdmk64f many net related applications meet hardfault, hal driver assert
- [GitHub #29139](https://github.com/zephyrproject-rtos/zephyr/issues/29139) - tests/kernel/fatal/exception failed on nsim\_sem\_mpu\_stack\_guard board
- [GitHub #29120](https://github.com/zephyrproject-rtos/zephyr/issues/29120) - STM32: Few issues on pinctrl generation script
- [GitHub #29113](https://github.com/zephyrproject-rtos/zephyr/issues/29113) - Build failure with OSPD
- [GitHub #29111](https://github.com/zephyrproject-rtos/zephyr/issues/29111) - Atmel SAM V71 UART\_0 fail
- [GitHub #29109](https://github.com/zephyrproject-rtos/zephyr/issues/29109) - HAL STM32 Missing ETH pin control configurations in DT files
- [GitHub #29101](https://github.com/zephyrproject-rtos/zephyr/issues/29101) - Bluetooth: assertion fail with basic repeated extended advertisement API
- [GitHub #29099](https://github.com/zephyrproject-rtos/zephyr/issues/29099) - net: dns: dns-sd: support for dns service discovery
- [GitHub #29098](https://github.com/zephyrproject-rtos/zephyr/issues/29098) - ATT timeout worker not canceled by destroy, and may operate on disposed object
- [GitHub #29095](https://github.com/zephyrproject-rtos/zephyr/issues/29095) - zefi.py has incorrect assertions
- [GitHub #29092](https://github.com/zephyrproject-rtos/zephyr/issues/29092) - tests/drivers/uart/uart\_async\_api fails on nrf52840dk\_nrf52840 (and additional platforms)
- [GitHub #29089](https://github.com/zephyrproject-rtos/zephyr/issues/29089) - doc: boards: cc1352r\_sensortag: fix minor rst issue
- [GitHub #29083](https://github.com/zephyrproject-rtos/zephyr/issues/29083) - Bluetooth: Host: Inconsistent permission value during discovery procedure
- [GitHub #29078](https://github.com/zephyrproject-rtos/zephyr/issues/29078) - nRF52840 doesn’t start legacy advertisment after extended advertisment
- [GitHub #29074](https://github.com/zephyrproject-rtos/zephyr/issues/29074) - #27901 breaks mikroe\_\* shields overlay
- [GitHub #29070](https://github.com/zephyrproject-rtos/zephyr/issues/29070) - NXP LPC GPIO driver masked set does not use the mask
- [GitHub #29068](https://github.com/zephyrproject-rtos/zephyr/issues/29068) - chosen zephyr,code-partition has no effect on ELF linking start address
- [GitHub #29066](https://github.com/zephyrproject-rtos/zephyr/issues/29066) - kernel: k\_sleep doesn’t handle relative or absolute timeouts >INT\_MAX
- [GitHub #29062](https://github.com/zephyrproject-rtos/zephyr/issues/29062) - samples/bluetooth/peripheral\_hr/sample.bluetooth.peripheral\_hr\_rv32m1\_vega\_ri5cy fails to build on rv32m1\_vega\_ri5cy
- [GitHub #29059](https://github.com/zephyrproject-rtos/zephyr/issues/29059) - HAL: mchp: Missing PCR ids to control PM for certain HW blocks
- [GitHub #29056](https://github.com/zephyrproject-rtos/zephyr/issues/29056) - tests/bluetooth/init/bluetooth.init.test\_ctlr\_dbg fails to build on nrf51dk\_nrf51422
- [GitHub #29050](https://github.com/zephyrproject-rtos/zephyr/issues/29050) - Ugrade lvgl library
- [GitHub #29048](https://github.com/zephyrproject-rtos/zephyr/issues/29048) - Removing pwr-gpio of rt1052 from devicetree will cause build error
- [GitHub #29047](https://github.com/zephyrproject-rtos/zephyr/issues/29047) - Boards: nucleo\_stm32g474re does not build
- [GitHub #29043](https://github.com/zephyrproject-rtos/zephyr/issues/29043) - dirvers: eth\_stm32\_hal: No interrupt is generated on the MII interface.
- [GitHub #29042](https://github.com/zephyrproject-rtos/zephyr/issues/29042) - CONFIG\_SHELL\_HELP=n fails to compile
- [GitHub #29034](https://github.com/zephyrproject-rtos/zephyr/issues/29034) - error in samples/subsys/usb/cdc\_acm
- [GitHub #29025](https://github.com/zephyrproject-rtos/zephyr/issues/29025) - [Coverity CID :214882] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29024](https://github.com/zephyrproject-rtos/zephyr/issues/29024) - [Coverity CID :214878] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29023](https://github.com/zephyrproject-rtos/zephyr/issues/29023) - [Coverity CID :214877] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29022](https://github.com/zephyrproject-rtos/zephyr/issues/29022) - [Coverity CID :214876] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29021](https://github.com/zephyrproject-rtos/zephyr/issues/29021) - [Coverity CID :214874] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29020](https://github.com/zephyrproject-rtos/zephyr/issues/29020) - [Coverity CID :214873] Argument cannot be negative in tests/posix/eventfd/src/main.c
- [GitHub #29019](https://github.com/zephyrproject-rtos/zephyr/issues/29019) - [Coverity CID :214871] Side effect in assertion in tests/kernel/sched/preempt/src/main.c
- [GitHub #29018](https://github.com/zephyrproject-rtos/zephyr/issues/29018) - [Coverity CID :214881] Unchecked return value in subsys/mgmt/ec\_host\_cmd/ec\_host\_cmd\_handler.c
- [GitHub #29017](https://github.com/zephyrproject-rtos/zephyr/issues/29017) - [Coverity CID :214879] Explicit null dereferenced in subsys/emul/spi/emul\_bmi160.c
- [GitHub #29016](https://github.com/zephyrproject-rtos/zephyr/issues/29016) - [Coverity CID :214875] Dereference after null check in subsys/emul/spi/emul\_bmi160.c
- [GitHub #29015](https://github.com/zephyrproject-rtos/zephyr/issues/29015) - [Coverity CID :214880] Out-of-bounds access in subsys/net/ip/tcp2.c
- [GitHub #29014](https://github.com/zephyrproject-rtos/zephyr/issues/29014) - [Coverity CID :214872] Bad bit shift operation in drivers/ethernet/eth\_w5500.c
- [GitHub #29008](https://github.com/zephyrproject-rtos/zephyr/issues/29008) - BLE Connection fails to establish between two nRF52840-USB Dongles with Zephyr controller
- [GitHub #29007](https://github.com/zephyrproject-rtos/zephyr/issues/29007) - OOT manifest+module discovery/builds fail
- [GitHub #29003](https://github.com/zephyrproject-rtos/zephyr/issues/29003) - memory corruption in pkt\_alloc
- [GitHub #28999](https://github.com/zephyrproject-rtos/zephyr/issues/28999) - STM32: Transition to device tree based pinctrl configuration
- [GitHub #28990](https://github.com/zephyrproject-rtos/zephyr/issues/28990) - Docs: Dead links to sample source directories
- [GitHub #28979](https://github.com/zephyrproject-rtos/zephyr/issues/28979) - Automatic reviewer assignment for PR does not seem to work anymore
- [GitHub #28976](https://github.com/zephyrproject-rtos/zephyr/issues/28976) - sanitycheck failing all tests for nsim\_em7d\_v22
- [GitHub #28970](https://github.com/zephyrproject-rtos/zephyr/issues/28970) - clarify thread life-cycle documentation
- [GitHub #28956](https://github.com/zephyrproject-rtos/zephyr/issues/28956) - API-less devices aren’t findable
- [GitHub #28955](https://github.com/zephyrproject-rtos/zephyr/issues/28955) - undesired kernel debug log
- [GitHub #28953](https://github.com/zephyrproject-rtos/zephyr/issues/28953) - winc1500 driver blocks on listen
- [GitHub #28948](https://github.com/zephyrproject-rtos/zephyr/issues/28948) - hci\_usb: ACL transfer not restarted after USB Suspend - Resume
- [GitHub #28942](https://github.com/zephyrproject-rtos/zephyr/issues/28942) - ARC: nsim\_hs\_smp: huge zephyr.hex file generated on build
- [GitHub #28941](https://github.com/zephyrproject-rtos/zephyr/issues/28941) - Civetweb: create separate directory
- [GitHub #28938](https://github.com/zephyrproject-rtos/zephyr/issues/28938) - EFR32BGx Bluetooth Support
- [GitHub #28935](https://github.com/zephyrproject-rtos/zephyr/issues/28935) - support code coverage in unit tests
- [GitHub #28934](https://github.com/zephyrproject-rtos/zephyr/issues/28934) - pinmux: stm32: port remaining pinctrl DT serial definitions for STM32 based boards
- [GitHub #28933](https://github.com/zephyrproject-rtos/zephyr/issues/28933) - mcuboot: Brick when using BOOT\_SWAP\_USING\_MOVE and reset happens during images swap
- [GitHub #28925](https://github.com/zephyrproject-rtos/zephyr/issues/28925) - west failed due to empty value in self.path
- [GitHub #28921](https://github.com/zephyrproject-rtos/zephyr/issues/28921) - MCUboot / smp\_svr sample broken in 2.4.0
- [GitHub #28916](https://github.com/zephyrproject-rtos/zephyr/issues/28916) - net\_if\_down doesn’t clear address
- [GitHub #28912](https://github.com/zephyrproject-rtos/zephyr/issues/28912) - Incorrect macro being used to init a sflist
- [GitHub #28908](https://github.com/zephyrproject-rtos/zephyr/issues/28908) - The same buffers are shared by the 2 Ethernet controllers in the eth\_mcux driver
- [GitHub #28898](https://github.com/zephyrproject-rtos/zephyr/issues/28898) - lwm2m\_client can’t start if mcuboot is enabled
- [GitHub #28897](https://github.com/zephyrproject-rtos/zephyr/issues/28897) - SPI does not work for STM32 min dev board
- [GitHub #28893](https://github.com/zephyrproject-rtos/zephyr/issues/28893) - Double-dot in path’s may cause problems with gcc under Windows
- [GitHub #28887](https://github.com/zephyrproject-rtos/zephyr/issues/28887) - Bluetooth encryption request overrides ongoing phy update
- [GitHub #28881](https://github.com/zephyrproject-rtos/zephyr/issues/28881) - tests/kernel/mem\_protect/sys\_sem: qemu\_x86\_64 intermittent failure
- [GitHub #28876](https://github.com/zephyrproject-rtos/zephyr/issues/28876) - -p doesn’t run a pristine build
- [GitHub #28872](https://github.com/zephyrproject-rtos/zephyr/issues/28872) - Support ESP32 as Bluetooth controller
- [GitHub #28870](https://github.com/zephyrproject-rtos/zephyr/issues/28870) - Peripheral initiated connection parameter update is ignored
- [GitHub #28867](https://github.com/zephyrproject-rtos/zephyr/issues/28867) - ARM Cortex-M4: Semaphores could not be used in ISRs with priority 0?
- [GitHub #28865](https://github.com/zephyrproject-rtos/zephyr/issues/28865) - Doc: Generate documentation using dts bindings
- [GitHub #28854](https://github.com/zephyrproject-rtos/zephyr/issues/28854) - `CONFIG_STACK_POINTER_RANDOM` may be undefined
- [GitHub #28847](https://github.com/zephyrproject-rtos/zephyr/issues/28847) - code\_relocation sample does not work on windows
- [GitHub #28844](https://github.com/zephyrproject-rtos/zephyr/issues/28844) - Double quote prepended when exporting CMAKE compile option using zephyr\_get\_compile\_options\_for\_lang()
- [GitHub #28833](https://github.com/zephyrproject-rtos/zephyr/issues/28833) - STM32: SPI DMA Driver - HW CS handling not compatible with spi\_nor (Winbond W25Q)
- [GitHub #28826](https://github.com/zephyrproject-rtos/zephyr/issues/28826) - nRF QSPI flash driver broken for GD25Q16
- [GitHub #28822](https://github.com/zephyrproject-rtos/zephyr/issues/28822) - Improve STM32 LL HAL usage
- [GitHub #28809](https://github.com/zephyrproject-rtos/zephyr/issues/28809) - Enable bt\_gatt\_notify() to overwrite notified value before sending rather than queue values
- [GitHub #28794](https://github.com/zephyrproject-rtos/zephyr/issues/28794) - RFC: API Change: k\_work
- [GitHub #28791](https://github.com/zephyrproject-rtos/zephyr/issues/28791) - STM32: Clock recovery system (CRS) support
- [GitHub #28787](https://github.com/zephyrproject-rtos/zephyr/issues/28787) - lwm2m-client sample can’t be build with openthread and DTLS
- [GitHub #28785](https://github.com/zephyrproject-rtos/zephyr/issues/28785) - shell: It should be possible to get list of commands without pressing tab
- [GitHub #28777](https://github.com/zephyrproject-rtos/zephyr/issues/28777) - Memory pool issue
- [GitHub #28775](https://github.com/zephyrproject-rtos/zephyr/issues/28775) - Update to TFM v1.2 release
- [GitHub #28774](https://github.com/zephyrproject-rtos/zephyr/issues/28774) - build failure: several bluetooth samples fail to build on nrf51dk\_nrf51422
- [GitHub #28773](https://github.com/zephyrproject-rtos/zephyr/issues/28773) - Lower Link Layer code use upper link layer function have “ undefined reference to”
- [GitHub #28758](https://github.com/zephyrproject-rtos/zephyr/issues/28758) - ASSERTION FAIL [conn->in\_retransmission == 1] with civetweb sample application
- [GitHub #28745](https://github.com/zephyrproject-rtos/zephyr/issues/28745) - Bug in drivers/modem/hl7800.c
- [GitHub #28739](https://github.com/zephyrproject-rtos/zephyr/issues/28739) - Bluetooth: Mesh: onoff\_level\_lighting\_vnd sample fails provisioning
- [GitHub #28735](https://github.com/zephyrproject-rtos/zephyr/issues/28735) - NULL pointer access in zsock\_getsockname\_ctx with TCP2
- [GitHub #28723](https://github.com/zephyrproject-rtos/zephyr/issues/28723) - Does not respect python virtualenv
- [GitHub #28722](https://github.com/zephyrproject-rtos/zephyr/issues/28722) - Bluetooth: provide `struct bt_conn` to ccc\_changed callback
- [GitHub #28714](https://github.com/zephyrproject-rtos/zephyr/issues/28714) - Bluetooth: PTS upper tester: GAP/CONN/NCON/BV-02-C Fails because of usage of NRPA
- [GitHub #28709](https://github.com/zephyrproject-rtos/zephyr/issues/28709) - phandle-array doesn’t allow array of just phandles
- [GitHub #28706](https://github.com/zephyrproject-rtos/zephyr/issues/28706) - west build -p auto -b nrf52840dk\_nrf52840 error: HAS\_SEGGER\_RTT
- [GitHub #28701](https://github.com/zephyrproject-rtos/zephyr/issues/28701) - ASSERTION FAIL [!radio\_is\_ready()]
- [GitHub #28699](https://github.com/zephyrproject-rtos/zephyr/issues/28699) - Bluetooth: controller: Speed up disconnect process when slave latency is used
- [GitHub #28694](https://github.com/zephyrproject-rtos/zephyr/issues/28694) - k\_wakeup follwed by k\_thread\_resume call causes system freeze
- [GitHub #28693](https://github.com/zephyrproject-rtos/zephyr/issues/28693) - FCB support for non-0xFF flash erase values
- [GitHub #28691](https://github.com/zephyrproject-rtos/zephyr/issues/28691) - tests: arch: arm: arm\_thread\_swap: fails with bus fault
- [GitHub #28688](https://github.com/zephyrproject-rtos/zephyr/issues/28688) - Bluetooth: provide `struct bt_gatt_indicate_params` to `bt_gatt_indicate_func_t`
- [GitHub #28670](https://github.com/zephyrproject-rtos/zephyr/issues/28670) - drivers: flash: bluetooth: stm32wb: attempt to erase internal flash before enabling Bluetooth cause fatal error
- [GitHub #28664](https://github.com/zephyrproject-rtos/zephyr/issues/28664) - Decide whether to enable HW\_STACK\_PROTECTION by default
- [GitHub #28650](https://github.com/zephyrproject-rtos/zephyr/issues/28650) - GCC-10.2 link issue w/g++ on aarch64
- [GitHub #28629](https://github.com/zephyrproject-rtos/zephyr/issues/28629) - tests: kernel: common: and common.misra are failing on nrf52840dk
- [GitHub #28620](https://github.com/zephyrproject-rtos/zephyr/issues/28620) - 6LowPAN ipsp: ping host -> µc failes, ping µc -> host works. after that: ping host -> µc works
- [GitHub #28613](https://github.com/zephyrproject-rtos/zephyr/issues/28613) - cannot set GDB watchpoints on QEMU x86 with icount enabled
- [GitHub #28590](https://github.com/zephyrproject-rtos/zephyr/issues/28590) - up\_squared\_adsp:running tests/kernel/smp/ failed
- [GitHub #28589](https://github.com/zephyrproject-rtos/zephyr/issues/28589) - up\_squared\_adsp:running tests/kernel/workq/work\_queue/ failed
- [GitHub #28587](https://github.com/zephyrproject-rtos/zephyr/issues/28587) - Data corruption while serving large files via HTTP with TCP2
- [GitHub #28556](https://github.com/zephyrproject-rtos/zephyr/issues/28556) - mec15xxevb\_assy6853:running tests/kernel/sched/schedule\_api/ failed
- [GitHub #28547](https://github.com/zephyrproject-rtos/zephyr/issues/28547) - up\_squared: tests/subsys/debug/coredump failed using twister command.
- [GitHub #28544](https://github.com/zephyrproject-rtos/zephyr/issues/28544) - Null pointer dereference in ll\_adv\_aux\_ad\_data\_set
- [GitHub #28533](https://github.com/zephyrproject-rtos/zephyr/issues/28533) - soc: ti\_simplelink: cc13xx-cc26xx: kconfig for subghz 802.15.4
- [GitHub #28509](https://github.com/zephyrproject-rtos/zephyr/issues/28509) - series-push-hook.sh: Don’t parse then-master-to-latest-master commits after rebase to lastest
- [GitHub #28504](https://github.com/zephyrproject-rtos/zephyr/issues/28504) - dfu: dfu libraries might fails to compile on redefined functions while building MCUBoot
- [GitHub #28502](https://github.com/zephyrproject-rtos/zephyr/issues/28502) - USB DFU class: support MCUBoot CONFIG\_SINGLE\_APPLICATION\_SLOT
- [GitHub #28493](https://github.com/zephyrproject-rtos/zephyr/issues/28493) - Sanitycheck on ARC em\_starterkit\_em7d has many tests timeout
- [GitHub #28483](https://github.com/zephyrproject-rtos/zephyr/issues/28483) - Fix nanosleep(2) for sub-microsecond durations
- [GitHub #28473](https://github.com/zephyrproject-rtos/zephyr/issues/28473) - Mcuboot fails to compile when using single image and usb dfu
- [GitHub #28469](https://github.com/zephyrproject-rtos/zephyr/issues/28469) - Unable to capture adc signal at 8ksps when using nrf52840dk board.
- [GitHub #28462](https://github.com/zephyrproject-rtos/zephyr/issues/28462) - SHIELD not handled correct in CMake when using custom board
- [GitHub #28461](https://github.com/zephyrproject-rtos/zephyr/issues/28461) - `HCI_CMD_TIMEOUT` when setting ext adv data in the hci\_usb project
- [GitHub #28456](https://github.com/zephyrproject-rtos/zephyr/issues/28456) - TOOLCHAIN\_LD\_FLAGS setting of -mabi/-march aren’t propagated to linker invocation on RISC-V
- [GitHub #28442](https://github.com/zephyrproject-rtos/zephyr/issues/28442) - How handle IRQ\_CONNECT const requirement?
- [GitHub #28406](https://github.com/zephyrproject-rtos/zephyr/issues/28406) - Condition variables
- [GitHub #28383](https://github.com/zephyrproject-rtos/zephyr/issues/28383) - bq274xx sample is not working
- [GitHub #28363](https://github.com/zephyrproject-rtos/zephyr/issues/28363) - ssd16xx: off-by-one with non-multiple-of-eight heights
- [GitHub #28355](https://github.com/zephyrproject-rtos/zephyr/issues/28355) - Document limitations of net\_buf queuing functions
- [GitHub #28309](https://github.com/zephyrproject-rtos/zephyr/issues/28309) - Sample/subsys/fs/littlefs with board=nucleo\_f429zi don’t work
- [GitHub #28299](https://github.com/zephyrproject-rtos/zephyr/issues/28299) - net: lwm2m: Improve token handling
- [GitHub #28298](https://github.com/zephyrproject-rtos/zephyr/issues/28298) - Deep sleep(system off) is not working with LVGL and display driver
- [GitHub #28296](https://github.com/zephyrproject-rtos/zephyr/issues/28296) - test\_essential\_thread\_abort: lpcxpresso55s16\_ns test failure
- [GitHub #28278](https://github.com/zephyrproject-rtos/zephyr/issues/28278) - PWM silently fails when changing output frequency on stm32
- [GitHub #28220](https://github.com/zephyrproject-rtos/zephyr/issues/28220) - flash: revise API to remove block restrictions on write operations
- [GitHub #28177](https://github.com/zephyrproject-rtos/zephyr/issues/28177) - gPTP gptp\_priority\_vector struct field ordering is wrong
- [GitHub #28176](https://github.com/zephyrproject-rtos/zephyr/issues/28176) - [Coverity CID :214217] Out-of-bounds access in tests/kernel/mem\_protect/mem\_map/src/main.c
- [GitHub #28175](https://github.com/zephyrproject-rtos/zephyr/issues/28175) - [Coverity CID :214214] Uninitialized pointer read in tests/benchmarks/data\_structure\_perf/rbtree\_perf/src/rbtree\_perf.c
- [GitHub #28170](https://github.com/zephyrproject-rtos/zephyr/issues/28170) - [Coverity CID :214222] Unrecoverable parse warning in include/ec\_host\_cmd.h
- [GitHub #28168](https://github.com/zephyrproject-rtos/zephyr/issues/28168) - [Coverity CID :214218] Unused value in subsys/mgmt/osdp/src/osdp.c
- [GitHub #28159](https://github.com/zephyrproject-rtos/zephyr/issues/28159) - [Coverity CID :214216] Logically dead code in drivers/pwm/pwm\_stm32.c
- [GitHub #28155](https://github.com/zephyrproject-rtos/zephyr/issues/28155) - sam\_e70\_xplained:running samples/net/sockets/civetweb/ failed
- [GitHub #28124](https://github.com/zephyrproject-rtos/zephyr/issues/28124) - Linking external lib against POSIX API
- [GitHub #28117](https://github.com/zephyrproject-rtos/zephyr/issues/28117) - CoAP/LWM2M: Clean Packet Retransmission Concept
- [GitHub #28113](https://github.com/zephyrproject-rtos/zephyr/issues/28113) - Embed precise Zephyr version & platform name in sanitycheck output .xml
- [GitHub #28094](https://github.com/zephyrproject-rtos/zephyr/issues/28094) - samples: drivers: spi\_flash\_at45: Not work for boards without internal flash driver
- [GitHub #28092](https://github.com/zephyrproject-rtos/zephyr/issues/28092) - Make SPI speed of SDHC card configurable
- [GitHub #28014](https://github.com/zephyrproject-rtos/zephyr/issues/28014) - tests: kernel: mem\_protect: sys\_sem: failed when CONFIG\_FPU is activated
- [GitHub #27999](https://github.com/zephyrproject-rtos/zephyr/issues/27999) - Add QSPI tests for microchip mec1521 board, drivers are in zephyr/drivers/spi, to be tested on mec15xxevb\_assy6853
- [GitHub #27997](https://github.com/zephyrproject-rtos/zephyr/issues/27997) - Errors in copy paste lengthy script into Shell Console
- [GitHub #27981](https://github.com/zephyrproject-rtos/zephyr/issues/27981) - Low UART utilization for hci\_uart
- [GitHub #27957](https://github.com/zephyrproject-rtos/zephyr/issues/27957) - flash signed binaries: key path and version
- [GitHub #27914](https://github.com/zephyrproject-rtos/zephyr/issues/27914) - frdm\_k64f async uart api
- [GitHub #27892](https://github.com/zephyrproject-rtos/zephyr/issues/27892) - [v2.1.x] lib: updatehub: Improve download on slow networks and security fix
- [GitHub #27890](https://github.com/zephyrproject-rtos/zephyr/issues/27890) - [v2.2.x] lib: updatehub: Improve download on slow networks and security fix
- [GitHub #27881](https://github.com/zephyrproject-rtos/zephyr/issues/27881) - Zephyr requirements.txt fails to install on Python 3.9rc1
- [GitHub #27879](https://github.com/zephyrproject-rtos/zephyr/issues/27879) - Make i2c\_slave callbacks public in the documentation
- [GitHub #27856](https://github.com/zephyrproject-rtos/zephyr/issues/27856) - Support per thread runtime statistics
- [GitHub #27846](https://github.com/zephyrproject-rtos/zephyr/issues/27846) - Weird ADC outliers on nrf52
- [GitHub #27841](https://github.com/zephyrproject-rtos/zephyr/issues/27841) - samples: disk: unable to access sd card
- [GitHub #27829](https://github.com/zephyrproject-rtos/zephyr/issues/27829) - sys\_mutex and futex missing documentation
- [GitHub #27809](https://github.com/zephyrproject-rtos/zephyr/issues/27809) - Cannot enable MPU for nucleo\_l552ze\_q\_ns
- [GitHub #27785](https://github.com/zephyrproject-rtos/zephyr/issues/27785) - memory domain arch implementation not correct with respect to SMP on ARC
- [GitHub #27716](https://github.com/zephyrproject-rtos/zephyr/issues/27716) - Bluetooth: Mesh: Devices relay their own messages (even with relay disabled!)
- [GitHub #27677](https://github.com/zephyrproject-rtos/zephyr/issues/27677) - RFC: Get rid of shell UART device selection in Kconfig
- [GitHub #27672](https://github.com/zephyrproject-rtos/zephyr/issues/27672) - [v2.2] BLE Transaction Collision
- [GitHub #27633](https://github.com/zephyrproject-rtos/zephyr/issues/27633) - arm64 SMP
- [GitHub #27628](https://github.com/zephyrproject-rtos/zephyr/issues/27628) - stm32: i2c bus failure when using USB
- [GitHub #27622](https://github.com/zephyrproject-rtos/zephyr/issues/27622) - Power management for modems using PPP
- [GitHub #27600](https://github.com/zephyrproject-rtos/zephyr/issues/27600) - JSON Api refuse to decode null value
- [GitHub #27596](https://github.com/zephyrproject-rtos/zephyr/issues/27596) - logging: backend inconsistency with console and shell
- [GitHub #27583](https://github.com/zephyrproject-rtos/zephyr/issues/27583) - sanitycheck does not fail on SRAM overflow, add option to make it fail on those cases.
- [GitHub #27574](https://github.com/zephyrproject-rtos/zephyr/issues/27574) - mec15xxevb\_assy6853:arch.arm.arch.arm.no.multithreading failed to run
- [GitHub #27573](https://github.com/zephyrproject-rtos/zephyr/issues/27573) - coverage: When enable coverage, some testcases need more time
- [GitHub #27570](https://github.com/zephyrproject-rtos/zephyr/issues/27570) - up\_squared:logging.add.logging.add.async failed
- [GitHub #27561](https://github.com/zephyrproject-rtos/zephyr/issues/27561) - drivers: gpio: pca9555 : Add GPIO driver enable interrupt support
- [GitHub #27559](https://github.com/zephyrproject-rtos/zephyr/issues/27559) - How to use stm32cubeIDE to build and debug?
- [GitHub #27525](https://github.com/zephyrproject-rtos/zephyr/issues/27525) - Including STM32Cube’s USB PD support to Zephyr
- [GitHub #27510](https://github.com/zephyrproject-rtos/zephyr/issues/27510) - [v1.14] Bluetooth: controller: Fix uninit conn context after invalid channel map
- [GitHub #27506](https://github.com/zephyrproject-rtos/zephyr/issues/27506) - driver: peci: mchp: Ping command is failing due to improper tx wait timeout.
- [GitHub #27490](https://github.com/zephyrproject-rtos/zephyr/issues/27490) - arch/common/isr\_tables.c compilation fails with CONFIG\_NUM\_IRQS=0
- [GitHub #27487](https://github.com/zephyrproject-rtos/zephyr/issues/27487) - storage/stream: should use only flash driver public API
- [GitHub #27468](https://github.com/zephyrproject-rtos/zephyr/issues/27468) - BT Host: Periodic Advertisement delayed receive
- [GitHub #27467](https://github.com/zephyrproject-rtos/zephyr/issues/27467) - BT Host: Periodic Advertiser List
- [GitHub #27466](https://github.com/zephyrproject-rtos/zephyr/issues/27466) - BT Host: Periodic Advertisement Sync Transfer (PAST)
- [GitHub #27457](https://github.com/zephyrproject-rtos/zephyr/issues/27457) - Add support for Nordic nrfx PDM driver for Nordic Thingy52
- [GitHub #27423](https://github.com/zephyrproject-rtos/zephyr/issues/27423) - RFC: API change: clock\_control: Change parameters of clock\_control\_async\_on
- [GitHub #27417](https://github.com/zephyrproject-rtos/zephyr/issues/27417) - CivetWeb Enable WebSocket
- [GitHub #27396](https://github.com/zephyrproject-rtos/zephyr/issues/27396) - samples/subsys/logging/logger timeout when sanitycheck enable coverage, it needs a filter
- [GitHub #27369](https://github.com/zephyrproject-rtos/zephyr/issues/27369) - spi: stm32: dma: rx transfer error when spi\_write called
- [GitHub #27367](https://github.com/zephyrproject-rtos/zephyr/issues/27367) - Sprintf - error while sending data to SD card
- [GitHub #27350](https://github.com/zephyrproject-rtos/zephyr/issues/27350) - ADC: adc shell failure when mismatch with dts device label
- [GitHub #27332](https://github.com/zephyrproject-rtos/zephyr/issues/27332) - [v2.3.x] lib: updatehub: Improve download on slow networks and security fix
- [GitHub #27299](https://github.com/zephyrproject-rtos/zephyr/issues/27299) - espi: xec: Whenever eSPI host indicates we are entering DnX mode, notification doesn’t reach application
- [GitHub #27279](https://github.com/zephyrproject-rtos/zephyr/issues/27279) - CMSIS RTOS v1 Signals Implementation Issue
- [GitHub #27231](https://github.com/zephyrproject-rtos/zephyr/issues/27231) - Sending data to .csv file on SD card - ERROR CS control inhibited (no GPIO device)
- [GitHub #27195](https://github.com/zephyrproject-rtos/zephyr/issues/27195) - Sanitycheck: BinaryHandler can’t kill children processes
- [GitHub #27176](https://github.com/zephyrproject-rtos/zephyr/issues/27176) - [v1.14] Restore socket descriptor permission management
- [GitHub #27174](https://github.com/zephyrproject-rtos/zephyr/issues/27174) - TCP Server don’t get the right data from the client
- [GitHub #27146](https://github.com/zephyrproject-rtos/zephyr/issues/27146) - [Coverity CID :211510] Unchecked return value in lib/posix/semaphore.c
- [GitHub #27122](https://github.com/zephyrproject-rtos/zephyr/issues/27122) - Implement watchdog driver for mimxrt1050\_evk
- [GitHub #27068](https://github.com/zephyrproject-rtos/zephyr/issues/27068) - ESP-IDF Bootloader bootloop
- [GitHub #27055](https://github.com/zephyrproject-rtos/zephyr/issues/27055) - BlueZ with ESP32 boards supported or not?
- [GitHub #27047](https://github.com/zephyrproject-rtos/zephyr/issues/27047) - zefi.py assumes host GCC is x86
- [GitHub #27031](https://github.com/zephyrproject-rtos/zephyr/issues/27031) - Zephyr OpenThread Simulation
- [GitHub #27020](https://github.com/zephyrproject-rtos/zephyr/issues/27020) - civetweb issues
- [GitHub #27006](https://github.com/zephyrproject-rtos/zephyr/issues/27006) - unsynchronized newlib uintptr\_t and PRIxPTR definition on xtensa
- [GitHub #26987](https://github.com/zephyrproject-rtos/zephyr/issues/26987) - [Coverity CID :211475] Unintended sign extension in drivers/sensor/wsen\_itds/itds.c
- [GitHub #26975](https://github.com/zephyrproject-rtos/zephyr/issues/26975) - Control never returns from stm32\_i2c\_msg\_write(), when SCL is pulled low permanently (hardware fault occurs)
- [GitHub #26961](https://github.com/zephyrproject-rtos/zephyr/issues/26961) - occasional sanitycheck failures in samples/subsys/settings
- [GitHub #26949](https://github.com/zephyrproject-rtos/zephyr/issues/26949) - sanitycheck gets overwhelmed by console output
- [GitHub #26912](https://github.com/zephyrproject-rtos/zephyr/issues/26912) - arm: cortex\_r: config\_userspace: hang during early power-up
- [GitHub #26873](https://github.com/zephyrproject-rtos/zephyr/issues/26873) - WIFI\_ESP: sockets left opened after unexpected reset of ESP
- [GitHub #26829](https://github.com/zephyrproject-rtos/zephyr/issues/26829) - GSM modem example on stm32f103 bluepill
- [GitHub #26819](https://github.com/zephyrproject-rtos/zephyr/issues/26819) - drivers: modem: SARA modem driver leaks sockets
- [GitHub #26807](https://github.com/zephyrproject-rtos/zephyr/issues/26807) - Bluetooth HCI USB sample is not working
- [GitHub #26799](https://github.com/zephyrproject-rtos/zephyr/issues/26799) - Introduce p99
- [GitHub #26794](https://github.com/zephyrproject-rtos/zephyr/issues/26794) - arc: smp: different sanitycheck results of ARC hsdk’s 2 cores and 4 cores configuration
- [GitHub #26732](https://github.com/zephyrproject-rtos/zephyr/issues/26732) - Advertise only on single bluetooth channel
- [GitHub #26722](https://github.com/zephyrproject-rtos/zephyr/issues/26722) - uarte\_nrfx\_poll\_out() in NRF UARTE driver does not work with hardware flow control
- [GitHub #26665](https://github.com/zephyrproject-rtos/zephyr/issues/26665) - Implement reset for ARC development boards
- [GitHub #26656](https://github.com/zephyrproject-rtos/zephyr/issues/26656) - SAM0 USB transfer slot leak
- [GitHub #26637](https://github.com/zephyrproject-rtos/zephyr/issues/26637) - How to identify sensor device?
- [GitHub #26584](https://github.com/zephyrproject-rtos/zephyr/issues/26584) - Multicast emission is only possible for ipv4 starting with 224.
- [GitHub #26533](https://github.com/zephyrproject-rtos/zephyr/issues/26533) - Support newlib for Aarch64 architecture
- [GitHub #26522](https://github.com/zephyrproject-rtos/zephyr/issues/26522) - Reported “Supported shields” list includes boards
- [GitHub #26515](https://github.com/zephyrproject-rtos/zephyr/issues/26515) - timers: platforms using cortex\_m\_systick does not enter indefinite wait on SLOPPY\_IDLE
- [GitHub #26500](https://github.com/zephyrproject-rtos/zephyr/issues/26500) - sanitycheck reports failing tests with test\_slice\_scheduling()
- [GitHub #26488](https://github.com/zephyrproject-rtos/zephyr/issues/26488) - Bluetooth: Connection failure using frdm\_kw41z shield
- [GitHub #26486](https://github.com/zephyrproject-rtos/zephyr/issues/26486) - possible SMP race with k\_thread\_join()
- [GitHub #26477](https://github.com/zephyrproject-rtos/zephyr/issues/26477) - GPIO sim driver
- [GitHub #26443](https://github.com/zephyrproject-rtos/zephyr/issues/26443) - sanitycheck shall generate results and detailed information about tests and environment in json format.
- [GitHub #26409](https://github.com/zephyrproject-rtos/zephyr/issues/26409) - Clearing of previously initialized data during IPv6 interface init causes infinite loop, memory corruption in timer ISR
- [GitHub #26383](https://github.com/zephyrproject-rtos/zephyr/issues/26383) - OpenThread NCP radio-only
- [GitHub #26372](https://github.com/zephyrproject-rtos/zephyr/issues/26372) - qspi driver does not work if multithreading is disabled
- [GitHub #26330](https://github.com/zephyrproject-rtos/zephyr/issues/26330) - tcp: low bulk receive performance due to window handling
- [GitHub #26315](https://github.com/zephyrproject-rtos/zephyr/issues/26315) - ieee802154: cc13xx\_cc26xx: sub\_ghz support
- [GitHub #26312](https://github.com/zephyrproject-rtos/zephyr/issues/26312) - drivers: ieee802154: cc13xx\_cc26xx: adopt hal/ti rf driverlib
- [GitHub #26275](https://github.com/zephyrproject-rtos/zephyr/issues/26275) - USB MSC fails ‘Command Set Test’ from USB3CV.
- [GitHub #26272](https://github.com/zephyrproject-rtos/zephyr/issues/26272) - Cannot use alternative simulation runner with sanitycheck
- [GitHub #26227](https://github.com/zephyrproject-rtos/zephyr/issues/26227) - icount support for qemu\_arc\_{em,hs}
- [GitHub #26225](https://github.com/zephyrproject-rtos/zephyr/issues/26225) - x86\_64 doesn’t seem to be handling spurious interrupts properly
- [GitHub #26219](https://github.com/zephyrproject-rtos/zephyr/issues/26219) - sys/util: add support for mapping lists with per-element terminal symbols
- [GitHub #26172](https://github.com/zephyrproject-rtos/zephyr/issues/26172) - Zephyr Master/Slave not conforming with Core Spec. 5.2 connection policies
- [GitHub #26163](https://github.com/zephyrproject-rtos/zephyr/issues/26163) - qemu\_arc\_{em,hs} keeps failing in CI on tests/kernel/lifo/lifo\_usage
- [GitHub #26142](https://github.com/zephyrproject-rtos/zephyr/issues/26142) - cmake warning: “Policy CMP0077 is not set”
- [GitHub #26084](https://github.com/zephyrproject-rtos/zephyr/issues/26084) - 2.4 Release Checklist
- [GitHub #26072](https://github.com/zephyrproject-rtos/zephyr/issues/26072) - refactor struct device to reduce RAM demands
- [GitHub #26051](https://github.com/zephyrproject-rtos/zephyr/issues/26051) - shell: uart: Allow a change in the shell initalisation to let routing it through USB UART
- [GitHub #26050](https://github.com/zephyrproject-rtos/zephyr/issues/26050) - devicetree: provide access to node ordinal
- [GitHub #26026](https://github.com/zephyrproject-rtos/zephyr/issues/26026) - RFC: drivers: pwm: add functions for capturing pwm pulse width and period
- [GitHub #25956](https://github.com/zephyrproject-rtos/zephyr/issues/25956) - Including header files from modules into app
- [GitHub #25927](https://github.com/zephyrproject-rtos/zephyr/issues/25927) - ARM: Core Stack Improvements/Bug fixes for 2.4 release
- [GitHub #25918](https://github.com/zephyrproject-rtos/zephyr/issues/25918) - qemu\_nios2 crash when enabled icount
- [GitHub #25832](https://github.com/zephyrproject-rtos/zephyr/issues/25832) - [test][kernel][lpcxpresso55s69\_ns] kernel cases meet ESF could not be retrieved successfully
- [GitHub #25604](https://github.com/zephyrproject-rtos/zephyr/issues/25604) - USB: enable/disable a class driver at runtime
- [GitHub #25600](https://github.com/zephyrproject-rtos/zephyr/issues/25600) - wifi\_eswifi: Unable to start TCP/UDP client
- [GitHub #25592](https://github.com/zephyrproject-rtos/zephyr/issues/25592) - Remove checks on board undocumented DT strings
- [GitHub #25597](https://github.com/zephyrproject-rtos/zephyr/issues/25597) - west sign fails to find header size or padding
- [GitHub #25508](https://github.com/zephyrproject-rtos/zephyr/issues/25508) - tests: add additonal power management tests
- [GitHub #25507](https://github.com/zephyrproject-rtos/zephyr/issues/25507) - up\_squared:tests/portability/cmsis\_rtos\_v2 failed.
- [GitHub #25482](https://github.com/zephyrproject-rtos/zephyr/issues/25482) - outdated recommendations for SYS\_CLOCK\_TICKS\_PER\_SEC
- [GitHub #25466](https://github.com/zephyrproject-rtos/zephyr/issues/25466) - log build errors are not helpful
- [GitHub #25434](https://github.com/zephyrproject-rtos/zephyr/issues/25434) - nRF5340 Bluetooth peripheral\_hr sample high power consumption
- [GitHub #25413](https://github.com/zephyrproject-rtos/zephyr/issues/25413) - soc: ti\_simplelink: kconfig: ble: placeholder for hal\_ti
- [GitHub #25409](https://github.com/zephyrproject-rtos/zephyr/issues/25409) - Inconsistent naming of Kconfig options related to stack sizes of various Zephyr components
- [GitHub #25395](https://github.com/zephyrproject-rtos/zephyr/issues/25395) - Websocket Server API
- [GitHub #25379](https://github.com/zephyrproject-rtos/zephyr/issues/25379) - Bluetooth mesh example not working
- [GitHub #25314](https://github.com/zephyrproject-rtos/zephyr/issues/25314) - Bluetooth: controller: legacy: Backport conformance test related changes
- [GitHub #25302](https://github.com/zephyrproject-rtos/zephyr/issues/25302) - lwm2m client sample bootstrap server support
- [GitHub #25182](https://github.com/zephyrproject-rtos/zephyr/issues/25182) - Raspberry Pi 4B Support
- [GitHub #25173](https://github.com/zephyrproject-rtos/zephyr/issues/25173) - k\_sem\_give(struct k\_sem \*sem) should report failure when the semaphore is full
- [GitHub #25164](https://github.com/zephyrproject-rtos/zephyr/issues/25164) - Remove `default:` functionality from devicetree bindings
- [GitHub #25015](https://github.com/zephyrproject-rtos/zephyr/issues/25015) - Bluetooth Isochronous Channels Support
- [GitHub #25010](https://github.com/zephyrproject-rtos/zephyr/issues/25010) - disco\_l475\_iot1 don’t confirm MCUBoot slot-1 image
- [GitHub #24803](https://github.com/zephyrproject-rtos/zephyr/issues/24803) - ADC driver test hangs on atsame54\_xpro
- [GitHub #24652](https://github.com/zephyrproject-rtos/zephyr/issues/24652) - sanitycheck doesn’t keep my cores busy
- [GitHub #24453](https://github.com/zephyrproject-rtos/zephyr/issues/24453) - docs: Allow to use the exact current zephyr version number in place of /latest/ in documentation URLs
- [GitHub #24358](https://github.com/zephyrproject-rtos/zephyr/issues/24358) - deprecate and remove old k\_mem\_pool / sys\_mem\_pool APIs
- [GitHub #24338](https://github.com/zephyrproject-rtos/zephyr/issues/24338) - UICR & FICR missing from nRF52\* devicetree files
- [GitHub #24211](https://github.com/zephyrproject-rtos/zephyr/issues/24211) - [v2.2.x] lib: updatehub: Not working on Zephyr 2.x
- [GitHub #23917](https://github.com/zephyrproject-rtos/zephyr/issues/23917) - Kconfig: problems with using backslash-escapes in “default” value of “string” option
- [GitHub #23874](https://github.com/zephyrproject-rtos/zephyr/issues/23874) - Test case to check registers data
- [GitHub #23866](https://github.com/zephyrproject-rtos/zephyr/issues/23866) - sample hci\_usb fails with zephyr 2.2.0 (worked with zephyr 2.1.0)
- [GitHub #23729](https://github.com/zephyrproject-rtos/zephyr/issues/23729) - hifive1\_revb fails to work with samples/subsys/console/getline
- [GitHub #23314](https://github.com/zephyrproject-rtos/zephyr/issues/23314) - Bluetooth: controller: Use defines for 625 us and 1250 us
- [GitHub #23302](https://github.com/zephyrproject-rtos/zephyr/issues/23302) - Poor TCP performance
- [GitHub #23212](https://github.com/zephyrproject-rtos/zephyr/issues/23212) - ARC: SMP: Enable use of ARConnect Inter-core Debug Unit
- [GitHub #23210](https://github.com/zephyrproject-rtos/zephyr/issues/23210) - mimxrt1050\_evk:tests/net/iface failed with v1.14 branch.
- [GitHub #23063](https://github.com/zephyrproject-rtos/zephyr/issues/23063) - CMSIS v2 osThreadJoin does not work if thread exits with osThreadExit
- [GitHub #23062](https://github.com/zephyrproject-rtos/zephyr/issues/23062) - thread\_num / thread\_num\_dynamic are never decremented in CMSIS v2 thread.c
- [GitHub #22942](https://github.com/zephyrproject-rtos/zephyr/issues/22942) - Missing TX power options for nRF52833
- [GitHub #22771](https://github.com/zephyrproject-rtos/zephyr/issues/22771) - z\_x86\_check\_stack\_bounds() doesn’t work right for nested IRQs on x86-64
- [GitHub #22703](https://github.com/zephyrproject-rtos/zephyr/issues/22703) - Implement ADC driver for lpcxpresso55s69
- [GitHub #22411](https://github.com/zephyrproject-rtos/zephyr/issues/22411) - AArch64 / Cortex-A port improvements / TODO
- [GitHub #22333](https://github.com/zephyrproject-rtos/zephyr/issues/22333) - drivers: can: Check bus-timing values at compile-time
- [GitHub #22247](https://github.com/zephyrproject-rtos/zephyr/issues/22247) - Discussion: Supporting the Arduino ecosystem
- [GitHub #22198](https://github.com/zephyrproject-rtos/zephyr/issues/22198) - BMA280 Sample Code
- [GitHub #22185](https://github.com/zephyrproject-rtos/zephyr/issues/22185) - Add Thread Local Storage (TLS) support
- [GitHub #22060](https://github.com/zephyrproject-rtos/zephyr/issues/22060) - Build fails with gcc-arm-none-eabi-9-2019-q4-major
- [GitHub #21991](https://github.com/zephyrproject-rtos/zephyr/issues/21991) - memory domain locking may not be entirely correct
- [GitHub #21495](https://github.com/zephyrproject-rtos/zephyr/issues/21495) - x86\_64: interrupt stack overflows are not caught
- [GitHub #21462](https://github.com/zephyrproject-rtos/zephyr/issues/21462) - x86\_64 exceptions are not safely preemptible, and stack overflows are not caught
- [GitHub #21273](https://github.com/zephyrproject-rtos/zephyr/issues/21273) - devicetree: improved support for enum values
- [GitHub #21238](https://github.com/zephyrproject-rtos/zephyr/issues/21238) - Improve Zephyr HCI VS extension detection
- [GitHub #21216](https://github.com/zephyrproject-rtos/zephyr/issues/21216) - Ztest “1cpu” cases don’t retarget interrupts on x86\_64
- [GitHub #21179](https://github.com/zephyrproject-rtos/zephyr/issues/21179) - Reduce RAM consumption for civetweb HTTP sample
- [GitHub #20980](https://github.com/zephyrproject-rtos/zephyr/issues/20980) - ESP32 flash error with segment count error using esptool.py from esp-idf
- [GitHub #20925](https://github.com/zephyrproject-rtos/zephyr/issues/20925) - tests/kernel/fp\_sharing/float\_disable crashes on qemu\_x86 with CONFIG\_KPTI=n
- [GitHub #20821](https://github.com/zephyrproject-rtos/zephyr/issues/20821) - Do USE\_(DT\_)CODE\_PARTITION and FLASH\_LOAD\_OFFSET/SIZE need to be user-configurable?
- [GitHub #20792](https://github.com/zephyrproject-rtos/zephyr/issues/20792) - sys\_pm: fragility in residency policy
- [GitHub #20775](https://github.com/zephyrproject-rtos/zephyr/issues/20775) - sys\_pm\_ctrl: fragility in managing state control
- [GitHub #20686](https://github.com/zephyrproject-rtos/zephyr/issues/20686) - tests/kernel/fp\_sharing/float\_disable failed when code coverage is enabled on qemu\_x86.
- [GitHub #20518](https://github.com/zephyrproject-rtos/zephyr/issues/20518) - [Coverity CID :205647]Memory - illegal accesses in /tests/arch/x86/info/src/memmap.c
- [GitHub #20337](https://github.com/zephyrproject-rtos/zephyr/issues/20337) - sifive\_gpio: gpio\_basic\_api test fails
- [GitHub #20262](https://github.com/zephyrproject-rtos/zephyr/issues/20262) - dt-binding for timers
- [GitHub #20118](https://github.com/zephyrproject-rtos/zephyr/issues/20118) - Zephyr BLE stack to work on the CC2650 Launchpad
- [GitHub #19850](https://github.com/zephyrproject-rtos/zephyr/issues/19850) - Bluetooth: Mesh: Modular settings handling
- [GitHub #19530](https://github.com/zephyrproject-rtos/zephyr/issues/19530) - Enhance sanitycheck/CI for separating build phase from testing
- [GitHub #19523](https://github.com/zephyrproject-rtos/zephyr/issues/19523) - Can’t build fade-led example for any Nordic board
- [GitHub #19511](https://github.com/zephyrproject-rtos/zephyr/issues/19511) - net: TCP: echo server blocks after a packet with zero TCP options
- [GitHub #19497](https://github.com/zephyrproject-rtos/zephyr/issues/19497) - log subsystem APIs need to be clearly namespaced as public or private
- [GitHub #19467](https://github.com/zephyrproject-rtos/zephyr/issues/19467) - Error building samples with PWM
- [GitHub #19448](https://github.com/zephyrproject-rtos/zephyr/issues/19448) - devicetree: support disabled devices
- [GitHub #19435](https://github.com/zephyrproject-rtos/zephyr/issues/19435) - how to change uart tx rx pins in zephyr
- [GitHub #19380](https://github.com/zephyrproject-rtos/zephyr/issues/19380) - Potential bugs re. ‘static inline’ and static variables
- [GitHub #19244](https://github.com/zephyrproject-rtos/zephyr/issues/19244) - BLE throughput of DFU by Mcumgr is too slow
- [GitHub #19138](https://github.com/zephyrproject-rtos/zephyr/issues/19138) - zassert prints to UART even when RTT is selected
- [GitHub #19100](https://github.com/zephyrproject-rtos/zephyr/issues/19100) - LwM2M sample with DTLS: does not connect
- [GitHub #19003](https://github.com/zephyrproject-rtos/zephyr/issues/19003) - bluetooth : Mesh: adv thread can be replace by other methods.
- [GitHub #18927](https://github.com/zephyrproject-rtos/zephyr/issues/18927) - settings: deprecate base64 encoding
- [GitHub #18778](https://github.com/zephyrproject-rtos/zephyr/issues/18778) - soc: arm: nordic\_nrf: Defining DT\_…\_DEV\_NAME
- [GitHub #18728](https://github.com/zephyrproject-rtos/zephyr/issues/18728) - sam\_e70\_xplained:tests/subsys/logging/log\_core failed.
- [GitHub #18608](https://github.com/zephyrproject-rtos/zephyr/issues/18608) - PCA9685 PWM driver is broken
- [GitHub #18607](https://github.com/zephyrproject-rtos/zephyr/issues/18607) - DesignWare PWM driver is broken
- [GitHub #18601](https://github.com/zephyrproject-rtos/zephyr/issues/18601) - LwM2M client sample: an overlay for OpenThread support
- [GitHub #18551](https://github.com/zephyrproject-rtos/zephyr/issues/18551) - address-of-temporary idiom not allowed in C++
- [GitHub #18529](https://github.com/zephyrproject-rtos/zephyr/issues/18529) - fs/fcb: consider backport of mynewt fixes
- [GitHub #18276](https://github.com/zephyrproject-rtos/zephyr/issues/18276) - irq\_connect\_dynamic() is not tested on all arches
- [GitHub #17893](https://github.com/zephyrproject-rtos/zephyr/issues/17893) - dynamic threads don’t work on x86 in some configurations
- [GitHub #17787](https://github.com/zephyrproject-rtos/zephyr/issues/17787) - openocd unable to flash hello\_world to cc26x2r1\_launchxl
- [GitHub #17743](https://github.com/zephyrproject-rtos/zephyr/issues/17743) - cross compiling for RISCV32 fails as compiler flags are not supplied by board but must be in target.cmake
- [GitHub #17645](https://github.com/zephyrproject-rtos/zephyr/issues/17645) - VSCode debugging Zephyr application
- [GitHub #17545](https://github.com/zephyrproject-rtos/zephyr/issues/17545) - Licensing and reference to public domain material
- [GitHub #17300](https://github.com/zephyrproject-rtos/zephyr/issues/17300) - [Zephyr v1.14.0] mcumgr: stm32: Strange Build warnings when counter is enabled
- [GitHub #17023](https://github.com/zephyrproject-rtos/zephyr/issues/17023) - userspace: thread indexes are not released when dynamic threads lose all references
- [GitHub #17014](https://github.com/zephyrproject-rtos/zephyr/issues/17014) - reentrancy protection in counter drivers?
- [GitHub #16766](https://github.com/zephyrproject-rtos/zephyr/issues/16766) - net: net\_pkt\_copy don’t work as expected when data was pulled from destination
- [GitHub #16544](https://github.com/zephyrproject-rtos/zephyr/issues/16544) - drivers: spi: spi\_mcux\_lpspi: inconsistent chip select behaviour
- [GitHub #16438](https://github.com/zephyrproject-rtos/zephyr/issues/16438) - fs/FCB fs/NVS : requires unaligned flash read-out length capabilities,
- [GitHub #16237](https://github.com/zephyrproject-rtos/zephyr/issues/16237) - disco\_l475\_iot1: samples/bluetooth/ipsp ko since 3151d26
- [GitHub #16195](https://github.com/zephyrproject-rtos/zephyr/issues/16195) - k\_uptime\_delta(): Defective by design
- [GitHub #15944](https://github.com/zephyrproject-rtos/zephyr/issues/15944) - stm32: New Driver for FMC/FSMC
- [GitHub #15713](https://github.com/zephyrproject-rtos/zephyr/issues/15713) - MCUMGR\_LOG build error
- [GitHub #15570](https://github.com/zephyrproject-rtos/zephyr/issues/15570) - Unbonded peripheral gets ‘Tx Buffer Overflow’ when erasing bond on master
- [GitHub #15372](https://github.com/zephyrproject-rtos/zephyr/issues/15372) - logging can’t dump exceptions without losing data with CONFIG\_LOG\_PRINTK
- [GitHub #14591](https://github.com/zephyrproject-rtos/zephyr/issues/14591) - Infineon Tricore architecture support
- [GitHub #14571](https://github.com/zephyrproject-rtos/zephyr/issues/14571) - TCP: sending lots of data deadlocks with slow peer
- [GitHub #14300](https://github.com/zephyrproject-rtos/zephyr/issues/14300) - Bluetooth connection using central and peripheral samples in nrf52840
- [GitHub #13955](https://github.com/zephyrproject-rtos/zephyr/issues/13955) - stm32: Implement async uart api
- [GitHub #13591](https://github.com/zephyrproject-rtos/zephyr/issues/13591) - tests/blutooth/tester: ASSERTION FAIL due to Recursive spinlock when running bt tester on qemu-cortex-m3
- [GitHub #13396](https://github.com/zephyrproject-rtos/zephyr/issues/13396) - Cannot connect to Galaxy S8 via BLE
- [GitHub #13244](https://github.com/zephyrproject-rtos/zephyr/issues/13244) - How to encrypt advertise packet with zephyr and nrf52832 ？
- [GitHub #12368](https://github.com/zephyrproject-rtos/zephyr/issues/12368) - File descriptors: Compile fails with non-POSIX out-of-tree libc
- [GitHub #12353](https://github.com/zephyrproject-rtos/zephyr/issues/12353) - intel\_s1000: SPI Flash Erase command doesn’t work when booting from flash
- [GitHub #12239](https://github.com/zephyrproject-rtos/zephyr/issues/12239) - BLE400 / nRF51822 (nRF51) PWM clock too low (servo-motor example)
- [GitHub #12150](https://github.com/zephyrproject-rtos/zephyr/issues/12150) - Power management on nRF52 boards
- [GitHub #11912](https://github.com/zephyrproject-rtos/zephyr/issues/11912) - net: SimpleLink: Create real cross-platform port
- [GitHub #11770](https://github.com/zephyrproject-rtos/zephyr/issues/11770) - Multiprotocol feature for BLE/Thread
- [GitHub #10904](https://github.com/zephyrproject-rtos/zephyr/issues/10904) - Requirements for driver devices generation using device tree
- [GitHub #10857](https://github.com/zephyrproject-rtos/zephyr/issues/10857) - Migrating from CMSIS-Core to DeviceTree results in loss of type information
- [GitHub #10460](https://github.com/zephyrproject-rtos/zephyr/issues/10460) - Bluetooth: settings: No space to store CCC config after successful pairing
- [GitHub #10158](https://github.com/zephyrproject-rtos/zephyr/issues/10158) - Have support for probot with Zephyr
- [GitHub #10022](https://github.com/zephyrproject-rtos/zephyr/issues/10022) - Porting Modbus Library: Need some guidance
- [GitHub #9944](https://github.com/zephyrproject-rtos/zephyr/issues/9944) - sockets: Connect doesn’t send new SYN in case the first connection attempt fails
- [GitHub #9883](https://github.com/zephyrproject-rtos/zephyr/issues/9883) - DTS processing generates unit\_address\_vs\_reg warning on entries with ‘reg’
- [GitHub #9875](https://github.com/zephyrproject-rtos/zephyr/issues/9875) - Bluetooth: Host LE Extended Advertising
- [GitHub #9783](https://github.com/zephyrproject-rtos/zephyr/issues/9783) - LwM2M: Cannot create object instance without specifying instance number
- [GitHub #9509](https://github.com/zephyrproject-rtos/zephyr/issues/9509) - Unable to upload firmware over serial with mcumgr
- [GitHub #9406](https://github.com/zephyrproject-rtos/zephyr/issues/9406) - Generate DTS ‘compatible’ based compilation flags
- [GitHub #9403](https://github.com/zephyrproject-rtos/zephyr/issues/9403) - is Support C++ standard library?
- [GitHub #9087](https://github.com/zephyrproject-rtos/zephyr/issues/9087) - driver: CAN interface should be compatible with CAN-FD interface
- [GitHub #8499](https://github.com/zephyrproject-rtos/zephyr/issues/8499) - Device Tree support overhaul
- [GitHub #8393](https://github.com/zephyrproject-rtos/zephyr/issues/8393) - `CONFIG_MULTITHREADING=n` builds call `main()` with interrupts locked
- [GitHub #8008](https://github.com/zephyrproject-rtos/zephyr/issues/8008) - net: Sockets (and likely net\_context’s) should not be closed behind application’s back
- [GitHub #7939](https://github.com/zephyrproject-rtos/zephyr/issues/7939) - Connections to TI CC254x break after conn\_update
- [GitHub #7404](https://github.com/zephyrproject-rtos/zephyr/issues/7404) - arch: arm: MSP initialization during early boot
- [GitHub #7331](https://github.com/zephyrproject-rtos/zephyr/issues/7331) - Precise time sync through BLE mesh.
- [GitHub #6857](https://github.com/zephyrproject-rtos/zephyr/issues/6857) - need to improve filtering and coverage in sanitycheck
- [GitHub #6818](https://github.com/zephyrproject-rtos/zephyr/issues/6818) - Question: Is Lightweight OpenMP implementation supported in Zephyr? Or any plan?
- [GitHub #6648](https://github.com/zephyrproject-rtos/zephyr/issues/6648) - Trusted Execution Framework: practical use-cases (high-level overview)
- [GitHub #6199](https://github.com/zephyrproject-rtos/zephyr/issues/6199) - STM32: document dts porting rules
- [GitHub #6040](https://github.com/zephyrproject-rtos/zephyr/issues/6040) - Implement flash driver for LPC54114
- [GitHub #5626](https://github.com/zephyrproject-rtos/zephyr/issues/5626) - Building samples failed
- [GitHub #4420](https://github.com/zephyrproject-rtos/zephyr/issues/4420) - net: tcp: RST handling is weak
- [GitHub #3675](https://github.com/zephyrproject-rtos/zephyr/issues/3675) - LE Adv. Ext.: Extended Scan with PHY selection for non-conn non-scan un-directed without aux packets
- [GitHub #3674](https://github.com/zephyrproject-rtos/zephyr/issues/3674) - LE Adv. Ext.: Non-Connectable and Non-Scannable Undirected without auxiliary packet
- [GitHub #3893](https://github.com/zephyrproject-rtos/zephyr/issues/3893) - Enhance k\_stack\_push() to check k\_stack->top to avoid corruption
- [GitHub #3719](https://github.com/zephyrproject-rtos/zephyr/issues/3719) - Multiple consoles support.
- [GitHub #3441](https://github.com/zephyrproject-rtos/zephyr/issues/3441) - IP stack: No TCP send window handling
- [GitHub #3102](https://github.com/zephyrproject-rtos/zephyr/issues/3102) - Make newlib libc the default c library
- [GitHub #2247](https://github.com/zephyrproject-rtos/zephyr/issues/2247) - LE Controller: Change hal/ into a set of drivers
