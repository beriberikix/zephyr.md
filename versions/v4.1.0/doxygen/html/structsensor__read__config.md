---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__read__config.html
original_path: doxygen/html/structsensor__read__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_read\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [sensor](#ad49d5ab5293017d1ad2cf60adc542090) |
| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_streaming](#aca96de2c23fb63f887c4c40dcb272798) |
| union { |  |
| struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*const   [channels](#a2aff44f02b25fd4ad1d4bc217800fad1) |  |
| struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) \*const   [triggers](#a6eaa6df7bc9378abe0f5b4b8c9a05909) |  |
| }; |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a5236049e0563ebba754994d70e22383a) |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [max](#aecb9c899e292fdb25c3c990bdaf1c76b) |

## Field Documentation

## [◆ ](#a7ee7e4bbe5132206f84eec1e0cba36ca)[union]

| union { ... } [sensor\_read\_config](structsensor__read__config.md) |
| --- |

## [◆ ](#a2aff44f02b25fd4ad1d4bc217800fad1)channels

| struct [sensor\_chan\_spec](structsensor__chan__spec.md)\* const sensor\_read\_config::channels |
| --- |

## [◆ ](#a5236049e0563ebba754994d70e22383a)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sensor\_read\_config::count |
| --- |

## [◆ ](#aca96de2c23fb63f887c4c40dcb272798)is\_streaming

| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sensor\_read\_config::is\_streaming |
| --- |

## [◆ ](#aecb9c899e292fdb25c3c990bdaf1c76b)max

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sensor\_read\_config::max |
| --- |

## [◆ ](#ad49d5ab5293017d1ad2cf60adc542090)sensor

| const struct [device](structdevice.md)\* sensor\_read\_config::sensor |
| --- |

## [◆ ](#a6eaa6df7bc9378abe0f5b4b8c9a05909)triggers

| struct [sensor\_stream\_trigger](structsensor__stream__trigger.md)\* const sensor\_read\_config::triggers |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_read\_config](structsensor__read__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
