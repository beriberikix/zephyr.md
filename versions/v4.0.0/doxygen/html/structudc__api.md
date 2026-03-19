---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structudc__api.html
original_path: doxygen/html/structudc__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_api Struct Reference

UDC driver API This is the mandatory API any USB device controller driver needs to expose with exception of: [device\_speed()](#adf2b8f76158d7bd2d3918628c8a9fc22), [test\_mode()](#ab06839ded48cbc671b2b915fe0010959) are only required for HS controllers.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b)(\* | [device\_speed](#adf2b8f76158d7bd2d3918628c8a9fc22) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [ep\_enqueue](#aa1d3dadf63cb156ce5346712e1c65069) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg, struct [net\_buf](structnet__buf.md) \*const buf) |
| int(\* | [ep\_dequeue](#a023fcfa0fa251dcadcb379347fe7531a) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [ep\_set\_halt](#adf2adaea90b53999d1e98756062a2050) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [ep\_clear\_halt](#a923a684868721d0b7232c86eed15e121) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [ep\_try\_config](#a775a18f5555f1c518762ff7dc016559c) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [ep\_enable](#a27291ab4d2acda207f6a6a2313d50793) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [ep\_disable](#a1af05b484e9c9d1f2a0dbfb822f09c98) )(const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| int(\* | [host\_wakeup](#aeca6c3a8a6b7af469d96bec8c9a8e5eb) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_address](#a2e8b88743ab56144a199b3ad0618755f) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
| int(\* | [test\_mode](#ab06839ded48cbc671b2b915fe0010959) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dryrun) |
| int(\* | [enable](#af8b916f6b8c211ad82ddcfdaa12de5ae) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [disable](#a8997bba956d264463b71aae0b1a4e3dc) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [init](#a01f803a2d258072df102b831cf184b27) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [shutdown](#ad7135abf78eb372730dddbba7dc6a75d) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [lock](#ad33ad060c97aa7e5896fdc5e33a3e141) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [unlock](#a2029ee9db16e15e2b609c3199b00e201) )(const struct [device](structdevice.md) \*dev) |

## Detailed Description

UDC driver API This is the mandatory API any USB device controller driver needs to expose with exception of: [device\_speed()](#adf2b8f76158d7bd2d3918628c8a9fc22), [test\_mode()](#ab06839ded48cbc671b2b915fe0010959) are only required for HS controllers.

## Field Documentation

## [◆ ](#adf2b8f76158d7bd2d3918628c8a9fc22)device\_speed

| enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b)(\* udc\_api::device\_speed) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a8997bba956d264463b71aae0b1a4e3dc)disable

| int(\* udc\_api::disable) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#af8b916f6b8c211ad82ddcfdaa12de5ae)enable

| int(\* udc\_api::enable) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a923a684868721d0b7232c86eed15e121)ep\_clear\_halt

| int(\* udc\_api::ep\_clear\_halt) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#a023fcfa0fa251dcadcb379347fe7531a)ep\_dequeue

| int(\* udc\_api::ep\_dequeue) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#a1af05b484e9c9d1f2a0dbfb822f09c98)ep\_disable

| int(\* udc\_api::ep\_disable) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#a27291ab4d2acda207f6a6a2313d50793)ep\_enable

| int(\* udc\_api::ep\_enable) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#aa1d3dadf63cb156ce5346712e1c65069)ep\_enqueue

| int(\* udc\_api::ep\_enqueue) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg, struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

## [◆ ](#adf2adaea90b53999d1e98756062a2050)ep\_set\_halt

| int(\* udc\_api::ep\_set\_halt) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#a775a18f5555f1c518762ff7dc016559c)ep\_try\_config

| int(\* udc\_api::ep\_try\_config) (const struct [device](structdevice.md) \*dev, struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
| --- |

## [◆ ](#aeca6c3a8a6b7af469d96bec8c9a8e5eb)host\_wakeup

| int(\* udc\_api::host\_wakeup) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a01f803a2d258072df102b831cf184b27)init

| int(\* udc\_api::init) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ad33ad060c97aa7e5896fdc5e33a3e141)lock

| int(\* udc\_api::lock) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a2e8b88743ab56144a199b3ad0618755f)set\_address

| int(\* udc\_api::set\_address) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
| --- |

## [◆ ](#ad7135abf78eb372730dddbba7dc6a75d)shutdown

| int(\* udc\_api::shutdown) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ab06839ded48cbc671b2b915fe0010959)test\_mode

| int(\* udc\_api::test\_mode) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dryrun) |
| --- |

## [◆ ](#a2029ee9db16e15e2b609c3199b00e201)unlock

| int(\* udc\_api::unlock) (const struct [device](structdevice.md) \*dev) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_api](structudc__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
