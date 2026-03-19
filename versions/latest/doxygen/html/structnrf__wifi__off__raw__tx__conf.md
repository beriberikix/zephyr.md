---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnrf__wifi__off__raw__tx__conf.html
original_path: doxygen/html/structnrf__wifi__off__raw__tx__conf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_wifi\_off\_raw\_tx\_conf Struct Reference

[nRF70 Offloaded raw TX API](group__nrf70__off__raw__tx__api.md)

- Configuration parameters for offloaded raw TX Parameters which can be used to configure the offloaded raw TX operation.

[More...](#details)

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [period\_us](#a2a772fb8c30ac44592a437d9782d76cf) |
|  | Time interval (in microseconds) between transmissions. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [tx\_pwr](#a328e1b3b7411e5685683c8718a05173e) |
|  | Transmit power in dBm (0 to 20). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [chan](#abff388f54589d410b10e2e55a4574314) |
|  | Channel number on which to transmit. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [short\_preamble](#a907d509fb2988e5003120ccff4f24932) |
|  | Set to TRUE to use short preamble for FALSE to disable short preamble. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [num\_retries](#ab88c522e97c5f624b78133a3d184ebd0) |
| enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) | [tput\_mode](#a631f15bbd4930256b3b6f64175a630b7) |
|  | Throughput mode for packet transmittion. |
| enum [nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) | [rate](#a52419b8149b390888491511413e17f98) |
| enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) | [he\_gi](#a3e56b1bf386d483d0f6eb04b00c46cac) |
|  | HE GI. |
| enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) | [he\_ltf](#a30ca67432373107948926c646c951237) |
|  | HE GI. |
| void \* | [pkt](#a5a110783498904f3e2a40b1c768a9af2) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [pkt\_len](#a447104d9cf7cd3ba6b7a50548e940a9e) |
|  | Packet length of the frame to be transmitted, (min 26 bytes and max 600 bytes). |

## Detailed Description

- Configuration parameters for offloaded raw TX Parameters which can be used to configure the offloaded raw TX operation.

## Field Documentation

## [◆ ](#abff388f54589d410b10e2e55a4574314)chan

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nrf\_wifi\_off\_raw\_tx\_conf::chan |
| --- |

Channel number on which to transmit.

## [◆ ](#a3e56b1bf386d483d0f6eb04b00c46cac)he\_gi

| enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) nrf\_wifi\_off\_raw\_tx\_conf::he\_gi |
| --- |

HE GI.

Refer &enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d "HE guard interval value Value of the guard interval to be used between symbols when transmitting usin...")

## [◆ ](#a30ca67432373107948926c646c951237)he\_ltf

| enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) nrf\_wifi\_off\_raw\_tx\_conf::he\_ltf |
| --- |

HE GI.

Refer &enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61 "HE long training field duration Value of the long training field duration to be used when transmittin...")

## [◆ ](#ab88c522e97c5f624b78133a3d184ebd0)num\_retries

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nrf\_wifi\_off\_raw\_tx\_conf::num\_retries |
| --- |

## [◆ ](#a2a772fb8c30ac44592a437d9782d76cf)period\_us

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nrf\_wifi\_off\_raw\_tx\_conf::period\_us |
| --- |

Time interval (in microseconds) between transmissions.

## [◆ ](#a5a110783498904f3e2a40b1c768a9af2)pkt

| void\* nrf\_wifi\_off\_raw\_tx\_conf::pkt |
| --- |

## [◆ ](#a447104d9cf7cd3ba6b7a50548e940a9e)pkt\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nrf\_wifi\_off\_raw\_tx\_conf::pkt\_len |
| --- |

Packet length of the frame to be transmitted, (min 26 bytes and max 600 bytes).

## [◆ ](#a52419b8149b390888491511413e17f98)rate

| enum [nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) nrf\_wifi\_off\_raw\_tx\_conf::rate |
| --- |

## [◆ ](#a907d509fb2988e5003120ccff4f24932)short\_preamble

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) nrf\_wifi\_off\_raw\_tx\_conf::short\_preamble |
| --- |

Set to TRUE to use short preamble for FALSE to disable short preamble.

## [◆ ](#a631f15bbd4930256b3b6f64175a630b7)tput\_mode

| enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) nrf\_wifi\_off\_raw\_tx\_conf::tput\_mode |
| --- |

Throughput mode for packet transmittion.

Refer &enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131 "Throughput mode Throughput mode to be used for transmitting the packet.")

## [◆ ](#a328e1b3b7411e5685683c8718a05173e)tx\_pwr

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nrf\_wifi\_off\_raw\_tx\_conf::tx\_pwr |
| --- |

Transmit power in dBm (0 to 20).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/wifi/nrf\_wifi/off\_raw\_tx/[off\_raw\_tx\_api.h](off__raw__tx__api_8h_source.md)

- [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
