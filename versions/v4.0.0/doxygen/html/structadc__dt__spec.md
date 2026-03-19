---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structadc__dt__spec.html
original_path: doxygen/html/structadc__dt__spec.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ADC driver APIs](group__adc__interface.md)

Container for ADC channel information specified in devicetree.
[More...](#details)

`#include <[adc.h](drivers_2adc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#aa2656b923d105743eaee3e03691edc44) |
|  | Pointer to the device structure for the ADC driver instance used by this io-channel. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_id](#a083e6c5bc707606c2ea1459fb58e29a8) |
|  | ADC channel identifier used by this io-channel. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [channel\_cfg\_dt\_node\_exists](#aaf239b0c62b34158bac1a3b63e35f612) |
|  | Flag indicating whether configuration of the associated ADC channel is provided as a child node of the corresponding ADC controller in devicetree. |
| struct [adc\_channel\_cfg](structadc__channel__cfg.md) | [channel\_cfg](#a056b22daa13da07cb3ff37bd4adf199d) |
|  | Configuration of the associated ADC channel specified in devicetree. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vref\_mv](#a9e120f52e3a905768d8e6bdc3469d20a) |
|  | Voltage of the reference selected for the channel or 0 if this value is not provided in devicetree. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [resolution](#abbe7052a144541b8d16afee3fd231c10) |
|  | ADC resolution to be used for that channel. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [oversampling](#aa7daf451a3438847ff989f32eae11e97) |
|  | Oversampling setting to be used for that channel. |

## Detailed Description

Container for ADC channel information specified in devicetree.

See also
:   [ADC\_DT\_SPEC\_GET\_BY\_IDX](group__adc__interface.md#gae9867df7a034d45ed3d3c58c69c246ed "Get ADC io-channel information from devicetree.")
:   [ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7 "Equivalent to ADC_DT_SPEC_GET_BY_IDX(node_id, 0).")

## Field Documentation

## [◆ ](#a056b22daa13da07cb3ff37bd4adf199d)channel\_cfg

| struct [adc\_channel\_cfg](structadc__channel__cfg.md) adc\_dt\_spec::channel\_cfg |
| --- |

Configuration of the associated ADC channel specified in devicetree.

This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

## [◆ ](#aaf239b0c62b34158bac1a3b63e35f612)channel\_cfg\_dt\_node\_exists

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) adc\_dt\_spec::channel\_cfg\_dt\_node\_exists |
| --- |

Flag indicating whether configuration of the associated ADC channel is provided as a child node of the corresponding ADC controller in devicetree.

## [◆ ](#a083e6c5bc707606c2ea1459fb58e29a8)channel\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_dt\_spec::channel\_id |
| --- |

ADC channel identifier used by this io-channel.

## [◆ ](#aa2656b923d105743eaee3e03691edc44)dev

| const struct [device](structdevice.md)\* adc\_dt\_spec::dev |
| --- |

Pointer to the device structure for the ADC driver instance used by this io-channel.

## [◆ ](#aa7daf451a3438847ff989f32eae11e97)oversampling

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_dt\_spec::oversampling |
| --- |

Oversampling setting to be used for that channel.

This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

## [◆ ](#abbe7052a144541b8d16afee3fd231c10)resolution

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_dt\_spec::resolution |
| --- |

ADC resolution to be used for that channel.

This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

## [◆ ](#a9e120f52e3a905768d8e6bdc3469d20a)vref\_mv

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) adc\_dt\_spec::vref\_mv |
| --- |

Voltage of the reference selected for the channel or 0 if this value is not provided in devicetree.

This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[adc.h](drivers_2adc_8h_source.md)

- [adc\_dt\_spec](structadc__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
