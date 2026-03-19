---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structqspi__config.html
original_path: doxygen/html/structqspi__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qspi\_config Struct Reference

`#include <[qspi_if.h](qspi__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [RDC4IO](#a0871c7febd31179f45eb095b70f5caee) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [easydma](#a6b79c9618e16540f93714008462b51be) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [single\_op](#a4b69e092bf8f73ac8e9b416690a58d28) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [quad\_spi](#aac7103e7473ccd56c2b9b3dc747f7ce1) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a88db2e115bbd7a1928c8cc54dba3857f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [CMD\_CNONCE](#a259a8d91bfe758d84df07acfc55499b6) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enc\_enabled](#aee934c27f6916f6c7297db5a1e6e8ded) |
| struct k\_sem | [lock](#abaf0a8bf1706301dcd27e1f4a17676af) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [addrmask](#a38bd66f9b0acdf6f0a656427b7c0c7f8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [qspi\_slave\_latency](#ab0c0611e6960a1c84e02f987f3c2a767) |
| int | [test\_hlread](#a945333ae972b568219b94b2ed5f640a9) |
| char \* | [test\_name](#a2d01b48538d0103b03faf800b9d74819) |
| int | [test\_start](#a5df29101652b0101b9cd24ffc8c469e9) |
| int | [test\_end](#a386c8f8150985ea26f1f7fb92abdd344) |
| int | [test\_iterations](#a8f3a31437f28208b5ce6b00c702b7c44) |
| int | [test\_timediff\_read](#a3bb96eee89df742635aa9cbc1101c025) |
| int | [test\_timediff\_write](#a423967ddc3952545c7f2081a8b649992) |
| int | [test\_status](#ad147f9c013f82fb08ca674f09791f731) |
| int | [test\_iteration](#a729d72b95d82092c2b9b7b1b17d2a121) |

## Field Documentation

## [◆ ](#a38bd66f9b0acdf6f0a656427b7c0c7f8)addrmask

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int qspi\_config::addrmask |
| --- |

## [◆ ](#a259a8d91bfe758d84df07acfc55499b6)CMD\_CNONCE

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::CMD\_CNONCE |
| --- |

## [◆ ](#a6b79c9618e16540f93714008462b51be)easydma

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::easydma |
| --- |

## [◆ ](#aee934c27f6916f6c7297db5a1e6e8ded)enc\_enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::enc\_enabled |
| --- |

## [◆ ](#a88db2e115bbd7a1928c8cc54dba3857f)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::encryption |
| --- |

## [◆ ](#abaf0a8bf1706301dcd27e1f4a17676af)lock

| struct k\_sem qspi\_config::lock |
| --- |

## [◆ ](#ab0c0611e6960a1c84e02f987f3c2a767)qspi\_slave\_latency

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char qspi\_config::qspi\_slave\_latency |
| --- |

## [◆ ](#aac7103e7473ccd56c2b9b3dc747f7ce1)quad\_spi

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::quad\_spi |
| --- |

## [◆ ](#a0871c7febd31179f45eb095b70f5caee)RDC4IO

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char qspi\_config::RDC4IO |
| --- |

## [◆ ](#a4b69e092bf8f73ac8e9b416690a58d28)single\_op

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) qspi\_config::single\_op |
| --- |

## [◆ ](#a386c8f8150985ea26f1f7fb92abdd344)test\_end

| int qspi\_config::test\_end |
| --- |

## [◆ ](#a945333ae972b568219b94b2ed5f640a9)test\_hlread

| int qspi\_config::test\_hlread |
| --- |

## [◆ ](#a729d72b95d82092c2b9b7b1b17d2a121)test\_iteration

| int qspi\_config::test\_iteration |
| --- |

## [◆ ](#a8f3a31437f28208b5ce6b00c702b7c44)test\_iterations

| int qspi\_config::test\_iterations |
| --- |

## [◆ ](#a2d01b48538d0103b03faf800b9d74819)test\_name

| char\* qspi\_config::test\_name |
| --- |

## [◆ ](#a5df29101652b0101b9cd24ffc8c469e9)test\_start

| int qspi\_config::test\_start |
| --- |

## [◆ ](#ad147f9c013f82fb08ca674f09791f731)test\_status

| int qspi\_config::test\_status |
| --- |

## [◆ ](#a3bb96eee89df742635aa9cbc1101c025)test\_timediff\_read

| int qspi\_config::test\_timediff\_read |
| --- |

## [◆ ](#a423967ddc3952545c7f2081a8b649992)test\_timediff\_write

| int qspi\_config::test\_timediff\_write |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/wifi/nrf\_wifi/bus/[qspi\_if.h](qspi__if_8h_source.md)

- [qspi\_config](structqspi__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
