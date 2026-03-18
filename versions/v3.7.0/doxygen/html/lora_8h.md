---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lora_8h.html
original_path: doxygen/html/lora_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lora.h File Reference

Public LoRa driver APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](lora_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [lora\_modem\_config](structlora__modem__config.md) |
|  | Structure containing the configuration of a LoRa modem. [More...](structlora__modem__config.md#details) |

| Enumerations | |
| --- | --- |
| enum | [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) { [BW\_125\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) = 0 , [BW\_250\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411) , [BW\_500\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9) } |
|  | LoRa signal bandwidth. [More...](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) |
| enum | [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) {     [SF\_6](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) = 6 , [SF\_7](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608) , [SF\_8](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e) , [SF\_9](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc) ,     [SF\_10](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6) , [SF\_11](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407) , [SF\_12](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)   } |
|  | LoRa data-rate. [More...](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) |
| enum | [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) { [CR\_4\_5](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) = 1 , [CR\_4\_6](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) = 2 , [CR\_4\_7](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) = 3 , [CR\_4\_8](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) = 4 } |
|  | LoRa coding rate. [More...](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) |

| Functions | |
| --- | --- |
| static int | [lora\_config](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb) (const struct [device](structdevice.md) \*dev, struct [lora\_modem\_config](structlora__modem__config.md) \*config) |
|  | Configure the LoRa modem. |
| static int | [lora\_send](group__lora__api.md#gad893b49a74e350bb05f42f863af31446) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len) |
|  | Send data over LoRa. |
| static int | [lora\_send\_async](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Asynchronously send data over LoRa. |
| static int | [lora\_recv](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr) |
|  | Receive data over LoRa. |
| static int | [lora\_recv\_async](group__lora__api.md#ga4f7ec5eaff55f295ff82f3e22d77f34c) (const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb) |
|  | Receive data asynchronously over LoRa. |
| static int | [lora\_test\_cw](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration) |
|  | Transmit an unmodulated continuous wave at a given frequency. |

## Detailed Description

Public LoRa driver APIs.

Public LoRa APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [lora.h](lora_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
