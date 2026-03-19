---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tcpci__priv_8h.html
original_path: doxygen/html/tcpci__priv_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci\_priv.h File Reference

Helper functions to use by the TCPCI-compliant drivers.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/usb_c/usbc.h](usbc_8h_source.md)>`

[Go to the source code of this file.](tcpci__priv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) |
|  | Structure used to bind the register address to name in registers dump. [More...](structtcpci__reg__dump__map.md#details) |

| Macros | |
| --- | --- |
| #define | [TCPCI\_STD\_REGS\_SIZE](#a031fe5b188cbe9b4e80e9cff0c845eda)   38 |
|  | Size of the array containing the standard registers used by tcpci dump command. |

| Functions | |
| --- | --- |
| int | [tcpci\_read\_reg8](#aaad4be0dbc4c31e9d3438b7f8a3e8433) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Function to read the 8-bit register of TCPCI device. |
| int | [tcpci\_write\_reg8](#abbe63527659134a5bc14d6ecefabb0af) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Function to write a value to the 8-bit register of TCPCI device. |
| int | [tcpci\_update\_reg8](#a2f4e5571a7f272dd968dc002d70ef3f4) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing this operation atomically. |
| int | [tcpci\_read\_reg16](#a00557a03647d6bd1ecba157ffff40e46) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Function to read the 16-bit register of TCPCI device. |
| int | [tcpci\_write\_reg16](#a7db13212d494bcc8c98190f8670fcd34) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Function to write a value to the 16-bit register of TCPCI device. |
| enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) | [tcpci\_alert\_reg\_to\_enum](#abafd9380a335483525d8ff5b2b9e2306) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg) |
|  | Function that converts the TCPCI alert register to the [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") enum The hard reset value takes priority, where the rest are returned in the bit order from least significant to most significant. |
| int | [tcpci\_tcpm\_get\_cc](#ade1aa43041be0cc1abcf074b8e4e07e9) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
|  | Function that reads the CC status registers and converts read values to enums representing voltages state and partner detection status. |
| int | [tcpci\_tcpm\_get\_chip\_info](#a49a2f453d03c75aaea608a17a85a6c6f) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info) |
|  | Function to retrieve information about the TCPCI chip. |
| int | [tcpci\_tcpm\_dump\_std\_reg](#a005a5b7130913ba80ff21d89f6d0c8a7) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus) |
|  | Function to dump the standard TCPCI registers. |
| int | [tcpci\_tcpm\_set\_bist\_test\_mode](#add2b2c0859e4ab1cf2f0e290e1d71d19) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Function to enable or disable the BIST (Built-In Self-Test) mode. |
| int | [tcpci\_tcpm\_transmit\_data](#a8ac9f08daf0f50749e9df389d1c8d41f) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, struct [pd\_msg](structpd__msg.md) \*msg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retries) |
|  | Function to transmit a PD (Power Delivery) message. |
| int | [tcpci\_tcpm\_select\_rp\_value](#ae2a60d3000187f640331816edbbcbcb6) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp) |
|  | Function to select the Rp (Pull-up Resistor) value. |
| int | [tcpci\_tcpm\_get\_rp\_value](#a2233ff710864ba8ec40f7792e6baf002) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
|  | Function to get the currently selected Rp value. |
| int | [tcpci\_tcpm\_set\_cc](#a56b77c066ecd306d98a9e8e7ca249dc6) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull) |
|  | Function to set the CC pull resistor and set the role as either Source or Sink. |
| int | [tcpci\_tcpm\_set\_drp\_toggle](#ad6024cfb180d53adc737ff4b49b3e5bf) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Function to enable or disable TCPC auto dual role toggle. |
| int | [tcpci\_tcpm\_set\_roles](#a0b0efcd606bdd19925ebaaaed017e5f9) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) pd\_rev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role) |
|  | Function to set the power and data role of the PD message header. |
| int | [tcpci\_tcpm\_set\_rx\_type](#a0223089c1ab73b1ec8c5a2e9de9b2932) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
|  | Function to set the RX type. |
| int | [tcpci\_tcpm\_set\_cc\_polarity](#a87aec00974ff403a0e60b1ee1346ec73) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity) |
|  | Function to set the polarity of the CC lines. |
| int | [tcpci\_tcpm\_set\_vconn](#ac37957893c769d805d997a93198827a7) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Function to enable or disable VCONN. |
| int | [tcpci\_tcpm\_get\_status\_register](#a4568c479db7a136e15b35289126e7109) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*status) |
|  | Function to get the status of a specific TCPCI status register. |
| int | [tcpci\_tcpm\_clear\_status\_register](#aef29ca84b4cc68a55b840e987ec87f28) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask) |
|  | Function to clear specific bits in a TCPCI status register. |
| int | [tcpci\_tcpm\_mask\_status\_register](#aadbf2ef0350b8c54c4da53b7ab79f7d6) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask) |
|  | Function to set the mask of a TCPCI status register. |

| Variables | |
| --- | --- |
| const struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) | [tcpci\_std\_regs](#ab2204d54c7483fb06f02dda83b0066f8) [38] |
|  | Array containing the standard TCPCI registers list. |

## Detailed Description

Helper functions to use by the TCPCI-compliant drivers.

This file contains generic TCPCI functions that may be used by the drivers to TCPCI-compliant devices that want to implement vendor-specific functionality without the need to reimplement the TCPCI generic functionality and register operations.

## Macro Definition Documentation

## [◆ ](#a031fe5b188cbe9b4e80e9cff0c845eda)TCPCI\_STD\_REGS\_SIZE

| #define TCPCI\_STD\_REGS\_SIZE   38 |
| --- |

Size of the array containing the standard registers used by tcpci dump command.

## Function Documentation

## [◆ ](#abafd9380a335483525d8ff5b2b9e2306)tcpci\_alert\_reg\_to\_enum()

| enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) tcpci\_alert\_reg\_to\_enum | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

Function that converts the TCPCI alert register to the [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") enum The hard reset value takes priority, where the rest are returned in the bit order from least significant to most significant.

Parameters
:   | reg | Value of the TCPCI alert register. This parameter must have value other than zero. |
    | --- | --- |

Returns
:   enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") Value of one of the flags being set in the alert register

## [◆ ](#a00557a03647d6bd1ecba157ffff40e46)tcpci\_read\_reg16()

| int tcpci\_read\_reg16 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *value* ) |

Function to read the 16-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Pointer to variable that will store the register value |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#aaad4be0dbc4c31e9d3438b7f8a3e8433)tcpci\_read\_reg8()

| int tcpci\_read\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

Function to read the 8-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Pointer to variable that will store the register value |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#aef29ca84b4cc68a55b840e987ec87f28)tcpci\_tcpm\_clear\_status\_register()

| int tcpci\_tcpm\_clear\_status\_register | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mask* ) |

Function to clear specific bits in a TCPCI status register.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Enum representing the status register to be cleared |
    | mask | Bitmask specifying which bits to clear |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a005a5b7130913ba80ff21d89f6d0c8a7)tcpci\_tcpm\_dump\_std\_reg()

| int tcpci\_tcpm\_dump\_std\_reg | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus* | ) |  |
| --- | --- | --- | --- | --- | --- |

Function to dump the standard TCPCI registers.

Parameters
:   | bus | I2C bus |
    | --- | --- |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#ade1aa43041be0cc1abcf074b8e4e07e9)tcpci\_tcpm\_get\_cc()

| int tcpci\_tcpm\_get\_cc | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc1*, |
|  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc2* ) |

Function that reads the CC status registers and converts read values to enums representing voltages state and partner detection status.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | cc1 | Pointer to variable where detected CC1 voltage state will be stored |
    | cc2 | Pointer to variable where detected CC2 voltage state will be stored |

Returns
:   -EINVAL if cc1 or cc2 pointer is NULL
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a49a2f453d03c75aaea608a17a85a6c6f)tcpci\_tcpm\_get\_chip\_info()

| int tcpci\_tcpm\_get\_chip\_info | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | struct [tcpc\_chip\_info](structtcpc__chip__info.md) \* | *chip\_info* ) |

Function to retrieve information about the TCPCI chip.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | chip\_info | Pointer to the structure where the chip information will be stored |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a2233ff710864ba8ec40f7792e6baf002)tcpci\_tcpm\_get\_rp\_value()

| int tcpci\_tcpm\_get\_rp\_value | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \* | *rp* ) |

Function to get the currently selected Rp value.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | rp | Pointer to the variable where the Rp value will be stored |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a4568c479db7a136e15b35289126e7109)tcpci\_tcpm\_get\_status\_register()

| int tcpci\_tcpm\_get\_status\_register | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *status* ) |

Function to get the status of a specific TCPCI status register.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Enum representing the status register to be read |
    | status | Pointer to the variable where the status will be stored |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#aadbf2ef0350b8c54c4da53b7ab79f7d6)tcpci\_tcpm\_mask\_status\_register()

| int tcpci\_tcpm\_mask\_status\_register | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mask* ) |

Function to set the mask of a TCPCI status register.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Enum representing the status register to be masked |
    | mask | Bitmask specifying which bits to mask |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#ae2a60d3000187f640331816edbbcbcb6)tcpci\_tcpm\_select\_rp\_value()

| int tcpci\_tcpm\_select\_rp\_value | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) | *rp* ) |

Function to select the Rp (Pull-up Resistor) value.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | rp | Enum representing the Rp value to be set |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#add2b2c0859e4ab1cf2f0e290e1d71d19)tcpci\_tcpm\_set\_bist\_test\_mode()

| int tcpci\_tcpm\_set\_bist\_test\_mode | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Function to enable or disable the BIST (Built-In Self-Test) mode.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | enable | Boolean flag to enable (true) or disable (false) BIST mode |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a56b77c066ecd306d98a9e8e7ca249dc6)tcpci\_tcpm\_set\_cc()

| int tcpci\_tcpm\_set\_cc | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) | *pull* ) |

Function to set the CC pull resistor and set the role as either Source or Sink.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | pull | Enum representing the CC pull resistor to be set |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a87aec00974ff403a0e60b1ee1346ec73)tcpci\_tcpm\_set\_cc\_polarity()

| int tcpci\_tcpm\_set\_cc\_polarity | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) | *polarity* ) |

Function to set the polarity of the CC lines.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | polarity | Enum representing the CC polarity to be set |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#ad6024cfb180d53adc737ff4b49b3e5bf)tcpci\_tcpm\_set\_drp\_toggle()

| int tcpci\_tcpm\_set\_drp\_toggle | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Function to enable or disable TCPC auto dual role toggle.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | enable | Boolean flag to enable (true) or disable (false) DRP toggle mode |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a0b0efcd606bdd19925ebaaaed017e5f9)tcpci\_tcpm\_set\_roles()

| int tcpci\_tcpm\_set\_roles | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) | *pd\_rev*, |
|  |  | enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) | *power\_role*, |
|  |  | enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) | *data\_role* ) |

Function to set the power and data role of the PD message header.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | pd\_rev | Enum representing the USB−PD Specification Revision to be set |
    | power\_role | Enum representing the power role to be set |
    | data\_role | Enum representing the data role to be set |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a0223089c1ab73b1ec8c5a2e9de9b2932)tcpci\_tcpm\_set\_rx\_type()

| int tcpci\_tcpm\_set\_rx\_type | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type* ) |

Function to set the RX type.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | type | Value representing the RX type to be set |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#ac37957893c769d805d997a93198827a7)tcpci\_tcpm\_set\_vconn()

| int tcpci\_tcpm\_set\_vconn | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Function to enable or disable VCONN.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | enable | Boolean flag to enable (true) or disable (false) VCONN |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a8ac9f08daf0f50749e9df389d1c8d41f)tcpci\_tcpm\_transmit\_data()

| int tcpci\_tcpm\_transmit\_data | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | struct [pd\_msg](structpd__msg.md) \* | *msg*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *retries* ) |

Function to transmit a PD (Power Delivery) message.

The message is transmitted with a specified number of retries in case of failure.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | msg | Pointer to the PD message structure to be transmitted |
    | retries | Number of retries in case of transmission failure |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a2f4e5571a7f272dd968dc002d70ef3f4)tcpci\_update\_reg8()

| int tcpci\_update\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing this operation atomically.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | mask | Bitmask specifying which bits of the device register will be modified |
    | value | Value that will be written to the device register after being ANDed with mask |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a7db13212d494bcc8c98190f8670fcd34)tcpci\_write\_reg16()

| int tcpci\_write\_reg16 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

Function to write a value to the 16-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Value that will be written to the device register |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#abbe63527659134a5bc14d6ecefabb0af)tcpci\_write\_reg8()

| int tcpci\_write\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

Function to write a value to the 8-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Value that will be written to the device register |

Returns
:   int Status of I2C operation, 0 in case of success

## Variable Documentation

## [◆ ](#ab2204d54c7483fb06f02dda83b0066f8)tcpci\_std\_regs

| | const struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) tcpci\_std\_regs[38] | | --- | | extern |
| --- | --- | --- |

Array containing the standard TCPCI registers list.

If the TCPC driver contain any vendor-specific registers, it may override the TCPCI dump\_std\_reg function tp dump them and should also dump the standard registers using this array.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [tcpci\_priv.h](tcpci__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
