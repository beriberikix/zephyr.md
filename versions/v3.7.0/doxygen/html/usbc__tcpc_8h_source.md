---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usbc__tcpc_8h_source.html
original_path: doxygen/html/usbc__tcpc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_tcpc.h

[Go to the documentation of this file.](usbc__tcpc_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TCPC\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TCPC\_H\_

17

26

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29#include <[errno.h](errno_8h.md)>

30

31#include "[usbc\_tc.h](usbc__tc_8h.md)"

32#include "[usbc\_pd.h](usbc__pd_8h.md)"

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 41](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed)enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) {

[ 43](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f) [TCPC\_ALERT\_CC\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f),

[ 45](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4) [TCPC\_ALERT\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4),

[ 47](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb) [TCPC\_ALERT\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb),

[ 49](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0) [TCPC\_ALERT\_HARD\_RESET\_RECEIVED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0),

[ 51](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec) [TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec),

[ 56](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe) [TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe),

[ 58](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2) [TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2),

[ 60](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66) [TCPC\_ALERT\_VBUS\_ALARM\_HI](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66),

[ 62](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0) [TCPC\_ALERT\_VBUS\_ALARM\_LO](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0),

[ 64](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e) [TCPC\_ALERT\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e),

[ 66](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752) [TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752),

[ 68](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd) [TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd),

[ 70](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb) [TCPC\_ALERT\_BEGINNING\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb),

[ 72](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9) [TCPC\_ALERT\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9),

[ 77](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25) [TCPC\_ALERT\_EXTENDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25),

[ 79](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992) [TCPC\_ALERT\_VENDOR\_DEFINED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)

80};

81

[ 85](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916)enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) {

[ 87](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4) [TCPC\_CC\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4),

[ 89](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f) [TCPC\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f),

[ 91](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440) [TCPC\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440),

[ 93](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d) [TCPC\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d),

[ 95](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db) [TCPC\_EXTENDED\_ALERT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db),

[ 97](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61) [TCPC\_VENDOR\_DEFINED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)

98};

99

[ 103](structtcpc__chip__info.md)struct [tcpc\_chip\_info](structtcpc__chip__info.md) {

[ 105](structtcpc__chip__info.md#ab48400ea4209d5443e5b7e0bfee6c4fc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vendor\_id](structtcpc__chip__info.md#ab48400ea4209d5443e5b7e0bfee6c4fc);

[ 107](structtcpc__chip__info.md#a14c11999ef548e41f4338f3e7208b7a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [product\_id](structtcpc__chip__info.md#a14c11999ef548e41f4338f3e7208b7a9);

[ 109](structtcpc__chip__info.md#a9e76ee3bcc395dbb77d7a065f6181cd6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [device\_id](structtcpc__chip__info.md#a9e76ee3bcc395dbb77d7a065f6181cd6);

[ 111](structtcpc__chip__info.md#a7789339580e2774d18a8f4c78332f774) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [fw\_version\_number](structtcpc__chip__info.md#a7789339580e2774d18a8f4c78332f774);

112

113 union {

[ 115](structtcpc__chip__info.md#a677a85ef27f0d5db969ce3232506d1bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_req\_fw\_version\_string](structtcpc__chip__info.md#a677a85ef27f0d5db969ce3232506d1bb)[8];

[ 117](structtcpc__chip__info.md#a8d66f33379493e1a0ed707b3715f863a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [min\_req\_fw\_version\_number](structtcpc__chip__info.md#a8d66f33379493e1a0ed707b3715f863a);

118 };

119};

120

[ 121](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7)typedef int (\*[tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7))(const struct [device](structdevice.md) \*dev,

122 enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, bool enable);

[ 123](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2)typedef int (\*[tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2))(const struct [device](structdevice.md) \*dev,

124 enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) pol, bool enable);

[ 125](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925)typedef void (\*[tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925))(const struct [device](structdevice.md) \*dev, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

126 enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) alert);

127

[ 128](structtcpc__driver__api.md)\_\_subsystem struct [tcpc\_driver\_api](structtcpc__driver__api.md) {

[ 129](structtcpc__driver__api.md#a00ee20f4d78ec1e337b614afdfa3a686) int (\*[init](structtcpc__driver__api.md#a00ee20f4d78ec1e337b614afdfa3a686))(const struct [device](structdevice.md) \*dev);

[ 130](structtcpc__driver__api.md#ae4b2588a327da51b961d7a00159e5aab) int (\*[get\_cc](structtcpc__driver__api.md#ae4b2588a327da51b961d7a00159e5aab))(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1,

131 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2);

[ 132](structtcpc__driver__api.md#a1eb311c296cfce9759d0f3137210fe6f) int (\*[select\_rp\_value](structtcpc__driver__api.md#a1eb311c296cfce9759d0f3137210fe6f))(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp);

[ 133](structtcpc__driver__api.md#ad3fe740a7b85807242c03b6f32a7dea7) int (\*[get\_rp\_value](structtcpc__driver__api.md#ad3fe740a7b85807242c03b6f32a7dea7))(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp);

[ 134](structtcpc__driver__api.md#a4263d2b2b1e1e2002c09ef2ecb3c5a36) int (\*[set\_cc](structtcpc__driver__api.md#a4263d2b2b1e1e2002c09ef2ecb3c5a36))(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull);

[ 135](structtcpc__driver__api.md#a291abd7642114da14031811f55c8991a) void (\*[set\_vconn\_discharge\_cb](structtcpc__driver__api.md#a291abd7642114da14031811f55c8991a))(const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb);

[ 136](structtcpc__driver__api.md#ad6b5fb88b0b39fd29584c2a2de685c20) void (\*[set\_vconn\_cb](structtcpc__driver__api.md#ad6b5fb88b0b39fd29584c2a2de685c20))(const struct [device](structdevice.md) \*dev, [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb);

[ 137](structtcpc__driver__api.md#a06bf9faa692527225dc6a8224f37fe24) int (\*[vconn\_discharge](structtcpc__driver__api.md#a06bf9faa692527225dc6a8224f37fe24))(const struct [device](structdevice.md) \*dev, bool enable);

[ 138](structtcpc__driver__api.md#a639486f042727c23781e90d725ac17fc) int (\*[set\_vconn](structtcpc__driver__api.md#a639486f042727c23781e90d725ac17fc))(const struct [device](structdevice.md) \*dev, bool enable);

[ 139](structtcpc__driver__api.md#a43d110db7d4808939d24850f2c6a73be) int (\*[set\_roles](structtcpc__driver__api.md#a43d110db7d4808939d24850f2c6a73be))(const struct [device](structdevice.md) \*dev, enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role,

140 enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role);

[ 141](structtcpc__driver__api.md#a0d5fb6c9f3724b38d627fb51f70d6583) int (\*[get\_rx\_pending\_msg](structtcpc__driver__api.md#a0d5fb6c9f3724b38d627fb51f70d6583))(const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg);

[ 142](structtcpc__driver__api.md#a3440cc5751b0820b7fd7f4c288089e23) int (\*[set\_rx\_enable](structtcpc__driver__api.md#a3440cc5751b0820b7fd7f4c288089e23))(const struct [device](structdevice.md) \*dev, bool enable);

[ 143](structtcpc__driver__api.md#a7bbd6583cfc43ac235333aad93cc79e3) int (\*[set\_cc\_polarity](structtcpc__driver__api.md#a7bbd6583cfc43ac235333aad93cc79e3))(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity);

[ 144](structtcpc__driver__api.md#abffc63aa90730025fae61891cb228cd4) int (\*[transmit\_data](structtcpc__driver__api.md#abffc63aa90730025fae61891cb228cd4))(const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*msg);

[ 145](structtcpc__driver__api.md#a11ecbb4c78aecb278e1a3568d032c05a) int (\*[dump\_std\_reg](structtcpc__driver__api.md#a11ecbb4c78aecb278e1a3568d032c05a))(const struct [device](structdevice.md) \*dev);

[ 146](structtcpc__driver__api.md#a271fc8d67338a4e7384d4f938026a5f3) void (\*[alert\_handler\_cb](structtcpc__driver__api.md#a271fc8d67338a4e7384d4f938026a5f3))(const struct [device](structdevice.md) \*dev, void \*data, enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) alert);

[ 147](structtcpc__driver__api.md#aa3d97fe5bc52b144a22551e38867fd2e) int (\*[get\_status\_register](structtcpc__driver__api.md#aa3d97fe5bc52b144a22551e38867fd2e))(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

148 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*status);

[ 149](structtcpc__driver__api.md#a45a1d895153d5e7182313a15e6908df0) int (\*[clear\_status\_register](structtcpc__driver__api.md#a45a1d895153d5e7182313a15e6908df0))(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

150 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask);

[ 151](structtcpc__driver__api.md#ac8750dd530c23a02e548b8b01c8abda3) int (\*[mask\_status\_register](structtcpc__driver__api.md#ac8750dd530c23a02e548b8b01c8abda3))(const struct [device](structdevice.md) \*dev, enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

152 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask);

[ 153](structtcpc__driver__api.md#a0bd24553cc59c3947f6ec634a2a611e0) int (\*[set\_debug\_accessory](structtcpc__driver__api.md#a0bd24553cc59c3947f6ec634a2a611e0))(const struct [device](structdevice.md) \*dev, bool enable);

[ 154](structtcpc__driver__api.md#ad3d06d75563e7a8f00a9a61fe279a6bc) int (\*[set\_debug\_detach](structtcpc__driver__api.md#ad3d06d75563e7a8f00a9a61fe279a6bc))(const struct [device](structdevice.md) \*dev);

[ 155](structtcpc__driver__api.md#aed51c3046411854b7be470d761e77faa) int (\*[set\_drp\_toggle](structtcpc__driver__api.md#aed51c3046411854b7be470d761e77faa))(const struct [device](structdevice.md) \*dev, bool enable);

[ 156](structtcpc__driver__api.md#a4a798a34ade8740ae3fff0a943c42ddd) int (\*[get\_snk\_ctrl](structtcpc__driver__api.md#a4a798a34ade8740ae3fff0a943c42ddd))(const struct [device](structdevice.md) \*dev);

[ 157](structtcpc__driver__api.md#a2aa06dc38fcf6d0d044d2094481c43c5) int (\*[set\_snk\_ctrl](structtcpc__driver__api.md#a2aa06dc38fcf6d0d044d2094481c43c5))(const struct [device](structdevice.md) \*dev, bool enable);

[ 158](structtcpc__driver__api.md#a4ba0050fb389cd281deedbe327eca49e) int (\*[get\_src\_ctrl](structtcpc__driver__api.md#a4ba0050fb389cd281deedbe327eca49e))(const struct [device](structdevice.md) \*dev);

[ 159](structtcpc__driver__api.md#a797e6472126c3a02b8651cbc40395526) int (\*[set\_src\_ctrl](structtcpc__driver__api.md#a797e6472126c3a02b8651cbc40395526))(const struct [device](structdevice.md) \*dev, bool enable);

[ 160](structtcpc__driver__api.md#a9ddaaae8e34bf36e868908d7555514dd) int (\*[get\_chip\_info](structtcpc__driver__api.md#a9ddaaae8e34bf36e868908d7555514dd))(const struct [device](structdevice.md) \*dev, struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info);

[ 161](structtcpc__driver__api.md#ac70604b14dd7fe966489c159e1b3433d) int (\*[set\_low\_power\_mode](structtcpc__driver__api.md#ac70604b14dd7fe966489c159e1b3433d))(const struct [device](structdevice.md) \*dev, bool enable);

[ 162](structtcpc__driver__api.md#a4402729135c40bbf30a18c148134b34c) int (\*[sop\_prime\_enable](structtcpc__driver__api.md#a4402729135c40bbf30a18c148134b34c))(const struct [device](structdevice.md) \*dev, bool enable);

[ 163](structtcpc__driver__api.md#afba03924bd5b3f62733309b9a0084552) int (\*[set\_bist\_test\_mode](structtcpc__driver__api.md#afba03924bd5b3f62733309b9a0084552))(const struct [device](structdevice.md) \*dev, bool enable);

[ 164](structtcpc__driver__api.md#adc0c8e5f174549fb7683028c58e890bd) int (\*[set\_alert\_handler\_cb](structtcpc__driver__api.md#adc0c8e5f174549fb7683028c58e890bd))(const struct [device](structdevice.md) \*dev, [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925) handler,

165 void \*data);

166};

167

[ 171](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436)static inline int [tcpc\_is\_cc\_rp](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) [cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6))

172{

173 return ([cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6) == [TC\_CC\_VOLT\_RP\_DEF](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)) || ([cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6) == [TC\_CC\_VOLT\_RP\_1A5](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)) ||

174 ([cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6) == [TC\_CC\_VOLT\_RP\_3A0](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca));

175}

176

[ 180](group__usb__type__c__port__controller__api.md#ga0db896e395812603a03548b8faac6791)static inline int [tcpc\_is\_cc\_open](group__usb__type__c__port__controller__api.md#ga0db896e395812603a03548b8faac6791)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

181 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

182{

183 return (cc1 < [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)) && (cc2 < [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9));

184}

185

[ 189](group__usb__type__c__port__controller__api.md#gaa0d2059c3a53df986150141f73b9a98a)static inline int [tcpc\_is\_cc\_snk\_dbg\_acc](group__usb__type__c__port__controller__api.md#gaa0d2059c3a53df986150141f73b9a98a)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

190 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

191{

192 return cc1 == [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) && cc2 == [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9);

193}

194

[ 198](group__usb__type__c__port__controller__api.md#ga03849a7a4fd7f468b18838c443d1ecd8)static inline int [tcpc\_is\_cc\_src\_dbg\_acc](group__usb__type__c__port__controller__api.md#ga03849a7a4fd7f468b18838c443d1ecd8)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

199 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

200{

201 return [tcpc\_is\_cc\_rp](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436)(cc1) && [tcpc\_is\_cc\_rp](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436)(cc2);

202}

203

[ 207](group__usb__type__c__port__controller__api.md#ga153054be89d5f21148fe3ee750c718ee)static inline int [tcpc\_is\_cc\_audio\_acc](group__usb__type__c__port__controller__api.md#ga153054be89d5f21148fe3ee750c718ee)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

208 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

209{

210 return cc1 == [TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea) && cc2 == [TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea);

211}

212

[ 216](group__usb__type__c__port__controller__api.md#gab4e9cc812679cf8cb0189f73a28d7cd2)static inline int [tcpc\_is\_cc\_at\_least\_one\_rd](group__usb__type__c__port__controller__api.md#gab4e9cc812679cf8cb0189f73a28d7cd2)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

217 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

218{

219 return cc1 == [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) || cc2 == [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9);

220}

221

[ 225](group__usb__type__c__port__controller__api.md#ga91c3c40ea82ce5a081918183d8b76c06)static inline int [tcpc\_is\_cc\_only\_one\_rd](group__usb__type__c__port__controller__api.md#ga91c3c40ea82ce5a081918183d8b76c06)(enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc1,

226 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) cc2)

227{

228 return [tcpc\_is\_cc\_at\_least\_one\_rd](group__usb__type__c__port__controller__api.md#gab4e9cc812679cf8cb0189f73a28d7cd2)(cc1, cc2) && cc1 != cc2;

229}

230

[ 240](group__usb__type__c__port__controller__api.md#gabc50daa9cc713b1d0e340007e3850ca8)static inline int [tcpc\_init](group__usb__type__c__port__controller__api.md#gabc50daa9cc713b1d0e340007e3850ca8)(const struct [device](structdevice.md) \*dev)

241{

242 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

243 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

244

245 \_\_ASSERT(api->[init](structtcpc__driver__api.md#a00ee20f4d78ec1e337b614afdfa3a686) != NULL,

246 "Callback pointer should not be NULL");

247

248 return api->[init](structtcpc__driver__api.md#a00ee20f4d78ec1e337b614afdfa3a686)(dev);

249}

250

[ 262](group__usb__type__c__port__controller__api.md#ga66ab7a9f3cd1b80cd5bc8e99040c5627)static inline int [tcpc\_get\_cc](group__usb__type__c__port__controller__api.md#ga66ab7a9f3cd1b80cd5bc8e99040c5627)(const struct [device](structdevice.md) \*dev,

263 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1,

264 enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2)

265{

266 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

267 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

268

269 if (api->[get\_cc](structtcpc__driver__api.md#ae4b2588a327da51b961d7a00159e5aab) == NULL) {

270 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

271 }

272

273 return api->[get\_cc](structtcpc__driver__api.md#ae4b2588a327da51b961d7a00159e5aab)(dev, cc1, cc2);

274}

275

[ 286](group__usb__type__c__port__controller__api.md#ga3958eac0cc0b9b2ac782e0cdb235036c)static inline int [tcpc\_select\_rp\_value](group__usb__type__c__port__controller__api.md#ga3958eac0cc0b9b2ac782e0cdb235036c)(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) rp)

287{

288 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

289 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

290

291 if (api->[select\_rp\_value](structtcpc__driver__api.md#a1eb311c296cfce9759d0f3137210fe6f) == NULL) {

292 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

293 }

294

295 return api->[select\_rp\_value](structtcpc__driver__api.md#a1eb311c296cfce9759d0f3137210fe6f)(dev, rp);

296}

297

[ 308](group__usb__type__c__port__controller__api.md#ga25a110be90977e768623f3a0c9a222d5)static inline int [tcpc\_get\_rp\_value](group__usb__type__c__port__controller__api.md#ga25a110be90977e768623f3a0c9a222d5)(const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp)

309{

310 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

311 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

312

313 if (api->[get\_rp\_value](structtcpc__driver__api.md#ad3fe740a7b85807242c03b6f32a7dea7) == NULL) {

314 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

315 }

316

317 return api->[get\_rp\_value](structtcpc__driver__api.md#ad3fe740a7b85807242c03b6f32a7dea7)(dev, rp);

318}

319

[ 329](group__usb__type__c__port__controller__api.md#gac5737d02caa2b9e649b469bcd648440f)static inline int [tcpc\_set\_cc](group__usb__type__c__port__controller__api.md#gac5737d02caa2b9e649b469bcd648440f)(const struct [device](structdevice.md) \*dev, enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) pull)

330{

331 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

332 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

333

334 \_\_ASSERT(api->[set\_cc](structtcpc__driver__api.md#a4263d2b2b1e1e2002c09ef2ecb3c5a36) != NULL,

335 "Callback pointer should not be NULL");

336

337 return api->[set\_cc](structtcpc__driver__api.md#a4263d2b2b1e1e2002c09ef2ecb3c5a36)(dev, pull);

338}

339

[ 350](group__usb__type__c__port__controller__api.md#gaa608f2c6627c4a9c3039f0ec1b238bbc)static inline void [tcpc\_set\_vconn\_cb](group__usb__type__c__port__controller__api.md#gaa608f2c6627c4a9c3039f0ec1b238bbc)(const struct [device](structdevice.md) \*dev,

351 [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) vconn\_cb)

352{

353 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

354 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

355

356 \_\_ASSERT(api->[set\_vconn\_cb](structtcpc__driver__api.md#ad6b5fb88b0b39fd29584c2a2de685c20) != NULL,

357 "Callback pointer should not be NULL");

358

359 return api->[set\_vconn\_cb](structtcpc__driver__api.md#ad6b5fb88b0b39fd29584c2a2de685c20)(dev, vconn\_cb);

360}

361

[ 372](group__usb__type__c__port__controller__api.md#ga975e7edea79de197c7230bd7b7a7efba)static inline void [tcpc\_set\_vconn\_discharge\_cb](group__usb__type__c__port__controller__api.md#ga975e7edea79de197c7230bd7b7a7efba)(const struct [device](structdevice.md) \*dev,

373 [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb)

374{

375 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

376 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

377

378 \_\_ASSERT(api->[set\_vconn\_discharge\_cb](structtcpc__driver__api.md#a291abd7642114da14031811f55c8991a) != NULL,

379 "Callback pointer should not be NULL");

380

381 return api->[set\_vconn\_discharge\_cb](structtcpc__driver__api.md#a291abd7642114da14031811f55c8991a)(dev, cb);

382}

383

[ 397](group__usb__type__c__port__controller__api.md#ga3937d66636a2b22422caf11c48f7628a)static inline int [tcpc\_vconn\_discharge](group__usb__type__c__port__controller__api.md#ga3937d66636a2b22422caf11c48f7628a)(const struct [device](structdevice.md) \*dev, bool enable)

398{

399 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

400 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

401

402 if (api->[vconn\_discharge](structtcpc__driver__api.md#a06bf9faa692527225dc6a8224f37fe24) == NULL) {

403 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

404 }

405

406 return api->[vconn\_discharge](structtcpc__driver__api.md#a06bf9faa692527225dc6a8224f37fe24)(dev, enable);

407}

408

[ 422](group__usb__type__c__port__controller__api.md#ga247f0ea91249753d6f5eefe006617e41)static inline int [tcpc\_set\_vconn](group__usb__type__c__port__controller__api.md#ga247f0ea91249753d6f5eefe006617e41)(const struct [device](structdevice.md) \*dev, bool enable)

423{

424 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

425 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

426

427 if (api->[set\_vconn](structtcpc__driver__api.md#a639486f042727c23781e90d725ac17fc) == NULL) {

428 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

429 }

430

431 return api->[set\_vconn](structtcpc__driver__api.md#a639486f042727c23781e90d725ac17fc)(dev, enable);

432}

433

[ 447](group__usb__type__c__port__controller__api.md#ga8d30c961335f62faa33aa7d842422da0)static inline int [tcpc\_set\_roles](group__usb__type__c__port__controller__api.md#ga8d30c961335f62faa33aa7d842422da0)(const struct [device](structdevice.md) \*dev,

448 enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) power\_role,

449 enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) data\_role)

450{

451 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

452 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

453

454 if (api->[set\_roles](structtcpc__driver__api.md#a43d110db7d4808939d24850f2c6a73be) == NULL) {

455 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

456 }

457

458 return api->[set\_roles](structtcpc__driver__api.md#a43d110db7d4808939d24850f2c6a73be)(dev, power\_role, data\_role);

459}

460

[ 474](group__usb__type__c__port__controller__api.md#ga34e4caefb0f660b170f97956ac57b707)static inline int [tcpc\_get\_rx\_pending\_msg](group__usb__type__c__port__controller__api.md#ga34e4caefb0f660b170f97956ac57b707)(const struct [device](structdevice.md) \*dev, struct [pd\_msg](structpd__msg.md) \*buf)

475{

476 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api = (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

477

478 \_\_ASSERT(api->[get\_rx\_pending\_msg](structtcpc__driver__api.md#a0d5fb6c9f3724b38d627fb51f70d6583) != NULL, "Callback pointer should not be NULL");

479

480 return api->[get\_rx\_pending\_msg](structtcpc__driver__api.md#a0d5fb6c9f3724b38d627fb51f70d6583)(dev, buf);

481}

482

[ 494](group__usb__type__c__port__controller__api.md#ga905176a77ff127f4df8f6a4f2c61a1b7)static inline int [tcpc\_set\_rx\_enable](group__usb__type__c__port__controller__api.md#ga905176a77ff127f4df8f6a4f2c61a1b7)(const struct [device](structdevice.md) \*dev, bool enable)

495{

496 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

497 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

498

499 if (api->[set\_rx\_enable](structtcpc__driver__api.md#a3440cc5751b0820b7fd7f4c288089e23) == NULL) {

500 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

501 }

502

503 return api->[set\_rx\_enable](structtcpc__driver__api.md#a3440cc5751b0820b7fd7f4c288089e23)(dev, enable);

504}

505

[ 515](group__usb__type__c__port__controller__api.md#ga53f0207ecb63011c6dfc3c298a841ed4)static inline int [tcpc\_set\_cc\_polarity](group__usb__type__c__port__controller__api.md#ga53f0207ecb63011c6dfc3c298a841ed4)(const struct [device](structdevice.md) \*dev,

516 enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) polarity)

517{

518 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

519 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

520

521 \_\_ASSERT(api->[set\_cc\_polarity](structtcpc__driver__api.md#a7bbd6583cfc43ac235333aad93cc79e3) != NULL,

522 "Callback pointer should not be NULL");

523

524 return api->[set\_cc\_polarity](structtcpc__driver__api.md#a7bbd6583cfc43ac235333aad93cc79e3)(dev, polarity);

525}

526

[ 537](group__usb__type__c__port__controller__api.md#ga8bf8fd202d582a4cc179a0fc4aff35e1)static inline int [tcpc\_transmit\_data](group__usb__type__c__port__controller__api.md#ga8bf8fd202d582a4cc179a0fc4aff35e1)(const struct [device](structdevice.md) \*dev,

538 struct [pd\_msg](structpd__msg.md) \*msg)

539{

540 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

541 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

542

543 if (api->[transmit\_data](structtcpc__driver__api.md#abffc63aa90730025fae61891cb228cd4) == NULL) {

544 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

545 }

546

547 return api->[transmit\_data](structtcpc__driver__api.md#abffc63aa90730025fae61891cb228cd4)(dev, msg);

548}

549

[ 559](group__usb__type__c__port__controller__api.md#ga91eef7084b523f1991e000f0592b8cbd)static inline int [tcpc\_dump\_std\_reg](group__usb__type__c__port__controller__api.md#ga91eef7084b523f1991e000f0592b8cbd)(const struct [device](structdevice.md) \*dev)

560{

561 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

562 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

563

564 if (api->[dump\_std\_reg](structtcpc__driver__api.md#a11ecbb4c78aecb278e1a3568d032c05a) == NULL) {

565 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

566 }

567

568 return api->[dump\_std\_reg](structtcpc__driver__api.md#a11ecbb4c78aecb278e1a3568d032c05a)(dev);

569}

570

[ 584](group__usb__type__c__port__controller__api.md#ga75f0dc246dac576f14c5ac51b45fd489)static inline int [tcpc\_set\_alert\_handler\_cb](group__usb__type__c__port__controller__api.md#ga75f0dc246dac576f14c5ac51b45fd489)(const struct [device](structdevice.md) \*dev,

585 [tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925) handler,

586 void \*data)

587{

588 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

589 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

590

591 \_\_ASSERT(api->[set\_alert\_handler\_cb](structtcpc__driver__api.md#adc0c8e5f174549fb7683028c58e890bd) != NULL,

592 "Callback pointer should not be NULL");

593

594 return api->[set\_alert\_handler\_cb](structtcpc__driver__api.md#adc0c8e5f174549fb7683028c58e890bd)(dev, handler, data);

595}

596

[ 608](group__usb__type__c__port__controller__api.md#ga41e81b8f83e06934a5eb984ae6f980ec)static inline int [tcpc\_get\_status\_register](group__usb__type__c__port__controller__api.md#ga41e81b8f83e06934a5eb984ae6f980ec)(const struct [device](structdevice.md) \*dev,

609 enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

610 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*status)

611{

612 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

613 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

614

615 if (api->[get\_status\_register](structtcpc__driver__api.md#aa3d97fe5bc52b144a22551e38867fd2e) == NULL) {

616 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

617 }

618

619 return api->[get\_status\_register](structtcpc__driver__api.md#aa3d97fe5bc52b144a22551e38867fd2e)(dev, reg, status);

620}

621

[ 634](group__usb__type__c__port__controller__api.md#ga00170b754d78d8eb7da24abd7d533e42)static inline int [tcpc\_clear\_status\_register](group__usb__type__c__port__controller__api.md#ga00170b754d78d8eb7da24abd7d533e42)(const struct [device](structdevice.md) \*dev,

635 enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

636 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask)

637{

638 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

639 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

640

641 if (api->[clear\_status\_register](structtcpc__driver__api.md#a45a1d895153d5e7182313a15e6908df0) == NULL) {

642 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

643 }

644

645 return api->[clear\_status\_register](structtcpc__driver__api.md#a45a1d895153d5e7182313a15e6908df0)(dev, reg, mask);

646}

647

[ 660](group__usb__type__c__port__controller__api.md#ga0d1868d555e99877e062fb7135d9db8f)static inline int [tcpc\_mask\_status\_register](group__usb__type__c__port__controller__api.md#ga0d1868d555e99877e062fb7135d9db8f)(const struct [device](structdevice.md) \*dev,

661 enum [tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916) reg,

662 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask)

663{

664 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

665 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

666

667 if (api->[mask\_status\_register](structtcpc__driver__api.md#ac8750dd530c23a02e548b8b01c8abda3) == NULL) {

668 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

669 }

670

671 return api->[mask\_status\_register](structtcpc__driver__api.md#ac8750dd530c23a02e548b8b01c8abda3)(dev, reg, mask);

672}

673

[ 684](group__usb__type__c__port__controller__api.md#ga01687aa218b25ba137e994a2a55bce23)static inline int [tcpc\_set\_debug\_accessory](group__usb__type__c__port__controller__api.md#ga01687aa218b25ba137e994a2a55bce23)(const struct [device](structdevice.md) \*dev,

685 bool enable)

686{

687 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

688 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

689

690 if (api->[set\_debug\_accessory](structtcpc__driver__api.md#a0bd24553cc59c3947f6ec634a2a611e0) == NULL) {

691 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

692 }

693

694 return api->[set\_debug\_accessory](structtcpc__driver__api.md#a0bd24553cc59c3947f6ec634a2a611e0)(dev, enable);

695}

696

[ 706](group__usb__type__c__port__controller__api.md#gaaa38e56e6bc8c41e936d8ed70aaa8a23)static inline int [tcpc\_set\_debug\_detach](group__usb__type__c__port__controller__api.md#gaaa38e56e6bc8c41e936d8ed70aaa8a23)(const struct [device](structdevice.md) \*dev)

707{

708 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

709 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

710

711 if (api->[set\_debug\_detach](structtcpc__driver__api.md#ad3d06d75563e7a8f00a9a61fe279a6bc) == NULL) {

712 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

713 }

714

715 return api->[set\_debug\_detach](structtcpc__driver__api.md#ad3d06d75563e7a8f00a9a61fe279a6bc)(dev);

716}

717

[ 728](group__usb__type__c__port__controller__api.md#gaa06e156bef46ff3f70cc8c302ddf0a4d)static inline int [tcpc\_set\_drp\_toggle](group__usb__type__c__port__controller__api.md#gaa06e156bef46ff3f70cc8c302ddf0a4d)(const struct [device](structdevice.md) \*dev, bool enable)

729{

730 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

731 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

732

733 if (api->[set\_drp\_toggle](structtcpc__driver__api.md#aed51c3046411854b7be470d761e77faa) == NULL) {

734 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

735 }

736

737 return api->[set\_drp\_toggle](structtcpc__driver__api.md#aed51c3046411854b7be470d761e77faa)(dev, enable);

738}

739

[ 749](group__usb__type__c__port__controller__api.md#ga0c1cd7bc86c89abf5e348987d34e4623)static inline int [tcpc\_get\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga0c1cd7bc86c89abf5e348987d34e4623)(const struct [device](structdevice.md) \*dev)

750{

751 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

752 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

753

754 if (api->[get\_snk\_ctrl](structtcpc__driver__api.md#a4a798a34ade8740ae3fff0a943c42ddd) == NULL) {

755 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

756 }

757

758 return api->[get\_snk\_ctrl](structtcpc__driver__api.md#a4a798a34ade8740ae3fff0a943c42ddd)(dev);

759}

760

[ 769](group__usb__type__c__port__controller__api.md#ga7a63d55cbe5de1d89aa76e10df0140ed)static inline int [tcpc\_set\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga7a63d55cbe5de1d89aa76e10df0140ed)(const struct [device](structdevice.md) \*dev, bool enable)

770{

771 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api = (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

772

773 if (api->[set\_snk\_ctrl](structtcpc__driver__api.md#a2aa06dc38fcf6d0d044d2094481c43c5) == NULL) {

774 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

775 }

776

777 return api->[set\_snk\_ctrl](structtcpc__driver__api.md#a2aa06dc38fcf6d0d044d2094481c43c5)(dev, enable);

778}

779

[ 789](group__usb__type__c__port__controller__api.md#ga03c8c6fc6f4c6adefacbc809588e1f85)static inline int [tcpc\_get\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga03c8c6fc6f4c6adefacbc809588e1f85)(const struct [device](structdevice.md) \*dev)

790{

791 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

792 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

793

794 if (api->[get\_src\_ctrl](structtcpc__driver__api.md#a4ba0050fb389cd281deedbe327eca49e) == NULL) {

795 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

796 }

797

798 return api->[get\_src\_ctrl](structtcpc__driver__api.md#a4ba0050fb389cd281deedbe327eca49e)(dev);

799}

800

[ 809](group__usb__type__c__port__controller__api.md#ga8f06b257d1bd0a17eb3042d204b2e6cd)static inline int [tcpc\_set\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga8f06b257d1bd0a17eb3042d204b2e6cd)(const struct [device](structdevice.md) \*dev, bool enable)

810{

811 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api = (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

812

813 if (api->[set\_src\_ctrl](structtcpc__driver__api.md#a797e6472126c3a02b8651cbc40395526) == NULL) {

814 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

815 }

816

817 return api->[set\_src\_ctrl](structtcpc__driver__api.md#a797e6472126c3a02b8651cbc40395526)(dev, enable);

818}

819

[ 831](group__usb__type__c__port__controller__api.md#gaccc728a1f27c59a163a5c0a221ab7c18)static inline int [tcpc\_set\_bist\_test\_mode](group__usb__type__c__port__controller__api.md#gaccc728a1f27c59a163a5c0a221ab7c18)(const struct [device](structdevice.md) \*dev,

832 bool enable)

833{

834 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

835 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

836

837 if (api->[set\_bist\_test\_mode](structtcpc__driver__api.md#afba03924bd5b3f62733309b9a0084552) == NULL) {

838 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

839 }

840

841 return api->[set\_bist\_test\_mode](structtcpc__driver__api.md#afba03924bd5b3f62733309b9a0084552)(dev, enable);

842}

843

[ 854](group__usb__type__c__port__controller__api.md#ga894d24140f8675b4f48d759c27f52076)static inline int [tcpc\_get\_chip\_info](group__usb__type__c__port__controller__api.md#ga894d24140f8675b4f48d759c27f52076)(const struct [device](structdevice.md) \*dev,

855 struct [tcpc\_chip\_info](structtcpc__chip__info.md) \*chip\_info)

856{

857 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

858 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

859

860 if (api->[get\_chip\_info](structtcpc__driver__api.md#a9ddaaae8e34bf36e868908d7555514dd) == NULL) {

861 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

862 }

863

864 return api->[get\_chip\_info](structtcpc__driver__api.md#a9ddaaae8e34bf36e868908d7555514dd)(dev, chip\_info);

865}

866

[ 877](group__usb__type__c__port__controller__api.md#ga961a4dc393d58dc44ea19a62c943ed48)static inline int [tcpc\_set\_low\_power\_mode](group__usb__type__c__port__controller__api.md#ga961a4dc393d58dc44ea19a62c943ed48)(const struct [device](structdevice.md) \*dev,

878 bool enable)

879{

880 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

881 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

882

883 if (api->[set\_low\_power\_mode](structtcpc__driver__api.md#ac70604b14dd7fe966489c159e1b3433d) == NULL) {

884 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

885 }

886

887 return api->[set\_low\_power\_mode](structtcpc__driver__api.md#ac70604b14dd7fe966489c159e1b3433d)(dev, enable);

888}

889

[ 900](group__usb__type__c__port__controller__api.md#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)static inline int [tcpc\_sop\_prime\_enable](group__usb__type__c__port__controller__api.md#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)(const struct [device](structdevice.md) \*dev,

901 bool enable)

902{

903 const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*api =

904 (const struct [tcpc\_driver\_api](structtcpc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

905

906 if (api->[sop\_prime\_enable](structtcpc__driver__api.md#a4402729135c40bbf30a18c148134b34c) == NULL) {

907 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

908 }

909

910 return api->[sop\_prime\_enable](structtcpc__driver__api.md#a4402729135c40bbf30a18c148134b34c)(dev, enable);

911}

912

916

917#ifdef \_\_cplusplus

918}

919#endif

920

921#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TCPC\_H\_ \*/

[cc](asm-macro-32-bit-gnu_8h.md#a6bcd6506e83f22db3e77c1172a6d7ba6)

irp cc

**Definition** asm-macro-32-bit-gnu.h:10

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[tcpc\_clear\_status\_register](group__usb__type__c__port__controller__api.md#ga00170b754d78d8eb7da24abd7d533e42)

static int tcpc\_clear\_status\_register(const struct device \*dev, enum tcpc\_status\_reg reg, uint32\_t mask)

Clears a TCPC status register.

**Definition** usbc\_tcpc.h:634

[tcpc\_set\_debug\_accessory](group__usb__type__c__port__controller__api.md#ga01687aa218b25ba137e994a2a55bce23)

static int tcpc\_set\_debug\_accessory(const struct device \*dev, bool enable)

Manual control of TCPC DebugAccessory control.

**Definition** usbc\_tcpc.h:684

[tcpc\_is\_cc\_src\_dbg\_acc](group__usb__type__c__port__controller__api.md#ga03849a7a4fd7f468b18838c443d1ecd8)

static int tcpc\_is\_cc\_src\_dbg\_acc(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if we detect the port partner is a src debug accessory.

**Definition** usbc\_tcpc.h:198

[tcpc\_get\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga03c8c6fc6f4c6adefacbc809588e1f85)

static int tcpc\_get\_src\_ctrl(const struct device \*dev)

Queries the current sourcing state of the TCPC.

**Definition** usbc\_tcpc.h:789

[tcpc\_get\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga0c1cd7bc86c89abf5e348987d34e4623)

static int tcpc\_get\_snk\_ctrl(const struct device \*dev)

Queries the current sinking state of the TCPC.

**Definition** usbc\_tcpc.h:749

[tcpc\_mask\_status\_register](group__usb__type__c__port__controller__api.md#ga0d1868d555e99877e062fb7135d9db8f)

static int tcpc\_mask\_status\_register(const struct device \*dev, enum tcpc\_status\_reg reg, uint32\_t mask)

Sets the mask of a TCPC status register.

**Definition** usbc\_tcpc.h:660

[tcpc\_is\_cc\_open](group__usb__type__c__port__controller__api.md#ga0db896e395812603a03548b8faac6791)

static int tcpc\_is\_cc\_open(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if both CC lines are completely open.

**Definition** usbc\_tcpc.h:180

[tcpc\_is\_cc\_audio\_acc](group__usb__type__c__port__controller__api.md#ga153054be89d5f21148fe3ee750c718ee)

static int tcpc\_is\_cc\_audio\_acc(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if the port partner is an audio accessory.

**Definition** usbc\_tcpc.h:207

[tcpc\_set\_vconn](group__usb__type__c__port__controller__api.md#ga247f0ea91249753d6f5eefe006617e41)

static int tcpc\_set\_vconn(const struct device \*dev, bool enable)

Enables or disables VCONN.

**Definition** usbc\_tcpc.h:422

[tcpc\_get\_rp\_value](group__usb__type__c__port__controller__api.md#ga25a110be90977e768623f3a0c9a222d5)

static int tcpc\_get\_rp\_value(const struct device \*dev, enum tc\_rp\_value \*rp)

Gets the value of the CC pull up resistor used when operating as a Source.

**Definition** usbc\_tcpc.h:308

[tcpc\_get\_rx\_pending\_msg](group__usb__type__c__port__controller__api.md#ga34e4caefb0f660b170f97956ac57b707)

static int tcpc\_get\_rx\_pending\_msg(const struct device \*dev, struct pd\_msg \*buf)

Retrieves the Power Delivery message from the TCPC.

**Definition** usbc\_tcpc.h:474

[tcpc\_vconn\_discharge](group__usb__type__c__port__controller__api.md#ga3937d66636a2b22422caf11c48f7628a)

static int tcpc\_vconn\_discharge(const struct device \*dev, bool enable)

Discharges VCONN.

**Definition** usbc\_tcpc.h:397

[tcpc\_select\_rp\_value](group__usb__type__c__port__controller__api.md#ga3958eac0cc0b9b2ac782e0cdb235036c)

static int tcpc\_select\_rp\_value(const struct device \*dev, enum tc\_rp\_value rp)

Sets the value of CC pull up resistor used when operating as a Source.

**Definition** usbc\_tcpc.h:286

[tcpc\_get\_status\_register](group__usb__type__c__port__controller__api.md#ga41e81b8f83e06934a5eb984ae6f980ec)

static int tcpc\_get\_status\_register(const struct device \*dev, enum tcpc\_status\_reg reg, int32\_t \*status)

Gets a status register.

**Definition** usbc\_tcpc.h:608

[tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2)

int(\* tcpc\_vconn\_discharge\_cb\_t)(const struct device \*dev, enum tc\_cc\_polarity pol, bool enable)

**Definition** usbc\_tcpc.h:123

[tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed)

tcpc\_alert

TCPC Alert bits.

**Definition** usbc\_tcpc.h:41

[tcpc\_set\_cc\_polarity](group__usb__type__c__port__controller__api.md#ga53f0207ecb63011c6dfc3c298a841ed4)

static int tcpc\_set\_cc\_polarity(const struct device \*dev, enum tc\_cc\_polarity polarity)

Sets the polarity of the CC lines.

**Definition** usbc\_tcpc.h:515

[tcpc\_alert\_handler\_cb\_t](group__usb__type__c__port__controller__api.md#ga5f42fa12f90d34961eeeb67c0dc4f925)

void(\* tcpc\_alert\_handler\_cb\_t)(const struct device \*dev, void \*data, enum tcpc\_alert alert)

**Definition** usbc\_tcpc.h:125

[tcpc\_get\_cc](group__usb__type__c__port__controller__api.md#ga66ab7a9f3cd1b80cd5bc8e99040c5627)

static int tcpc\_get\_cc(const struct device \*dev, enum tc\_cc\_voltage\_state \*cc1, enum tc\_cc\_voltage\_state \*cc2)

Reads the status of the CC lines.

**Definition** usbc\_tcpc.h:262

[tcpc\_is\_cc\_rp](group__usb__type__c__port__controller__api.md#ga6dfd68915ffe093058f6187b770a2436)

static int tcpc\_is\_cc\_rp(enum tc\_cc\_voltage\_state cc)

Returns whether the sink has detected a Rp resistor on the other side.

**Definition** usbc\_tcpc.h:171

[tcpc\_set\_alert\_handler\_cb](group__usb__type__c__port__controller__api.md#ga75f0dc246dac576f14c5ac51b45fd489)

static int tcpc\_set\_alert\_handler\_cb(const struct device \*dev, tcpc\_alert\_handler\_cb\_t handler, void \*data)

Sets the alert function that's called when an interrupt is triggered due to an alert bit.

**Definition** usbc\_tcpc.h:584

[tcpc\_set\_snk\_ctrl](group__usb__type__c__port__controller__api.md#ga7a63d55cbe5de1d89aa76e10df0140ed)

static int tcpc\_set\_snk\_ctrl(const struct device \*dev, bool enable)

Set the VBUS sinking state of the TCPC.

**Definition** usbc\_tcpc.h:769

[tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7)

int(\* tcpc\_vconn\_control\_cb\_t)(const struct device \*dev, enum tc\_cc\_polarity pol, bool enable)

**Definition** usbc\_tcpc.h:121

[tcpc\_get\_chip\_info](group__usb__type__c__port__controller__api.md#ga894d24140f8675b4f48d759c27f52076)

static int tcpc\_get\_chip\_info(const struct device \*dev, struct tcpc\_chip\_info \*chip\_info)

Gets the TCPC firmware version.

**Definition** usbc\_tcpc.h:854

[tcpc\_transmit\_data](group__usb__type__c__port__controller__api.md#ga8bf8fd202d582a4cc179a0fc4aff35e1)

static int tcpc\_transmit\_data(const struct device \*dev, struct pd\_msg \*msg)

Transmits a Power Delivery message.

**Definition** usbc\_tcpc.h:537

[tcpc\_set\_roles](group__usb__type__c__port__controller__api.md#ga8d30c961335f62faa33aa7d842422da0)

static int tcpc\_set\_roles(const struct device \*dev, enum tc\_power\_role power\_role, enum tc\_data\_role data\_role)

Sets the Power and Data Role of the PD message header.

**Definition** usbc\_tcpc.h:447

[tcpc\_set\_src\_ctrl](group__usb__type__c__port__controller__api.md#ga8f06b257d1bd0a17eb3042d204b2e6cd)

static int tcpc\_set\_src\_ctrl(const struct device \*dev, bool enable)

Set the VBUS sourcing state of the TCPC.

**Definition** usbc\_tcpc.h:809

[tcpc\_set\_rx\_enable](group__usb__type__c__port__controller__api.md#ga905176a77ff127f4df8f6a4f2c61a1b7)

static int tcpc\_set\_rx\_enable(const struct device \*dev, bool enable)

Enables the reception of SOP\* message types.

**Definition** usbc\_tcpc.h:494

[tcpc\_is\_cc\_only\_one\_rd](group__usb__type__c__port__controller__api.md#ga91c3c40ea82ce5a081918183d8b76c06)

static int tcpc\_is\_cc\_only\_one\_rd(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if the port partner is presenting Rd on only one CC line.

**Definition** usbc\_tcpc.h:225

[tcpc\_dump\_std\_reg](group__usb__type__c__port__controller__api.md#ga91eef7084b523f1991e000f0592b8cbd)

static int tcpc\_dump\_std\_reg(const struct device \*dev)

Dump a set of TCPC registers.

**Definition** usbc\_tcpc.h:559

[tcpc\_set\_low\_power\_mode](group__usb__type__c__port__controller__api.md#ga961a4dc393d58dc44ea19a62c943ed48)

static int tcpc\_set\_low\_power\_mode(const struct device \*dev, bool enable)

Instructs the TCPC to enter or exit low power mode.

**Definition** usbc\_tcpc.h:877

[tcpc\_set\_vconn\_discharge\_cb](group__usb__type__c__port__controller__api.md#ga975e7edea79de197c7230bd7b7a7efba)

static void tcpc\_set\_vconn\_discharge\_cb(const struct device \*dev, tcpc\_vconn\_discharge\_cb\_t cb)

Sets a callback that can enable or discharge VCONN if the TCPC is unable to or the system is configur...

**Definition** usbc\_tcpc.h:372

[tcpc\_set\_drp\_toggle](group__usb__type__c__port__controller__api.md#gaa06e156bef46ff3f70cc8c302ddf0a4d)

static int tcpc\_set\_drp\_toggle(const struct device \*dev, bool enable)

Enable TCPC auto dual role toggle.

**Definition** usbc\_tcpc.h:728

[tcpc\_is\_cc\_snk\_dbg\_acc](group__usb__type__c__port__controller__api.md#gaa0d2059c3a53df986150141f73b9a98a)

static int tcpc\_is\_cc\_snk\_dbg\_acc(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if we detect the port partner is a snk debug accessory.

**Definition** usbc\_tcpc.h:189

[tcpc\_set\_vconn\_cb](group__usb__type__c__port__controller__api.md#gaa608f2c6627c4a9c3039f0ec1b238bbc)

static void tcpc\_set\_vconn\_cb(const struct device \*dev, tcpc\_vconn\_control\_cb\_t vconn\_cb)

Sets a callback that can enable or disable VCONN if the TCPC is unable to or the system is configured...

**Definition** usbc\_tcpc.h:350

[tcpc\_set\_debug\_detach](group__usb__type__c__port__controller__api.md#gaaa38e56e6bc8c41e936d8ed70aaa8a23)

static int tcpc\_set\_debug\_detach(const struct device \*dev)

Detach from a debug connection.

**Definition** usbc\_tcpc.h:706

[tcpc\_sop\_prime\_enable](group__usb__type__c__port__controller__api.md#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)

static int tcpc\_sop\_prime\_enable(const struct device \*dev, bool enable)

Enables the reception of SOP Prime messages.

**Definition** usbc\_tcpc.h:900

[tcpc\_is\_cc\_at\_least\_one\_rd](group__usb__type__c__port__controller__api.md#gab4e9cc812679cf8cb0189f73a28d7cd2)

static int tcpc\_is\_cc\_at\_least\_one\_rd(enum tc\_cc\_voltage\_state cc1, enum tc\_cc\_voltage\_state cc2)

Returns true if the port partner is presenting at least one Rd.

**Definition** usbc\_tcpc.h:216

[tcpc\_init](group__usb__type__c__port__controller__api.md#gabc50daa9cc713b1d0e340007e3850ca8)

static int tcpc\_init(const struct device \*dev)

Initializes the TCPC.

**Definition** usbc\_tcpc.h:240

[tcpc\_set\_cc](group__usb__type__c__port__controller__api.md#gac5737d02caa2b9e649b469bcd648440f)

static int tcpc\_set\_cc(const struct device \*dev, enum tc\_cc\_pull pull)

Sets the CC pull resistor and sets the role as either Source or Sink.

**Definition** usbc\_tcpc.h:329

[tcpc\_set\_bist\_test\_mode](group__usb__type__c__port__controller__api.md#gaccc728a1f27c59a163a5c0a221ab7c18)

static int tcpc\_set\_bist\_test\_mode(const struct device \*dev, bool enable)

Controls the BIST Mode of the TCPC.

**Definition** usbc\_tcpc.h:831

[tcpc\_status\_reg](group__usb__type__c__port__controller__api.md#gafd8253dfa6abc80d0717b17271ed8916)

tcpc\_status\_reg

TCPC Status register.

**Definition** usbc\_tcpc.h:85

[TCPC\_ALERT\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9)

@ TCPC\_ALERT\_EXTENDED\_STATUS

Extended status changed.

**Definition** usbc\_tcpc.h:72

[TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe)

@ TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED

Reset or SOP\* message transmission not sent due to an incoming receive message.

**Definition** usbc\_tcpc.h:56

[TCPC\_ALERT\_CC\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f)

@ TCPC\_ALERT\_CC\_STATUS

CC status changed.

**Definition** usbc\_tcpc.h:43

[TCPC\_ALERT\_EXTENDED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25)

@ TCPC\_ALERT\_EXTENDED

An extended interrupt event has occurred.

**Definition** usbc\_tcpc.h:77

[TCPC\_ALERT\_BEGINNING\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb)

@ TCPC\_ALERT\_BEGINNING\_MSG\_STATUS

Receive buffer register changed.

**Definition** usbc\_tcpc.h:70

[TCPC\_ALERT\_MSG\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb)

@ TCPC\_ALERT\_MSG\_STATUS

Receive Buffer register changed.

**Definition** usbc\_tcpc.h:47

[TCPC\_ALERT\_HARD\_RESET\_RECEIVED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0)

@ TCPC\_ALERT\_HARD\_RESET\_RECEIVED

Received Hard Reset message.

**Definition** usbc\_tcpc.h:49

[TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2)

@ TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS

Reset or SOP\* message transmission successful.

**Definition** usbc\_tcpc.h:58

[TCPC\_ALERT\_VBUS\_ALARM\_HI](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66)

@ TCPC\_ALERT\_VBUS\_ALARM\_HI

A high-voltage alarm has occurred.

**Definition** usbc\_tcpc.h:60

[TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd)

@ TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT

The TCPC in Attached.SNK state has detected a sink disconnect.

**Definition** usbc\_tcpc.h:68

[TCPC\_ALERT\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4)

@ TCPC\_ALERT\_POWER\_STATUS

Power status changed.

**Definition** usbc\_tcpc.h:45

[TCPC\_ALERT\_VBUS\_ALARM\_LO](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0)

@ TCPC\_ALERT\_VBUS\_ALARM\_LO

A low-voltage alarm has occurred.

**Definition** usbc\_tcpc.h:62

[TCPC\_ALERT\_VENDOR\_DEFINED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)

@ TCPC\_ALERT\_VENDOR\_DEFINED

A vendor defined alert has been detected.

**Definition** usbc\_tcpc.h:79

[TCPC\_ALERT\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e)

@ TCPC\_ALERT\_FAULT\_STATUS

A fault has occurred.

**Definition** usbc\_tcpc.h:64

[TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec)

@ TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED

SOP\* message transmission not successful.

**Definition** usbc\_tcpc.h:51

[TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW](group__usb__type__c__port__controller__api.md#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752)

@ TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW

TCPC RX buffer has overflowed.

**Definition** usbc\_tcpc.h:66

[TCPC\_FAULT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440)

@ TCPC\_FAULT\_STATUS

The Fault Status register.

**Definition** usbc\_tcpc.h:91

[TCPC\_VENDOR\_DEFINED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)

@ TCPC\_VENDOR\_DEFINED\_STATUS

The Vendor Defined Status register.

**Definition** usbc\_tcpc.h:97

[TCPC\_EXTENDED\_ALERT\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db)

@ TCPC\_EXTENDED\_ALERT\_STATUS

The Extended Alert Status register.

**Definition** usbc\_tcpc.h:95

[TCPC\_POWER\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f)

@ TCPC\_POWER\_STATUS

The Power Status register.

**Definition** usbc\_tcpc.h:89

[TCPC\_CC\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4)

@ TCPC\_CC\_STATUS

The CC Status register.

**Definition** usbc\_tcpc.h:87

[TCPC\_EXTENDED\_STATUS](group__usb__type__c__port__controller__api.md#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d)

@ TCPC\_EXTENDED\_STATUS

The Extended Status register.

**Definition** usbc\_tcpc.h:93

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

[TC\_CC\_VOLT\_RP\_DEF](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)

@ TC\_CC\_VOLT\_RP\_DEF

Port partner is applying Rp (0.5A).

**Definition** usbc\_tc.h:316

[TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea)

@ TC\_CC\_VOLT\_RA

Port partner is applying Ra.

**Definition** usbc\_tc.h:312

[TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)

@ TC\_CC\_VOLT\_RD

Port partner is applying Rd.

**Definition** usbc\_tc.h:314

[TC\_CC\_VOLT\_RP\_3A0](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca)

@ TC\_CC\_VOLT\_RP\_3A0

Port partner is applying Rp (3.0A).

**Definition** usbc\_tc.h:320

[TC\_CC\_VOLT\_RP\_1A5](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)

@ TC\_CC\_VOLT\_RP\_1A5

**Definition** usbc\_tc.h:318

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[pd\_msg](structpd__msg.md)

Power Delivery message.

**Definition** usbc\_pd.h:1040

[tcpc\_chip\_info](structtcpc__chip__info.md)

TCPC Chip Information.

**Definition** usbc\_tcpc.h:103

[tcpc\_chip\_info::product\_id](structtcpc__chip__info.md#a14c11999ef548e41f4338f3e7208b7a9)

uint16\_t product\_id

Product Id.

**Definition** usbc\_tcpc.h:107

[tcpc\_chip\_info::min\_req\_fw\_version\_string](structtcpc__chip__info.md#a677a85ef27f0d5db969ce3232506d1bb)

uint8\_t min\_req\_fw\_version\_string[8]

Minimum Required firmware version string.

**Definition** usbc\_tcpc.h:115

[tcpc\_chip\_info::fw\_version\_number](structtcpc__chip__info.md#a7789339580e2774d18a8f4c78332f774)

uint64\_t fw\_version\_number

Firmware version number.

**Definition** usbc\_tcpc.h:111

[tcpc\_chip\_info::min\_req\_fw\_version\_number](structtcpc__chip__info.md#a8d66f33379493e1a0ed707b3715f863a)

uint64\_t min\_req\_fw\_version\_number

Minimum Required firmware version number.

**Definition** usbc\_tcpc.h:117

[tcpc\_chip\_info::device\_id](structtcpc__chip__info.md#a9e76ee3bcc395dbb77d7a065f6181cd6)

uint16\_t device\_id

Device Id.

**Definition** usbc\_tcpc.h:109

[tcpc\_chip\_info::vendor\_id](structtcpc__chip__info.md#ab48400ea4209d5443e5b7e0bfee6c4fc)

uint16\_t vendor\_id

Vendor Id.

**Definition** usbc\_tcpc.h:105

[tcpc\_driver\_api](structtcpc__driver__api.md)

**Definition** usbc\_tcpc.h:128

[tcpc\_driver\_api::init](structtcpc__driver__api.md#a00ee20f4d78ec1e337b614afdfa3a686)

int(\* init)(const struct device \*dev)

**Definition** usbc\_tcpc.h:129

[tcpc\_driver\_api::vconn\_discharge](structtcpc__driver__api.md#a06bf9faa692527225dc6a8224f37fe24)

int(\* vconn\_discharge)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:137

[tcpc\_driver\_api::set\_debug\_accessory](structtcpc__driver__api.md#a0bd24553cc59c3947f6ec634a2a611e0)

int(\* set\_debug\_accessory)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:153

[tcpc\_driver\_api::get\_rx\_pending\_msg](structtcpc__driver__api.md#a0d5fb6c9f3724b38d627fb51f70d6583)

int(\* get\_rx\_pending\_msg)(const struct device \*dev, struct pd\_msg \*msg)

**Definition** usbc\_tcpc.h:141

[tcpc\_driver\_api::dump\_std\_reg](structtcpc__driver__api.md#a11ecbb4c78aecb278e1a3568d032c05a)

int(\* dump\_std\_reg)(const struct device \*dev)

**Definition** usbc\_tcpc.h:145

[tcpc\_driver\_api::select\_rp\_value](structtcpc__driver__api.md#a1eb311c296cfce9759d0f3137210fe6f)

int(\* select\_rp\_value)(const struct device \*dev, enum tc\_rp\_value rp)

**Definition** usbc\_tcpc.h:132

[tcpc\_driver\_api::alert\_handler\_cb](structtcpc__driver__api.md#a271fc8d67338a4e7384d4f938026a5f3)

void(\* alert\_handler\_cb)(const struct device \*dev, void \*data, enum tcpc\_alert alert)

**Definition** usbc\_tcpc.h:146

[tcpc\_driver\_api::set\_vconn\_discharge\_cb](structtcpc__driver__api.md#a291abd7642114da14031811f55c8991a)

void(\* set\_vconn\_discharge\_cb)(const struct device \*dev, tcpc\_vconn\_discharge\_cb\_t cb)

**Definition** usbc\_tcpc.h:135

[tcpc\_driver\_api::set\_snk\_ctrl](structtcpc__driver__api.md#a2aa06dc38fcf6d0d044d2094481c43c5)

int(\* set\_snk\_ctrl)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:157

[tcpc\_driver\_api::set\_rx\_enable](structtcpc__driver__api.md#a3440cc5751b0820b7fd7f4c288089e23)

int(\* set\_rx\_enable)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:142

[tcpc\_driver\_api::set\_cc](structtcpc__driver__api.md#a4263d2b2b1e1e2002c09ef2ecb3c5a36)

int(\* set\_cc)(const struct device \*dev, enum tc\_cc\_pull pull)

**Definition** usbc\_tcpc.h:134

[tcpc\_driver\_api::set\_roles](structtcpc__driver__api.md#a43d110db7d4808939d24850f2c6a73be)

int(\* set\_roles)(const struct device \*dev, enum tc\_power\_role power\_role, enum tc\_data\_role data\_role)

**Definition** usbc\_tcpc.h:139

[tcpc\_driver\_api::sop\_prime\_enable](structtcpc__driver__api.md#a4402729135c40bbf30a18c148134b34c)

int(\* sop\_prime\_enable)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:162

[tcpc\_driver\_api::clear\_status\_register](structtcpc__driver__api.md#a45a1d895153d5e7182313a15e6908df0)

int(\* clear\_status\_register)(const struct device \*dev, enum tcpc\_status\_reg reg, uint32\_t mask)

**Definition** usbc\_tcpc.h:149

[tcpc\_driver\_api::get\_snk\_ctrl](structtcpc__driver__api.md#a4a798a34ade8740ae3fff0a943c42ddd)

int(\* get\_snk\_ctrl)(const struct device \*dev)

**Definition** usbc\_tcpc.h:156

[tcpc\_driver\_api::get\_src\_ctrl](structtcpc__driver__api.md#a4ba0050fb389cd281deedbe327eca49e)

int(\* get\_src\_ctrl)(const struct device \*dev)

**Definition** usbc\_tcpc.h:158

[tcpc\_driver\_api::set\_vconn](structtcpc__driver__api.md#a639486f042727c23781e90d725ac17fc)

int(\* set\_vconn)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:138

[tcpc\_driver\_api::set\_src\_ctrl](structtcpc__driver__api.md#a797e6472126c3a02b8651cbc40395526)

int(\* set\_src\_ctrl)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:159

[tcpc\_driver\_api::set\_cc\_polarity](structtcpc__driver__api.md#a7bbd6583cfc43ac235333aad93cc79e3)

int(\* set\_cc\_polarity)(const struct device \*dev, enum tc\_cc\_polarity polarity)

**Definition** usbc\_tcpc.h:143

[tcpc\_driver\_api::get\_chip\_info](structtcpc__driver__api.md#a9ddaaae8e34bf36e868908d7555514dd)

int(\* get\_chip\_info)(const struct device \*dev, struct tcpc\_chip\_info \*chip\_info)

**Definition** usbc\_tcpc.h:160

[tcpc\_driver\_api::get\_status\_register](structtcpc__driver__api.md#aa3d97fe5bc52b144a22551e38867fd2e)

int(\* get\_status\_register)(const struct device \*dev, enum tcpc\_status\_reg reg, int32\_t \*status)

**Definition** usbc\_tcpc.h:147

[tcpc\_driver\_api::transmit\_data](structtcpc__driver__api.md#abffc63aa90730025fae61891cb228cd4)

int(\* transmit\_data)(const struct device \*dev, struct pd\_msg \*msg)

**Definition** usbc\_tcpc.h:144

[tcpc\_driver\_api::set\_low\_power\_mode](structtcpc__driver__api.md#ac70604b14dd7fe966489c159e1b3433d)

int(\* set\_low\_power\_mode)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:161

[tcpc\_driver\_api::mask\_status\_register](structtcpc__driver__api.md#ac8750dd530c23a02e548b8b01c8abda3)

int(\* mask\_status\_register)(const struct device \*dev, enum tcpc\_status\_reg reg, uint32\_t mask)

**Definition** usbc\_tcpc.h:151

[tcpc\_driver\_api::set\_debug\_detach](structtcpc__driver__api.md#ad3d06d75563e7a8f00a9a61fe279a6bc)

int(\* set\_debug\_detach)(const struct device \*dev)

**Definition** usbc\_tcpc.h:154

[tcpc\_driver\_api::get\_rp\_value](structtcpc__driver__api.md#ad3fe740a7b85807242c03b6f32a7dea7)

int(\* get\_rp\_value)(const struct device \*dev, enum tc\_rp\_value \*rp)

**Definition** usbc\_tcpc.h:133

[tcpc\_driver\_api::set\_vconn\_cb](structtcpc__driver__api.md#ad6b5fb88b0b39fd29584c2a2de685c20)

void(\* set\_vconn\_cb)(const struct device \*dev, tcpc\_vconn\_control\_cb\_t vconn\_cb)

**Definition** usbc\_tcpc.h:136

[tcpc\_driver\_api::set\_alert\_handler\_cb](structtcpc__driver__api.md#adc0c8e5f174549fb7683028c58e890bd)

int(\* set\_alert\_handler\_cb)(const struct device \*dev, tcpc\_alert\_handler\_cb\_t handler, void \*data)

**Definition** usbc\_tcpc.h:164

[tcpc\_driver\_api::get\_cc](structtcpc__driver__api.md#ae4b2588a327da51b961d7a00159e5aab)

int(\* get\_cc)(const struct device \*dev, enum tc\_cc\_voltage\_state \*cc1, enum tc\_cc\_voltage\_state \*cc2)

**Definition** usbc\_tcpc.h:130

[tcpc\_driver\_api::set\_drp\_toggle](structtcpc__driver__api.md#aed51c3046411854b7be470d761e77faa)

int(\* set\_drp\_toggle)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:155

[tcpc\_driver\_api::set\_bist\_test\_mode](structtcpc__driver__api.md#afba03924bd5b3f62733309b9a0084552)

int(\* set\_bist\_test\_mode)(const struct device \*dev, bool enable)

**Definition** usbc\_tcpc.h:163

[usbc\_pd.h](usbc__pd_8h.md)

USB-C Power Delivery API used for USB-C drivers.

[usbc\_tc.h](usbc__tc_8h.md)

USB Type-C Cable and Connector API used for USB-C drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_tcpc.h](usbc__tcpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
