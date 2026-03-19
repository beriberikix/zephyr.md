---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__lora__api.html
original_path: doxygen/html/group__lora__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LoRa APIs

[Device Driver APIs](group__io__interfaces.md)

| Data Structures | |
| --- | --- |
| struct | [lora\_modem\_config](structlora__modem__config.md) |
|  | Structure containing the configuration of a LoRa modem. [More...](structlora__modem__config.md#details) |

| Enumerations | |
| --- | --- |
| enum | [lora\_signal\_bandwidth](#gabb5feb9d1a2bb160d9b55939efb17136) { [BW\_125\_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) = 0 , [BW\_250\_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411) , [BW\_500\_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9) } |
|  | LoRa signal bandwidth. [More...](#gabb5feb9d1a2bb160d9b55939efb17136) |
| enum | [lora\_datarate](#ga30bfeb2e6f4e35869996b597b614becb) {     [SF\_6](#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) = 6 , [SF\_7](#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608) , [SF\_8](#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e) , [SF\_9](#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc) ,     [SF\_10](#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6) , [SF\_11](#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407) , [SF\_12](#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)   } |
|  | LoRa data-rate. [More...](#ga30bfeb2e6f4e35869996b597b614becb) |
| enum | [lora\_coding\_rate](#ga5af378491814d0d3a059cd6cd39265c8) { [CR\_4\_5](#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) = 1 , [CR\_4\_6](#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) = 2 , [CR\_4\_7](#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) = 3 , [CR\_4\_8](#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) = 4 } |
|  | LoRa coding rate. [More...](#ga5af378491814d0d3a059cd6cd39265c8) |

| Functions | |
| --- | --- |
| static int | [lora\_config](#gad7c6c516d2d0e023da952666d3f8decb) (const struct [device](structdevice.md) \*dev, struct [lora\_modem\_config](structlora__modem__config.md) \*config) |
|  | Configure the LoRa modem. |
| static int | [lora\_send](#gad893b49a74e350bb05f42f863af31446) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len) |
|  | Send data over LoRa. |
| static int | [lora\_send\_async](#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Asynchronously send data over LoRa. |
| static int | [lora\_recv](#ga28005c24ab1c13eb311bc05c3454a8f6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr) |
|  | Receive data over LoRa. |
| static int | [lora\_recv\_async](#ga4f7ec5eaff55f295ff82f3e22d77f34c) (const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb) |
|  | Receive data asynchronously over LoRa. |
| static int | [lora\_test\_cw](#ga27d78168c737d56f9f7f3bbdacb808fb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration) |
|  | Transmit an unmodulated continuous wave at a given frequency. |

## Detailed Description

Since
:   2.2

Version
:   0.1.0

## Enumeration Type Documentation

## [◆ ](#ga5af378491814d0d3a059cd6cd39265c8)lora\_coding\_rate

| enum [lora\_coding\_rate](#ga5af378491814d0d3a059cd6cd39265c8) |
| --- |

`#include <[lora.h](lora_8h.md)>`

LoRa coding rate.

| Enumerator | |
| --- | --- |
| CR\_4\_5 |  |
| CR\_4\_6 |  |
| CR\_4\_7 |  |
| CR\_4\_8 |  |

## [◆ ](#ga30bfeb2e6f4e35869996b597b614becb)lora\_datarate

| enum [lora\_datarate](#ga30bfeb2e6f4e35869996b597b614becb) |
| --- |

`#include <[lora.h](lora_8h.md)>`

LoRa data-rate.

| Enumerator | |
| --- | --- |
| SF\_6 |  |
| SF\_7 |  |
| SF\_8 |  |
| SF\_9 |  |
| SF\_10 |  |
| SF\_11 |  |
| SF\_12 |  |

## [◆ ](#gabb5feb9d1a2bb160d9b55939efb17136)lora\_signal\_bandwidth

| enum [lora\_signal\_bandwidth](#gabb5feb9d1a2bb160d9b55939efb17136) |
| --- |

`#include <[lora.h](lora_8h.md)>`

LoRa signal bandwidth.

| Enumerator | |
| --- | --- |
| BW\_125\_KHZ |  |
| BW\_250\_KHZ |  |
| BW\_500\_KHZ |  |

## Function Documentation

## [◆ ](#gad7c6c516d2d0e023da952666d3f8decb)lora\_config()

| | int lora\_config | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [lora\_modem\_config](structlora__modem__config.md) \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Configure the LoRa modem.

Parameters
:   | dev | LoRa device |
    | --- | --- |
    | config | Data structure containing the intended configuration for the modem |

Returns
:   0 on success, negative on error

## [◆ ](#ga28005c24ab1c13eb311bc05c3454a8f6)lora\_recv()

| | int lora\_recv | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, | |  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *rssi*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \* | *snr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Receive data over LoRa.

Note
:   This is a blocking call.

Parameters
:   | dev | LoRa device |
    | --- | --- |
    | data | Buffer to hold received data |
    | size | Size of the buffer to hold the received data. Max size allowed is 255. |
    | timeout | Duration to wait for a packet. |
    | rssi | RSSI of received data |
    | snr | SNR of received data |

Returns
:   Length of the data received on success, negative on error

## [◆ ](#ga4f7ec5eaff55f295ff82f3e22d77f34c)lora\_recv\_async()

| | int lora\_recv\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | lora\_recv\_cb | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Receive data asynchronously over LoRa.

Receive packets continuously under the configuration previously setup by [lora\_config](#gad7c6c516d2d0e023da952666d3f8decb).

Reception is cancelled by calling this function again with `cb` = NULL. This can be done within the callback handler.

Parameters
:   | dev | Modem to receive data on. |
    | --- | --- |
    | cb | Callback to run on receiving data. If NULL, any pending asynchronous receptions will be cancelled. |

Returns
:   0 when reception successfully setup, negative on error

## [◆ ](#gad893b49a74e350bb05f42f863af31446)lora\_send()

| | int lora\_send | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Send data over LoRa.

Note
:   This blocks until transmission is complete.

Parameters
:   | dev | LoRa device |
    | --- | --- |
    | data | Data to be sent |
    | data\_len | Length of the data to be sent |

Returns
:   0 on success, negative on error

## [◆ ](#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)lora\_send\_async()

| | int lora\_send\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data\_len*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *async* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Asynchronously send data over LoRa.

Note
:   This returns immediately after starting transmission, and locks the LoRa modem until the transmission completes.

Parameters
:   | dev | LoRa device |
    | --- | --- |
    | data | Data to be sent |
    | data\_len | Length of the data to be sent |
    | async | A pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). (Note: if NULL this function will not notify the end of the transmission). |

Returns
:   0 on success, negative on error

## [◆ ](#ga27d78168c737d56f9f7f3bbdacb808fb)lora\_test\_cw()

| | int lora\_test\_cw | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *frequency*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *tx\_power*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *duration* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[lora.h](lora_8h.md)>`

Transmit an unmodulated continuous wave at a given frequency.

Note
:   Only use this functionality in a test setup where the transmission does not interfere with other devices.

Parameters
:   | dev | LoRa device |
    | --- | --- |
    | frequency | Output frequency (Hertz) |
    | tx\_power | TX power (dBm) |
    | duration | Transmission duration in seconds. |

Returns
:   0 on success, negative on error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
