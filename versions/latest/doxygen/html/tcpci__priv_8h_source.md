---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tcpci__priv_8h_source.html
original_path: doxygen/html/tcpci__priv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 126](tcpci__priv_8h.md#a49a2f453d03c75aaea608a17a85a6c6f)int [tcpci\_tcpm\_get\_chip\_info](tcpci__priv_8h.md#a49a2f453d03c75aaea608a17a85a6c6f)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info);

127

[ 134](tcpci__priv_8h.md#a005a5b7130913ba80ff21d89f6d0c8a7)int [tcpci\_tcpm\_dump\_std\_reg](tcpci__priv_8h.md#a005a5b7130913ba80ff21d89f6d0c8a7)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus);

135

[ 143](tcpci__priv_8h.md#add2b2c0859e4ab1cf2f0e290e1d71d19)int [tcpci\_tcpm\_set\_bist\_test\_mode](tcpci__priv_8h.md#add2b2c0859e4ab1cf2f0e290e1d71d19)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, bool enable);

144

[ 154](tcpci__priv_8h.md#a8ac9f08daf0f50749e9df389d1c8d41f)int [tcpci\_tcpm\_transmit\_data](tcpci__priv_8h.md#a8ac9f08daf0f50749e9df389d1c8d41f)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, struct [pd\_msg](structpd__msg.md) \*msg,

155 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retries);

156

[ 164](tcpci__priv_8h.md#ae2a60d3000187f640331816edbbcbcb6)int [tcpci\_tcpm\_select\_rp\_value](tcpci__priv_8h.md#ae2a60d3000187f640331816edbbcbcb6)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp);

165

[ 173](tcpci__priv_8h.md#a2233ff710864ba8ec40f7792e6baf002)int [tcpci\_tcpm\_get\_rp\_value](tcpci__priv_8h.md#a2233ff710864ba8ec40f7792e6baf002)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp);

174

[ 182](tcpci__priv_8h.md#a56b77c066ecd306d98a9e8e7ca249dc6)int [tcpci\_tcpm\_set\_cc](tcpci__priv_8h.md#a56b77c066ecd306d98a9e8e7ca249dc6)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull);

183

[ 191](tcpci__priv_8h.md#ad6024cfb180d53adc737ff4b49b3e5bf)int [tcpci\_tcpm\_set\_drp\_toggle](tcpci__priv_8h.md#ad6024cfb180d53adc737ff4b49b3e5bf)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, bool enable);

192

[ 202](tcpci__priv_8h.md#a0b0efcd606bdd19925ebaaaed017e5f9)int [tcpci\_tcpm\_set\_roles](tcpci__priv_8h.md#a0b0efcd606bdd19925ebaaaed017e5f9)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) pd\_rev,

203 enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role);

204

[ 212](tcpci__priv_8h.md#a0223089c1ab73b1ec8c5a2e9de9b2932)int [tcpci\_tcpm\_set\_rx\_type](tcpci__priv_8h.md#a0223089c1ab73b1ec8c5a2e9de9b2932)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type);

213

[ 221](tcpci__priv_8h.md#a87aec00974ff403a0e60b1ee1346ec73)int [tcpci\_tcpm\_set\_cc\_polarity](tcpci__priv_8h.md#a87aec00974ff403a0e60b1ee1346ec73)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity);

222

[ 230](tcpci__priv_8h.md#ac37957893c769d805d997a93198827a7)int [tcpci\_tcpm\_set\_vconn](tcpci__priv_8h.md#ac37957893c769d805d997a93198827a7)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, bool enable);

231

[ 240](tcpci__priv_8h.md#a4568c479db7a136e15b35289126e7109)int [tcpci\_tcpm\_get\_status\_register](tcpci__priv_8h.md#a4568c479db7a136e15b35289126e7109)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

241 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*status);

242

[ 251](tcpci__priv_8h.md#aef29ca84b4cc68a55b840e987ec87f28)int [tcpci\_tcpm\_clear\_status\_register](tcpci__priv_8h.md#aef29ca84b4cc68a55b840e987ec87f28)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

252 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask);

253

[ 262](tcpci__priv_8h.md#aadbf2ef0350b8c54c4da53b7ab79f7d6)int [tcpci\_tcpm\_mask\_status\_register](tcpci__priv_8h.md#aadbf2ef0350b8c54c4da53b7ab79f7d6)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

263 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask);

264

265#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_TCPCI\_PRIV\_H\_ \*/

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700)

pd\_rev\_type

Protocol revision.

**Definition** usbc\_pd.h:859

[tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed)

tcpc\_alert

TCPC Alert bits.

**Definition** usbc\_tcpc.h:41

[tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916)

tcpc\_status\_reg

TCPC Status register.

**Definition** usbc\_tcpc.h:85

[tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada)

tc\_cc\_pull

CC pull resistors.

**Definition** usbc\_tc.h:352

[tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5)

tc\_rp\_value

Pull-Up resistor values.

**Definition** usbc\_tc.h:338

[tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c)

tc\_cc\_voltage\_state

CC Voltage status.

**Definition** usbc\_tc.h:308

[tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2)

tc\_data\_role

Power Delivery Data Role.

**Definition** usbc\_tc.h:389

[tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)

tc\_power\_role

Power Delivery Power Role.

**Definition** usbc\_tc.h:379

[tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db)

tc\_cc\_polarity

Polarity of the CC lines.

**Definition** usbc\_tc.h:401

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

[pd\_msg](structpd__msg.md)

Power Delivery message.

**Definition** usbc\_pd.h:1040

[tcpc\_chip\_info](structtcpc__chip__info.md)

TCPC Chip Information.

**Definition** usbc\_tcpc.h:105

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

[tcpci\_tcpm\_dump\_std\_reg](tcpci__priv_8h.md#a005a5b7130913ba80ff21d89f6d0c8a7)

int tcpci\_tcpm\_dump\_std\_reg(const struct i2c\_dt\_spec \*bus)

Function to dump the standard TCPCI registers.

[tcpci\_tcpm\_set\_rx\_type](tcpci__priv_8h.md#a0223089c1ab73b1ec8c5a2e9de9b2932)

int tcpci\_tcpm\_set\_rx\_type(const struct i2c\_dt\_spec \*bus, uint8\_t type)

Function to set the RX type.

[TCPCI\_STD\_REGS\_SIZE](tcpci__priv_8h.md#a031fe5b188cbe9b4e80e9cff0c845eda)

#define TCPCI\_STD\_REGS\_SIZE

Size of the array containing the standard registers used by tcpci dump command.

**Definition** tcpci\_priv.h:35

[tcpci\_tcpm\_set\_roles](tcpci__priv_8h.md#a0b0efcd606bdd19925ebaaaed017e5f9)

int tcpci\_tcpm\_set\_roles(const struct i2c\_dt\_spec \*bus, enum pd\_rev\_type pd\_rev, enum tc\_power\_role power\_role, enum tc\_data\_role data\_role)

Function to set the power and data role of the PD message header.

[tcpci\_tcpm\_get\_rp\_value](tcpci__priv_8h.md#a2233ff710864ba8ec40f7792e6baf002)

int tcpci\_tcpm\_get\_rp\_value(const struct i2c\_dt\_spec \*bus, enum tc\_rp\_value \*rp)

Function to get the currently selected Rp value.

[tcpci\_update\_reg8](tcpci__priv_8h.md#a2f4e5571a7f272dd968dc002d70ef3f4)

int tcpci\_update\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t mask, uint8\_t value)

Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing...

[tcpci\_tcpm\_get\_status\_register](tcpci__priv_8h.md#a4568c479db7a136e15b35289126e7109)

int tcpci\_tcpm\_get\_status\_register(const struct i2c\_dt\_spec \*bus, enum tcpc\_status\_reg reg, uint16\_t \*status)

Function to get the status of a specific TCPCI status register.

[tcpci\_tcpm\_get\_chip\_info](tcpci__priv_8h.md#a49a2f453d03c75aaea608a17a85a6c6f)

int tcpci\_tcpm\_get\_chip\_info(const struct i2c\_dt\_spec \*bus, struct tcpc\_chip\_info \*chip\_info)

Function to retrieve information about the TCPCI chip.

[tcpci\_tcpm\_set\_cc](tcpci__priv_8h.md#a56b77c066ecd306d98a9e8e7ca249dc6)

int tcpci\_tcpm\_set\_cc(const struct i2c\_dt\_spec \*bus, enum tc\_cc\_pull pull)

Function to set the CC pull resistor and set the role as either Source or Sink.

[tcpci\_write\_reg16](tcpci__priv_8h.md#a7db13212d494bcc8c98190f8670fcd34)

int tcpci\_write\_reg16(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint16\_t value)

Function to write a value to the 16-bit register of TCPCI device.

[tcpci\_tcpm\_set\_cc\_polarity](tcpci__priv_8h.md#a87aec00974ff403a0e60b1ee1346ec73)

int tcpci\_tcpm\_set\_cc\_polarity(const struct i2c\_dt\_spec \*bus, enum tc\_cc\_polarity polarity)

Function to set the polarity of the CC lines.

[tcpci\_tcpm\_transmit\_data](tcpci__priv_8h.md#a8ac9f08daf0f50749e9df389d1c8d41f)

int tcpci\_tcpm\_transmit\_data(const struct i2c\_dt\_spec \*bus, struct pd\_msg \*msg, const uint8\_t retries)

Function to transmit a PD (Power Delivery) message.

[tcpci\_read\_reg8](tcpci__priv_8h.md#aaad4be0dbc4c31e9d3438b7f8a3e8433)

int tcpci\_read\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t \*value)

Function to read the 8-bit register of TCPCI device.

[tcpci\_tcpm\_mask\_status\_register](tcpci__priv_8h.md#aadbf2ef0350b8c54c4da53b7ab79f7d6)

int tcpci\_tcpm\_mask\_status\_register(const struct i2c\_dt\_spec \*bus, enum tcpc\_status\_reg reg, uint16\_t mask)

Function to set the mask of a TCPCI status register.

[tcpci\_std\_regs](tcpci__priv_8h.md#ab2204d54c7483fb06f02dda83b0066f8)

const struct tcpci\_reg\_dump\_map tcpci\_std\_regs[38]

Array containing the standard TCPCI registers list.

[tcpci\_alert\_reg\_to\_enum](tcpci__priv_8h.md#abafd9380a335483525d8ff5b2b9e2306)

enum tcpc\_alert tcpci\_alert\_reg\_to\_enum(uint16\_t reg)

Function that converts the TCPCI alert register to the tcpc\_alert enum The hard reset value takes pri...

[tcpci\_write\_reg8](tcpci__priv_8h.md#abbe63527659134a5bc14d6ecefabb0af)

int tcpci\_write\_reg8(const struct i2c\_dt\_spec \*bus, uint8\_t reg, uint8\_t value)

Function to write a value to the 8-bit register of TCPCI device.

[tcpci\_tcpm\_set\_vconn](tcpci__priv_8h.md#ac37957893c769d805d997a93198827a7)

int tcpci\_tcpm\_set\_vconn(const struct i2c\_dt\_spec \*bus, bool enable)

Function to enable or disable VCONN.

[tcpci\_tcpm\_set\_drp\_toggle](tcpci__priv_8h.md#ad6024cfb180d53adc737ff4b49b3e5bf)

int tcpci\_tcpm\_set\_drp\_toggle(const struct i2c\_dt\_spec \*bus, bool enable)

Function to enable or disable TCPC auto dual role toggle.

[tcpci\_tcpm\_set\_bist\_test\_mode](tcpci__priv_8h.md#add2b2c0859e4ab1cf2f0e290e1d71d19)

int tcpci\_tcpm\_set\_bist\_test\_mode(const struct i2c\_dt\_spec \*bus, bool enable)

Function to enable or disable the BIST (Built-In Self-Test) mode.

[tcpci\_tcpm\_get\_cc](tcpci__priv_8h.md#ade1aa43041be0cc1abcf074b8e4e07e9)

int tcpci\_tcpm\_get\_cc(const struct i2c\_dt\_spec \*bus, enum tc\_cc\_voltage\_state \*cc1, enum tc\_cc\_voltage\_state \*cc2)

Function that reads the CC status registers and converts read values to enums representing voltages s...

[tcpci\_tcpm\_select\_rp\_value](tcpci__priv_8h.md#ae2a60d3000187f640331816edbbcbcb6)

int tcpci\_tcpm\_select\_rp\_value(const struct i2c\_dt\_spec \*bus, enum tc\_rp\_value rp)

Function to select the Rp (Pull-up Resistor) value.

[tcpci\_tcpm\_clear\_status\_register](tcpci__priv_8h.md#aef29ca84b4cc68a55b840e987ec87f28)

int tcpci\_tcpm\_clear\_status\_register(const struct i2c\_dt\_spec \*bus, enum tcpc\_status\_reg reg, uint16\_t mask)

Function to clear specific bits in a TCPCI status register.

[usbc.h](usbc_8h.md)

USB-C Device APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [tcpci\_priv.h](tcpci__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
