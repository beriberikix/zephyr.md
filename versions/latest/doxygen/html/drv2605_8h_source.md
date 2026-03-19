---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drv2605_8h_source.html
original_path: doxygen/html/drv2605_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

drv2605.h

[Go to the documentation of this file.](drv2605_8h.md)

1/\*

2 \* Copyright (c) 2024 Cirrus Logic, Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_HAPTICS\_DRV2605\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_HAPTICS\_DRV2605\_H\_

8

9#include <[zephyr/drivers/haptics.h](haptics_8h.md)>

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

[ 12](drv2605_8h.md#ab9069fcfd891cadbe5838d0caac5bca0)#define DRV2605\_WAVEFORM\_SEQUENCER\_MAX 8

13

[ 14](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16)enum [drv2605\_library](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16) {

[ 15](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aad90f2d8bdee21c390c4344bd808d345) [DRV2605\_LIBRARY\_EMPTY](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aad90f2d8bdee21c390c4344bd808d345) = 0,

[ 16](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3babadb779b635c80d88fbd5eeb1dd7a) [DRV2605\_LIBRARY\_TS2200\_A](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3babadb779b635c80d88fbd5eeb1dd7a),

[ 17](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a368575d421fedc421e0540393cc27845) [DRV2605\_LIBRARY\_TS2200\_B](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a368575d421fedc421e0540393cc27845),

[ 18](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a53c2477779bae577572c1d38ccffbcf1) [DRV2605\_LIBRARY\_TS2200\_C](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a53c2477779bae577572c1d38ccffbcf1),

[ 19](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa2df9656713c03702620e945de72de56) [DRV2605\_LIBRARY\_TS2200\_D](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa2df9656713c03702620e945de72de56),

[ 20](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa3656aebd793e203c0b986abb7846f64) [DRV2605\_LIBRARY\_TS2200\_E](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa3656aebd793e203c0b986abb7846f64),

[ 21](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3f114d1e1095105c5db786e9aa2dff60) [DRV2605\_LIBRARY\_LRA](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3f114d1e1095105c5db786e9aa2dff60),

22};

23

[ 24](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02a)enum [drv2605\_mode](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02a) {

[ 25](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaab537e7781201365d04f1b61ca1293b5) [DRV2605\_MODE\_INTERNAL\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaab537e7781201365d04f1b61ca1293b5) = 0,

[ 26](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaeb3d84bd67bd5ffa36cd11628d051fb9) [DRV2605\_MODE\_EXTERNAL\_EDGE\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaeb3d84bd67bd5ffa36cd11628d051fb9),

[ 27](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa8303fe0cf8044350d6be89eb0865b254) [DRV2605\_MODE\_EXTERNAL\_LEVEL\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa8303fe0cf8044350d6be89eb0865b254),

[ 28](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa62b722c2507a7f9160f775631894cc2f) [DRV2605\_MODE\_PWM\_ANALOG\_INPUT](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa62b722c2507a7f9160f775631894cc2f),

[ 29](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aafca2555c87c8b63e417e5353f24b2c24) [DRV2605\_MODE\_AUDIO\_TO\_VIBE](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aafca2555c87c8b63e417e5353f24b2c24),

[ 30](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaf9d11ca9fce86e99cad74b77a2089d9a) [DRV2605\_MODE\_RTP](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaf9d11ca9fce86e99cad74b77a2089d9a),

[ 31](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa3c980005d0daee97567fa5e35d8a2836) [DRV2605\_MODE\_DIAGNOSTICS](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa3c980005d0daee97567fa5e35d8a2836),

[ 32](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aadcfb6eb9e12238478bf23fb76423f248) [DRV2605\_MODE\_AUTO\_CAL](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aadcfb6eb9e12238478bf23fb76423f248),

33};

34

[ 38](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639c)enum [drv2605\_haptics\_source](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639c) {

[ 40](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca38623b24d3ca65f42e8ab09ad2764d5d) [DRV2605\_HAPTICS\_SOURCE\_ROM](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca38623b24d3ca65f42e8ab09ad2764d5d),

[ 42](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca51dd1dcc3db5a89efd31a9f72c7db43a) [DRV2605\_HAPTICS\_SOURCE\_RTP](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca51dd1dcc3db5a89efd31a9f72c7db43a),

[ 44](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca3903c6a4404288eaa77a8d365cfc344a) [DRV2605\_HAPTICS\_SOURCE\_AUDIO](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca3903c6a4404288eaa77a8d365cfc344a),

[ 46](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639caa30841998fe2092cdf959153291e0d08) [DRV2605\_HAPTICS\_SOURCE\_PWM](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639caa30841998fe2092cdf959153291e0d08),

[ 48](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca84df3211177d36ab92cd44fde7bb1b1a) [DRV2605\_HAPTICS\_SOURCE\_ANALOG](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca84df3211177d36ab92cd44fde7bb1b1a),

49};

50

[ 51](structdrv2605__rom__data.md)struct [drv2605\_rom\_data](structdrv2605__rom__data.md) {

[ 52](structdrv2605__rom__data.md#a6a0a1208315a415b05384367c8e4eacf) enum [drv2605\_mode](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02a) [trigger](structdrv2605__rom__data.md#a6a0a1208315a415b05384367c8e4eacf);

[ 53](structdrv2605__rom__data.md#aed0ccb13c7f8bf4388d77437e14d15fb) enum [drv2605\_library](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16) [library](structdrv2605__rom__data.md#aed0ccb13c7f8bf4388d77437e14d15fb);

[ 54](structdrv2605__rom__data.md#a06f0e0017c1595fa65978c6fdbce6904) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seq\_regs](structdrv2605__rom__data.md#a06f0e0017c1595fa65978c6fdbce6904)[[DRV2605\_WAVEFORM\_SEQUENCER\_MAX](drv2605_8h.md#ab9069fcfd891cadbe5838d0caac5bca0)];

[ 55](structdrv2605__rom__data.md#a30f72132bcb2e5e028c64476b7cf6a24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [overdrive\_time](structdrv2605__rom__data.md#a30f72132bcb2e5e028c64476b7cf6a24);

[ 56](structdrv2605__rom__data.md#afb9a2a3cd3a6fa107e72cb49ae043f19) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sustain\_pos\_time](structdrv2605__rom__data.md#afb9a2a3cd3a6fa107e72cb49ae043f19);

[ 57](structdrv2605__rom__data.md#a9212ba2b4704bd754ab7bc2a7161549f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sustain\_neg\_time](structdrv2605__rom__data.md#a9212ba2b4704bd754ab7bc2a7161549f);

[ 58](structdrv2605__rom__data.md#ab9a8d1f4c7d0f390aad49fc5f2d607d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [brake\_time](structdrv2605__rom__data.md#ab9a8d1f4c7d0f390aad49fc5f2d607d9);

59};

60

[ 61](structdrv2605__rtp__data.md)struct [drv2605\_rtp\_data](structdrv2605__rtp__data.md) {

[ 62](structdrv2605__rtp__data.md#aa9025d92cc16f39d15042b9b41209c0c) size\_t [size](structdrv2605__rtp__data.md#aa9025d92cc16f39d15042b9b41209c0c);

[ 63](structdrv2605__rtp__data.md#a928e62ef97eccfc70d2c777ad58c98f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[rtp\_hold\_us](structdrv2605__rtp__data.md#a928e62ef97eccfc70d2c777ad58c98f0);

[ 64](structdrv2605__rtp__data.md#a358f8d7119dbcc42f0b42f41f307c237) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rtp\_input](structdrv2605__rtp__data.md#a358f8d7119dbcc42f0b42f41f307c237);

65};

66

[ 67](uniondrv2605__config__data.md)union [drv2605\_config\_data](uniondrv2605__config__data.md) {

[ 68](uniondrv2605__config__data.md#a5ce02bc581a432bc04eec84e00bbc342) struct [drv2605\_rom\_data](structdrv2605__rom__data.md) \*[rom\_data](uniondrv2605__config__data.md#a5ce02bc581a432bc04eec84e00bbc342);

[ 69](uniondrv2605__config__data.md#a7be34001008f23458c72b3b537f6c0bd) struct [drv2605\_rtp\_data](structdrv2605__rtp__data.md) \*[rtp\_data](uniondrv2605__config__data.md#a7be34001008f23458c72b3b537f6c0bd);

70};

71

[ 83](drv2605_8h.md#afe7decc53e258a7162b44ae2076c10d1)int [drv2605\_haptic\_config](drv2605_8h.md#afe7decc53e258a7162b44ae2076c10d1)(const struct [device](structdevice.md) \*dev, enum [drv2605\_haptics\_source](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639c) source,

84 const union [drv2605\_config\_data](uniondrv2605__config__data.md) \*config\_data);

85

86#endif

[drv2605\_mode](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02a)

drv2605\_mode

**Definition** drv2605.h:24

[DRV2605\_MODE\_DIAGNOSTICS](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa3c980005d0daee97567fa5e35d8a2836)

@ DRV2605\_MODE\_DIAGNOSTICS

**Definition** drv2605.h:31

[DRV2605\_MODE\_PWM\_ANALOG\_INPUT](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa62b722c2507a7f9160f775631894cc2f)

@ DRV2605\_MODE\_PWM\_ANALOG\_INPUT

**Definition** drv2605.h:28

[DRV2605\_MODE\_EXTERNAL\_LEVEL\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aa8303fe0cf8044350d6be89eb0865b254)

@ DRV2605\_MODE\_EXTERNAL\_LEVEL\_TRIGGER

**Definition** drv2605.h:27

[DRV2605\_MODE\_INTERNAL\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaab537e7781201365d04f1b61ca1293b5)

@ DRV2605\_MODE\_INTERNAL\_TRIGGER

**Definition** drv2605.h:25

[DRV2605\_MODE\_AUTO\_CAL](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aadcfb6eb9e12238478bf23fb76423f248)

@ DRV2605\_MODE\_AUTO\_CAL

**Definition** drv2605.h:32

[DRV2605\_MODE\_EXTERNAL\_EDGE\_TRIGGER](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaeb3d84bd67bd5ffa36cd11628d051fb9)

@ DRV2605\_MODE\_EXTERNAL\_EDGE\_TRIGGER

**Definition** drv2605.h:26

[DRV2605\_MODE\_RTP](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aaf9d11ca9fce86e99cad74b77a2089d9a)

@ DRV2605\_MODE\_RTP

**Definition** drv2605.h:30

[DRV2605\_MODE\_AUDIO\_TO\_VIBE](drv2605_8h.md#a01ec80a028b1101fbdf3e624800ca02aafca2555c87c8b63e417e5353f24b2c24)

@ DRV2605\_MODE\_AUDIO\_TO\_VIBE

**Definition** drv2605.h:29

[DRV2605\_WAVEFORM\_SEQUENCER\_MAX](drv2605_8h.md#ab9069fcfd891cadbe5838d0caac5bca0)

#define DRV2605\_WAVEFORM\_SEQUENCER\_MAX

**Definition** drv2605.h:12

[drv2605\_library](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16)

drv2605\_library

**Definition** drv2605.h:14

[DRV2605\_LIBRARY\_TS2200\_B](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a368575d421fedc421e0540393cc27845)

@ DRV2605\_LIBRARY\_TS2200\_B

**Definition** drv2605.h:17

[DRV2605\_LIBRARY\_TS2200\_A](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3babadb779b635c80d88fbd5eeb1dd7a)

@ DRV2605\_LIBRARY\_TS2200\_A

**Definition** drv2605.h:16

[DRV2605\_LIBRARY\_LRA](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a3f114d1e1095105c5db786e9aa2dff60)

@ DRV2605\_LIBRARY\_LRA

**Definition** drv2605.h:21

[DRV2605\_LIBRARY\_TS2200\_C](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16a53c2477779bae577572c1d38ccffbcf1)

@ DRV2605\_LIBRARY\_TS2200\_C

**Definition** drv2605.h:18

[DRV2605\_LIBRARY\_TS2200\_D](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa2df9656713c03702620e945de72de56)

@ DRV2605\_LIBRARY\_TS2200\_D

**Definition** drv2605.h:19

[DRV2605\_LIBRARY\_TS2200\_E](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aa3656aebd793e203c0b986abb7846f64)

@ DRV2605\_LIBRARY\_TS2200\_E

**Definition** drv2605.h:20

[DRV2605\_LIBRARY\_EMPTY](drv2605_8h.md#ad8242facf545ff18b81f0703bcf6bb16aad90f2d8bdee21c390c4344bd808d345)

@ DRV2605\_LIBRARY\_EMPTY

**Definition** drv2605.h:15

[drv2605\_haptics\_source](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639c)

drv2605\_haptics\_source

DRV2605 haptic driver signal sources.

**Definition** drv2605.h:38

[DRV2605\_HAPTICS\_SOURCE\_ROM](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca38623b24d3ca65f42e8ab09ad2764d5d)

@ DRV2605\_HAPTICS\_SOURCE\_ROM

The playback source is device ROM.

**Definition** drv2605.h:40

[DRV2605\_HAPTICS\_SOURCE\_AUDIO](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca3903c6a4404288eaa77a8d365cfc344a)

@ DRV2605\_HAPTICS\_SOURCE\_AUDIO

The playback source is audio.

**Definition** drv2605.h:44

[DRV2605\_HAPTICS\_SOURCE\_RTP](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca51dd1dcc3db5a89efd31a9f72c7db43a)

@ DRV2605\_HAPTICS\_SOURCE\_RTP

The playback source is the RTP buffer.

**Definition** drv2605.h:42

[DRV2605\_HAPTICS\_SOURCE\_ANALOG](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639ca84df3211177d36ab92cd44fde7bb1b1a)

@ DRV2605\_HAPTICS\_SOURCE\_ANALOG

The playback source is an analog signal.

**Definition** drv2605.h:48

[DRV2605\_HAPTICS\_SOURCE\_PWM](drv2605_8h.md#ae98fe02355253b7d8f4583a36919639caa30841998fe2092cdf959153291e0d08)

@ DRV2605\_HAPTICS\_SOURCE\_PWM

The playback source is a PWM signal.

**Definition** drv2605.h:46

[drv2605\_haptic\_config](drv2605_8h.md#afe7decc53e258a7162b44ae2076c10d1)

int drv2605\_haptic\_config(const struct device \*dev, enum drv2605\_haptics\_source source, const union drv2605\_config\_data \*config\_data)

Configure the DRV2605 device for a particular signal source.

[haptics.h](haptics_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[drv2605\_rom\_data](structdrv2605__rom__data.md)

**Definition** drv2605.h:51

[drv2605\_rom\_data::seq\_regs](structdrv2605__rom__data.md#a06f0e0017c1595fa65978c6fdbce6904)

uint8\_t seq\_regs[8]

**Definition** drv2605.h:54

[drv2605\_rom\_data::overdrive\_time](structdrv2605__rom__data.md#a30f72132bcb2e5e028c64476b7cf6a24)

uint8\_t overdrive\_time

**Definition** drv2605.h:55

[drv2605\_rom\_data::trigger](structdrv2605__rom__data.md#a6a0a1208315a415b05384367c8e4eacf)

enum drv2605\_mode trigger

**Definition** drv2605.h:52

[drv2605\_rom\_data::sustain\_neg\_time](structdrv2605__rom__data.md#a9212ba2b4704bd754ab7bc2a7161549f)

uint8\_t sustain\_neg\_time

**Definition** drv2605.h:57

[drv2605\_rom\_data::brake\_time](structdrv2605__rom__data.md#ab9a8d1f4c7d0f390aad49fc5f2d607d9)

uint8\_t brake\_time

**Definition** drv2605.h:58

[drv2605\_rom\_data::library](structdrv2605__rom__data.md#aed0ccb13c7f8bf4388d77437e14d15fb)

enum drv2605\_library library

**Definition** drv2605.h:53

[drv2605\_rom\_data::sustain\_pos\_time](structdrv2605__rom__data.md#afb9a2a3cd3a6fa107e72cb49ae043f19)

uint8\_t sustain\_pos\_time

**Definition** drv2605.h:56

[drv2605\_rtp\_data](structdrv2605__rtp__data.md)

**Definition** drv2605.h:61

[drv2605\_rtp\_data::rtp\_input](structdrv2605__rtp__data.md#a358f8d7119dbcc42f0b42f41f307c237)

uint8\_t \* rtp\_input

**Definition** drv2605.h:64

[drv2605\_rtp\_data::rtp\_hold\_us](structdrv2605__rtp__data.md#a928e62ef97eccfc70d2c777ad58c98f0)

uint32\_t \* rtp\_hold\_us

**Definition** drv2605.h:63

[drv2605\_rtp\_data::size](structdrv2605__rtp__data.md#aa9025d92cc16f39d15042b9b41209c0c)

size\_t size

**Definition** drv2605.h:62

[drv2605\_config\_data](uniondrv2605__config__data.md)

**Definition** drv2605.h:67

[drv2605\_config\_data::rom\_data](uniondrv2605__config__data.md#a5ce02bc581a432bc04eec84e00bbc342)

struct drv2605\_rom\_data \* rom\_data

**Definition** drv2605.h:68

[drv2605\_config\_data::rtp\_data](uniondrv2605__config__data.md#a7be34001008f23458c72b3b537f6c0bd)

struct drv2605\_rtp\_data \* rtp\_data

**Definition** drv2605.h:69

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [haptics](dir_774527316cd59357de8be7eb369b9f4a.md)
- [drv2605.h](drv2605_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
