---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/release-notes-1.14.html
original_path: releases/release-notes-1.14.html
---

# Zephyr 1.14.3

This is an LTS maintenance release with fixes.

## Security Vulnerability Related

The following security vulnerabilities (CVEs) were addressed in this
release:

- CVE-2020-10066
- CVE-2020-10069
- CVE-2020-13601
- CVE-2020-13602

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Issues Fixed

These GitHub issues were addressed since the previous 1.14.0 tagged
release:

- [GitHub #18334](https://github.com/zephyrproject-rtos/zephyr/issues/18334) - DNS resolution is broken for some addresses in master/2.0-pre
- [GitHub #19917](https://github.com/zephyrproject-rtos/zephyr/issues/19917) - Bluetooth: Controller: Missing LL\_ENC\_RSP after HCI LTK Negative Reply
- [GitHub #21107](https://github.com/zephyrproject-rtos/zephyr/issues/21107) - LL\_ASSERT and ‘Imprecise data bus error’ in LL Controller
- [GitHub #21257](https://github.com/zephyrproject-rtos/zephyr/issues/21257) - tests/net/net\_pkt failed on mimxrt1050\_evk board.
- [GitHub #21299](https://github.com/zephyrproject-rtos/zephyr/issues/21299) - bluetooth: Controller does not release buffer on central side after peripheral reset
- [GitHub #21601](https://github.com/zephyrproject-rtos/zephyr/issues/21601) - ‘!radio\_is\_ready()’ failed
- [GitHub #21756](https://github.com/zephyrproject-rtos/zephyr/issues/21756) - tests/kernel/obj\_tracing failed on mec15xxevb\_assy6853 board.
- [GitHub #22968](https://github.com/zephyrproject-rtos/zephyr/issues/22968) - Bluetooth: controller: LEGACY: ASSERTION failure on invalid packet sequence
- [GitHub #23069](https://github.com/zephyrproject-rtos/zephyr/issues/23069) - Bluetooth: controller: Assert in data length update procedure
- [GitHub #23109](https://github.com/zephyrproject-rtos/zephyr/issues/23109) - LL.TS Test LL/CON/SLA/BV-129-C fails (split)
- [GitHub #23805](https://github.com/zephyrproject-rtos/zephyr/issues/23805) - Bluetooth: controller: Switching to non conn adv fails for Mesh LPN
- [GitHub #24601](https://github.com/zephyrproject-rtos/zephyr/issues/24601) - Bluetooth: Mesh: Config Client’s net\_key\_status pulls two key indexes, should pull one.
- [GitHub #25518](https://github.com/zephyrproject-rtos/zephyr/issues/25518) - settings\_fcb: Fix storing the data
- [GitHub #25519](https://github.com/zephyrproject-rtos/zephyr/issues/25519) - wrong debug function cause kinds of building error
- [GitHub #26080](https://github.com/zephyrproject-rtos/zephyr/issues/26080) - gPTP time sync fails if having more than one port
- [GitHub #28151](https://github.com/zephyrproject-rtos/zephyr/issues/28151) - gPTP should allow user setting of priority1 and priority2 fields used in BMCA
- [GitHub #28177](https://github.com/zephyrproject-rtos/zephyr/issues/28177) - gPTP gptp\_priority\_vector struct field ordering is wrong
- [GitHub #29386](https://github.com/zephyrproject-rtos/zephyr/issues/29386) - unexpected behavior when doing syscall with 7 or more arguments
- [GitHub #29858](https://github.com/zephyrproject-rtos/zephyr/issues/29858) - Bluetooth: Mesh: RPL cleared on LPN disconnect
- [GitHub #32430](https://github.com/zephyrproject-rtos/zephyr/issues/32430) - Bluetooth: thread crashes when configuring a non 0 Slave Latency
- [GitHub #32898](https://github.com/zephyrproject-rtos/zephyr/issues/32898) - Bluetooth: controller: Control PDU buffer leak into Data PDU buffer pool

# Zephyr 1.14.2

This is an LTS maintenance release with fixes.

## Security Vulnerability Related

The following security vulnerabilities (CVEs) were addressed in this
release:

- CVE-2020-10019
- CVE-2020-10021
- CVE-2020-10022
- CVE-2020-10023
- CVE-2020-10024
- CVE-2020-10027
- CVE-2020-10028

More detailed information can be found in:
[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](https://docs.zephyrproject.org/latest/security/vulnerabilities.html)

## Issues Fixed

These GitHub issues were addressed since the previous 1.14.0 tagged
release:

- [GitHub #11617](https://github.com/zephyrproject-rtos/zephyr/issues/11617) - net: ipv4: udp: broadcast delivery not supported
- [GitHub #11743](https://github.com/zephyrproject-rtos/zephyr/issues/11743) - logging: add user mode access
- [GitHub #14459](https://github.com/zephyrproject-rtos/zephyr/issues/14459) - usb: samples: mass: doesn’t build with FLASH overlay
- [GitHub #15119](https://github.com/zephyrproject-rtos/zephyr/issues/15119) - GPIO callback not disabled from an interrupt
- [GitHub #15339](https://github.com/zephyrproject-rtos/zephyr/issues/15339) - RISC-V: RV32M1: Load access fault when accessing GPIO port E
- [GitHub #15354](https://github.com/zephyrproject-rtos/zephyr/issues/15354) - counter: stm32: Issue with LSE clock source selection
- [GitHub #15373](https://github.com/zephyrproject-rtos/zephyr/issues/15373) - IPv4 link local packets are not sent with ARP ethernet type
- [GitHub #15443](https://github.com/zephyrproject-rtos/zephyr/issues/15443) - usb\_dc\_stm32: Missing semaphore initialization and missing pin remapping configuration
- [GitHub #15444](https://github.com/zephyrproject-rtos/zephyr/issues/15444) - Error initiating sdhc disk
- [GitHub #15497](https://github.com/zephyrproject-rtos/zephyr/issues/15497) - USB DFU: STM32: usb dfu mode doesn’t work
- [GitHub #15507](https://github.com/zephyrproject-rtos/zephyr/issues/15507) - NRF52840: usb composite MSC + HID (with CONFIG\_ENABLE\_HID\_INT\_OUT\_EP)
- [GitHub #15526](https://github.com/zephyrproject-rtos/zephyr/issues/15526) - Unhandled identity in bt\_conn\_create\_slave\_le
- [GitHub #15558](https://github.com/zephyrproject-rtos/zephyr/issues/15558) - support for power-of-two MPUs on non-XIP systems
- [GitHub #15601](https://github.com/zephyrproject-rtos/zephyr/issues/15601) - pwm: nRF default prescalar value is wrong
- [GitHub #15603](https://github.com/zephyrproject-rtos/zephyr/issues/15603) - Unable to use C++ Standard Library
- [GitHub #15605](https://github.com/zephyrproject-rtos/zephyr/issues/15605) - Unaligned memory access by ldrd
- [GitHub #15678](https://github.com/zephyrproject-rtos/zephyr/issues/15678) - Watchdog peripheral api docs aren’t generated correctly.
- [GitHub #15698](https://github.com/zephyrproject-rtos/zephyr/issues/15698) - bluetooth: bt\_conn: No proper ID handling
- [GitHub #15733](https://github.com/zephyrproject-rtos/zephyr/issues/15733) - Bluetooth: controller: Central Encryption setup overlaps Length Request procedure
- [GitHub #15794](https://github.com/zephyrproject-rtos/zephyr/issues/15794) - mps2\_an385 crashes if CONFIG\_INIT\_STACKS=y and CONFIG\_COVERAGE=y
- [GitHub #15817](https://github.com/zephyrproject-rtos/zephyr/issues/15817) - nrf52: HFXO is not turned off as expected
- [GitHub #15904](https://github.com/zephyrproject-rtos/zephyr/issues/15904) - concerns with use of CONFIG\_BT\_MESH\_RPL\_STORE\_TIMEOUT in examples
- [GitHub #15911](https://github.com/zephyrproject-rtos/zephyr/issues/15911) - Stack size is smaller than it should be
- [GitHub #15975](https://github.com/zephyrproject-rtos/zephyr/issues/15975) - Openthread - fault with dual network interfaces
- [GitHub #16001](https://github.com/zephyrproject-rtos/zephyr/issues/16001) - ARC iotdk supports MPU and fpu in hardware but not enabled in kconfig
- [GitHub #16002](https://github.com/zephyrproject-rtos/zephyr/issues/16002) - the spi base reg address in arc\_iot.dtsi has an error
- [GitHub #16010](https://github.com/zephyrproject-rtos/zephyr/issues/16010) - Coverage reporting fails on many tests
- [GitHub #16012](https://github.com/zephyrproject-rtos/zephyr/issues/16012) - Source IP address for DHCP renewal messages is unset
- [GitHub #16046](https://github.com/zephyrproject-rtos/zephyr/issues/16046) - modules are being processed too late.
- [GitHub #16080](https://github.com/zephyrproject-rtos/zephyr/issues/16080) - Zephyr UART shell crashes on start if main() is blocked
- [GitHub #16089](https://github.com/zephyrproject-rtos/zephyr/issues/16089) - Mcux Ethernet driver does not detect carrier anymore (it’s alway on)
- [GitHub #16090](https://github.com/zephyrproject-rtos/zephyr/issues/16090) - mpu align support for code relocation on non-XIP system
- [GitHub #16143](https://github.com/zephyrproject-rtos/zephyr/issues/16143) - posix: clock\_settime calculates the base time incorrectly
- [GitHub #16155](https://github.com/zephyrproject-rtos/zephyr/issues/16155) - drivers: can: wrong value used for filter mode set
- [GitHub #16257](https://github.com/zephyrproject-rtos/zephyr/issues/16257) - net: icmpv4: Zephyr sends echo reply with multicast source address
- [GitHub #16307](https://github.com/zephyrproject-rtos/zephyr/issues/16307) - cannot move location counter backwards error happen
- [GitHub #16323](https://github.com/zephyrproject-rtos/zephyr/issues/16323) - net: ipv6: tcp: unexpected reply to malformed HBH in TCP/IPv6 SYN
- [GitHub #16339](https://github.com/zephyrproject-rtos/zephyr/issues/16339) - openthread: off-by-one error when calculating ot\_flash\_offset for settings
- [GitHub #16354](https://github.com/zephyrproject-rtos/zephyr/issues/16354) - net: ipv6: Zephyr does not reply to fragmented packet
- [GitHub #16375](https://github.com/zephyrproject-rtos/zephyr/issues/16375) - net: ipv4: udp: Zephyr does not reply to a valid datagram with checksum zero
- [GitHub #16379](https://github.com/zephyrproject-rtos/zephyr/issues/16379) - net: ipv6: udp: Zephyr replies with illegal UDP checksum zero
- [GitHub #16411](https://github.com/zephyrproject-rtos/zephyr/issues/16411) - bad regex for west version check in host-tools.cmake
- [GitHub #16412](https://github.com/zephyrproject-rtos/zephyr/issues/16412) - on reel\_board the consumption increases because TX pin is floating
- [GitHub #16413](https://github.com/zephyrproject-rtos/zephyr/issues/16413) - Missing dependency in cmake
- [GitHub #16414](https://github.com/zephyrproject-rtos/zephyr/issues/16414) - Backport west build –pristine
- [GitHub #16415](https://github.com/zephyrproject-rtos/zephyr/issues/16415) - Build errors with C++
- [GitHub #16416](https://github.com/zephyrproject-rtos/zephyr/issues/16416) - sram size for RT1015 and RT1020 needs to be update.
- [GitHub #16417](https://github.com/zephyrproject-rtos/zephyr/issues/16417) - issues with can filter mode set
- [GitHub #16418](https://github.com/zephyrproject-rtos/zephyr/issues/16418) - drivers: watchdog: sam0: check if timeout is valid
- [GitHub #16419](https://github.com/zephyrproject-rtos/zephyr/issues/16419) - Bluetooth: XTAL feature regression
- [GitHub #16478](https://github.com/zephyrproject-rtos/zephyr/issues/16478) - Bluetooth: Improper bonded peers handling
- [GitHub #16570](https://github.com/zephyrproject-rtos/zephyr/issues/16570) - [Coverity CID :198877]Null pointer dereferences in /subsys/net/ip/net\_if.c
- [GitHub #16577](https://github.com/zephyrproject-rtos/zephyr/issues/16577) - [Coverity CID :198870]Error handling issues in /subsys/net/lib/lwm2m/lwm2m\_obj\_firmware\_pull.c
- [GitHub #16581](https://github.com/zephyrproject-rtos/zephyr/issues/16581) - [Coverity CID :198866]Null pointer dereferences in /subsys/net/lib/dns/llmnr\_responder.c
- [GitHub #16584](https://github.com/zephyrproject-rtos/zephyr/issues/16584) - [Coverity CID :198863]Error handling issues in /subsys/net/lib/sntp/sntp.c
- [GitHub #16600](https://github.com/zephyrproject-rtos/zephyr/issues/16600) - Bluetooth: Mesh: Proxy SAR timeout is not implemented
- [GitHub #16602](https://github.com/zephyrproject-rtos/zephyr/issues/16602) - Bluetooth: GATT Discovery: Descriptor Discovery by range Seg Fault
- [GitHub #16639](https://github.com/zephyrproject-rtos/zephyr/issues/16639) - eth: pinging frdm k64f eventually leads to unresponsive ethernet device
- [GitHub #16678](https://github.com/zephyrproject-rtos/zephyr/issues/16678) - LPN establishment of Friendship never completes if there is no response to the initial Friend Poll
- [GitHub #16711](https://github.com/zephyrproject-rtos/zephyr/issues/16711) - Settings reworked to const char processing
- [GitHub #16734](https://github.com/zephyrproject-rtos/zephyr/issues/16734) - Bluetooth: GATT: Writing 1 byte to a CCC access invalid memory
- [GitHub #16745](https://github.com/zephyrproject-rtos/zephyr/issues/16745) - PTHREAD\_MUTEX\_DEFINE(): don’t store into the \_k\_mutex section
- [GitHub #16746](https://github.com/zephyrproject-rtos/zephyr/issues/16746) - boards: nrf52840\_pca10059: Configure NFC pins as GPIOs by default
- [GitHub #16749](https://github.com/zephyrproject-rtos/zephyr/issues/16749) - IRQ\_CONNECT and irq\_enable calls in the SiFive UART driver is misconfigured
- [GitHub #16750](https://github.com/zephyrproject-rtos/zephyr/issues/16750) - counter: lack of interrupt when CC=0
- [GitHub #16760](https://github.com/zephyrproject-rtos/zephyr/issues/16760) - K\_THREAD\_STACK\_EXTERN() confuses gen\_kobject\_list.py
- [GitHub #16779](https://github.com/zephyrproject-rtos/zephyr/issues/16779) - [Zephyr v1.14] ARM: fix the start address of MPU guard in stack-fail checking (when building with no user mode)
- [GitHub #16799](https://github.com/zephyrproject-rtos/zephyr/issues/16799) - Bluetooth: L2CAP: Interpretation of SCID and DCID in Disconnect is wrong
- [GitHub #16861](https://github.com/zephyrproject-rtos/zephyr/issues/16861) - nRF52: UARTE: Data corruption right after resuming device
- [GitHub #16864](https://github.com/zephyrproject-rtos/zephyr/issues/16864) - Bluetooth: Mesh: Rx buffer exhaustion causes deadlock
- [GitHub #16893](https://github.com/zephyrproject-rtos/zephyr/issues/16893) - Bluetooth: Multiple local IDs, privacy problem
- [GitHub #16943](https://github.com/zephyrproject-rtos/zephyr/issues/16943) - Missing test coverage for lib/os/crc\*.c
- [GitHub #16944](https://github.com/zephyrproject-rtos/zephyr/issues/16944) - Insufficient test coverage for lib/os/json.c
- [GitHub #17031](https://github.com/zephyrproject-rtos/zephyr/issues/17031) - Compiler warnings in settings module in Zephyr 1.14
- [GitHub #17038](https://github.com/zephyrproject-rtos/zephyr/issues/17038) - code relocation generating different memory layout cause user mode not working
- [GitHub #17041](https://github.com/zephyrproject-rtos/zephyr/issues/17041) - [1.14] Bluetooth: Mesh: RPL handling is not in line with the spec
- [GitHub #17055](https://github.com/zephyrproject-rtos/zephyr/issues/17055) - net: Incorrect data length after the connection is established
- [GitHub #17057](https://github.com/zephyrproject-rtos/zephyr/issues/17057) - Bluetooth: Mesh: Implementation doesn’t conform to latest errata and 1.0.1 version
- [GitHub #17092](https://github.com/zephyrproject-rtos/zephyr/issues/17092) - Bluetooth: GAP/IDLE/NAMP/BV-01-C requires Read by UUID
- [GitHub #17170](https://github.com/zephyrproject-rtos/zephyr/issues/17170) - x86\_64 crash with spinning child thread
- [GitHub #17171](https://github.com/zephyrproject-rtos/zephyr/issues/17171) - Insufficient code coverage for lib/os/fdtable.c
- [GitHub #17177](https://github.com/zephyrproject-rtos/zephyr/issues/17177) - ARM: userspace/test\_bad\_syscall fails on ARMv8-M
- [GitHub #17190](https://github.com/zephyrproject-rtos/zephyr/issues/17190) - net-mgmt should pass info element size to callback
- [GitHub #17250](https://github.com/zephyrproject-rtos/zephyr/issues/17250) - After first GC operation the 1st sector had become scratch and the 2nd sector had became write sector.
- [GitHub #17251](https://github.com/zephyrproject-rtos/zephyr/issues/17251) - w25q: erase operations must be erase-size aligned
- [GitHub #17262](https://github.com/zephyrproject-rtos/zephyr/issues/17262) - insufficient code coverage for lib/os/base64.c
- [GitHub #17288](https://github.com/zephyrproject-rtos/zephyr/issues/17288) - Bluetooth: controller: Fix handling of L2CAP start frame with zero PDU length
- [GitHub #17294](https://github.com/zephyrproject-rtos/zephyr/issues/17294) - DB corruption when adding/removing service
- [GitHub #17337](https://github.com/zephyrproject-rtos/zephyr/issues/17337) - ArmV7-M mpu sub region alignment
- [GitHub #17338](https://github.com/zephyrproject-rtos/zephyr/issues/17338) - kernel objects address check in elf\_helper.py
- [GitHub #17368](https://github.com/zephyrproject-rtos/zephyr/issues/17368) - Time Slicing cause system sleep short time
- [GitHub #17399](https://github.com/zephyrproject-rtos/zephyr/issues/17399) - LwM2M: Can’t use an alternate mbedtls implementation
- [GitHub #17401](https://github.com/zephyrproject-rtos/zephyr/issues/17401) - LwM2M: requires that CONFIG\_NET\_IPV\* be enabled (can’t use 100% offloaded IP stack)
- [GitHub #17415](https://github.com/zephyrproject-rtos/zephyr/issues/17415) - Settings Module - settings\_line\_val\_read() returning -EINVAL instead of 0 for deleted setting entries
- [GitHub #17427](https://github.com/zephyrproject-rtos/zephyr/issues/17427) - net: IPv4/UDP datagram with zero src addr and TTL causes Zephyr to segfault
- [GitHub #17450](https://github.com/zephyrproject-rtos/zephyr/issues/17450) - net: IPv6/UDP datagram with unspecified addr and zero hop limit causes Zephyr to quit
- [GitHub #17463](https://github.com/zephyrproject-rtos/zephyr/issues/17463) - Bluetooth: API limits usage of MITM flags in Pairing Request
- [GitHub #17534](https://github.com/zephyrproject-rtos/zephyr/issues/17534) - Race condition in GATT API.
- [GitHub #17595](https://github.com/zephyrproject-rtos/zephyr/issues/17595) - two userspace tests fail if stack canaries are enabled in board configuration
- [GitHub #17600](https://github.com/zephyrproject-rtos/zephyr/issues/17600) - Enable Mesh Friend support in Bluetooth tester application
- [GitHub #17613](https://github.com/zephyrproject-rtos/zephyr/issues/17613) - POSIX arch: occasional failures of tests/kernel/sched/schedule\_api on CI
- [GitHub #17630](https://github.com/zephyrproject-rtos/zephyr/issues/17630) - efr32mg\_sltb004a tick clock error
- [GitHub #17723](https://github.com/zephyrproject-rtos/zephyr/issues/17723) - Advertiser never clears state flags
- [GitHub #17732](https://github.com/zephyrproject-rtos/zephyr/issues/17732) - cannot use bt\_conn\_security in connected callback
- [GitHub #17764](https://github.com/zephyrproject-rtos/zephyr/issues/17764) - Broken link to latest development version of docs
- [GitHub #17802](https://github.com/zephyrproject-rtos/zephyr/issues/17802) - [zephyr 1.14] Address type 0x02 is used by LE Create Connection in device privacy mode
- [GitHub #17820](https://github.com/zephyrproject-rtos/zephyr/issues/17820) - Mesh bug report In access.c
- [GitHub #17838](https://github.com/zephyrproject-rtos/zephyr/issues/17838) - state DEVICE\_PM\_LOW\_POWER\_STATE of Device Power Management
- [GitHub #17843](https://github.com/zephyrproject-rtos/zephyr/issues/17843) - Bluetooth: controller: v1.14.x release conformance test failures
- [GitHub #17857](https://github.com/zephyrproject-rtos/zephyr/issues/17857) - GATT: Incorrect byte order for GATT database hash
- [GitHub #17861](https://github.com/zephyrproject-rtos/zephyr/issues/17861) - Tester application lacks BTP Discover All Primary Services handler
- [GitHub #17880](https://github.com/zephyrproject-rtos/zephyr/issues/17880) - Unable to re-connect to privacy enabled peer when using stack generated Identity
- [GitHub #17944](https://github.com/zephyrproject-rtos/zephyr/issues/17944) - [zephyr 1.14] LE Enhanced Connection Complete indicates Resolved Public once connected to Public peer address
- [GitHub #17948](https://github.com/zephyrproject-rtos/zephyr/issues/17948) - Bluetooth: privacy: Reconnection issue
- [GitHub #17967](https://github.com/zephyrproject-rtos/zephyr/issues/17967) - drivers/pwm/pwm\_api test failed on frdm\_k64f board.
- [GitHub #17971](https://github.com/zephyrproject-rtos/zephyr/issues/17971) - [zephyr 1.14] Unable to register GATT service that was unregistered before
- [GitHub #17979](https://github.com/zephyrproject-rtos/zephyr/issues/17979) - Security level cannot be elevated after re-connection with privacy
- [GitHub #18021](https://github.com/zephyrproject-rtos/zephyr/issues/18021) - Socket vtable can access null pointer callback function
- [GitHub #18090](https://github.com/zephyrproject-rtos/zephyr/issues/18090) - [zephyr 1.14][MESH/NODE/FRND/FN/BV-08-C] Mesh Friend queues more messages than indicates it’s Friend Cache
- [GitHub #18178](https://github.com/zephyrproject-rtos/zephyr/issues/18178) - BLE Mesh When Provisioning Use Input OOB Method
- [GitHub #18183](https://github.com/zephyrproject-rtos/zephyr/issues/18183) - [zephyr 1.14][GATT/SR/GAS/BV-07-C] GATT Server does not inform change-unaware client about DB changes
- [GitHub #18297](https://github.com/zephyrproject-rtos/zephyr/issues/18297) - Bluetooth: SMP: Pairing issues
- [GitHub #18306](https://github.com/zephyrproject-rtos/zephyr/issues/18306) - Unable to reconnect paired devices with controller privacy disabled (host privacy enabled)
- [GitHub #18308](https://github.com/zephyrproject-rtos/zephyr/issues/18308) - net: TCP/IPv6 set of fragmented packets causes Zephyr to quit
- [GitHub #18394](https://github.com/zephyrproject-rtos/zephyr/issues/18394) - [Coverity CID :203464]Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #18462](https://github.com/zephyrproject-rtos/zephyr/issues/18462) - potential buffer overrun in logging infrastructure
- [GitHub #18580](https://github.com/zephyrproject-rtos/zephyr/issues/18580) - Bluetooth: Security fail on initial pairing
- [GitHub #18658](https://github.com/zephyrproject-rtos/zephyr/issues/18658) - Bluetooth BR/EDR encryption key negotiation vulnerability
- [GitHub #18739](https://github.com/zephyrproject-rtos/zephyr/issues/18739) - k\_uptime\_get\_32() does not behave as documented
- [GitHub #18935](https://github.com/zephyrproject-rtos/zephyr/issues/18935) - [Zephyr 1.14] drivers: flash: spi\_nor: Problematic write with page boundaries
- [GitHub #18961](https://github.com/zephyrproject-rtos/zephyr/issues/18961) - [Coverity CID :203912]Error handling issues in /samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #19015](https://github.com/zephyrproject-rtos/zephyr/issues/19015) - Bluetooth: Mesh: Node doesn’t respond to “All Proxies” address
- [GitHub #19038](https://github.com/zephyrproject-rtos/zephyr/issues/19038) - [zephyr branch 1.14 and master -stm32-netusb]:errors when i view RNDIS Device‘s properties on Windows 10
- [GitHub #19059](https://github.com/zephyrproject-rtos/zephyr/issues/19059) - i2c\_ll\_stm32\_v2: nack on write is not handled correctly
- [GitHub #19103](https://github.com/zephyrproject-rtos/zephyr/issues/19103) - zsock\_accept\_ctx blocks even when O\_NONBLOCK is specified
- [GitHub #19165](https://github.com/zephyrproject-rtos/zephyr/issues/19165) - zephyr\_file generates bad links on branches
- [GitHub #19263](https://github.com/zephyrproject-rtos/zephyr/issues/19263) - Bluetooth: Mesh: Friend Clear Procedure Timeout
- [GitHub #19515](https://github.com/zephyrproject-rtos/zephyr/issues/19515) - Bluetooth: Controller: assertion failed
- [GitHub #19612](https://github.com/zephyrproject-rtos/zephyr/issues/19612) - ICMPv6 packet is routed to wrong interface when peer is not found in neighbor cache
- [GitHub #19678](https://github.com/zephyrproject-rtos/zephyr/issues/19678) - Noticeable delay between processing multiple client connection requests (200ms+)
- [GitHub #19889](https://github.com/zephyrproject-rtos/zephyr/issues/19889) - Buffer leak in GATT for Write Without Response and Notifications
- [GitHub #19982](https://github.com/zephyrproject-rtos/zephyr/issues/19982) - Periodically wake up log process thread consume more power
- [GitHub #20042](https://github.com/zephyrproject-rtos/zephyr/issues/20042) - Telnet can connect only once
- [GitHub #20100](https://github.com/zephyrproject-rtos/zephyr/issues/20100) - Slave PTP clock time is updated with large value when Master PTP Clock time has changed
- [GitHub #20229](https://github.com/zephyrproject-rtos/zephyr/issues/20229) - cmake: add –divide to GNU assembler options for x86
- [GitHub #20299](https://github.com/zephyrproject-rtos/zephyr/issues/20299) - bluetooth: host: Connection not being unreferenced when using CCC match callback
- [GitHub #20313](https://github.com/zephyrproject-rtos/zephyr/issues/20313) - Zperf documentation points to wrong iPerf varsion
- [GitHub #20811](https://github.com/zephyrproject-rtos/zephyr/issues/20811) - spi driver
- [GitHub #20970](https://github.com/zephyrproject-rtos/zephyr/issues/20970) - Bluetooth: Mesh: seg\_tx\_reset in the transport layer
- [GitHub #21131](https://github.com/zephyrproject-rtos/zephyr/issues/21131) - Bluetooth: host: Subscriptions not removed upon unpair
- [GitHub #21306](https://github.com/zephyrproject-rtos/zephyr/issues/21306) - ARC: syscall register save/restore needs backport to 1.14
- [GitHub #21431](https://github.com/zephyrproject-rtos/zephyr/issues/21431) - missing async uart.h system calls
- [GitHub #21432](https://github.com/zephyrproject-rtos/zephyr/issues/21432) - watchdog subsystem has no system calls
- [GitHub #22275](https://github.com/zephyrproject-rtos/zephyr/issues/22275) - arm: cortex-R & M: CONFIG\_USERSPACE: intermittent Memory region write access failures
- [GitHub #22280](https://github.com/zephyrproject-rtos/zephyr/issues/22280) - incorrect linker routing
- [GitHub #23153](https://github.com/zephyrproject-rtos/zephyr/issues/23153) - Binding AF\_PACKET socket second time will fail with multiple network interfaces
- [GitHub #23339](https://github.com/zephyrproject-rtos/zephyr/issues/23339) - tests/kernel/sched/schedule\_api failed on mps2\_an385 with v1.14 branch.
- [GitHub #23346](https://github.com/zephyrproject-rtos/zephyr/issues/23346) - bl65x\_dvk boards do not reset after flashing

# Zephyr 1.14.1

This is an LTS maintenance release with fixes, as well as Bluetooth
qualification listings for the Bluetooth protocol stack included in Zephyr.

See [Zephyr Kernel 1.14.0](#zephyr-1-14-0) for the previous version release notes.

## Security Vulnerability Related

The following security vulnerability (CVE) was addressed in this
release:

- Fixes CVE-2019-9506: The Bluetooth BR/EDR specification up to and
  including version 5.1 permits sufficiently low encryption key length
  and does not prevent an attacker from influencing the key length
  negotiation. This allows practical brute-force attacks (aka “KNOB”)
  that can decrypt traffic and inject arbitrary ciphertext without the
  victim noticing.

## Bluetooth

- Qualification:

  - 1.14.x Host subsystem qualified with QDID 139258
  - 1.14.x Mesh subsystem qualified with QDID 139259
  - 1.14.x Controller component qualified on Nordic nRF52 with QDID 135679

## Issues Fixed

These GitHub issues were addressed since the previous 1.14.0 tagged
release:

- [GitHub #11617](https://github.com/zephyrproject-rtos/zephyr/issues/11617) - net: ipv4: udp: broadcast delivery not supported
- [GitHub #11743](https://github.com/zephyrproject-rtos/zephyr/issues/11743) - logging: add user mode access
- [GitHub #14459](https://github.com/zephyrproject-rtos/zephyr/issues/14459) - usb: samples: mass: doesn’t build with FLASH overlay
- [GitHub #15279](https://github.com/zephyrproject-rtos/zephyr/issues/15279) - mempool alignment might cause a memory block allocated twice
- [GitHub #15339](https://github.com/zephyrproject-rtos/zephyr/issues/15339) - RISC-V: RV32M1: Load access fault when accessing GPIO port E
- [GitHub #15354](https://github.com/zephyrproject-rtos/zephyr/issues/15354) - counter: stm32: Issue with LSE clock source selection
- [GitHub #15373](https://github.com/zephyrproject-rtos/zephyr/issues/15373) - IPv4 link local packets are not sent with ARP ethernet type
- [GitHub #15443](https://github.com/zephyrproject-rtos/zephyr/issues/15443) - usb\_dc\_stm32: Missing semaphore initialization and missing pin remapping configuration
- [GitHub #15444](https://github.com/zephyrproject-rtos/zephyr/issues/15444) - Error initiating sdhc disk
- [GitHub #15497](https://github.com/zephyrproject-rtos/zephyr/issues/15497) - USB DFU: STM32: usb dfu mode doesn’t work
- [GitHub #15507](https://github.com/zephyrproject-rtos/zephyr/issues/15507) - NRF52840: usb composite MSC + HID (with CONFIG\_ENABLE\_HID\_INT\_OUT\_EP)
- [GitHub #15526](https://github.com/zephyrproject-rtos/zephyr/issues/15526) - Unhandled identity in bt\_conn\_create\_slave\_le
- [GitHub #15558](https://github.com/zephyrproject-rtos/zephyr/issues/15558) - support for power-of-two MPUs on non-XIP systems
- [GitHub #15601](https://github.com/zephyrproject-rtos/zephyr/issues/15601) - pwm: nRF default prescalar value is wrong
- [GitHub #15603](https://github.com/zephyrproject-rtos/zephyr/issues/15603) - Unable to use C++ Standard Library
- [GitHub #15605](https://github.com/zephyrproject-rtos/zephyr/issues/15605) - Unaligned memory access by ldrd
- [GitHub #15606](https://github.com/zephyrproject-rtos/zephyr/issues/15606) - trickle.c can’t work for multiple triggerings
- [GitHub #15678](https://github.com/zephyrproject-rtos/zephyr/issues/15678) - Watchdog peripheral api docs aren’t generated correctly.
- [GitHub #15698](https://github.com/zephyrproject-rtos/zephyr/issues/15698) - bluetooth: bt\_conn: No proper ID handling
- [GitHub #15733](https://github.com/zephyrproject-rtos/zephyr/issues/15733) - Bluetooth: controller: Central Encryption setup overlaps Length Request procedure
- [GitHub #15794](https://github.com/zephyrproject-rtos/zephyr/issues/15794) - mps2\_an385 crashes if CONFIG\_INIT\_STACKS=y and CONFIG\_COVERAGE=y
- [GitHub #15817](https://github.com/zephyrproject-rtos/zephyr/issues/15817) - nrf52: HFXO is not turned off as expected
- [GitHub #15904](https://github.com/zephyrproject-rtos/zephyr/issues/15904) - concerns with use of CONFIG\_BT\_MESH\_RPL\_STORE\_TIMEOUT in examples
- [GitHub #15911](https://github.com/zephyrproject-rtos/zephyr/issues/15911) - Stack size is smaller than it should be
- [GitHub #15975](https://github.com/zephyrproject-rtos/zephyr/issues/15975) - Openthread - fault with dual network interfaces
- [GitHub #16001](https://github.com/zephyrproject-rtos/zephyr/issues/16001) - ARC iotdk supports MPU and fpu in hardware but not enabled in kconfig
- [GitHub #16002](https://github.com/zephyrproject-rtos/zephyr/issues/16002) - the spi base reg address in arc\_iot.dtsi has an error
- [GitHub #16010](https://github.com/zephyrproject-rtos/zephyr/issues/16010) - Coverage reporting fails on many tests
- [GitHub #16012](https://github.com/zephyrproject-rtos/zephyr/issues/16012) - Source IP address for DHCP renewal messages is unset
- [GitHub #16027](https://github.com/zephyrproject-rtos/zephyr/issues/16027) - support for no-flash systems
- [GitHub #16046](https://github.com/zephyrproject-rtos/zephyr/issues/16046) - modules are being processed too late.
- [GitHub #16090](https://github.com/zephyrproject-rtos/zephyr/issues/16090) - mpu align support for code relocation on non-XIP system
- [GitHub #16107](https://github.com/zephyrproject-rtos/zephyr/issues/16107) - Using bt\_gatt\_read() with ‘by\_uuid’ method returns 3 extra bytes
- [GitHub #16143](https://github.com/zephyrproject-rtos/zephyr/issues/16143) - posix: clock\_settime calculates the base time incorrectly
- [GitHub #16155](https://github.com/zephyrproject-rtos/zephyr/issues/16155) - drivers: can: wrong value used for filter mode set
- [GitHub #16257](https://github.com/zephyrproject-rtos/zephyr/issues/16257) - net: icmpv4: Zephyr sends echo reply with multicast source address
- [GitHub #16307](https://github.com/zephyrproject-rtos/zephyr/issues/16307) - cannot move location counter backwards error happen
- [GitHub #16323](https://github.com/zephyrproject-rtos/zephyr/issues/16323) - net: ipv6: tcp: unexpected reply to malformed HBH in TCP/IPv6 SYN
- [GitHub #16339](https://github.com/zephyrproject-rtos/zephyr/issues/16339) - openthread: off-by-one error when calculating ot\_flash\_offset for settings
- [GitHub #16354](https://github.com/zephyrproject-rtos/zephyr/issues/16354) - net: ipv6: Zephyr does not reply to fragmented packet
- [GitHub #16375](https://github.com/zephyrproject-rtos/zephyr/issues/16375) - net: ipv4: udp: Zephyr does not reply to a valid datagram with checksum zero
- [GitHub #16379](https://github.com/zephyrproject-rtos/zephyr/issues/16379) - net: ipv6: udp: Zephyr replies with illegal UDP checksum zero
- [GitHub #16411](https://github.com/zephyrproject-rtos/zephyr/issues/16411) - bad regex for west version check in host-tools.cmake
- [GitHub #16412](https://github.com/zephyrproject-rtos/zephyr/issues/16412) - on reel\_board the consumption increases because TX pin is floating
- [GitHub #16413](https://github.com/zephyrproject-rtos/zephyr/issues/16413) - Missing dependency in cmake
- [GitHub #16414](https://github.com/zephyrproject-rtos/zephyr/issues/16414) - Backport west build –pristine
- [GitHub #16415](https://github.com/zephyrproject-rtos/zephyr/issues/16415) - Build errors with C++
- [GitHub #16416](https://github.com/zephyrproject-rtos/zephyr/issues/16416) - sram size for RT1015 and RT1020 needs to be update.
- [GitHub #16417](https://github.com/zephyrproject-rtos/zephyr/issues/16417) - issues with can filter mode set
- [GitHub #16418](https://github.com/zephyrproject-rtos/zephyr/issues/16418) - drivers: watchdog: sam0: check if timeout is valid
- [GitHub #16419](https://github.com/zephyrproject-rtos/zephyr/issues/16419) - Bluetooth: XTAL feature regression
- [GitHub #16478](https://github.com/zephyrproject-rtos/zephyr/issues/16478) - Bluetooth: Improper bonded peers handling
- [GitHub #16570](https://github.com/zephyrproject-rtos/zephyr/issues/16570) - [Coverity CID :198877]Null pointer dereferences in /subsys/net/ip/net\_if.c
- [GitHub #16577](https://github.com/zephyrproject-rtos/zephyr/issues/16577) - [Coverity CID :198870]Error handling issues in /subsys/net/lib/lwm2m/lwm2m\_obj\_firmware\_pull.c
- [GitHub #16581](https://github.com/zephyrproject-rtos/zephyr/issues/16581) - [Coverity CID :198866]Null pointer dereferences in /subsys/net/lib/dns/llmnr\_responder.c
- [GitHub #16584](https://github.com/zephyrproject-rtos/zephyr/issues/16584) - [Coverity CID :198863]Error handling issues in /subsys/net/lib/sntp/sntp.c
- [GitHub #16594](https://github.com/zephyrproject-rtos/zephyr/issues/16594) - net: dns: Zephyr is unable to unpack mDNS answers produced by another Zephyr node
- [GitHub #16600](https://github.com/zephyrproject-rtos/zephyr/issues/16600) - Bluetooth: Mesh: Proxy SAR timeout is not implemented
- [GitHub #16602](https://github.com/zephyrproject-rtos/zephyr/issues/16602) - Bluetooth: GATT Discovery: Descriptor Discovery by range Seg Fault
- [GitHub #16639](https://github.com/zephyrproject-rtos/zephyr/issues/16639) - eth: pinging frdm k64f eventually leads to unresponsive ethernet device
- [GitHub #16678](https://github.com/zephyrproject-rtos/zephyr/issues/16678) - LPN establishment of Friendship never completes if there is no response to the initial Friend Poll
- [GitHub #16711](https://github.com/zephyrproject-rtos/zephyr/issues/16711) - Settings reworked to const char processing
- [GitHub #16734](https://github.com/zephyrproject-rtos/zephyr/issues/16734) - Bluetooth: GATT: Writing 1 byte to a CCC access invalid memory
- [GitHub #16745](https://github.com/zephyrproject-rtos/zephyr/issues/16745) - PTHREAD\_MUTEX\_DEFINE(): don’t store into the \_k\_mutex section
- [GitHub #16746](https://github.com/zephyrproject-rtos/zephyr/issues/16746) - boards: nrf52840\_pca10059: Configure NFC pins as GPIOs by default
- [GitHub #16749](https://github.com/zephyrproject-rtos/zephyr/issues/16749) - IRQ\_CONNECT and irq\_enable calls in the SiFive UART driver is misconfigured
- [GitHub #16750](https://github.com/zephyrproject-rtos/zephyr/issues/16750) - counter: lack of interrupt when CC=0
- [GitHub #16760](https://github.com/zephyrproject-rtos/zephyr/issues/16760) - K\_THREAD\_STACK\_EXTERN() confuses gen\_kobject\_list.py
- [GitHub #16779](https://github.com/zephyrproject-rtos/zephyr/issues/16779) - [Zephyr v1.14] ARM: fix the start address of MPU guard in stack-fail checking (when building with no user mode)
- [GitHub #16799](https://github.com/zephyrproject-rtos/zephyr/issues/16799) - Bluetooth: L2CAP: Interpretation of SCID and DCID in Disconnect is wrong
- [GitHub #16864](https://github.com/zephyrproject-rtos/zephyr/issues/16864) - Bluetooth: Mesh: Rx buffer exhaustion causes deadlock
- [GitHub #16893](https://github.com/zephyrproject-rtos/zephyr/issues/16893) - Bluetooth: Multiple local IDs, privacy problem
- [GitHub #16943](https://github.com/zephyrproject-rtos/zephyr/issues/16943) - Missing test coverage for lib/os/crc\*.c
- [GitHub #16944](https://github.com/zephyrproject-rtos/zephyr/issues/16944) - Insufficient test coverage for lib/os/json.c
- [GitHub #17031](https://github.com/zephyrproject-rtos/zephyr/issues/17031) - Compiler warnings in settings module in Zephyr 1.14
- [GitHub #17038](https://github.com/zephyrproject-rtos/zephyr/issues/17038) - code relocation generating different memory layout cause user mode not working
- [GitHub #17041](https://github.com/zephyrproject-rtos/zephyr/issues/17041) - [1.14] Bluetooth: Mesh: RPL handling is not in line with the spec
- [GitHub #17055](https://github.com/zephyrproject-rtos/zephyr/issues/17055) - net: Incorrect data length after the connection is established
- [GitHub #17057](https://github.com/zephyrproject-rtos/zephyr/issues/17057) - Bluetooth: Mesh: Implementation doesn’t conform to latest errata and 1.0.1 version
- [GitHub #17092](https://github.com/zephyrproject-rtos/zephyr/issues/17092) - Bluetooth: GAP/IDLE/NAMP/BV-01-C requires Read by UUID
- [GitHub #17170](https://github.com/zephyrproject-rtos/zephyr/issues/17170) - x86\_64 crash with spinning child thread
- [GitHub #17177](https://github.com/zephyrproject-rtos/zephyr/issues/17177) - ARM: userspace/test\_bad\_syscall fails on ARMv8-M
- [GitHub #17190](https://github.com/zephyrproject-rtos/zephyr/issues/17190) - net-mgmt should pass info element size to callback
- [GitHub #17250](https://github.com/zephyrproject-rtos/zephyr/issues/17250) - After first GC operation the 1st sector had become scratch and the 2nd sector had became write sector.
- [GitHub #17251](https://github.com/zephyrproject-rtos/zephyr/issues/17251) - w25q: erase operations must be erase-size aligned
- [GitHub #17262](https://github.com/zephyrproject-rtos/zephyr/issues/17262) - insufficient code coverage for lib/os/base64.c
- [GitHub #17288](https://github.com/zephyrproject-rtos/zephyr/issues/17288) - Bluetooth: controller: Fix handling of L2CAP start frame with zero PDU length
- [GitHub #17294](https://github.com/zephyrproject-rtos/zephyr/issues/17294) - DB corruption when adding/removing service
- [GitHub #17337](https://github.com/zephyrproject-rtos/zephyr/issues/17337) - ArmV7-M mpu sub region alignment
- [GitHub #17338](https://github.com/zephyrproject-rtos/zephyr/issues/17338) - kernel objects address check in elf\_helper.py
- [GitHub #17368](https://github.com/zephyrproject-rtos/zephyr/issues/17368) - Time Slicing cause system sleep short time
- [GitHub #17399](https://github.com/zephyrproject-rtos/zephyr/issues/17399) - LwM2M: Can’t use an alternate mbedtls implementation
- [GitHub #17401](https://github.com/zephyrproject-rtos/zephyr/issues/17401) - LwM2M: requires that CONFIG\_NET\_IPV\* be enabled (can’t use 100% offloaded IP stack)
- [GitHub #17415](https://github.com/zephyrproject-rtos/zephyr/issues/17415) - Settings Module - settings\_line\_val\_read() returning -EINVAL instead of 0 for deleted setting entries
- [GitHub #17427](https://github.com/zephyrproject-rtos/zephyr/issues/17427) - net: IPv4/UDP datagram with zero src addr and TTL causes Zephyr to segfault
- [GitHub #17450](https://github.com/zephyrproject-rtos/zephyr/issues/17450) - net: IPv6/UDP datagram with unspecified addr and zero hop limit causes Zephyr to quit
- [GitHub #17463](https://github.com/zephyrproject-rtos/zephyr/issues/17463) - Bluetooth: API limits usage of MITM flags in Pairing Request
- [GitHub #17534](https://github.com/zephyrproject-rtos/zephyr/issues/17534) - Race condition in GATT API.
- [GitHub #17564](https://github.com/zephyrproject-rtos/zephyr/issues/17564) - Missing stdlib.h include when C++ standard library is used.
- [GitHub #17595](https://github.com/zephyrproject-rtos/zephyr/issues/17595) - two userspace tests fail if stack canaries are enabled in board configuration
- [GitHub #17600](https://github.com/zephyrproject-rtos/zephyr/issues/17600) - Enable Mesh Friend support in Bluetooth tester application
- [GitHub #17613](https://github.com/zephyrproject-rtos/zephyr/issues/17613) - POSIX arch: occasional failures of tests/kernel/sched/schedule\_api on CI
- [GitHub #17723](https://github.com/zephyrproject-rtos/zephyr/issues/17723) - Advertiser never clears state flags
- [GitHub #17732](https://github.com/zephyrproject-rtos/zephyr/issues/17732) - cannot use bt\_conn\_security in connected callback
- [GitHub #17764](https://github.com/zephyrproject-rtos/zephyr/issues/17764) - Broken link to latest development version of docs
- [GitHub #17789](https://github.com/zephyrproject-rtos/zephyr/issues/17789) - Bluetooth: host: conn.c missing parameter copy
- [GitHub #17802](https://github.com/zephyrproject-rtos/zephyr/issues/17802) - [zephyr 1.14] Address type 0x02 is used by LE Create Connection in device privacy mode
- [GitHub #17809](https://github.com/zephyrproject-rtos/zephyr/issues/17809) - Bluetooth Mesh message cached too early when LPN
- [GitHub #17820](https://github.com/zephyrproject-rtos/zephyr/issues/17820) - Mesh bug report In access.c
- [GitHub #17821](https://github.com/zephyrproject-rtos/zephyr/issues/17821) - Mesh Bug on access.c
- [GitHub #17843](https://github.com/zephyrproject-rtos/zephyr/issues/17843) - Bluetooth: controller: v1.14.x release conformance test failures
- [GitHub #17857](https://github.com/zephyrproject-rtos/zephyr/issues/17857) - GATT: Incorrect byte order for GATT database hash
- [GitHub #17861](https://github.com/zephyrproject-rtos/zephyr/issues/17861) - Tester application lacks BTP Discover All Primary Services handler
- [GitHub #17880](https://github.com/zephyrproject-rtos/zephyr/issues/17880) - Unable to re-connect to privacy enabled peer when using stack generated Identity
- [GitHub #17882](https://github.com/zephyrproject-rtos/zephyr/issues/17882) - [zephyr 1.14] Database Out of Sync error is not returned as expected
- [GitHub #17907](https://github.com/zephyrproject-rtos/zephyr/issues/17907) - BLE Mesh when resend use GATT bearer
- [GitHub #17932](https://github.com/zephyrproject-rtos/zephyr/issues/17932) - BLE Mesh When Friend Send Seg Message To LPN
- [GitHub #17936](https://github.com/zephyrproject-rtos/zephyr/issues/17936) - Bluetooth: Mesh: The canceled buffer is not free, causing a memory leak
- [GitHub #17944](https://github.com/zephyrproject-rtos/zephyr/issues/17944) - [zephyr 1.14] LE Enhanced Connection Complete indicates Resolved Public once connected to Public peer address
- [GitHub #17948](https://github.com/zephyrproject-rtos/zephyr/issues/17948) - Bluetooth: privacy: Reconnection issue
- [GitHub #17971](https://github.com/zephyrproject-rtos/zephyr/issues/17971) - [zephyr 1.14] Unable to register GATT service that was unregistered before
- [GitHub #17977](https://github.com/zephyrproject-rtos/zephyr/issues/17977) - BLE Mesh When IV Update Procedure
- [GitHub #17979](https://github.com/zephyrproject-rtos/zephyr/issues/17979) - Security level cannot be elevated after re-connection with privacy
- [GitHub #18013](https://github.com/zephyrproject-rtos/zephyr/issues/18013) - BLE Mesh On Net Buffer free issue
- [GitHub #18021](https://github.com/zephyrproject-rtos/zephyr/issues/18021) - Socket vtable can access null pointer callback function
- [GitHub #18090](https://github.com/zephyrproject-rtos/zephyr/issues/18090) - [zephyr 1.14][MESH/NODE/FRND/FN/BV-08-C] Mesh Friend queues more messages than indicates it’s Friend Cache
- [GitHub #18150](https://github.com/zephyrproject-rtos/zephyr/issues/18150) - [zephyr 1.14] Host does not change the RPA
- [GitHub #18178](https://github.com/zephyrproject-rtos/zephyr/issues/18178) - BLE Mesh When Provisioning Use Input OOB Method
- [GitHub #18183](https://github.com/zephyrproject-rtos/zephyr/issues/18183) - [zephyr 1.14][GATT/SR/GAS/BV-07-C] GATT Server does not inform change-unaware client about DB changes
- [GitHub #18194](https://github.com/zephyrproject-rtos/zephyr/issues/18194) - [zephyr 1.14][MESH/NODE/CFG/HBP/BV-05-C] Zephyr does not send Heartbeat message on friendship termination
- [GitHub #18297](https://github.com/zephyrproject-rtos/zephyr/issues/18297) - Bluetooth: SMP: Pairing issues
- [GitHub #18306](https://github.com/zephyrproject-rtos/zephyr/issues/18306) - Unable to reconnect paired devices with controller privacy disabled (host privacy enabled)
- [GitHub #18308](https://github.com/zephyrproject-rtos/zephyr/issues/18308) - net: TCP/IPv6 set of fragmented packets causes Zephyr to quit
- [GitHub #18394](https://github.com/zephyrproject-rtos/zephyr/issues/18394) - [Coverity CID :203464]Memory - corruptions in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #18462](https://github.com/zephyrproject-rtos/zephyr/issues/18462) - potential buffer overrun in logging infrastructure
- [GitHub #18522](https://github.com/zephyrproject-rtos/zephyr/issues/18522) - BLE: Mesh: When transport send seg\_msg to LPN
- [GitHub #18580](https://github.com/zephyrproject-rtos/zephyr/issues/18580) - Bluetooth: Security fail on initial pairing
- [GitHub #18658](https://github.com/zephyrproject-rtos/zephyr/issues/18658) - Bluetooth BR/EDR encryption key negotiation vulnerability
- [GitHub #18739](https://github.com/zephyrproject-rtos/zephyr/issues/18739) - k\_uptime\_get\_32() does not behave as documented
- [GitHub #18813](https://github.com/zephyrproject-rtos/zephyr/issues/18813) - fs: nvs: Cannot delete entries
- [GitHub #18873](https://github.com/zephyrproject-rtos/zephyr/issues/18873) - zsock\_socket() should support proto==0
- [GitHub #18935](https://github.com/zephyrproject-rtos/zephyr/issues/18935) - [Zephyr 1.14] drivers: flash: spi\_nor: Problematic write with page boundaries
- [GitHub #18961](https://github.com/zephyrproject-rtos/zephyr/issues/18961) - [Coverity CID :203912]Error handling issues in /samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #19015](https://github.com/zephyrproject-rtos/zephyr/issues/19015) - Bluetooth: Mesh: Node doesn’t respond to “All Proxies” address
- [GitHub #19165](https://github.com/zephyrproject-rtos/zephyr/issues/19165) - zephyr\_file generates bad links on branches
- [GitHub #19181](https://github.com/zephyrproject-rtos/zephyr/issues/19181) - sock\_set\_flag implementation in sock\_internal.h does not work for 64 bit pointers
- [GitHub #19191](https://github.com/zephyrproject-rtos/zephyr/issues/19191) - problem with implementation of sock\_set\_flag

# Zephyr Kernel 1.14.0

We are pleased to announce the release of Zephyr kernel version 1.14.0.

Major enhancements with this release include:

- The Zephyr project now supports over 160 different board configurations
  spanning 8 architectures. All architectures are rigorously tested and
  validated using one of the many simulation platforms supported by the
  project: QEMU, Renode, ARC Simulator, and the native POSIX configuration.
- The timing subsystem has been reworked and reimplemented, greatly
  simplifying the resulting drivers, removing thousands of lines
  of code, and reducing a typical kernel build size by hundreds of bytes.
  TICKLESS\_KERNEL mode is now the default on all architectures.
- The Symmetric Multi-Processing (SMP) subsystem continues to evolve
  with the addition of a new CPU affinity API that can “pin” threads to
  specific cores or sets of cores. The core kernel no longer uses the
  global irq\_lock on SMP systems, and exclusively uses the spinlock API
  (which on uniprocessor systems reduces to the same code).
- Zephyr now has support for the x86\_64 architecture. It is currently
  implemented only for QEMU targets, supports arbitrary numbers of CPUs,
  and runs in SMP mode by default, our first platform to do so.
- We’ve overhauled the Network packet ([net-pkt](../connectivity/networking/api/net_pkt.md#net-pkt-interface))
  API and moved the majority of components and protocols to use the
  [BSD socket API](../connectivity/networking/api/sockets.md#bsd-sockets-interface), including MQTT, CoAP,
  LWM2M, and SNTP.
- We enhanced the native POSIX port by adding UART, USB, and display
  drivers. Based on this port, we added a simulated NRF52832 SoC which enables
  running full system, multi-node simulations, without the need of real
  hardware.
- We added an experimental BLE split software Controller with Upper Link Layer
  and Lower Link Layer for supporting multiple BLE radio hardware
  architectures.
- The power management subsystem has been overhauled to support device idle
  power management and move most of the power management logic from the
  application back to the BSP.
- We introduced major updates and an overhaul to both the logging and
  shell subsystems, supporting multiple back-ends, integration
  of logging into the shell, and delayed log processing.
- Introduced the `west` tool for management of multiple repositories and
  enhanced support for flashing and debugging.
- Added support for application user mode, application memory
  partitions, and hardware stack protection in ARMv8m
- Applied MISRA-C code guideline on the kernel and core components of Zephyr.
  MISRA-C is a well established code guideline focused on embedded systems and
  aims to improve code safety, security and portability.

The following sections provide detailed lists of changes by component.

## Security Vulnerability Related

The following security vulnerabilities (CVEs) were addressed in this release:

- Tinycrypt HMAC-PRNG implementation doesn’t take the HMAC state
  clearing into account as it performs the HMAC operations, thereby using a
  incorrect HMAC key for some of the HMAC operations.
  (CVE-2017-14200)
- The shell DNS command can cause unpredictable results due to misuse of stack
  variables.
  (CVE-2017-14201)
- The shell implementation does not protect against buffer overruns resulting
  in unpredictable behavior.
  (CVE-2017-14202)
- We introduced Kernel Page Table Isolation, a technique for
  mitigating the Meltdown security vulnerability on x86 systems. This
  technique helps isolate user and kernel space memory by ensuring
  non-essential kernel pages are unmapped in the page tables when the CPU
  is running in the least privileged user mode, Ring 3. This is the
  fix for Rogue Data Cache Load. (CVE-2017-5754)
- We also addressed these CVEs for the x86 port:

  - Bounds Check Bypass (CVE-2017-5753)
  - Branch Target Injection (CVE-2017-5715)
  - Speculative Store Bypass (CVE-2018-3639)
  - L1 Terminal Fault (CVE-2018-3620)
  - Lazy FP State Restore (CVE-2018-3665)

## Kernel

- The timing subsystem has been reworked and mostly replaced:

  > - The timer driver API has been extensively reworked, greatly
  >   simplifying the resulting drivers. By removing thousands of lines
  >   of code, we reduced the size of a typical kernel build by hundreds
  >   of bytes.
  > - TICKLESS\_KERNEL mode is now the default on all architectures. Many
  >   bugs were fixed in this support.
- Lots of work on the rapidly-evolving SMP subsystem:

  - There is a new CPU affinity API available to “pin” threads to
    specific cores or sets of cores.
  - The core kernel is now 100% free of use of the global irq\_lock on
    SMP systems, and exclusively uses the spinlock API (which on
    uniprocessor systems reduces to the same code).
  - Zephyr now has a simple interprocessor interrupt framework for
    applications, such as the scheduler, to use for synchronously
    notifying other processors of state changes. It’s currently implemented
    only on x86\_64 and used only for thread abort.
- Zephyr now has support for the x86\_64 architecture. It is
  currently implemented only for QEMU targets.

  - It supports arbitrary numbers of CPUs in SMP, and runs in SMP mode
    by default, our first platform to do so.
  - It currently runs code built for the “x32” ABI, which is a native
    64-bit hardware state, where pointers are 32 bit in memory.
    Zephyr still has some lurking word size bugs that will need to be
    fixed to turn on native 64 bit code generation.
- K\_THREAD\_STACK\_BUFFER() has been demoted to a private API and will be removed
  in a future Zephyr release.
- A new API sys\_mutex has been introduced. It has the same semantics
  as a k\_mutex, but the memory for it can reside in user memory and so
  no explicit permission management is required.
- sys\_mem\_pool() now uses a sys\_mutex() for concurrency control.
- Memory protection changes:

  - CONFIG\_APPLICATION\_MEMORY option has been removed from Zephyr. All test
    cases have been appropriately converted to use memory domains.
  - The build time memory domain partition generation mechanism, formerly
    an optional feature under CONFIG\_APP\_SHARED\_MEM, has been overhauled
    and is now a core part of memory protection.
  - Userspace is no longer enabled by default for tests. Tests that are
    written to execute wholly or in part in user mode will need to enable
    CONFIG\_TEST\_USERSPACE in the test’s project configuration. There are
    assertions in place to enforce that this is done.
  - The default stack size for handling system calls has been increased to
    1024 bytes.
- We started applying MISRA-C ([https://www.misra.org.uk/](https://www.misra.org.uk/)) code guideline on
  the Zephyr kernel. MISRA-C is a well established code guideline focused on
  embedded systems and aims to improve code safety, security, and portability.
  This initial effort was narrowed to the Zephyr kernel and architecture
  code, and focused only on mandatory and required rules. The following rules
  were addressed:

  - Namespace changes
  - Normalize switch() operators
  - Avoid implicit conversion to boolean types
  - Fix and normalize headers guard
  - Make if() evaluate boolean operands
  - Remove all VLAs (variable length array)
  - Avoid undefined and implementation defined behavior with shift operator
  - Remove recursions

## Architectures

- Introduced X86\_64 (64 bit) architecture support with SMP features
- High-level Kconfig symbol structure for Trusted Execution
- ARM:

  - Re-architect Memory Protection code for ARM and NXP
  - Fully support application user mode, memory partitions, and
    stack protection in ARMv8m
  - Support built-in stack overflow protection in user mode in ARMv8m
  - Fix stack overflow error reporting
  - Support executing from SRAM in XIP builds
  - Support non-cacheable memory sections
  - Remove power-of-two align and size requirement for ARMv8-m
  - Introduce sync barriers in ARM-specific IRQ lock/unlock functions
  - Enforce double-word stack alignment on exception entry
  - API to allow Non-Secure FPU Access (ARMv8-M)
  - Various enhancements in ARM system boot code
  - Indicate Secure domain fault in Non-Secure fault exception
  - Update ARM CMSIS headers to version 5.4.0
- ARC:

  - Userspace and MPU driver improvements
  - Optimization of the thread stack definition macros
  - Bug fixes: handling of lp\_xxx registers in \_rirq\_return\_from\_coop, nested
    interrupt handling, hardware stack bounds checking, execution benchmarking
  - Atomic operations are now usable from user mode on all ARC CPUs
- x86:

  - Support for non-PAE page tables has been dropped.
  - Fixed various security CVEs related to micro-architecture side-effects of
    speculative execution, as detailed in the security notes.
  - Added robustness when reporting exceptions generated due to stack
    overflows or induced in user mode
  - Pages containing read-only data no longer have the execute disable (XD)
    bit un-set.
  - Fix potential IRQ stack corruption when handling double faults

## Boards & SoC Support

- Added the all new [NRF52 simulated board](../boards/native/nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim):
  This simulator models some of the hardware in an NRF52832 SOC, to enable
  running full system, multi-node simulations, without the need of real
  hardware. It enables fast, reproducible testing, development, and debugging
  of an application, BlueTooth (BT) stack, and kernel. It relies on [BabbleSim](https://BabbleSim.github.io)
  to simulate the radio physical layer.
- Added SoC configuration for nRF9160 and Musca ARM Cortex-M33 CPU
- Added support for the following ARM boards:

  - 96b\_stm32\_sensor\_mez
  - b\_l072z\_lrwan1
  - bl652\_dvk
  - bl654\_dvk
  - cy8ckit\_062\_wifi\_bt\_m0
  - cy8ckit\_062\_wifi\_bt\_m4
  - efm32hg\_slstk3400a
  - efm32pg\_stk3402a
  - efr32mg\_sltb004a
  - mimxrt1020\_evk
  - mimxrt1060\_evk
  - mimxrt1064\_evk
  - nrf52832\_mdk
  - nrf52840\_blip
  - nrf52840\_mdk
  - nrf52840\_papyr
  - nrf52840\_pca10090
  - nrf9160\_pca10090
  - nucleo\_f302r8
  - nucleo\_f746zg
  - nucleo\_f756zg
  - nucleo\_l496zg
  - nucleo\_l4r5zi
  - particle\_argon
  - particle\_xenon
  - v2m\_musca
- Added support for the following RISC-V boards:

  - rv32m1\_vega
- Added support for the following ARC boards:
  \* Synopsys ARC IoT DevKit
  \* Several ARC simulation targets (ARC nSIM EM/SEM; with and without MPU stack guards)
- Added support for the following shield boards:

  - frdm\_kw41z
  - x\_nucleo\_iks01a1
  - x\_nucleo\_iks01a2

## Drivers and Sensors

- Added new drivers and backends for [native\_posix](../boards/native/native_posix/doc/index.md#native-posix):

  - A UART driver that maps the Zephyr UART to a new host PTY
  - A USB driver that can expose a host connected USB device
  - A display driver that will render to a dedicated window using the SDL
    library
  - A dedicated backend for the new logger subsystem
- Counter

  - Refactored API
  - Ported existing counter and RTC drivers to the new API
  - Deprecated legacy API
- RTC

  - Deprecated the RTC API. The Counter API should be used instead
- UART

  - Added asynchronous API.
  - Added implementation of the new asynchronous API for nRF series (UART and
    UARTE).
- ADC

  - ADC driver APIs are now available to threads running in user mode.
  - Overhauled adc\_dw and renamed it to adc\_intel\_quark\_se\_c1000\_ss
  - Fixed handling of invalid sampling requests
- Display

  - Introduced mcux elcdif shim driver
  - Added support for ssd16xx monochrome controllers
  - Added support for ssd1608, gde029a1, and hink e0154a05
  - Added SDL based display emulation driver
  - Added SSD1673 EPD controller driver
  - Added SSD1306 display controller driver
- Flash:

  - nRF5 flash driver support UICR operations
  - Added driver for STM32F7x series
  - Added flash driver support for Atmel SAM E70
  - Added a generic spi nor flash driver
  - Added flash driver for SiLabs Gecko SoCs
- Ethernet:

  - Extended mcux driver for i.mx rt socs
  - Added driver for Intel PRO/1000 Ethernet controller
- I2C

  - Added mcux lpi2c shim driver
  - Removed deprecated i2c\_atmel\_sam3 driver
  - Introduced Silabs i2c shim driver
  - Added support for I2S stm32
- Pinmux

  - Added RV32M1 driver
  - Added pinmux driver for Intel S1000
  - Added support for STM32F302x8
- PWM

  - Added SiFive PWM driver
  - Added Atmel SAM PWM driver
  - Converted nRF drivers to use device tree
- Sensor

  - Added lis2ds12, lis2dw12, lis2mdl, and lsm303dlhc drivers
  - Added ms5837 driver
  - Added support for Nordic QDEC
  - Converted drivers to use device tree
- Serial

  - Added RV32M1 driver
  - Added new asynchronous UART API
  - Added support for ARM PL011 UART
  - Introduced Silabs leuart shim serial driver
  - Adapted gecko uart driver for Silabs EFM32HG
- USB

  - Added native\_posix USB driver
  - Added usb device driver for Atmel SAM E70 family
  - Added nRF52840 USBD driver
- Other Drivers

  - clock\_control: Added RV32M1 driver
  - console: Removed telnet driver
  - entropy: Added Atmel SAM entropy generator driver
  - spi: Converted nRF drivers to use device tree
  - watchdog: Converted drivers to new API
  - wifi: simplelink: Implemented setsockopt() for TLS offload
  - wifi: Added inventek es-WiFi driver
  - timer: Refactored and accuracy improvements of the arcv2 timer driver (boot
    time measurements)
  - timer: Added/reworked Xtensa, RISV-V, NRF, HPET, and ARM systick drivers
  - gpio: Added RV32M1 driver
  - hwinfo: Added new hwinfo API and drivers
  - ipm: Added IMX IPM driver for i.MX socs
  - interrupt\_controller: Added RV32M1 driver
  - interrupt\_controller: Added support for STM32F302x8 EXTI\_LINES
  - neural\_net: Added Intel GNA driver
  - can: Added socket CAN support

## Networking

- The [BSD socket API](../connectivity/networking/api/sockets.md#bsd-sockets-interface) should be used by
  applications for any network connectivity needs.
- Majority of the network sample applications were converted to use
  the BSD socket API.
- New BSD socket based APIs were created for these components and protocols:

  - [MQTT](../connectivity/networking/api/mqtt.md#mqtt-socket-interface)
  - [CoAP](../connectivity/networking/api/coap.md#coap-sock-interface)
  - [LWM2M](../connectivity/networking/api/lwm2m.md#lwm2m-interface)
  - [SNTP](../connectivity/networking/api/sntp.md#sntp-interface)
- net-app client and server APIs were removed. This also required removal of
  the following net-app based legacy APIs:

  - MQTT
  - CoAP
  - SNTP
  - LWM2M
  - HTTP client and server
  - Websocket
- Network packet ([net-pkt](../connectivity/networking/api/net_pkt.md#net-pkt-interface)) API overhaul. The new
  net-pkt API uses less memory and is more streamlined than the old one.
- Implement following BSD socket APIs: `freeaddrinfo()`, `gethostname()`,
  `getnameinfo()`, `getsockopt()`, `select()`, `setsockopt()`,
  `shutdown()`
- Converted BSD socket code to use global file descriptor numbers.
- Network subsystem converted to use new [logging system](../services/logging/index.md#logging-api).
- Added support for disabling IPv4, IPv6, UDP, and TCP simultaneously.
- Added support for [BSD socket offloading](../connectivity/networking/api/net_offload.md#net-socket-offloading).
- Added support for long lifetime IPv6 prefixes.
- Added enhancements to IPv6 multicast address checking.
- Added support for IPv6 Destination Options Header extension.
- Added support for packet socket (AF\_PACKET).
- Added support for socket CAN (AF\_CAN).
- Added support for SOCKS5 proxy in MQTT client.
- Added support for IPSO Timer object in LWM2M.
- Added support for receiving gratuitous ARP request.
- Added sample application for Google IoT Cloud.
- [Network interface](../connectivity/networking/api/net_if.md#net-if-interface) numbering starts now from 1 for
  POSIX compatibility.
- [OpenThread](../connectivity/networking/api/thread.md#thread-protocol-interface) enhancements.
- [zperf](../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.") sample application fixes.
- [LLDP](../connectivity/networking/api/lldp.md#lldp-interface) (Link Layer Discovery Protocol) enhancements.
- ARP cache update fix.
- gPTP link delay calculation fixes.
- Changed how network data is passed from
  [L2 to network device driver](../connectivity/networking/net-stack-architecture.md#network-stack-architecture).
- Removed RPL (Ripple) IPv6 mesh routing support.
- MQTT is now available to threads running in user mode.
- Network device driver additions and enhancements:

  - Added Intel PRO/1000 Ethernet driver (e1000).
  - Added SMSC9118/LAN9118 Ethernet driver (smsc911x).
  - Added Inventek es-WiFi driver for disco\_l475\_iot1 board.
  - Added support for automatically enabling QEMU based Ethernet drivers.
  - SAM-E70 gmac Ethernet driver Qav fixes.
  - enc28j60 Ethernet driver fixes and enhancements.

## Bluetooth

- Host:

  - GATT: Added support for Robust Caching
  - GATT: L2CAP: User driven flow control
  - Many fixes to Mesh
  - Fixed and improved persistent storage handling
  - Fixed direct advertising support
  - Fixed security level 4 handling
  - Add option to configure peripheral connection parameters
  - Added support for updating advertising data without having to restart advertising
  - Added API to iterate through existing bonds
  - Added support for setting channel map
  - Converted SPI HCI driver to use device tree
- New BLE split software Controller (experimental):

  - Split design with Upper Link Layer and Lower Link Layer
  - Enabled with [`CONFIG_BT_LL_SW_SPLIT`](../kconfig.md#CONFIG_BT_LL_SW_SPLIT "CONFIG_BT_LL_SW_SPLIT") (disabled by default)
  - Support for multiple BLE radio hardware architectures
  - Asynchronous handling of procedures in the ULL
  - Enhanced radio utilization (99% on continuous 100ms scan)
  - Latency resilience: Approx 100uS vs 10uS, 10x improvement
  - CPU and power usage: About 20% improvement
  - Multiple advertiser and scanner instances
  - Support for both Big and Little-Endian architectures
- Controller:

  - Added support for setting the public address
  - Multiple control procedures fixes and improvements
  - Advertising random delay fixes
  - Fixed a serious memory corruption issue during scanning
  - Fixes to RSSI measurement
  - Fixes to Connection Failed to be Established sequence
  - Transitioned to the new logging subsystem from syslog
  - Switched from `-Ofast` to `-O2` in time-critical sections
  - Reworked the RNG/entropy driver to make it available to apps
  - Multiple size optimizations to make it fit in smaller devices
  - nRF: Rework the PPI channel assignment to use pre-assigned ones
  - Add extensive documentation to the shared primitives
- Several fixes for big-endian architectures

## Build and Infrastructure

- Added support for out-of-tree architectures.
- Added support for out-of-tree implementations of in-tree drivers.
- [BabbleSim](https://BabbleSim.github.io) has been integrated in Zephyr’s CI system.
- Introduced `DT_` prefix for all labels generated for information extracted
  from device tree (with a few exceptions, such as labels for LEDs and buttons,
  kept for backward compatibility with existing applications). Deprecated all
  other defines that are generated.
- Introduce CMake variables for DT symbols, just as we have for CONFIG symbols.
- Move DeviceTree processing before Kconfig. Thereby allowing software
  to be configured based on DeviceTree information.
- Automatically change the KCONFIG\_ROOT when the application directory
  has a Kconfig file.
- Added [west](../develop/west/index.md#west) tool for multiple repository management
- Added support for [Zephyr modules](../develop/modules.md#modules)
- Build system `flash` and `debug` targets now require west
- Added generation of DT\_<COMPAT>\_<INSTANCE>\_<PROP> defines which allowed
  sensor or other drivers on buses like I2C or SPI to not require dts fixup.
- Added proper support for device tree boolean properties

## Libraries / Subsystems

- Added a new display API and subsystem
- Added support for CTF Tracing
- Added support for JWT (JSON Web Tokens)
- Flash Maps:

  - API extension
  - Automatic generation of the list of flash areas
- Settings:

  - Enabled logging instead of ASSERTs
  - Always use the storage partition for FCB
  - Fixed FCB backend and common bugs
- Logging:

  - Removed sys\_log, which has been replaced by the new logging subsystem
    introduced in v1.13
  - Refactored log modules registration macros
  - Improved synchronous operation (see `CONFIG_LOG_IMMEDIATE`)
  - Added commands to control the logger using shell
  - Added [`LOG_PANIC()`](../doxygen/html/group__log__ctrl.md#ga9ee5a99e0487e3f1e6d289b12c19ad5a) call to the fault handlers to ensure that
    logs are output on fault
  - Added mechanism for handling logging of transient strings. See
    `log_strdup()`
  - Added support for up to 15 arguments in the log message
  - Added optional function name prefix in the log message
  - Changed logging thread priority to the lowest application priority
  - Added notification about dropped log messages due to insufficient logger
    buffer size
  - Added log backends:

    - RTT
    - native\_posix
    - net
    - SWO
    - Xtensa Sim
  - Changed default timestamp source function to [`k_uptime_get_32()`](../doxygen/html/group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)
- Shell:

  - Added new implementation of the shell sub-system. See [Shell](../services/shell/index.md#shell-api)
  - Added shell backends:

    - UART
    - RTT
    - telnet
- Ring buffer:

  - Added byte mode
  - Added API to work directly on ring buffer memory to reduce memory copying
  - Removed `sys_` prefix from API functions
- MBEDTLS APIs may now be used from user mode.

## HALs

- Updated Nordic nrfx to version 1.6.2
- Updated Nordic nrf ieee802154 radio driver to version 1.2.3
- Updated SimpleLink to TI CC32XX SDK 2.40.01.01
- Added Microchip MEC1701 Support
- Added Cypress PDL for PSoC6 SoC Support
- Updates to stm32cube, Silabs Gecko SDK, Atmel.
- Update ARM CMSIS headers to version 5.4.0

## Documentation

- Reorganized subsystem documentation into more meaningful collections
  and added or improved introductory material for each subsystem.
- Overhauled Bluetooth documentation to split it into
  manageable units and included additional information, such as
  architecture and tooling.
- Added to and improved documentation on many subsystems and APIs
  including socket offloading, Ethernet management, LLDP networking,
  network architecture and overview, net shell, CoAP, network interface,
  network configuration library, DNS resolver, DHCPv4, DTS, flash\_area,
  flash\_mpa, NVS, settings, and more.
- Introduced a new debugging guide (see [Debug Probes](../develop/flash_debug/probes.md#debug-probes)) that documents
  the supported debug probes and host tools in
  one place, including which combinations are valid.
- Clarified and improved information about the west tool and its use.
- Improved [development process](../project/index.md#development-model) documentation
  including how new features
  are proposed and tracked, and clarifying API lifecycle, issue and PR
  tagging requirements, contributing guidelines, doc guidelines,
  release process, and PR review process.
- Introduced a developer “fast” doc build option to eliminate
  the time needed to create the full kconfig option docs from a local
  doc build, saving potentially five minutes for a full doc build. (Doc
  building time depends on your development hardware performance.)
- Made dramatic improvements to the doc build processing, bringing
  iterative local doc generation down from over two minutes to only a
  few seconds. This makes it much faster for doc developers to iteratively
  edit and test doc changes locally before submitting a PR.
- Added a new `zephyr-file` directive to link directly to files in the
  Git tree.
- Introduced simplified linking to doxygen-generated API reference
  material.
- Made board documentation consistent, enabling a board-image carousel
  on the zephyrproject.org home page.
- Reduced unnecessarily large images to improve page load times.
- Added CSS changes to improve API docs appearance and usability
- Made doc version selector more obvious, making it easier to select
  documentation for a specific release
- Added a friendlier and more graphic home page.

## Tests and Samples

- A new set of, multinode, full system tests of the BT stack,
  based on [BabbleSim](https://BabbleSim.github.io) have been added.
- Added unique identifiers to all tests and samples.
- Removed old footprint benchmarks
- Added tests for CMSIS RTOS API v2, BSD Sockets, CANBus, Settings, USB,
  and miscellaneous drivers.
- Added benchmark applications for the scheduler and mbedTLS
- Added samples for the display subsystem, LVGL, Google IOT, Sockets, CMSIS RTOS
  API v2, Wifi, Shields, IPC subsystem, USB CDC ACM, and USB HID.
- Add support for using sanitycheck testing with Renode

## Issue Related Items

These GitHub issues were addressed since the previous 1.13.0 tagged
release:

- [GitHub #15407](https://github.com/zephyrproject-rtos/zephyr/issues/15407) - [Coverity CID :197597]Incorrect expression in /tests/kernel/static\_idt/src/main.c
- [GitHub #15406](https://github.com/zephyrproject-rtos/zephyr/issues/15406) - [Coverity CID :197598]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #15405](https://github.com/zephyrproject-rtos/zephyr/issues/15405) - [Coverity CID :197599]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #15404](https://github.com/zephyrproject-rtos/zephyr/issues/15404) - [Coverity CID :197600]Incorrect expression in /tests/lib/c\_lib/src/main.c
- [GitHub #15403](https://github.com/zephyrproject-rtos/zephyr/issues/15403) - [Coverity CID :197601]Incorrect expression in /tests/kernel/common/src/intmath.c
- [GitHub #15402](https://github.com/zephyrproject-rtos/zephyr/issues/15402) - [Coverity CID :197602]Incorrect expression in /tests/kernel/common/src/intmath.c
- [GitHub #15401](https://github.com/zephyrproject-rtos/zephyr/issues/15401) - [Coverity CID :197603]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #15400](https://github.com/zephyrproject-rtos/zephyr/issues/15400) - [Coverity CID :197604]Memory - corruptions in /tests/kernel/mem\_protect/userspace/src/main.c
- [GitHub #15399](https://github.com/zephyrproject-rtos/zephyr/issues/15399) - [Coverity CID :197605]Null pointer dereferences in /subsys/testsuite/ztest/src/ztest\_mock.c
- [GitHub #15398](https://github.com/zephyrproject-rtos/zephyr/issues/15398) - [Coverity CID :197606]Incorrect expression in /tests/kernel/common/src/irq\_offload.c
- [GitHub #15397](https://github.com/zephyrproject-rtos/zephyr/issues/15397) - [Coverity CID :197607]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #15396](https://github.com/zephyrproject-rtos/zephyr/issues/15396) - [Coverity CID :197608]Incorrect expression in /tests/lib/c\_lib/src/main.c
- [GitHub #15395](https://github.com/zephyrproject-rtos/zephyr/issues/15395) - [Coverity CID :197609]Incorrect expression in /tests/kernel/interrupt/src/nested\_irq.c
- [GitHub #15394](https://github.com/zephyrproject-rtos/zephyr/issues/15394) - [Coverity CID :197610]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #15393](https://github.com/zephyrproject-rtos/zephyr/issues/15393) - [Coverity CID :197611]Integer handling issues in /lib/os/printk.c
- [GitHub #15392](https://github.com/zephyrproject-rtos/zephyr/issues/15392) - [Coverity CID :197612]Integer handling issues in /lib/os/printk.c
- [GitHub #15390](https://github.com/zephyrproject-rtos/zephyr/issues/15390) - [Coverity CID :197614]Incorrect expression in /tests/lib/c\_lib/src/main.c
- [GitHub #15389](https://github.com/zephyrproject-rtos/zephyr/issues/15389) - [Coverity CID :197615]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #15388](https://github.com/zephyrproject-rtos/zephyr/issues/15388) - [Coverity CID :197616]Null pointer dereferences in /subsys/testsuite/ztest/src/ztest\_mock.c
- [GitHub #15387](https://github.com/zephyrproject-rtos/zephyr/issues/15387) - [Coverity CID :197617]Incorrect expression in /tests/kernel/common/src/multilib.c
- [GitHub #15386](https://github.com/zephyrproject-rtos/zephyr/issues/15386) - [Coverity CID :197618]Error handling issues in /subsys/shell/shell\_telnet.c
- [GitHub #15385](https://github.com/zephyrproject-rtos/zephyr/issues/15385) - [Coverity CID :197619]Incorrect expression in /tests/kernel/mem\_pool/mem\_pool/src/main.c
- [GitHub #15384](https://github.com/zephyrproject-rtos/zephyr/issues/15384) - [Coverity CID :197620]Incorrect expression in /tests/kernel/static\_idt/src/main.c
- [GitHub #15383](https://github.com/zephyrproject-rtos/zephyr/issues/15383) - [Coverity CID :197621]Incorrect expression in /tests/kernel/static\_idt/src/main.c
- [GitHub #15382](https://github.com/zephyrproject-rtos/zephyr/issues/15382) - [Coverity CID :197622]Incorrect expression in /tests/kernel/tickless/tickless\_concept/src/main.c
- [GitHub #15381](https://github.com/zephyrproject-rtos/zephyr/issues/15381) - [Coverity CID :197623]Incorrect expression in /tests/kernel/interrupt/src/nested\_irq.c
- [GitHub #15380](https://github.com/zephyrproject-rtos/zephyr/issues/15380) - USAGE FAULT on tests/crypto/rand32/ on sam\_e70\_xplained
- [GitHub #15379](https://github.com/zephyrproject-rtos/zephyr/issues/15379) - foundries.io CI: tests/kernel/mem\_protect/stackprot fails on nrf52
- [GitHub #15370](https://github.com/zephyrproject-rtos/zephyr/issues/15370) - log\_strdup() leaks memory if log message is filtered
- [GitHub #15365](https://github.com/zephyrproject-rtos/zephyr/issues/15365) - Bluetooth qualification test MESH/SR/HM/CFS/BV-02-C is failing
- [GitHub #15361](https://github.com/zephyrproject-rtos/zephyr/issues/15361) - nRF timer: investigate race condition when setting clock timeout in TICKLESS mode
- [GitHub #15348](https://github.com/zephyrproject-rtos/zephyr/issues/15348) - ARM Cortex-M: SysTick: unhandled race condition
- [GitHub #15346](https://github.com/zephyrproject-rtos/zephyr/issues/15346) - VLAN support is broken
- [GitHub #15336](https://github.com/zephyrproject-rtos/zephyr/issues/15336) - Unable to transmit data using interrupt driven API with nrf UARTE peripheral
- [GitHub #15333](https://github.com/zephyrproject-rtos/zephyr/issues/15333) - hci\_uart controller driver loses sync after host driver is reset
- [GitHub #15329](https://github.com/zephyrproject-rtos/zephyr/issues/15329) - Bluetooth: GATT Client Configuration is not cleared when device is unpaired
- [GitHub #15325](https://github.com/zephyrproject-rtos/zephyr/issues/15325) - conn->le.keys pointer is not cleared even after the keys struct is invalidated after unpair
- [GitHub #15324](https://github.com/zephyrproject-rtos/zephyr/issues/15324) - Error undefined reference to ‘\_\_aeabi\_uldivmod’ when build Zephyr for nrf52\_pca10040 board
- [GitHub #15309](https://github.com/zephyrproject-rtos/zephyr/issues/15309) - ARM Cortex-M SysTick Load value setting off-by-one
- [GitHub #15303](https://github.com/zephyrproject-rtos/zephyr/issues/15303) - net: Stackoverflow in net mgmt thread
- [GitHub #15300](https://github.com/zephyrproject-rtos/zephyr/issues/15300) - Bluetooth: Mesh: bt\_mesh\_fault\_update() doesn’t update publication message
- [GitHub #15299](https://github.com/zephyrproject-rtos/zephyr/issues/15299) - west init fails in powershell
- [GitHub #15289](https://github.com/zephyrproject-rtos/zephyr/issues/15289) - Zephyr module uses ‘' in path on windows when creating Kconfig files
- [GitHub #15285](https://github.com/zephyrproject-rtos/zephyr/issues/15285) - arc: it’s not reliable to use exc\_nest\_count to check nest interrupt
- [GitHub #15280](https://github.com/zephyrproject-rtos/zephyr/issues/15280) - tests/kernel/mem\_protect/stackprot fails on platform qemu\_riscv32
- [GitHub #15266](https://github.com/zephyrproject-rtos/zephyr/issues/15266) - doc: Contribution guidelines still link to IRC
- [GitHub #15260](https://github.com/zephyrproject-rtos/zephyr/issues/15260) - Shell doesn’t always process input data when it arrives
- [GitHub #15259](https://github.com/zephyrproject-rtos/zephyr/issues/15259) - CAN sample does not work
- [GitHub #15251](https://github.com/zephyrproject-rtos/zephyr/issues/15251) - nRF Watchdog not triggering on kernel panic
- [GitHub #15246](https://github.com/zephyrproject-rtos/zephyr/issues/15246) - doc: confusion about dtc version
- [GitHub #15240](https://github.com/zephyrproject-rtos/zephyr/issues/15240) - esp32 build broken
- [GitHub #15236](https://github.com/zephyrproject-rtos/zephyr/issues/15236) - add external spi-nor flash will build fail
- [GitHub #15235](https://github.com/zephyrproject-rtos/zephyr/issues/15235) - Missing license references in DTS files
- [GitHub #15234](https://github.com/zephyrproject-rtos/zephyr/issues/15234) - Missing SPDX license references in drivers source files.
- [GitHub #15228](https://github.com/zephyrproject-rtos/zephyr/issues/15228) - tests: getnameinfo runs with user mode disabled
- [GitHub #15227](https://github.com/zephyrproject-rtos/zephyr/issues/15227) - sockets: no syscall for gethostname()
- [GitHub #15221](https://github.com/zephyrproject-rtos/zephyr/issues/15221) - ARC: incorrect value checked for MPU violation
- [GitHub #15216](https://github.com/zephyrproject-rtos/zephyr/issues/15216) - k\_sleep() expires sooner than expected on STM32F4 (Cortex M4)
- [GitHub #15213](https://github.com/zephyrproject-rtos/zephyr/issues/15213) - cmake infrastructure in code missing file level license identifiers
- [GitHub #15206](https://github.com/zephyrproject-rtos/zephyr/issues/15206) - sanitycheck –coverage: stack overflows on qemu\_x86, mps2\_an385 and qemu\_x86\_nommu
- [GitHub #15205](https://github.com/zephyrproject-rtos/zephyr/issues/15205) - hci\_usb not working on v1.14.0rc3 with SDK 0.10.0
- [GitHub #15204](https://github.com/zephyrproject-rtos/zephyr/issues/15204) - lwm2m engine hangs on native\_posix
- [GitHub #15198](https://github.com/zephyrproject-rtos/zephyr/issues/15198) - tests/booting: Considering remove it
- [GitHub #15197](https://github.com/zephyrproject-rtos/zephyr/issues/15197) - Socket-based DNS API will hang device if DNS query is not answered
- [GitHub #15184](https://github.com/zephyrproject-rtos/zephyr/issues/15184) - Fix build issue with z\_sys\_trace\_thread\_switched\_in
- [GitHub #15183](https://github.com/zephyrproject-rtos/zephyr/issues/15183) - BLE HID sample often asserts on Windows 10 reconnection
- [GitHub #15178](https://github.com/zephyrproject-rtos/zephyr/issues/15178) - samples/mpu/mem\_domain\_apis\_test: Did not get to “destroy app0 domain”, went into indefinite loop
- [GitHub #15177](https://github.com/zephyrproject-rtos/zephyr/issues/15177) - samples/drivers/crypto: CBC and CTR mode not supported
- [GitHub #15170](https://github.com/zephyrproject-rtos/zephyr/issues/15170) - undefined symbol TINYCBOR during doc build
- [GitHub #15169](https://github.com/zephyrproject-rtos/zephyr/issues/15169) - [Coverity CID :197534]Memory - corruptions in /subsys/logging/log\_backend\_rtt.c
- [GitHub #15168](https://github.com/zephyrproject-rtos/zephyr/issues/15168) - [Coverity CID :197535]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #15167](https://github.com/zephyrproject-rtos/zephyr/issues/15167) - [Coverity CID :197536]Parse warnings in /include/mgmt/buf.h
- [GitHub #15166](https://github.com/zephyrproject-rtos/zephyr/issues/15166) - [Coverity CID :197537]Control flow issues in /subsys/power/power.c
- [GitHub #15163](https://github.com/zephyrproject-rtos/zephyr/issues/15163) - nsim\_\*\_mpu\_stack\_guard fails if CONFIG\_USERSPACE=n but CONFIG\_HW\_STACK\_PROTECTION=y
- [GitHub #15161](https://github.com/zephyrproject-rtos/zephyr/issues/15161) - stack overflow in tests/posix/common on nsim\_em\_mpu\_stack\_guard
- [GitHub #15157](https://github.com/zephyrproject-rtos/zephyr/issues/15157) - mps2\_an385 and GNU Arm Embedded gcc-arm-none-eabi-7-2018-q2-update failed tests
- [GitHub #15154](https://github.com/zephyrproject-rtos/zephyr/issues/15154) - mempool can result in OOM while memory is available
- [GitHub #15153](https://github.com/zephyrproject-rtos/zephyr/issues/15153) - Some empty qemu\_x86 output when running code coverage using sanity\_check
- [GitHub #15152](https://github.com/zephyrproject-rtos/zephyr/issues/15152) - tests/kernel/pipe/pipe: “Kernel Oops” and “CPU Page Fault” when running coverage for qemu\_x86
- [GitHub #15151](https://github.com/zephyrproject-rtos/zephyr/issues/15151) - tests/tickless/tickless\_concept: Assertions when running code coverage on qemu\_x86
- [GitHub #15150](https://github.com/zephyrproject-rtos/zephyr/issues/15150) - tests/kernel/threads/thread\_api: “Double faults” when running code coverage in qemu\_x86
- [GitHub #15149](https://github.com/zephyrproject-rtos/zephyr/issues/15149) - mps2\_an385: fatal lockup when running code coverage
- [GitHub #15148](https://github.com/zephyrproject-rtos/zephyr/issues/15148) - tests/kernel/mem\_pool/mem\_pool\_concept/: Assertion failures for mpns2\_an385
- [GitHub #15146](https://github.com/zephyrproject-rtos/zephyr/issues/15146) - mps2\_an385: Multiple “MPU Fault”s, “Hardware Fault”s “Stack Check Fail!” and “Bus Fault” when running code coverage
- [GitHub #15145](https://github.com/zephyrproject-rtos/zephyr/issues/15145) - USB HF clock stop fail
- [GitHub #15131](https://github.com/zephyrproject-rtos/zephyr/issues/15131) - ARC: off-by-one in MPU V2 \_is\_in\_region()
- [GitHub #15130](https://github.com/zephyrproject-rtos/zephyr/issues/15130) - ARC: Z\_ARCH\_THREAD\_STACK\_MEMBER defined incorrectly
- [GitHub #15129](https://github.com/zephyrproject-rtos/zephyr/issues/15129) - ARC: tests/kernel/critical times out on nsim\_sem
- [GitHub #15126](https://github.com/zephyrproject-rtos/zephyr/issues/15126) - multiple intermittent test failure on ARC
- [GitHub #15124](https://github.com/zephyrproject-rtos/zephyr/issues/15124) - DNS not working with NET\_OFFLOAD
- [GitHub #15109](https://github.com/zephyrproject-rtos/zephyr/issues/15109) - ATSAME70 MCU(SAM E70 Xplained) RAM random after a watchdog reset.
- [GitHub #15107](https://github.com/zephyrproject-rtos/zephyr/issues/15107) - samples/application\_development/code\_relocation fails to build with coverage on mps2\_an385
- [GitHub #15103](https://github.com/zephyrproject-rtos/zephyr/issues/15103) - nrf52810\_pca10040 SRAM space not enough
- [GitHub #15100](https://github.com/zephyrproject-rtos/zephyr/issues/15100) - Bluetooth: GATT (un)subscribe can silently fail
- [GitHub #15099](https://github.com/zephyrproject-rtos/zephyr/issues/15099) - Bluetooth: GATT Subscribe does not detect duplicate if new parameters are used.
- [GitHub #15096](https://github.com/zephyrproject-rtos/zephyr/issues/15096) - Cannot build samples/net/ipv4\_autoconf
- [GitHub #15093](https://github.com/zephyrproject-rtos/zephyr/issues/15093) - zephyr\_library\_compile\_options() lost support for duplicates
- [GitHub #15090](https://github.com/zephyrproject-rtos/zephyr/issues/15090) - FIFO: Clarify doc for k\_fifo\_alloc\_put
- [GitHub #15085](https://github.com/zephyrproject-rtos/zephyr/issues/15085) - Sanitycheck when running on devices is not counting samples in the final report
- [GitHub #15083](https://github.com/zephyrproject-rtos/zephyr/issues/15083) - MCUBoot is linked to slot0 because overlay is dropped in boilerplate.cmake
- [GitHub #15077](https://github.com/zephyrproject-rtos/zephyr/issues/15077) - Cannot boot application flashed to nrf52840\_pca10059
- [GitHub #15073](https://github.com/zephyrproject-rtos/zephyr/issues/15073) - Device crashes when starting with USB connected
- [GitHub #15070](https://github.com/zephyrproject-rtos/zephyr/issues/15070) - ieee802154: Configuration for CC2520 is not working
- [GitHub #15069](https://github.com/zephyrproject-rtos/zephyr/issues/15069) - arch: arm: thread arch.mode not always inline with thread’s privilege mode (e.g. system calls)
- [GitHub #15067](https://github.com/zephyrproject-rtos/zephyr/issues/15067) - bluetooth: bt\_set\_name rejects names of size CONFIG\_BT\_DEVICE\_NAME\_MAX
- [GitHub #15064](https://github.com/zephyrproject-rtos/zephyr/issues/15064) - tests/kernel/fp\_sharing: undefined reference k\_float\_disable()
- [GitHub #15063](https://github.com/zephyrproject-rtos/zephyr/issues/15063) - tests/subsys/settings/fcb/src/settings\_test\_save\_unaligned.c fail with assertion failure on nrf52\_pca10040
- [GitHub #15061](https://github.com/zephyrproject-rtos/zephyr/issues/15061) - Builds on Windows are broken due to invalid zephyr\_modules.txt parsing
- [GitHub #15059](https://github.com/zephyrproject-rtos/zephyr/issues/15059) - Fix builds w/o modules
- [GitHub #15056](https://github.com/zephyrproject-rtos/zephyr/issues/15056) - arch: arm: arch.mode variable \_not\_ initialized to nPRIV in user space enter
- [GitHub #15050](https://github.com/zephyrproject-rtos/zephyr/issues/15050) - Using TCP in zperf causes free memory access
- [GitHub #15044](https://github.com/zephyrproject-rtos/zephyr/issues/15044) - ARC: test failure in tests/kernel/threads/thread\_apis
- [GitHub #15039](https://github.com/zephyrproject-rtos/zephyr/issues/15039) - ADC drivers adc\_read\_async() keep pointers to sequence
- [GitHub #15037](https://github.com/zephyrproject-rtos/zephyr/issues/15037) - xtensa: context returns to thread after kernel oops
- [GitHub #15035](https://github.com/zephyrproject-rtos/zephyr/issues/15035) - build breakage on two ARC targets: missing arc\_exc\_saved\_sp
- [GitHub #15031](https://github.com/zephyrproject-rtos/zephyr/issues/15031) - net: 9cd547f53b “Fix ref counting for the net\_pkt” allegedly broke reference counting
- [GitHub #15019](https://github.com/zephyrproject-rtos/zephyr/issues/15019) - tests/kernel/common: test\_bitfield: test\_bitfield: (b1 not equal to (1 << bit))
- [GitHub #15018](https://github.com/zephyrproject-rtos/zephyr/issues/15018) - tests/kernel/threads/no-multithreading: Not booting
- [GitHub #15017](https://github.com/zephyrproject-rtos/zephyr/issues/15017) - Not able to set “0xFFFF No specific value” for GAP PPCP structured data
- [GitHub #15013](https://github.com/zephyrproject-rtos/zephyr/issues/15013) - tests/kernel/fatal: check\_stack\_overflow: (rv equal to TC\_FAIL)
- [GitHub #15012](https://github.com/zephyrproject-rtos/zephyr/issues/15012) - Unable to establish security after reconnect to dongle
- [GitHub #15009](https://github.com/zephyrproject-rtos/zephyr/issues/15009) - sanitycheck –coverage on qemu\_x86: cannot move location counter backwards
- [GitHub #15008](https://github.com/zephyrproject-rtos/zephyr/issues/15008) - SWO logger backend produces no output in ‘in place’ mode
- [GitHub #14992](https://github.com/zephyrproject-rtos/zephyr/issues/14992) - West documentation is largely missing
- [GitHub #14989](https://github.com/zephyrproject-rtos/zephyr/issues/14989) - Doc build does not include the zephyr modules Kconfig files
- [GitHub #14988](https://github.com/zephyrproject-rtos/zephyr/issues/14988) - USB device not recognized on PCA10056 preview-DK
- [GitHub #14985](https://github.com/zephyrproject-rtos/zephyr/issues/14985) - Clarify in release docs NOT to use github tagging.
- [GitHub #14974](https://github.com/zephyrproject-rtos/zephyr/issues/14974) - Kconfig.modules needs to be at the top level build folder
- [GitHub #14958](https://github.com/zephyrproject-rtos/zephyr/issues/14958) - [Coverity CID :197457]Control flow issues in /subsys/bluetooth/host/gatt.c
- [GitHub #14957](https://github.com/zephyrproject-rtos/zephyr/issues/14957) - [Coverity CID :197458]Insecure data handling in /subsys/usb/usb\_device.c
- [GitHub #14956](https://github.com/zephyrproject-rtos/zephyr/issues/14956) - [Coverity CID :197459]Memory - corruptions in /subsys/bluetooth/shell/gatt.c
- [GitHub #14955](https://github.com/zephyrproject-rtos/zephyr/issues/14955) - [Coverity CID :197460]Integer handling issues in /samples/bluetooth/ipsp/src/main.c
- [GitHub #14954](https://github.com/zephyrproject-rtos/zephyr/issues/14954) - [Coverity CID :197461]Insecure data handling in /subsys/usb/usb\_device.c
- [GitHub #14953](https://github.com/zephyrproject-rtos/zephyr/issues/14953) - [Coverity CID :197462]Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #14952](https://github.com/zephyrproject-rtos/zephyr/issues/14952) - [Coverity CID :197463]Memory - corruptions in /samples/bluetooth/central\_hr/src/main.c
- [GitHub #14951](https://github.com/zephyrproject-rtos/zephyr/issues/14951) - [Coverity CID :197464]Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #14950](https://github.com/zephyrproject-rtos/zephyr/issues/14950) - [Coverity CID :197465]Integer handling issues in /samples/bluetooth/ipsp/src/main.c
- [GitHub #14947](https://github.com/zephyrproject-rtos/zephyr/issues/14947) - no user mode access to MQTT subsystem
- [GitHub #14946](https://github.com/zephyrproject-rtos/zephyr/issues/14946) - cdc\_acm example doesn’t work on nrf52840\_pca10059
- [GitHub #14945](https://github.com/zephyrproject-rtos/zephyr/issues/14945) - nrf52840\_pca10059 executables do not work without mcuboot
- [GitHub #14943](https://github.com/zephyrproject-rtos/zephyr/issues/14943) - config BOARD\_HAS\_NRF5\_BOOTLOADER not honored for nrf52840\_pca10059
- [GitHub #14942](https://github.com/zephyrproject-rtos/zephyr/issues/14942) - tests/posix/fs don’t build on em\_starterkit\_em11d
- [GitHub #14934](https://github.com/zephyrproject-rtos/zephyr/issues/14934) - tinycbor is failing in nightly CI
- [GitHub #14928](https://github.com/zephyrproject-rtos/zephyr/issues/14928) - Bluetooth: Mesh: Provisioning state doesn’t always get properly re-initialized when doing reset
- [GitHub #14903](https://github.com/zephyrproject-rtos/zephyr/issues/14903) - tests/posix/fs test show messages dropped in the logs
- [GitHub #14902](https://github.com/zephyrproject-rtos/zephyr/issues/14902) - logger: Enabling USB CDC ACM disables logging
- [GitHub #14899](https://github.com/zephyrproject-rtos/zephyr/issues/14899) - Bluetooth controller ACL data packets stall
- [GitHub #14882](https://github.com/zephyrproject-rtos/zephyr/issues/14882) - USB DFU never enters DFU mode, when composite device is enabled and mcuboot is used
- [GitHub #14871](https://github.com/zephyrproject-rtos/zephyr/issues/14871) - tests/posix/fs : Dropped console output
- [GitHub #14870](https://github.com/zephyrproject-rtos/zephyr/issues/14870) - samples/mpu/mpu\_stack\_guard\_test: Found “Test not passed”
- [GitHub #14869](https://github.com/zephyrproject-rtos/zephyr/issues/14869) - tests/lib/ringbuffer: Assertion failure at test\_ring\_buffer\_main()
- [GitHub #14840](https://github.com/zephyrproject-rtos/zephyr/issues/14840) - settings: settings\_save\_one() doesn’t always seem to store data, even if it returns success
- [GitHub #14837](https://github.com/zephyrproject-rtos/zephyr/issues/14837) - Bluetooth shell scan command parameter mandatory/optional evaluation is broken
- [GitHub #14833](https://github.com/zephyrproject-rtos/zephyr/issues/14833) - Bluetooth init procedure with BT\_SETTINGS is not reliable
- [GitHub #14827](https://github.com/zephyrproject-rtos/zephyr/issues/14827) - cmake error
- [GitHub #14821](https://github.com/zephyrproject-rtos/zephyr/issues/14821) - [Coverity CID :196635]Error handling issues in /tests/net/mld/src/main.c
- [GitHub #14820](https://github.com/zephyrproject-rtos/zephyr/issues/14820) - [Coverity CID :196636]Integer handling issues in /kernel/sched.c
- [GitHub #14819](https://github.com/zephyrproject-rtos/zephyr/issues/14819) - [Coverity CID :196637]Uninitialized variables in /samples/net/sockets/can/src/main.c
- [GitHub #14818](https://github.com/zephyrproject-rtos/zephyr/issues/14818) - [Coverity CID :196638]Null pointer dereferences in /subsys/bluetooth/host/hci\_core.c
- [GitHub #14817](https://github.com/zephyrproject-rtos/zephyr/issues/14817) - [Coverity CID :196639]Error handling issues in /samples/bluetooth/ipsp/src/main.c
- [GitHub #14816](https://github.com/zephyrproject-rtos/zephyr/issues/14816) - [Coverity CID :196640]Integer handling issues in /arch/x86/core/thread.c
- [GitHub #14815](https://github.com/zephyrproject-rtos/zephyr/issues/14815) - [Coverity CID :196641]Null pointer dereferences in /samples/net/nats/src/nats.c
- [GitHub #14814](https://github.com/zephyrproject-rtos/zephyr/issues/14814) - [Coverity CID :196642]Error handling issues in /subsys/shell/shell\_uart.c
- [GitHub #14813](https://github.com/zephyrproject-rtos/zephyr/issues/14813) - [Coverity CID :196643]Null pointer dereferences in /subsys/net/ip/net\_context.c
- [GitHub #14807](https://github.com/zephyrproject-rtos/zephyr/issues/14807) - disable SPIN\_VALIDATE when SMP enabled
- [GitHub #14789](https://github.com/zephyrproject-rtos/zephyr/issues/14789) - doc: flash\_map and flash\_area
- [GitHub #14786](https://github.com/zephyrproject-rtos/zephyr/issues/14786) - Information about old sdk version provides wrong download link
- [GitHub #14782](https://github.com/zephyrproject-rtos/zephyr/issues/14782) - Build process produces hex files which will not install on BBC micro:bit
- [GitHub #14780](https://github.com/zephyrproject-rtos/zephyr/issues/14780) - USB: netusb: Unable to send maximum Ethernet packet
- [GitHub #14779](https://github.com/zephyrproject-rtos/zephyr/issues/14779) - stm32: If the memory usage is high, the flash is abnormal.
- [GitHub #14770](https://github.com/zephyrproject-rtos/zephyr/issues/14770) - samples/net/promiscuous\_mode the include file is not there
- [GitHub #14767](https://github.com/zephyrproject-rtos/zephyr/issues/14767) - ARC: hang in exception handling when CONFIG\_LOG is enabled
- [GitHub #14766](https://github.com/zephyrproject-rtos/zephyr/issues/14766) - K\_THREAD\_STACK\_BUFFER() is broken
- [GitHub #14763](https://github.com/zephyrproject-rtos/zephyr/issues/14763) - PCI debug logging cannot work with PCI-enabled NS16550
- [GitHub #14762](https://github.com/zephyrproject-rtos/zephyr/issues/14762) - elf\_helper: Call to undefined debug\_die() in AggregateTypeMember (wrong class)
- [GitHub #14753](https://github.com/zephyrproject-rtos/zephyr/issues/14753) - nrf52840\_pca10056: Get rid of leading spurious 0x00 byte in UART output
- [GitHub #14743](https://github.com/zephyrproject-rtos/zephyr/issues/14743) - Directed advertising to Android does not work
- [GitHub #14741](https://github.com/zephyrproject-rtos/zephyr/issues/14741) - Bluetooth scanning frequent resetting
- [GitHub #14714](https://github.com/zephyrproject-rtos/zephyr/issues/14714) - Mesh network traffic overflow ungraceful stop. (MMFAR Address: 0x0)
- [GitHub #14698](https://github.com/zephyrproject-rtos/zephyr/issues/14698) - USB: usb/console sample does not work for most of the boards
- [GitHub #14697](https://github.com/zephyrproject-rtos/zephyr/issues/14697) - USB: cdc\_acm\_composite sample might lose characters
- [GitHub #14693](https://github.com/zephyrproject-rtos/zephyr/issues/14693) - ARC: need test coverage for MPU stack guards
- [GitHub #14691](https://github.com/zephyrproject-rtos/zephyr/issues/14691) - samples: telnet: net shell is not working
- [GitHub #14684](https://github.com/zephyrproject-rtos/zephyr/issues/14684) - samples/net/promiscuous \_mode : Cannot set promiscuous mode for interface
- [GitHub #14665](https://github.com/zephyrproject-rtos/zephyr/issues/14665) - samples/net/zperf does not work for TCP in qemu\_x86
- [GitHub #14663](https://github.com/zephyrproject-rtos/zephyr/issues/14663) - net: echo server sends unknown packets on start
- [GitHub #14661](https://github.com/zephyrproject-rtos/zephyr/issues/14661) - samples/net/syslog\_net fails for native\_posix
- [GitHub #14658](https://github.com/zephyrproject-rtos/zephyr/issues/14658) - Disabling CONFIG\_BT\_PHY\_UPDATE makes connections stall with iOS
- [GitHub #14657](https://github.com/zephyrproject-rtos/zephyr/issues/14657) - Sample: echo\_async: setsockopt fail
- [GitHub #14654](https://github.com/zephyrproject-rtos/zephyr/issues/14654) - Samples: echo\_client: No reply packet from the server
- [GitHub #14647](https://github.com/zephyrproject-rtos/zephyr/issues/14647) - IP: Zephyr replies to broadcast ethernet packets in other subnets on the same wire
- [GitHub #14643](https://github.com/zephyrproject-rtos/zephyr/issues/14643) - ARC: tests/kernel/mem\_protect/mem\_protect/kernel.memory\_protection fails on nsim\_sem
- [GitHub #14642](https://github.com/zephyrproject-rtos/zephyr/issues/14642) - ARC: tests/posix/common/ and tests/kernel/critical time out on nsim\_sem with userspace enabled
- [GitHub #14641](https://github.com/zephyrproject-rtos/zephyr/issues/14641) - ARC: tests/kernel/critical/kernel.common times out on nsim\_em and nsim\_sem
- [GitHub #14640](https://github.com/zephyrproject-rtos/zephyr/issues/14640) - ARC: tests/cmsis\_rtos\_v2/portability.cmsis\_rtos\_v2 fails on nsim\_em and nsim\_sem
- [GitHub #14635](https://github.com/zephyrproject-rtos/zephyr/issues/14635) - bluetooth: controller: Control procedure collision with Encryption and PHY update procedure
- [GitHub #14627](https://github.com/zephyrproject-rtos/zephyr/issues/14627) - USB HID device only detected after replugging
- [GitHub #14623](https://github.com/zephyrproject-rtos/zephyr/issues/14623) - sanitycheck error when trying to run specific test
- [GitHub #14622](https://github.com/zephyrproject-rtos/zephyr/issues/14622) - net: IPv6: malformed packet in fragmented echo reply
- [GitHub #14612](https://github.com/zephyrproject-rtos/zephyr/issues/14612) - samples/net/sockets/echo\_async\_select doesn’t work for qemu\_x86 target
- [GitHub #14609](https://github.com/zephyrproject-rtos/zephyr/issues/14609) - mimxrt1050\_evk Fatal fault in thread tests/kernel/mem\_protect/stackprot Fatal fault in thread
- [GitHub #14608](https://github.com/zephyrproject-rtos/zephyr/issues/14608) - Promiscuous mode net sample cannot be build
- [GitHub #14606](https://github.com/zephyrproject-rtos/zephyr/issues/14606) - mimxrt1050\_evk tests/kernel/fp\_sharing kernel.fp\_sharing fails
- [GitHub #14605](https://github.com/zephyrproject-rtos/zephyr/issues/14605) - mimxrt1060\_evk cpp\_synchronization meets Hardware exception
- [GitHub #14603](https://github.com/zephyrproject-rtos/zephyr/issues/14603) - pyocd can’t support more board\_runner\_args
- [GitHub #14586](https://github.com/zephyrproject-rtos/zephyr/issues/14586) - Sanitycheck shows “FAILED: failed” for successful test: tests/kernel/fifo/fifo\_api/kernel.fifo
- [GitHub #14568](https://github.com/zephyrproject-rtos/zephyr/issues/14568) - I2C stm32 LL driver V2 will hang when trying again after an error occurs
- [GitHub #14566](https://github.com/zephyrproject-rtos/zephyr/issues/14566) - mcuboot doesn’t link into code-partition
- [GitHub #14556](https://github.com/zephyrproject-rtos/zephyr/issues/14556) - tests/benchmarks/timing\_info reports strange values on quark\_se\_c1000:x86, altera\_max10:nios2
- [GitHub #14554](https://github.com/zephyrproject-rtos/zephyr/issues/14554) - UP2 console no output after commit fb4f5e727b.
- [GitHub #14546](https://github.com/zephyrproject-rtos/zephyr/issues/14546) - shell compilation error when disabling CONFIG\_SHELL\_ECHO\_STATUS
- [GitHub #14542](https://github.com/zephyrproject-rtos/zephyr/issues/14542) - STM32F4XX dts\_fixup.h error
- [GitHub #14540](https://github.com/zephyrproject-rtos/zephyr/issues/14540) - kernel: message queue MACRO not compatible with C++
- [GitHub #14536](https://github.com/zephyrproject-rtos/zephyr/issues/14536) - out of bounds access in log\_backend\_rtt
- [GitHub #14523](https://github.com/zephyrproject-rtos/zephyr/issues/14523) - echo-client doesn’t close socket if echo-server is offline
- [GitHub #14510](https://github.com/zephyrproject-rtos/zephyr/issues/14510) - USB DFU sample doc outdated
- [GitHub #14508](https://github.com/zephyrproject-rtos/zephyr/issues/14508) - mempool allocator can return with no allocation even if memory is available
- [GitHub #14504](https://github.com/zephyrproject-rtos/zephyr/issues/14504) - mempool can return success if no memory was available
- [GitHub #14501](https://github.com/zephyrproject-rtos/zephyr/issues/14501) - crash in qemu\_x86\_64:tests/kernel/fifo/fifo\_usage/kernel.fifo.usage
- [GitHub #14500](https://github.com/zephyrproject-rtos/zephyr/issues/14500) - sanitycheck –coverage: stack overflows on qemu\_x86 and mps2\_an385
- [GitHub #14499](https://github.com/zephyrproject-rtos/zephyr/issues/14499) - sanitycheck –coverage on qemu\_x86: stack overflows on qemu\_x86 and mps2\_an385
- [GitHub #14496](https://github.com/zephyrproject-rtos/zephyr/issues/14496) - PyYAML 5.1 breaks DTS parsing
- [GitHub #14492](https://github.com/zephyrproject-rtos/zephyr/issues/14492) - doc: update robots.txt to exclude more old docs
- [GitHub #14479](https://github.com/zephyrproject-rtos/zephyr/issues/14479) - Regression for net\_offload API in net\_if.c?
- [GitHub #14477](https://github.com/zephyrproject-rtos/zephyr/issues/14477) - tests/crypto/tinycrypt: test\_ecc\_dh() ‘s montecarlo\_ecdh() hangs when num\_tests (1st parameter) is greater than 1
- [GitHub #14476](https://github.com/zephyrproject-rtos/zephyr/issues/14476) - quark\_d2000\_crb: samples/sensor/bmg160 runs out of ROM (CI failure)
- [GitHub #14471](https://github.com/zephyrproject-rtos/zephyr/issues/14471) - MPU fault during application startup
- [GitHub #14469](https://github.com/zephyrproject-rtos/zephyr/issues/14469) - sanitycheck failures on 96b\_carbon due to commit 75164763868ebd604904af3fdbc86845da833abc
- [GitHub #14462](https://github.com/zephyrproject-rtos/zephyr/issues/14462) - tests/kernel/threads/no-multithreading/testcase.yam: Not Booting
- [GitHub #14460](https://github.com/zephyrproject-rtos/zephyr/issues/14460) - python requirements.txt: pyocd and pyyaml conflict
- [GitHub #14454](https://github.com/zephyrproject-rtos/zephyr/issues/14454) - tests/kernel/threads/no-multithreading/: Single/Repeated delay boot banner
- [GitHub #14447](https://github.com/zephyrproject-rtos/zephyr/issues/14447) - Rename macro functions starting with two or three underscores
- [GitHub #14422](https://github.com/zephyrproject-rtos/zephyr/issues/14422) - [Coverity CID :195758]Uninitialized variables in /drivers/usb/device/usb\_dc\_nrfx.c
- [GitHub #14421](https://github.com/zephyrproject-rtos/zephyr/issues/14421) - [Coverity CID :195760]Error handling issues in /tests/net/tcp/src/main.c
- [GitHub #14420](https://github.com/zephyrproject-rtos/zephyr/issues/14420) - [Coverity CID :195768]API usage errors in /arch/x86\_64/core/xuk-stub32.c
- [GitHub #14419](https://github.com/zephyrproject-rtos/zephyr/issues/14419) - [Coverity CID :195770]Memory - illegal accesses in /drivers/ethernet/eth\_native\_posix\_adapt.c
- [GitHub #14418](https://github.com/zephyrproject-rtos/zephyr/issues/14418) - [Coverity CID :195774]API usage errors in /arch/x86\_64/core/xuk-stub32.c
- [GitHub #14417](https://github.com/zephyrproject-rtos/zephyr/issues/14417) - [Coverity CID :195786]Error handling issues in /samples/drivers/CAN/src/main.c
- [GitHub #14416](https://github.com/zephyrproject-rtos/zephyr/issues/14416) - [Coverity CID :195789]Uninitialized variables in /subsys/usb/class/netusb/function\_rndis.c
- [GitHub #14415](https://github.com/zephyrproject-rtos/zephyr/issues/14415) - [Coverity CID :195793]Insecure data handling in /drivers/counter/counter\_ll\_stm32\_rtc.c
- [GitHub #14414](https://github.com/zephyrproject-rtos/zephyr/issues/14414) - [Coverity CID :195800]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14413](https://github.com/zephyrproject-rtos/zephyr/issues/14413) - [Coverity CID :195816]Null pointer dereferences in /tests/net/dhcpv4/src/main.c
- [GitHub #14412](https://github.com/zephyrproject-rtos/zephyr/issues/14412) - [Coverity CID :195819]Null pointer dereferences in /tests/net/tcp/src/main.c
- [GitHub #14411](https://github.com/zephyrproject-rtos/zephyr/issues/14411) - [Coverity CID :195821]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14410](https://github.com/zephyrproject-rtos/zephyr/issues/14410) - [Coverity CID :195828]Memory - corruptions in /boards/posix/native\_posix/cmdline.c
- [GitHub #14409](https://github.com/zephyrproject-rtos/zephyr/issues/14409) - [Coverity CID :195835]Null pointer dereferences in /tests/net/ipv6/src/main.c
- [GitHub #14408](https://github.com/zephyrproject-rtos/zephyr/issues/14408) - [Coverity CID :195838]Memory - illegal accesses in /samples/subsys/usb/hid-cdc/src/main.c
- [GitHub #14407](https://github.com/zephyrproject-rtos/zephyr/issues/14407) - [Coverity CID :195839]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14406](https://github.com/zephyrproject-rtos/zephyr/issues/14406) - [Coverity CID :195841]Insecure data handling in /drivers/usb/device/usb\_dc\_native\_posix.c
- [GitHub #14405](https://github.com/zephyrproject-rtos/zephyr/issues/14405) - [Coverity CID :195844]Null pointer dereferences in /tests/net/mld/src/main.c
- [GitHub #14404](https://github.com/zephyrproject-rtos/zephyr/issues/14404) - [Coverity CID :195845]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14403](https://github.com/zephyrproject-rtos/zephyr/issues/14403) - [Coverity CID :195847]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14402](https://github.com/zephyrproject-rtos/zephyr/issues/14402) - [Coverity CID :195848]Error handling issues in /samples/net/sockets/echo\_async\_select/src/socket\_echo\_select.c
- [GitHub #14401](https://github.com/zephyrproject-rtos/zephyr/issues/14401) - [Coverity CID :195855]Memory - corruptions in /drivers/serial/uart\_native\_posix.c
- [GitHub #14400](https://github.com/zephyrproject-rtos/zephyr/issues/14400) - [Coverity CID :195858]Incorrect expression in /arch/posix/core/posix\_core.c
- [GitHub #14399](https://github.com/zephyrproject-rtos/zephyr/issues/14399) - [Coverity CID :195860]Null pointer dereferences in /tests/net/tcp/src/main.c
- [GitHub #14398](https://github.com/zephyrproject-rtos/zephyr/issues/14398) - [Coverity CID :195867]Memory - corruptions in /arch/posix/core/posix\_core.c
- [GitHub #14397](https://github.com/zephyrproject-rtos/zephyr/issues/14397) - [Coverity CID :195871]Integer handling issues in /drivers/counter/counter\_ll\_stm32\_rtc.c
- [GitHub #14396](https://github.com/zephyrproject-rtos/zephyr/issues/14396) - [Coverity CID :195872]Error handling issues in /drivers/serial/uart\_native\_posix.c
- [GitHub #14395](https://github.com/zephyrproject-rtos/zephyr/issues/14395) - [Coverity CID :195880]Null pointer dereferences in /tests/net/dhcpv4/src/main.c
- [GitHub #14394](https://github.com/zephyrproject-rtos/zephyr/issues/14394) - [Coverity CID :195884]Control flow issues in /arch/x86\_64/core/xuk.c
- [GitHub #14393](https://github.com/zephyrproject-rtos/zephyr/issues/14393) - [Coverity CID :195896]Memory - corruptions in /tests/net/traffic\_class/src/main.c
- [GitHub #14392](https://github.com/zephyrproject-rtos/zephyr/issues/14392) - [Coverity CID :195897]Error handling issues in /samples/net/sockets/echo\_async/src/socket\_echo.c
- [GitHub #14391](https://github.com/zephyrproject-rtos/zephyr/issues/14391) - [Coverity CID :195900]Security best practices violations in /drivers/entropy/fake\_entropy\_native\_posix.c
- [GitHub #14390](https://github.com/zephyrproject-rtos/zephyr/issues/14390) - [Coverity CID :195903]Null pointer dereferences in /tests/net/iface/src/main.c
- [GitHub #14389](https://github.com/zephyrproject-rtos/zephyr/issues/14389) - [Coverity CID :195905]Control flow issues in /arch/x86\_64/core/x86\_64.c
- [GitHub #14388](https://github.com/zephyrproject-rtos/zephyr/issues/14388) - [Coverity CID :195921]Null pointer dereferences in /tests/net/tcp/src/main.c
- [GitHub #14315](https://github.com/zephyrproject-rtos/zephyr/issues/14315) - iamcu has build issues due to lfence
- [GitHub #14313](https://github.com/zephyrproject-rtos/zephyr/issues/14313) - doc: API references such as `funcname()` aren’t creating links
- [GitHub #14310](https://github.com/zephyrproject-rtos/zephyr/issues/14310) - 64 bit print format specifiers not defined with newlib and SDK 0.10.0
- [GitHub #14297](https://github.com/zephyrproject-rtos/zephyr/issues/14297) - mimxrt1020\_evk tests/kernel/gen\_isr\_table test failure
- [GitHub #14293](https://github.com/zephyrproject-rtos/zephyr/issues/14293) - mimxrt1060\_evk tests/benchmarks/latency\_measure failed
- [GitHub #14289](https://github.com/zephyrproject-rtos/zephyr/issues/14289) - Cannot build GRUB2 boot loader image in Clear Linux
- [GitHub #14275](https://github.com/zephyrproject-rtos/zephyr/issues/14275) - [ci.foundries.io] regression 4344e27 all: Update reserved function names
- [GitHub #14265](https://github.com/zephyrproject-rtos/zephyr/issues/14265) - Bluetooth GATT descriptor discovery returns all attributes
- [GitHub #14261](https://github.com/zephyrproject-rtos/zephyr/issues/14261) - DTS file for the esp32
- [GitHub #14258](https://github.com/zephyrproject-rtos/zephyr/issues/14258) - doc: Recommended SDK version is out of date
- [GitHub #14247](https://github.com/zephyrproject-rtos/zephyr/issues/14247) - tests/net/ieee802154/crypto fails with assertion failure in subsys/net/ip/net\_if.c
- [GitHub #14246](https://github.com/zephyrproject-rtos/zephyr/issues/14246) - ./sample/bluetooth/mesh/ always issue an “HARD FALUT”
- [GitHub #14244](https://github.com/zephyrproject-rtos/zephyr/issues/14244) - tests/crypto/rand32/testcase.yaml#crypto.rand32.random\_hw\_xoroshiro.rand32: Not Booting
- [GitHub #14235](https://github.com/zephyrproject-rtos/zephyr/issues/14235) - Bluetooth connection timeout
- [GitHub #14209](https://github.com/zephyrproject-rtos/zephyr/issues/14209) - unable to flash sam\_e70\_xplained due to west errors
- [GitHub #14191](https://github.com/zephyrproject-rtos/zephyr/issues/14191) - Logger corrupts itself on rescheduling
- [GitHub #14186](https://github.com/zephyrproject-rtos/zephyr/issues/14186) - tests/cmsis\_rtos\_v1 fails on nrf boards
- [GitHub #14184](https://github.com/zephyrproject-rtos/zephyr/issues/14184) - tests/benchmarks: Stuck at delaying boot banner on quark\_se\_c1000\_ss\_board
- [GitHub #14177](https://github.com/zephyrproject-rtos/zephyr/issues/14177) - Spurious Error: “zephyr-no-west/samples/hello\_world” is not in a west installation
- [GitHub #14160](https://github.com/zephyrproject-rtos/zephyr/issues/14160) - Bluetooth API documentation - bt\_conn\_create\_slave\_le
- [GitHub #14156](https://github.com/zephyrproject-rtos/zephyr/issues/14156) - Mac OSX Documentation Update Needed
- [GitHub #14141](https://github.com/zephyrproject-rtos/zephyr/issues/14141) - USB suspend/resume on board startup
- [GitHub #14139](https://github.com/zephyrproject-rtos/zephyr/issues/14139) - nsim failed in tests/subsys/jwt/libraries\_encoding
- [GitHub #14127](https://github.com/zephyrproject-rtos/zephyr/issues/14127) - netusb: TX path doesn’t work in RNDIS driver
- [GitHub #14125](https://github.com/zephyrproject-rtos/zephyr/issues/14125) - system calls are vulnerable to Spectre V1 attacks on CPUs with speculative execution
- [GitHub #14121](https://github.com/zephyrproject-rtos/zephyr/issues/14121) - gaps between app shared memory partitions can waste a lot of space
- [GitHub #14109](https://github.com/zephyrproject-rtos/zephyr/issues/14109) - Incorrect documentation for k\_work\_\*() API
- [GitHub #14105](https://github.com/zephyrproject-rtos/zephyr/issues/14105) - Race condition in k\_delayed\_work\_submit\_to\_queue()
- [GitHub #14104](https://github.com/zephyrproject-rtos/zephyr/issues/14104) - Invalid locking in k\_delayed\_work\_submit\_to\_queue()
- [GitHub #14099](https://github.com/zephyrproject-rtos/zephyr/issues/14099) - Minnowboard doesn’t build tests/kernel/xip/
- [GitHub #14098](https://github.com/zephyrproject-rtos/zephyr/issues/14098) - Test Framework documentation issue
- [GitHub #14096](https://github.com/zephyrproject-rtos/zephyr/issues/14096) - Timeslicing is broken
- [GitHub #14093](https://github.com/zephyrproject-rtos/zephyr/issues/14093) - net: Description of net\_pkt\_skip() is not clear
- [GitHub #14087](https://github.com/zephyrproject-rtos/zephyr/issues/14087) - serial/stm32: uart\_stm32\_fifo\_fill can’t transmit data complete
- [GitHub #14084](https://github.com/zephyrproject-rtos/zephyr/issues/14084) - ADC driver subsystem has no system calls
- [GitHub #14063](https://github.com/zephyrproject-rtos/zephyr/issues/14063) - net: ipv6: Neighbor table management improvements
- [GitHub #14059](https://github.com/zephyrproject-rtos/zephyr/issues/14059) - CONFIG\_XUK\_64\_BIT\_ABI is referenced but undefined (outside of tests)
- [GitHub #14044](https://github.com/zephyrproject-rtos/zephyr/issues/14044) - BLE HID sample fails to reconnect on Windows 10 tablets - Wrong Sequence Number (follow-up)
- [GitHub #14042](https://github.com/zephyrproject-rtos/zephyr/issues/14042) - MCUboot fails to boot STM32L4 device
- [GitHub #14010](https://github.com/zephyrproject-rtos/zephyr/issues/14010) - logger: timestamp resets after 35.7 seconds on K64F
- [GitHub #14001](https://github.com/zephyrproject-rtos/zephyr/issues/14001) - drivers: modem: modem receiver is sending extra bytes around rn
- [GitHub #13984](https://github.com/zephyrproject-rtos/zephyr/issues/13984) - nucleo\_l496zg: samples: console/echo: It doesn’t echo
- [GitHub #13972](https://github.com/zephyrproject-rtos/zephyr/issues/13972) - bt\_le\_scan\_stop() before finding device results in Data Access Violation
- [GitHub #13964](https://github.com/zephyrproject-rtos/zephyr/issues/13964) - rv32m1\_vega\_ri5cy doesn’t build w/o warnings
- [GitHub #13960](https://github.com/zephyrproject-rtos/zephyr/issues/13960) - tests/kernel/lifo/lifo\_usage fails on m2gl025\_miv
- [GitHub #13956](https://github.com/zephyrproject-rtos/zephyr/issues/13956) - CI scripting doesn’t retry modifications to tests on non-default platforms
- [GitHub #13949](https://github.com/zephyrproject-rtos/zephyr/issues/13949) - tests: Ztest problem - not booting properly
- [GitHub #13943](https://github.com/zephyrproject-rtos/zephyr/issues/13943) - net: QEMU Ethernet drivers are flaky
- [GitHub #13937](https://github.com/zephyrproject-rtos/zephyr/issues/13937) - tests/net/tcp: Page fault
- [GitHub #13934](https://github.com/zephyrproject-rtos/zephyr/issues/13934) - tests/kernel/fatal: test\_fatal rv equal to TC\_FAIL
- [GitHub #13923](https://github.com/zephyrproject-rtos/zephyr/issues/13923) - app shared memory placeholders waste memory
- [GitHub #13919](https://github.com/zephyrproject-rtos/zephyr/issues/13919) - tests/crypto/mbedtls reports some errors without failing
- [GitHub #13918](https://github.com/zephyrproject-rtos/zephyr/issues/13918) - x86 memory domain configuration not always applied correctly on context switch when partitions are added
- [GitHub #13906](https://github.com/zephyrproject-rtos/zephyr/issues/13906) - posix: Recently enabled POSIX+newlib tests fail to build with gnuarmemb
- [GitHub #13890](https://github.com/zephyrproject-rtos/zephyr/issues/13890) - stm32: serial: Data is not read properly at a certain baud rate
- [GitHub #13889](https://github.com/zephyrproject-rtos/zephyr/issues/13889) - ARM: Userspace: should we have default system app partitions?
- [GitHub #13888](https://github.com/zephyrproject-rtos/zephyr/issues/13888) - [Coverity CID :190924]Integer handling issues in /subsys/net/lib/sntp/sntp.c
- [GitHub #13887](https://github.com/zephyrproject-rtos/zephyr/issues/13887) - [Coverity CID :190925]Memory - corruptions in /subsys/bluetooth/controller/hci/hci\_driver.c
- [GitHub #13886](https://github.com/zephyrproject-rtos/zephyr/issues/13886) - [Coverity CID :190926]Error handling issues in /drivers/can/stm32\_can.c
- [GitHub #13885](https://github.com/zephyrproject-rtos/zephyr/issues/13885) - [Coverity CID :190928]Error handling issues in /samples/net/sockets/echo\_async/src/socket\_echo.c
- [GitHub #13884](https://github.com/zephyrproject-rtos/zephyr/issues/13884) - [Coverity CID :190929]Integer handling issues in /tests/drivers/hwinfo/api/src/main.c
- [GitHub #13883](https://github.com/zephyrproject-rtos/zephyr/issues/13883) - [Coverity CID :190930]Integer handling issues in /samples/subsys/fs/src/main.c
- [GitHub #13882](https://github.com/zephyrproject-rtos/zephyr/issues/13882) - [Coverity CID :190931]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #13881](https://github.com/zephyrproject-rtos/zephyr/issues/13881) - [Coverity CID :190932]Control flow issues in /samples/subsys/ipc/openamp/src/main.c
- [GitHub #13880](https://github.com/zephyrproject-rtos/zephyr/issues/13880) - [Coverity CID :190933]Control flow issues in /drivers/gpio/gpio\_intel\_apl.c
- [GitHub #13879](https://github.com/zephyrproject-rtos/zephyr/issues/13879) - [Coverity CID :190934]Parse warnings in /tests/drivers/can/stm32/src/main.c
- [GitHub #13878](https://github.com/zephyrproject-rtos/zephyr/issues/13878) - [Coverity CID :190935]Parse warnings in /tests/drivers/can/stm32/src/main.c
- [GitHub #13877](https://github.com/zephyrproject-rtos/zephyr/issues/13877) - [Coverity CID :190936]Uninitialized variables in /tests/subsys/fs/nffs\_fs\_api/common/test\_performance.c
- [GitHub #13876](https://github.com/zephyrproject-rtos/zephyr/issues/13876) - [Coverity CID :190937]Incorrect expression in /tests/drivers/counter/counter\_basic\_api/src/test\_counter.c
- [GitHub #13875](https://github.com/zephyrproject-rtos/zephyr/issues/13875) - [Coverity CID :190938]Parse warnings in /tests/drivers/can/stm32/src/main.c
- [GitHub #13874](https://github.com/zephyrproject-rtos/zephyr/issues/13874) - [Coverity CID :190939]Error handling issues in /tests/subsys/fs/fat\_fs\_dual\_drive/src/test\_fat\_file.c
- [GitHub #13873](https://github.com/zephyrproject-rtos/zephyr/issues/13873) - [Coverity CID :190940]Memory - corruptions in /soc/arm/microchip\_mec/mec1701/soc.c
- [GitHub #13872](https://github.com/zephyrproject-rtos/zephyr/issues/13872) - [Coverity CID :190942]Memory - corruptions in /subsys/mgmt/smp\_shell.c
- [GitHub #13871](https://github.com/zephyrproject-rtos/zephyr/issues/13871) - [Coverity CID :190943]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #13870](https://github.com/zephyrproject-rtos/zephyr/issues/13870) - [Coverity CID :190944]Control flow issues in /subsys/usb/class/usb\_dfu.c
- [GitHub #13869](https://github.com/zephyrproject-rtos/zephyr/issues/13869) - [Coverity CID :190945]Parse warnings in /tests/drivers/can/api/src/main.c
- [GitHub #13868](https://github.com/zephyrproject-rtos/zephyr/issues/13868) - [Coverity CID :190946]Null pointer dereferences in /tests/net/utils/src/main.c
- [GitHub #13867](https://github.com/zephyrproject-rtos/zephyr/issues/13867) - [Coverity CID :190948]Null pointer dereferences in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #13866](https://github.com/zephyrproject-rtos/zephyr/issues/13866) - [Coverity CID :190949]Error handling issues in /tests/subsys/fs/nffs\_fs\_api/common/test\_append.c
- [GitHub #13865](https://github.com/zephyrproject-rtos/zephyr/issues/13865) - [Coverity CID :190950]Integer handling issues in /arch/arm/core/cortex\_m/mpu/nxp\_mpu.c
- [GitHub #13864](https://github.com/zephyrproject-rtos/zephyr/issues/13864) - [Coverity CID :190951]Control flow issues in /subsys/net/ip/net\_context.c
- [GitHub #13863](https://github.com/zephyrproject-rtos/zephyr/issues/13863) - [Coverity CID :190952]Incorrect expression in /tests/drivers/counter/counter\_basic\_api/src/test\_counter.c
- [GitHub #13862](https://github.com/zephyrproject-rtos/zephyr/issues/13862) - [Coverity CID :190953]Error handling issues in /subsys/fs/shell.c
- [GitHub #13861](https://github.com/zephyrproject-rtos/zephyr/issues/13861) - [Coverity CID :190954]Error handling issues in /subsys/bluetooth/controller/ll\_sw/nordic/lll/lll\_test.c
- [GitHub #13860](https://github.com/zephyrproject-rtos/zephyr/issues/13860) - [Coverity CID :190955]Error handling issues in /tests/subsys/fs/nffs\_fs\_api/common/nffs\_test\_utils.c
- [GitHub #13859](https://github.com/zephyrproject-rtos/zephyr/issues/13859) - [Coverity CID :190956]Error handling issues in /samples/net/sockets/can/src/main.c
- [GitHub #13858](https://github.com/zephyrproject-rtos/zephyr/issues/13858) - [Coverity CID :190957]Incorrect expression in /tests/kernel/fatal/src/main.c
- [GitHub #13857](https://github.com/zephyrproject-rtos/zephyr/issues/13857) - [Coverity CID :190958]Control flow issues in /samples/boards/96b\_argonkey/microphone/src/main.c
- [GitHub #13856](https://github.com/zephyrproject-rtos/zephyr/issues/13856) - [Coverity CID :190960]Various in /tests/subsys/fs/fcb/src/fcb\_test\_last\_of\_n.c
- [GitHub #13855](https://github.com/zephyrproject-rtos/zephyr/issues/13855) - [Coverity CID :190961]Error handling issues in /subsys/bluetooth/host/mesh/prov.c
- [GitHub #13854](https://github.com/zephyrproject-rtos/zephyr/issues/13854) - [Coverity CID :190964]Integer handling issues in /arch/arm/core/cortex\_m/mpu/nxp\_mpu.c
- [GitHub #13853](https://github.com/zephyrproject-rtos/zephyr/issues/13853) - [Coverity CID :190965]Error handling issues in /subsys/net/ip/ipv4\_autoconf.c
- [GitHub #13852](https://github.com/zephyrproject-rtos/zephyr/issues/13852) - [Coverity CID :190966]Error handling issues in /samples/net/sockets/echo\_async\_select/src/socket\_echo\_select.c
- [GitHub #13851](https://github.com/zephyrproject-rtos/zephyr/issues/13851) - [Coverity CID :190967]Incorrect expression in /tests/drivers/counter/counter\_basic\_api/src/test\_counter.c
- [GitHub #13850](https://github.com/zephyrproject-rtos/zephyr/issues/13850) - [Coverity CID :190969]Uninitialized variables in /samples/net/sockets/coap\_client/src/coap-client.c
- [GitHub #13849](https://github.com/zephyrproject-rtos/zephyr/issues/13849) - [Coverity CID :190970]Uninitialized variables in /subsys/bluetooth/shell/ll.c
- [GitHub #13848](https://github.com/zephyrproject-rtos/zephyr/issues/13848) - [Coverity CID :190971]Null pointer dereferences in /subsys/net/ip/net\_pkt.c
- [GitHub #13847](https://github.com/zephyrproject-rtos/zephyr/issues/13847) - [Coverity CID :190972]Control flow issues in /subsys/power/power.c
- [GitHub #13846](https://github.com/zephyrproject-rtos/zephyr/issues/13846) - [Coverity CID :190973]Control flow issues in /subsys/net/ip/net\_context.c
- [GitHub #13845](https://github.com/zephyrproject-rtos/zephyr/issues/13845) - [Coverity CID :190974]Integer handling issues in /subsys/net/ip/trickle.c
- [GitHub #13844](https://github.com/zephyrproject-rtos/zephyr/issues/13844) - [Coverity CID :190976]Integer handling issues in /arch/arm/core/cortex\_m/mpu/nxp\_mpu.c
- [GitHub #13843](https://github.com/zephyrproject-rtos/zephyr/issues/13843) - [Coverity CID :190977]Integer handling issues in /lib/os/printk.c
- [GitHub #13842](https://github.com/zephyrproject-rtos/zephyr/issues/13842) - [Coverity CID :190978]Control flow issues in /drivers/spi/spi\_intel.c
- [GitHub #13841](https://github.com/zephyrproject-rtos/zephyr/issues/13841) - [Coverity CID :190980]Parse warnings in /tests/drivers/can/api/src/main.c
- [GitHub #13840](https://github.com/zephyrproject-rtos/zephyr/issues/13840) - [Coverity CID :190981]Error handling issues in /subsys/fs/nffs\_fs.c
- [GitHub #13839](https://github.com/zephyrproject-rtos/zephyr/issues/13839) - [Coverity CID :190983]Incorrect expression in /tests/drivers/counter/counter\_basic\_api/src/test\_counter.c
- [GitHub #13838](https://github.com/zephyrproject-rtos/zephyr/issues/13838) - [Coverity CID :190985]Memory - illegal accesses in /arch/x86/core/x86\_mmu.c
- [GitHub #13837](https://github.com/zephyrproject-rtos/zephyr/issues/13837) - [Coverity CID :190986]Control flow issues in /subsys/net/lib/sockets/sockets\_tls.c
- [GitHub #13836](https://github.com/zephyrproject-rtos/zephyr/issues/13836) - [Coverity CID :190987]Integer handling issues in /arch/arm/core/cortex\_m/mpu/nxp\_mpu.c
- [GitHub #13835](https://github.com/zephyrproject-rtos/zephyr/issues/13835) - [Coverity CID :190989]Parse warnings in /tests/drivers/can/api/src/main.c
- [GitHub #13834](https://github.com/zephyrproject-rtos/zephyr/issues/13834) - [Coverity CID :190990]Null pointer dereferences in /subsys/net/ip/net\_pkt.c
- [GitHub #13833](https://github.com/zephyrproject-rtos/zephyr/issues/13833) - [Coverity CID :190991]Error handling issues in /subsys/bluetooth/controller/ll\_sw/ull\_conn.c
- [GitHub #13832](https://github.com/zephyrproject-rtos/zephyr/issues/13832) - [Coverity CID :190992]Null pointer dereferences in /subsys/net/ip/dhcpv4.c
- [GitHub #13831](https://github.com/zephyrproject-rtos/zephyr/issues/13831) - [Coverity CID :190993]Various in /subsys/shell/shell.c
- [GitHub #13830](https://github.com/zephyrproject-rtos/zephyr/issues/13830) - [Coverity CID :190995]Control flow issues in /subsys/net/ip/ipv6.c
- [GitHub #13829](https://github.com/zephyrproject-rtos/zephyr/issues/13829) - [Coverity CID :190996]Integer handling issues in /drivers/can/stm32\_can.c
- [GitHub #13828](https://github.com/zephyrproject-rtos/zephyr/issues/13828) - [Coverity CID :190997]Integer handling issues in /lib/os/printk.c
- [GitHub #13827](https://github.com/zephyrproject-rtos/zephyr/issues/13827) - [Coverity CID :190998]Incorrect expression in /tests/drivers/uart/uart\_async\_api/src/test\_uart\_async.c
- [GitHub #13826](https://github.com/zephyrproject-rtos/zephyr/issues/13826) - [Coverity CID :191001]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #13825](https://github.com/zephyrproject-rtos/zephyr/issues/13825) - [Coverity CID :191002]Error handling issues in /tests/net/lib/mqtt\_pubsub/src/test\_mqtt\_pubsub.c
- [GitHub #13824](https://github.com/zephyrproject-rtos/zephyr/issues/13824) - [Coverity CID :191003]Resource leaks in /samples/net/sockets/can/src/main.c
- [GitHub #13823](https://github.com/zephyrproject-rtos/zephyr/issues/13823) - tests/kernel/arm\_irq\_vector\_table: test case cannot quit displaying “isr 0 ran!”
- [GitHub #13822](https://github.com/zephyrproject-rtos/zephyr/issues/13822) - Invalid USB state: powered after cable is disconnected
- [GitHub #13821](https://github.com/zephyrproject-rtos/zephyr/issues/13821) - tests/kernel/sched/schedule\_api: Assertion failed for test\_slice\_scheduling
- [GitHub #13813](https://github.com/zephyrproject-rtos/zephyr/issues/13813) - Test suite mslab\_threadsafe fails randomly
- [GitHub #13783](https://github.com/zephyrproject-rtos/zephyr/issues/13783) - tests/kernel/mem\_protect/stackprot failure in frdm\_k64f due to limited privilege stack size
- [GitHub #13780](https://github.com/zephyrproject-rtos/zephyr/issues/13780) - mimxrt1060\_evk tests/crypto/tinycrypt\_hmac\_prng and test\_mbedtls meet Unaligned memory access
- [GitHub #13779](https://github.com/zephyrproject-rtos/zephyr/issues/13779) - mimxrt1060\_evk tests/kernel/mem\_pool/mem\_pool\_threadsafe meets Imprecise data bus error
- [GitHub #13778](https://github.com/zephyrproject-rtos/zephyr/issues/13778) - mimxrt1060\_evk tests/kernel/pending meets assert
- [GitHub #13777](https://github.com/zephyrproject-rtos/zephyr/issues/13777) - mimxrt1060\_evk tests/kernel/profiling/profiling\_api meets Illegal use of the EPSR
- [GitHub #13769](https://github.com/zephyrproject-rtos/zephyr/issues/13769) - mimxrt1060\_evk tests/kernel/fifo/fifo\_timeout and kernel/fifo/fifo\_usage meet system error
- [GitHub #13768](https://github.com/zephyrproject-rtos/zephyr/issues/13768) - mimxrt1060\_evk tests/kernel/device illegal use of the EPSR
- [GitHub #13767](https://github.com/zephyrproject-rtos/zephyr/issues/13767) - mimxrt1060\_evk tests/kernel/context and tests/kernel/critical caught system err
- [GitHub #13766](https://github.com/zephyrproject-rtos/zephyr/issues/13766) - mimxrt1060\_evk tests/kernel/fatal meet many unwanted exceptions
- [GitHub #13765](https://github.com/zephyrproject-rtos/zephyr/issues/13765) - mimxrt1060\_evk tests/kernel/workq/work\_queue meets Illegal use of the EPSR
- [GitHub #13764](https://github.com/zephyrproject-rtos/zephyr/issues/13764) - mimxrt1060\_evk test/kernel/mem\_slab/mslab\_threadsafe meets Imprecise data bus error
- [GitHub #13762](https://github.com/zephyrproject-rtos/zephyr/issues/13762) - mimxrt1060\_evk test/lib/c\_lib and test/lib/json test/lib/ringbuffer meet Unaligned memory access
- [GitHub #13754](https://github.com/zephyrproject-rtos/zephyr/issues/13754) - Error: “West version found in path does not support ‘/usr/bin/make flash’, ensure west is installed and not only the bootstrapper”
- [GitHub #13753](https://github.com/zephyrproject-rtos/zephyr/issues/13753) - \_UART\_NS16550\_PORT\_{2,3}\_ seems to be a (possibly broken) Kconfig/DTS mishmash
- [GitHub #13752](https://github.com/zephyrproject-rtos/zephyr/issues/13752) - The Arduino 101 docs tell people to set CONFIG\_UART\_QMSI\_1\_BAUDRATE, which was removed
- [GitHub #13750](https://github.com/zephyrproject-rtos/zephyr/issues/13750) - CONFIG\_SPI\_3\_NRF\_SPIS is undefined but referenced
- [GitHub #13748](https://github.com/zephyrproject-rtos/zephyr/issues/13748) - CONFIG\_SOC\_MCIMX7D\_M4 is undefined but referenced
- [GitHub #13747](https://github.com/zephyrproject-rtos/zephyr/issues/13747) - CONFIG\_NRFX\_UARTE{2-3} are undefined but referenced
- [GitHub #13735](https://github.com/zephyrproject-rtos/zephyr/issues/13735) - mimxrt1020\_evk tests/benchmarks/app\_kernel meets Illegal use of the EPSR
- [GitHub #13734](https://github.com/zephyrproject-rtos/zephyr/issues/13734) - tests/subsys/settings/fcb/src/settings\_test\_save\_unaligned.c fail with assertion failure on nrf52\_pca10040
- [GitHub #13733](https://github.com/zephyrproject-rtos/zephyr/issues/13733) - mimxrt1020\_evk samples/net/zperf meets Unaligned memory access
- [GitHub #13729](https://github.com/zephyrproject-rtos/zephyr/issues/13729) - sanitycheck –coverage failed
- [GitHub #13728](https://github.com/zephyrproject-rtos/zephyr/issues/13728) - mimxrt1020\_evk tests/subsys/logging/log\_core test\_log\_strdup\_gc meets Unaligned memory access
- [GitHub #13727](https://github.com/zephyrproject-rtos/zephyr/issues/13727) - MIMXRT1020\_EVK sample/subsys/logging/logger report unaligned memory access
- [GitHub #13716](https://github.com/zephyrproject-rtos/zephyr/issues/13716) - CAN tests don’t build
- [GitHub #13710](https://github.com/zephyrproject-rtos/zephyr/issues/13710) - Build failure when using XCC toolchain
- [GitHub #13703](https://github.com/zephyrproject-rtos/zephyr/issues/13703) - Build error w/Flash driver enabled on hexiwear kw40
- [GitHub #13701](https://github.com/zephyrproject-rtos/zephyr/issues/13701) - x86 stack check fail w/posix-lib & newlib
- [GitHub #13686](https://github.com/zephyrproject-rtos/zephyr/issues/13686) - newlib, posix-lib and xtensa/riscv (with sdk-0.9.5) don’t build cleanly
- [GitHub #13680](https://github.com/zephyrproject-rtos/zephyr/issues/13680) - XCC install directions need updating in boards/xtensa/intel\_s1000\_crb/doc/index.rst
- [GitHub #13665](https://github.com/zephyrproject-rtos/zephyr/issues/13665) - amples/subsys/usb/cdc\_acm\_composite: Stuck at “Wait for DTR”
- [GitHub #13664](https://github.com/zephyrproject-rtos/zephyr/issues/13664) - samples/subsys/usb/cdc\_acm\_composite: No output beyond “**\*** Booting Zephyr OS v1.14.0-rc- ….\*\*\*\*\*\* banner
- [GitHub #13662](https://github.com/zephyrproject-rtos/zephyr/issues/13662) - samples/subsys/usb/cdc\_acm: Stuck at “Wait for DTR”
- [GitHub #13655](https://github.com/zephyrproject-rtos/zephyr/issues/13655) - mimxrt1050\_evk test/crypto/rand32 meets Kernel Panic
- [GitHub #13654](https://github.com/zephyrproject-rtos/zephyr/issues/13654) - mimxrt1050\_evk test/kernel/mem\_protect/stack\_random fails on stack fault
- [GitHub #13642](https://github.com/zephyrproject-rtos/zephyr/issues/13642) - stack canaries don’t work with user mode threads
- [GitHub #13624](https://github.com/zephyrproject-rtos/zephyr/issues/13624) - ATMEL SAM family UART and USART - functions u(s)art\_sam\_irq\_is\_pending doesn’t respect IRQ settings
- [GitHub #13610](https://github.com/zephyrproject-rtos/zephyr/issues/13610) - kernel: Non-deterministic and very high ISR latencies
- [GitHub #13609](https://github.com/zephyrproject-rtos/zephyr/issues/13609) - samples: cfb: text is not displayed due to display\_blanking\_off()
- [GitHub #13595](https://github.com/zephyrproject-rtos/zephyr/issues/13595) - tests/kernel/stack fails to build on nios2 with new SDK 0.10.0-rc3
- [GitHub #13594](https://github.com/zephyrproject-rtos/zephyr/issues/13594) - tests/kernel/mem\_protect/mem\_protect/kernel.memory\_protection build failure on minnowboard with new SDK
- [GitHub #13585](https://github.com/zephyrproject-rtos/zephyr/issues/13585) - CONFIG\_BT\_HCI\_TX\_STACK\_SIZE is too small
- [GitHub #13584](https://github.com/zephyrproject-rtos/zephyr/issues/13584) - i.MX RT board flashing and debugging sections are out of date
- [GitHub #13572](https://github.com/zephyrproject-rtos/zephyr/issues/13572) - settings: Bluetooth: Failed parse/lookup
- [GitHub #13567](https://github.com/zephyrproject-rtos/zephyr/issues/13567) - tests/subsys/settings/fcb/base64 fails when write-block-size is 8
- [GitHub #13560](https://github.com/zephyrproject-rtos/zephyr/issues/13560) - STM32 USB: netusb: kernel crash when testing example echo\_server with nucleo\_f412zg (ECM on Windows)
- [GitHub #13550](https://github.com/zephyrproject-rtos/zephyr/issues/13550) - stm32: i2c: SSD1306 does not work due to write size limitation
- [GitHub #13547](https://github.com/zephyrproject-rtos/zephyr/issues/13547) - tests/drivers/build\_all: The Zephyr library ‘drivers\_\_adc’ was created without source files
- [GitHub #13541](https://github.com/zephyrproject-rtos/zephyr/issues/13541) - sanitycheck errors when device-testing frdm\_k64f
- [GitHub #13536](https://github.com/zephyrproject-rtos/zephyr/issues/13536) - test: tests/kernel/mem\_slab/mslab\_threadsafe fails sporadically on nrf52
- [GitHub #13522](https://github.com/zephyrproject-rtos/zephyr/issues/13522) - BT SUBSCRIBE to characteristic for Indication or WRITE to value results in kernel crash
- [GitHub #13515](https://github.com/zephyrproject-rtos/zephyr/issues/13515) - samples/net/sockets/echo doesn’t link with CONFIG\_NO\_OPTIMIZATIONS=y
- [GitHub #13514](https://github.com/zephyrproject-rtos/zephyr/issues/13514) - #stm32 creating #gpio #interrupts on 2+ pins with the same pin number failes
- [GitHub #13502](https://github.com/zephyrproject-rtos/zephyr/issues/13502) - tests/benchmarks/timing\_info: Output only consist of Delay Boot Banner
- [GitHub #13489](https://github.com/zephyrproject-rtos/zephyr/issues/13489) - frdm\_k64f test/net/tcp bus fault after test ends
- [GitHub #13484](https://github.com/zephyrproject-rtos/zephyr/issues/13484) - net: (At least) eth\_smsc911x driver is broken in the master
- [GitHub #13482](https://github.com/zephyrproject-rtos/zephyr/issues/13482) - The frdm\_k64f board resets itself periodically/A possible NXP MPU bug
- [GitHub #13481](https://github.com/zephyrproject-rtos/zephyr/issues/13481) - Regression in CI coverage for (at least) some Ethernet drivers after net\_app code removal
- [GitHub #13470](https://github.com/zephyrproject-rtos/zephyr/issues/13470) - Lack of POSIX compliance for sched\_param struct
- [GitHub #13465](https://github.com/zephyrproject-rtos/zephyr/issues/13465) - tests/lib/mem\_alloc/testcase.yaml#libraries.libc.minimal: Bus fault at test\_malloc
- [GitHub #13464](https://github.com/zephyrproject-rtos/zephyr/issues/13464) - rb.h: macro RB\_FOR\_EACH\_CONTAINER bug
- [GitHub #13463](https://github.com/zephyrproject-rtos/zephyr/issues/13463) - frdm\_kl25z samples/basic/threads Kernel Panic
- [GitHub #13462](https://github.com/zephyrproject-rtos/zephyr/issues/13462) - frdm\_kl25z samples/basic/disco meet hard fault
- [GitHub #13458](https://github.com/zephyrproject-rtos/zephyr/issues/13458) - galileo I2C bus master names aren’t getting set in the build
- [GitHub #13449](https://github.com/zephyrproject-rtos/zephyr/issues/13449) - sanitycheck failure: [nocache] build failures with sdk-ng-0.10.0
- [GitHub #13448](https://github.com/zephyrproject-rtos/zephyr/issues/13448) - OpenOCD support code version not raised on recent additions
- [GitHub #13437](https://github.com/zephyrproject-rtos/zephyr/issues/13437) - 6LoWPAN: ICMP Ping Zephyr -> Linux broken in master [regression, bisected]
- [GitHub #13434](https://github.com/zephyrproject-rtos/zephyr/issues/13434) - Aliases inside dts leads to warnings
- [GitHub #13433](https://github.com/zephyrproject-rtos/zephyr/issues/13433) - Error when rebooting the frdm\_k64f board
- [GitHub #13424](https://github.com/zephyrproject-rtos/zephyr/issues/13424) - Logger got recently slower
- [GitHub #13423](https://github.com/zephyrproject-rtos/zephyr/issues/13423) - Default logger stack size insufficient for various samples
- [GitHub #13422](https://github.com/zephyrproject-rtos/zephyr/issues/13422) - Can’t use GPIO 2, 3 and 4
- [GitHub #13421](https://github.com/zephyrproject-rtos/zephyr/issues/13421) - tests/drivers/watchdog/wdt\_basic\_api: test\_wdt\_no\_callback() repeats indefinitely
- [GitHub #13413](https://github.com/zephyrproject-rtos/zephyr/issues/13413) - x86 reports incorrect stack pointer for user mode exceptions
- [GitHub #13411](https://github.com/zephyrproject-rtos/zephyr/issues/13411) - kernel: ASSERTION FAIL [z\_spin\_lock\_valid(l)]
- [GitHub #13410](https://github.com/zephyrproject-rtos/zephyr/issues/13410) - qemu\_x86 transient build errors for mmu\_tables.o
- [GitHub #13408](https://github.com/zephyrproject-rtos/zephyr/issues/13408) - DT\_FLASH\_AREA generated seems to be different for Zephyr and MCUBootloader
- [GitHub #13397](https://github.com/zephyrproject-rtos/zephyr/issues/13397) - Function documentation is missing for BSD sockets
- [GitHub #13396](https://github.com/zephyrproject-rtos/zephyr/issues/13396) - Cannot connect to Galaxy S8 via BLE
- [GitHub #13394](https://github.com/zephyrproject-rtos/zephyr/issues/13394) - Missing Documentation for Bluetooth subsystem
- [GitHub #13384](https://github.com/zephyrproject-rtos/zephyr/issues/13384) - linking error of gettimeofday with zephyr-sdk-0.10.0-rc2
- [GitHub #13380](https://github.com/zephyrproject-rtos/zephyr/issues/13380) - sockets: ordering of send() vs. poll() when using socket API + DTLS causes a crash
- [GitHub #13378](https://github.com/zephyrproject-rtos/zephyr/issues/13378) - Missing Documentation for Networking subsystem
- [GitHub #13361](https://github.com/zephyrproject-rtos/zephyr/issues/13361) - nucleo\_f103rb blinky example cannot run
- [GitHub #13357](https://github.com/zephyrproject-rtos/zephyr/issues/13357) - Tracing hooks problem on POSIX
- [GitHub #13353](https://github.com/zephyrproject-rtos/zephyr/issues/13353) - z\_timeout\_remaining should subtract z\_clock\_elapsed
- [GitHub #13342](https://github.com/zephyrproject-rtos/zephyr/issues/13342) - arm: user thread stack overflows do not report \_NANO\_ERR\_STACK\_CHK\_FAIL
- [GitHub #13341](https://github.com/zephyrproject-rtos/zephyr/issues/13341) - arc: user thread stack overflows do not report \_NANO\_ERR\_STACK\_CHK\_FAIL
- [GitHub #13340](https://github.com/zephyrproject-rtos/zephyr/issues/13340) - NRF52 pca10040 boards open the “Flash hardware support” option, the BT Mesh example does not work properly
- [GitHub #13323](https://github.com/zephyrproject-rtos/zephyr/issues/13323) - No USB instance
- [GitHub #13320](https://github.com/zephyrproject-rtos/zephyr/issues/13320) - sanitycheck miss extra\_args: OVERLAY\_CONFIG parameter
- [GitHub #13316](https://github.com/zephyrproject-rtos/zephyr/issues/13316) - Notification enabled before connection
- [GitHub #13306](https://github.com/zephyrproject-rtos/zephyr/issues/13306) - Checking if UARTE TX complete on nRF52
- [GitHub #13301](https://github.com/zephyrproject-rtos/zephyr/issues/13301) - frdm\_k64f: samples/net/sockets/echo\_server doesn’t work
- [GitHub #13300](https://github.com/zephyrproject-rtos/zephyr/issues/13300) - NET: USB Ethernet tests were removed allowing to submit not compiling code
- [GitHub #13291](https://github.com/zephyrproject-rtos/zephyr/issues/13291) - samples/drivers/watchdog: Fatal fault in ISR
- [GitHub #13290](https://github.com/zephyrproject-rtos/zephyr/issues/13290) - samples/drivers/watchdog: Watchdog setup error
- [GitHub #13289](https://github.com/zephyrproject-rtos/zephyr/issues/13289) - tests/kernel/fifo/fifo\_timeout fails on nrf52840\_pca10056
- [GitHub #13287](https://github.com/zephyrproject-rtos/zephyr/issues/13287) - Zephyr can no longer apply DT overlays on a per-SoC basis
- [GitHub #13272](https://github.com/zephyrproject-rtos/zephyr/issues/13272) - Catch all bug for build issues with SDK 0.10.0-rc2
- [GitHub #13257](https://github.com/zephyrproject-rtos/zephyr/issues/13257) - Shell not compatible with c++
- [GitHub #13256](https://github.com/zephyrproject-rtos/zephyr/issues/13256) - UART error bitmask broken by new asynchronous UART API
- [GitHub #13255](https://github.com/zephyrproject-rtos/zephyr/issues/13255) - tests/drivers/counter/counter\_basic\_api: Kernel panic and an assertion error when you run test\_multiple\_alarms() after test\_single\_shot\_alarm\_top() failed
- [GitHub #13254](https://github.com/zephyrproject-rtos/zephyr/issues/13254) - tests/drivers/counter/counter\_basic\_api: counter failed to raise alarm after ticks limit reached
- [GitHub #13253](https://github.com/zephyrproject-rtos/zephyr/issues/13253) - tests/drivers/counter/counter\_basic\_api: nchan not equal to alarm\_cnt
- [GitHub #13251](https://github.com/zephyrproject-rtos/zephyr/issues/13251) - frdm\_k64f: samples/net/sockets/echo\_server doesn’t work
- [GitHub #13249](https://github.com/zephyrproject-rtos/zephyr/issues/13249) - Latest Zephyr HEAD results in a crash in mcuboot tree
- [GitHub #13247](https://github.com/zephyrproject-rtos/zephyr/issues/13247) - tests/drivers/counter/counter\_basic\_api: counter\_set\_top\_value() failed
- [GitHub #13245](https://github.com/zephyrproject-rtos/zephyr/issues/13245) - Including module(s):
- [GitHub #13243](https://github.com/zephyrproject-rtos/zephyr/issues/13243) - DT: error in generated\_dts\_board\_fixups.h for board: frdm\_k64f
- [GitHub #13237](https://github.com/zephyrproject-rtos/zephyr/issues/13237) - stm32 USB sanitycheck failures with sdk 0.10.0-beta2
- [GitHub #13236](https://github.com/zephyrproject-rtos/zephyr/issues/13236) - Failure tests/kernel/gen\_isr\_table on some stm32 platforms
- [GitHub #13223](https://github.com/zephyrproject-rtos/zephyr/issues/13223) - I2S transfers causes exception/crash in xtensa/Intel S1000
- [GitHub #13220](https://github.com/zephyrproject-rtos/zephyr/issues/13220) - qemu\_x86\_64 build failures
- [GitHub #13218](https://github.com/zephyrproject-rtos/zephyr/issues/13218) - tests: intel\_s1000\_crb: CONFIG\_I2C\_0\_NAME undeclared build error
- [GitHub #13211](https://github.com/zephyrproject-rtos/zephyr/issues/13211) - net/sockets: send/sendto broken when len > MTU
- [GitHub #13209](https://github.com/zephyrproject-rtos/zephyr/issues/13209) - FATAL ERROR: unknown key “posixpath” in format string “{posixpath}”
- [GitHub #13203](https://github.com/zephyrproject-rtos/zephyr/issues/13203) - drivers: wifi: simplelink: Need to translate socket family macro values
- [GitHub #13194](https://github.com/zephyrproject-rtos/zephyr/issues/13194) - soc/arm/nordic\_nrf/nrf52/soc\_power.h warning spew when CONFIG\_SYS\_POWER\_MANAGEMENT=n
- [GitHub #13192](https://github.com/zephyrproject-rtos/zephyr/issues/13192) - silabs flash\_gecko driver warning (will fail in CI)
- [GitHub #13187](https://github.com/zephyrproject-rtos/zephyr/issues/13187) - qemu\_x86\_64 leaks system headers into the build process
- [GitHub #13166](https://github.com/zephyrproject-rtos/zephyr/issues/13166) - tests/kernel/threads/dynamic\_thread test cases are failing on frdm\_k64f board
- [GitHub #13161](https://github.com/zephyrproject-rtos/zephyr/issues/13161) - QMSI drivers/counter/counter\_qmsi\_aon.c doesn’t build
- [GitHub #13147](https://github.com/zephyrproject-rtos/zephyr/issues/13147) - net: ICMPv4 echo reply packets do not use default values in the IP header
- [GitHub #13122](https://github.com/zephyrproject-rtos/zephyr/issues/13122) - build for KW40z, KW41z fails to generate isr\_tables
- [GitHub #13113](https://github.com/zephyrproject-rtos/zephyr/issues/13113) - Samples fail to build for SimpleLink when CONFIG\_XIP=n
- [GitHub #13110](https://github.com/zephyrproject-rtos/zephyr/issues/13110) - MPU fault on performing fifo operations
- [GitHub #13096](https://github.com/zephyrproject-rtos/zephyr/issues/13096) - Remove CONFIG\_X86\_PAE\_MODE from scripts/gen\_mmu\_x86.py
- [GitHub #13084](https://github.com/zephyrproject-rtos/zephyr/issues/13084) - net: Align interface numbering with POSIX/BSD/Linux
- [GitHub #13083](https://github.com/zephyrproject-rtos/zephyr/issues/13083) - Problem pairing/bonding 2nd device, whilst the first device is still connected using sample project (bluetoothperipheral)
- [GitHub #13082](https://github.com/zephyrproject-rtos/zephyr/issues/13082) - s1000 board: multiple registrations for irq error
- [GitHub #13073](https://github.com/zephyrproject-rtos/zephyr/issues/13073) - intermittent failure in tests/benchmarks/timing\_info
- [GitHub #13066](https://github.com/zephyrproject-rtos/zephyr/issues/13066) - Bug on STM32F2 USB Low Layer HAL
- [GitHub #13065](https://github.com/zephyrproject-rtos/zephyr/issues/13065) - CONFIG\_BT leads Fatal fault in ISR on esp32
- [GitHub #13051](https://github.com/zephyrproject-rtos/zephyr/issues/13051) - Two timers are expiring at one time and crashing for platform nrf52\_pca10040
- [GitHub #13050](https://github.com/zephyrproject-rtos/zephyr/issues/13050) - net: Zephyr drops TCPv4 packet with extended MAC frame size
- [GitHub #13047](https://github.com/zephyrproject-rtos/zephyr/issues/13047) - Build error while executing tests/kernel/tickless/tickless on quark\_se\_c1000\_devboard
- [GitHub #13044](https://github.com/zephyrproject-rtos/zephyr/issues/13044) - intermittent tests/kernel/workq/work\_queue failure
- [GitHub #13043](https://github.com/zephyrproject-rtos/zephyr/issues/13043) - intermittent tests/posix/common/ failure
- [GitHub #13034](https://github.com/zephyrproject-rtos/zephyr/issues/13034) - samples/bluetooth/peripheral\_hr: could not connect with reel board
- [GitHub #13025](https://github.com/zephyrproject-rtos/zephyr/issues/13025) - CAN not working on Nucleo L432KC with external transciever
- [GitHub #13014](https://github.com/zephyrproject-rtos/zephyr/issues/13014) - sanitycheck fails to generate coverage report if samples/application\_development/external\_lib is run
- [GitHub #13013](https://github.com/zephyrproject-rtos/zephyr/issues/13013) - Problem executing ‘west flash’ outside zephyr directory.
- [GitHub #13011](https://github.com/zephyrproject-rtos/zephyr/issues/13011) - tests/posix/fs/ segfaults randomly in POSIX arch
- [GitHub #13009](https://github.com/zephyrproject-rtos/zephyr/issues/13009) - Coverage broken for nrf52\_bsim
- [GitHub #13005](https://github.com/zephyrproject-rtos/zephyr/issues/13005) - syslog\_net doc error
- [GitHub #13001](https://github.com/zephyrproject-rtos/zephyr/issues/13001) - app shared memory rules in CMakeLists.txt breaks incremental builds
- [GitHub #12994](https://github.com/zephyrproject-rtos/zephyr/issues/12994) - intermittent failures in tests/net/socket/select/ on qemu\_x86
- [GitHub #12982](https://github.com/zephyrproject-rtos/zephyr/issues/12982) - net: Zephyr drops IPv4 packet with extended MAC frame size
- [GitHub #12967](https://github.com/zephyrproject-rtos/zephyr/issues/12967) - settings/fcb-backend: value size might be bigger than expected
- [GitHub #12959](https://github.com/zephyrproject-rtos/zephyr/issues/12959) - Error with cmake build “string sub-command REGEX, mode MATCH needs at least 5 arguments”
- [GitHub #12958](https://github.com/zephyrproject-rtos/zephyr/issues/12958) - Missing LwM2M protocol information in the network section of docs
- [GitHub #12957](https://github.com/zephyrproject-rtos/zephyr/issues/12957) - Need documentation for MQTT
- [GitHub #12956](https://github.com/zephyrproject-rtos/zephyr/issues/12956) - CoAP missing documentation
- [GitHub #12955](https://github.com/zephyrproject-rtos/zephyr/issues/12955) - Missing Documentation for many subsystems and features
- [GitHub #12950](https://github.com/zephyrproject-rtos/zephyr/issues/12950) - tests/kernel/workq/work\_queue\_api/kernel.workqueue fails on nsim\_em
- [GitHub #12949](https://github.com/zephyrproject-rtos/zephyr/issues/12949) - tests/benchmarks/timing\_info/benchmark.timing.userspace fails on nsim\_em
- [GitHub #12948](https://github.com/zephyrproject-rtos/zephyr/issues/12948) - tests/kernel/mem\_protect/stack\_random/kernel.memory\_protection.stack\_random fails on nsim\_em
- [GitHub #12947](https://github.com/zephyrproject-rtos/zephyr/issues/12947) - tests/benchmarks/timing\_info/benchmark.timing.default\_kernel fails on nsim\_em
- [GitHub #12946](https://github.com/zephyrproject-rtos/zephyr/issues/12946) - Zephyr/BLE stack: Problem pairing/bonding more than one device, whilst the first device is still connected.
- [GitHub #12945](https://github.com/zephyrproject-rtos/zephyr/issues/12945) - mqtt\_socket connect is hung on sam\_e70\_xplained
- [GitHub #12933](https://github.com/zephyrproject-rtos/zephyr/issues/12933) - MCUboot: high current
- [GitHub #12908](https://github.com/zephyrproject-rtos/zephyr/issues/12908) - Data allocation in sections for quark\_se is incorrect
- [GitHub #12905](https://github.com/zephyrproject-rtos/zephyr/issues/12905) - Build improperly does a partial discard of ‘const’ defined variables
- [GitHub #12900](https://github.com/zephyrproject-rtos/zephyr/issues/12900) - tests/benchmarks/timing\_info doesn’t print userspace stats
- [GitHub #12886](https://github.com/zephyrproject-rtos/zephyr/issues/12886) - Application development primer docs broken by west merge
- [GitHub #12873](https://github.com/zephyrproject-rtos/zephyr/issues/12873) - Early log panic does not print logs on shell
- [GitHub #12851](https://github.com/zephyrproject-rtos/zephyr/issues/12851) - Early log panic does not print logs
- [GitHub #12849](https://github.com/zephyrproject-rtos/zephyr/issues/12849) - i2c: frdm-k64f and mimxrt1050\_evk I2C driver will cause hardware exception if read/write to a not existing device
- [GitHub #12844](https://github.com/zephyrproject-rtos/zephyr/issues/12844) - ARC MPU version 3 is configured incorrectly
- [GitHub #12821](https://github.com/zephyrproject-rtos/zephyr/issues/12821) - When CPU\_STATS is enable with MPU\_STACK\_GUARD in DEBUG\_OPTIMIZATIONS mode, it cause a MPU FAULT / Instruction Access Violation.
- [GitHub #12820](https://github.com/zephyrproject-rtos/zephyr/issues/12820) - CONFIG\_NO\_OPTIMIZATION triggers a usage fault
- [GitHub #12813](https://github.com/zephyrproject-rtos/zephyr/issues/12813) - DTS: CONFIG\_FLASH\_BASE\_ADDRESS not being generated for SPI based Flash chip
- [GitHub #12812](https://github.com/zephyrproject-rtos/zephyr/issues/12812) - ninja flash when running without ‘west’
- [GitHub #12810](https://github.com/zephyrproject-rtos/zephyr/issues/12810) - Up Squared serial console character output corrupted
- [GitHub #12804](https://github.com/zephyrproject-rtos/zephyr/issues/12804) - tests/drivers/watchdog/wdt\_basic\_api/: wdt\_install\_timeout() failed to call callback
- [GitHub #12803](https://github.com/zephyrproject-rtos/zephyr/issues/12803) - tests/drivers/watchdog/wdt\_basic\_api/: Watchdog setup error
- [GitHub #12800](https://github.com/zephyrproject-rtos/zephyr/issues/12800) - topic-counter: nrfx\_\*: counter\_set\_top\_value inconsistent behavior
- [GitHub #12796](https://github.com/zephyrproject-rtos/zephyr/issues/12796) - USB Power Event Panic
- [GitHub #12766](https://github.com/zephyrproject-rtos/zephyr/issues/12766) - drivers: gpio: stm32: implementation silently ignores attempts to configure level interrupts
- [GitHub #12765](https://github.com/zephyrproject-rtos/zephyr/issues/12765) - drivers: gpio: intel\_apl: implementation silently ignores double-edge interrupt config
- [GitHub #12764](https://github.com/zephyrproject-rtos/zephyr/issues/12764) - drivers: gpio: cmsdk\_ahb: implementation silently ignores double-edge interrupt config
- [GitHub #12763](https://github.com/zephyrproject-rtos/zephyr/issues/12763) - drivers: gpio: sch: implementation does not configure interrupt level/edge
- [GitHub #12758](https://github.com/zephyrproject-rtos/zephyr/issues/12758) - doc: Samples and Demos documentation hierarchy looks unintentionally deep
- [GitHub #12745](https://github.com/zephyrproject-rtos/zephyr/issues/12745) - SimpleLink socket functions, on error, sometimes do not set errno and return (-1)
- [GitHub #12734](https://github.com/zephyrproject-rtos/zephyr/issues/12734) - drivers: flash: Recent change in spi\_nor.c does not let have multiple flash devs on a board.
- [GitHub #12726](https://github.com/zephyrproject-rtos/zephyr/issues/12726) - Dead loop of the kernel during Bluetooth Mesh pressure communication
- [GitHub #12724](https://github.com/zephyrproject-rtos/zephyr/issues/12724) - SPI CS: in case of multiple slaves, wrong cs-gpio is chosen in DT\_ define
- [GitHub #12708](https://github.com/zephyrproject-rtos/zephyr/issues/12708) - Drivers may call net\_pkt\_(un)ref from ISR concurrently with other code
- [GitHub #12696](https://github.com/zephyrproject-rtos/zephyr/issues/12696) - CMAKE\_EXPORT\_COMPILE\_COMMANDS is broken
- [GitHub #12688](https://github.com/zephyrproject-rtos/zephyr/issues/12688) - arm: userspace: inconsistent configuration between ARM and NXP MPU
- [GitHub #12685](https://github.com/zephyrproject-rtos/zephyr/issues/12685) - 717aa9cea7 broke use of dtc 1.4.6
- [GitHub #12657](https://github.com/zephyrproject-rtos/zephyr/issues/12657) - subsys/settings: fcb might compress areas more than once
- [GitHub #12654](https://github.com/zephyrproject-rtos/zephyr/issues/12654) - Build error while executing tests/kernel/smp on ESP32
- [GitHub #12652](https://github.com/zephyrproject-rtos/zephyr/issues/12652) - UART console is showing garbage with driver uart\_ns15560
- [GitHub #12650](https://github.com/zephyrproject-rtos/zephyr/issues/12650) - drivers: wifi: simplelink: socket() always returns fd of zero on success
- [GitHub #12640](https://github.com/zephyrproject-rtos/zephyr/issues/12640) - CONFIG\_ETH\_ENC28J60\_0\_GPIO\_SPI\_CS=y cause build error
- [GitHub #12632](https://github.com/zephyrproject-rtos/zephyr/issues/12632) - tests/drivers/adc/adc\_api/ fails on quark platforms
- [GitHub #12621](https://github.com/zephyrproject-rtos/zephyr/issues/12621) - warning about images when building docs
- [GitHub #12615](https://github.com/zephyrproject-rtos/zephyr/issues/12615) - Network documentation might miss API documentation
- [GitHub #12611](https://github.com/zephyrproject-rtos/zephyr/issues/12611) - Shell does not support network backends
- [GitHub #12609](https://github.com/zephyrproject-rtos/zephyr/issues/12609) - ext: stm32: revert fix [https://github.com/zephyrproject-rtos/zephyr/pull/8762](https://github.com/zephyrproject-rtos/zephyr/pull/8762)
- [GitHub #12594](https://github.com/zephyrproject-rtos/zephyr/issues/12594) - stm32\_min\_dev board no console output
- [GitHub #12589](https://github.com/zephyrproject-rtos/zephyr/issues/12589) - Several nRF based boards enable both I2C & SPI by default in dts at same MMIO address
- [GitHub #12574](https://github.com/zephyrproject-rtos/zephyr/issues/12574) - Bluetooth: Mesh: 2nd time commissioning configuration details (APP Key) not get saved on SoC flash
- [GitHub #12571](https://github.com/zephyrproject-rtos/zephyr/issues/12571) - No coverage reports are being generated
- [GitHub #12570](https://github.com/zephyrproject-rtos/zephyr/issues/12570) - Zephyr codebase incorrectly uses #ifdef for boolean config values
- [GitHub #12560](https://github.com/zephyrproject-rtos/zephyr/issues/12560) - Using TCP w/ wired NIC results in mismanagement of buffers due to ACK accounting error
- [GitHub #12559](https://github.com/zephyrproject-rtos/zephyr/issues/12559) - tests/kernel/mem\_pool/mem\_pool\_threadsafe/kernel.memory\_pool fails sporadically
- [GitHub #12553](https://github.com/zephyrproject-rtos/zephyr/issues/12553) - List of tests that keep failing sporadically
- [GitHub #12548](https://github.com/zephyrproject-rtos/zephyr/issues/12548) - ISR sometimes run with the MPU disabled: breaks \_\_nocache
- [GitHub #12544](https://github.com/zephyrproject-rtos/zephyr/issues/12544) - commit 2fb616e broke I2C on Nucleo F401RE + IKS01A2 shield
- [GitHub #12543](https://github.com/zephyrproject-rtos/zephyr/issues/12543) - doc: Wrong file path for code relocation sample
- [GitHub #12541](https://github.com/zephyrproject-rtos/zephyr/issues/12541) - nrf timer handling exceeds bluetooth hard realtime deadline
- [GitHub #12530](https://github.com/zephyrproject-rtos/zephyr/issues/12530) - DTS: Changes done to support QSPI memory mapped flash breaks intel\_s1000 build
- [GitHub #12528](https://github.com/zephyrproject-rtos/zephyr/issues/12528) - a bug in code
- [GitHub #12501](https://github.com/zephyrproject-rtos/zephyr/issues/12501) - nRF52: UARTE lacks pm interface
- [GitHub #12494](https://github.com/zephyrproject-rtos/zephyr/issues/12494) - Logging with CONFIG\_LOG\_IMMEDIATE=y from ISR leads to assert
- [GitHub #12488](https://github.com/zephyrproject-rtos/zephyr/issues/12488) - RedBear Nano v2 Mesh Instruction Fault
- [GitHub #12487](https://github.com/zephyrproject-rtos/zephyr/issues/12487) - Power management and RTTLogger
- [GitHub #12479](https://github.com/zephyrproject-rtos/zephyr/issues/12479) - arc: the pollution of lp\_start,lpend and lp\_count will break down the system
- [GitHub #12478](https://github.com/zephyrproject-rtos/zephyr/issues/12478) - tests/drivers/ipm/peripheral.mailbox failing sporadically on qemu\_x86\_64 (timeout)
- [GitHub #12455](https://github.com/zephyrproject-rtos/zephyr/issues/12455) - Fatal fault when openthread commissioner starts
- [GitHub #12454](https://github.com/zephyrproject-rtos/zephyr/issues/12454) - doc: Some board images are pretty big (> 1MB)
- [GitHub #12453](https://github.com/zephyrproject-rtos/zephyr/issues/12453) - nrf52 SPIM spi\_transceive function occasionally doesn’t return
- [GitHub #12449](https://github.com/zephyrproject-rtos/zephyr/issues/12449) - Existing LPN lookup in Mesh Friend Request handling
- [GitHub #12441](https://github.com/zephyrproject-rtos/zephyr/issues/12441) - include: net: Link error when inet\_pton() is used and wifi offloading is enabled
- [GitHub #12429](https://github.com/zephyrproject-rtos/zephyr/issues/12429) - Bluetooth samples not working on qemu\_x86
- [GitHub #12419](https://github.com/zephyrproject-rtos/zephyr/issues/12419) - cannot flash with segger jlink in windows environment
- [GitHub #12410](https://github.com/zephyrproject-rtos/zephyr/issues/12410) - Assert and printk not printed on RTT
- [GitHub #12409](https://github.com/zephyrproject-rtos/zephyr/issues/12409) - non-tickless kernels incorrectly advance system clock with delayed ticks
- [GitHub #12395](https://github.com/zephyrproject-rtos/zephyr/issues/12395) - Some Bluetooth samples wont run using the latest branch on some boards
- [GitHub #12369](https://github.com/zephyrproject-rtos/zephyr/issues/12369) - WDT: wdt callbacks are not getting triggerred before CPU going for a reboot
- [GitHub #12362](https://github.com/zephyrproject-rtos/zephyr/issues/12362) - BLE HID sample fails to reconnect on Windows 10 tablets
- [GitHub #12352](https://github.com/zephyrproject-rtos/zephyr/issues/12352) - intermittent kernel.mutex sanitycheck with mps2\_an385
- [GitHub #12347](https://github.com/zephyrproject-rtos/zephyr/issues/12347) - net ping shell can’t show reply
- [GitHub #12339](https://github.com/zephyrproject-rtos/zephyr/issues/12339) - drivers: nordic: usb: missing fragmentation handling for IN transfers, causing buffer overflow
- [GitHub #12329](https://github.com/zephyrproject-rtos/zephyr/issues/12329) - enable CONFIG\_NET\_DEBUG\_HTTP\_CONN cause build error
- [GitHub #12326](https://github.com/zephyrproject-rtos/zephyr/issues/12326) - [Coverity CID :158187]Control flow issues in /sanitylog/nrf52840\_pca10056/samples/net/echo\_server/test\_nrf\_openthread/zephyr/ext\_proj/Source/ot/third\_party/mbedtls/repo/library/ecp.c
- [GitHub #12325](https://github.com/zephyrproject-rtos/zephyr/issues/12325) - [Coverity CID :190377]Control flow issues in /sanitylog/nrf52840\_pca10056/samples/net/echo\_server/test\_nrf\_openthread/zephyr/ext\_proj/Source/ot/examples/platforms/utils/settings\_flash.c
- [GitHub #12324](https://github.com/zephyrproject-rtos/zephyr/issues/12324) - [Coverity CID :190380]Insecure data handling in /sanitylog/nrf52840\_pca10056/samples/net/echo\_server/test\_nrf\_openthread/zephyr/ext\_proj/Source/ot/third\_party/mbedtls/repo/library/ssl\_tls.c
- [GitHub #12323](https://github.com/zephyrproject-rtos/zephyr/issues/12323) - [Coverity CID :190383]Null pointer dereferences in /sanitylog/nrf52840\_pca10056/samples/net/echo\_server/test\_nrf\_openthread/zephyr/ext\_proj/Source/ot/third\_party/mbedtls/repo/library/ssl\_tls.c
- [GitHub #12322](https://github.com/zephyrproject-rtos/zephyr/issues/12322) - [Coverity CID :190611]Control flow issues in /drivers/usb/device/usb\_dc\_nrfx.c
- [GitHub #12321](https://github.com/zephyrproject-rtos/zephyr/issues/12321) - [Coverity CID :190612]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #12320](https://github.com/zephyrproject-rtos/zephyr/issues/12320) - [Coverity CID :190613]Integer handling issues in /subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #12319](https://github.com/zephyrproject-rtos/zephyr/issues/12319) - [Coverity CID :190614]Control flow issues in /subsys/shell/shell\_utils.c
- [GitHub #12318](https://github.com/zephyrproject-rtos/zephyr/issues/12318) - [Coverity CID :190615]Null pointer dereferences in /subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #12317](https://github.com/zephyrproject-rtos/zephyr/issues/12317) - [Coverity CID :190616]Integer handling issues in /subsys/net/lib/lwm2m/lwm2m\_engine.c
- [GitHub #12316](https://github.com/zephyrproject-rtos/zephyr/issues/12316) - [Coverity CID :190617]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #12315](https://github.com/zephyrproject-rtos/zephyr/issues/12315) - [Coverity CID :190618]Code maintainability issues in /drivers/modem/wncm14a2a.c
- [GitHub #12314](https://github.com/zephyrproject-rtos/zephyr/issues/12314) - [Coverity CID :190619]Memory - illegal accesses in /subsys/bluetooth/host/mesh/settings.c
- [GitHub #12313](https://github.com/zephyrproject-rtos/zephyr/issues/12313) - [Coverity CID :190620]Null pointer dereferences in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #12312](https://github.com/zephyrproject-rtos/zephyr/issues/12312) - [Coverity CID :190621]Memory - corruptions in /subsys/net/lib/lwm2m/lwm2m\_rw\_oma\_tlv.c
- [GitHub #12311](https://github.com/zephyrproject-rtos/zephyr/issues/12311) - [Coverity CID :190622]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_offload.c
- [GitHub #12310](https://github.com/zephyrproject-rtos/zephyr/issues/12310) - [Coverity CID :190623]Error handling issues in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #12309](https://github.com/zephyrproject-rtos/zephyr/issues/12309) - [Coverity CID :190624]Memory - corruptions in /tests/posix/fs/src/test\_fs\_file.c
- [GitHub #12308](https://github.com/zephyrproject-rtos/zephyr/issues/12308) - [Coverity CID :190625]Integer handling issues in /samples/bluetooth/peripheral/src/main.c
- [GitHub #12307](https://github.com/zephyrproject-rtos/zephyr/issues/12307) - [Coverity CID :190626]Null pointer dereferences in /subsys/net/lib/coap/coap\_sock.c
- [GitHub #12306](https://github.com/zephyrproject-rtos/zephyr/issues/12306) - [Coverity CID :190627]Incorrect expression in /samples/net/zperf/src/zperf\_tcp\_receiver.c
- [GitHub #12305](https://github.com/zephyrproject-rtos/zephyr/issues/12305) - [Coverity CID :190628]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #12304](https://github.com/zephyrproject-rtos/zephyr/issues/12304) - [Coverity CID :190629]Incorrect expression in /samples/net/zperf/src/zperf\_udp\_receiver.c
- [GitHub #12303](https://github.com/zephyrproject-rtos/zephyr/issues/12303) - [Coverity CID :190630]Null pointer dereferences in /drivers/modem/wncm14a2a.c
- [GitHub #12302](https://github.com/zephyrproject-rtos/zephyr/issues/12302) - [Coverity CID :190631]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_json.c
- [GitHub #12301](https://github.com/zephyrproject-rtos/zephyr/issues/12301) - [Coverity CID :190632]Memory - corruptions in /drivers/wifi/eswifi/eswifi\_offload.c
- [GitHub #12300](https://github.com/zephyrproject-rtos/zephyr/issues/12300) - [Coverity CID :190633]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_rw\_plain\_text.c
- [GitHub #12299](https://github.com/zephyrproject-rtos/zephyr/issues/12299) - [Coverity CID :190634]Control flow issues in /subsys/net/lib/lwm2m/lwm2m\_obj\_device.c
- [GitHub #12298](https://github.com/zephyrproject-rtos/zephyr/issues/12298) - [Coverity CID :190635]Integer handling issues in /subsys/net/lib/coap/coap\_link\_format\_sock.c
- [GitHub #12297](https://github.com/zephyrproject-rtos/zephyr/issues/12297) - [Coverity CID :190636]Incorrect expression in /samples/subsys/usb/console/src/main.c
- [GitHub #12296](https://github.com/zephyrproject-rtos/zephyr/issues/12296) - [Coverity CID :190637]Null pointer dereferences in /subsys/net/lib/lwm2m/lwm2m\_rw\_plain\_text.c
- [GitHub #12295](https://github.com/zephyrproject-rtos/zephyr/issues/12295) - [Coverity CID :190638]Control flow issues in /samples/portability/cmsis\_rtos\_v2/timer\_synchronization/src/main.c
- [GitHub #12294](https://github.com/zephyrproject-rtos/zephyr/issues/12294) - [Coverity CID :190639]Null pointer dereferences in /subsys/net/ip/route.c
- [GitHub #12293](https://github.com/zephyrproject-rtos/zephyr/issues/12293) - [Coverity CID :190640]Null pointer dereferences in /drivers/wifi/eswifi/eswifi\_core.c
- [GitHub #12292](https://github.com/zephyrproject-rtos/zephyr/issues/12292) - [Coverity CID :190641]Null pointer dereferences in /lib/cmsis\_rtos\_v2/kernel.c
- [GitHub #12291](https://github.com/zephyrproject-rtos/zephyr/issues/12291) - [Coverity CID :190642]Error handling issues in /drivers/console/telnet\_console.c
- [GitHub #12290](https://github.com/zephyrproject-rtos/zephyr/issues/12290) - [Coverity CID :190644]Memory - illegal accesses in /drivers/modem/wncm14a2a.c
- [GitHub #12282](https://github.com/zephyrproject-rtos/zephyr/issues/12282) - “make htmldocs” reports a cmake warning
- [GitHub #12274](https://github.com/zephyrproject-rtos/zephyr/issues/12274) - Assert crash in logger’s out\_func
- [GitHub #12268](https://github.com/zephyrproject-rtos/zephyr/issues/12268) - doc: nightly published AWS docs are not as generated
- [GitHub #12265](https://github.com/zephyrproject-rtos/zephyr/issues/12265) - doc: Some API documentation is not being generated
- [GitHub #12257](https://github.com/zephyrproject-rtos/zephyr/issues/12257) - The latest GNU ARM Embedded Toolchain can’t produce hex files on Windows
- [GitHub #12252](https://github.com/zephyrproject-rtos/zephyr/issues/12252) - potential non-termination of k\_mem\_pool\_alloc
- [GitHub #12250](https://github.com/zephyrproject-rtos/zephyr/issues/12250) - DTS: Inconsistencies seen for SPI node with size-cells
- [GitHub #12249](https://github.com/zephyrproject-rtos/zephyr/issues/12249) - Can’t flash CC3220 with OpenOCD
- [GitHub #12243](https://github.com/zephyrproject-rtos/zephyr/issues/12243) - Build error with I2C driver for nucleo\_f103rb: DT\_ST\_STM32\_I2C\_V1\_40005400\_BASE\_ADDRESS’ undeclared here
- [GitHub #12241](https://github.com/zephyrproject-rtos/zephyr/issues/12241) - logging: log output busy loops if log output function can not process buffer
- [GitHub #12224](https://github.com/zephyrproject-rtos/zephyr/issues/12224) - POSIX api are incompatible with arm gcc 2018q2 toolchain
- [GitHub #12203](https://github.com/zephyrproject-rtos/zephyr/issues/12203) - openthread: bind IP is randomly selected causing off-mesh communication problems
- [GitHub #12201](https://github.com/zephyrproject-rtos/zephyr/issues/12201) - Enabling CONFIG\_LOG is throwing exceptions on intel\_s1000
- [GitHub #12192](https://github.com/zephyrproject-rtos/zephyr/issues/12192) - include: \_\_assert: enabling assert causes build errors
- [GitHub #12190](https://github.com/zephyrproject-rtos/zephyr/issues/12190) - Mbedtls MBEDTLS\_PLATFORM\_STD\_SNPRINTF issue
- [GitHub #12186](https://github.com/zephyrproject-rtos/zephyr/issues/12186) - net: arp: Zephyr does not use MAC address from unicast ARP reply with wrong target MAC
- [GitHub #12179](https://github.com/zephyrproject-rtos/zephyr/issues/12179) - net: arp: Zephyr does not use MAC address from unicast ARP reply
- [GitHub #12171](https://github.com/zephyrproject-rtos/zephyr/issues/12171) - ot: ping ten times will crash
- [GitHub #12170](https://github.com/zephyrproject-rtos/zephyr/issues/12170) - logging: previous changes to dropped message notification break wifi sample debug
- [GitHub #12164](https://github.com/zephyrproject-rtos/zephyr/issues/12164) - net: icmpv4: Zephyr drops ICMPv4 packet with correct checksum 0
- [GitHub #12162](https://github.com/zephyrproject-rtos/zephyr/issues/12162) - net: icmpv4: Zephyr replies to ICMPv4 echo request with broadcast destination IPv4 address
- [GitHub #12159](https://github.com/zephyrproject-rtos/zephyr/issues/12159) - bt\_gatt\_attr\_read\_chrc: no characteristic for value
- [GitHub #12154](https://github.com/zephyrproject-rtos/zephyr/issues/12154) - 802.15.4 6LowPAN stopped working with multiple samples
- [GitHub #12147](https://github.com/zephyrproject-rtos/zephyr/issues/12147) - tests/kernel/interrupt fails on quark\_se\_c1000\_ss\_devboard
- [GitHub #12146](https://github.com/zephyrproject-rtos/zephyr/issues/12146) - tests/kernel/arm\_irq\_vector\_table fails on NRF5 boards
- [GitHub #12144](https://github.com/zephyrproject-rtos/zephyr/issues/12144) - There’s lots of references to undefined Kconfig symbols
- [GitHub #12123](https://github.com/zephyrproject-rtos/zephyr/issues/12123) - samples: cmsis\_rtos\_v1/philosophers faults with a FATAL EXCEPTION on esp32
- [GitHub #12122](https://github.com/zephyrproject-rtos/zephyr/issues/12122) - system.settings.nffs fails on NRF5 boards
- [GitHub #12120](https://github.com/zephyrproject-rtos/zephyr/issues/12120) - Can’t pair with nrf52832 running zephyr
- [GitHub #12118](https://github.com/zephyrproject-rtos/zephyr/issues/12118) - printf doesn’t work on qemu\_cortex\_m3 with newlib and arm gcc 2018q2 toolchain
- [GitHub #12092](https://github.com/zephyrproject-rtos/zephyr/issues/12092) - Default Virtual COM port on nucleo\_l4r5zi is lpuart1
- [GitHub #12091](https://github.com/zephyrproject-rtos/zephyr/issues/12091) - tests/subsys/settings/fcb/base64 fails on NRF5 boards
- [GitHub #12089](https://github.com/zephyrproject-rtos/zephyr/issues/12089) - Unexpected fault during test does not cause test failure
- [GitHub #12069](https://github.com/zephyrproject-rtos/zephyr/issues/12069) - iwdg\_stm32.c: potential failure in wdt\_set\_config()
- [GitHub #12066](https://github.com/zephyrproject-rtos/zephyr/issues/12066) - Observing a Python path Issue with Git based Compile
- [GitHub #12065](https://github.com/zephyrproject-rtos/zephyr/issues/12065) - enormous .BSS size while building tests/subsys/fs/nffs\_fs\_api
- [GitHub #12059](https://github.com/zephyrproject-rtos/zephyr/issues/12059) - kernel.memory\_protection.stack\_random fails on quark\_d2000\_crb board
- [GitHub #12058](https://github.com/zephyrproject-rtos/zephyr/issues/12058) - Lots of tests don’t honor CONFIG\_TEST\_EXTRA\_STACK\_SIZE
- [GitHub #12051](https://github.com/zephyrproject-rtos/zephyr/issues/12051) - LOG\_PANIC never returns if RTT is disconnected
- [GitHub #12045](https://github.com/zephyrproject-rtos/zephyr/issues/12045) - frdm\_k64f + shell breaks Ethernet driver
- [GitHub #12043](https://github.com/zephyrproject-rtos/zephyr/issues/12043) - logger: Invalid pointer deference in samples/subsys/logging/logger/
- [GitHub #12040](https://github.com/zephyrproject-rtos/zephyr/issues/12040) - Log messages are dropped even with huge log buffer
- [GitHub #12037](https://github.com/zephyrproject-rtos/zephyr/issues/12037) - nrf52840 ram retention example failed
- [GitHub #12033](https://github.com/zephyrproject-rtos/zephyr/issues/12033) - samples/application\_development/code\_relocation fails on mps2\_an385
- [GitHub #12029](https://github.com/zephyrproject-rtos/zephyr/issues/12029) - CONFIG\_STACK\_CANARIES doesn’t work on x86\_64
- [GitHub #12016](https://github.com/zephyrproject-rtos/zephyr/issues/12016) - Crash while disconnecting device from USB
- [GitHub #12006](https://github.com/zephyrproject-rtos/zephyr/issues/12006) - valgrind detected issue in tests/net/ipv6/
- [GitHub #11999](https://github.com/zephyrproject-rtos/zephyr/issues/11999) - CONFIG\_TEXT\_SECTION\_OFFSET doesn’t seem to work on x86
- [GitHub #11998](https://github.com/zephyrproject-rtos/zephyr/issues/11998) - intermittent failures in tests/kernel/common: test\_timeout\_order: (poll\_events[ii].state not equal to K\_POLL\_STATE\_SEM\_AVAILABLE)
- [GitHub #11989](https://github.com/zephyrproject-rtos/zephyr/issues/11989) - Reel Board mesh\_badge sample | Light sensor bug
- [GitHub #11980](https://github.com/zephyrproject-rtos/zephyr/issues/11980) - cmake: Build fails in an environment without ‘python’ binary
- [GitHub #11967](https://github.com/zephyrproject-rtos/zephyr/issues/11967) - nrfx SPI driver blocks indefinitely when transferring
- [GitHub #11961](https://github.com/zephyrproject-rtos/zephyr/issues/11961) - Python warning in process\_gperf.py
- [GitHub #11935](https://github.com/zephyrproject-rtos/zephyr/issues/11935) - Invalid usage of k\_busy\_wait()
- [GitHub #11916](https://github.com/zephyrproject-rtos/zephyr/issues/11916) - ISR table (\_sw\_isr\_table) generation is fragile and can result in corrupted binaries
- [GitHub #11914](https://github.com/zephyrproject-rtos/zephyr/issues/11914) - NXP documentation: frdm-k64f links dead
- [GitHub #11904](https://github.com/zephyrproject-rtos/zephyr/issues/11904) - blinky example can’t work on nucleo-f070rb and nucleo-f030r8 platform
- [GitHub #11894](https://github.com/zephyrproject-rtos/zephyr/issues/11894) - zephyr\_env.sh failes to correctly set $ZEPHYR\_BASE with zsh hooks bound to cd
- [GitHub #11889](https://github.com/zephyrproject-rtos/zephyr/issues/11889) - Race between SimpleLink WiFi driver FastConnect and networking app startup.
- [GitHub #11859](https://github.com/zephyrproject-rtos/zephyr/issues/11859) - sanitycheck failures on lpcxpresso54114\_m4: Error: Aborting due to non-whitelisted Kconfig warning
- [GitHub #11857](https://github.com/zephyrproject-rtos/zephyr/issues/11857) - cmake does not detect most recent python, it is fixed somehow to 3.4.x
- [GitHub #11844](https://github.com/zephyrproject-rtos/zephyr/issues/11844) - rtc\_ll\_stm32.c:232: undefined reference to ‘LL\_RCC\_LSE\_SetDriveCapability’ #stm32 #rtc
- [GitHub #11841](https://github.com/zephyrproject-rtos/zephyr/issues/11841) - Assert invoked in exception in ctrl.c line 7653 (zephyr 1.13.00)
- [GitHub #11827](https://github.com/zephyrproject-rtos/zephyr/issues/11827) - gPTP Sample Application fails on frdm\_k64f board ,and PDelay Response Receipt Timeout
- [GitHub #11815](https://github.com/zephyrproject-rtos/zephyr/issues/11815) - nxp\_kinetis: system reset leaves interrupts enabled during startup
- [GitHub #11806](https://github.com/zephyrproject-rtos/zephyr/issues/11806) - gpio\_nrf mishandles level interrupts
- [GitHub #11798](https://github.com/zephyrproject-rtos/zephyr/issues/11798) - A thread may lock a mutex before it is fully unlocked.
- [GitHub #11794](https://github.com/zephyrproject-rtos/zephyr/issues/11794) - cmake: CMake 3.13 doesn’t like INTERFACE with target\_link\_libraries
- [GitHub #11792](https://github.com/zephyrproject-rtos/zephyr/issues/11792) - drivers: nrf: UARTE interrupt driven cannot be compiled
- [GitHub #11780](https://github.com/zephyrproject-rtos/zephyr/issues/11780) - Bluetooth: Mesh: initialisation delay after disabling CONFIG\_BT\_DEBUG\_LOG
- [GitHub #11779](https://github.com/zephyrproject-rtos/zephyr/issues/11779) - watchdog sample application not being built on Nordic devices
- [GitHub #11767](https://github.com/zephyrproject-rtos/zephyr/issues/11767) - tests: counter api: Failed when MPU enabled
- [GitHub #11763](https://github.com/zephyrproject-rtos/zephyr/issues/11763) - logger drops log messages without any indication
- [GitHub #11754](https://github.com/zephyrproject-rtos/zephyr/issues/11754) - NRFX TWI driver does not compile with newlib
- [GitHub #11752](https://github.com/zephyrproject-rtos/zephyr/issues/11752) - tests/lib/ringbuffer: build error on Xtensa ESP32
- [GitHub #11749](https://github.com/zephyrproject-rtos/zephyr/issues/11749) - logging: default log thread priority is too high
- [GitHub #11744](https://github.com/zephyrproject-rtos/zephyr/issues/11744) - Regression: nNRF52840 HW dies at 8 minutes 20 seconds in various samples using IPSP
- [GitHub #11741](https://github.com/zephyrproject-rtos/zephyr/issues/11741) - mqtt\_publisher sample not working with BLE IPSP and has outdated net setup/prj configs
- [GitHub #11723](https://github.com/zephyrproject-rtos/zephyr/issues/11723) - tests/cmsis\_rtos\_v1 fails on nrf52840\_pca10056
- [GitHub #11722](https://github.com/zephyrproject-rtos/zephyr/issues/11722) - tests/kernel/timer/timer\_api fails on nrf52\_pca10040 board
- [GitHub #11721](https://github.com/zephyrproject-rtos/zephyr/issues/11721) - tests/kernel/sched/schedule\_api fails on nrf5\* boards
- [GitHub #11719](https://github.com/zephyrproject-rtos/zephyr/issues/11719) - Legacy MQTT sample app breaking
- [GitHub #11698](https://github.com/zephyrproject-rtos/zephyr/issues/11698) - net: ipv4: Zephyr replies to ICMPv4 packets with incorrect checksums
- [GitHub #11694](https://github.com/zephyrproject-rtos/zephyr/issues/11694) - system clock problem on NRF52 boards
- [GitHub #11682](https://github.com/zephyrproject-rtos/zephyr/issues/11682) - Mesh Friend replies to initial Friend Poll with “old” security credentials
- [GitHub #11675](https://github.com/zephyrproject-rtos/zephyr/issues/11675) - Cannot set UART device name in menuconfig
- [GitHub #11674](https://github.com/zephyrproject-rtos/zephyr/issues/11674) - Wrong assert condition @@zephyr/kernel/sched.c:345
- [GitHub #11651](https://github.com/zephyrproject-rtos/zephyr/issues/11651) - Time consumption is not constant during the pend and unpend operation with 0(1) pending queue
- [GitHub #11633](https://github.com/zephyrproject-rtos/zephyr/issues/11633) - logging: CONFIG\_LOG\_INPLACE\_PROCESS is not synchronous
- [GitHub #11626](https://github.com/zephyrproject-rtos/zephyr/issues/11626) - k\_busy\_wait exits early on Nordic chips
- [GitHub #11625](https://github.com/zephyrproject-rtos/zephyr/issues/11625) - Problem with printk and LOG\_ERR used with shell enabled
- [GitHub #11618](https://github.com/zephyrproject-rtos/zephyr/issues/11618) - net: icmpv4: Zephyr drops valid echo request
- [GitHub #11617](https://github.com/zephyrproject-rtos/zephyr/issues/11617) - net: ipv4: udp: broadcast delivery not supported
- [GitHub #11612](https://github.com/zephyrproject-rtos/zephyr/issues/11612) - i2c\_burst\_write on nrf51 is not a burst write
- [GitHub #11586](https://github.com/zephyrproject-rtos/zephyr/issues/11586) - mimxrt1050\_evb board: Can’t get Ethernet to work
- [GitHub #11579](https://github.com/zephyrproject-rtos/zephyr/issues/11579) - net: arp: MAC address not updated if target address is not its own
- [GitHub #11565](https://github.com/zephyrproject-rtos/zephyr/issues/11565) - gpio\_callback ambiguity in union pin vs pin\_mask
- [GitHub #11564](https://github.com/zephyrproject-rtos/zephyr/issues/11564) - Bluetooth: settings: Invalid base64 value written to flash
- [GitHub #11562](https://github.com/zephyrproject-rtos/zephyr/issues/11562) - net: arp: Zephyr does use MAC address from broadcast ARP reply
- [GitHub #11561](https://github.com/zephyrproject-rtos/zephyr/issues/11561) - Ping through net shell seems to be broken
- [GitHub #11533](https://github.com/zephyrproject-rtos/zephyr/issues/11533) - Energy-efficient BLE controller on the nRF52
- [GitHub #11532](https://github.com/zephyrproject-rtos/zephyr/issues/11532) - drivers: serial: uart\_msp432p4xx.c not compile for interrupt API
- [GitHub #11531](https://github.com/zephyrproject-rtos/zephyr/issues/11531) - Networking samples documentation updates
- [GitHub #11513](https://github.com/zephyrproject-rtos/zephyr/issues/11513) - drivers: SPI NOR: Inconsistency with flash interface docs
- [GitHub #11502](https://github.com/zephyrproject-rtos/zephyr/issues/11502) - Delayed works are not scheduled when system is busy
- [GitHub #11495](https://github.com/zephyrproject-rtos/zephyr/issues/11495) - Printk processed by logger overwrites each other
- [GitHub #11489](https://github.com/zephyrproject-rtos/zephyr/issues/11489) - net: arp: Zephyr replies to localhost address
- [GitHub #11488](https://github.com/zephyrproject-rtos/zephyr/issues/11488) - [Coverity CID :183483]Incorrect expression in /sanitylog/v2m\_beetle/tests/ztest/test/base/testing.ztest.verbose\_2/zephyr/priv\_stacks\_hash.gperf
- [GitHub #11487](https://github.com/zephyrproject-rtos/zephyr/issues/11487) - [Coverity CID :185396]Incorrect expression in /sanitylog/v2m\_beetle/tests/posix/fs/portability.posix/zephyr/kobject\_hash.gperf
- [GitHub #11486](https://github.com/zephyrproject-rtos/zephyr/issues/11486) - [Coverity CID :186197]Parse warnings in /sanitylog/lpcxpresso54114\_m4/samples/subsys/ipc/openamp/test/openamp\_remote-prefix/src/openamp\_remote-build/CMakeFiles/CheckIncludeFiles/HAVE\_FCNTL\_H.c
- [GitHub #11485](https://github.com/zephyrproject-rtos/zephyr/issues/11485) - [Coverity CID :189738]Null pointer dereferences in /subsys/net/lib/dns/llmnr\_responder.c
- [GitHub #11484](https://github.com/zephyrproject-rtos/zephyr/issues/11484) - [Coverity CID :189739]Parse warnings in /subsys/usb/class/netusb/function\_eem.c
- [GitHub #11483](https://github.com/zephyrproject-rtos/zephyr/issues/11483) - [Coverity CID :189740]Control flow issues in /samples/boards/reel\_board/mesh\_badge/src/reel\_board.c
- [GitHub #11482](https://github.com/zephyrproject-rtos/zephyr/issues/11482) - [Coverity CID :189741]Memory - illegal accesses in /samples/boards/reel\_board/mesh\_badge/src/reel\_board.c
- [GitHub #11481](https://github.com/zephyrproject-rtos/zephyr/issues/11481) - [Coverity CID :189742]Program hangs in /drivers/usb/device/usb\_dc\_sam.c
- [GitHub #11480](https://github.com/zephyrproject-rtos/zephyr/issues/11480) - [Coverity CID :189743]Incorrect expression in /drivers/usb/device/usb\_dc\_sam.c
- [GitHub #11465](https://github.com/zephyrproject-rtos/zephyr/issues/11465) - UART\_INTERRUPT\_DRIVEN broken on SOC\_SERIES\_IMX7\_M4 and SOC\_SERIES\_IMX\_6X\_M4
- [GitHub #11464](https://github.com/zephyrproject-rtos/zephyr/issues/11464) - where is PM\_CONTROL\_OS defined in Kconfig?
- [GitHub #11462](https://github.com/zephyrproject-rtos/zephyr/issues/11462) - tests: intel\_s1000: flash test will fail or erase code when booting from flash
- [GitHub #11461](https://github.com/zephyrproject-rtos/zephyr/issues/11461) - tests: intel\_s1000: build error due to offsets lib
- [GitHub #11447](https://github.com/zephyrproject-rtos/zephyr/issues/11447) - Build error for lwm2m\_client w/ modem overlay
- [GitHub #11425](https://github.com/zephyrproject-rtos/zephyr/issues/11425) - MISRA C Do not use recursions
- [GitHub #11417](https://github.com/zephyrproject-rtos/zephyr/issues/11417) - logging doesn’t log, again
- [GitHub #11409](https://github.com/zephyrproject-rtos/zephyr/issues/11409) - Device crash on BLE reconnection
- [GitHub #11394](https://github.com/zephyrproject-rtos/zephyr/issues/11394) - GPIO API: Do not blindly re-install an already installed callback
- [GitHub #11393](https://github.com/zephyrproject-rtos/zephyr/issues/11393) - printk (RTT backend) from isr can deadlock the system
- [GitHub #11390](https://github.com/zephyrproject-rtos/zephyr/issues/11390) - soc: intel\_s1000: Fix the tests for dma and i2s drivers
- [GitHub #11384](https://github.com/zephyrproject-rtos/zephyr/issues/11384) - CI ignores result of multiple test suites in one test application
- [GitHub #11383](https://github.com/zephyrproject-rtos/zephyr/issues/11383) - tests/drivers/i2s/i2s\_api failing on sam\_e70\_xplained
- [GitHub #11373](https://github.com/zephyrproject-rtos/zephyr/issues/11373) - Move STM32 RTC to new counter API
- [GitHub #11339](https://github.com/zephyrproject-rtos/zephyr/issues/11339) - zephyr stm32f4 startup freezes at startup in PRINT\_BOOT\_BANNER() #stm32 #uart #boot
- [GitHub #11329](https://github.com/zephyrproject-rtos/zephyr/issues/11329) - net: arp: Zephyr replies to multicast address cause of malfored ARP request
- [GitHub #11310](https://github.com/zephyrproject-rtos/zephyr/issues/11310) - Wifi scan crashes on disco\_l475\_iot1
- [GitHub #11301](https://github.com/zephyrproject-rtos/zephyr/issues/11301) - KW41Z crash on echo apps (ieee802154)
- [GitHub #11281](https://github.com/zephyrproject-rtos/zephyr/issues/11281) - uart shell: ring buffer usage bug
- [GitHub #11276](https://github.com/zephyrproject-rtos/zephyr/issues/11276) - nrf51\_pca10028:tests/kernel/interrupt/arch.interrupt registers IRQ 24 twice
- [GitHub #11275](https://github.com/zephyrproject-rtos/zephyr/issues/11275) - frdm\_k64f/samples/net/gptp/test: irq line 85 registered twice
- [GitHub #11268](https://github.com/zephyrproject-rtos/zephyr/issues/11268) - soc: intel\_s1000: linker section size updates
- [GitHub #11266](https://github.com/zephyrproject-rtos/zephyr/issues/11266) - intel\_s1000: usb\_hid: load/store alignment exception
- [GitHub #11260](https://github.com/zephyrproject-rtos/zephyr/issues/11260) - Detection of an MSYS environment sometimes fails
- [GitHub #11255](https://github.com/zephyrproject-rtos/zephyr/issues/11255) - Pinging sam\_e70 leads to unresponsive ethernet device at some point
- [GitHub #11250](https://github.com/zephyrproject-rtos/zephyr/issues/11250) - ‘net help’ or ‘kernel help’ shell commands lead to a fatal fault
- [GitHub #11244](https://github.com/zephyrproject-rtos/zephyr/issues/11244) - Turning on SystemView causes error
- [GitHub #11232](https://github.com/zephyrproject-rtos/zephyr/issues/11232) - nrf52: reel\_board: USB unable to send fragmented packets through Control endpoint
- [GitHub #11226](https://github.com/zephyrproject-rtos/zephyr/issues/11226) - Logging: duplicate log messages for some samples when building for qemu\_x86
- [GitHub #11202](https://github.com/zephyrproject-rtos/zephyr/issues/11202) - recent “shell: shell\_uart” commit breaks shell samples on cc3220sf
- [GitHub #11187](https://github.com/zephyrproject-rtos/zephyr/issues/11187) - cmake/toolchain/clang: selecting clang doesn’t select the correct compiler file
- [GitHub #11182](https://github.com/zephyrproject-rtos/zephyr/issues/11182) - qemu\_xtensa tests fail spuriously under sanitycheck/CI
- [GitHub #11179](https://github.com/zephyrproject-rtos/zephyr/issues/11179) - Minor Typo “dirver” in UART of Native Posix
- [GitHub #11171](https://github.com/zephyrproject-rtos/zephyr/issues/11171) - usb: nrf: usb\_nrfx is in endless loop when USB cable in not connected
- [GitHub #11170](https://github.com/zephyrproject-rtos/zephyr/issues/11170) - kernel.profiling.call\_stacks\_analyze\_idle: assertion fails on em\_starterkit\_em7d\_v22
- [GitHub #11167](https://github.com/zephyrproject-rtos/zephyr/issues/11167) - Building failing in arm cortex-m0
- [GitHub #11166](https://github.com/zephyrproject-rtos/zephyr/issues/11166) - quark\_se\_c1000\_devboard has no docs
- [GitHub #11147](https://github.com/zephyrproject-rtos/zephyr/issues/11147) - subsys: logging: rtt: undeclared macro
- [GitHub #11146](https://github.com/zephyrproject-rtos/zephyr/issues/11146) - ext: debug: segger: rtt: SEGGER\_RTT\_Init() missing return statement
- [GitHub #11136](https://github.com/zephyrproject-rtos/zephyr/issues/11136) - drivers/spi: WARNING: Unsigned expression compared with zero
- [GitHub #11135](https://github.com/zephyrproject-rtos/zephyr/issues/11135) - subsys/net/lib/: WARNING: Unsigned expression compared with zero
- [GitHub #11134](https://github.com/zephyrproject-rtos/zephyr/issues/11134) - drivers/flash/soc\_flash\_nios2\_qspi.c: WARNING: Unsigned expression compared with zero
- [GitHub #11133](https://github.com/zephyrproject-rtos/zephyr/issues/11133) - lib/posix/mqueue.c: WARNING: Unsigned expression compared with zero
- [GitHub #11129](https://github.com/zephyrproject-rtos/zephyr/issues/11129) - CONFIG\_TICKLESS\_KERNEL makes z\_clock\_set\_timeout doesn’t work
- [GitHub #11103](https://github.com/zephyrproject-rtos/zephyr/issues/11103) - The wrong Python version can be detected on Windows
- [GitHub #11102](https://github.com/zephyrproject-rtos/zephyr/issues/11102) - [Coverity CID :189504]Error handling issues in /samples/net/sockets/echo/src/socket\_echo.c
- [GitHub #11101](https://github.com/zephyrproject-rtos/zephyr/issues/11101) - [Coverity CID :189505]Error handling issues in /drivers/sensor/lis2mdl/lis2mdl\_trigger.c
- [GitHub #11100](https://github.com/zephyrproject-rtos/zephyr/issues/11100) - [Coverity CID :189506]Control flow issues in /subsys/net/ip/net\_shell.c
- [GitHub #11099](https://github.com/zephyrproject-rtos/zephyr/issues/11099) - [Coverity CID :189507]Parse warnings in /samples/drivers/flash\_shell/src/main.c
- [GitHub #11098](https://github.com/zephyrproject-rtos/zephyr/issues/11098) - [Coverity CID :189508]Control flow issues in /drivers/usb/device/usb\_dc\_nrfx.c
- [GitHub #11097](https://github.com/zephyrproject-rtos/zephyr/issues/11097) - [Coverity CID :189509]Integer handling issues in /drivers/sensor/ms5837/ms5837.c
- [GitHub #11096](https://github.com/zephyrproject-rtos/zephyr/issues/11096) - [Coverity CID :189510]Memory - corruptions in /subsys/bluetooth/host/monitor.c
- [GitHub #11095](https://github.com/zephyrproject-rtos/zephyr/issues/11095) - [Coverity CID :189511]Code maintainability issues in /subsys/settings/src/settings\_fcb.c
- [GitHub #11094](https://github.com/zephyrproject-rtos/zephyr/issues/11094) - [Coverity CID :189512]Null pointer dereferences in /subsys/logging/log\_msg.c
- [GitHub #11093](https://github.com/zephyrproject-rtos/zephyr/issues/11093) - [Coverity CID :189513]Control flow issues in /subsys/bluetooth/shell/gatt.c
- [GitHub #11092](https://github.com/zephyrproject-rtos/zephyr/issues/11092) - [Coverity CID :189514]Possible Control flow issues in /drivers/display/ssd1673.c
- [GitHub #11091](https://github.com/zephyrproject-rtos/zephyr/issues/11091) - [Coverity CID :189515]Incorrect expression in /drivers/usb/device/usb\_dc\_stm32.c
- [GitHub #11090](https://github.com/zephyrproject-rtos/zephyr/issues/11090) - [Coverity CID :189516]Null pointer dereferences in /drivers/wifi/simplelink/simplelink\_sockets.c
- [GitHub #11089](https://github.com/zephyrproject-rtos/zephyr/issues/11089) - [Coverity CID :189517]Control flow issues in /drivers/sensor/fxos8700/fxos8700.c
- [GitHub #11088](https://github.com/zephyrproject-rtos/zephyr/issues/11088) - [Coverity CID :189518]Memory - illegal accesses in /samples/boards/reel\_board/mesh\_badge/src/reel\_board.c
- [GitHub #11087](https://github.com/zephyrproject-rtos/zephyr/issues/11087) - [Coverity CID :189519]Error handling issues in /samples/net/sockets/echo/src/socket\_echo.c
- [GitHub #11086](https://github.com/zephyrproject-rtos/zephyr/issues/11086) - [Coverity CID :189520]Error handling issues in /samples/net/sockets/echo/src/socket\_echo.c
- [GitHub #11077](https://github.com/zephyrproject-rtos/zephyr/issues/11077) - Compiler warning at include/misc/util.h when building for ESP32
- [GitHub #11047](https://github.com/zephyrproject-rtos/zephyr/issues/11047) - doc: missing Doxygen generated documentation for any function which name starts with an underscore
- [GitHub #11046](https://github.com/zephyrproject-rtos/zephyr/issues/11046) - Enabling SYS\_POWER\_MANAGEMENT results in a linker error.
- [GitHub #11034](https://github.com/zephyrproject-rtos/zephyr/issues/11034) - Enabling config XTENSA\_ASM2 is causing system crash on intel\_s1000
- [GitHub #11022](https://github.com/zephyrproject-rtos/zephyr/issues/11022) - mempool allocator is broken
- [GitHub #11019](https://github.com/zephyrproject-rtos/zephyr/issues/11019) - About printk configuration
- [GitHub #11016](https://github.com/zephyrproject-rtos/zephyr/issues/11016) - nRF52840-PCA10056/59: Cannot bring up HCI0 when using HCI\_USB sample
- [GitHub #11008](https://github.com/zephyrproject-rtos/zephyr/issues/11008) - net-related logging: Don’t see the expected output + crash in logging
- [GitHub #11007](https://github.com/zephyrproject-rtos/zephyr/issues/11007) - logging: “log\_strdup pool empty!” is confusing
- [GitHub #10994](https://github.com/zephyrproject-rtos/zephyr/issues/10994) - upsquared sample gpio\_counter sample.yaml is malformatted/sanitycheck doens’t build samples/boards/up\_squared/gpio\_counter
- [GitHub #10993](https://github.com/zephyrproject-rtos/zephyr/issues/10993) - upsquared sample gpio\_counter doesnt build
- [GitHub #10990](https://github.com/zephyrproject-rtos/zephyr/issues/10990) - ext: lib: crypto: mbedTLS: warning in platform.h glue
- [GitHub #10971](https://github.com/zephyrproject-rtos/zephyr/issues/10971) - net: ipv6: Zephyr replies to ICMPv6 packets with incorrect checksums
- [GitHub #10970](https://github.com/zephyrproject-rtos/zephyr/issues/10970) - net: ipv6: Zephyr replies to malformed ICMPv6 message
- [GitHub #10967](https://github.com/zephyrproject-rtos/zephyr/issues/10967) - FRDM-K64F and MCR-20A configuration does not work
- [GitHub #10961](https://github.com/zephyrproject-rtos/zephyr/issues/10961) - net: ipv6: Zephyr replies to a packet with organization local multicast destination address
- [GitHub #10960](https://github.com/zephyrproject-rtos/zephyr/issues/10960) - net: ipv6: Zephyr replies to a packet with site-local multicast destination address
- [GitHub #10959](https://github.com/zephyrproject-rtos/zephyr/issues/10959) - net: ipv6: Zephyr replies to a packet with interface-local multicast destination
- [GitHub #10958](https://github.com/zephyrproject-rtos/zephyr/issues/10958) - net: ipv6: Zephyr replies to a packet with destination multicast with scope zero
- [GitHub #10955](https://github.com/zephyrproject-rtos/zephyr/issues/10955) - I can’t see the output using the minicom when flash on STM32F429IGT6
- [GitHub #10952](https://github.com/zephyrproject-rtos/zephyr/issues/10952) - Bluetooth Mesh: Disabling “CONFIG\_BT\_MESH\_DEBUG\_ACCESS” leads to wrong OpCode attached to sent messages
- [GitHub #10917](https://github.com/zephyrproject-rtos/zephyr/issues/10917) - Convert iwdg\_stm32 STM32 Watchdog driver to new API
- [GitHub #10916](https://github.com/zephyrproject-rtos/zephyr/issues/10916) - Convert CMSDK APB Watchdog driver to new API
- [GitHub #10914](https://github.com/zephyrproject-rtos/zephyr/issues/10914) - Convert Atmel SAM0 Watchdog driver to new API
- [GitHub #10913](https://github.com/zephyrproject-rtos/zephyr/issues/10913) - Convert Atmel SAM Watchdog driver to new API
- [GitHub #10909](https://github.com/zephyrproject-rtos/zephyr/issues/10909) - Missing stm32l433.dtsi file
- [GitHub #10899](https://github.com/zephyrproject-rtos/zephyr/issues/10899) - nRF52840 DevKit generates USB TX timeout when using HCI\_USB
- [GitHub #10894](https://github.com/zephyrproject-rtos/zephyr/issues/10894) - Add dts support to SPI slave drivers & tests
- [GitHub #10882](https://github.com/zephyrproject-rtos/zephyr/issues/10882) - Web instructions: quotes are wrong in build chain for Windows
- [GitHub #10878](https://github.com/zephyrproject-rtos/zephyr/issues/10878) - errno for error codes for key management break on newlib
- [GitHub #10845](https://github.com/zephyrproject-rtos/zephyr/issues/10845) - ext: hal: nxp: Use ARRAY\_SIZE helper macro
- [GitHub #10825](https://github.com/zephyrproject-rtos/zephyr/issues/10825) - The DesignWare SPI driver should be hidden on unsupported platforms
- [GitHub #10817](https://github.com/zephyrproject-rtos/zephyr/issues/10817) - Getting Started Guide script error
- [GitHub #10811](https://github.com/zephyrproject-rtos/zephyr/issues/10811) - crash while connecting a USB cable
- [GitHub #10803](https://github.com/zephyrproject-rtos/zephyr/issues/10803) - Compiler warning at /kernel/sched.c
- [GitHub #10801](https://github.com/zephyrproject-rtos/zephyr/issues/10801) - Compiler warning in soc/xtensa/esp32/include/\_soc\_inthandlers.h
- [GitHub #10788](https://github.com/zephyrproject-rtos/zephyr/issues/10788) - riscv\_machine\_timer driver don’t follow the spec ?
- [GitHub #10775](https://github.com/zephyrproject-rtos/zephyr/issues/10775) - Build error in zephyr.git/include/toolchain/gcc.h leading to shippable failures
- [GitHub #10772](https://github.com/zephyrproject-rtos/zephyr/issues/10772) - tests/drivers/adc/adc\_api results into build failure on nRF platforms
- [GitHub #10760](https://github.com/zephyrproject-rtos/zephyr/issues/10760) - Flash Shell compilation error without BT
- [GitHub #10758](https://github.com/zephyrproject-rtos/zephyr/issues/10758) - [Coverity CID :188881]Control flow issues in /samples/net/zperf/src/zperf\_shell.c
- [GitHub #10757](https://github.com/zephyrproject-rtos/zephyr/issues/10757) - [Coverity CID :188882]Incorrect expression in /tests/kernel/interrupt/src/nested\_irq.c
- [GitHub #10756](https://github.com/zephyrproject-rtos/zephyr/issues/10756) - [Coverity CID :188883]Memory - illegal accesses in /subsys/bluetooth/host/hci\_core.c
- [GitHub #10755](https://github.com/zephyrproject-rtos/zephyr/issues/10755) - [Coverity CID :188885]Error handling issues in /lib/ring\_buffer/ring\_buffer.c
- [GitHub #10754](https://github.com/zephyrproject-rtos/zephyr/issues/10754) - [Coverity CID :188886]Error handling issues in /tests/posix/common/src/mqueue.c
- [GitHub #10753](https://github.com/zephyrproject-rtos/zephyr/issues/10753) - [Coverity CID :188887]Error handling issues in /tests/posix/common/src/pthread.c
- [GitHub #10752](https://github.com/zephyrproject-rtos/zephyr/issues/10752) - [Coverity CID :188888]Incorrect expression in /tests/kernel/interrupt/src/nested\_irq.c
- [GitHub #10751](https://github.com/zephyrproject-rtos/zephyr/issues/10751) - [Coverity CID :188889]Memory - illegal accesses in /subsys/bluetooth/host/gatt.c
- [GitHub #10750](https://github.com/zephyrproject-rtos/zephyr/issues/10750) - [Coverity CID :188890]Insecure data handling in /drivers/watchdog/wdt\_qmsi.c
- [GitHub #10747](https://github.com/zephyrproject-rtos/zephyr/issues/10747) - tests/kernel/tickless/tickless\_concept fails on ARC boards
- [GitHub #10733](https://github.com/zephyrproject-rtos/zephyr/issues/10733) - Logger thread should be started earlier than \_init\_static\_threads() in init.c
- [GitHub #10720](https://github.com/zephyrproject-rtos/zephyr/issues/10720) - SSD1673 driver it setting a Kconfig symbol in dts\_fixup.h
- [GitHub #10707](https://github.com/zephyrproject-rtos/zephyr/issues/10707) - tests/benchmarks/latency\_measure fails on sam\_e70\_xplained
- [GitHub #10693](https://github.com/zephyrproject-rtos/zephyr/issues/10693) - samples/subsys/usb/console: Console routed to UART of no USB
- [GitHub #10685](https://github.com/zephyrproject-rtos/zephyr/issues/10685) - Missing # for else in segger conf
- [GitHub #10678](https://github.com/zephyrproject-rtos/zephyr/issues/10678) - nRF52840: hci\_usb timeout during initialization by bluez
- [GitHub #10672](https://github.com/zephyrproject-rtos/zephyr/issues/10672) - nRF52: UARTE: uart\_fifo\_fill return value unreliable
- [GitHub #10671](https://github.com/zephyrproject-rtos/zephyr/issues/10671) - Callback function le\_param\_req() is never called.
- [GitHub #10668](https://github.com/zephyrproject-rtos/zephyr/issues/10668) - nRF52832: RTT vs. Bluetooth
- [GitHub #10662](https://github.com/zephyrproject-rtos/zephyr/issues/10662) - “Quick start - Integration testing” does not work as intended.
- [GitHub #10658](https://github.com/zephyrproject-rtos/zephyr/issues/10658) - Cannot use SPI\_0 on nRF52810
- [GitHub #10649](https://github.com/zephyrproject-rtos/zephyr/issues/10649) - bug when build project which new c lib
- [GitHub #10639](https://github.com/zephyrproject-rtos/zephyr/issues/10639) - make run for native\_posix has dependency issues
- [GitHub #10636](https://github.com/zephyrproject-rtos/zephyr/issues/10636) - quark\_se is missing SPI\_DRV\_NAME symbol
- [GitHub #10635](https://github.com/zephyrproject-rtos/zephyr/issues/10635) - tests/kernel/mem\_pool/mem\_pool\_api#test\_mpool\_alloc\_timeout crashes on qemu\_riscv32
- [GitHub #10633](https://github.com/zephyrproject-rtos/zephyr/issues/10633) - tests/kernel/mem\_protect/syscall crashes on freedom\_k64f, sam\_e70\_xplained and nrf52\_pca10040
- [GitHub #10632](https://github.com/zephyrproject-rtos/zephyr/issues/10632) - tests/kernel/poll faults on freedom\_k64f, sam\_e70\_xplained and nrf52\_pca10040
- [GitHub #10623](https://github.com/zephyrproject-rtos/zephyr/issues/10623) - tests/drivers/watchdog/wdt\_basic\_api fails on Quark platforms
- [GitHub #10619](https://github.com/zephyrproject-rtos/zephyr/issues/10619) - [Zephyr] Firmware upgrade through UART [Nordic 52840 - pca 10056 Board]
- [GitHub #10617](https://github.com/zephyrproject-rtos/zephyr/issues/10617) - net: shell: Converting net and wifi shells to new shell breaks samples/net/wifi app for SimpleLink WiFi driver
- [GitHub #10611](https://github.com/zephyrproject-rtos/zephyr/issues/10611) - STM32L4 GPIOC Missing Interrupt support? (nucleo\_l476rg)
- [GitHub #10610](https://github.com/zephyrproject-rtos/zephyr/issues/10610) - i2s driver for stm still uses old logger
- [GitHub #10609](https://github.com/zephyrproject-rtos/zephyr/issues/10609) - RISC-V timer incorrectly written
- [GitHub #10600](https://github.com/zephyrproject-rtos/zephyr/issues/10600) - [Coverity CID :174409]Memory - illegal accesses in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/fs.c
- [GitHub #10599](https://github.com/zephyrproject-rtos/zephyr/issues/10599) - [Coverity CID :174410]Memory - corruptions in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/wlan.c
- [GitHub #10598](https://github.com/zephyrproject-rtos/zephyr/issues/10598) - [Coverity CID :174412]Incorrect expression in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/wlan.c
- [GitHub #10597](https://github.com/zephyrproject-rtos/zephyr/issues/10597) - [Coverity CID :174414]Error handling issues in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/driver.c
- [GitHub #10596](https://github.com/zephyrproject-rtos/zephyr/issues/10596) - [Coverity CID :174417]Code maintainability issues in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/device.c
- [GitHub #10595](https://github.com/zephyrproject-rtos/zephyr/issues/10595) - [Coverity CID :174418]Error handling issues in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/fs.c
- [GitHub #10594](https://github.com/zephyrproject-rtos/zephyr/issues/10594) - [Coverity CID :188729]Uninitialized variables in /subsys/bluetooth/shell/bt.c
- [GitHub #10593](https://github.com/zephyrproject-rtos/zephyr/issues/10593) - [Coverity CID :188730]Memory - corruptions in /drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #10592](https://github.com/zephyrproject-rtos/zephyr/issues/10592) - [Coverity CID :188731]Memory - illegal accesses in /ext/hal/ti/simplelink/source/ti/drivers/net/wifi/source/driver.c
- [GitHub #10591](https://github.com/zephyrproject-rtos/zephyr/issues/10591) - [Coverity CID :188732]Integer handling issues in /subsys/net/lib/http/http\_server.c
- [GitHub #10590](https://github.com/zephyrproject-rtos/zephyr/issues/10590) - [Coverity CID :188733]Error handling issues in /drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #10589](https://github.com/zephyrproject-rtos/zephyr/issues/10589) - [Coverity CID :188734]Control flow issues in /drivers/sensor/lis2dh/lis2dh.c
- [GitHub #10588](https://github.com/zephyrproject-rtos/zephyr/issues/10588) - [Coverity CID :188735]Uninitialized variables in /subsys/bluetooth/shell/bt.c
- [GitHub #10587](https://github.com/zephyrproject-rtos/zephyr/issues/10587) - [Coverity CID :188738]Memory - illegal accesses in /subsys/bluetooth/host/conn.c
- [GitHub #10586](https://github.com/zephyrproject-rtos/zephyr/issues/10586) - [Coverity CID :188739]Program hangs in /tests/posix/common/src/posix\_rwlock.c
- [GitHub #10585](https://github.com/zephyrproject-rtos/zephyr/issues/10585) - [Coverity CID :188740]Error handling issues in /drivers/sensor/isl29035/isl29035\_trigger.c
- [GitHub #10584](https://github.com/zephyrproject-rtos/zephyr/issues/10584) - [Coverity CID :188741]Control flow issues in /subsys/shell/shell\_utils.c
- [GitHub #10583](https://github.com/zephyrproject-rtos/zephyr/issues/10583) - [Coverity CID :188742]Incorrect expression in /subsys/net/ip/connection.c
- [GitHub #10582](https://github.com/zephyrproject-rtos/zephyr/issues/10582) - [Coverity CID :188743]Program hangs in /tests/posix/common/src/posix\_rwlock.c
- [GitHub #10581](https://github.com/zephyrproject-rtos/zephyr/issues/10581) - [Coverity CID :188744]Memory - corruptions in /drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #10580](https://github.com/zephyrproject-rtos/zephyr/issues/10580) - [Coverity CID :188745]Error handling issues in /drivers/wifi/winc1500/wifi\_winc1500.c
- [GitHub #10579](https://github.com/zephyrproject-rtos/zephyr/issues/10579) - [Coverity CID :188747]Security best practices violations in /subsys/shell/shell.c
- [GitHub #10578](https://github.com/zephyrproject-rtos/zephyr/issues/10578) - [Coverity CID :188748]Memory - corruptions in /subsys/bluetooth/host/gatt.c
- [GitHub #10577](https://github.com/zephyrproject-rtos/zephyr/issues/10577) - [Coverity CID :188749]Null pointer dereferences in /subsys/bluetooth/controller/ll\_sw/ctrl.c
- [GitHub #10576](https://github.com/zephyrproject-rtos/zephyr/issues/10576) - [Coverity CID :188750]Memory - illegal accesses in /subsys/bluetooth/shell/bt.c
- [GitHub #10575](https://github.com/zephyrproject-rtos/zephyr/issues/10575) - [Coverity CID :188752]Security best practices violations in /subsys/shell/shell.c
- [GitHub #10574](https://github.com/zephyrproject-rtos/zephyr/issues/10574) - [Coverity CID :188753]Incorrect expression in /subsys/net/ip/connection.c
- [GitHub #10573](https://github.com/zephyrproject-rtos/zephyr/issues/10573) - [Coverity CID :188754]Control flow issues in /samples/basic/userspace/shared\_mem/src/enc.c
- [GitHub #10572](https://github.com/zephyrproject-rtos/zephyr/issues/10572) - [Coverity CID :188755]Control flow issues in /subsys/shell/shell\_utils.c
- [GitHub #10571](https://github.com/zephyrproject-rtos/zephyr/issues/10571) - [Coverity CID :188756]Memory - corruptions in /drivers/sensor/lis2dh/lis2dh\_trigger.c
- [GitHub #10570](https://github.com/zephyrproject-rtos/zephyr/issues/10570) - [Coverity CID :188757]Memory - illegal accesses in /subsys/bluetooth/shell/bt.c
- [GitHub #10569](https://github.com/zephyrproject-rtos/zephyr/issues/10569) - [Coverity CID :188758]Incorrect expression in /drivers/wifi/winc1500/wifi\_winc1500.c
- [GitHub #10568](https://github.com/zephyrproject-rtos/zephyr/issues/10568) - [Coverity CID :188759]Integer handling issues in /subsys/net/l2/ethernet/gptp/gptp\_mi.c
- [GitHub #10567](https://github.com/zephyrproject-rtos/zephyr/issues/10567) - [Coverity CID :188760]Error handling issues in /drivers/wifi/winc1500/wifi\_winc1500.c
- [GitHub #10537](https://github.com/zephyrproject-rtos/zephyr/issues/10537) - nRF52 regression: random resets noted across several boards / use cases
- [GitHub #10535](https://github.com/zephyrproject-rtos/zephyr/issues/10535) - Failure on tests/posix/common/ due to uninitialized memory access
- [GitHub #10531](https://github.com/zephyrproject-rtos/zephyr/issues/10531) - Default idle thread stack sizes too small when OS controlled power management is used
- [GitHub #10524](https://github.com/zephyrproject-rtos/zephyr/issues/10524) - PM\_CONTROL\_OS doesn’t work in combination with certain I2C drivers in a single thread context
- [GitHub #10518](https://github.com/zephyrproject-rtos/zephyr/issues/10518) - drivers/modem/modem\_receiver.c needs LOG\_MODULE\_REGISTER(mdm\_receiver)
- [GitHub #10517](https://github.com/zephyrproject-rtos/zephyr/issues/10517) - Compatibility problem with increased BLE Tx buffers
- [GitHub #10515](https://github.com/zephyrproject-rtos/zephyr/issues/10515) - tests/benchmarks/timing\_info faults on ARM platforms
- [GitHub #10509](https://github.com/zephyrproject-rtos/zephyr/issues/10509) - tests/kernel/interrupt is failing on NRFx boards
- [GitHub #10508](https://github.com/zephyrproject-rtos/zephyr/issues/10508) - tests/posix/common fails randomly on all platforms
- [GitHub #10493](https://github.com/zephyrproject-rtos/zephyr/issues/10493) - native\_posix: Warnings during link on orphan sections after #10368
- [GitHub #10476](https://github.com/zephyrproject-rtos/zephyr/issues/10476) - kernel/threads/thread\_apis tests crashes on ARM boards
- [GitHub #10475](https://github.com/zephyrproject-rtos/zephyr/issues/10475) - tests/kernel/threads/dynamic\_thread test cases are failing on ARM boards
- [GitHub #10474](https://github.com/zephyrproject-rtos/zephyr/issues/10474) - tests/kernel/pipe/pipe test cases are failing on ARM boards
- [GitHub #10473](https://github.com/zephyrproject-rtos/zephyr/issues/10473) - tests/kernel/mem\_protect/mem\_protect tests are failing on ARM boards
- [GitHub #10460](https://github.com/zephyrproject-rtos/zephyr/issues/10460) - Bluetooth: settings: No space to store CCC config after successful pairing
- [GitHub #10453](https://github.com/zephyrproject-rtos/zephyr/issues/10453) - dma\_stm32 driver has been broken by commit 07ff2d5
- [GitHub #10444](https://github.com/zephyrproject-rtos/zephyr/issues/10444) - tests/subsys/logging/log\_core fails on few ARM platforms
- [GitHub #10439](https://github.com/zephyrproject-rtos/zephyr/issues/10439) - Logger calls will execute functions even though the LOG\_LEVEL is masked
- [GitHub #10428](https://github.com/zephyrproject-rtos/zephyr/issues/10428) - logging: Weird output from log\_strdup()
- [GitHub #10420](https://github.com/zephyrproject-rtos/zephyr/issues/10420) - gcc: “Exec format error” - WSL in Windows 10 1803
- [GitHub #10415](https://github.com/zephyrproject-rtos/zephyr/issues/10415) - logging: Unaligned memory access in log\_free
- [GitHub #10413](https://github.com/zephyrproject-rtos/zephyr/issues/10413) - Shell: trying to browse history freezes shell on disco\_l475\_iot1
- [GitHub #10402](https://github.com/zephyrproject-rtos/zephyr/issues/10402) - Crash with new logger and with new shell
- [GitHub #10389](https://github.com/zephyrproject-rtos/zephyr/issues/10389) - Conversion of net core to new logger breaks WiFi driver builds
- [GitHub #10382](https://github.com/zephyrproject-rtos/zephyr/issues/10382) - samples/sensor/apds9960/ results into build failure on multiple platforms.
- [GitHub #10369](https://github.com/zephyrproject-rtos/zephyr/issues/10369) - Logger crashes shell when boot banner is enabled
- [GitHub #10348](https://github.com/zephyrproject-rtos/zephyr/issues/10348) - valgrind detected issue in logger, during msg free
- [GitHub #10345](https://github.com/zephyrproject-rtos/zephyr/issues/10345) - The OpenAMP remote build is for wrong board
- [GitHub #10344](https://github.com/zephyrproject-rtos/zephyr/issues/10344) - SPI Chip Select usage is not unambiguous
- [GitHub #10329](https://github.com/zephyrproject-rtos/zephyr/issues/10329) - SystemView overflow event
- [GitHub #10320](https://github.com/zephyrproject-rtos/zephyr/issues/10320) - arm: mpu: mpu\_config and mpu\_regions to be declared/defined as const
- [GitHub #10318](https://github.com/zephyrproject-rtos/zephyr/issues/10318) - It is not documented what YAML bindings do
- [GitHub #10316](https://github.com/zephyrproject-rtos/zephyr/issues/10316) - net: sockets: Close doesn’t unblock recv
- [GitHub #10313](https://github.com/zephyrproject-rtos/zephyr/issues/10313) - net: sockets: Packets are leaked on TCP abort connection
- [GitHub #10312](https://github.com/zephyrproject-rtos/zephyr/issues/10312) - Bluetooth: settings: CCC not stored on device reset
- [GitHub #10271](https://github.com/zephyrproject-rtos/zephyr/issues/10271) - Unexpected Kconfig warnings during documentation build
- [GitHub #10243](https://github.com/zephyrproject-rtos/zephyr/issues/10243) - native\_posix linking issues under Ubuntu 18.04 after upgrade
- [GitHub #10241](https://github.com/zephyrproject-rtos/zephyr/issues/10241) - scripts/requirements.txt needs updating for west
- [GitHub #10234](https://github.com/zephyrproject-rtos/zephyr/issues/10234) - There is one too many “Shields” entry in the root Kconfig menu
- [GitHub #10231](https://github.com/zephyrproject-rtos/zephyr/issues/10231) - zephyr supported targets fail to flash with “ImportError: No module named ‘colorama’”
- [GitHub #10207](https://github.com/zephyrproject-rtos/zephyr/issues/10207) - Shell should accept either CR or LF as line delimiter
- [GitHub #10204](https://github.com/zephyrproject-rtos/zephyr/issues/10204) - net: ipv6: corrupted UDP header after forwarding over 6lo iface
- [GitHub #10195](https://github.com/zephyrproject-rtos/zephyr/issues/10195) - Shell dereferences invalid pointer when printing demo command help
- [GitHub #10192](https://github.com/zephyrproject-rtos/zephyr/issues/10192) - SHELL asserts when pressing tab
- [GitHub #10191](https://github.com/zephyrproject-rtos/zephyr/issues/10191) - The new shell uses CONSOLE kconfig options, even though it does not use CONSOLE.
- [GitHub #10190](https://github.com/zephyrproject-rtos/zephyr/issues/10190) - The new shell can only be compiled on boards with SERIAL but it does not set the dependency in its Kconfig
- [GitHub #10186](https://github.com/zephyrproject-rtos/zephyr/issues/10186) - GPIO callback disable has no effect due to \_gpio\_fire\_callbacks
- [GitHub #10164](https://github.com/zephyrproject-rtos/zephyr/issues/10164) - logger sample fails on qemu\_xtensa due to lack of backend
- [GitHub #10152](https://github.com/zephyrproject-rtos/zephyr/issues/10152) - gitlint complains of apostrophe in user name
- [GitHub #10146](https://github.com/zephyrproject-rtos/zephyr/issues/10146) - [bluetooth][PTS] Getting Connection failed to be established occasionally
- [GitHub #10143](https://github.com/zephyrproject-rtos/zephyr/issues/10143) - Why does BT\_SETTINGS require PRINTK?
- [GitHub #10137](https://github.com/zephyrproject-rtos/zephyr/issues/10137) - sample/basic/button should configure expected pin configuration
- [GitHub #10134](https://github.com/zephyrproject-rtos/zephyr/issues/10134) - sensor: vl53l0x: Warning message when building in ext/hal/st/lib/sensor/vl53l0x
- [GitHub #10130](https://github.com/zephyrproject-rtos/zephyr/issues/10130) - sanitycheck errors with “not well-formed text” warning
- [GitHub #10127](https://github.com/zephyrproject-rtos/zephyr/issues/10127) - Cannot use new shell with native\_posix
- [GitHub #10102](https://github.com/zephyrproject-rtos/zephyr/issues/10102) - /tests/subsys/logging/log\_core compilation fails on nios2 platform
- [GitHub #10096](https://github.com/zephyrproject-rtos/zephyr/issues/10096) - [Coverity CID :188167] Concurrent data access violations in /lib/posix/pthread.c
- [GitHub #10095](https://github.com/zephyrproject-rtos/zephyr/issues/10095) - [Coverity CID :188168] Concurrent data access violations in /lib/posix/pthread.c
- [GitHub #10094](https://github.com/zephyrproject-rtos/zephyr/issues/10094) - [Coverity CID :188169] Null pointer dereferences in /subsys/net/ip/rpl.c
- [GitHub #10093](https://github.com/zephyrproject-rtos/zephyr/issues/10093) - [Coverity CID :188170] Concurrent data access violations in /lib/posix/pthread.c
- [GitHub #10092](https://github.com/zephyrproject-rtos/zephyr/issues/10092) - [Coverity CID :188171] Null pointer dereferences in /lib/cmsis\_rtos\_v1/cmsis\_thread.c
- [GitHub #10091](https://github.com/zephyrproject-rtos/zephyr/issues/10091) - [Coverity CID :188172] Null pointer dereferences in /subsys/net/ip/route.c
- [GitHub #10090](https://github.com/zephyrproject-rtos/zephyr/issues/10090) - [Coverity CID :188173] Null pointer dereferences in /subsys/net/ip/route.c
- [GitHub #10089](https://github.com/zephyrproject-rtos/zephyr/issues/10089) - [Coverity CID :188174] Control flow issues in /tests/crypto/mbedtls/src/mbedtls.c
- [GitHub #10058](https://github.com/zephyrproject-rtos/zephyr/issues/10058) - The test mem\_pool\_threadsafe sporadically hangs forever
- [GitHub #10055](https://github.com/zephyrproject-rtos/zephyr/issues/10055) - nRF52: MPU Fault issue
- [GitHub #10054](https://github.com/zephyrproject-rtos/zephyr/issues/10054) - Logger thread spins forever if there is no backend
- [GitHub #10043](https://github.com/zephyrproject-rtos/zephyr/issues/10043) - RISCv32 qemu configuration does not work with upstream qemu
- [GitHub #10038](https://github.com/zephyrproject-rtos/zephyr/issues/10038) - Inversed logic in fade\_led sample for nRF boards
- [GitHub #10037](https://github.com/zephyrproject-rtos/zephyr/issues/10037) - fade\_led sample doesn’t work with pwm\_nrfx driver
- [GitHub #10035](https://github.com/zephyrproject-rtos/zephyr/issues/10035) - nrfx PWM driver breaking API contract
- [GitHub #10034](https://github.com/zephyrproject-rtos/zephyr/issues/10034) - Possible regression of #8815 (“Nordic: Directly accessing GPIOTE might create unstable firmware”…)
- [GitHub #10028](https://github.com/zephyrproject-rtos/zephyr/issues/10028) - MCUBoot using W25Q SPI Flash not working (use of Zephyr semaphore)
- [GitHub #10026](https://github.com/zephyrproject-rtos/zephyr/issues/10026) - undefined reference to ‘\_\_log\_current\_const\_data\_get’ when using LOG\_MODULE\_DECLARE
- [GitHub #10013](https://github.com/zephyrproject-rtos/zephyr/issues/10013) - MISRA C - Review the use of memcpy, memcmp and memmove
- [GitHub #10012](https://github.com/zephyrproject-rtos/zephyr/issues/10012) - MISRA-C Do not use feature from stdarg.h
- [GitHub #10003](https://github.com/zephyrproject-rtos/zephyr/issues/10003) - Bluetooth: Identity creation is incomplete through vendor HCI
- [GitHub #9993](https://github.com/zephyrproject-rtos/zephyr/issues/9993) - Few error codes in POSIX API implementation is not supported
- [GitHub #9992](https://github.com/zephyrproject-rtos/zephyr/issues/9992) - cmake compiler cache failures in CI
- [GitHub #9975](https://github.com/zephyrproject-rtos/zephyr/issues/9975) - tests/lib/mem\_alloc fails to build on Arduino Due after SoC move
- [GitHub #9972](https://github.com/zephyrproject-rtos/zephyr/issues/9972) - Porting to a new architecture needs to be documented
- [GitHub #9971](https://github.com/zephyrproject-rtos/zephyr/issues/9971) - doc: DT: use-prop-name is not documented
- [GitHub #9970](https://github.com/zephyrproject-rtos/zephyr/issues/9970) - Native posix port drivers need to be documented
- [GitHub #9960](https://github.com/zephyrproject-rtos/zephyr/issues/9960) - Stack check test fails - qemu\_x86:tests/kernel/fatal/kernel.common.stack\_protection
- [GitHub #9956](https://github.com/zephyrproject-rtos/zephyr/issues/9956) - Build failed when CONFIG\_STM32\_ARM\_MPU\_ENABLE=y
- [GitHub #9954](https://github.com/zephyrproject-rtos/zephyr/issues/9954) - samples/hello\_world build failed on Windows/MSYS
- [GitHub #9953](https://github.com/zephyrproject-rtos/zephyr/issues/9953) - wrong behavior in pthread\_barrier\_wait()
- [GitHub #9949](https://github.com/zephyrproject-rtos/zephyr/issues/9949) - Make West launcher scripts in mainline zephyr compatible with multi- and mono-repo
- [GitHub #9936](https://github.com/zephyrproject-rtos/zephyr/issues/9936) - docs: Ring Buffers docs are hidden away under unexpected title
- [GitHub #9935](https://github.com/zephyrproject-rtos/zephyr/issues/9935) - sockets: Connect always binds the context to the default interface
- [GitHub #9932](https://github.com/zephyrproject-rtos/zephyr/issues/9932) - Invalid documentation link in README.rst
- [GitHub #9926](https://github.com/zephyrproject-rtos/zephyr/issues/9926) - samples/net/sockets/echo\_client/server: No docs for testing TLS mode
- [GitHub #9924](https://github.com/zephyrproject-rtos/zephyr/issues/9924) - Segger Systemview + newlib does not compile
- [GitHub #9922](https://github.com/zephyrproject-rtos/zephyr/issues/9922) - Networking: Neighbour Discovery may be breaking an ongoing UDP Transmission
- [GitHub #9912](https://github.com/zephyrproject-rtos/zephyr/issues/9912) - Group posix tests
- [GitHub #9901](https://github.com/zephyrproject-rtos/zephyr/issues/9901) - Default nrfx PWM interrupt prio results in assert
- [GitHub #9892](https://github.com/zephyrproject-rtos/zephyr/issues/9892) - MISRA C Avoid dynamic memory allocation
- [GitHub #9879](https://github.com/zephyrproject-rtos/zephyr/issues/9879) - Portability: Arithmetic on void pointers
- [GitHub #9867](https://github.com/zephyrproject-rtos/zephyr/issues/9867) - Bluetooth LESC debug keys support (BT\_USE\_DEBUG\_KEYS) is broken
- [GitHub #9861](https://github.com/zephyrproject-rtos/zephyr/issues/9861) - samples/subsys/usb/hid/ test hangs on quark\_se\_c1000\_devboard
- [GitHub #9849](https://github.com/zephyrproject-rtos/zephyr/issues/9849) - samples/drivers/i2c fails with error writing to FRAM sensor
- [GitHub #9843](https://github.com/zephyrproject-rtos/zephyr/issues/9843) - tests/kernel/sched/deadline fails on NRF5x boards
- [GitHub #9830](https://github.com/zephyrproject-rtos/zephyr/issues/9830) - ASSERTION FAILURE : /tests/drivers/adc/adc\_api fails on arduino\_101 and quark\_se\_c1000 platforms
- [GitHub #9816](https://github.com/zephyrproject-rtos/zephyr/issues/9816) - DHT driver fetch fail
- [GitHub #9812](https://github.com/zephyrproject-rtos/zephyr/issues/9812) - drivers: eth: gmac: Fix incorrect cache coherency handling code
- [GitHub #9777](https://github.com/zephyrproject-rtos/zephyr/issues/9777) - tests/kernel/mem\_pool/mem\_pool\_api:mpool\_alloc\_timeout crashes on qemu\_riscv32 with boot delay
- [GitHub #9767](https://github.com/zephyrproject-rtos/zephyr/issues/9767) - [Coverity CID :187903] Uninitialized variables in /subsys/fs/nvs/nvs.c
- [GitHub #9765](https://github.com/zephyrproject-rtos/zephyr/issues/9765) - [Coverity CID :187905] Incorrect expression in /arch/arc/core/thread.c
- [GitHub #9763](https://github.com/zephyrproject-rtos/zephyr/issues/9763) - samples/net/http\_client: Failed to send Head requrest
- [GitHub #9749](https://github.com/zephyrproject-rtos/zephyr/issues/9749) - NRF52 : NFFS file system : use of write function returns 0 but fails
- [GitHub #9743](https://github.com/zephyrproject-rtos/zephyr/issues/9743) - tests/posix/fs crashes with BUS FAULT on nRF52
- [GitHub #9741](https://github.com/zephyrproject-rtos/zephyr/issues/9741) - tests/kernel/spinlock:kernel.multiprocessing.spinlock\_bounce crashing on ESP32
- [GitHub #9720](https://github.com/zephyrproject-rtos/zephyr/issues/9720) - samplesbluetoothmesh\_demo crash with real payload
- [GitHub #9708](https://github.com/zephyrproject-rtos/zephyr/issues/9708) - tests/kernel/tickless/tickless\_concept fails on nRF5x with 1000msec boot delay
- [GitHub #9704](https://github.com/zephyrproject-rtos/zephyr/issues/9704) - tests/lib/mem\_alloc/testcase.yaml#libraries.libc.newlib @ minnowboard:x86 results into exception
- [GitHub #9703](https://github.com/zephyrproject-rtos/zephyr/issues/9703) - tests/kernel/threads/no-multithreading: kernel.threads.no-multithreading failing on nrf52\_pca10040 and qemu\_x86 with boot delay
- [GitHub #9695](https://github.com/zephyrproject-rtos/zephyr/issues/9695) - Deprecated configurations around ‘SPI\_CS\_GPIO’
- [GitHub #9689](https://github.com/zephyrproject-rtos/zephyr/issues/9689) - Multiple tests are failing on sam\_e70\_xplained once the cache is enabled
- [GitHub #9666](https://github.com/zephyrproject-rtos/zephyr/issues/9666) - tests/benchmarks/timing\_info/testcase.yaml#benchmark.timing.default\_kernel crashes on Arduino 101 / ARC
- [GitHub #9656](https://github.com/zephyrproject-rtos/zephyr/issues/9656) - tests/kernel/fp\_sharing failing on sam\_e70\_xplained
- [GitHub #9653](https://github.com/zephyrproject-rtos/zephyr/issues/9653) - tests/lib/mem\_alloc/testcase.yaml#libraries.libc.newlib @ esp32:xtensa BUILD failed
- [GitHub #9651](https://github.com/zephyrproject-rtos/zephyr/issues/9651) - [Shell\_module@mimxrt1050\_evk](mailto:Shell_module%40mimxrt1050_evk) runs failure on R1.13\_RC1
- [GitHub #9650](https://github.com/zephyrproject-rtos/zephyr/issues/9650) - [latency\_measure@mimxrt1050\_evk](mailto:latency_measure%40mimxrt1050_evk) meets hard fault for R1.13 RC1
- [GitHub #9590](https://github.com/zephyrproject-rtos/zephyr/issues/9590) - Template with C linkage in util.h:41
- [GitHub #9587](https://github.com/zephyrproject-rtos/zephyr/issues/9587) - System stack usage analysis code seems to be broken
- [GitHub #9582](https://github.com/zephyrproject-rtos/zephyr/issues/9582) - Cannot find g++ when CONFIG\_CPLUSPLUS is set to y
- [GitHub #9560](https://github.com/zephyrproject-rtos/zephyr/issues/9560) - Failed test: mem\_protect/usespace failed in nsim\_sem and em\_starterkit\_em7d\_v22
- [GitHub #9510](https://github.com/zephyrproject-rtos/zephyr/issues/9510) - zephyr/doc/security/security-overview.rst needs update
- [GitHub #9509](https://github.com/zephyrproject-rtos/zephyr/issues/9509) - Unable to upload firmware over serial with mcumgr
- [GitHub #9498](https://github.com/zephyrproject-rtos/zephyr/issues/9498) - Invalid argument saved on IRQ\_CONNECT
- [GitHub #9463](https://github.com/zephyrproject-rtos/zephyr/issues/9463) - bt\_le\_scan\_start Fails with Error -5 after 128 scan start/stop cycles
- [GitHub #9432](https://github.com/zephyrproject-rtos/zephyr/issues/9432) - Overriding ‘LOG\_LEVEL’ could crash the firmware
- [GitHub #9411](https://github.com/zephyrproject-rtos/zephyr/issues/9411) - checkpatch.pl generates warning messages during execution for tests/kernel/static\_idt/src/main.c
- [GitHub #9340](https://github.com/zephyrproject-rtos/zephyr/issues/9340) - Failed test: kernel.common.errno.thread\_context on em\_starterkit\_em7d\_v22 and minnowboard
- [GitHub #9290](https://github.com/zephyrproject-rtos/zephyr/issues/9290) - [Coverity CID :187325] Control flow issues in /samples/boards/nrf52/mesh/onoff\_level\_lighting\_vnd\_app/src/mesh/device\_composition.c
- [GitHub #9289](https://github.com/zephyrproject-rtos/zephyr/issues/9289) - [Coverity CID :187326] Control flow issues in /samples/boards/nrf52/mesh/onoff\_level\_lighting\_vnd\_app/src/mesh/device\_composition.c
- [GitHub #9174](https://github.com/zephyrproject-rtos/zephyr/issues/9174) - STM32L4 I2C read polling hang on NACK in stm32\_i2c\_msg\_read()
- [GitHub #9076](https://github.com/zephyrproject-rtos/zephyr/issues/9076) - doc: correct SMP server sample imgtool.py sign usage
- [GitHub #9043](https://github.com/zephyrproject-rtos/zephyr/issues/9043) - New logging subsystem’s timestamps wrap a little before the 3-minute mark
- [GitHub #9015](https://github.com/zephyrproject-rtos/zephyr/issues/9015) - eth\_sam\_gmac driver (and BOARD=sam\_e70\_xplained using it) sets unduly high memory requirements on the IP stack overall
- [GitHub #9003](https://github.com/zephyrproject-rtos/zephyr/issues/9003) - [Coverity CID :187062] Incorrect expression in /samples/net/sockets/echo\_server/src/udp.c
- [GitHub #8999](https://github.com/zephyrproject-rtos/zephyr/issues/8999) - [Coverity CID :187067] Memory - corruptions in /subsys/logging/log\_output.c
- [GitHub #8988](https://github.com/zephyrproject-rtos/zephyr/issues/8988) - [Coverity CID :187079] Integer handling issues in /subsys/net/l2/ethernet/gptp/gptp.c
- [GitHub #8979](https://github.com/zephyrproject-rtos/zephyr/issues/8979) - Failed test: tests/subsys/dfu/mcuboot/dfu.bank\_erase failing on nrf52840\_pca10056
- [GitHub #8915](https://github.com/zephyrproject-rtos/zephyr/issues/8915) - STM32 I2C hang
- [GitHub #8914](https://github.com/zephyrproject-rtos/zephyr/issues/8914) - Failed test: net.app.no-ipv6 (/tests/net/app/) on sam\_e70\_xplained
- [GitHub #8869](https://github.com/zephyrproject-rtos/zephyr/issues/8869) - uart: Problems with interrupt-driven UART in QEMU and some hw boards
- [GitHub #8838](https://github.com/zephyrproject-rtos/zephyr/issues/8838) - hello\_world not working on frdm\_k64f/qemu\_cortex\_m3 with newlib and arm gcc embedded 2018q2
- [GitHub #8810](https://github.com/zephyrproject-rtos/zephyr/issues/8810) - Cannot flash board stm32f4\_disco
- [GitHub #8804](https://github.com/zephyrproject-rtos/zephyr/issues/8804) - esp32 cannot get character from UART port
- [GitHub #8796](https://github.com/zephyrproject-rtos/zephyr/issues/8796) - Bluetooth: controller: assert on conn update in slave role under max. throughput usecases
- [GitHub #8789](https://github.com/zephyrproject-rtos/zephyr/issues/8789) - tests/ztest/test/mock fails to complete on max10/nios2
- [GitHub #8746](https://github.com/zephyrproject-rtos/zephyr/issues/8746) - net\_app DTLS Client net/pkt ERR log when doing handshake
- [GitHub #8684](https://github.com/zephyrproject-rtos/zephyr/issues/8684) - driver: i2c\_mcux: unable to perform more than one write transfer like i2c\_burst\_write
- [GitHub #8683](https://github.com/zephyrproject-rtos/zephyr/issues/8683) - issue with nrf52840\_pca10040 and peripheral sample
- [GitHub #8631](https://github.com/zephyrproject-rtos/zephyr/issues/8631) - memory leak in mbedtls using net\_app DTLS client
- [GitHub #8614](https://github.com/zephyrproject-rtos/zephyr/issues/8614) - cmake: Zephyr wrapped functions does not allow keywords on zephyr\_link\_libraries
- [GitHub #8470](https://github.com/zephyrproject-rtos/zephyr/issues/8470) - Broken Arduino 101 Bluetooth Core flashing
- [GitHub #8409](https://github.com/zephyrproject-rtos/zephyr/issues/8409) - Pin interrupt not handled when two pin ints fires in quick succession
- [GitHub #8376](https://github.com/zephyrproject-rtos/zephyr/issues/8376) - DTS: ‘boolean’ type value was defined as True, not 1
- [GitHub #8374](https://github.com/zephyrproject-rtos/zephyr/issues/8374) - arm: core: cortex\_m: wrongly assumes double precision FPU on Cortex-M7
- [GitHub #8348](https://github.com/zephyrproject-rtos/zephyr/issues/8348) - sanitycheck: localized make error message leads to false “passed” result
- [GitHub #8339](https://github.com/zephyrproject-rtos/zephyr/issues/8339) - crypto: drivers use cipher\_aead\_pkt.tag differently
- [GitHub #8208](https://github.com/zephyrproject-rtos/zephyr/issues/8208) - tests/crypto/ecc\_dsa hangs in montecarlo\_signverify test on nrf51\_pca10028:arm
- [GitHub #8197](https://github.com/zephyrproject-rtos/zephyr/issues/8197) - kernel.memory\_protection.stack\_random: Stack pointer randomization fails on em\_starterkit\_em7d\_v22
- [GitHub #8190](https://github.com/zephyrproject-rtos/zephyr/issues/8190) - scheduler: thread priorities need to be cleaned up
- [GitHub #8187](https://github.com/zephyrproject-rtos/zephyr/issues/8187) - QEMU serial output is not reliable, may affect SLIP and thus network testing
- [GitHub #8160](https://github.com/zephyrproject-rtos/zephyr/issues/8160) - BUILD\_ASSERT doesn’t work outside gcc
- [GitHub #8159](https://github.com/zephyrproject-rtos/zephyr/issues/8159) - tests/kernel/fifo/fifo\_timeout fails on nrf51\_pca10028 and nrf52\_pca10040
- [GitHub #8131](https://github.com/zephyrproject-rtos/zephyr/issues/8131) - net\_if\_tx sends a 0 Reference counter(pkt->ref == 0) packet
- [GitHub #8116](https://github.com/zephyrproject-rtos/zephyr/issues/8116) - tests/kernel/profiling/profiling\_api fails to complete on minnowboard
- [GitHub #8115](https://github.com/zephyrproject-rtos/zephyr/issues/8115) - tests/kernel/xip crasshes on minnowboard
- [GitHub #8108](https://github.com/zephyrproject-rtos/zephyr/issues/8108) - make ‘rom\_report’ misreports \_sw\_isr\_table
- [GitHub #8104](https://github.com/zephyrproject-rtos/zephyr/issues/8104) - open-amp: enable C library cause open-ampopen-amplibcommonsh\_mem.c compile error
- [GitHub #8097](https://github.com/zephyrproject-rtos/zephyr/issues/8097) - tests/drivers/watchdog/wdt\_basic\_api fails on Quark SE / x86 and esp32
- [GitHub #8057](https://github.com/zephyrproject-rtos/zephyr/issues/8057) - samples/net/: Experiencing the delayed response from zephyr networking stack
- [GitHub #7999](https://github.com/zephyrproject-rtos/zephyr/issues/7999) - HCI UART with Linux host cannot connect to nrf52 6lowpan peripheral
- [GitHub #7986](https://github.com/zephyrproject-rtos/zephyr/issues/7986) - The scripts (debug, debugserver and flash) are not working for Intel S1000 board
- [GitHub #7818](https://github.com/zephyrproject-rtos/zephyr/issues/7818) - big\_http\_download stuck during download on qemu\_x86
- [GitHub #7817](https://github.com/zephyrproject-rtos/zephyr/issues/7817) - Confusing macros: SECONDS vs K\_SECONDS, MSEC vs K\_MSEC
- [GitHub #7760](https://github.com/zephyrproject-rtos/zephyr/issues/7760) - cmake failure using ExternalProject and dependencies w/ninja
- [GitHub #7706](https://github.com/zephyrproject-rtos/zephyr/issues/7706) - ARM NXP hardware stack overflows do not report \_NANO\_ERR\_STACK\_CHK\_FAIL or provide MPU fault information
- [GitHub #7638](https://github.com/zephyrproject-rtos/zephyr/issues/7638) - get FAULT when fuzzing sys\_ring\_buf\_ put and sys\_ring\_bug\_get APIs
- [GitHub #7510](https://github.com/zephyrproject-rtos/zephyr/issues/7510) - [Coverity CID :185395] Memory - corruptions in /samples/net/mbedtls\_sslclient/src/mini\_client.c
- [GitHub #7441](https://github.com/zephyrproject-rtos/zephyr/issues/7441) - newlib support in zephyr is untested and very broken
- [GitHub #7409](https://github.com/zephyrproject-rtos/zephyr/issues/7409) - Networking examples crash on optimization levels different than -Os
- [GitHub #7390](https://github.com/zephyrproject-rtos/zephyr/issues/7390) - pinmux subsystem API is undocumented and does not enforce validation
- [GitHub #7381](https://github.com/zephyrproject-rtos/zephyr/issues/7381) - gpio\_mcux driver needs to validate pin parameters
- [GitHub #7291](https://github.com/zephyrproject-rtos/zephyr/issues/7291) - intermittent issue with tests/kernel/fatal
- [GitHub #7196](https://github.com/zephyrproject-rtos/zephyr/issues/7196) - kernel: CONFIG\_INIT\_STACKS : minor documentation & dependency update
- [GitHub #7193](https://github.com/zephyrproject-rtos/zephyr/issues/7193) - tickless and timeslicing don’t play well together
- [GitHub #7179](https://github.com/zephyrproject-rtos/zephyr/issues/7179) - \_vprintk incorrectly prints 64-bit values
- [GitHub #7048](https://github.com/zephyrproject-rtos/zephyr/issues/7048) - Tickless Kernel Timekeeping Problem
- [GitHub #7013](https://github.com/zephyrproject-rtos/zephyr/issues/7013) - cleanup device tree warnings on STM32
- [GitHub #6874](https://github.com/zephyrproject-rtos/zephyr/issues/6874) - Not able to join OpenThread BorderRouter or a ot-ftd-cli network
- [GitHub #6866](https://github.com/zephyrproject-rtos/zephyr/issues/6866) - build: requirements: No module named yaml and elftools
- [GitHub #6696](https://github.com/zephyrproject-rtos/zephyr/issues/6696) - [Coverity CID: 183036] Control flow issues in /drivers/gpio/gpio\_sam.c
- [GitHub #6695](https://github.com/zephyrproject-rtos/zephyr/issues/6695) - [Coverity CID: 183037] Memory - corruptions in /samples/net/mbedtls\_dtlsclient/src/dtls\_client.c
- [GitHub #6666](https://github.com/zephyrproject-rtos/zephyr/issues/6666) - [Coverity CID: 183066] Error handling issues in /tests/kernel/mbox/mbox\_api/src/test\_mbox\_api.c
- [GitHub #6585](https://github.com/zephyrproject-rtos/zephyr/issues/6585) - kernel: re-delete event list node [bug]
- [GitHub #6452](https://github.com/zephyrproject-rtos/zephyr/issues/6452) - Jumbled Console log over USB
- [GitHub #6365](https://github.com/zephyrproject-rtos/zephyr/issues/6365) - “dummy-flash” device tree bug
- [GitHub #6319](https://github.com/zephyrproject-rtos/zephyr/issues/6319) - Missing documentation for zephyr API to query kernel version: sys\_kernel\_version\_get
- [GitHub #6276](https://github.com/zephyrproject-rtos/zephyr/issues/6276) - assert when running sys\_kernel on disco\_l475\_iot1 (with asserts enabled)
- [GitHub #6226](https://github.com/zephyrproject-rtos/zephyr/issues/6226) - IRC-bot sample eventually stops responding to IRC commands
- [GitHub #6180](https://github.com/zephyrproject-rtos/zephyr/issues/6180) - CONFIG\_IS\_BOOTLOADER is poorly named and documented
- [GitHub #6147](https://github.com/zephyrproject-rtos/zephyr/issues/6147) - “ninja flash” cannot be used with DFU-capable applications
- [GitHub #5781](https://github.com/zephyrproject-rtos/zephyr/issues/5781) - Initial TLS connection failure causes TLS client handler to stop and fail endlessly w/ EBUSY
- [GitHub #5735](https://github.com/zephyrproject-rtos/zephyr/issues/5735) - mpu\_stack\_guard\_test fails on many arm platforms, including qemu
- [GitHub #5734](https://github.com/zephyrproject-rtos/zephyr/issues/5734) - samples/drivers/crypto fails on qemu\_nios2
- [GitHub #5702](https://github.com/zephyrproject-rtos/zephyr/issues/5702) - usb subsystem doc not pulling from header doxygen comments
- [GitHub #5678](https://github.com/zephyrproject-rtos/zephyr/issues/5678) - USB: DW driver does not work properly with mass storage class
- [GitHub #5634](https://github.com/zephyrproject-rtos/zephyr/issues/5634) - The dependency between the Kconfig source files and the Kconfig output is missing
- [GitHub #5605](https://github.com/zephyrproject-rtos/zephyr/issues/5605) - Compiler flags added late in the build are not exported to external build systems
- [GitHub #5603](https://github.com/zephyrproject-rtos/zephyr/issues/5603) - Bluetooth logging is hardcoded with level 4 (debug)
- [GitHub #5485](https://github.com/zephyrproject-rtos/zephyr/issues/5485) - tests: kernel/xip: CONFIG\_BOOT\_DELAY issue for qemu\_riscv32
- [GitHub #5426](https://github.com/zephyrproject-rtos/zephyr/issues/5426) - [kconfig] Allow user-input when new options are detected
- [GitHub #5411](https://github.com/zephyrproject-rtos/zephyr/issues/5411) - Secondary repos are missing licenses
- [GitHub #5387](https://github.com/zephyrproject-rtos/zephyr/issues/5387) - Many of the samples using mbedtls\_ssl\_conf\_psk() dont check for error
- [GitHub #5376](https://github.com/zephyrproject-rtos/zephyr/issues/5376) - No way to get clock control subsystem type
- [GitHub #5343](https://github.com/zephyrproject-rtos/zephyr/issues/5343) - cmake: libapp.a in unexpected location
- [GitHub #5289](https://github.com/zephyrproject-rtos/zephyr/issues/5289) - IPv6 over BLE: IPSP sample crashes and ble controller gets disconnected
- [GitHub #5244](https://github.com/zephyrproject-rtos/zephyr/issues/5244) - UART continuous interrupt
- [GitHub #5226](https://github.com/zephyrproject-rtos/zephyr/issues/5226) - Compiling with -O0 causes the kobject text area to exceed the limit (linker error)
- [GitHub #5006](https://github.com/zephyrproject-rtos/zephyr/issues/5006) - syscalls: properly fix how unit testing deals with \_\_syscall
- [GitHub #4977](https://github.com/zephyrproject-rtos/zephyr/issues/4977) - USB: documentation needs to be updated
- [GitHub #4927](https://github.com/zephyrproject-rtos/zephyr/issues/4927) - Hard Fault when no device driver is setup for ENTROPY results
- [GitHub #4888](https://github.com/zephyrproject-rtos/zephyr/issues/4888) - LwM2M: Fix BT device pending / retry errors
- [GitHub #4836](https://github.com/zephyrproject-rtos/zephyr/issues/4836) - connection disconnected due to Le timeout(0x22)
- [GitHub #4682](https://github.com/zephyrproject-rtos/zephyr/issues/4682) - http\_server example fails for ESP32
- [GitHub #4324](https://github.com/zephyrproject-rtos/zephyr/issues/4324) - samples/net/http\_client: error in detecting and processing the message received
- [GitHub #4082](https://github.com/zephyrproject-rtos/zephyr/issues/4082) - remove \_current NULL check in ARM’s \_is\_thread\_user()
- [GitHub #4042](https://github.com/zephyrproject-rtos/zephyr/issues/4042) - net: NET\_CONN\_CACHE relevant
- [GitHub #4002](https://github.com/zephyrproject-rtos/zephyr/issues/4002) - Can not compile C++ project without setting -fpermissive
- [GitHub #3999](https://github.com/zephyrproject-rtos/zephyr/issues/3999) - qemu\_xtensa crash while running sample/net/sockets/echo with ipv6 enabled
- [GitHub #3997](https://github.com/zephyrproject-rtos/zephyr/issues/3997) - **\* ERROR \*** pkt 0x2000c524 is freed already by prepare\_segment():388 (mqtt\_tx\_publish():242)
- [GitHub #3906](https://github.com/zephyrproject-rtos/zephyr/issues/3906) - Static code scan (coverity CID: 151975, 173645, 173658 ) issues seen
- [GitHub #3847](https://github.com/zephyrproject-rtos/zephyr/issues/3847) - Fix LwM2M object firmware pull block transfer mode to select size via interface type (BT, ethernet, etc)
- [GitHub #3796](https://github.com/zephyrproject-rtos/zephyr/issues/3796) - Multiple issues with http\_server library design and implementation
- [GitHub #3670](https://github.com/zephyrproject-rtos/zephyr/issues/3670) - ARC: timeslice not reset on interrupt-induced swap
- [GitHub #3669](https://github.com/zephyrproject-rtos/zephyr/issues/3669) - xtensa: timeslice not reset for interrupt-induced swaps
- [GitHub #3606](https://github.com/zephyrproject-rtos/zephyr/issues/3606) - \_NanoFatalErrorHandler and other internal kernel APIs are inconsistently defined
- [GitHub #3524](https://github.com/zephyrproject-rtos/zephyr/issues/3524) - Bluetooth data types missing API documentation
- [GitHub #3522](https://github.com/zephyrproject-rtos/zephyr/issues/3522) - New Zephyr-defined types missing API documentation
- [GitHub #3464](https://github.com/zephyrproject-rtos/zephyr/issues/3464) - xtensa hifi\_mini SOC does not build
- [GitHub #3375](https://github.com/zephyrproject-rtos/zephyr/issues/3375) - Debugging difficulties on Cortex-M with frame pointer missing
- [GitHub #3288](https://github.com/zephyrproject-rtos/zephyr/issues/3288) - Fatal fault in SPI ISR when using multiple interfaces
- [GitHub #3244](https://github.com/zephyrproject-rtos/zephyr/issues/3244) - Ataes132a fails to encrypt/decrypt with mode ECB and CCM mode
- [GitHub #3226](https://github.com/zephyrproject-rtos/zephyr/issues/3226) - ATT channel gets disconnected on ATT timeout but GATT API doesn’t check for it
- [GitHub #3198](https://github.com/zephyrproject-rtos/zephyr/issues/3198) - ARC: Boot\_time test not functioning
- [GitHub #3132](https://github.com/zephyrproject-rtos/zephyr/issues/3132) - frdm\_k64f: Sometimes, there may be 1000+ms roundtrip for pings and other Ethernet packets (instead of sub-ms)
- [GitHub #3129](https://github.com/zephyrproject-rtos/zephyr/issues/3129) - frdm\_k64f: Ethernet may become stuck in semi-persistent weird state, not transferring data, potentially affecting host Ethernet
- [GitHub #2984](https://github.com/zephyrproject-rtos/zephyr/issues/2984) - frdm\_k64f bus exception bug due to peculiar RAM configuration
- [GitHub #2907](https://github.com/zephyrproject-rtos/zephyr/issues/2907) - make menuconfig .config easily overwritten
- [GitHub #2627](https://github.com/zephyrproject-rtos/zephyr/issues/2627) - LE L2CAP CoC transfers less octets that claims to be
- [GitHub #2108](https://github.com/zephyrproject-rtos/zephyr/issues/2108) - Stack alignment on ARM doesn’t always follow Procedure Call Standard
- [GitHub #1677](https://github.com/zephyrproject-rtos/zephyr/issues/1677) - sys\_\*\_bit and sys\_bitfield\_\*\_bit APIs are not implemented on ARM
- [GitHub #1550](https://github.com/zephyrproject-rtos/zephyr/issues/1550) - problem with pci\_bus\_scan resulting in an endless loop
- [GitHub #1533](https://github.com/zephyrproject-rtos/zephyr/issues/1533) - It is not documented how to discover, install, and use external toolchains
- [GitHub #1495](https://github.com/zephyrproject-rtos/zephyr/issues/1495) - esp32: newlibc errors
- [GitHub #1429](https://github.com/zephyrproject-rtos/zephyr/issues/1429) - LWM2M configs not defined
- [GitHub #1381](https://github.com/zephyrproject-rtos/zephyr/issues/1381) - HMC5883L driver config error
- [GitHub #729](https://github.com/zephyrproject-rtos/zephyr/issues/729) - TCP SYN backlog change likely has concurrent global var access issues
