---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/udc_8h_source.html
original_path: doxygen/html/udc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc.h

[Go to the documentation of this file.](udc_8h.md)

1/\*

2 \* Copyright (c) 2021-2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_UDC\_H

13#define ZEPHYR\_INCLUDE\_UDC\_H

14

15#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/net/buf.h](net_2buf_8h.md)>

18#include <[zephyr/sys/atomic.h](atomic_8h.md)>

19#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

20

[ 24](udc_8h.md#ac254f8a970f890d14e35c43474c915fd)enum [udc\_mps0](udc_8h.md#ac254f8a970f890d14e35c43474c915fd) {

[ 25](udc_8h.md#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb) [UDC\_MPS0\_8](udc_8h.md#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb),

[ 26](udc_8h.md#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a) [UDC\_MPS0\_16](udc_8h.md#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a),

[ 27](udc_8h.md#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7) [UDC\_MPS0\_32](udc_8h.md#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7),

[ 28](udc_8h.md#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a) [UDC\_MPS0\_64](udc_8h.md#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a),

29};

30

[ 36](structudc__device__caps.md)struct [udc\_device\_caps](structudc__device__caps.md) {

[ 38](structudc__device__caps.md#aea376ff4a0c5a27c3b8f7d4416e17b5b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hs](structudc__device__caps.md#aea376ff4a0c5a27c3b8f7d4416e17b5b) : 1;

[ 40](structudc__device__caps.md#aab85e74e40876040c3d2f961c36b9780) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rwup](structudc__device__caps.md#aab85e74e40876040c3d2f961c36b9780) : 1;

[ 42](structudc__device__caps.md#a0adada5003bccfbd6df8329198639dc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [out\_ack](structudc__device__caps.md#a0adada5003bccfbd6df8329198639dc0) : 1;

[ 44](structudc__device__caps.md#aefef262532e3eab3baa90eb8e79f9dc8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [addr\_before\_status](structudc__device__caps.md#aefef262532e3eab3baa90eb8e79f9dc8) : 1;

[ 46](structudc__device__caps.md#a63affa3fe08cbaec8351297ad9d26911) enum [udc\_mps0](udc_8h.md#ac254f8a970f890d14e35c43474c915fd) [mps0](structudc__device__caps.md#a63affa3fe08cbaec8351297ad9d26911) : 2;

47};

48

[ 52](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b)enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b) {

[ 54](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d) [UDC\_BUS\_UNKNOWN](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d),

[ 56](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5) [UDC\_BUS\_SPEED\_FS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5),

[ 58](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599) [UDC\_BUS\_SPEED\_HS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599),

[ 60](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a) [UDC\_BUS\_SPEED\_SS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a),

61};

62

[ 66](structudc__ep__caps.md)struct [udc\_ep\_caps](structudc__ep__caps.md) {

[ 68](structudc__ep__caps.md#a5e90d1362855dd77a1f7ef9e0cd82ef8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mps](structudc__ep__caps.md#a5e90d1362855dd77a1f7ef9e0cd82ef8) : 16;

[ 70](structudc__ep__caps.md#a98afb85c03ff01ba82d55884cea0ea31) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [control](structudc__ep__caps.md#a98afb85c03ff01ba82d55884cea0ea31) : 1;

[ 72](structudc__ep__caps.md#a73f06f9e2af5770cab84d2adb76d42de) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interrupt](structudc__ep__caps.md#a73f06f9e2af5770cab84d2adb76d42de) : 1;

[ 74](structudc__ep__caps.md#a73ec7e7c7fd043065a7c59c89c6cc36e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bulk](structudc__ep__caps.md#a73ec7e7c7fd043065a7c59c89c6cc36e) : 1;

[ 76](structudc__ep__caps.md#a15ce10028e09b3af021a83dc36eba99a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iso](structudc__ep__caps.md#a15ce10028e09b3af021a83dc36eba99a) : 1;

[ 78](structudc__ep__caps.md#a3a944cda429c916b60cff3a332b970a7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [in](structudc__ep__caps.md#a3a944cda429c916b60cff3a332b970a7) : 1;

[ 80](structudc__ep__caps.md#afc424ee2bb31c19451facc0b79bb73c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [out](structudc__ep__caps.md#afc424ee2bb31c19451facc0b79bb73c7) : 1;

81};

82

[ 86](structudc__ep__stat.md)struct [udc\_ep\_stat](structudc__ep__stat.md) {

[ 88](structudc__ep__stat.md#a448c82eb3884dba20e1bdf0980d3a2b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enabled](structudc__ep__stat.md#a448c82eb3884dba20e1bdf0980d3a2b3) : 1;

[ 90](structudc__ep__stat.md#af245db473a046885e4f97b00493718e2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [halted](structudc__ep__stat.md#af245db473a046885e4f97b00493718e2) : 1;

[ 92](structudc__ep__stat.md#a30b66675236f30c75837c446b87ced91) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data1](structudc__ep__stat.md#a30b66675236f30c75837c446b87ced91) : 1;

[ 94](structudc__ep__stat.md#a0a437fb1e4b9a79eea7e4c6b0316c450) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [odd](structudc__ep__stat.md#a0a437fb1e4b9a79eea7e4c6b0316c450) : 1;

[ 96](structudc__ep__stat.md#ad515a667ffd705408617dd28700db1e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [busy](structudc__ep__stat.md#ad515a667ffd705408617dd28700db1e9) : 1;

97};

98

[ 106](structudc__ep__config.md)struct [udc\_ep\_config](structudc__ep__config.md) {

[ 108](structudc__ep__config.md#aa62ff3f308771d51563df88439570918) struct [k\_fifo](structk__fifo.md) [fifo](structudc__ep__config.md#aa62ff3f308771d51563df88439570918);

[ 110](structudc__ep__config.md#a706987205ac971574d1b81bf72d03248) struct [udc\_ep\_caps](structudc__ep__caps.md) [caps](structudc__ep__config.md#a706987205ac971574d1b81bf72d03248);

[ 112](structudc__ep__config.md#ad42f77d1a9d65239cdb142209050e38e) struct [udc\_ep\_stat](structudc__ep__stat.md) [stat](structudc__ep__config.md#ad42f77d1a9d65239cdb142209050e38e);

[ 114](structudc__ep__config.md#ac795b839cbd426d233a1f91d10d5fc7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structudc__ep__config.md#ac795b839cbd426d233a1f91d10d5fc7e);

[ 116](structudc__ep__config.md#acbeab755d1b03da0c58f43aff5bd7d00) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [attributes](structudc__ep__config.md#acbeab755d1b03da0c58f43aff5bd7d00);

[ 118](structudc__ep__config.md#ae4f75e52d1c822f5d873095a761c6b48) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structudc__ep__config.md#ae4f75e52d1c822f5d873095a761c6b48);

[ 120](structudc__ep__config.md#a1f2afc2d5e512229688764e1b7cd0171) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [interval](structudc__ep__config.md#a1f2afc2d5e512229688764e1b7cd0171);

121};

122

123

[ 127](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040)enum [udc\_event\_type](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040) {

[ 129](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d) [UDC\_EVT\_VBUS\_READY](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d),

[ 131](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432) [UDC\_EVT\_VBUS\_REMOVED](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432),

[ 133](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332) [UDC\_EVT\_RESUME](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332),

[ 135](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f) [UDC\_EVT\_SUSPEND](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f),

[ 137](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb) [UDC\_EVT\_RESET](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb),

[ 139](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78) [UDC\_EVT\_SOF](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78),

[ 141](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b) [UDC\_EVT\_EP\_REQUEST](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b),

[ 146](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d) [UDC\_EVT\_ERROR](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d),

147};

148

[ 157](structudc__event.md)struct [udc\_event](structudc__event.md) {

[ 159](structudc__event.md#a3acfe5d21d16f6edfa24e9964b636434) enum [udc\_event\_type](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040) [type](structudc__event.md#a3acfe5d21d16f6edfa24e9964b636434);

160 union {

[ 162](structudc__event.md#ada24e0e920c39bc60a6c7fbbe54277f4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](structudc__event.md#ada24e0e920c39bc60a6c7fbbe54277f4);

[ 164](structudc__event.md#a0707d65716a4b1e6dd3132a0bb370770) int [status](structudc__event.md#a0707d65716a4b1e6dd3132a0bb370770);

[ 166](structudc__event.md#ac1ff3bc9d629eb9b6c55602e7861e945) struct [net\_buf](structnet__buf.md) \*[buf](structudc__event.md#ac1ff3bc9d629eb9b6c55602e7861e945);

167 };

[ 169](structudc__event.md#a900404c46850d34cd7121eeedc2fce9d) const struct [device](structdevice.md) \*[dev](structudc__event.md#a900404c46850d34cd7121eeedc2fce9d);

170};

171

[ 179](structudc__buf__info.md)struct [udc\_buf\_info](structudc__buf__info.md) {

[ 181](structudc__buf__info.md#a0a1c09f587d3f6847cb7ce77514a3321) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structudc__buf__info.md#a0a1c09f587d3f6847cb7ce77514a3321);

[ 183](structudc__buf__info.md#a9664e1f7cddd36dbc7d206b52da45170) unsigned int [setup](structudc__buf__info.md#a9664e1f7cddd36dbc7d206b52da45170) : 1;

[ 185](structudc__buf__info.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2) unsigned int [data](structudc__buf__info.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2) : 1;

[ 187](structudc__buf__info.md#a84cf74496eddc4a69a47d23dcdbf753f) unsigned int [status](structudc__buf__info.md#a84cf74496eddc4a69a47d23dcdbf753f) : 1;

[ 189](structudc__buf__info.md#afc2d0c391aca7f68a1ae5539a1fed8a0) unsigned int [zlp](structudc__buf__info.md#afc2d0c391aca7f68a1ae5539a1fed8a0) : 1;

[ 191](structudc__buf__info.md#a9b03b6dd8418d4200733a612aac73daa) unsigned int [claimed](structudc__buf__info.md#a9b03b6dd8418d4200733a612aac73daa) : 1;

[ 193](structudc__buf__info.md#a4cd2e83000a0551d126bebe89552eab9) unsigned int [queued](structudc__buf__info.md#a4cd2e83000a0551d126bebe89552eab9) : 1;

[ 195](structudc__buf__info.md#a33e927f23d227a4974915c65927284ec) void \*[owner](structudc__buf__info.md#a33e927f23d227a4974915c65927284ec);

[ 197](structudc__api.md#adf2b8f76158d7bd2d3918628c8a9fc22) int [err](structudc__buf__info.md#af1c92f1cdd6e0474a19f788140fdc573);

198} \_\_packed;

199

[ 213](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a)typedef int (\*[udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a))(const struct [device](structdevice.md) \*dev,

214 const struct [udc\_event](structudc__event.md) \*const event);

215

[ 222](structudc__api.md)struct [udc\_api](structudc__api.md) {

223 enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b) (\*[device\_speed](structudc__api.md#adf2b8f76158d7bd2d3918628c8a9fc22))(const struct [device](structdevice.md) \*dev);

[ 224](structudc__api.md#aa1d3dadf63cb156ce5346712e1c65069) int (\*[ep\_enqueue](structudc__api.md#aa1d3dadf63cb156ce5346712e1c65069))(const struct [device](structdevice.md) \*dev,

225 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg,

226 struct [net\_buf](structnet__buf.md) \*const buf);

[ 227](structudc__api.md#a023fcfa0fa251dcadcb379347fe7531a) int (\*[ep\_dequeue](structudc__api.md#a023fcfa0fa251dcadcb379347fe7531a))(const struct [device](structdevice.md) \*dev,

228 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 229](structudc__api.md#adf2adaea90b53999d1e98756062a2050) int (\*[ep\_set\_halt](structudc__api.md#adf2adaea90b53999d1e98756062a2050))(const struct [device](structdevice.md) \*dev,

230 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 231](structudc__api.md#a923a684868721d0b7232c86eed15e121) int (\*[ep\_clear\_halt](structudc__api.md#a923a684868721d0b7232c86eed15e121))(const struct [device](structdevice.md) \*dev,

232 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 233](structudc__api.md#a775a18f5555f1c518762ff7dc016559c) int (\*[ep\_try\_config](structudc__api.md#a775a18f5555f1c518762ff7dc016559c))(const struct [device](structdevice.md) \*dev,

234 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 235](structudc__api.md#a27291ab4d2acda207f6a6a2313d50793) int (\*[ep\_enable](structudc__api.md#a27291ab4d2acda207f6a6a2313d50793))(const struct [device](structdevice.md) \*dev,

236 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 237](structudc__api.md#a1af05b484e9c9d1f2a0dbfb822f09c98) int (\*[ep\_disable](structudc__api.md#a1af05b484e9c9d1f2a0dbfb822f09c98))(const struct [device](structdevice.md) \*dev,

238 struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg);

[ 239](structudc__api.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb) int (\*[host\_wakeup](structudc__api.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb))(const struct [device](structdevice.md) \*dev);

[ 240](structudc__api.md#a2e8b88743ab56144a199b3ad0618755f) int (\*[set\_address](structudc__api.md#a2e8b88743ab56144a199b3ad0618755f))(const struct [device](structdevice.md) \*dev,

241 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

[ 242](structudc__api.md#ab06839ded48cbc671b2b915fe0010959) int (\*[test\_mode](structudc__api.md#ab06839ded48cbc671b2b915fe0010959))(const struct [device](structdevice.md) \*dev,

243 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const bool dryrun);

[ 244](structudc__api.md#af8b916f6b8c211ad82ddcfdaa12de5ae) int (\*[enable](structudc__api.md#af8b916f6b8c211ad82ddcfdaa12de5ae))(const struct [device](structdevice.md) \*dev);

[ 245](structudc__api.md#a8997bba956d264463b71aae0b1a4e3dc) int (\*[disable](structudc__api.md#a8997bba956d264463b71aae0b1a4e3dc))(const struct [device](structdevice.md) \*dev);

[ 246](structudc__api.md#a01f803a2d258072df102b831cf184b27) int (\*[init](structudc__api.md#a01f803a2d258072df102b831cf184b27))(const struct [device](structdevice.md) \*dev);

[ 247](structudc__api.md#ad7135abf78eb372730dddbba7dc6a75d) int (\*[shutdown](structudc__api.md#ad7135abf78eb372730dddbba7dc6a75d))(const struct [device](structdevice.md) \*dev);

[ 248](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141) int (\*[lock](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141))(const struct [device](structdevice.md) \*dev);

[ 249](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201) int (\*[unlock](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201))(const struct [device](structdevice.md) \*dev);

250};

251

[ 256](udc_8h.md#a8c96946734085924e2afc591ac502551)#define UDC\_STATUS\_INITIALIZED 0

[ 261](udc_8h.md#ad10596af54465c3cb10cc59ae9a507d2)#define UDC\_STATUS\_ENABLED 1

[ 263](udc_8h.md#ac3a36aa8cb3aab95d7931cb602631c36)#define UDC\_STATUS\_SUSPENDED 2

264

[ 271](structudc__data.md)struct [udc\_data](structudc__data.md) {

[ 273](structudc__data.md#acc471b34bb24453377b1ae54d33fa415) struct [udc\_ep\_config](structudc__ep__config.md) \*[ep\_lut](structudc__data.md#acc471b34bb24453377b1ae54d33fa415)[32];

[ 275](structudc__data.md#aae68bfba2e92894851c36dd40c33c0f0) struct [udc\_device\_caps](structudc__device__caps.md) [caps](structudc__data.md#aae68bfba2e92894851c36dd40c33c0f0);

[ 277](structudc__data.md#a1ba1b93af26bca4f4554a43a65ab3c2a) struct [k\_mutex](structk__mutex.md) [mutex](structudc__data.md#a1ba1b93af26bca4f4554a43a65ab3c2a);

[ 279](structudc__data.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381) [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) [event\_cb](structudc__data.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381);

[ 281](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [status](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f);

[ 283](structudc__data.md#ab957eea73de90379642ed56ddbb84989) int [stage](structudc__data.md#ab957eea73de90379642ed56ddbb84989);

[ 285](structudc__data.md#a1bbb7a70a14368efc4b933a7d1945fb5) struct [net\_buf](structnet__buf.md) \*[setup](structudc__data.md#a1bbb7a70a14368efc4b933a7d1945fb5);

[ 287](structudc__data.md#ac58682fa2f37bf2034a69cc9b6b10dfb) void \*[priv](structudc__data.md#ac58682fa2f37bf2034a69cc9b6b10dfb);

288};

289

296

[ 304](group__udc__api.md#ga40e50cf79b40d3792513e8fea3347f59)static inline bool [udc\_is\_initialized](group__udc__api.md#ga40e50cf79b40d3792513e8fea3347f59)(const struct [device](structdevice.md) \*dev)

305{

306 struct [udc\_data](structudc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

307

308 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f), [UDC\_STATUS\_INITIALIZED](udc_8h.md#a8c96946734085924e2afc591ac502551));

309}

310

[ 318](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)static inline bool [udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)(const struct [device](structdevice.md) \*dev)

319{

320 struct [udc\_data](structudc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

321

322 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f), [UDC\_STATUS\_ENABLED](udc_8h.md#ad10596af54465c3cb10cc59ae9a507d2));

323}

324

[ 332](group__udc__api.md#ga88786eda763fce5c2a51521650ccc9f4)static inline bool [udc\_is\_suspended](group__udc__api.md#ga88786eda763fce5c2a51521650ccc9f4)(const struct [device](structdevice.md) \*dev)

333{

334 struct [udc\_data](structudc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

335

336 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f), [UDC\_STATUS\_SUSPENDED](udc_8h.md#ac3a36aa8cb3aab95d7931cb602631c36));

337}

338

[ 353](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c)int [udc\_init](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c)(const struct [device](structdevice.md) \*dev, [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) [event\_cb](structudc__data.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381));

354

[ 367](group__udc__api.md#gafbb0dec089f83fd674bd19670a882c65)int [udc\_enable](group__udc__api.md#gafbb0dec089f83fd674bd19670a882c65)(const struct [device](structdevice.md) \*dev);

368

[ 380](group__udc__api.md#gaa7c2eaa52bdbe1d763b2961124570e8a)int [udc\_disable](group__udc__api.md#gaa7c2eaa52bdbe1d763b2961124570e8a)(const struct [device](structdevice.md) \*dev);

381

[ 393](group__udc__api.md#ga59a92eb60575ca80d205cc29b4fb4f21)int [udc\_shutdown](group__udc__api.md#ga59a92eb60575ca80d205cc29b4fb4f21)(const struct [device](structdevice.md) \*dev);

394

[ 405](group__udc__api.md#ga3ee738bad8e1ee3928d32f57f82bef70)static inline struct [udc\_device\_caps](structudc__device__caps.md) [udc\_caps](group__udc__api.md#ga3ee738bad8e1ee3928d32f57f82bef70)(const struct [device](structdevice.md) \*dev)

406{

407 struct [udc\_data](structudc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

408

409 return data->[caps](structudc__data.md#aae68bfba2e92894851c36dd40c33c0f0);

410}

411

[ 422](group__udc__api.md#gab936f04015b0fee584756bcdf40d2f50)enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b) [udc\_device\_speed](group__udc__api.md#gab936f04015b0fee584756bcdf40d2f50)(const struct [device](structdevice.md) \*dev);

423

[ 435](group__udc__api.md#ga6feb32a2263307bdde9acc63d3c2ebb1)static inline int [udc\_set\_address](group__udc__api.md#ga6feb32a2263307bdde9acc63d3c2ebb1)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr)

436{

437 const struct [udc\_api](structudc__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

438 int ret;

439

440 if (![udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)(dev)) {

441 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

442 }

443

444 api->[lock](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141)(dev);

445 ret = api->[set\_address](structudc__api.md#a2e8b88743ab56144a199b3ad0618755f)(dev, addr);

446 api->[unlock](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201)(dev);

447

448 return ret;

449}

450

[ 466](group__udc__api.md#ga7f575b548833cc1e5109e0d919630b3f)static inline int [udc\_test\_mode](group__udc__api.md#ga7f575b548833cc1e5109e0d919630b3f)(const struct [device](structdevice.md) \*dev,

467 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const bool dryrun)

468{

469 const struct [udc\_api](structudc__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

470 int ret;

471

472 if (![udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)(dev)) {

473 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

474 }

475

476 if (api->[test\_mode](structudc__api.md#ab06839ded48cbc671b2b915fe0010959) != NULL) {

477 api->[lock](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141)(dev);

478 ret = api->[test\_mode](structudc__api.md#ab06839ded48cbc671b2b915fe0010959)(dev, mode, dryrun);

479 api->[unlock](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201)(dev);

480 } else {

481 ret = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

482 }

483

484 return ret;

485}

486

[ 497](group__udc__api.md#ga075edc81fb3e39c2b377fc56c8c0915c)static inline int [udc\_host\_wakeup](group__udc__api.md#ga075edc81fb3e39c2b377fc56c8c0915c)(const struct [device](structdevice.md) \*dev)

498{

499 const struct [udc\_api](structudc__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

500 int ret;

501

502 if (![udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)(dev)) {

503 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

504 }

505

506 api->[lock](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141)(dev);

507 ret = api->[host\_wakeup](structudc__api.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb)(dev);

508 api->[unlock](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201)(dev);

509

510 return ret;

511}

512

[ 534](group__udc__api.md#ga81307ae4ab17ccd86be64bdf1653df0e)int [udc\_ep\_try\_config](group__udc__api.md#ga81307ae4ab17ccd86be64bdf1653df0e)(const struct [device](structdevice.md) \*dev,

535 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep,

536 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes,

537 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const mps,

538 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval);

539

[ 558](group__udc__api.md#gacc4b5c127532c994406df30bacab5684)int [udc\_ep\_enable](group__udc__api.md#gacc4b5c127532c994406df30bacab5684)(const struct [device](structdevice.md) \*dev,

559 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep,

560 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes,

561 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps,

562 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval);

563

[ 578](group__udc__api.md#ga52da2366ac5da1a695caa8826b342cbc)int [udc\_ep\_disable](group__udc__api.md#ga52da2366ac5da1a695caa8826b342cbc)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

579

[ 593](group__udc__api.md#ga19488ec4c93d81592bb5ffccfc1eadc4)int [udc\_ep\_set\_halt](group__udc__api.md#ga19488ec4c93d81592bb5ffccfc1eadc4)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

594

[ 608](group__udc__api.md#gadec9c8af89b28984028fd8e0b1a8c776)int [udc\_ep\_clear\_halt](group__udc__api.md#gadec9c8af89b28984028fd8e0b1a8c776)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

609

[ 625](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d)int [udc\_ep\_enqueue](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf);

626

[ 643](group__udc__api.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)int [udc\_ep\_dequeue](group__udc__api.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

644

[ 656](group__udc__api.md#gad3fb1d64b6e0cf051627011ce673bb1e)struct [net\_buf](structnet__buf.md) \*[udc\_ep\_buf\_alloc](group__udc__api.md#gad3fb1d64b6e0cf051627011ce673bb1e)(const struct [device](structdevice.md) \*dev,

657 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep,

658 const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

659

[ 670](group__udc__api.md#gaedd615defad234b001e74448f89488e1)int [udc\_ep\_buf\_free](group__udc__api.md#gaedd615defad234b001e74448f89488e1)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf);

671

[ 679](group__udc__api.md#ga50f6bde28b6a5fcab6b685107570e081)static inline void [udc\_ep\_buf\_set\_zlp](group__udc__api.md#ga50f6bde28b6a5fcab6b685107570e081)(struct [net\_buf](structnet__buf.md) \*const buf)

680{

681 struct [udc\_buf\_info](structudc__buf__info.md) \*bi;

682

683 \_\_ASSERT\_NO\_MSG(buf);

684 bi = (struct [udc\_buf\_info](structudc__buf__info.md) \*)[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(buf);

685 if ([USB\_EP\_DIR\_IS\_IN](usb__ch9_8h.md#a495d790dfb00609ce029631f40d0a422)(bi->[ep](structudc__buf__info.md#a0a1c09f587d3f6847cb7ce77514a3321))) {

686 bi->[zlp](structudc__buf__info.md#afc2d0c391aca7f68a1ae5539a1fed8a0) = 1;

687 }

688}

689

[ 697](group__udc__api.md#ga073a51222ac639d3c70af7b57970b42a)static inline struct [udc\_buf\_info](structudc__buf__info.md) \*[udc\_get\_buf\_info](group__udc__api.md#ga073a51222ac639d3c70af7b57970b42a)(const struct [net\_buf](structnet__buf.md) \*const buf)

698{

699 \_\_ASSERT\_NO\_MSG(buf);

700 return (struct [udc\_buf\_info](structudc__buf__info.md) \*)[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(buf);

701}

702

706

707#endif /\* ZEPHYR\_INCLUDE\_UDC\_H \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically test a bit.

**Definition** atomic.h:127

[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)

static void \* net\_buf\_user\_data(const struct net\_buf \*buf)

Get a pointer to the user data of a buffer.

**Definition** buf.h:1465

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3)

#define EPERM

Not owner.

**Definition** errno.h:40

[udc\_get\_buf\_info](group__udc__api.md#ga073a51222ac639d3c70af7b57970b42a)

static struct udc\_buf\_info \* udc\_get\_buf\_info(const struct net\_buf \*const buf)

Get requests metadata.

**Definition** udc.h:697

[udc\_host\_wakeup](group__udc__api.md#ga075edc81fb3e39c2b377fc56c8c0915c)

static int udc\_host\_wakeup(const struct device \*dev)

Initiate host wakeup procedure.

**Definition** udc.h:497

[udc\_ep\_set\_halt](group__udc__api.md#ga19488ec4c93d81592bb5ffccfc1eadc4)

int udc\_ep\_set\_halt(const struct device \*dev, const uint8\_t ep)

Halt endpoint.

[udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f)

static bool udc\_is\_enabled(const struct device \*dev)

Checks whether the controller is enabled.

**Definition** udc.h:318

[udc\_caps](group__udc__api.md#ga3ee738bad8e1ee3928d32f57f82bef70)

static struct udc\_device\_caps udc\_caps(const struct device \*dev)

Get USB device controller capabilities.

**Definition** udc.h:405

[udc\_is\_initialized](group__udc__api.md#ga40e50cf79b40d3792513e8fea3347f59)

static bool udc\_is\_initialized(const struct device \*dev)

Checks whether the controller is initialized.

**Definition** udc.h:304

[udc\_ep\_buf\_set\_zlp](group__udc__api.md#ga50f6bde28b6a5fcab6b685107570e081)

static void udc\_ep\_buf\_set\_zlp(struct net\_buf \*const buf)

Set ZLP flag in requests metadata.

**Definition** udc.h:679

[udc\_ep\_disable](group__udc__api.md#ga52da2366ac5da1a695caa8826b342cbc)

int udc\_ep\_disable(const struct device \*dev, const uint8\_t ep)

Disable endpoint.

[udc\_shutdown](group__udc__api.md#ga59a92eb60575ca80d205cc29b4fb4f21)

int udc\_shutdown(const struct device \*dev)

Poweroff USB device controller.

[udc\_ep\_dequeue](group__udc__api.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)

int udc\_ep\_dequeue(const struct device \*dev, const uint8\_t ep)

Remove all USB device controller requests from endpoint queue.

[udc\_set\_address](group__udc__api.md#ga6feb32a2263307bdde9acc63d3c2ebb1)

static int udc\_set\_address(const struct device \*dev, const uint8\_t addr)

Set USB device address.

**Definition** udc.h:435

[udc\_test\_mode](group__udc__api.md#ga7f575b548833cc1e5109e0d919630b3f)

static int udc\_test\_mode(const struct device \*dev, const uint8\_t mode, const bool dryrun)

Enable Test Mode.

**Definition** udc.h:466

[udc\_ep\_try\_config](group__udc__api.md#ga81307ae4ab17ccd86be64bdf1653df0e)

int udc\_ep\_try\_config(const struct device \*dev, const uint8\_t ep, const uint8\_t attributes, uint16\_t \*const mps, const uint8\_t interval)

Try an endpoint configuration.

[udc\_is\_suspended](group__udc__api.md#ga88786eda763fce5c2a51521650ccc9f4)

static bool udc\_is\_suspended(const struct device \*dev)

Checks whether the controller is suspended.

**Definition** udc.h:332

[udc\_disable](group__udc__api.md#gaa7c2eaa52bdbe1d763b2961124570e8a)

int udc\_disable(const struct device \*dev)

Disable USB device controller.

[udc\_init](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c)

int udc\_init(const struct device \*dev, udc\_event\_cb\_t event\_cb)

Initialize USB device controller.

[udc\_device\_speed](group__udc__api.md#gab936f04015b0fee584756bcdf40d2f50)

enum udc\_bus\_speed udc\_device\_speed(const struct device \*dev)

Get actual USB device speed.

[udc\_ep\_enqueue](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d)

int udc\_ep\_enqueue(const struct device \*dev, struct net\_buf \*const buf)

Queue USB device controller request.

[udc\_ep\_enable](group__udc__api.md#gacc4b5c127532c994406df30bacab5684)

int udc\_ep\_enable(const struct device \*dev, const uint8\_t ep, const uint8\_t attributes, const uint16\_t mps, const uint8\_t interval)

Configure and enable endpoint.

[udc\_ep\_buf\_alloc](group__udc__api.md#gad3fb1d64b6e0cf051627011ce673bb1e)

struct net\_buf \* udc\_ep\_buf\_alloc(const struct device \*dev, const uint8\_t ep, const size\_t size)

Allocate UDC request buffer.

[udc\_ep\_clear\_halt](group__udc__api.md#gadec9c8af89b28984028fd8e0b1a8c776)

int udc\_ep\_clear\_halt(const struct device \*dev, const uint8\_t ep)

Clear endpoint halt.

[udc\_ep\_buf\_free](group__udc__api.md#gaedd615defad234b001e74448f89488e1)

int udc\_ep\_buf\_free(const struct device \*dev, struct net\_buf \*const buf)

Free UDC request buffer.

[udc\_enable](group__udc__api.md#gafbb0dec089f83fd674bd19670a882c65)

int udc\_enable(const struct device \*dev)

Enable USB device controller.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[buf.h](net_2buf_8h.md)

Buffer management.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** buf.h:942

[udc\_api](structudc__api.md)

UDC driver API This is the mandatory API any USB device controller driver needs to expose with except...

**Definition** udc.h:222

[udc\_api::init](structudc__api.md#a01f803a2d258072df102b831cf184b27)

int(\* init)(const struct device \*dev)

**Definition** udc.h:246

[udc\_api::ep\_dequeue](structudc__api.md#a023fcfa0fa251dcadcb379347fe7531a)

int(\* ep\_dequeue)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:227

[udc\_api::ep\_disable](structudc__api.md#a1af05b484e9c9d1f2a0dbfb822f09c98)

int(\* ep\_disable)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:237

[udc\_api::unlock](structudc__api.md#a2029ee9db16e15e2b609c3199b00e201)

int(\* unlock)(const struct device \*dev)

**Definition** udc.h:249

[udc\_api::ep\_enable](structudc__api.md#a27291ab4d2acda207f6a6a2313d50793)

int(\* ep\_enable)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:235

[udc\_api::set\_address](structudc__api.md#a2e8b88743ab56144a199b3ad0618755f)

int(\* set\_address)(const struct device \*dev, const uint8\_t addr)

**Definition** udc.h:240

[udc\_api::ep\_try\_config](structudc__api.md#a775a18f5555f1c518762ff7dc016559c)

int(\* ep\_try\_config)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:233

[udc\_api::disable](structudc__api.md#a8997bba956d264463b71aae0b1a4e3dc)

int(\* disable)(const struct device \*dev)

**Definition** udc.h:245

[udc\_api::ep\_clear\_halt](structudc__api.md#a923a684868721d0b7232c86eed15e121)

int(\* ep\_clear\_halt)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:231

[udc\_api::ep\_enqueue](structudc__api.md#aa1d3dadf63cb156ce5346712e1c65069)

int(\* ep\_enqueue)(const struct device \*dev, struct udc\_ep\_config \*const cfg, struct net\_buf \*const buf)

**Definition** udc.h:224

[udc\_api::test\_mode](structudc__api.md#ab06839ded48cbc671b2b915fe0010959)

int(\* test\_mode)(const struct device \*dev, const uint8\_t mode, const bool dryrun)

**Definition** udc.h:242

[udc\_api::lock](structudc__api.md#ad33ad060c97aa7e5896fdc5e33a3e141)

int(\* lock)(const struct device \*dev)

**Definition** udc.h:248

[udc\_api::shutdown](structudc__api.md#ad7135abf78eb372730dddbba7dc6a75d)

int(\* shutdown)(const struct device \*dev)

**Definition** udc.h:247

[udc\_api::ep\_set\_halt](structudc__api.md#adf2adaea90b53999d1e98756062a2050)

int(\* ep\_set\_halt)(const struct device \*dev, struct udc\_ep\_config \*const cfg)

**Definition** udc.h:229

[udc\_api::device\_speed](structudc__api.md#adf2b8f76158d7bd2d3918628c8a9fc22)

enum udc\_bus\_speed(\* device\_speed)(const struct device \*dev)

**Definition** udc.h:223

[udc\_api::host\_wakeup](structudc__api.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb)

int(\* host\_wakeup)(const struct device \*dev)

**Definition** udc.h:239

[udc\_api::enable](structudc__api.md#af8b916f6b8c211ad82ddcfdaa12de5ae)

int(\* enable)(const struct device \*dev)

**Definition** udc.h:244

[udc\_buf\_info](structudc__buf__info.md)

UDC endpoint buffer info.

**Definition** udc.h:179

[udc\_buf\_info::ep](structudc__buf__info.md#a0a1c09f587d3f6847cb7ce77514a3321)

uint8\_t ep

Endpoint to which request is associated.

**Definition** udc.h:181

[udc\_buf\_info::owner](structudc__buf__info.md#a33e927f23d227a4974915c65927284ec)

void \* owner

Transfer owner (usually pointer to a class instance).

**Definition** udc.h:195

[udc\_buf\_info::queued](structudc__buf__info.md#a4cd2e83000a0551d126bebe89552eab9)

unsigned int queued

Flag marks request buffer is queued (TBD).

**Definition** udc.h:193

[udc\_buf\_info::status](structudc__buf__info.md#a84cf74496eddc4a69a47d23dcdbf753f)

unsigned int status

Flag marks status stage of setup transfer.

**Definition** udc.h:187

[udc\_buf\_info::setup](structudc__buf__info.md#a9664e1f7cddd36dbc7d206b52da45170)

unsigned int setup

Flag marks setup transfer.

**Definition** udc.h:183

[udc\_buf\_info::claimed](structudc__buf__info.md#a9b03b6dd8418d4200733a612aac73daa)

unsigned int claimed

Flag marks request buffer claimed by the controller (TBD).

**Definition** udc.h:191

[udc\_buf\_info::data](structudc__buf__info.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2)

unsigned int data

Flag marks data stage of setup transfer.

**Definition** udc.h:185

[udc\_buf\_info::err](structudc__buf__info.md#af1c92f1cdd6e0474a19f788140fdc573)

int err

Transfer result, 0 on success, other values on error.

**Definition** udc.h:197

[udc\_buf\_info::zlp](structudc__buf__info.md#afc2d0c391aca7f68a1ae5539a1fed8a0)

unsigned int zlp

Flag marks ZLP at the end of a transfer.

**Definition** udc.h:189

[udc\_data](structudc__data.md)

Common UDC driver data structure.

**Definition** udc.h:271

[udc\_data::mutex](structudc__data.md#a1ba1b93af26bca4f4554a43a65ab3c2a)

struct k\_mutex mutex

Driver access mutex.

**Definition** udc.h:277

[udc\_data::setup](structudc__data.md#a1bbb7a70a14368efc4b933a7d1945fb5)

struct net\_buf \* setup

Pointer to buffer containing setup packet.

**Definition** udc.h:285

[udc\_data::event\_cb](structudc__data.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381)

udc\_event\_cb\_t event\_cb

Callback to submit an UDC event to upper layer.

**Definition** udc.h:279

[udc\_data::status](structudc__data.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f)

atomic\_t status

USB device controller status.

**Definition** udc.h:281

[udc\_data::caps](structudc__data.md#aae68bfba2e92894851c36dd40c33c0f0)

struct udc\_device\_caps caps

Controller capabilities.

**Definition** udc.h:275

[udc\_data::stage](structudc__data.md#ab957eea73de90379642ed56ddbb84989)

int stage

Internal used Control Sequence Stage.

**Definition** udc.h:283

[udc\_data::priv](structudc__data.md#ac58682fa2f37bf2034a69cc9b6b10dfb)

void \* priv

Driver private data.

**Definition** udc.h:287

[udc\_data::ep\_lut](structudc__data.md#acc471b34bb24453377b1ae54d33fa415)

struct udc\_ep\_config \* ep\_lut[32]

LUT for endpoint management.

**Definition** udc.h:273

[udc\_device\_caps](structudc__device__caps.md)

USB device controller capabilities.

**Definition** udc.h:36

[udc\_device\_caps::out\_ack](structudc__device__caps.md#a0adada5003bccfbd6df8329198639dc0)

uint32\_t out\_ack

Controller performs status OUT stage automatically.

**Definition** udc.h:42

[udc\_device\_caps::mps0](structudc__device__caps.md#a63affa3fe08cbaec8351297ad9d26911)

enum udc\_mps0 mps0

Maximum packet size for control endpoint.

**Definition** udc.h:46

[udc\_device\_caps::rwup](structudc__device__caps.md#aab85e74e40876040c3d2f961c36b9780)

uint32\_t rwup

Controller supports USB remote wakeup.

**Definition** udc.h:40

[udc\_device\_caps::hs](structudc__device__caps.md#aea376ff4a0c5a27c3b8f7d4416e17b5b)

uint32\_t hs

USB high speed capable controller.

**Definition** udc.h:38

[udc\_device\_caps::addr\_before\_status](structudc__device__caps.md#aefef262532e3eab3baa90eb8e79f9dc8)

uint32\_t addr\_before\_status

Controller expects device address to be set before status stage.

**Definition** udc.h:44

[udc\_ep\_caps](structudc__ep__caps.md)

USB device controller endpoint capabilities.

**Definition** udc.h:66

[udc\_ep\_caps::iso](structudc__ep__caps.md#a15ce10028e09b3af021a83dc36eba99a)

uint32\_t iso

ISO transfer capable endpoint.

**Definition** udc.h:76

[udc\_ep\_caps::in](structudc__ep__caps.md#a3a944cda429c916b60cff3a332b970a7)

uint32\_t in

IN transfer capable endpoint.

**Definition** udc.h:78

[udc\_ep\_caps::mps](structudc__ep__caps.md#a5e90d1362855dd77a1f7ef9e0cd82ef8)

uint32\_t mps

Maximum packet size of the endpoint buffer.

**Definition** udc.h:68

[udc\_ep\_caps::bulk](structudc__ep__caps.md#a73ec7e7c7fd043065a7c59c89c6cc36e)

uint32\_t bulk

Bulk transfer capable endpoint.

**Definition** udc.h:74

[udc\_ep\_caps::interrupt](structudc__ep__caps.md#a73f06f9e2af5770cab84d2adb76d42de)

uint32\_t interrupt

Interrupt transfer capable endpoint.

**Definition** udc.h:72

[udc\_ep\_caps::control](structudc__ep__caps.md#a98afb85c03ff01ba82d55884cea0ea31)

uint32\_t control

Control transfer capable endpoint (for completeness).

**Definition** udc.h:70

[udc\_ep\_caps::out](structudc__ep__caps.md#afc424ee2bb31c19451facc0b79bb73c7)

uint32\_t out

OUT transfer capable endpoint.

**Definition** udc.h:80

[udc\_ep\_config](structudc__ep__config.md)

USB device controller endpoint configuration.

**Definition** udc.h:106

[udc\_ep\_config::interval](structudc__ep__config.md#a1f2afc2d5e512229688764e1b7cd0171)

uint8\_t interval

Polling interval.

**Definition** udc.h:120

[udc\_ep\_config::caps](structudc__ep__config.md#a706987205ac971574d1b81bf72d03248)

struct udc\_ep\_caps caps

Endpoint capabilities.

**Definition** udc.h:110

[udc\_ep\_config::fifo](structudc__ep__config.md#aa62ff3f308771d51563df88439570918)

struct k\_fifo fifo

Endpoint requests FIFO.

**Definition** udc.h:108

[udc\_ep\_config::addr](structudc__ep__config.md#ac795b839cbd426d233a1f91d10d5fc7e)

uint8\_t addr

Endpoint address.

**Definition** udc.h:114

[udc\_ep\_config::attributes](structudc__ep__config.md#acbeab755d1b03da0c58f43aff5bd7d00)

uint8\_t attributes

Endpoint attributes.

**Definition** udc.h:116

[udc\_ep\_config::stat](structudc__ep__config.md#ad42f77d1a9d65239cdb142209050e38e)

struct udc\_ep\_stat stat

Endpoint status.

**Definition** udc.h:112

[udc\_ep\_config::mps](structudc__ep__config.md#ae4f75e52d1c822f5d873095a761c6b48)

uint16\_t mps

Maximum packet size.

**Definition** udc.h:118

[udc\_ep\_stat](structudc__ep__stat.md)

USB device controller endpoint status.

**Definition** udc.h:86

[udc\_ep\_stat::odd](structudc__ep__stat.md#a0a437fb1e4b9a79eea7e4c6b0316c450)

uint32\_t odd

If double buffering is supported, last used buffer is odd.

**Definition** udc.h:94

[udc\_ep\_stat::data1](structudc__ep__stat.md#a30b66675236f30c75837c446b87ced91)

uint32\_t data1

Last submitted PID is DATA1.

**Definition** udc.h:92

[udc\_ep\_stat::enabled](structudc__ep__stat.md#a448c82eb3884dba20e1bdf0980d3a2b3)

uint32\_t enabled

Endpoint is enabled.

**Definition** udc.h:88

[udc\_ep\_stat::busy](structudc__ep__stat.md#ad515a667ffd705408617dd28700db1e9)

uint32\_t busy

Endpoint is busy.

**Definition** udc.h:96

[udc\_ep\_stat::halted](structudc__ep__stat.md#af245db473a046885e4f97b00493718e2)

uint32\_t halted

Endpoint is halted (returning STALL PID).

**Definition** udc.h:90

[udc\_event](structudc__event.md)

USB device controller event.

**Definition** udc.h:157

[udc\_event::status](structudc__event.md#a0707d65716a4b1e6dd3132a0bb370770)

int status

Event status value, if any.

**Definition** udc.h:164

[udc\_event::type](structudc__event.md#a3acfe5d21d16f6edfa24e9964b636434)

enum udc\_event\_type type

Event type.

**Definition** udc.h:159

[udc\_event::dev](structudc__event.md#a900404c46850d34cd7121eeedc2fce9d)

const struct device \* dev

Pointer to device struct.

**Definition** udc.h:169

[udc\_event::buf](structudc__event.md#ac1ff3bc9d629eb9b6c55602e7861e945)

struct net\_buf \* buf

Pointer to request used only for UDC\_EVT\_EP\_REQUEST.

**Definition** udc.h:166

[udc\_event::value](structudc__event.md#ada24e0e920c39bc60a6c7fbbe54277f4)

uint32\_t value

Event value.

**Definition** udc.h:162

[udc\_event\_type](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040)

udc\_event\_type

USB device controller event types.

**Definition** udc.h:127

[UDC\_EVT\_VBUS\_READY](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d)

@ UDC\_EVT\_VBUS\_READY

VBUS ready event.

**Definition** udc.h:129

[UDC\_EVT\_RESUME](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332)

@ UDC\_EVT\_RESUME

Device resume event.

**Definition** udc.h:133

[UDC\_EVT\_SUSPEND](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f)

@ UDC\_EVT\_SUSPEND

Device suspended event.

**Definition** udc.h:135

[UDC\_EVT\_VBUS\_REMOVED](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432)

@ UDC\_EVT\_VBUS\_REMOVED

VBUS removed event.

**Definition** udc.h:131

[UDC\_EVT\_EP\_REQUEST](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b)

@ UDC\_EVT\_EP\_REQUEST

Endpoint request result event.

**Definition** udc.h:141

[UDC\_EVT\_ERROR](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d)

@ UDC\_EVT\_ERROR

Non-correctable error event, requires attention from higher levels or application.

**Definition** udc.h:146

[UDC\_EVT\_RESET](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb)

@ UDC\_EVT\_RESET

Port reset detected.

**Definition** udc.h:137

[UDC\_EVT\_SOF](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78)

@ UDC\_EVT\_SOF

Start of Frame event.

**Definition** udc.h:139

[udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b)

udc\_bus\_speed

USB device actual speed.

**Definition** udc.h:52

[UDC\_BUS\_SPEED\_SS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a)

@ UDC\_BUS\_SPEED\_SS

Device is connected to a super speed bus.

**Definition** udc.h:60

[UDC\_BUS\_SPEED\_FS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5)

@ UDC\_BUS\_SPEED\_FS

Device is connected to a full speed bus.

**Definition** udc.h:56

[UDC\_BUS\_UNKNOWN](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d)

@ UDC\_BUS\_UNKNOWN

Device is probably not connected.

**Definition** udc.h:54

[UDC\_BUS\_SPEED\_HS](udc_8h.md#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599)

@ UDC\_BUS\_SPEED\_HS

Device is connected to a high speed bus.

**Definition** udc.h:58

[UDC\_STATUS\_INITIALIZED](udc_8h.md#a8c96946734085924e2afc591ac502551)

#define UDC\_STATUS\_INITIALIZED

Controller is initialized by udc\_init() and can generate the VBUS events, if capable,...

**Definition** udc.h:256

[udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a)

int(\* udc\_event\_cb\_t)(const struct device \*dev, const struct udc\_event \*const event)

Callback to submit UDC event to higher layer.

**Definition** udc.h:213

[udc\_mps0](udc_8h.md#ac254f8a970f890d14e35c43474c915fd)

udc\_mps0

Maximum packet size of control endpoint supported by the controller.

**Definition** udc.h:24

[UDC\_MPS0\_32](udc_8h.md#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7)

@ UDC\_MPS0\_32

**Definition** udc.h:27

[UDC\_MPS0\_16](udc_8h.md#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a)

@ UDC\_MPS0\_16

**Definition** udc.h:26

[UDC\_MPS0\_64](udc_8h.md#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a)

@ UDC\_MPS0\_64

**Definition** udc.h:28

[UDC\_MPS0\_8](udc_8h.md#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb)

@ UDC\_MPS0\_8

**Definition** udc.h:25

[UDC\_STATUS\_SUSPENDED](udc_8h.md#ac3a36aa8cb3aab95d7931cb602631c36)

#define UDC\_STATUS\_SUSPENDED

Controller is suspended by the host.

**Definition** udc.h:263

[UDC\_STATUS\_ENABLED](udc_8h.md#ad10596af54465c3cb10cc59ae9a507d2)

#define UDC\_STATUS\_ENABLED

Controller is enabled and all API functions are available, controller is recognizable by host.

**Definition** udc.h:261

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

[USB\_EP\_DIR\_IS\_IN](usb__ch9_8h.md#a495d790dfb00609ce029631f40d0a422)

#define USB\_EP\_DIR\_IS\_IN(ep)

True if the endpoint is an IN endpoint.

**Definition** usb\_ch9.h:298

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [udc.h](udc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
