---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-1.9.html
original_path: releases/release-notes-1.9.html
---

# Zephyr Kernel 1.9.2

This is a maintenance release with fixes.

## Kernel

- Generic queue item acquisition fixed to always return a valid item when
  using K\_FOREVER

## Bluetooth

- Multiple stability fixes for BLE Mesh
- Multiple stability fixes for the BLE Controller

# Zephyr Kernel 1.9.1

This is a maintenance release with fixes and a two new features in the
BLE Controller.

## Drivers and Sensors

- mcux ethernet driver buffer overflow fixed
- STM32 PWM prescaler issue fixed

## Networking

- Support for IPv6 in DNS fixed

## Bluetooth

- Multiple stability fixes for the BLE Controller
- Support for PA/LNA amplifiers in the BLE Controller
- Support for additional VS commands in the BLE Controller

# Zephyr Kernel 1.9.0

We are pleased to announce the release of Zephyr kernel version 1.9.0

Major enhancements planned with this release include:

- Bluetooth 5.0 Support (all features except Advertising Extensions)
- Bluetooth Qualification-ready BLE Controller
- BLE Mesh
- Lightweight Machine to Machine (LwM2M) support
- Pthreads compatible API
- BSD Sockets compatible API
- MMU/MPU (Cont.): Thread Isolation, Paging
- Expand Device Tree support to more architectures
- Revamp Testsuite, Increase Coverage
- Stack Sentinel support (See details below)

The following sections provide detailed lists of changes by component.

## Kernel

- Added POSIX thread IPC support for Kernel
- kernel: introduce opaque data type for stacks
- Timeslicing and tickless kernel improvements

## Architectures

- arm: Added STM32F405, STM32F417, STM32F103x8 SoCs
- arm: Added TI CC2650 SoC
- arm: Removed TI CC3200 SoC
- arm: Added MPU support to nRF52, STM32L4, and STM32F3
- xtensa: Added ESP32 support
- Stack sentinel: This places a sentinel value at the lowest 4 bytes of a stack
  memory region and checks it at various intervals, including when servicing
  interrupts or context switching.
- x86: Enable MMU for application memory
- ARC: Added initial MPU support, including stack sentinel checking for ARC
  configurations not featuring hardware stack bounds checking
- ARC: Nested interrupt support for normal, non-FIRQ interrupts

## Boards

- Added device tree support for Intel Quark based microcontroller boards
  such as Arduino\_101, tinytile, and Quark\_d2000\_crb.
- arm: Added Atmel SAM4S Xplained board
- arm: Added Olimex STM32-E407 and STM32-P405 boards
- arm: Added STM32F412 Nucleo and STM32F429I-DISC1 boards
- arm: Added TI SensorTag board
- arm: Removed TI CC3200 LaunchXL board
- arm: Added VBLUno51 and VBLUno52 boards
- xtensa: Added ESP32 board support
- ARC: Added support for EMSK EM7D v2.2 version (incl. MPU)
- ARC: Board configuration restructuring, peripheral configs moved from soc to
  board level

## Drivers and Sensors

- KW40Z IEEE 802.15.4 radio driver support added
- APDS9960 sensor driver added
- Added TICKLESS KERNEL support for nrf RTC Timer
- Added Kinetis adc and pwm drivers
- Removed deprecated PWM driver APIs
- Added ESP32 drivers for GPIO, pin mux, watchdog, random number generator,
  and UART
- sensor: Add BMM150 Geomagnetic sensor driver

## Networking

- LWM2M support added
- net-app API support added. This is higher level API that can be used
  by applications to create client/server applications with transparent
  TLS (for TCP) or DTLS (for UDP) support.
- MQTT TLS support added
- Add support to automatically setup IEEE 802.15.4 and Bluetooth IPSP networks
- TCP receive window support added
- Network sample application configuration file unification, where most of the
  similar configuration files were merged together
- Added Bluetooth support to HTTP(S) server sample application
- BSD Socket compatible API layer, allowing to write and/or port simple
  networking applications using a well-known, cross-platform API
- Networking API documentation fixes
- Network shell enhancements
- Trickle algorithm fixes
- Improvements to HTTP server and client libraries
- CoAP API fixes
- IPv6 fixes
- RPL fixes

## Bluetooth

- Bluetooth Mesh support (all mandatory features and most optional ones)
- GATT Service Changed Characteristic support
- IPSP net-app support: a simplified networking API reducing duplication
  of common tasks an application writer has to go through to connect
  to the network.
- BLE controller qualification-ready, with all required tests passing
- Controller-based privacy (including all optional features)
- Extended Scanner Filter Policies support in the controller
- Controller roles (Advertiser, Scanner, Master and Slave) separation in
  source code, conditionally includable
- Flash access cooperation with BLE radio activity
- Bluetooth Kconfig options have been renamed have the same (consistent)
  prefix as the Bluetooth APIs, namely BT\_\* instead of BLUETOOTH\_\*.
  Controller Kconfig options have been shortened to use CTLR instead of
  CONTROLLER.
- Removed deprecated NBLE support

## Build and Infrastructure

- change description

## Libraries

- mbedTLS updated to 2.6.0
- TinyCrypt updated to 0.2.7

## HALs

- Added support for stm32f417 SOC
- Added support for stm32f405 SOC
- pinmux: stm32: 96b\_carbon: Add support for SPI
- Added rcc node on stm32 socs
- Added pin config for USART1 on PB6/PB7 for stm32l4
- Removed TI cc3200 SOC and LaunchXL board support

## Documentation

- CONTRIBUTING.rst and Contribution Guide material added
- Configuration options doc reorganized for easier access
- Navigation sidebar issues fixed for supported boards section
- Fixed link targets hidden behind header
- Completed migration of wiki.zephyrproject.org content into docs and
  GitHub wiki. All links to old wiki updated.
- Broken link and spelling check scans through .rst, Kconfig (used for
  auto-generated configuration docs), and source code doxygen comments
  (used for API documentation).
- API documentation added for new interfaces and improved for existing
  ones.
- Documentation added for new boards supported with this release.
- Python packages needed for document generation added to new python
  pip requirements.txt

## Build System and Tools

- Convert post-processing host tools to python, this includes the following
  tools: gen\_offset\_header.py gen\_idt.py gen\_gdt.py gen\_mmu.py

## Tests and Samples

- Added test Case to stress test round robin scheduling in schedule\_api test.
- Added test case to stress test priority scheduling in scheduling\_api\_test.

## JIRA Related Items

- `ZEP-230` - Define I2S driver APIs
- `ZEP-601` - enable CONFIG\_DEBUG\_INFO
- `ZEP-702` - Integrate Nordic’s Phoenix Link Layer into Zephyr
- `ZEP-749` - TinyCrypt uses an old, unoptimized version of micro-ecc
- `ZEP-896` - nRF5x Series: Add support for power and clock peripheral
- `ZEP-1067` - Driver for BMM150
- `ZEP-1396` - Add ksdk adc shim driver
- `ZEP-1426` - CONFIG\_BOOT\_TIME\_MEASUREMENT on all targets?
- `ZEP-1552` - Provide apds9960 sensor driver
- `ZEP-1647` - Figure out new combo for breathe/doxygen/sphinx versions that are supported
- `ZEP-1744` - UPF 56 BLE Controller Issues
- `ZEP-1751` - Add template YAML file
- `ZEP-1819` - Add tickless kernel support in nrf\_rtc\_timer timer
- `ZEP-1843` - provide mechanism to filter test cases based on available hardware
- `ZEP-1892` - Fix issues with Fix Release
- `ZEP-1902` - Missing board documentation for arm/nucleo\_f334r8
- `ZEP-1911` - Missing board documentation for arm/stm3210c\_eval
- `ZEP-1917` - Missing board documentation for arm/stm32373c\_eval
- `ZEP-1918` - Fix connection parameter request procedure
- `ZEP-2018` - Remove deprecated PWM APIs
- `ZEP-2020` - tests/crypto/test\_ecc\_dsa intermittently fails on riscv32
- `ZEP-2025` - Add mcux pwm shim driver for k64
- `ZEP-2031` - ESP32 Architecture Configuration
- `ZEP-2032` - Espressif Open-source Toolchain Support
- `ZEP-2039` - Implement stm32cube LL based clock control driver
- `ZEP-2054` - Convert all helper script to use python3
- `ZEP-2062` - Convert gen\_offset\_header to a python script
- `ZEP-2063` - Convert gen\_idt to python
- `ZEP-2068` - Need Tasks to Be Tracked in QRC too
- `ZEP-2071` - samples: warning: (SPI\_CS\_GPIO && SPI\_SS\_CS\_GPIO && I2C\_NRF5) selects GPIO which has unmet direct dependencies
- `ZEP-2085` - Add CONTRIBUTING.rst to root folder w/contributing guidelines
- `ZEP-2089` - UART support for ESP32
- `ZEP-2115` - Common API for networked applications for setting up network
- `ZEP-2116` - Common API for networked apps to create client/server applications
- `ZEP-2141` - Coverity CID 169303 in tests/net/ipv6/src/main.c
- `ZEP-2150` - Move Arduino 101 to Device Tree
- `ZEP-2151` - Move Quark D2000 to device tree
- `ZEP-2156` - Build warnings [-Wformat] with LLVM/icx (tests/kernel/sprintf)
- `ZEP-2168` - Timers seem to be broken with TICKLESS\_KERNEL on nRF51 (Cortex M0)
- `ZEP-2171` - Move all board pinmux code from drivers/pinmux/stm32 to the corresponding board/soc locations
- `ZEP-2184` - Split data, bss, noinit sections into application and kernel areas
- `ZEP-2188` - x86: Implement simple stack memory protection
- `ZEP-2217` - schedule\_api test fails on ARM with tickless kernel enabled
- `ZEP-2218` - unexpected short timeslice when running schedule\_api with tickless kernel enabled
- `ZEP-2220` - Extend MPU to stm32 family
- `ZEP-2225` - Ability to unregister GATT services
- `ZEP-2226` - BSD Sockets API: Basic blocking API
- `ZEP-2227` - BSD Sockets API: Non-blocking API
- `ZEP-2229` - test\_time\_slicing\_preemptible fails on bbc\_microbit and other NRF boards
- `ZEP-2250` - sanitycheck not filtering defconfigs properly
- `ZEP-2258` - Coverity static scan issues seen
- `ZEP-2265` - stack declaration macros for ARM MPU
- `ZEP-2267` - Create Release Notes
- `ZEP-2270` - Convert mpu\_stack\_guard\_test from using k\_thread\_spawn to k\_thread\_create
- `ZEP-2274` - Build warnings [-Wpointer-sign] with LLVM/icx (tests/net/ipv6\_fragment)
- `ZEP-2278` - KW41-Z 802.15.4 driver hangs if full debug is disabled
- `ZEP-2279` - echo\_server TCP handler corrupt by SYN flood
- `ZEP-2280` - add test case for KBUILD\_ZEPHYR\_APP
- `ZEP-2285` - non-boards shows up in board list for docs
- `ZEP-2286` - Write a GPIO driver for ESP32
- `ZEP-2289` - [DoS] Memory leak from large TCP packets
- `ZEP-2296` - ESP32: watchdog driver
- `ZEP-2297` - ESP32: Pin mux driver
- `ZEP-2303` - Concurrent incoming TCP connections
- `ZEP-2305` - linker: implement MMU alignment constraints
- `ZEP-2306` - echo server hangs from IPv6 hop-by-hop option anomaly
- `ZEP-2308` - (New) Networking API details documentation is missing
- `ZEP-2310` - Improve configuration documentation index organization
- `ZEP-2314` - Testcase failure :tests/benchmarks/timing\_info/testcase.ini#test
- `ZEP-2316` - Testcase failure :tests/bluetooth/shell/testcase.ini#test\_br
- `ZEP-2318` - some kernel objects sections are misaligned
- `ZEP-2319` - tests/net/ieee802154/l2 uses semaphore before initialization
- `ZEP-2321` - [PTS] All TC’s of SM/GATT/GAP failed due to BTP\_TIMEOUT error.
- `ZEP-2326` - x86: API to validate user buffer
- `ZEP-2328` - gen\_mmu.py appears to generate incorrect tables in some situations
- `ZEP-2329` - bad memory access tests/net/route
- `ZEP-2330` - bad memory access tests/net/rpl
- `ZEP-2331` - bad memory access tests/net/ieee802154/l2
- `ZEP-2332` - bad memory access tests/net/ip-addr
- `ZEP-2334` - bluetooth shell build warning when CONFIG\_DEBUG=y
- `ZEP-2335` - Ensure the Licensing page is up-to-date for the release
- `ZEP-2340` - Disabling advertising gets stuck
- `ZEP-2341` - Build warnings:override: reassigning to symbol MAIN\_STACK\_SIZE with LLVM/icx (/tests/net/6lo)
- `ZEP-2343` - Coverity static scan issues seen
- `ZEP-2344` - Coverity static scan issues seen
- `ZEP-2345` - Coverity static scan issues seen
- `ZEP-2352` - network API docs don’t mention when callbacks are called from a different thread
- `ZEP-2354` - ESP32: Random number generator
- `ZEP-2355` - Coverity static scan issues seen
- `ZEP-2358` - samples:net:echo\_server: Failed to send UDP packets
- `ZEP-2359` - samples:net:coaps\_server: unable to bind with IPv6
- `ZEP-2360` - Initial implementation of Bluetooth Mesh
- `ZEP-2361` - Provide a POSIX compatibility Layer on top of native APIs
- `ZEP-2365` - samples/net/wpanusb/test\_15\_4 fail on nrf52840\_pca10056 and frdm\_kw41z
- `ZEP-2366` - implement \_\_kernel attribute
- `ZEP-2367` - NULL pointer read in udp, tcp, context net tests
- `ZEP-2368` - x86: QEMU: enable MMU at boot by default
- `ZEP-2370` - [test] Create a stress test to test preemptive scheduling on zephyr
- `ZEP-2371` - [test] Create a stress test to test round robin scheduling with equal priority tasks on zephyr
- `ZEP-2374` - Build warnings:override: reassigning to symbol NET\_IPV4 with LLVM/icx (/tests/net/dhcpv4)
- `ZEP-2375` - Build warnings [-Wpointer-sign] with LLVM/icx (tests/net/udp)
- `ZEP-2378` - sample/bluetooth/ipsp: When build the app ‘ROM’ overflowed
- `ZEP-2379` - samples/bluetooth: Bluetooth init failed (err -19)
- `ZEP-2380` - TCP is broken by Zephyr commit 3604c391e
- `ZEP-2382` - Convert test to use ztest framework
- `ZEP-2383` - Net-app API needs to support DTLS
- `ZEP-2384` - “Common” bluetooth sample code does not build out of tree
- `ZEP-2385` - Update TinyCrypt to 0.2.7
- `ZEP-2395` - Assert in http\_server example when run over bluetooth on nrf52840
- `ZEP-2397` - net\_if\_ipv6\_addr\_rm calls k\_delayed\_work\_cancel() on uninitialized k\_delayed\_work object
- `ZEP-2398` - network stack test cases are only tested on x86
- `ZEP-2403` - Enabling MMU for qemu\_x86 broke active connect support
- `ZEP-2407` - [Cortex m series ] Getting a crash on Cortex m3 series when more than 8 preemptive threads with equal priority are scheduled
- `ZEP-2408` - design mechanism for kernel object sharing policy
- `ZEP-2412` - Bluetooth tester app not working from commit c1e5cb
- `ZEP-2423` - samples/bluetooth/ipsp’s builtin TCP echo crashes on TCP closure
- `ZEP-2432` - ieee802154\_shell.c, net\_mgmt call leads to a BUS FAULT
- `ZEP-2433` - x86: do forensic analysis to determine stack overflow context in supervisor mode
- `ZEP-2436` - Unable to see console output in Quark\_D200\_CRB
- `ZEP-2437` - warnings when building applications for quark d2000
- `ZEP-2444` - [nrf] Scheduling test API is getting failed in case of nrf51/nrf52 platforms
- `ZEP-2445` - nrf52: CPU lock-up when using Bluetooth + Flash driver + CONFIG\_ASSERT
- `ZEP-2447` - ‘make debugserver’ fails for qemu\_x86\_iamcu
- `ZEP-2451` - Move Bluetooth IPSP support functions from samples/bluetooth to a separate library
- `ZEP-2452` - https server does not build for olimex\_stm32\_e407
- `ZEP-2457` - generated/offsets.h is being regenerated unnecessarily
- `ZEP-2459` - Sample application not working with Quark SE C1000
- `ZEP-2460` - tests/crypto/ecc\_dh fails on qemu\_nios2
- `ZEP-2464` - “allow IPv6 interface init to work with late IP assignment” patch broke non-late IPv6 assignment
- `ZEP-2465` - Static code scan (coverity) issues seen
- `ZEP-2467` - Static code scan (coverity) issues seen
- `ZEP-2468` - Static code scan (coverity) issues seen
- `ZEP-2469` - Static code scan (coverity) issues seen
- `ZEP-2474` - Static code scan (coverity) issues seen
- `ZEP-2480` - Build warnings [-Wpointer-sign] with LLVM/icx (samples/net/coaps\_server)
- `ZEP-2482` - Build warnings [-Wpointer-sign] with LLVM/icx (samples/net/telnet)
- `ZEP-2483` - samples:net:http\_client: Failed to get http requests in IPv6
- `ZEP-2484` - samples:net:http\_server: Failed to work in IPv6
- `ZEP-2485` - Build warnings [-Wpointer-sign] with LLVM/icx (samples/net/coaps\_client)
- `ZEP-2486` - Build warnings [-Wpointer-sign] with LLVM/icx (samples/net/mbedtls\_dtlsserver)
- `ZEP-2488` - Build warnings [-Wpointer-sign] and [-Warray-bounds] with LLVM/icx (samples/net/irc\_bot)
- `ZEP-2489` - bug in \_x86\_mmu\_buffer\_validate API
- `ZEP-2496` - Build failure on tests/benchmarks/object\_footprint
- `ZEP-2497` - [TIMER] k\_timer\_start should take 0 value for duration parameter
- `ZEP-2498` - [Display] Minimum Duration argument to k\_timer\_start should be non Zero positive value
- `ZEP-2508` - esp32 linkage doesn’t unify ELF sections correctly
- `ZEP-2510` - BT: CONFIG\_BT\_HCI\_TX\_STACK\_SIZE appears to be too low for BT\_SPI
- `ZEP-2514` - XCC sanitycheck build compile wrong targets
- `ZEP-2523` - Static code scan (Coverity) issue seen in file: /samples/net/zoap\_server/src/zoap-server.c
- `ZEP-2525` - Static code scan (Coverity) issue seen in file: /samples/net/zoap\_server/src/zoap-server.c
- `ZEP-2531` - Static code scan (Coverity) issue seen in file: /tests/net/lib/dns\_resolve/src/main.c
- `ZEP-2528` - Static code scan (Coverity) issue seen in file: /samples/net/nats/src/nats.c
- `ZEP-2534` - Static code scan (Coverity) issue seen in file: /tests/kernel/irq\_offload/src/irq\_offload.c
- `ZEP-2535` - Static code scan (Coverity) issue seen in file: /tests/net/lib/zoap/src/main.c
- `ZEP-2537` - Static code scan (Coverity) issue seen in file: /tests/crypto/ecc\_dh/src/ecc\_dh.c
- `ZEP-2538` - Static code scan (Coverity) issue seen in file: /arch/arm/soc/st\_stm32/stm32f1/soc\_gpio.c
- `ZEP-2539` - Static code scan (Coverity) issue seen in file: /tests/net/ieee802154/l2/src/ieee802154\_test.c
- `ZEP-2540` - Static code scan (Coverity) issue seen in file: /ext/lib/crypto/tinycrypt/source/ecc\_dh.c
- `ZEP-2541` - Static code scan (Coverity) issue seen in file: /subsys/bluetooth/host/mesh/cfg.c
- `ZEP-2549` - Static code scan (Coverity) issue seen in file: /samples/net/leds\_demo/src/leds-demo.c
- `ZEP-2552` - ESP32 uart poll\_out always return 0
- `ZEP-2553` - k\_queue\_poll not handling -EADDRINUSE (another thread already polling) properly
- `ZEP-2556` - ESP32 watchdog WDT\_MODE\_INTERRUPT\_RESET mode fails
- `ZEP-2557` - ESP32 : Some GPIO tests are getting failed (tests/drivers/gpio/gpio\_basic\_api)
- `ZEP-2558` - CONFIG\_BLUETOOTH\_\* Kconfig options silently ignored
- `ZEP-2560` - samples/net: the sample of zoap\_server fails to add multicast address
- `ZEP-2561` - samples/net: The HTTP client failed to send the POST request
- `ZEP-2568` - [PTS] All TC’s of L2CAP/SM/GATT/GAP failed due to BTP\_ERROR.
- `ZEP-2575` - error:[ ‘-O: command not found’] with LLVM/icx (samples/hello\_world)
- `ZEP-2576` - samples/net/sockets/echo, echo\_async : fails to send the TCP packets
- `ZEP-2581` - CC3220 executable binary format support
- `ZEP-2584` - Update mbedTLS to 2.6.0
- `ZEP-713` - Implement preemptible regular IRQs on ARC
