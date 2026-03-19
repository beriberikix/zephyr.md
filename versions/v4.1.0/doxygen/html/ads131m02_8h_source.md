---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ads131m02_8h_source.html
original_path: doxygen/html/ads131m02_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads131m02.h

[Go to the documentation of this file.](ads131m02_8h.md)

1/\*

2 \* Copyright (c) 2024 Linumiz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS131M02\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS131M02\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

[ 12](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723)enum [ads131m02\_adc\_mode](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723) {

[ 13](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723ac536b7369f6a00a2405a267439dbab29) [ADS131M02\_CONTINUOUS\_MODE](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723ac536b7369f6a00a2405a267439dbab29), /\* Continuous conversion mode \*/

[ 14](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723aefc260abb9c9ce184fbb7216e6e45de2) [ADS131M02\_GLOBAL\_CHOP\_MODE](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723aefc260abb9c9ce184fbb7216e6e45de2) /\* Global chop mode \*/

15};

16

[ 17](ads131m02_8h.md#adce793d507c5962362d9bd85818a886c)enum [ads131m02\_adc\_power\_mode](ads131m02_8h.md#adce793d507c5962362d9bd85818a886c) {

[ 18](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca5a881112e5b695ab55dfacb0b6879b2a) [ADS131M02\_VLP](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca5a881112e5b695ab55dfacb0b6879b2a), /\* Very Low Power \*/

[ 19](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca687e531cdc9b9f08fdaf6c47f9450c82) [ADS131M02\_LP](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca687e531cdc9b9f08fdaf6c47f9450c82), /\* Low Power \*/

[ 20](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca2146287eb5fbda0079c280bc1a9f6a36) [ADS131M02\_HR](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca2146287eb5fbda0079c280bc1a9f6a36) /\* High Resolution \*/

21};

22

[ 23](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7d)enum [ads131m02\_gc\_delay](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7d) {

[ 24](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daccd3c64901e9aaa30a4461e5044de21a) [ADS131M02\_GC\_DELAY\_2](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daccd3c64901e9aaa30a4461e5044de21a),

[ 25](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6cfa9898f4d8803890f715548785796c) [ADS131M02\_GC\_DELAY\_4](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6cfa9898f4d8803890f715548785796c),

[ 26](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb9ee92fc3d77e41754f822fe4ec0cb6) [ADS131M02\_GC\_DELAY\_8](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb9ee92fc3d77e41754f822fe4ec0cb6),

[ 27](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dacae711ef11e3e2668dd9b64343185ab5) [ADS131M02\_GC\_DELAY\_16](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dacae711ef11e3e2668dd9b64343185ab5),

[ 28](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab18deb65a7e28c5e9827678dc3e13862) [ADS131M02\_GC\_DELAY\_32](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab18deb65a7e28c5e9827678dc3e13862),

[ 29](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da91a6015efb301c998df3ceb631d89fc6) [ADS131M02\_GC\_DELAY\_64](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da91a6015efb301c998df3ceb631d89fc6),

[ 30](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaac93eddc8896d914a48463bb0cf277d) [ADS131M02\_GC\_DELAY\_128](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaac93eddc8896d914a48463bb0cf277d),

[ 31](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da2c4baf74c237423ac584a943fc28c4ff) [ADS131M02\_GC\_DELAY\_256](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da2c4baf74c237423ac584a943fc28c4ff),

[ 32](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da0e7959cebba38878924af4e6e0ec1218) [ADS131M02\_GC\_DELAY\_512](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da0e7959cebba38878924af4e6e0ec1218),

[ 33](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaf8f4e7ed69bd5332efe1acb59e876cf) [ADS131M02\_GC\_DELAY\_1024](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaf8f4e7ed69bd5332efe1acb59e876cf),

[ 34](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb87ba8a9ac1eb5aa12fa2d8907263a1) [ADS131M02\_GC\_DELAY\_2048](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb87ba8a9ac1eb5aa12fa2d8907263a1),

[ 35](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab56b732017be8afa576a5fa517fd04fb) [ADS131M02\_GC\_DELAY\_4096](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab56b732017be8afa576a5fa517fd04fb),

[ 36](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da191c6f08a6ad4bbd4f57ae1b25dbc143) [ADS131M02\_GC\_DELAY\_8192](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da191c6f08a6ad4bbd4f57ae1b25dbc143),

[ 37](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dabe33c4d4fe7bfd00d9d8d8669a085479) [ADS131M02\_GC\_DELAY\_16384](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dabe33c4d4fe7bfd00d9d8d8669a085479),

[ 38](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dafcd84e5cea9262ff99056fe74fa2b62e) [ADS131M02\_GC\_DELAY\_32768](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dafcd84e5cea9262ff99056fe74fa2b62e),

[ 39](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6a006e3a0b8c146d9adb74fd0ba713c0) [ADS131M02\_GC\_DELAY\_65536](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6a006e3a0b8c146d9adb74fd0ba713c0)

40};

41

[ 42](ads131m02_8h.md#a49268275ec5a266225a0a4e39ed9f50f)int [ads131m02\_set\_adc\_mode](ads131m02_8h.md#a49268275ec5a266225a0a4e39ed9f50f)(const struct [device](structdevice.md) \*dev, enum [ads131m02\_adc\_mode](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723) mode,

43 enum [ads131m02\_gc\_delay](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7d) gc\_delay);

44

[ 45](ads131m02_8h.md#a5590a77342f9cec5c68e8fed2e9f1aed)int [ads131m02\_set\_power\_mode](ads131m02_8h.md#a5590a77342f9cec5c68e8fed2e9f1aed)(const struct [device](structdevice.md) \*dev,

46 enum [ads131m02\_adc\_power\_mode](ads131m02_8h.md#adce793d507c5962362d9bd85818a886c) mode);

47

48#endif

[ads131m02\_gc\_delay](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7d)

ads131m02\_gc\_delay

**Definition** ads131m02.h:23

[ADS131M02\_GC\_DELAY\_512](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da0e7959cebba38878924af4e6e0ec1218)

@ ADS131M02\_GC\_DELAY\_512

**Definition** ads131m02.h:32

[ADS131M02\_GC\_DELAY\_8192](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da191c6f08a6ad4bbd4f57ae1b25dbc143)

@ ADS131M02\_GC\_DELAY\_8192

**Definition** ads131m02.h:36

[ADS131M02\_GC\_DELAY\_256](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da2c4baf74c237423ac584a943fc28c4ff)

@ ADS131M02\_GC\_DELAY\_256

**Definition** ads131m02.h:31

[ADS131M02\_GC\_DELAY\_65536](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6a006e3a0b8c146d9adb74fd0ba713c0)

@ ADS131M02\_GC\_DELAY\_65536

**Definition** ads131m02.h:39

[ADS131M02\_GC\_DELAY\_4](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da6cfa9898f4d8803890f715548785796c)

@ ADS131M02\_GC\_DELAY\_4

**Definition** ads131m02.h:25

[ADS131M02\_GC\_DELAY\_64](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7da91a6015efb301c998df3ceb631d89fc6)

@ ADS131M02\_GC\_DELAY\_64

**Definition** ads131m02.h:29

[ADS131M02\_GC\_DELAY\_128](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaac93eddc8896d914a48463bb0cf277d)

@ ADS131M02\_GC\_DELAY\_128

**Definition** ads131m02.h:30

[ADS131M02\_GC\_DELAY\_1024](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daaf8f4e7ed69bd5332efe1acb59e876cf)

@ ADS131M02\_GC\_DELAY\_1024

**Definition** ads131m02.h:33

[ADS131M02\_GC\_DELAY\_32](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab18deb65a7e28c5e9827678dc3e13862)

@ ADS131M02\_GC\_DELAY\_32

**Definition** ads131m02.h:28

[ADS131M02\_GC\_DELAY\_4096](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dab56b732017be8afa576a5fa517fd04fb)

@ ADS131M02\_GC\_DELAY\_4096

**Definition** ads131m02.h:35

[ADS131M02\_GC\_DELAY\_16384](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dabe33c4d4fe7bfd00d9d8d8669a085479)

@ ADS131M02\_GC\_DELAY\_16384

**Definition** ads131m02.h:37

[ADS131M02\_GC\_DELAY\_16](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dacae711ef11e3e2668dd9b64343185ab5)

@ ADS131M02\_GC\_DELAY\_16

**Definition** ads131m02.h:27

[ADS131M02\_GC\_DELAY\_2](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daccd3c64901e9aaa30a4461e5044de21a)

@ ADS131M02\_GC\_DELAY\_2

**Definition** ads131m02.h:24

[ADS131M02\_GC\_DELAY\_2048](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb87ba8a9ac1eb5aa12fa2d8907263a1)

@ ADS131M02\_GC\_DELAY\_2048

**Definition** ads131m02.h:34

[ADS131M02\_GC\_DELAY\_8](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7daeb9ee92fc3d77e41754f822fe4ec0cb6)

@ ADS131M02\_GC\_DELAY\_8

**Definition** ads131m02.h:26

[ADS131M02\_GC\_DELAY\_32768](ads131m02_8h.md#a06f6638f3ba51cbd7ef9028d83cb0d7dafcd84e5cea9262ff99056fe74fa2b62e)

@ ADS131M02\_GC\_DELAY\_32768

**Definition** ads131m02.h:38

[ads131m02\_set\_adc\_mode](ads131m02_8h.md#a49268275ec5a266225a0a4e39ed9f50f)

int ads131m02\_set\_adc\_mode(const struct device \*dev, enum ads131m02\_adc\_mode mode, enum ads131m02\_gc\_delay gc\_delay)

[ads131m02\_set\_power\_mode](ads131m02_8h.md#a5590a77342f9cec5c68e8fed2e9f1aed)

int ads131m02\_set\_power\_mode(const struct device \*dev, enum ads131m02\_adc\_power\_mode mode)

[ads131m02\_adc\_mode](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723)

ads131m02\_adc\_mode

**Definition** ads131m02.h:12

[ADS131M02\_CONTINUOUS\_MODE](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723ac536b7369f6a00a2405a267439dbab29)

@ ADS131M02\_CONTINUOUS\_MODE

**Definition** ads131m02.h:13

[ADS131M02\_GLOBAL\_CHOP\_MODE](ads131m02_8h.md#ad760dc7a7036158af94ced3d9e8c6723aefc260abb9c9ce184fbb7216e6e45de2)

@ ADS131M02\_GLOBAL\_CHOP\_MODE

**Definition** ads131m02.h:14

[ads131m02\_adc\_power\_mode](ads131m02_8h.md#adce793d507c5962362d9bd85818a886c)

ads131m02\_adc\_power\_mode

**Definition** ads131m02.h:17

[ADS131M02\_HR](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca2146287eb5fbda0079c280bc1a9f6a36)

@ ADS131M02\_HR

**Definition** ads131m02.h:20

[ADS131M02\_VLP](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca5a881112e5b695ab55dfacb0b6879b2a)

@ ADS131M02\_VLP

**Definition** ads131m02.h:18

[ADS131M02\_LP](ads131m02_8h.md#adce793d507c5962362d9bd85818a886ca687e531cdc9b9f08fdaf6c47f9450c82)

@ ADS131M02\_LP

**Definition** ads131m02.h:19

[device.h](device_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [ads131m02.h](ads131m02_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
