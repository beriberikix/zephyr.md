---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structtcpc__driver__api.html
original_path: doxygen/html/structtcpc__driver__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpc\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Type-C Port Controller API](group__usb__type__c__port__controller__api.md)

`#include <[usbc_tcpc.h](usbc__tcpc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#a00ee20f4d78ec1e337b614afdfa3a686) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [get\_cc](#ae4b2588a327da51b961d7a00159e5aab) )(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
| int(\* | [select\_rp\_value](#a1eb311c296cfce9759d0f3137210fe6f) )(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp) |
| int(\* | [get\_rp\_value](#ad3fe740a7b85807242c03b6f32a7dea7) )(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
| int(\* | [set\_cc](#a4263d2b2b1e1e2002c09ef2ecb3c5a36) )(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull) |
| void(\* | [set\_vconn\_discharge\_cb](#a291abd7642114da14031811f55c8991a) )(const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb) |
| void(\* | [set\_vconn\_cb](#ad6b5fb88b0b39fd29584c2a2de685c20) )(const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb) |
| int(\* | [vconn\_discharge](#a06bf9faa692527225dc6a8224f37fe24) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_vconn](#a639486f042727c23781e90d725ac17fc) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_roles](#a43d110db7d4808939d24850f2c6a73be) )(const struct [device](structdevice.md) \*dev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role) |
| int(\* | [get\_rx\_pending\_msg](#a0d5fb6c9f3724b38d627fb51f70d6583) )(const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
| int(\* | [set\_rx\_enable](#a3440cc5751b0820b7fd7f4c288089e23) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_cc\_polarity](#a7bbd6583cfc43ac235333aad93cc79e3) )(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity) |
| int(\* | [transmit\_data](#abffc63aa90730025fae61891cb228cd4) )(const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
| int(\* | [dump\_std\_reg](#a11ecbb4c78aecb278e1a3568d032c05a) )(const struct [device](structdevice.md) \*dev) |
| void(\* | [alert\_handler\_cb](#a271fc8d67338a4e7384d4f938026a5f3) )(const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) alert) |
| int(\* | [get\_status\_register](#aa3d97fe5bc52b144a22551e38867fd2e) )(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*status) |
| int(\* | [clear\_status\_register](#a45a1d895153d5e7182313a15e6908df0) )(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
| int(\* | [mask\_status\_register](#ac8750dd530c23a02e548b8b01c8abda3) )(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
| int(\* | [set\_debug\_accessory](#a0bd24553cc59c3947f6ec634a2a611e0) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_debug\_detach](#ad3d06d75563e7a8f00a9a61fe279a6bc) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_drp\_toggle](#aed51c3046411854b7be470d761e77faa) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [get\_snk\_ctrl](#a4a798a34ade8740ae3fff0a943c42ddd) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [get\_src\_ctrl](#a4ba0050fb389cd281deedbe327eca49e) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [get\_chip\_info](#a9ddaaae8e34bf36e868908d7555514dd) )(const struct [device](structdevice.md) \*dev, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info) |
| int(\* | [set\_low\_power\_mode](#ac70604b14dd7fe966489c159e1b3433d) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [sop\_prime\_enable](#a4402729135c40bbf30a18c148134b34c) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_bist\_test\_mode](#afba03924bd5b3f62733309b9a0084552) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_alert\_handler\_cb](#adc0c8e5f174549fb7683028c58e890bd) )(const struct [device](structdevice.md) \*dev, [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925) handler, void \*data) |

## Field Documentation

## [◆ ](#a271fc8d67338a4e7384d4f938026a5f3)alert\_handler\_cb

| void(\* tcpc\_driver\_api::alert\_handler\_cb) (const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) alert) |
| --- |

## [◆ ](#a45a1d895153d5e7182313a15e6908df0)clear\_status\_register

| int(\* tcpc\_driver\_api::clear\_status\_register) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
| --- |

## [◆ ](#a11ecbb4c78aecb278e1a3568d032c05a)dump\_std\_reg

| int(\* tcpc\_driver\_api::dump\_std\_reg) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ae4b2588a327da51b961d7a00159e5aab)get\_cc

| int(\* tcpc\_driver\_api::get\_cc) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
| --- |

## [◆ ](#a9ddaaae8e34bf36e868908d7555514dd)get\_chip\_info

| int(\* tcpc\_driver\_api::get\_chip\_info) (const struct [device](structdevice.md) \*dev, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info) |
| --- |

## [◆ ](#ad3fe740a7b85807242c03b6f32a7dea7)get\_rp\_value

| int(\* tcpc\_driver\_api::get\_rp\_value) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
| --- |

## [◆ ](#a0d5fb6c9f3724b38d627fb51f70d6583)get\_rx\_pending\_msg

| int(\* tcpc\_driver\_api::get\_rx\_pending\_msg) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
| --- |

## [◆ ](#a4a798a34ade8740ae3fff0a943c42ddd)get\_snk\_ctrl

| int(\* tcpc\_driver\_api::get\_snk\_ctrl) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a4ba0050fb389cd281deedbe327eca49e)get\_src\_ctrl

| int(\* tcpc\_driver\_api::get\_src\_ctrl) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#aa3d97fe5bc52b144a22551e38867fd2e)get\_status\_register

| int(\* tcpc\_driver\_api::get\_status\_register) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*status) |
| --- |

## [◆ ](#a00ee20f4d78ec1e337b614afdfa3a686)init

| int(\* tcpc\_driver\_api::init) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ac8750dd530c23a02e548b8b01c8abda3)mask\_status\_register

| int(\* tcpc\_driver\_api::mask\_status\_register) (const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask) |
| --- |

## [◆ ](#a1eb311c296cfce9759d0f3137210fe6f)select\_rp\_value

| int(\* tcpc\_driver\_api::select\_rp\_value) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp) |
| --- |

## [◆ ](#adc0c8e5f174549fb7683028c58e890bd)set\_alert\_handler\_cb

| int(\* tcpc\_driver\_api::set\_alert\_handler\_cb) (const struct [device](structdevice.md) \*dev, [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925) handler, void \*data) |
| --- |

## [◆ ](#afba03924bd5b3f62733309b9a0084552)set\_bist\_test\_mode

| int(\* tcpc\_driver\_api::set\_bist\_test\_mode) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a4263d2b2b1e1e2002c09ef2ecb3c5a36)set\_cc

| int(\* tcpc\_driver\_api::set\_cc) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull) |
| --- |

## [◆ ](#a7bbd6583cfc43ac235333aad93cc79e3)set\_cc\_polarity

| int(\* tcpc\_driver\_api::set\_cc\_polarity) (const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity) |
| --- |

## [◆ ](#a0bd24553cc59c3947f6ec634a2a611e0)set\_debug\_accessory

| int(\* tcpc\_driver\_api::set\_debug\_accessory) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#ad3d06d75563e7a8f00a9a61fe279a6bc)set\_debug\_detach

| int(\* tcpc\_driver\_api::set\_debug\_detach) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#aed51c3046411854b7be470d761e77faa)set\_drp\_toggle

| int(\* tcpc\_driver\_api::set\_drp\_toggle) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#ac70604b14dd7fe966489c159e1b3433d)set\_low\_power\_mode

| int(\* tcpc\_driver\_api::set\_low\_power\_mode) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a43d110db7d4808939d24850f2c6a73be)set\_roles

| int(\* tcpc\_driver\_api::set\_roles) (const struct [device](structdevice.md) \*dev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role, enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role) |
| --- |

## [◆ ](#a3440cc5751b0820b7fd7f4c288089e23)set\_rx\_enable

| int(\* tcpc\_driver\_api::set\_rx\_enable) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a639486f042727c23781e90d725ac17fc)set\_vconn

| int(\* tcpc\_driver\_api::set\_vconn) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#ad6b5fb88b0b39fd29584c2a2de685c20)set\_vconn\_cb

| void(\* tcpc\_driver\_api::set\_vconn\_cb) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb) |
| --- |

## [◆ ](#a291abd7642114da14031811f55c8991a)set\_vconn\_discharge\_cb

| void(\* tcpc\_driver\_api::set\_vconn\_discharge\_cb) (const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb) |
| --- |

## [◆ ](#a4402729135c40bbf30a18c148134b34c)sop\_prime\_enable

| int(\* tcpc\_driver\_api::sop\_prime\_enable) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#abffc63aa90730025fae61891cb228cd4)transmit\_data

| int(\* tcpc\_driver\_api::transmit\_data) (const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg) |
| --- |

## [◆ ](#a06bf9faa692527225dc6a8224f37fe24)vconn\_discharge

| int(\* tcpc\_driver\_api::vconn\_discharge) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_tcpc.h](usbc__tcpc_8h_source.md)

- [tcpc\_driver\_api](structtcpc__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
