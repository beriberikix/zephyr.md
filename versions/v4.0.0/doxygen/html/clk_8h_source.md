---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clk_8h_source.html
original_path: doxygen/html/clk_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clk.h

[Go to the documentation of this file.](clk_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CLK\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CLK\_H\_

14

15#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h.md)>

16

[ 17](clk_8h.md#a8b14e6d0d7329cb53c57ec21d241c3de)#define SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK GENMASK(1, 0)

[ 18](clk_8h.md#af797af4466ae90d17a58527f53d698ce)#define SCMI\_CLK\_CONFIG\_ENABLE\_DISABLE(x)\

19 ((uint32\_t)(x) & SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK)

20

[ 21](clk_8h.md#a9c2b446e167d9d5a903c55e4644d85ed)#define SCMI\_CLK\_ATTRIBUTES\_CLK\_NUM(x) ((x) & GENMASK(15, 0))

22

[ 29](structscmi__clock__config.md)struct [scmi\_clock\_config](structscmi__clock__config.md) {

[ 30](structscmi__clock__config.md#a1f4acfb41d1b75448f96acad6cfd3498) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_id](structscmi__clock__config.md#a1f4acfb41d1b75448f96acad6cfd3498);

[ 31](structscmi__clock__config.md#ae21186dde1af79f55bdce325d08cdc06) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attributes](structscmi__clock__config.md#ae21186dde1af79f55bdce325d08cdc06);

[ 32](structscmi__clock__config.md#ae180ad04a48558130e26a268ec444297) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [extended\_cfg\_val](structscmi__clock__config.md#ae180ad04a48558130e26a268ec444297);

33};

34

[ 38](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1e)enum [scmi\_clock\_message](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1e) {

[ 39](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaca2f0a8361ee5dc916124025f6526607) [SCMI\_CLK\_MSG\_PROTOCOL\_VERSION](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaca2f0a8361ee5dc916124025f6526607) = 0x0,

[ 40](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea408af2dc0a8c4dca018bbf2631b7a516) [SCMI\_CLK\_MSG\_PROTOCOL\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea408af2dc0a8c4dca018bbf2631b7a516) = 0x1,

[ 41](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eafbadc52b702794b36a42e033f7ddfc42) [SCMI\_CLK\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eafbadc52b702794b36a42e033f7ddfc42) = 0x2,

[ 42](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea4e3d5c2fdf920e72621b9bd20217d1c2) [SCMI\_CLK\_MSG\_CLOCK\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea4e3d5c2fdf920e72621b9bd20217d1c2) = 0x3,

[ 43](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea6551cd48e112cb0b839be88734865390) [SCMI\_CLK\_MSG\_CLOCK\_DESCRIBE\_RATES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea6551cd48e112cb0b839be88734865390) = 0x4,

[ 44](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8b57e5ba159084a0f4567ef57666dda6) [SCMI\_CLK\_MSG\_CLOCK\_RATE\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8b57e5ba159084a0f4567ef57666dda6) = 0x5,

[ 45](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8ec4db9ccd6aea715001a41fcef20cd9) [SCMI\_CLK\_MSG\_CLOCK\_RATE\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8ec4db9ccd6aea715001a41fcef20cd9) = 0x6,

[ 46](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea97cc819e6d0a8ef184c137c1400ae059) [SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea97cc819e6d0a8ef184c137c1400ae059) = 0x7,

[ 47](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea0146f7bab4392d882f7b362976c78488) [SCMI\_CLK\_MSG\_CLOCK\_NAME\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea0146f7bab4392d882f7b362976c78488) = 0x8,

[ 48](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaadac9b02cf7136a3de2deb4139f8b891) [SCMI\_CLK\_MSG\_CLOCK\_RATE\_NOTIFY](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaadac9b02cf7136a3de2deb4139f8b891) = 0x9,

[ 49](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea2eaf16c90fcaf03d087ed2226c24f382) [SCMI\_CLK\_MSG\_CLOCK\_RATE\_CHANGE\_REQUESTED\_NOTIFY](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea2eaf16c90fcaf03d087ed2226c24f382) = 0xa,

[ 50](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea255aabcc89b96395c6e0db65054c7ee4) [SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea255aabcc89b96395c6e0db65054c7ee4) = 0xb,

[ 51](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea895901f8e1ba97f961107ab21124df22) [SCMI\_CLK\_MSG\_CLOCK\_POSSIBLE\_PARENTS\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea895901f8e1ba97f961107ab21124df22) = 0xc,

[ 52](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eae5eedf089ea7fc08b49fd6a3086e79a9) [SCMI\_CLK\_MSG\_CLOCK\_PARENT\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eae5eedf089ea7fc08b49fd6a3086e79a9) = 0xd,

[ 53](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaaa3979a8e0ad76b674f1bd02ee6ccfab) [SCMI\_CLK\_MSG\_CLOCK\_PARENT\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaaa3979a8e0ad76b674f1bd02ee6ccfab) = 0xe,

[ 54](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaf1de9a844e0d6ab5e840757d1f069957) [SCMI\_CLK\_MSG\_CLOCK\_GET\_PERMISSIONS](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaf1de9a844e0d6ab5e840757d1f069957) = 0xf,

[ 55](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea76ddf68387ac3dd18a014b20d5139495) [SCMI\_CLK\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea76ddf68387ac3dd18a014b20d5139495) = 0x10,

56};

57

[ 68](clk_8h.md#ab4dd6c5aba4beea5e73679bbe96244cc)int [scmi\_clock\_protocol\_attributes](clk_8h.md#ab4dd6c5aba4beea5e73679bbe96244cc)(struct [scmi\_protocol](structscmi__protocol.md) \*proto,

69 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*attributes);

70

[ 81](clk_8h.md#ac9fe7f4275895fd9e6a7eada26012efb)int [scmi\_clock\_config\_set](clk_8h.md#ac9fe7f4275895fd9e6a7eada26012efb)(struct [scmi\_protocol](structscmi__protocol.md) \*proto,

82 struct [scmi\_clock\_config](structscmi__clock__config.md) \*cfg);

[ 93](clk_8h.md#ac69cff69cef158aebf5b40ba2c3c7bb4)int [scmi\_clock\_rate\_get](clk_8h.md#ac69cff69cef158aebf5b40ba2c3c7bb4)(struct [scmi\_protocol](structscmi__protocol.md) \*proto,

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clk\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

95

96#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CLK\_H\_ \*/

[scmi\_clock\_message](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1e)

scmi\_clock\_message

Clock protocol command message IDs.

**Definition** clk.h:38

[SCMI\_CLK\_MSG\_CLOCK\_NAME\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea0146f7bab4392d882f7b362976c78488)

@ SCMI\_CLK\_MSG\_CLOCK\_NAME\_GET

**Definition** clk.h:47

[SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea255aabcc89b96395c6e0db65054c7ee4)

@ SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_GET

**Definition** clk.h:50

[SCMI\_CLK\_MSG\_CLOCK\_RATE\_CHANGE\_REQUESTED\_NOTIFY](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea2eaf16c90fcaf03d087ed2226c24f382)

@ SCMI\_CLK\_MSG\_CLOCK\_RATE\_CHANGE\_REQUESTED\_NOTIFY

**Definition** clk.h:49

[SCMI\_CLK\_MSG\_PROTOCOL\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea408af2dc0a8c4dca018bbf2631b7a516)

@ SCMI\_CLK\_MSG\_PROTOCOL\_ATTRIBUTES

**Definition** clk.h:40

[SCMI\_CLK\_MSG\_CLOCK\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea4e3d5c2fdf920e72621b9bd20217d1c2)

@ SCMI\_CLK\_MSG\_CLOCK\_ATTRIBUTES

**Definition** clk.h:42

[SCMI\_CLK\_MSG\_CLOCK\_DESCRIBE\_RATES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea6551cd48e112cb0b839be88734865390)

@ SCMI\_CLK\_MSG\_CLOCK\_DESCRIBE\_RATES

**Definition** clk.h:43

[SCMI\_CLK\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea76ddf68387ac3dd18a014b20d5139495)

@ SCMI\_CLK\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION

**Definition** clk.h:55

[SCMI\_CLK\_MSG\_CLOCK\_POSSIBLE\_PARENTS\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea895901f8e1ba97f961107ab21124df22)

@ SCMI\_CLK\_MSG\_CLOCK\_POSSIBLE\_PARENTS\_GET

**Definition** clk.h:51

[SCMI\_CLK\_MSG\_CLOCK\_RATE\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8b57e5ba159084a0f4567ef57666dda6)

@ SCMI\_CLK\_MSG\_CLOCK\_RATE\_SET

**Definition** clk.h:44

[SCMI\_CLK\_MSG\_CLOCK\_RATE\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea8ec4db9ccd6aea715001a41fcef20cd9)

@ SCMI\_CLK\_MSG\_CLOCK\_RATE\_GET

**Definition** clk.h:45

[SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1ea97cc819e6d0a8ef184c137c1400ae059)

@ SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_SET

**Definition** clk.h:46

[SCMI\_CLK\_MSG\_CLOCK\_PARENT\_GET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaaa3979a8e0ad76b674f1bd02ee6ccfab)

@ SCMI\_CLK\_MSG\_CLOCK\_PARENT\_GET

**Definition** clk.h:53

[SCMI\_CLK\_MSG\_CLOCK\_RATE\_NOTIFY](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaadac9b02cf7136a3de2deb4139f8b891)

@ SCMI\_CLK\_MSG\_CLOCK\_RATE\_NOTIFY

**Definition** clk.h:48

[SCMI\_CLK\_MSG\_PROTOCOL\_VERSION](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaca2f0a8361ee5dc916124025f6526607)

@ SCMI\_CLK\_MSG\_PROTOCOL\_VERSION

**Definition** clk.h:39

[SCMI\_CLK\_MSG\_CLOCK\_PARENT\_SET](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eae5eedf089ea7fc08b49fd6a3086e79a9)

@ SCMI\_CLK\_MSG\_CLOCK\_PARENT\_SET

**Definition** clk.h:52

[SCMI\_CLK\_MSG\_CLOCK\_GET\_PERMISSIONS](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eaf1de9a844e0d6ab5e840757d1f069957)

@ SCMI\_CLK\_MSG\_CLOCK\_GET\_PERMISSIONS

**Definition** clk.h:54

[SCMI\_CLK\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](clk_8h.md#a1f469b4773ddd8bcf07c9dc5c1319c1eafbadc52b702794b36a42e033f7ddfc42)

@ SCMI\_CLK\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES

**Definition** clk.h:41

[scmi\_clock\_protocol\_attributes](clk_8h.md#ab4dd6c5aba4beea5e73679bbe96244cc)

int scmi\_clock\_protocol\_attributes(struct scmi\_protocol \*proto, uint32\_t \*attributes)

Send the PROTOCOL\_ATTRIBUTES command and get its reply.

[scmi\_clock\_rate\_get](clk_8h.md#ac69cff69cef158aebf5b40ba2c3c7bb4)

int scmi\_clock\_rate\_get(struct scmi\_protocol \*proto, uint32\_t clk\_id, uint32\_t \*rate)

Query the rate of a clock.

[scmi\_clock\_config\_set](clk_8h.md#ac9fe7f4275895fd9e6a7eada26012efb)

int scmi\_clock\_config\_set(struct scmi\_protocol \*proto, struct scmi\_clock\_config \*cfg)

Send the CLOCK\_CONFIG\_SET command and get its reply.

[protocol.h](protocol_8h.md)

SCMI protocol generic functions and structures.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[scmi\_clock\_config](structscmi__clock__config.md)

Describes the parameters for the CLOCK\_CONFIG\_SET command.

**Definition** clk.h:29

[scmi\_clock\_config::clk\_id](structscmi__clock__config.md#a1f4acfb41d1b75448f96acad6cfd3498)

uint32\_t clk\_id

**Definition** clk.h:30

[scmi\_clock\_config::extended\_cfg\_val](structscmi__clock__config.md#ae180ad04a48558130e26a268ec444297)

uint32\_t extended\_cfg\_val

**Definition** clk.h:32

[scmi\_clock\_config::attributes](structscmi__clock__config.md#ae21186dde1af79f55bdce325d08cdc06)

uint32\_t attributes

**Definition** clk.h:31

[scmi\_protocol](structscmi__protocol.md)

SCMI protocol structure.

**Definition** protocol.h:74

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [clk.h](clk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
