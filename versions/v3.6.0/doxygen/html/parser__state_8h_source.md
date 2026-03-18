---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/parser__state_8h_source.html
original_path: doxygen/html/parser__state_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser\_state.h

[Go to the documentation of this file.](parser__state_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\* Copyright Joyent, Inc. and other Node contributors. All rights reserved.

4 \*

5 \* Permission is hereby granted, free of charge, to any person obtaining a copy

6 \* of this software and associated documentation files (the "Software"), to

7 \* deal in the Software without restriction, including without limitation the

8 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

9 \* sell copies of the Software, and to permit persons to whom the Software is

10 \* furnished to do so, subject to the following conditions:

11 \*

12 \* The above copyright notice and this permission notice shall be included in

13 \* all copies or substantial portions of the Software.

14 \*

15 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

16 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

17 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

18 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

19 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

20 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS

21 \* IN THE SOFTWARE.

22 \*/

23#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_STATE\_H\_

24#define ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_STATE\_H\_

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 29](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) {

[ 30](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08) [s\_dead](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08) = 1, /\* important that this is > 0 \*/

[ 31](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e) [s\_start\_req\_or\_res](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e),

[ 32](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be) [s\_res\_or\_resp\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be),

[ 33](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8) [s\_start\_res](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8),

[ 34](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4) [s\_res\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4),

[ 35](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e) [s\_res\_HT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e),

[ 36](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85) [s\_res\_HTT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85),

[ 37](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7) [s\_res\_HTTP](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7),

[ 38](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c) [s\_res\_first\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c),

[ 39](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6) [s\_res\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6),

[ 40](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a) [s\_res\_first\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a),

[ 41](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8) [s\_res\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8),

[ 42](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a) [s\_res\_first\_status\_code](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a),

[ 43](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15) [s\_res\_status\_code](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15),

[ 44](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21) [s\_res\_status\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21),

[ 45](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c) [s\_res\_status](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c),

[ 46](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b) [s\_res\_line\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b),

[ 47](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b) [s\_start\_req](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b),

[ 48](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443) [s\_req\_method](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443),

[ 49](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8) [s\_req\_spaces\_before\_url](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8),

[ 50](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea) [s\_req\_schema](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea),

[ 51](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759) [s\_req\_schema\_slash](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759),

[ 52](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d) [s\_req\_schema\_slash\_slash](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d),

[ 53](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c) [s\_req\_server\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c),

[ 54](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf) [s\_req\_server](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf),

[ 55](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26) [s\_req\_server\_with\_at](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26),

[ 56](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe) [s\_req\_path](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe),

[ 57](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809) [s\_req\_query\_string\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809),

[ 58](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef) [s\_req\_query\_string](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef),

[ 59](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d) [s\_req\_fragment\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d),

[ 60](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1) [s\_req\_fragment](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1),

[ 61](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f) [s\_req\_http\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f),

[ 62](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7) [s\_req\_http\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7),

[ 63](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7) [s\_req\_http\_HT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7),

[ 64](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907) [s\_req\_http\_HTT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907),

[ 65](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3) [s\_req\_http\_HTTP](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3),

[ 66](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6) [s\_req\_first\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6),

[ 67](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6) [s\_req\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6),

[ 68](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d) [s\_req\_first\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d),

[ 69](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872) [s\_req\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872),

[ 70](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb) [s\_req\_line\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb),

[ 71](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769) [s\_header\_field\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769),

[ 72](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1) [s\_header\_field](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1),

[ 73](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec) [s\_header\_value\_discard\_ws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec),

[ 74](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d) [s\_header\_value\_discard\_ws\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d),

[ 75](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b) [s\_header\_value\_discard\_lws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b),

[ 76](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0) [s\_header\_value\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0),

[ 77](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69) [s\_header\_value](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69),

[ 78](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d) [s\_header\_value\_lws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d),

[ 79](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435) [s\_header\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435),

[ 80](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409) [s\_chunk\_size\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409),

[ 81](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad) [s\_chunk\_size](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad),

[ 82](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a) [s\_chunk\_parameters](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a),

[ 83](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20) [s\_chunk\_size\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20),

[ 84](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe) [s\_headers\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe),

[ 85](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390) [s\_headers\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390),

86 /\* Important: 's\_headers\_done' must be the last 'header' state. All

87 \* states beyond this must be 'body' states. It is used for overflow

88 \* checking. See the PARSING\_HEADER() macro.

89 \*/

[ 90](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2) [s\_chunk\_data](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2),

[ 91](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0) [s\_chunk\_data\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0),

[ 92](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64) [s\_chunk\_data\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64),

[ 93](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95) [s\_body\_identity](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95),

[ 94](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73) [s\_body\_identity\_eof](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73),

[ 95](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774) [s\_message\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774)

96};

97

98#ifdef \_\_cplusplus

99}

100#endif

101#endif

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[s\_body\_identity](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95)

@ s\_body\_identity

**Definition** parser\_state.h:93

[s\_req\_server\_with\_at](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26)

@ s\_req\_server\_with\_at

**Definition** parser\_state.h:55

[s\_header\_value\_discard\_ws\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d)

@ s\_header\_value\_discard\_ws\_almost\_done

**Definition** parser\_state.h:74

[s\_chunk\_data\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64)

@ s\_chunk\_data\_done

**Definition** parser\_state.h:92

[s\_chunk\_size\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20)

@ s\_chunk\_size\_almost\_done

**Definition** parser\_state.h:83

[s\_start\_res](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8)

@ s\_start\_res

**Definition** parser\_state.h:33

[s\_body\_identity\_eof](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73)

@ s\_body\_identity\_eof

**Definition** parser\_state.h:94

[s\_chunk\_data](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2)

@ s\_chunk\_data

**Definition** parser\_state.h:90

[s\_res\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4)

@ s\_res\_H

**Definition** parser\_state.h:34

[s\_headers\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390)

@ s\_headers\_done

**Definition** parser\_state.h:85

[s\_res\_first\_status\_code](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a)

@ s\_res\_first\_status\_code

**Definition** parser\_state.h:42

[s\_res\_first\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a)

@ s\_res\_first\_http\_minor

**Definition** parser\_state.h:40

[s\_header\_value\_discard\_lws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b)

@ s\_header\_value\_discard\_lws

**Definition** parser\_state.h:75

[s\_res\_status](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c)

@ s\_res\_status

**Definition** parser\_state.h:45

[s\_header\_field](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1)

@ s\_header\_field

**Definition** parser\_state.h:72

[s\_req\_query\_string](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef)

@ s\_req\_query\_string

**Definition** parser\_state.h:58

[s\_req\_query\_string\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809)

@ s\_req\_query\_string\_start

**Definition** parser\_state.h:57

[s\_res\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6)

@ s\_res\_http\_major

**Definition** parser\_state.h:39

[s\_req\_spaces\_before\_url](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8)

@ s\_req\_spaces\_before\_url

**Definition** parser\_state.h:49

[s\_header\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435)

@ s\_header\_almost\_done

**Definition** parser\_state.h:79

[s\_req\_path](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe)

@ s\_req\_path

**Definition** parser\_state.h:56

[s\_res\_HTTP](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7)

@ s\_res\_HTTP

**Definition** parser\_state.h:37

[s\_header\_value](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69)

@ s\_header\_value

**Definition** parser\_state.h:77

[s\_start\_req\_or\_res](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e)

@ s\_start\_req\_or\_res

**Definition** parser\_state.h:31

[s\_req\_method](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443)

@ s\_req\_method

**Definition** parser\_state.h:48

[s\_chunk\_size](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad)

@ s\_chunk\_size

**Definition** parser\_state.h:81

[s\_req\_http\_HTTP](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3)

@ s\_req\_http\_HTTP

**Definition** parser\_state.h:65

[s\_req\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872)

@ s\_req\_http\_minor

**Definition** parser\_state.h:69

[s\_req\_server](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf)

@ s\_req\_server

**Definition** parser\_state.h:54

[s\_chunk\_parameters](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a)

@ s\_chunk\_parameters

**Definition** parser\_state.h:82

[s\_start\_req](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b)

@ s\_start\_req

**Definition** parser\_state.h:47

[s\_res\_first\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c)

@ s\_res\_first\_http\_major

**Definition** parser\_state.h:38

[s\_res\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8)

@ s\_res\_http\_minor

**Definition** parser\_state.h:41

[s\_req\_schema](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea)

@ s\_req\_schema

**Definition** parser\_state.h:50

[s\_req\_http\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7)

@ s\_req\_http\_H

**Definition** parser\_state.h:62

[s\_req\_schema\_slash\_slash](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d)

@ s\_req\_schema\_slash\_slash

**Definition** parser\_state.h:52

[s\_header\_field\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769)

@ s\_header\_field\_start

**Definition** parser\_state.h:71

[s\_req\_first\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6)

@ s\_req\_first\_http\_major

**Definition** parser\_state.h:66

[s\_res\_line\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b)

@ s\_res\_line\_almost\_done

**Definition** parser\_state.h:46

[s\_header\_value\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0)

@ s\_header\_value\_start

**Definition** parser\_state.h:76

[s\_res\_HTT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85)

@ s\_res\_HTT

**Definition** parser\_state.h:36

[s\_req\_http\_major](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6)

@ s\_req\_http\_major

**Definition** parser\_state.h:67

[s\_header\_value\_lws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d)

@ s\_header\_value\_lws

**Definition** parser\_state.h:78

[s\_req\_line\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb)

@ s\_req\_line\_almost\_done

**Definition** parser\_state.h:70

[s\_headers\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe)

@ s\_headers\_almost\_done

**Definition** parser\_state.h:84

[s\_req\_fragment](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1)

@ s\_req\_fragment

**Definition** parser\_state.h:60

[s\_req\_schema\_slash](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759)

@ s\_req\_schema\_slash

**Definition** parser\_state.h:51

[s\_res\_or\_resp\_H](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be)

@ s\_res\_or\_resp\_H

**Definition** parser\_state.h:32

[s\_req\_fragment\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d)

@ s\_req\_fragment\_start

**Definition** parser\_state.h:59

[s\_req\_http\_HT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7)

@ s\_req\_http\_HT

**Definition** parser\_state.h:63

[s\_header\_value\_discard\_ws](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec)

@ s\_header\_value\_discard\_ws

**Definition** parser\_state.h:73

[s\_message\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774)

@ s\_message\_done

**Definition** parser\_state.h:95

[s\_dead](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08)

@ s\_dead

**Definition** parser\_state.h:30

[s\_req\_http\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f)

@ s\_req\_http\_start

**Definition** parser\_state.h:61

[s\_req\_http\_HTT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907)

@ s\_req\_http\_HTT

**Definition** parser\_state.h:64

[s\_res\_HT](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e)

@ s\_res\_HT

**Definition** parser\_state.h:35

[s\_res\_status\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21)

@ s\_res\_status\_start

**Definition** parser\_state.h:44

[s\_res\_status\_code](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15)

@ s\_res\_status\_code

**Definition** parser\_state.h:43

[s\_req\_first\_http\_minor](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d)

@ s\_req\_first\_http\_minor

**Definition** parser\_state.h:68

[s\_chunk\_size\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409)

@ s\_chunk\_size\_start

**Definition** parser\_state.h:80

[s\_req\_server\_start](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c)

@ s\_req\_server\_start

**Definition** parser\_state.h:53

[s\_chunk\_data\_almost\_done](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0)

@ s\_chunk\_data\_almost\_done

**Definition** parser\_state.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser\_state.h](parser__state_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
