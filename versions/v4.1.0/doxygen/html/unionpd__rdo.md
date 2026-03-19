---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionpd__rdo.html
original_path: doxygen/html/unionpd__rdo.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_rdo Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

The Request Data Object (RDO) Shall be returned by the Sink making a request for power.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_or\_max\_operating\_current](#a41d023e9308e6d252f0bc8412a6c6184): 10 |  |
|  | Operating Current 10mA units NOTE: If Give Back Flag is zero, this field is the Maximum Operating Current. [More...](#a41d023e9308e6d252f0bc8412a6c6184) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operating\_current](#a8c11df4b75772cda511bd94e5a297128): 10 |  |
|  | Operating current in 10mA units. [More...](#a8c11df4b75772cda511bd94e5a297128) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#ab4065aee18c3a68df38592122f607343): 3 |  |
|  | Reserved - Shall be set to zero. [More...](#ab4065aee18c3a68df38592122f607343) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unchunked\_ext\_msg\_supported](#ae71e9abde3d69211c7bcfc7b80d18c41): 1 |  |
|  | Unchunked Extended Messages Supported. [More...](#ae71e9abde3d69211c7bcfc7b80d18c41) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [no\_usb\_suspend](#ae90a23cc166373f7bb3c35be0c3967f2): 1 |  |
|  | No USB Suspend. [More...](#ae90a23cc166373f7bb3c35be0c3967f2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comm\_capable](#a30f6044378cad6f277f8694df5611230): 1 |  |
|  | USB Communications Capable. [More...](#a30f6044378cad6f277f8694df5611230) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cap\_mismatch](#afd24863b120085c57e77b8d246effd54): 1 |  |
|  | Capability Mismatch. [More...](#afd24863b120085c57e77b8d246effd54) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [giveback](#ae5ae5d3c823254ab895becc3b01761fe): 1 |  |
|  | Give Back Flag. [More...](#ae5ae5d3c823254ab895becc3b01761fe) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [object\_pos](#aff1b20a6e4905ac714ab5e7af7ff9593): 3 |  |
|  | Object Position (000b is Reserved and Shall Not be used). [More...](#aff1b20a6e4905ac714ab5e7af7ff9593) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba): 1 |  |
|  | Reserved - Shall be set to zero. [More...](#aa5af5685e6d9c3d8a7ec3a40d25b43ba) |
| } | [fixed](#a0b7502c79b0976b8e0d118cae3950191) |
|  | Create a Fixed RDO value See Table 6-19 Fixed and Variable Request Data Object. |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_or\_max\_operating\_current](#a41d023e9308e6d252f0bc8412a6c6184): 10 |  |
|  | Operating Current 10mA units NOTE: If Give Back Flag is zero, this field is the Maximum Operating Current. [More...](#a41d023e9308e6d252f0bc8412a6c6184) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operating\_current](#a8c11df4b75772cda511bd94e5a297128): 10 |  |
|  | Operating current in 10mA units. [More...](#a8c11df4b75772cda511bd94e5a297128) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#ab4065aee18c3a68df38592122f607343): 3 |  |
|  | Reserved - Shall be set to zero. [More...](#ab4065aee18c3a68df38592122f607343) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unchunked\_ext\_msg\_supported](#ae71e9abde3d69211c7bcfc7b80d18c41): 1 |  |
|  | Unchunked Extended Messages Supported. [More...](#ae71e9abde3d69211c7bcfc7b80d18c41) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [no\_usb\_suspend](#ae90a23cc166373f7bb3c35be0c3967f2): 1 |  |
|  | No USB Suspend. [More...](#ae90a23cc166373f7bb3c35be0c3967f2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comm\_capable](#a30f6044378cad6f277f8694df5611230): 1 |  |
|  | USB Communications Capable. [More...](#a30f6044378cad6f277f8694df5611230) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cap\_mismatch](#afd24863b120085c57e77b8d246effd54): 1 |  |
|  | Capability Mismatch. [More...](#afd24863b120085c57e77b8d246effd54) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [giveback](#ae5ae5d3c823254ab895becc3b01761fe): 1 |  |
|  | Give Back Flag. [More...](#ae5ae5d3c823254ab895becc3b01761fe) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [object\_pos](#aff1b20a6e4905ac714ab5e7af7ff9593): 3 |  |
|  | Object Position (000b is Reserved and Shall Not be used). [More...](#aff1b20a6e4905ac714ab5e7af7ff9593) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba): 1 |  |
|  | Reserved - Shall be set to zero. [More...](#aa5af5685e6d9c3d8a7ec3a40d25b43ba) |
| } | [variable](#a82e1adf30b6fc476b794b94cfb379214) |
|  | Create a Variable RDO value See Table 6-19 Fixed and Variable Request Data Object. |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_operating\_power](#ab59da7098c1d33c9269f66dd3ac3fc5b): 10 |  |
|  | Minimum Operating Power in 250mW units. [More...](#ab59da7098c1d33c9269f66dd3ac3fc5b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operating\_power](#a63dd2a9e94f3a61205b95efc0cf79f13): 10 |  |
|  | Operating power in 250mW units. [More...](#a63dd2a9e94f3a61205b95efc0cf79f13) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#ab4065aee18c3a68df38592122f607343): 3 |  |
|  | Reserved - Shall be set to zero. [More...](#ab4065aee18c3a68df38592122f607343) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unchunked\_ext\_msg\_supported](#ae71e9abde3d69211c7bcfc7b80d18c41): 1 |  |
|  | Unchunked Extended Messages Supported. [More...](#ae71e9abde3d69211c7bcfc7b80d18c41) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [no\_usb\_suspend](#ae90a23cc166373f7bb3c35be0c3967f2): 1 |  |
|  | No USB Suspend. [More...](#ae90a23cc166373f7bb3c35be0c3967f2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comm\_capable](#a30f6044378cad6f277f8694df5611230): 1 |  |
|  | USB Communications Capable. [More...](#a30f6044378cad6f277f8694df5611230) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cap\_mismatch](#afd24863b120085c57e77b8d246effd54): 1 |  |
|  | Capability Mismatch. [More...](#afd24863b120085c57e77b8d246effd54) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [giveback](#ae5ae5d3c823254ab895becc3b01761fe): 1 |  |
|  | Give Back Flag. [More...](#ae5ae5d3c823254ab895becc3b01761fe) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [object\_pos](#aff1b20a6e4905ac714ab5e7af7ff9593): 3 |  |
|  | Object Position (000b is Reserved and Shall Not be used). [More...](#aff1b20a6e4905ac714ab5e7af7ff9593) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba): 1 |  |
|  | Reserved - Shall be set to zero. [More...](#aa5af5685e6d9c3d8a7ec3a40d25b43ba) |
| } | [battery](#a5838022e249981be50aee897c16ce56e) |
|  | Create a Battery RDO value See Table 6-20 Battery Request Data Object. |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operating\_current](#a8c11df4b75772cda511bd94e5a297128): 7 |  |
|  | Operating Current 50mA units. [More...](#a8c11df4b75772cda511bd94e5a297128) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#ab4065aee18c3a68df38592122f607343): 2 |  |
|  | Reserved - Shall be set to zero. [More...](#ab4065aee18c3a68df38592122f607343) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [output\_voltage](#ad7a98411aad054f1161b4ce32ef3ee33): 11 |  |
|  | Output Voltage in 20mV units. [More...](#ad7a98411aad054f1161b4ce32ef3ee33) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba): 3 |  |
|  | Reserved - Shall be set to zero. [More...](#aa5af5685e6d9c3d8a7ec3a40d25b43ba) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unchunked\_ext\_msg\_supported](#ae71e9abde3d69211c7bcfc7b80d18c41): 1 |  |
|  | Unchunked Extended Messages Supported. [More...](#ae71e9abde3d69211c7bcfc7b80d18c41) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [no\_usb\_suspend](#ae90a23cc166373f7bb3c35be0c3967f2): 1 |  |
|  | No USB Suspend. [More...](#ae90a23cc166373f7bb3c35be0c3967f2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comm\_capable](#a30f6044378cad6f277f8694df5611230): 1 |  |
|  | USB Communications Capable. [More...](#a30f6044378cad6f277f8694df5611230) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cap\_mismatch](#afd24863b120085c57e77b8d246effd54): 1 |  |
|  | Capability Mismatch. [More...](#afd24863b120085c57e77b8d246effd54) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved2](#a5f8b64ce53d9881a007405a986b6b490): 1 |  |
|  | Reserved - Shall be set to zero. [More...](#a5f8b64ce53d9881a007405a986b6b490) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [object\_pos](#aff1b20a6e4905ac714ab5e7af7ff9593): 3 |  |
|  | Object Position (000b is Reserved and Shall Not be used). [More...](#aff1b20a6e4905ac714ab5e7af7ff9593) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved3](#aa0ddbfb3c345b671f97d4b4e760168b4): 1 |  |
|  | Reserved - Shall be set to zero. [More...](#aa0ddbfb3c345b671f97d4b4e760168b4) |
| } | [augmented](#ad6b45a879e689dcd05bf9e07aedc4d20) |
|  | Create an Augmented RDO value See Table 6-22 Programmable Request Data Object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#a477cf38b68b9386e950c085a1ce4f336) |
|  | Raw RDO value. |

## Detailed Description

The Request Data Object (RDO) Shall be returned by the Sink making a request for power.

See Section 6.4.2 Request Message

## Field Documentation

## [◆ ](#ad6b45a879e689dcd05bf9e07aedc4d20)[struct]

| struct { ... } pd\_rdo::augmented |
| --- |

Create an Augmented RDO value See Table 6-22 Programmable Request Data Object.

## [◆ ](#a5838022e249981be50aee897c16ce56e)[struct]

| struct { ... } pd\_rdo::battery |
| --- |

Create a Battery RDO value See Table 6-20 Battery Request Data Object.

## [◆ ](#afd24863b120085c57e77b8d246effd54)cap\_mismatch

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::cap\_mismatch |
| --- |

Capability Mismatch.

## [◆ ](#a0b7502c79b0976b8e0d118cae3950191)[struct]

| struct { ... } pd\_rdo::fixed |
| --- |

Create a Fixed RDO value See Table 6-19 Fixed and Variable Request Data Object.

## [◆ ](#ae5ae5d3c823254ab895becc3b01761fe)giveback

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::giveback |
| --- |

Give Back Flag.

## [◆ ](#ab59da7098c1d33c9269f66dd3ac3fc5b)min\_operating\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::min\_operating\_power |
| --- |

Minimum Operating Power in 250mW units.

## [◆ ](#a41d023e9308e6d252f0bc8412a6c6184)min\_or\_max\_operating\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::min\_or\_max\_operating\_current |
| --- |

Operating Current 10mA units NOTE: If Give Back Flag is zero, this field is the Maximum Operating Current.

If Give Back Flag is one, this field is the Minimum Operating Current.

## [◆ ](#ae90a23cc166373f7bb3c35be0c3967f2)no\_usb\_suspend

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::no\_usb\_suspend |
| --- |

No USB Suspend.

## [◆ ](#aff1b20a6e4905ac714ab5e7af7ff9593)object\_pos

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::object\_pos |
| --- |

Object Position (000b is Reserved and Shall Not be used).

## [◆ ](#a8c11df4b75772cda511bd94e5a297128)operating\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::operating\_current |
| --- |

Operating current in 10mA units.

Operating Current 50mA units.

## [◆ ](#a63dd2a9e94f3a61205b95efc0cf79f13)operating\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::operating\_power |
| --- |

Operating power in 250mW units.

## [◆ ](#ad7a98411aad054f1161b4ce32ef3ee33)output\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::output\_voltage |
| --- |

Output Voltage in 20mV units.

## [◆ ](#a477cf38b68b9386e950c085a1ce4f336)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::raw\_value |
| --- |

Raw RDO value.

## [◆ ](#ab4065aee18c3a68df38592122f607343)reserved0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::reserved0 |
| --- |

Reserved - Shall be set to zero.

## [◆ ](#aa5af5685e6d9c3d8a7ec3a40d25b43ba)reserved1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::reserved1 |
| --- |

Reserved - Shall be set to zero.

## [◆ ](#a5f8b64ce53d9881a007405a986b6b490)reserved2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::reserved2 |
| --- |

Reserved - Shall be set to zero.

## [◆ ](#aa0ddbfb3c345b671f97d4b4e760168b4)reserved3

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::reserved3 |
| --- |

Reserved - Shall be set to zero.

## [◆ ](#ae71e9abde3d69211c7bcfc7b80d18c41)unchunked\_ext\_msg\_supported

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::unchunked\_ext\_msg\_supported |
| --- |

Unchunked Extended Messages Supported.

## [◆ ](#a30f6044378cad6f277f8694df5611230)usb\_comm\_capable

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_rdo::usb\_comm\_capable |
| --- |

USB Communications Capable.

## [◆ ](#a82e1adf30b6fc476b794b94cfb379214)[struct]

| struct { ... } pd\_rdo::variable |
| --- |

Create a Variable RDO value See Table 6-19 Fixed and Variable Request Data Object.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_rdo](unionpd__rdo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
