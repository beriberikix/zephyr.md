---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usb__type__c__port__controller__api.html
original_path: doxygen/html/group__usb__type__c__port__controller__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Type-C Port Controller API

[Device Driver APIs](group__io__interfaces.md)

USB Type-C Port Controller API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [tcpc\_chip\_info](structtcpc__chip__info.md) |
|  | TCPC Chip Information. [More...](structtcpc__chip__info.md#details) |
| struct | [tcpc\_driver\_api](structtcpc__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [tcpc\_vconn\_control\_cb\_t](#ga7a989ffd6bdc83696188de59acbd49c7)) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| typedef int(\* | [tcpc\_vconn\_discharge\_cb\_t](#ga4437e66605f988be1e16c52b9912e9c2)) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| typedef void(\* | [tcpc\_alert\_handler\_cb\_t](#ga5f42fa12f90d34961eeeb67c0dc4f925)) (const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](#ga4687047910cad0dd970bbd28adcf22ed) alert) |

| Enumerations | |
| --- | --- |
| enum | [tcpc\_alert](#ga4687047910cad0dd970bbd28adcf22ed) {     [TCPC\_ALERT\_CC\_STATUS](#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f) , [TCPC\_ALERT\_POWER\_STATUS](#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4) , [TCPC\_ALERT\_MSG\_STATUS](#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb) , [TCPC\_ALERT\_HARD\_RESET\_RECEIVED](#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0) ,     [TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED](#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec) , [TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED](#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe) , [TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS](#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2) , [TCPC\_ALERT\_VBUS\_ALARM\_HI](#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66) ,     [TCPC\_ALERT\_VBUS\_ALARM\_LO](#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0) , [TCPC\_ALERT\_FAULT\_STATUS](#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e) , [TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW](#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752) , [TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT](#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd) ,     [TCPC\_ALERT\_BEGINNING\_MSG\_STATUS](#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb) , [TCPC\_ALERT\_EXTENDED\_STATUS](#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9) , [TCPC\_ALERT\_EXTENDED](#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25) , [TCPC\_ALERT\_VENDOR\_DEFINED](#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)   } |
|  | TCPC Alert bits. [More...](#ga4687047910cad0dd970bbd28adcf22ed) |
| enum | [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) {     [TCPC\_ALERT\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b) , [TCPC\_CC\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4) , [TCPC\_POWER\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f) , [TCPC\_FAULT\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440) ,     [TCPC\_EXTENDED\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d) , [TCPC\_EXTENDED\_ALERT\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db) , [TCPC\_VENDOR\_DEFINED\_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)   } |
|  | TCPC Status register. [More...](#gafd8253dfa6abc80d0717b17271ed8916) |

| Functions | |
| --- | --- |
| static int | [tcpc\_is\_cc\_rp](#ga6dfd68915ffe093058f6187b770a2436) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6)) |
|  | Returns whether the sink has detected a Rp resistor on the other side. |
| static int | [tcpc\_is\_cc\_open](#ga0db896e395812603a03548b8faac6791) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if both CC lines are completely open. |
| static int | [tcpc\_is\_cc\_snk\_dbg\_acc](#gaa0d2059c3a53df986150141f73b9a98a) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if we detect the port partner is a snk debug accessory. |
| static int | [tcpc\_is\_cc\_src\_dbg\_acc](#ga03849a7a4fd7f468b18838c443d1ecd8) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if we detect the port partner is a src debug accessory. |
| static int | [tcpc\_is\_cc\_audio\_acc](#ga153054be89d5f21148fe3ee750c718ee) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is an audio accessory. |
| static int | [tcpc\_is\_cc\_at\_least\_one\_rd](#gab4e9cc812679cf8cb0189f73a28d7cd2) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is presenting at least one Rd. |
| static int | [tcpc\_is\_cc\_only\_one\_rd](#ga91c3c40ea82ce5a081918183d8b76c06) (enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2) |
|  | Returns true if the port partner is presenting Rd on only one CC line. |
| static int | [tcpc\_init](#gabc50daa9cc713b1d0e340007e3850ca8) (const struct [device](structdevice.md) \*dev) |
|  | Initializes the TCPC. |
| static int | [tcpc\_get\_cc](#ga66ab7a9f3cd1b80cd5bc8e99040c5627) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
|  | Reads the status of the CC lines. |
| static int | [tcpc\_select\_rp\_value](#ga3958eac0cc0b9b2ac782e0cdb235036c) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp) |
|  | Sets the value of CC pull up resistor used when operating as a Source. |
| static int | [tcpc\_get\_rp\_value](#ga25a110be90977e768623f3a0c9a222d5) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
|  | Gets the value of the CC pull up resistor used when operating as a Source. |
| static int | [tcpc\_set\_cc](#gac5737d02caa2b9e649b469bcd648440f) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull) |
|  | Sets the CC pull resistor and sets the role as either Source or Sink. |
| static void | [tcpc\_set\_vconn\_cb](#gaa608f2c6627c4a9c3039f0ec1b238bbc) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_control\_cb\_t](#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb) |
|  | Sets a callback that can enable or disable VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC. |
| static void | [tcpc\_set\_vconn\_discharge\_cb](#ga975e7edea79de197c7230bd7b7a7efba) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_discharge\_cb\_t](#ga4437e66605f988be1e16c52b9912e9c2) cb) |
|  | Sets a callback that can enable or discharge VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC. |
| static int | [tcpc\_vconn\_discharge](#ga3937d66636a2b22422caf11c48f7628a) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Discharges VCONN. |
| static int | [tcpc\_set\_vconn](#ga247f0ea91249753d6f5eefe006617e41) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables or disables VCONN. |
| static int | [tcpc\_set\_roles](#ga8d30c961335f62faa33aa7d842422da0) (const struct [device](structdevice.md) \*dev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role) |
|  | Sets the Power and Data Role of the PD message header. |
| static int | [tcpc\_get\_rx\_pending\_msg](#ga34e4caefb0f660b170f97956ac57b707) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*buf) |
|  | Retrieves the Power Delivery message from the TCPC. |
| static int | [tcpc\_set\_rx\_enable](#ga905176a77ff127f4df8f6a4f2c61a1b7) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables the reception of SOP\* message types. |
| static int | [tcpc\_set\_cc\_polarity](#ga53f0207ecb63011c6dfc3c298a841ed4) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity) |
|  | Sets the polarity of the CC lines. |
| static int | [tcpc\_transmit\_data](#ga8bf8fd202d582a4cc179a0fc4aff35e1) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
|  | Transmits a Power Delivery message. |
| static int | [tcpc\_dump\_std\_reg](#ga91eef7084b523f1991e000f0592b8cbd) (const struct [device](structdevice.md) \*dev) |
|  | Dump a set of TCPC registers. |
| static int | [tcpc\_set\_alert\_handler\_cb](#ga75f0dc246dac576f14c5ac51b45fd489) (const struct [device](structdevice.md) \*dev, [tcpc\_alert\_handler\_cb\_t](#ga5f42fa12f90d34961eeeb67c0dc4f925) handler, void \*data) |
|  | Sets the alert function that's called when an interrupt is triggered due to an alert bit. |
| static int | [tcpc\_get\_status\_register](#gace43dc303d3874a386cc79aa4304b846) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*status) |
|  | Gets a status register. |
| static int | [tcpc\_clear\_status\_register](#ga00170b754d78d8eb7da24abd7d533e42) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
|  | Clears a TCPC status register. |
| static int | [tcpc\_mask\_status\_register](#ga0d1868d555e99877e062fb7135d9db8f) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
|  | Sets the mask of a TCPC status register. |
| static int | [tcpc\_set\_debug\_accessory](#ga01687aa218b25ba137e994a2a55bce23) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Manual control of TCPC DebugAccessory control. |
| static int | [tcpc\_set\_debug\_detach](#gaaa38e56e6bc8c41e936d8ed70aaa8a23) (const struct [device](structdevice.md) \*dev) |
|  | Detach from a debug connection. |
| static int | [tcpc\_set\_drp\_toggle](#gaa06e156bef46ff3f70cc8c302ddf0a4d) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable TCPC auto dual role toggle. |
| static int | [tcpc\_get\_snk\_ctrl](#ga0c1cd7bc86c89abf5e348987d34e4623) (const struct [device](structdevice.md) \*dev) |
|  | Queries the current sinking state of the TCPC. |
| static int | [tcpc\_set\_snk\_ctrl](#ga7a63d55cbe5de1d89aa76e10df0140ed) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the VBUS sinking state of the TCPC. |
| static int | [tcpc\_get\_src\_ctrl](#ga03c8c6fc6f4c6adefacbc809588e1f85) (const struct [device](structdevice.md) \*dev) |
|  | Queries the current sourcing state of the TCPC. |
| static int | [tcpc\_set\_src\_ctrl](#ga8f06b257d1bd0a17eb3042d204b2e6cd) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the VBUS sourcing state of the TCPC. |
| static int | [tcpc\_set\_bist\_test\_mode](#gaccc728a1f27c59a163a5c0a221ab7c18) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls the BIST Mode of the TCPC. |
| static int | [tcpc\_get\_chip\_info](#ga894d24140f8675b4f48d759c27f52076) (const struct [device](structdevice.md) \*dev, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info) |
|  | Gets the TCPC firmware version. |
| static int | [tcpc\_set\_low\_power\_mode](#ga961a4dc393d58dc44ea19a62c943ed48) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Instructs the TCPC to enter or exit low power mode. |
| static int | [tcpc\_sop\_prime\_enable](#gab0f1f5d47c1e2b8ee9eb3d7875a0051e) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enables the reception of SOP Prime and optionally SOP Double Prime messages. |

## Detailed Description

USB Type-C Port Controller API.

Since
:   3.1

Version
:   0.1.0

## Typedef Documentation

## [◆ ](#ga5f42fa12f90d34961eeeb67c0dc4f925)tcpc\_alert\_handler\_cb\_t

| typedef void(\* tcpc\_alert\_handler\_cb\_t) (const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](#ga4687047910cad0dd970bbd28adcf22ed) alert) |
| --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

## [◆ ](#ga7a989ffd6bdc83696188de59acbd49c7)tcpc\_vconn\_control\_cb\_t

| typedef int(\* tcpc\_vconn\_control\_cb\_t) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

## [◆ ](#ga4437e66605f988be1e16c52b9912e9c2)tcpc\_vconn\_discharge\_cb\_t

| typedef int(\* tcpc\_vconn\_discharge\_cb\_t) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga4687047910cad0dd970bbd28adcf22ed)tcpc\_alert

| enum [tcpc\_alert](#ga4687047910cad0dd970bbd28adcf22ed) |
| --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

TCPC Alert bits.

| Enumerator | |
| --- | --- |
| TCPC\_ALERT\_CC\_STATUS | CC status changed. |
| TCPC\_ALERT\_POWER\_STATUS | Power status changed. |
| TCPC\_ALERT\_MSG\_STATUS | Receive Buffer register changed. |
| TCPC\_ALERT\_HARD\_RESET\_RECEIVED | Received Hard Reset message. |
| TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED | SOP\* message transmission not successful. |
| TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED | Reset or SOP\* message transmission not sent due to an incoming receive message. |
| TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS | Reset or SOP\* message transmission successful. |
| TCPC\_ALERT\_VBUS\_ALARM\_HI | A high-voltage alarm has occurred. |
| TCPC\_ALERT\_VBUS\_ALARM\_LO | A low-voltage alarm has occurred. |
| TCPC\_ALERT\_FAULT\_STATUS | A fault has occurred.  Read the FAULT\_STATUS register |
| TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW | TCPC RX buffer has overflowed. |
| TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT | The TCPC in Attached.SNK state has detected a sink disconnect. |
| TCPC\_ALERT\_BEGINNING\_MSG\_STATUS | Receive buffer register changed. |
| TCPC\_ALERT\_EXTENDED\_STATUS | Extended status changed. |
| TCPC\_ALERT\_EXTENDED | An extended interrupt event has occurred.  Read the alert\_extended register |
| TCPC\_ALERT\_VENDOR\_DEFINED | A vendor defined alert has been detected. |

## [◆ ](#gafd8253dfa6abc80d0717b17271ed8916)tcpc\_status\_reg

| enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) |
| --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

TCPC Status register.

| Enumerator | |
| --- | --- |
| TCPC\_ALERT\_STATUS | The Altert register. |
| TCPC\_CC\_STATUS | The CC Status register. |
| TCPC\_POWER\_STATUS | The Power Status register. |
| TCPC\_FAULT\_STATUS | The Fault Status register. |
| TCPC\_EXTENDED\_STATUS | The Extended Status register. |
| TCPC\_EXTENDED\_ALERT\_STATUS | The Extended Alert Status register. |
| TCPC\_VENDOR\_DEFINED\_STATUS | The Vendor Defined Status register. |

## Function Documentation

## [◆ ](#ga00170b754d78d8eb7da24abd7d533e42)tcpc\_clear\_status\_register()

| | int tcpc\_clear\_status\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Clears a TCPC status register.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | reg | The status register to read |
    | mask | A bit mask of the status register to clear. A status bit is cleared when it's set to 1. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga91eef7084b523f1991e000f0592b8cbd)tcpc\_dump\_std\_reg()

| | int tcpc\_dump\_std\_reg | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Dump a set of TCPC registers.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga66ab7a9f3cd1b80cd5bc8e99040c5627)tcpc\_get\_cc()

| | int tcpc\_get\_cc | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc1*, | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Reads the status of the CC lines.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | cc1 | A pointer where the CC1 status is written |
    | cc2 | A pointer where the CC2 status is written |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga894d24140f8675b4f48d759c27f52076)tcpc\_get\_chip\_info()

| | int tcpc\_get\_chip\_info | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [tcpc\_chip\_info](structtcpc__chip__info.md) \* | *chip\_info* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Gets the TCPC firmware version.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | chip\_info | Pointer to TCPC chip info where the version is stored |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga25a110be90977e768623f3a0c9a222d5)tcpc\_get\_rp\_value()

| | int tcpc\_get\_rp\_value | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \* | *rp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Gets the value of the CC pull up resistor used when operating as a Source.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | rp | pointer where the value of the Pull-Up Resistor is stored |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOSYS |  |
    | -EIO | on failure |

## [◆ ](#ga34e4caefb0f660b170f97956ac57b707)tcpc\_get\_rx\_pending\_msg()

| | int tcpc\_get\_rx\_pending\_msg | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [pd\_msg](structpd__msg.md) \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Retrieves the Power Delivery message from the TCPC.

If buf is NULL, then only the status is returned, where 0 means there is a message pending and -ENODATA means there is no pending message.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | buf | pointer where the pd\_buf pointer is written, NULL if only checking the status |

Return values
:   | Greater | or equal to 0 is the number of bytes received if buf parameter is provided |
    | --- | --- |
    | 0 | if there is a message pending and buf parameter is NULL |
    | -EIO | on failure |
    | -ENODATA | if no message is pending |

## [◆ ](#ga0c1cd7bc86c89abf5e348987d34e4623)tcpc\_get\_snk\_ctrl()

| | int tcpc\_get\_snk\_ctrl | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Queries the current sinking state of the TCPC.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if sinking power |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if not sinking power |
    | -ENOSYS | if not implemented |

## [◆ ](#ga03c8c6fc6f4c6adefacbc809588e1f85)tcpc\_get\_src\_ctrl()

| | int tcpc\_get\_src\_ctrl | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Queries the current sourcing state of the TCPC.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if sourcing power |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if not sourcing power |
    | -ENOSYS | if not implemented |

## [◆ ](#gace43dc303d3874a386cc79aa4304b846)tcpc\_get\_status\_register()

| | int tcpc\_get\_status\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *status* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Gets a status register.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | reg | The status register to read |
    | status | Pointer where the status is stored |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#gabc50daa9cc713b1d0e340007e3850ca8)tcpc\_init()

| | int tcpc\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Initializes the TCPC.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -EAGAIN | if initialization should be postponed |

## [◆ ](#gab4e9cc812679cf8cb0189f73a28d7cd2)tcpc\_is\_cc\_at\_least\_one\_rd()

| | int tcpc\_is\_cc\_at\_least\_one\_rd | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if the port partner is presenting at least one Rd.

## [◆ ](#ga153054be89d5f21148fe3ee750c718ee)tcpc\_is\_cc\_audio\_acc()

| | int tcpc\_is\_cc\_audio\_acc | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if the port partner is an audio accessory.

## [◆ ](#ga91c3c40ea82ce5a081918183d8b76c06)tcpc\_is\_cc\_only\_one\_rd()

| | int tcpc\_is\_cc\_only\_one\_rd | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if the port partner is presenting Rd on only one CC line.

## [◆ ](#ga0db896e395812603a03548b8faac6791)tcpc\_is\_cc\_open()

| | int tcpc\_is\_cc\_open | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if both CC lines are completely open.

## [◆ ](#ga6dfd68915ffe093058f6187b770a2436)tcpc\_is\_cc\_rp()

| | int tcpc\_is\_cc\_rp | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns whether the sink has detected a Rp resistor on the other side.

## [◆ ](#gaa0d2059c3a53df986150141f73b9a98a)tcpc\_is\_cc\_snk\_dbg\_acc()

| | int tcpc\_is\_cc\_snk\_dbg\_acc | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if we detect the port partner is a snk debug accessory.

## [◆ ](#ga03849a7a4fd7f468b18838c443d1ecd8)tcpc\_is\_cc\_src\_dbg\_acc()

| | int tcpc\_is\_cc\_src\_dbg\_acc | ( | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc1*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) | *cc2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Returns true if we detect the port partner is a src debug accessory.

## [◆ ](#ga0d1868d555e99877e062fb7135d9db8f)tcpc\_mask\_status\_register()

| | int tcpc\_mask\_status\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tcpc\_status\_reg](#gafd8253dfa6abc80d0717b17271ed8916) | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the mask of a TCPC status register.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | reg | The status register to read |
    | mask | A bit mask of the status register to mask. The status bit is masked if it's 0, else it's unmasked. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga3958eac0cc0b9b2ac782e0cdb235036c)tcpc\_select\_rp\_value()

| | int tcpc\_select\_rp\_value | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) | *rp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the value of CC pull up resistor used when operating as a Source.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | rp | Value of the Pull-Up Resistor. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOSYS |  |
    | -EIO | on failure |

## [◆ ](#ga75f0dc246dac576f14c5ac51b45fd489)tcpc\_set\_alert\_handler\_cb()

| | int tcpc\_set\_alert\_handler\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [tcpc\_alert\_handler\_cb\_t](#ga5f42fa12f90d34961eeeb67c0dc4f925) | *handler*, | |  |  | void \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the alert function that's called when an interrupt is triggered due to an alert bit.

Calling this function enables the particular alert bit

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | handler | The callback function called when the bit is set |
    | data | user data passed to the callback |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | on failure |

## [◆ ](#gaccc728a1f27c59a163a5c0a221ab7c18)tcpc\_set\_bist\_test\_mode()

| | int tcpc\_set\_bist\_test\_mode | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Controls the BIST Mode of the TCPC.

It disables RX alerts while the mode is active.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | The TCPC enters BIST TEST Mode when true |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#gac5737d02caa2b9e649b469bcd648440f)tcpc\_set\_cc()

| | int tcpc\_set\_cc | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) | *pull* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the CC pull resistor and sets the role as either Source or Sink.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | pull | The pull resistor to set |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |

## [◆ ](#ga53f0207ecb63011c6dfc3c298a841ed4)tcpc\_set\_cc\_polarity()

| | int tcpc\_set\_cc\_polarity | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) | *polarity* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the polarity of the CC lines.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | polarity | Polarity of the cc line |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |

## [◆ ](#ga01687aa218b25ba137e994a2a55bce23)tcpc\_set\_debug\_accessory()

| | int tcpc\_set\_debug\_accessory | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Manual control of TCPC DebugAccessory control.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | Enable Debug Accessory when true, else it's disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#gaaa38e56e6bc8c41e936d8ed70aaa8a23)tcpc\_set\_debug\_detach()

| | int tcpc\_set\_debug\_detach | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Detach from a debug connection.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#gaa06e156bef46ff3f70cc8c302ddf0a4d)tcpc\_set\_drp\_toggle()

| | int tcpc\_set\_drp\_toggle | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Enable TCPC auto dual role toggle.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | Auto dual role toggle is active when true, else it's disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga961a4dc393d58dc44ea19a62c943ed48)tcpc\_set\_low\_power\_mode()

| | int tcpc\_set\_low\_power\_mode | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Instructs the TCPC to enter or exit low power mode.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | The TCPC enters low power mode when true, else it exits it |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga8d30c961335f62faa33aa7d842422da0)tcpc\_set\_roles()

| | int tcpc\_set\_roles | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) | *power\_role*, | |  |  | enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) | *data\_role* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets the Power and Data Role of the PD message header.

This function only needs to be called once per data / power role change

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | power\_role | current power role |
    | data\_role | current data role |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga905176a77ff127f4df8f6a4f2c61a1b7)tcpc\_set\_rx\_enable()

| | int tcpc\_set\_rx\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Enables the reception of SOP\* message types.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | Enable Power Delivery when true, else it's disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga7a63d55cbe5de1d89aa76e10df0140ed)tcpc\_set\_snk\_ctrl()

| | int tcpc\_set\_snk\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Set the VBUS sinking state of the TCPC.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | True if sinking should be enabled, false if disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOSYS | if not implemented |

## [◆ ](#ga8f06b257d1bd0a17eb3042d204b2e6cd)tcpc\_set\_src\_ctrl()

| | int tcpc\_set\_src\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Set the VBUS sourcing state of the TCPC.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | True if sourcing should be enabled, false if disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOSYS | if not implemented |

## [◆ ](#ga247f0ea91249753d6f5eefe006617e41)tcpc\_set\_vconn()

| | int tcpc\_set\_vconn | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Enables or disables VCONN.

This function uses the TCPC to measure VCONN if possible or calls the callback function set by tcpc\_set\_vconn\_cb

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | VCONN is enabled when true, it's disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#gaa608f2c6627c4a9c3039f0ec1b238bbc)tcpc\_set\_vconn\_cb()

| | void tcpc\_set\_vconn\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [tcpc\_vconn\_control\_cb\_t](#ga7a989ffd6bdc83696188de59acbd49c7) | *vconn\_cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets a callback that can enable or disable VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC.

The callback is called in the tcpc\_set\_vconn function if vconn\_cb isn't NULL

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | vconn\_cb | pointer to the callback function that controls vconn |

## [◆ ](#ga975e7edea79de197c7230bd7b7a7efba)tcpc\_set\_vconn\_discharge\_cb()

| | void tcpc\_set\_vconn\_discharge\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [tcpc\_vconn\_discharge\_cb\_t](#ga4437e66605f988be1e16c52b9912e9c2) | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Sets a callback that can enable or discharge VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC.

The callback is called in the tcpc\_vconn\_discharge function if cb isn't NULL

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | cb | pointer to the callback function that discharges vconn |

## [◆ ](#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)tcpc\_sop\_prime\_enable()

| | int tcpc\_sop\_prime\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Enables the reception of SOP Prime and optionally SOP Double Prime messages.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | Can receive SOP Prime messages and SOP Double Prime messages when true, else it can not |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga8bf8fd202d582a4cc179a0fc4aff35e1)tcpc\_transmit\_data()

| | int tcpc\_transmit\_data | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [pd\_msg](structpd__msg.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Transmits a Power Delivery message.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | msg | Power Delivery message to transmit |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

## [◆ ](#ga3937d66636a2b22422caf11c48f7628a)tcpc\_vconn\_discharge()

| | int tcpc\_vconn\_discharge | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_tcpc.h](usbc__tcpc_8h.md)>`

Discharges VCONN.

This function uses the TCPC to discharge VCONN if possible or calls the callback function set by tcpc\_set\_vconn\_cb

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | VCONN discharge is enabled when true, it's disabled |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOSYS | if not implemented |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
