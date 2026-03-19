---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__cs__capabilities.html
original_path: doxygen/html/structbt__conn__le__cs__capabilities.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_cs\_capabilities Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Remote channel sounding capabilities for LE connections supporting CS.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_config\_supported](#a77aacfd02b354e04d4cc29cc1bf4b779) |
|  | Number of CS configurations. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_consecutive\_procedures\_supported](#ae76fbc0f88525e83717e1d8ef5acae59) |
|  | Maximum number of consecutive CS procedures. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_antennas\_supported](#a4e4c56c5066d02b2a0cd59c067f1e4b9) |
|  | Number of antennas. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_antenna\_paths\_supported](#ac842e123166008ad1ad663f827937a3b) |
|  | Maximum number of antenna paths. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [initiator\_supported](#a6530d2a3fb66d498711856b723acecb7) |
|  | Initiator role. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [reflector\_supported](#a694119619d359d0b7e298edf6201ee20) |
|  | Reflector role. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mode\_3\_supported](#aa1616417e6183cf283cf96efc9a92b8e) |
|  | Mode-3. |
| enum [bt\_conn\_le\_cs\_capability\_rtt\_aa\_only](group__bt__conn.md#gafe14d64a64383b097760764697b035e2) | [rtt\_aa\_only\_precision](#a46c9168328d3fbc98a2625799c733818) |
|  | RTT AA-Only. |
| enum [bt\_conn\_le\_cs\_capability\_rtt\_sounding](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433) | [rtt\_sounding\_precision](#acef0d65ed55ae304fea47006bfb0076f) |
|  | RTT Sounding. |
| enum [bt\_conn\_le\_cs\_capability\_rtt\_random\_payload](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813) | [rtt\_random\_payload\_precision](#abbefdc0268a775712c7abd664adcb6b2) |
|  | RTT Random Payload. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_aa\_only\_n](#abe3c611316bb5f710f355846ee9ec437) |
|  | Number of CS steps needed to achieve the accuracy requirements for RTT AA Only. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_sounding\_n](#a7f35343a1572800850e791ba3ff5ffb1) |
|  | Number of CS steps needed to achieve the accuracy requirements for RTT Sounding. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_random\_payload\_n](#a345d9e43222d77024a8f4283b274b48f) |
|  | Number of CS steps needed to achieve the accuracy requirements for RTT Random Payload. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [phase\_based\_nadm\_sounding\_supported](#a94fd00a7a9b22d649f75c7fdd17590a9) |
|  | Phase-based normalized attack detector metric when a CS\_SYNC with sounding sequence is received. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [phase\_based\_nadm\_random\_supported](#a1a0076a0c97317803976f4aca86afc0d) |
|  | Phase-based normalized attack detector metric when a CS\_SYNC with random sequence is received. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cs\_sync\_2m\_phy\_supported](#a3fd09db5fae9c5e307994a78131199c6) |
|  | CS\_SYNC LE 2M PHY. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cs\_sync\_2m\_2bt\_phy\_supported](#a6513d8ffe7d168441205f6dd656dcbbc) |
|  | CS\_SYNC LE 2M 2BT PHY. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cs\_without\_fae\_supported](#a22604c052da2f8ccf77c81a0a5c628b7) |
|  | Subfeature: CS with no Frequency Actuation Error. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [chsel\_alg\_3c\_supported](#aba0db15183d4fa4ae0e3f1333202e55e) |
|  | Subfeature: Channel Selection Algorithm #3c. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pbr\_from\_rtt\_sounding\_seq\_supported](#ad57f15b4dda88e2b747f30451601c923) |
|  | Subfeature: Phase-based Ranging from RTT sounding sequence. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_ip1\_times\_supported](#a090f869cfe7e39a70cea94afbd5ac376) |
|  | Optional T\_IP1 time durations during CS steps. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_ip2\_times\_supported](#ae93594f360430e9c0c80cf3edcf570f6) |
|  | Optional T\_IP2 time durations during CS steps. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_fcs\_times\_supported](#a1ff1d7d769e3ba915f91bf672a6f8a61) |
|  | Optional T\_FCS time durations during CS steps. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_pm\_times\_supported](#a6e92391b21d4acaebba8a171643f572f) |
|  | Optional T\_PM time durations during CS steps. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_sw\_time](#a5a86629a5ad4203b5efe3802cd8b6ae7) |
|  | Time in microseconds for the antenna switch period of the CS tones. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_snr\_capability](#ad58deea7a825bb5f0bc2ca0034183948) |
|  | Supported SNR levels used in RTT packets. |

## Detailed Description

Remote channel sounding capabilities for LE connections supporting CS.

## Field Documentation

## [◆ ](#aba0db15183d4fa4ae0e3f1333202e55e)chsel\_alg\_3c\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::chsel\_alg\_3c\_supported |
| --- |

Subfeature: Channel Selection Algorithm #3c.

## [◆ ](#a6513d8ffe7d168441205f6dd656dcbbc)cs\_sync\_2m\_2bt\_phy\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::cs\_sync\_2m\_2bt\_phy\_supported |
| --- |

CS\_SYNC LE 2M 2BT PHY.

## [◆ ](#a3fd09db5fae9c5e307994a78131199c6)cs\_sync\_2m\_phy\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::cs\_sync\_2m\_phy\_supported |
| --- |

CS\_SYNC LE 2M PHY.

## [◆ ](#a22604c052da2f8ccf77c81a0a5c628b7)cs\_without\_fae\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::cs\_without\_fae\_supported |
| --- |

Subfeature: CS with no Frequency Actuation Error.

## [◆ ](#a6530d2a3fb66d498711856b723acecb7)initiator\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::initiator\_supported |
| --- |

Initiator role.

## [◆ ](#ac842e123166008ad1ad663f827937a3b)max\_antenna\_paths\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::max\_antenna\_paths\_supported |
| --- |

Maximum number of antenna paths.

## [◆ ](#ae76fbc0f88525e83717e1d8ef5acae59)max\_consecutive\_procedures\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_capabilities::max\_consecutive\_procedures\_supported |
| --- |

Maximum number of consecutive CS procedures.

When set to zero, indicates support for both fixed and indefinite numbers of CS procedures before termination.

## [◆ ](#aa1616417e6183cf283cf96efc9a92b8e)mode\_3\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::mode\_3\_supported |
| --- |

Mode-3.

## [◆ ](#a4e4c56c5066d02b2a0cd59c067f1e4b9)num\_antennas\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::num\_antennas\_supported |
| --- |

Number of antennas.

## [◆ ](#a77aacfd02b354e04d4cc29cc1bf4b779)num\_config\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::num\_config\_supported |
| --- |

Number of CS configurations.

## [◆ ](#ad57f15b4dda88e2b747f30451601c923)pbr\_from\_rtt\_sounding\_seq\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::pbr\_from\_rtt\_sounding\_seq\_supported |
| --- |

Subfeature: Phase-based Ranging from RTT sounding sequence.

## [◆ ](#a1a0076a0c97317803976f4aca86afc0d)phase\_based\_nadm\_random\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::phase\_based\_nadm\_random\_supported |
| --- |

Phase-based normalized attack detector metric when a CS\_SYNC with random sequence is received.

## [◆ ](#a94fd00a7a9b22d649f75c7fdd17590a9)phase\_based\_nadm\_sounding\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::phase\_based\_nadm\_sounding\_supported |
| --- |

Phase-based normalized attack detector metric when a CS\_SYNC with sounding sequence is received.

## [◆ ](#a694119619d359d0b7e298edf6201ee20)reflector\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_conn\_le\_cs\_capabilities::reflector\_supported |
| --- |

Reflector role.

## [◆ ](#abe3c611316bb5f710f355846ee9ec437)rtt\_aa\_only\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::rtt\_aa\_only\_n |
| --- |

Number of CS steps needed to achieve the accuracy requirements for RTT AA Only.

Set to 0 if RTT AA Only isn't supported.

## [◆ ](#a46c9168328d3fbc98a2625799c733818)rtt\_aa\_only\_precision

| enum [bt\_conn\_le\_cs\_capability\_rtt\_aa\_only](group__bt__conn.md#gafe14d64a64383b097760764697b035e2) bt\_conn\_le\_cs\_capabilities::rtt\_aa\_only\_precision |
| --- |

RTT AA-Only.

## [◆ ](#a345d9e43222d77024a8f4283b274b48f)rtt\_random\_payload\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::rtt\_random\_payload\_n |
| --- |

Number of CS steps needed to achieve the accuracy requirements for RTT Random Payload.

Set to 0 if RTT Random Payload isn't supported.

## [◆ ](#abbefdc0268a775712c7abd664adcb6b2)rtt\_random\_payload\_precision

| enum [bt\_conn\_le\_cs\_capability\_rtt\_random\_payload](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813) bt\_conn\_le\_cs\_capabilities::rtt\_random\_payload\_precision |
| --- |

RTT Random Payload.

## [◆ ](#a7f35343a1572800850e791ba3ff5ffb1)rtt\_sounding\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::rtt\_sounding\_n |
| --- |

Number of CS steps needed to achieve the accuracy requirements for RTT Sounding.

Set to 0 if RTT Sounding isn't supported

## [◆ ](#acef0d65ed55ae304fea47006bfb0076f)rtt\_sounding\_precision

| enum [bt\_conn\_le\_cs\_capability\_rtt\_sounding](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433) bt\_conn\_le\_cs\_capabilities::rtt\_sounding\_precision |
| --- |

RTT Sounding.

## [◆ ](#a1ff1d7d769e3ba915f91bf672a6f8a61)t\_fcs\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_capabilities::t\_fcs\_times\_supported |
| --- |

Optional T\_FCS time durations during CS steps.

- Bit 0: 15 us
- Bit 1: 20 us
- Bit 2: 30 us
- Bit 3: 40 us
- Bit 4: 50 us
- Bit 5: 60 us
- Bit 6: 80 us
- Bit 7: 100 us
- Bit 8: 120 us

## [◆ ](#a090f869cfe7e39a70cea94afbd5ac376)t\_ip1\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_capabilities::t\_ip1\_times\_supported |
| --- |

Optional T\_IP1 time durations during CS steps.

- Bit 0: 10 us
- Bit 1: 20 us
- Bit 2: 30 us
- Bit 3: 40 us
- Bit 4: 50 us
- Bit 5: 60 us
- Bit 6: 80 us

## [◆ ](#ae93594f360430e9c0c80cf3edcf570f6)t\_ip2\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_capabilities::t\_ip2\_times\_supported |
| --- |

Optional T\_IP2 time durations during CS steps.

- Bit 0: 10 us
- Bit 1: 20 us
- Bit 2: 30 us
- Bit 3: 40 us
- Bit 4: 50 us
- Bit 5: 60 us
- Bit 6: 80 us

## [◆ ](#a6e92391b21d4acaebba8a171643f572f)t\_pm\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_capabilities::t\_pm\_times\_supported |
| --- |

Optional T\_PM time durations during CS steps.

- Bit 0: 10 us
- Bit 1: 20 us

## [◆ ](#a5a86629a5ad4203b5efe3802cd8b6ae7)t\_sw\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::t\_sw\_time |
| --- |

Time in microseconds for the antenna switch period of the CS tones.

## [◆ ](#ad58deea7a825bb5f0bc2ca0034183948)tx\_snr\_capability

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_capabilities::tx\_snr\_capability |
| --- |

Supported SNR levels used in RTT packets.

- Bit 0: 18dB
- Bit 1: 21dB
- Bit 2: 24dB
- Bit 3: 27dB
- Bit 4: 30dB

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
