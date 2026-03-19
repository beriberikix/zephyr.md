---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__cs__test__param.html
original_path: doxygen/html/structbt__le__cs__test__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_test\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

CS Test parameters.
[More...](#details)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) | [main\_mode](#a93e487780ffb55c66708bd6c3b293456) |
|  | CS mode to be used during the CS procedure. |
| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) | [sub\_mode](#a6b0ce9871c26b0a5c9c98a9339d234e1) |
|  | CS sub-mode to be used during the CS procedure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [main\_mode\_repetition](#ac13c4390574bd9a540b632c3ee387870) |
|  | Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode\_0\_steps](#a84f346fafa174ba8b2acf33ff3db72eb) |
|  | Number of CS mode-0 steps at the beginning of the test CS subevent. |
| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) | [role](#a797dda190cc01447054ee4dc08f2a332) |
|  | CS Test role. |
| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) | [rtt\_type](#ab3af198a629e0fb082a177b6b482771a) |
|  | RTT variant. |
| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) | [cs\_sync\_phy](#a41c70c829d16299eb7d25029ddad01bb) |
|  | CS\_SYNC PHY. |
| enum [bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) | [cs\_sync\_antenna\_selection](#af26b66e0a28e4f3c6fce0dd5ad8a7606) |
|  | Antenna identifier to be used for CS\_SYNC packets. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [subevent\_len](#a78aeb8d6e7ac9565ea19a1ffd51ceb6a) |
|  | CS subevent length in microseconds. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subevent\_interval](#a1bff7f98cb72a9f73b0499b8fc89d262) |
|  | Gap between the start of two consecutive CS subevents (N \* 0.625 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_num\_subevents](#aaf09c64fcfa1a0a4257d805ad9b49d56) |
|  | Maximum allowed number of subevents in the procedure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [transmit\_power\_level](#a5951fa7f55752905a0180e8389c3d245) |
|  | Desired TX power level for the CS procedure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip1\_time](#a02437a42f0c3e8563d1600b02e7ca517) |
|  | Interlude time in microseconds between the RTT packets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip2\_time](#a1ce5f3400442ebdd8cf45f9db6367e58) |
|  | Interlude time in microseconds between the CS tones. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_fcs\_time](#a8a2d1540e35d194729df373c79f9eaf2) |
|  | Time in microseconds for frequency changes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_pm\_time](#a8eb7e6fcf4431513404ac5f75da401a9) |
|  | Time in microseconds for the phase measurement period of the CS tones. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_sw\_time](#a94c3e1dcfb7290b61784c5dcd6a67531) |
|  | Time in microseconds for the antenna switch period of the CS tones. |
| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) | [tone\_antenna\_config\_selection](#aff02c121f9c8ae63a137dbb19bf4acd2) |
|  | Antenna Configuration Index used during antenna switching during the tone phases of CS steps. |
| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) | [initiator\_snr\_control](#aa58cf62583c83e32362216bc060a9a8e) |
|  | Initiator SNR control options. |
| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) | [reflector\_snr\_control](#aaa7305e11ee3e22b10b4ceb3c743d4e9) |
|  | Reflector SNR control options. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [drbg\_nonce](#a3ba9bfaa63f144af3117233e7a7e3d3d) |
|  | Determines octets 14 and 15 of the initial value of the DRBG nonce. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [override\_config](#a0ac14a9e1055870ee33ef83e54c1a248) |
|  | Override configuration. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [channel\_map\_repetition](#a5f0cefe32070be29bc918ff4f7a3a46d) |  |
|  | Number of times the channels indicated by the channel map or channel field are cycled through for non-mode-0 steps within a CS procedure. [More...](#a5f0cefe32070be29bc918ff4f7a3a46d) |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [num\_channels](#acb2eed00edb4cac80ce097b241d8e1c8) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [channels](#aeb66cc7b6744cd1709d6199d2ae2dc98) |  |
| }   [set](#a7eb22e2e410701b2baa5f7d9d7123721) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [channel\_map](#a6092db75cfc8143d2e308fce87c18dfe) [10] |  |
| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0)   [channel\_selection\_type](#ad2f4775d56677c63ef1ff71c0d3bc08a) |  |
| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b)   [ch3c\_shape](#a656de42b2afb3d9c53899d3c4d6f3a88) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ch3c\_jump](#aac51c328149cce847057b913f2733198) |  |
| }   [not\_set](#a1c241926b6d1c57c1bde197c1fb37251) |
| } |  |
| } | [override\_config\_0](#a802545d0c7f560166250d4ad585a7d80) |
|  | override config bit 0. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [main\_mode\_steps](#a1e92044ae3538cb71a9192ebcbd8c884) |  |
| } | [override\_config\_2](#a63e8e44842b894bee57ffdcdee4f2cd0) |
|  | Override config bit 2. |
| struct { |  |
| enum [bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28)   [t\_pm\_tone\_ext](#a905f49912a99c105ce4087c4d3327deb) |  |
| } | [override\_config\_3](#afe036f2effcb41c9a4d888592916c329) |
|  | Override config bit 3. |
| struct { |  |
| enum [bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d)   [tone\_antenna\_permutation](#a22e2ec51e87887b74c8251fa004a4497) |  |
| } | [override\_config\_4](#a40671e60cf8e1ff16e7389f6a24c9bb7) |
|  | Override config bit 4. |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cs\_sync\_aa\_initiator](#a355cdcf57dcafdfdc98959ec6b742cc1) |  |
|  | Access Address used in CS\_SYNC packets sent by the initiator. [More...](#a355cdcf57dcafdfdc98959ec6b742cc1) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cs\_sync\_aa\_reflector](#ad8ce97db93b0fbc267552db64491483a) |  |
|  | Access Address used in CS\_SYNC packets sent by the reflector. [More...](#ad8ce97db93b0fbc267552db64491483a) |
| } | [override\_config\_5](#a9bba99348c662adad1f16194409b2ae1) |
|  | Override config bit 5. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ss\_marker1\_position](#a1404de78072df4910a1823eadcb78cd1) |  |
|  | Bit number where the first marker in the channel sounding sequence starts. [More...](#a1404de78072df4910a1823eadcb78cd1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ss\_marker2\_position](#a093b0425d87266c9cb31c8dc209477ff) |  |
|  | Bit number where the second marker in the channel sounding sequence starts. [More...](#a093b0425d87266c9cb31c8dc209477ff) |
| } | [override\_config\_6](#af4f16878d530ec19294673756e7b6358) |
|  | Override config bit 6. |
| struct { |  |
| enum [bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a)   [ss\_marker\_value](#aad705c92184ed8f1577bac68dc810373) |  |
|  | Value of the Sounding Sequence marker. [More...](#aad705c92184ed8f1577bac68dc810373) |
| } | [override\_config\_7](#a9a2763c3062b2ee4d8a1d70393ed2aa2) |
|  | Override config bit 7. |
| struct { |  |
| enum [bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb)   [cs\_sync\_payload\_pattern](#ace81aeaeefc788ccf6bb1b6c491ff0b2) |  |
|  | CS\_SYNC payload pattern selection. [More...](#ace81aeaeefc788ccf6bb1b6c491ff0b2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [cs\_sync\_user\_payload](#a79ce15e5034572a4b5015240b7db4de5) [16] |  |
|  | User payload for CS\_SYNC packets. [More...](#a79ce15e5034572a4b5015240b7db4de5) |
| } | [override\_config\_8](#afb85cec959d8bd59b560828af14dbced) |
|  | Override config bit 8. |

## Detailed Description

CS Test parameters.

## Field Documentation

## [◆ ](#aac51c328149cce847057b913f2733198)ch3c\_jump

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::ch3c\_jump |
| --- |

## [◆ ](#a656de42b2afb3d9c53899d3c4d6f3a88)ch3c\_shape

| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) bt\_le\_cs\_test\_param::ch3c\_shape |
| --- |

## [◆ ](#a6092db75cfc8143d2e308fce87c18dfe)channel\_map

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::channel\_map[10] |
| --- |

## [◆ ](#a5f0cefe32070be29bc918ff4f7a3a46d)channel\_map\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::channel\_map\_repetition |
| --- |

Number of times the channels indicated by the channel map or channel field are cycled through for non-mode-0 steps within a CS procedure.

## [◆ ](#ad2f4775d56677c63ef1ff71c0d3bc08a)channel\_selection\_type

| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) bt\_le\_cs\_test\_param::channel\_selection\_type |
| --- |

## [◆ ](#aeb66cc7b6744cd1709d6199d2ae2dc98)channels

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_le\_cs\_test\_param::channels |
| --- |

## [◆ ](#a355cdcf57dcafdfdc98959ec6b742cc1)cs\_sync\_aa\_initiator

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_cs\_test\_param::cs\_sync\_aa\_initiator |
| --- |

Access Address used in CS\_SYNC packets sent by the initiator.

## [◆ ](#ad8ce97db93b0fbc267552db64491483a)cs\_sync\_aa\_reflector

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_cs\_test\_param::cs\_sync\_aa\_reflector |
| --- |

Access Address used in CS\_SYNC packets sent by the reflector.

## [◆ ](#af26b66e0a28e4f3c6fce0dd5ad8a7606)cs\_sync\_antenna\_selection

| enum [bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) bt\_le\_cs\_test\_param::cs\_sync\_antenna\_selection |
| --- |

Antenna identifier to be used for CS\_SYNC packets.

## [◆ ](#ace81aeaeefc788ccf6bb1b6c491ff0b2)cs\_sync\_payload\_pattern

| enum [bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb) bt\_le\_cs\_test\_param::cs\_sync\_payload\_pattern |
| --- |

CS\_SYNC payload pattern selection.

## [◆ ](#a41c70c829d16299eb7d25029ddad01bb)cs\_sync\_phy

| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) bt\_le\_cs\_test\_param::cs\_sync\_phy |
| --- |

CS\_SYNC PHY.

## [◆ ](#a79ce15e5034572a4b5015240b7db4de5)cs\_sync\_user\_payload

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::cs\_sync\_user\_payload[16] |
| --- |

User payload for CS\_SYNC packets.

This parameter is only used when using [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_USER](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1 "BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER")

The least significant bit corresponds to the most significant bit of the CS payload. When the sequence is less than 16 octets, the least significant octets shall be padded with zeros.

## [◆ ](#a3ba9bfaa63f144af3117233e7a7e3d3d)drbg\_nonce

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_test\_param::drbg\_nonce |
| --- |

Determines octets 14 and 15 of the initial value of the DRBG nonce.

## [◆ ](#aa58cf62583c83e32362216bc060a9a8e)initiator\_snr\_control

| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) bt\_le\_cs\_test\_param::initiator\_snr\_control |
| --- |

Initiator SNR control options.

## [◆ ](#a93e487780ffb55c66708bd6c3b293456)main\_mode

| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) bt\_le\_cs\_test\_param::main\_mode |
| --- |

CS mode to be used during the CS procedure.

## [◆ ](#ac13c4390574bd9a540b632c3ee387870)main\_mode\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::main\_mode\_repetition |
| --- |

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event.

## [◆ ](#a1e92044ae3538cb71a9192ebcbd8c884)main\_mode\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::main\_mode\_steps |
| --- |

## [◆ ](#aaf09c64fcfa1a0a4257d805ad9b49d56)max\_num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::max\_num\_subevents |
| --- |

Maximum allowed number of subevents in the procedure.

A value of 0 means that this parameter is ignored.

## [◆ ](#a84f346fafa174ba8b2acf33ff3db72eb)mode\_0\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::mode\_0\_steps |
| --- |

Number of CS mode-0 steps at the beginning of the test CS subevent.

## [◆ ](#a1c241926b6d1c57c1bde197c1fb37251)[struct]

| struct { ... } bt\_le\_cs\_test\_param::not\_set |
| --- |

## [◆ ](#acb2eed00edb4cac80ce097b241d8e1c8)num\_channels

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::num\_channels |
| --- |

## [◆ ](#a0ac14a9e1055870ee33ef83e54c1a248)override\_config

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_test\_param::override\_config |
| --- |

Override configuration.

This parameter is used to override CS parameters from the DRBG. Each bit configures a different set of parameters.

All overrides are optional, except for those configured by bit 0.

These are:

- Bit 0 set: Override using list of channels
- Bit 0 not set: Override using channel map
- Bit 2 set: Override main mode steps
- Bit 3 set: Override T\_PM\_Tone\_Ext
- Bit 4 set: Override tone antenna permutation
- Bit 5 set: Override CS\_SYNC AA
- Bit 6 set: Override SS marker positions
- Bit 7 set: Override SS marker value
- Bit 8 set: Override CS\_SYNC payload pattern and user payload
- Bit 10 set: Procedure is replaced with a stable phase test

## [◆ ](#a802545d0c7f560166250d4ad585a7d80)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_0 |
| --- |

override config bit 0.

## [◆ ](#a63e8e44842b894bee57ffdcdee4f2cd0)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_2 |
| --- |

Override config bit 2.

These parameters are ignored if the bit is not set.

## [◆ ](#afe036f2effcb41c9a4d888592916c329)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_3 |
| --- |

Override config bit 3.

These parameters are ignored if the bit is not set.

## [◆ ](#a40671e60cf8e1ff16e7389f6a24c9bb7)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_4 |
| --- |

Override config bit 4.

These parameters are ignored if the bit is not set.

## [◆ ](#a9bba99348c662adad1f16194409b2ae1)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_5 |
| --- |

Override config bit 5.

These parameters are ignored if the bit is not set.

## [◆ ](#af4f16878d530ec19294673756e7b6358)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_6 |
| --- |

Override config bit 6.

These parameters are ignored if the bit is not set.

## [◆ ](#a9a2763c3062b2ee4d8a1d70393ed2aa2)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_7 |
| --- |

Override config bit 7.

These parameters are ignored if the bit is not set.

## [◆ ](#afb85cec959d8bd59b560828af14dbced)[struct]

| struct { ... } bt\_le\_cs\_test\_param::override\_config\_8 |
| --- |

Override config bit 8.

These parameters are ignored if the bit is not set.

## [◆ ](#aaa7305e11ee3e22b10b4ceb3c743d4e9)reflector\_snr\_control

| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) bt\_le\_cs\_test\_param::reflector\_snr\_control |
| --- |

Reflector SNR control options.

## [◆ ](#a797dda190cc01447054ee4dc08f2a332)role

| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) bt\_le\_cs\_test\_param::role |
| --- |

CS Test role.

## [◆ ](#ab3af198a629e0fb082a177b6b482771a)rtt\_type

| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) bt\_le\_cs\_test\_param::rtt\_type |
| --- |

RTT variant.

## [◆ ](#a7eb22e2e410701b2baa5f7d9d7123721)[struct]

| struct { ... } bt\_le\_cs\_test\_param::set |
| --- |

## [◆ ](#a1404de78072df4910a1823eadcb78cd1)ss\_marker1\_position

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::ss\_marker1\_position |
| --- |

Bit number where the first marker in the channel sounding sequence starts.

Must be between 0 and 28 when using [BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc "BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING").

## [◆ ](#a093b0425d87266c9cb31c8dc209477ff)ss\_marker2\_position

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::ss\_marker2\_position |
| --- |

Bit number where the second marker in the channel sounding sequence starts.

Must be between 67 and 92 when using [BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2 "BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING").

A value of [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_2\_POSITION\_NOT\_PRESENT](hci__types_8h.md#a1f2bfc1afab1928321c01beddb658f01 "BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT") indicates that this sounding sequence or marker is not present.

## [◆ ](#aad705c92184ed8f1577bac68dc810373)ss\_marker\_value

| enum [bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a) bt\_le\_cs\_test\_param::ss\_marker\_value |
| --- |

Value of the Sounding Sequence marker.

## [◆ ](#a6b0ce9871c26b0a5c9c98a9339d234e1)sub\_mode

| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) bt\_le\_cs\_test\_param::sub\_mode |
| --- |

CS sub-mode to be used during the CS procedure.

## [◆ ](#a1bff7f98cb72a9f73b0499b8fc89d262)subevent\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_test\_param::subevent\_interval |
| --- |

Gap between the start of two consecutive CS subevents (N \* 0.625 ms).

A value of 0 means that there is only one CS subevent.

## [◆ ](#a78aeb8d6e7ac9565ea19a1ffd51ceb6a)subevent\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_cs\_test\_param::subevent\_len |
| --- |

CS subevent length in microseconds.

Range: 1250us to 4s

## [◆ ](#a8a2d1540e35d194729df373c79f9eaf2)t\_fcs\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::t\_fcs\_time |
| --- |

Time in microseconds for frequency changes.

Valid options are:

- 15 us
- 20 us
- 30 us
- 40 us
- 50 us
- 60 us
- 80 us
- 100 us
- 120 us
- 150 us

## [◆ ](#a02437a42f0c3e8563d1600b02e7ca517)t\_ip1\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::t\_ip1\_time |
| --- |

Interlude time in microseconds between the RTT packets.

Valid options are:

- 10 us
- 20 us
- 30 us
- 40 us
- 50 us
- 60 us
- 80 us
- 145 us

## [◆ ](#a1ce5f3400442ebdd8cf45f9db6367e58)t\_ip2\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::t\_ip2\_time |
| --- |

Interlude time in microseconds between the CS tones.

Valid options are:

- 10 us
- 20 us
- 30 us
- 40 us
- 50 us
- 60 us
- 80 us
- 145 us

## [◆ ](#a8eb7e6fcf4431513404ac5f75da401a9)t\_pm\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::t\_pm\_time |
| --- |

Time in microseconds for the phase measurement period of the CS tones.

Valid options are:

- 10 us
- 20 us
- 40 us

## [◆ ](#a905f49912a99c105ce4087c4d3327deb)t\_pm\_tone\_ext

| enum [bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28) bt\_le\_cs\_test\_param::t\_pm\_tone\_ext |
| --- |

## [◆ ](#a94c3e1dcfb7290b61784c5dcd6a67531)t\_sw\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::t\_sw\_time |
| --- |

Time in microseconds for the antenna switch period of the CS tones.

Valid options are:

- 0 us
- 1 us
- 2 us
- 4 us
- 10 us

## [◆ ](#aff02c121f9c8ae63a137dbb19bf4acd2)tone\_antenna\_config\_selection

| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) bt\_le\_cs\_test\_param::tone\_antenna\_config\_selection |
| --- |

Antenna Configuration Index used during antenna switching during the tone phases of CS steps.

## [◆ ](#a22e2ec51e87887b74c8251fa004a4497)tone\_antenna\_permutation

| enum [bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d) bt\_le\_cs\_test\_param::tone\_antenna\_permutation |
| --- |

## [◆ ](#a5951fa7f55752905a0180e8389c3d245)transmit\_power\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_test\_param::transmit\_power\_level |
| --- |

Desired TX power level for the CS procedure.

Value range is [BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER](hci__types_8h.md#a040315a8ac4f80a2c497919a2fd4d7bc "BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER") to [BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER](hci__types_8h.md#a29a240b2d3f209b1f5f3d96e380dde08 "BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER").

Special values:

- [BT\_HCI\_OP\_LE\_CS\_TEST\_MAXIMIZE\_TX\_POWER](hci__types_8h.md#a50eb827977c0c596cb357ed62a6e80bd "BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER") tells the controller it should use as high a transmit power as possible
- [BT\_HCI\_OP\_LE\_CS\_TEST\_MINIMIZE\_TX\_POWER](hci__types_8h.md#a500597c78a6ada65d1224960bf6a370f "BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER") tells the controller it should use as low a transmit power as possible

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
