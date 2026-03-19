---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lorawan_2emul_8h.html
original_path: doxygen/html/lorawan_2emul_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/lorawan/lorawan.h](lorawan_8h_source.md)>`

[Go to the source code of this file.](lorawan_2emul_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [lorawan\_uplink\_cb\_t](#ad3b92479562707f0819696a5de0baa41)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Defines the emulator uplink callback handler function signature. |

| Functions | |
| --- | --- |
| void | [lorawan\_emul\_send\_downlink](#abedb7884445ac1bb0eb0351a6c413761) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) data\_pending, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Emulate LoRaWAN downlink message. |
| void | [lorawan\_emul\_register\_uplink\_callback](#a665c46cfe16f6c894e44a3bfbbf235b7) ([lorawan\_uplink\_cb\_t](#ad3b92479562707f0819696a5de0baa41) cb) |
|  | Register callback for emulated uplink messages. |

## Typedef Documentation

## [◆ ](#ad3b92479562707f0819696a5de0baa41)lorawan\_uplink\_cb\_t

| typedef void(\* lorawan\_uplink\_cb\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

Defines the emulator uplink callback handler function signature.

Parameters
:   | port | LoRaWAN port |
    | --- | --- |
    | len | Payload data length |
    | data | Pointer to the payload data |

## Function Documentation

## [◆ ](#a665c46cfe16f6c894e44a3bfbbf235b7)lorawan\_emul\_register\_uplink\_callback()

| void lorawan\_emul\_register\_uplink\_callback | ( | [lorawan\_uplink\_cb\_t](#ad3b92479562707f0819696a5de0baa41) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register callback for emulated uplink messages.

Parameters
:   | cb | Pointer to the uplink callback handler function |
    | --- | --- |

## [◆ ](#abedb7884445ac1bb0eb0351a6c413761)lorawan\_emul\_send\_downlink()

| void lorawan\_emul\_send\_downlink | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *port*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *data\_pending*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *rssi*, |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *snr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) |

Emulate LoRaWAN downlink message.

Parameters
:   | port | Port message was sent on |
    | --- | --- |
    | data\_pending | Network server has more downlink packets pending |
    | rssi | Received signal strength in dBm |
    | snr | Signal to Noise ratio in dBm |
    | len | Length of data received, will be 0 for ACKs |
    | data | Data received, will be NULL for ACKs |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [lorawan](dir_025fd8c7c9e823719407606758d0c447.md)
- [emul.h](lorawan_2emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
