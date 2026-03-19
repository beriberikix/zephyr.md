---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbc__tcpc_8h.html
original_path: doxygen/html/usbc__tcpc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_tcpc.h File Reference

USBC Type-C Port Controller device APIs.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include "[usbc_tc.h](usbc__tc_8h_source.md)"`  
`#include "[usbc_pd.h](usbc__pd_8h_source.md)"`

[Go to the source code of this file.](usbc__tcpc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tcpc\_chip\_info](structtcpc__chip__info.md) |
|  | TCPC Chip Information. [More...](structtcpc__chip__info.md#details) |
| struct | [tcpc\_driver\_api](structtcpc__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7)) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| typedef int(\* | [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2)) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| typedef void(\* | [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925)) (const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) alert) |

| Enumerations | |
| --- | --- |
| enum | [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) {     [TCPC\_ALERT\_CC\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f) , [TCPC\_ALERT\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4) , [TCPC\_ALERT\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb) , [TCPC\_ALERT\_HARD\_RESET\_RECEIVED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0) ,     [TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec) , [TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe) , [TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2) , [TCPC\_ALERT\_VBUS\_ALARM\_HI](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66) ,     [TCPC\_ALERT\_VBUS\_ALARM\_LO](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0) , [TCPC\_ALERT\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e) , [TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752) , [TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd) ,     [TCPC\_ALERT\_BEGINNING\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb) , [TCPC\_ALERT\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9) , [TCPC\_ALERT\_EXTENDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25) , [TCPC\_ALERT\_VENDOR\_DEFINED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)   } |
|  | TCPC Alert bits. [More...](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) |
| enum | [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) {     [TCPC\_ALERT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b) , [TCPC\_CC\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4) , [TCPC\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f) , [TCPC\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440) ,     [TCPC\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d) , [TCPC\_EXTENDED\_ALERT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db) , [TCPC\_VENDOR\_DEFINED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)   } |
|  | TCPC Status register. [More...](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) |

| Functions | |
| --- | --- |
| static int | [tcpc\_is\_cc\_rp](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6)) |
|  | Returns whether the sink has detected a Rp resistor on the other side. |
| static int | [tcpc\_is\_cc\_open](group__usb__type__c__port__controller__api.md#ga0db896e395812603a03548b8faac6791) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if both CC lines are completely open. |
| static int | [tcpc\_is\_cc\_snk\_dbg\_acc](group__usb__type__c__port__controller__api.md#gaa0d2059c3a53df986150141f73b9a98a) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if we detect the port partner is a snk debug accessory. |
| static int | [tcpc\_is\_cc\_src\_dbg\_acc](group__usb__type__c__port__controller__api.md#ga03849a7a4fd7f468b18838c443d1ecd8) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if we detect the port partner is a src debug accessory. |
| static int | [tcpc\_is\_cc\_audio\_acc](group__usb__type__c__port__controller__api.md#ga153054be89d5f21148fe3ee750c718ee) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is an audio accessory. |
| static int | [tcpc\_is\_cc\_at\_least\_one\_rd](group__usb__type__c__port__controller__api.md#gab4e9cc812679cf8cb0189f73a28d7cd2) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is presenting at least one Rd. |
| static int | [tcpc\_is\_cc\_only\_one\_rd](group__usb__type__c__port__controller__api.md#ga91c3c40ea82ce5a081918183d8b76c06) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is presenting Rd on only one CC line. |
| static int | [tcpc\_init](group__usb__type__c__port__controller__api.md#gabc50daa9cc713b1d0e340007e3850ca8) (const struct [device](structdevice.md) \*dev) |
|  | Initializes the TCPC. |
| static int | [tcpc\_get\_cc](group__usb__type__c__port__controller__api.md#ga66ab7a9f3cd1b80cd5bc8e99040c5627) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
|  | Reads the status of the CC lines. |
| static int | [tcpc\_select\_rp\_value](group__usb__type__c__port__controller__api.md#ga3958eac0cc0b9b2ac782e0cdb235036c) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp) |
|  | Sets the value of CC pull up resistor used when operating as a Source. |
| static int | [tcpc\_get\_rp\_value](group__usb__type__c__port__controller__api.md#ga25a110be90977e768623f3a0c9a222d5) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
|  | Gets the value of the CC pull up resistor used when operating as a Source. |
| static int | [tcpc\_set\_cc](group__usb__type__c__port__controller__api.md#gac5737d02caa2b9e649b469bcd648440f) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull) |
|  | Sets the CC pull resistor and sets the role as either Source or Sink. |
| static void | [tcpc\_set\_vconn\_cb](group__usb__type__c__port__controller__api.md#gaa608f2c6627c4a9c3039f0ec1b238bbc) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb) |
|  | Sets a callback that can enable or disable VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC. |
| static void | [tcpc\_set\_vconn\_discharge\_cb](group__usb__type__c__port__controller__api.md#ga975e7edea79de197c7230bd7b7a7efba) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb) |
|  | Sets a callback that can enable or discharge VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC. |
| static int | [tcpc\_vconn\_discharge](group__usb__type__c__port__controller__api.md#ga3937d66636a2b22422caf11c48f7628a) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Discharges VCONN. |
| static int | [tcpc\_set\_vconn](group__usb__type__c__port__controller__api.md#ga247f0ea91249753d6f5eefe006617e41) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables or disables VCONN. |
| static int | [tcpc\_set\_roles](group__usb__type__c__port__controller__api.md#ga8d30c961335f62faa33aa7d842422da0) (const struct [device](structdevice.md) \*dev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role) |
|  | Sets the Power and Data Role of the PD message header. |
| static int | [tcpc\_get\_rx\_pending\_msg](group__usb__type__c__port__controller__api.md#ga34e4caefb0f660b170f97956ac57b707) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*buf) |
|  | Retrieves the Power Delivery message from the TCPC. |
| static int | [tcpc\_set\_rx\_enable](group__usb__type__c__port__controller__api.md#ga905176a77ff127f4df8f6a4f2c61a1b7) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables the reception of SOP\* message types. |
| static int | [tcpc\_set\_cc\_polarity](group__usb__type__c__port__controller__api.md#ga53f0207ecb63011c6dfc3c298a841ed4) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity) |
|  | Sets the polarity of the CC lines. |
| static int | [tcpc\_transmit\_data](group__usb__type__c__port__controller__api.md#ga8bf8fd202d582a4cc179a0fc4aff35e1) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
|  | Transmits a Power Delivery message. |
| static int | [tcpc\_dump\_std\_reg](group__usb__type__c__port__controller__api.md#ga91eef7084b523f1991e000f0592b8cbd) (const struct [device](structdevice.md) \*dev) |
|  | Dump a set of TCPC registers. |
| static int | [tcpc\_set\_alert\_handler\_cb](group__usb__type__c__port__controller__api.md#ga75f0dc246dac576f14c5ac51b45fd489) (const struct [device](structdevice.md) \*dev, [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925) handler, void \*data) |
|  | Sets the alert function that's called when an interrupt is triggered due to an alert bit. |
| static int | [tcpc\_get\_status\_register](group__usb__type__c__port__controller__api.md#gace43dc303d3874a386cc79aa4304b846) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*status) |
|  | Gets a status register. |
| static int | [tcpc\_clear\_status\_register](group__usb__type__c__port__controller__api.md#ga00170b754d78d8eb7da24abd7d533e42) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
|  | Clears a TCPC status register. |
| static int | [tcpc\_mask\_status\_register](group__usb__type__c__port__controller__api.md#ga0d1868d555e99877e062fb7135d9db8f) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
|  | Sets the mask of a TCPC status register. |
| static int | [tcpc\_set\_debug\_accessory](group__usb__type__c__port__controller__api.md#ga01687aa218b25ba137e994a2a55bce23) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Manual control of TCPC DebugAccessory control. |
| static int | [tcpc\_set\_debug\_detach](group__usb__type__c__port__controller__api.md#gaaa38e56e6bc8c41e936d8ed70aaa8a23) (const struct [device](structdevice.md) \*dev) |
|  | Detach from a debug connection. |
| static int | [tcpc\_set\_drp\_toggle](group__usb__type__c__port__controller__api.md#gaa06e156bef46ff3f70cc8c302ddf0a4d) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable TCPC auto dual role toggle. |
| static int | [tcpc\_get\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga0c1cd7bc86c89abf5e348987d34e4623) (const struct [device](structdevice.md) \*dev) |
|  | Queries the current sinking state of the TCPC. |
| static int | [tcpc\_set\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga7a63d55cbe5de1d89aa76e10df0140ed) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the VBUS sinking state of the TCPC. |
| static int | [tcpc\_get\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga03c8c6fc6f4c6adefacbc809588e1f85) (const struct [device](structdevice.md) \*dev) |
|  | Queries the current sourcing state of the TCPC. |
| static int | [tcpc\_set\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga8f06b257d1bd0a17eb3042d204b2e6cd) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the VBUS sourcing state of the TCPC. |
| static int | [tcpc\_set\_bist\_test\_mode](group__usb__type__c__port__controller__api.md#gaccc728a1f27c59a163a5c0a221ab7c18) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls the BIST Mode of the TCPC. |
| static int | [tcpc\_get\_chip\_info](group__usb__type__c__port__controller__api.md#ga894d24140f8675b4f48d759c27f52076) (const struct [device](structdevice.md) \*dev, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info) |
|  | Gets the TCPC firmware version. |
| static int | [tcpc\_set\_low\_power\_mode](group__usb__type__c__port__controller__api.md#ga961a4dc393d58dc44ea19a62c943ed48) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Instructs the TCPC to enter or exit low power mode. |
| static int | [tcpc\_sop\_prime\_enable](group__usb__type__c__port__controller__api.md#gab0f1f5d47c1e2b8ee9eb3d7875a0051e) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables the reception of SOP Prime and optionally SOP Double Prime messages. |

## Detailed Description

USBC Type-C Port Controller device APIs.

This file contains the USB Type-C Port Controller device APIs. All Type-C Port Controller device drivers should implement the APIs described in this file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_tcpc.h](usbc__tcpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
