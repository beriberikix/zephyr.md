---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structnrf__clock__control__driver__api.html
original_path: doxygen/html/structnrf__clock__control__driver__api.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control\_driver\_api Struct Reference

`#include <[zephyr/drivers/clock_control/nrf_clock_control.h](nrf__clock__control_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [clock\_control\_driver\_api](structclock__control__driver__api.md) | [std\_api](#ac2bd169ad00d069e5b4dc384c7d05a69) |
| int(\* | [request](#a5ad4fb66f464ffac5e5b221a53c276bc) )(const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
| int(\* | [release](#aca297620f0fc63b8fd2769cb069d144a) )(const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec) |
| int(\* | [cancel\_or\_release](#a86ac5fa7b2dbae88e4be8f4adde37319) )(const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
| int(\* | [resolve](#a37b6a7723376a51f112fdeda13219604) )(const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*req\_spec, struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*res\_spec) |
| int(\* | [get\_startup\_time](#ac9570d7876580df1b66d108c7b0aa78b) )(const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*startup\_time\_us) |

## Field Documentation

## [◆ ](#a86ac5fa7b2dbae88e4be8f4adde37319)cancel\_or\_release

| int(\* nrf\_clock\_control\_driver\_api::cancel\_or\_release) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
| --- |

## [◆ ](#ac9570d7876580df1b66d108c7b0aa78b)get\_startup\_time

| int(\* nrf\_clock\_control\_driver\_api::get\_startup\_time) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*startup\_time\_us) |
| --- |

## [◆ ](#aca297620f0fc63b8fd2769cb069d144a)release

| int(\* nrf\_clock\_control\_driver\_api::release) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec) |
| --- |

## [◆ ](#a5ad4fb66f464ffac5e5b221a53c276bc)request

| int(\* nrf\_clock\_control\_driver\_api::request) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
| --- |

## [◆ ](#a37b6a7723376a51f112fdeda13219604)resolve

| int(\* nrf\_clock\_control\_driver\_api::resolve) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*req\_spec, struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*res\_spec) |
| --- |

## [◆ ](#ac2bd169ad00d069e5b4dc384c7d05a69)std\_api

| struct [clock\_control\_driver\_api](structclock__control__driver__api.md) nrf\_clock\_control\_driver\_api::std\_api |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/clock\_control/[nrf\_clock\_control.h](nrf__clock__control_8h_source.md)

- [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
