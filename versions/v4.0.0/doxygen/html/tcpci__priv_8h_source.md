---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tcpci__priv_8h_source.html
original_path: doxygen/html/tcpci__priv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci\_priv.h

[Go to the documentation of this file.](tcpci__priv_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_TCPCI\_PRIV\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_TCPCI\_PRIV\_H\_

17

18#include <[stdint.h](stdint_8h.md)>

19#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

20#include <[zephyr/usb\_c/usbc.h](usbc_8h.md)>

21

[ 25](structtcpci__reg__dump__map.md)struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) {

[ 27](structtcpci__reg__dump__map.md#ad68dd201d76bfb2193567b8db2ec514a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structtcpci__reg__dump__map.md#ad68dd201d76bfb2193567b8db2ec514a);

[ 29](structtcpci__reg__dump__map.md#a316d7f2a6b4b5fd42eb6450a810b7dd8) const char \*[name](structtcpci__reg__dump__map.md#a316d7f2a6b4b5fd42eb6450a810b7dd8);

[ 31](structtcpci__reg__dump__map.md#a6e84093c1d027233230d8f27b0698756) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [size](structtcpci__reg__dump__map.md#a6e84093c1d027233230d8f27b0698756);

32};

33

[ 35](tcpci__priv_8h.md#a031fe5b188cbe9b4e80e9cff0c845eda)#define TCPCI\_STD\_REGS\_SIZE 38

42extern const struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) [tcpci\_std\_regs](tcpci__priv_8h.md#ab2204d54c7483fb06f02dda83b0066f8)[[TCPCI\_STD\_REGS\_SIZE](tcpci__priv_8h.md#a031fe5b188cbe9b4e80e9cff0c845eda)];

43

[ 52](tcpci__priv_8h.md#aaad4be0dbc4c31e9d3438b7f8a3e8433)int [tcpci\_read\_reg8](tcpci__priv_8h.md#aaad4be0dbc4c31e9d3438b7f8a3e8433)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

53

[ 62](tcpci__priv_8h.md#abbe63527659134a5bc14d6ecefabb0af)int [tcpci\_write\_reg8](tcpci__priv_8h.md#abbe63527659134a5bc14d6ecefabb0af)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

63

[ 74](tcpci__priv_8h.md#a2f4e5571a7f272dd968dc002d70ef3f4)int [tcpci\_update\_reg8](tcpci__priv_8h.md#a2f4e5571a7f272dd968dc002d70ef3f4)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

75

[ 84](tcpci__priv_8h.md#a00557a03647d6bd1ecba157ffff40e46)int [tcpci\_read\_reg16](tcpci__priv_8h.md#a00557a03647d6bd1ecba157ffff40e46)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value);

85

[ 94](tcpci__priv_8h.md#a7db13212d494bcc8c98190f8670fcd34)int [tcpci\_write\_reg16](tcpci__priv_8h.md#a7db13212d494bcc8c98190f8670fcd34)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

95

[ 104](tcpci__priv_8h.md#abafd9380a335483525d8ff5b2b9e2306)enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) [tcpci\_alert\_reg\_to\_enum](tcpci__priv_8h.md#abafd9380a335483525d8ff5b2b9e2306)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg);

105

[ 116](tcpci__priv_8h.md#ade1aa43041be0cc1abcf074b8e4e07e9)int [tcpci\_tcpm\_get\_cc](tcpci__priv_8h.md#ade1aa43041be0cc1abcf074b8e4e07e9)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1,

117 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2);

118

119#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_TCPCI\_PRIV\_H\_ \*/

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed)

tcpc\_alert

TCPC Alert bits.

**Definition** usbc\_tcpc.h:41

[tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c)

tc\_cc\_voltage\_state

CC Voltage status.

**Definition** usbc\_tc.h:308

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

[tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md)

Structure used to bind the register address to name in registers dump.

**Definition** tcpci\_priv.h:25

[tcpci\_reg\_dump\_map::name](structtcpci__reg__dump__map.md#a316d7f2a6b4b5fd42eb6450a810b7dd8)

const char \* name

Human readable name of register.

**Definition** tcpci\_priv.h:29

[tcpci\_reg\_dump\_map::size](structtcpci__reg__dump__map.md#a6e84093c1d027233230d8f27b0698756)

uint8\_t size

Size in bytes of the register.

**Definition** tcpci\_priv.h:31

[tcpci\_reg\_dump\_map::addr](structtcpci__reg__dump__map.md#ad68dd201d76bfb2193567b8db2ec514a)

uint8\_t addr

Address of I2C device register.

**Definition** tcpci\_priv.h:27

[tcpci\_read\_reg16](tcpci__priv_8h.md#a00557a03647d6bd1ecba157ffff40e46)

int tcpci\_read\_reg16(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint16\_t \*value)

Function to read the 16-bit register of TCPCI device.

[TCPCI\_STD\_REGS\_SIZE](tcpci__priv_8h.md#a031fe5b188cbe9b4e80e9cff0c845eda)

#define TCPCI\_STD\_REGS\_SIZE

Size of the array containing the standard registers used by tcpci dump command.

**Definition** tcpci\_priv.h:35

[tcpci\_update\_reg8](tcpci__priv_8h.md#a2f4e5571a7f272dd968dc002d70ef3f4)

int tcpci\_update\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t mask, uint8\_t value)

Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing...

[tcpci\_write\_reg16](tcpci__priv_8h.md#a7db13212d494bcc8c98190f8670fcd34)

int tcpci\_write\_reg16(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint16\_t value)

Function to write a value to the 16-bit register of TCPCI device.

[tcpci\_read\_reg8](tcpci__priv_8h.md#aaad4be0dbc4c31e9d3438b7f8a3e8433)

int tcpci\_read\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t \*value)

Function to read the 8-bit register of TCPCI device.

[tcpci\_std\_regs](tcpci__priv_8h.md#ab2204d54c7483fb06f02dda83b0066f8)

const struct tcpci\_reg\_dump\_map tcpci\_std\_regs[38]

Array containing the standard TCPCI registers list.

[tcpci\_alert\_reg\_to\_enum](tcpci__priv_8h.md#abafd9380a335483525d8ff5b2b9e2306)

enum tcpc\_alert tcpci\_alert\_reg\_to\_enum(uint16\_t reg)

Function that converts the TCPCI alert register to the tcpc\_alert enum The hard reset value takes pri...

[tcpci\_write\_reg8](tcpci__priv_8h.md#abbe63527659134a5bc14d6ecefabb0af)

int tcpci\_write\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t value)

Function to write a value to the 8-bit register of TCPCI device.

[tcpci\_tcpm\_get\_cc](tcpci__priv_8h.md#ade1aa43041be0cc1abcf074b8e4e07e9)

int tcpci\_tcpm\_get\_cc(const struct i2c\_dt\_spec \*bus, enum tc\_cc\_voltage\_state \*cc1, enum tc\_cc\_voltage\_state \*cc2)

Function that reads the CC status registers and converts read values to enums representing voltages s...

[usbc.h](usbc_8h.md)

USB-C Device APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [tcpci\_priv.h](tcpci__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
