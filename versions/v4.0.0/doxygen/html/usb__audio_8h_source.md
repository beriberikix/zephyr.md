---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usb__audio_8h_source.html
original_path: doxygen/html/usb__audio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_audio.h

[Go to the documentation of this file.](usb__audio_8h.md)

1/\*

2 \* USB audio class core header

3 \*

4 \* Copyright (c) 2020 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

20

21#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_AUDIO\_H\_

22#define ZEPHYR\_INCLUDE\_USB\_CLASS\_AUDIO\_H\_

23

24#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/net\_buf.h](net__buf_8h.md)>

27#include <[zephyr/sys/util.h](sys_2util_8h.md)>

28

[ 32](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582)enum [usb\_audio\_int\_subclass\_codes](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582) {

[ 33](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2) [USB\_AUDIO\_SUBCLASS\_UNDEFINED](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2) = 0x00,

[ 34](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac) [USB\_AUDIO\_AUDIOCONTROL](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac) = 0x01,

[ 35](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892) [USB\_AUDIO\_AUDIOSTREAMING](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892) = 0x02,

[ 36](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2) [USB\_AUDIO\_MIDISTREAMING](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2) = 0x03

37};

38

[ 42](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9a)enum [usb\_audio\_cs\_ac\_int\_desc\_subtypes](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9a) {

[ 43](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d) [USB\_AUDIO\_AC\_DESCRIPTOR\_UNDEFINED](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d) = 0x00,

[ 44](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51) [USB\_AUDIO\_HEADER](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51) = 0x01,

[ 45](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343) [USB\_AUDIO\_INPUT\_TERMINAL](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343) = 0x02,

[ 46](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f) [USB\_AUDIO\_OUTPUT\_TERMINAL](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f) = 0x03,

[ 47](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe) [USB\_AUDIO\_MIXER\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe) = 0x04,

[ 48](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5) [USB\_AUDIO\_SELECTOR\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5) = 0x05,

[ 49](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7) [USB\_AUDIO\_FEATURE\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7) = 0x06,

[ 50](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab) [USB\_AUDIO\_PROCESSING\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab) = 0x07,

[ 51](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1) [USB\_AUDIO\_EXTENSION\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1) = 0x08

52};

53

[ 57](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeb)enum [usb\_audio\_cs\_as\_int\_desc\_subtypes](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeb) {

[ 58](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e) [USB\_AUDIO\_AS\_DESCRIPTOR\_UNDEFINED](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e) = 0x00,

[ 59](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84) [USB\_AUDIO\_AS\_GENERAL](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84) = 0x01,

[ 60](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4) [USB\_AUDIO\_FORMAT\_TYPE](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4) = 0x02,

[ 61](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a) [USB\_AUDIO\_FORMAT\_SPECIFIC](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a) = 0x03

62};

63

[ 67](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ad)enum [usb\_audio\_cs\_req\_codes](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ad) {

[ 68](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220) [USB\_AUDIO\_REQUEST\_CODE\_UNDEFINED](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220) = 0x00,

[ 69](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d) [USB\_AUDIO\_SET\_CUR](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d) = 0x01,

[ 70](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6) [USB\_AUDIO\_GET\_CUR](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6) = 0x81,

[ 71](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab) [USB\_AUDIO\_SET\_MIN](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab) = 0x02,

[ 72](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6) [USB\_AUDIO\_GET\_MIN](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6) = 0x82,

[ 73](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707) [USB\_AUDIO\_SET\_MAX](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707) = 0x03,

[ 74](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb) [USB\_AUDIO\_GET\_MAX](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb) = 0x83,

[ 75](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7) [USB\_AUDIO\_SET\_RES](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7) = 0x04,

[ 76](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485) [USB\_AUDIO\_GET\_RES](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485) = 0x84,

[ 77](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0) [USB\_AUDIO\_SET\_MEM](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0) = 0x05,

[ 78](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259) [USB\_AUDIO\_GET\_MEM](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259) = 0x85,

[ 79](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109) [USB\_AUDIO\_GET\_STAT](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109) = 0xFF

80};

81

[ 85](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2)enum [usb\_audio\_fucs](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2) {

[ 86](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794) [USB\_AUDIO\_FU\_CONTROL\_UNDEFINED](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794) = 0x00,

[ 87](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d) [USB\_AUDIO\_FU\_MUTE\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d) = 0x01,

[ 88](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8) [USB\_AUDIO\_FU\_VOLUME\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8) = 0x02,

[ 89](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc) [USB\_AUDIO\_FU\_BASS\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc) = 0x03,

[ 90](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601) [USB\_AUDIO\_FU\_MID\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601) = 0x04,

[ 91](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89) [USB\_AUDIO\_FU\_TREBLE\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89) = 0x05,

[ 92](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5) [USB\_AUDIO\_FU\_GRAPHIC\_EQUALIZER\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5) = 0x06,

[ 93](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f) [USB\_AUDIO\_FU\_AUTOMATIC\_GAIN\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f) = 0x07,

[ 94](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da) [USB\_AUDIO\_FU\_DELAY\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da) = 0x08,

[ 95](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3) [USB\_AUDIO\_FU\_BASS\_BOOST\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3) = 0x09,

[ 96](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d) [USB\_AUDIO\_FU\_LOUDNESS\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d) = 0x0A

97};

98

[ 102](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79e)enum [usb\_audio\_terminal\_types](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79e) {

[ 108](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4) [USB\_AUDIO\_USB\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4) = 0x0100,

[ 110](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661) [USB\_AUDIO\_USB\_STREAMING](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661) = 0x0101,

[ 112](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486) [USB\_AUDIO\_USB\_VENDOR\_SPEC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486) = 0x01FF,

114

[ 120](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57) [USB\_AUDIO\_IN\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57) = 0x0200,

[ 122](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d) [USB\_AUDIO\_IN\_MICROPHONE](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d) = 0x0201,

[ 124](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a) [USB\_AUDIO\_IN\_DESKTOP\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a) = 0x0202,

[ 126](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749) [USB\_AUDIO\_IN\_PERSONAL\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749) = 0x0203,

[ 128](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b) [USB\_AUDIO\_IN\_OM\_DIR\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b) = 0x0204,

[ 130](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262) [USB\_AUDIO\_IN\_MIC\_ARRAY](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262) = 0x0205,

[ 132](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86) [USB\_AUDIO\_IN\_PROC\_MIC\_ARRAY](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86) = 0x0205,

134

[ 140](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0) [USB\_AUDIO\_OUT\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0) = 0x0300,

[ 142](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c) [USB\_AUDIO\_OUT\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c) = 0x0301,

[ 144](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9) [USB\_AUDIO\_OUT\_HEADPHONES](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9) = 0x0302,

[ 146](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73) [USB\_AUDIO\_OUT\_HEAD\_AUDIO](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73) = 0x0303,

[ 148](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795) [USB\_AUDIO\_OUT\_DESKTOP\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795) = 0x0304,

[ 150](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213) [USB\_AUDIO\_OUT\_ROOM\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213) = 0x0305,

[ 152](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b) [USB\_AUDIO\_OUT\_COMM\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b) = 0x0306,

[ 154](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480) [USB\_AUDIO\_OUT\_LOW\_FREQ\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480) = 0x0307,

156

[ 162](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8) [USB\_AUDIO\_IO\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8) = 0x0400,

[ 164](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207) [USB\_AUDIO\_IO\_HANDSET](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207) = 0x0401,

[ 166](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e) [USB\_AUDIO\_IO\_HEADSET](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e) = 0x0402,

[ 168](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d) [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_NONE](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d) = 0x0403,

[ 170](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6) [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_SUP](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6) = 0x0404,

[ 172](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14) [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_CAN](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14) = 0x0405,

173};

174

[ 178](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb)enum [usb\_audio\_direction](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb) {

[ 179](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd) [USB\_AUDIO\_IN](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd) = 0x00,

[ 180](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba) [USB\_AUDIO\_OUT](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba) = 0x01

181};

182

[ 189](structusb__audio__fu__evt.md)struct [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md) {

[ 194](structusb__audio__fu__evt.md#a5baf5d4e2a39337dc9c21c4465d5ad8e) enum [usb\_audio\_direction](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb) [dir](structusb__audio__fu__evt.md#a5baf5d4e2a39337dc9c21c4465d5ad8e);

[ 196](structusb__audio__fu__evt.md#a1cb4849aae8b9a4e667ed126e9bce26b) enum [usb\_audio\_fucs](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2) [cs](structusb__audio__fu__evt.md#a1cb4849aae8b9a4e667ed126e9bce26b);

[ 201](structusb__audio__fu__evt.md#a9313b39f178c8a86d680a950ce505713) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structusb__audio__fu__evt.md#a9313b39f178c8a86d680a950ce505713);

[ 203](structusb__audio__fu__evt.md#a6ef19bf7d37c3d636edba243dac8ecb2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [val\_len](structusb__audio__fu__evt.md#a6ef19bf7d37c3d636edba243dac8ecb2);

[ 205](structusb__audio__fu__evt.md#a47c6c7c00fac32a04bffd251d715dc39) const void \*[val](structusb__audio__fu__evt.md#a47c6c7c00fac32a04bffd251d715dc39);

206};

207

[ 219](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8)typedef void (\*[usb\_audio\_data\_request\_cb\_t](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8))(const struct [device](structdevice.md) \*dev);

220

[ 232](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2)typedef void (\*[usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2))(const struct [device](structdevice.md) \*dev,

233 struct [net\_buf](structnet__buf.md) \*buffer,

234 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

235

[ 248](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219)typedef void (\*[usb\_audio\_feature\_updated\_cb\_t](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219))(const struct [device](structdevice.md) \*dev,

249 const struct [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md) \*evt);

250

[ 261](structusb__audio__ops.md)struct [usb\_audio\_ops](structusb__audio__ops.md) {

[ 263](structusb__audio__ops.md#a6ee19a7aef47561f14981b7e7ebd8ac7) [usb\_audio\_data\_request\_cb\_t](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8) [data\_request\_cb](structusb__audio__ops.md#a6ee19a7aef47561f14981b7e7ebd8ac7);

264

[ 269](structusb__audio__ops.md#a2752018597ba5bd4e9a80d1ae650bf8b) [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) [data\_written\_cb](structusb__audio__ops.md#a2752018597ba5bd4e9a80d1ae650bf8b);

270

[ 275](structusb__audio__ops.md#a483af21f54537bef1a6ae3be2cd3717d) [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) [data\_received\_cb](structusb__audio__ops.md#a483af21f54537bef1a6ae3be2cd3717d);

276

[ 278](structusb__audio__ops.md#a861823185efb5c9a06b900799adb9efb) [usb\_audio\_feature\_updated\_cb\_t](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219) [feature\_update\_cb](structusb__audio__ops.md#a861823185efb5c9a06b900799adb9efb);

279};

280

[ 295](usb__audio_8h.md#af314d5beb1d16377855313d46148a86c)size\_t [usb\_audio\_get\_in\_frame\_size](usb__audio_8h.md#af314d5beb1d16377855313d46148a86c)(const struct [device](structdevice.md) \*dev);

296

[ 306](usb__audio_8h.md#a6a69824dadab0c36bb6a6ce378da8ba5)void [usb\_audio\_register](usb__audio_8h.md#a6a69824dadab0c36bb6a6ce378da8ba5)(const struct [device](structdevice.md) \*dev,

307 const struct [usb\_audio\_ops](structusb__audio__ops.md) \*ops);

308

[ 329](usb__audio_8h.md#af1874c929638325e9e2a44da0e613041)int [usb\_audio\_send](usb__audio_8h.md#af1874c929638325e9e2a44da0e613041)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buffer,

330 size\_t len);

331

332#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_AUDIO\_H\_ \*/

[device.h](device_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[usb\_audio\_fu\_evt](structusb__audio__fu__evt.md)

Feature Unit event structure.

**Definition** usb\_audio.h:189

[usb\_audio\_fu\_evt::cs](structusb__audio__fu__evt.md#a1cb4849aae8b9a4e667ed126e9bce26b)

enum usb\_audio\_fucs cs

Control selector feature that has been changed.

**Definition** usb\_audio.h:196

[usb\_audio\_fu\_evt::val](structusb__audio__fu__evt.md#a47c6c7c00fac32a04bffd251d715dc39)

const void \* val

Value of the feature that has been set.

**Definition** usb\_audio.h:205

[usb\_audio\_fu\_evt::dir](structusb__audio__fu__evt.md#a5baf5d4e2a39337dc9c21c4465d5ad8e)

enum usb\_audio\_direction dir

The device direction that has been changed.

**Definition** usb\_audio.h:194

[usb\_audio\_fu\_evt::val\_len](structusb__audio__fu__evt.md#a6ef19bf7d37c3d636edba243dac8ecb2)

uint8\_t val\_len

Length of the val field.

**Definition** usb\_audio.h:203

[usb\_audio\_fu\_evt::channel](structusb__audio__fu__evt.md#a9313b39f178c8a86d680a950ce505713)

uint8\_t channel

Device channel that has been changed.

**Definition** usb\_audio.h:201

[usb\_audio\_ops](structusb__audio__ops.md)

Audio callbacks used to interact with audio devices by user App.

**Definition** usb\_audio.h:261

[usb\_audio\_ops::data\_written\_cb](structusb__audio__ops.md#a2752018597ba5bd4e9a80d1ae650bf8b)

usb\_audio\_data\_completion\_cb\_t data\_written\_cb

Callback called when data were successfully written with sending capable device.

**Definition** usb\_audio.h:269

[usb\_audio\_ops::data\_received\_cb](structusb__audio__ops.md#a483af21f54537bef1a6ae3be2cd3717d)

usb\_audio\_data\_completion\_cb\_t data\_received\_cb

Callback called when data were successfully received by receive capable device.

**Definition** usb\_audio.h:275

[usb\_audio\_ops::data\_request\_cb](structusb__audio__ops.md#a6ee19a7aef47561f14981b7e7ebd8ac7)

usb\_audio\_data\_request\_cb\_t data\_request\_cb

Callback called when data could be send.

**Definition** usb\_audio.h:263

[usb\_audio\_ops::feature\_update\_cb](structusb__audio__ops.md#a861823185efb5c9a06b900799adb9efb)

usb\_audio\_feature\_updated\_cb\_t feature\_update\_cb

Callback called when features were modified by the Host.

**Definition** usb\_audio.h:278

[util.h](sys_2util_8h.md)

Misc utilities.

[usb\_audio\_int\_subclass\_codes](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582)

usb\_audio\_int\_subclass\_codes

Audio Interface Subclass Codes.

**Definition** usb\_audio.h:32

[USB\_AUDIO\_MIDISTREAMING](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2)

@ USB\_AUDIO\_MIDISTREAMING

**Definition** usb\_audio.h:36

[USB\_AUDIO\_AUDIOSTREAMING](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892)

@ USB\_AUDIO\_AUDIOSTREAMING

**Definition** usb\_audio.h:35

[USB\_AUDIO\_AUDIOCONTROL](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac)

@ USB\_AUDIO\_AUDIOCONTROL

**Definition** usb\_audio.h:34

[USB\_AUDIO\_SUBCLASS\_UNDEFINED](usb__audio_8h.md#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2)

@ USB\_AUDIO\_SUBCLASS\_UNDEFINED

**Definition** usb\_audio.h:33

[usb\_audio\_fucs](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2)

usb\_audio\_fucs

Feature Unit Control Selectors Refer to Table A-11 from audio10.pdf.

**Definition** usb\_audio.h:85

[USB\_AUDIO\_FU\_CONTROL\_UNDEFINED](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794)

@ USB\_AUDIO\_FU\_CONTROL\_UNDEFINED

**Definition** usb\_audio.h:86

[USB\_AUDIO\_FU\_BASS\_BOOST\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3)

@ USB\_AUDIO\_FU\_BASS\_BOOST\_CONTROL

**Definition** usb\_audio.h:95

[USB\_AUDIO\_FU\_GRAPHIC\_EQUALIZER\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5)

@ USB\_AUDIO\_FU\_GRAPHIC\_EQUALIZER\_CONTROL

**Definition** usb\_audio.h:92

[USB\_AUDIO\_FU\_BASS\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc)

@ USB\_AUDIO\_FU\_BASS\_CONTROL

**Definition** usb\_audio.h:89

[USB\_AUDIO\_FU\_TREBLE\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89)

@ USB\_AUDIO\_FU\_TREBLE\_CONTROL

**Definition** usb\_audio.h:91

[USB\_AUDIO\_FU\_VOLUME\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8)

@ USB\_AUDIO\_FU\_VOLUME\_CONTROL

**Definition** usb\_audio.h:88

[USB\_AUDIO\_FU\_AUTOMATIC\_GAIN\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f)

@ USB\_AUDIO\_FU\_AUTOMATIC\_GAIN\_CONTROL

**Definition** usb\_audio.h:93

[USB\_AUDIO\_FU\_MID\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601)

@ USB\_AUDIO\_FU\_MID\_CONTROL

**Definition** usb\_audio.h:90

[USB\_AUDIO\_FU\_LOUDNESS\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d)

@ USB\_AUDIO\_FU\_LOUDNESS\_CONTROL

**Definition** usb\_audio.h:96

[USB\_AUDIO\_FU\_MUTE\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d)

@ USB\_AUDIO\_FU\_MUTE\_CONTROL

**Definition** usb\_audio.h:87

[USB\_AUDIO\_FU\_DELAY\_CONTROL](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da)

@ USB\_AUDIO\_FU\_DELAY\_CONTROL

**Definition** usb\_audio.h:94

[usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2)

void(\* usb\_audio\_data\_completion\_cb\_t)(const struct device \*dev, struct net\_buf \*buffer, size\_t size)

Callback type used to inform the app that data were successfully send/received.

**Definition** usb\_audio.h:232

[usb\_audio\_feature\_updated\_cb\_t](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219)

void(\* usb\_audio\_feature\_updated\_cb\_t)(const struct device \*dev, const struct usb\_audio\_fu\_evt \*evt)

Callback type used to inform the app that Host has changed one of the features configured for the dev...

**Definition** usb\_audio.h:248

[usb\_audio\_register](usb__audio_8h.md#a6a69824dadab0c36bb6a6ce378da8ba5)

void usb\_audio\_register(const struct device \*dev, const struct usb\_audio\_ops \*ops)

Register the USB Audio device and make it usable.

[usb\_audio\_data\_request\_cb\_t](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8)

void(\* usb\_audio\_data\_request\_cb\_t)(const struct device \*dev)

Callback type used to inform the app that data were requested from the device and may be send to the ...

**Definition** usb\_audio.h:219

[usb\_audio\_cs\_ac\_int\_desc\_subtypes](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9a)

usb\_audio\_cs\_ac\_int\_desc\_subtypes

Audio Class-Specific AC Interface Descriptor Subtypes.

**Definition** usb\_audio.h:42

[USB\_AUDIO\_MIXER\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe)

@ USB\_AUDIO\_MIXER\_UNIT

**Definition** usb\_audio.h:47

[USB\_AUDIO\_AC\_DESCRIPTOR\_UNDEFINED](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d)

@ USB\_AUDIO\_AC\_DESCRIPTOR\_UNDEFINED

**Definition** usb\_audio.h:43

[USB\_AUDIO\_OUTPUT\_TERMINAL](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f)

@ USB\_AUDIO\_OUTPUT\_TERMINAL

**Definition** usb\_audio.h:46

[USB\_AUDIO\_HEADER](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51)

@ USB\_AUDIO\_HEADER

**Definition** usb\_audio.h:44

[USB\_AUDIO\_INPUT\_TERMINAL](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343)

@ USB\_AUDIO\_INPUT\_TERMINAL

**Definition** usb\_audio.h:45

[USB\_AUDIO\_SELECTOR\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5)

@ USB\_AUDIO\_SELECTOR\_UNIT

**Definition** usb\_audio.h:48

[USB\_AUDIO\_FEATURE\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7)

@ USB\_AUDIO\_FEATURE\_UNIT

**Definition** usb\_audio.h:49

[USB\_AUDIO\_EXTENSION\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1)

@ USB\_AUDIO\_EXTENSION\_UNIT

**Definition** usb\_audio.h:51

[USB\_AUDIO\_PROCESSING\_UNIT](usb__audio_8h.md#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab)

@ USB\_AUDIO\_PROCESSING\_UNIT

**Definition** usb\_audio.h:50

[usb\_audio\_direction](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb)

usb\_audio\_direction

Audio device direction.

**Definition** usb\_audio.h:178

[USB\_AUDIO\_OUT](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba)

@ USB\_AUDIO\_OUT

**Definition** usb\_audio.h:180

[USB\_AUDIO\_IN](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd)

@ USB\_AUDIO\_IN

**Definition** usb\_audio.h:179

[usb\_audio\_cs\_req\_codes](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ad)

usb\_audio\_cs\_req\_codes

Audio Class-Specific Request Codes Refer to Table A-9 from audio10.pdf.

**Definition** usb\_audio.h:67

[USB\_AUDIO\_SET\_CUR](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d)

@ USB\_AUDIO\_SET\_CUR

**Definition** usb\_audio.h:69

[USB\_AUDIO\_SET\_RES](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7)

@ USB\_AUDIO\_SET\_RES

**Definition** usb\_audio.h:75

[USB\_AUDIO\_GET\_STAT](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109)

@ USB\_AUDIO\_GET\_STAT

**Definition** usb\_audio.h:79

[USB\_AUDIO\_GET\_MIN](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6)

@ USB\_AUDIO\_GET\_MIN

**Definition** usb\_audio.h:72

[USB\_AUDIO\_GET\_RES](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485)

@ USB\_AUDIO\_GET\_RES

**Definition** usb\_audio.h:76

[USB\_AUDIO\_GET\_MEM](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259)

@ USB\_AUDIO\_GET\_MEM

**Definition** usb\_audio.h:78

[USB\_AUDIO\_REQUEST\_CODE\_UNDEFINED](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220)

@ USB\_AUDIO\_REQUEST\_CODE\_UNDEFINED

**Definition** usb\_audio.h:68

[USB\_AUDIO\_SET\_MIN](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab)

@ USB\_AUDIO\_SET\_MIN

**Definition** usb\_audio.h:71

[USB\_AUDIO\_GET\_CUR](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6)

@ USB\_AUDIO\_GET\_CUR

**Definition** usb\_audio.h:70

[USB\_AUDIO\_SET\_MAX](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707)

@ USB\_AUDIO\_SET\_MAX

**Definition** usb\_audio.h:73

[USB\_AUDIO\_GET\_MAX](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb)

@ USB\_AUDIO\_GET\_MAX

**Definition** usb\_audio.h:74

[USB\_AUDIO\_SET\_MEM](usb__audio_8h.md#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0)

@ USB\_AUDIO\_SET\_MEM

**Definition** usb\_audio.h:77

[usb\_audio\_terminal\_types](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79e)

usb\_audio\_terminal\_types

USB Terminal Types Refer to Table 2-1 - Table 2-4 from termt10.pdf.

**Definition** usb\_audio.h:102

[USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_NONE](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d)

@ USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_NONE

Speakerphone, no echo reduction.

**Definition** usb\_audio.h:168

[USB\_AUDIO\_IO\_HANDSET](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207)

@ USB\_AUDIO\_IO\_HANDSET

Handset.

**Definition** usb\_audio.h:164

[USB\_AUDIO\_IN\_MIC\_ARRAY](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262)

@ USB\_AUDIO\_IN\_MIC\_ARRAY

Microphone array.

**Definition** usb\_audio.h:130

[USB\_AUDIO\_IN\_DESKTOP\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a)

@ USB\_AUDIO\_IN\_DESKTOP\_MIC

Desktop microphone.

**Definition** usb\_audio.h:124

[USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_CAN](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14)

@ USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_CAN

Speakerphone, echo cancellation.

**Definition** usb\_audio.h:172

[USB\_AUDIO\_OUT\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c)

@ USB\_AUDIO\_OUT\_SPEAKER

Speaker.

**Definition** usb\_audio.h:142

[USB\_AUDIO\_IN\_PERSONAL\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749)

@ USB\_AUDIO\_IN\_PERSONAL\_MIC

Personal microphone.

**Definition** usb\_audio.h:126

[USB\_AUDIO\_IN\_OM\_DIR\_MIC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b)

@ USB\_AUDIO\_IN\_OM\_DIR\_MIC

Omni directional microphone.

**Definition** usb\_audio.h:128

[USB\_AUDIO\_USB\_VENDOR\_SPEC](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486)

@ USB\_AUDIO\_USB\_VENDOR\_SPEC

USB vendor specific.

**Definition** usb\_audio.h:112

[USB\_AUDIO\_OUT\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0)

@ USB\_AUDIO\_OUT\_UNDEFINED

Output undefined.

**Definition** usb\_audio.h:140

[USB\_AUDIO\_IN\_MICROPHONE](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d)

@ USB\_AUDIO\_IN\_MICROPHONE

Microphone.

**Definition** usb\_audio.h:122

[USB\_AUDIO\_OUT\_LOW\_FREQ\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480)

@ USB\_AUDIO\_OUT\_LOW\_FREQ\_SPEAKER

Low frequency effects speaker.

**Definition** usb\_audio.h:154

[USB\_AUDIO\_USB\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4)

@ USB\_AUDIO\_USB\_UNDEFINED

USB undefined.

**Definition** usb\_audio.h:108

[USB\_AUDIO\_USB\_STREAMING](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661)

@ USB\_AUDIO\_USB\_STREAMING

USB streaming.

**Definition** usb\_audio.h:110

[USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_SUP](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6)

@ USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_SUP

Speakerphone, echo reduction.

**Definition** usb\_audio.h:170

[USB\_AUDIO\_OUT\_HEADPHONES](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9)

@ USB\_AUDIO\_OUT\_HEADPHONES

Headphones.

**Definition** usb\_audio.h:144

[USB\_AUDIO\_IN\_PROC\_MIC\_ARRAY](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86)

@ USB\_AUDIO\_IN\_PROC\_MIC\_ARRAY

Processing microphone array.

**Definition** usb\_audio.h:132

[USB\_AUDIO\_IO\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8)

@ USB\_AUDIO\_IO\_UNDEFINED

Bidirectional undefined.

**Definition** usb\_audio.h:162

[USB\_AUDIO\_OUT\_DESKTOP\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795)

@ USB\_AUDIO\_OUT\_DESKTOP\_SPEAKER

Desktop speaker.

**Definition** usb\_audio.h:148

[USB\_AUDIO\_OUT\_ROOM\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213)

@ USB\_AUDIO\_OUT\_ROOM\_SPEAKER

Room speaker.

**Definition** usb\_audio.h:150

[USB\_AUDIO\_OUT\_HEAD\_AUDIO](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73)

@ USB\_AUDIO\_OUT\_HEAD\_AUDIO

Head mounted display audio.

**Definition** usb\_audio.h:146

[USB\_AUDIO\_IO\_HEADSET](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e)

@ USB\_AUDIO\_IO\_HEADSET

Headset.

**Definition** usb\_audio.h:166

[USB\_AUDIO\_IN\_UNDEFINED](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57)

@ USB\_AUDIO\_IN\_UNDEFINED

Input undefined.

**Definition** usb\_audio.h:120

[USB\_AUDIO\_OUT\_COMM\_SPEAKER](usb__audio_8h.md#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b)

@ USB\_AUDIO\_OUT\_COMM\_SPEAKER

Communication speaker.

**Definition** usb\_audio.h:152

[usb\_audio\_cs\_as\_int\_desc\_subtypes](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeb)

usb\_audio\_cs\_as\_int\_desc\_subtypes

Audio Class-Specific AS Interface Descriptor Subtypes Refer to Table A-6 from audio10....

**Definition** usb\_audio.h:57

[USB\_AUDIO\_AS\_DESCRIPTOR\_UNDEFINED](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e)

@ USB\_AUDIO\_AS\_DESCRIPTOR\_UNDEFINED

**Definition** usb\_audio.h:58

[USB\_AUDIO\_AS\_GENERAL](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84)

@ USB\_AUDIO\_AS\_GENERAL

**Definition** usb\_audio.h:59

[USB\_AUDIO\_FORMAT\_TYPE](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4)

@ USB\_AUDIO\_FORMAT\_TYPE

**Definition** usb\_audio.h:60

[USB\_AUDIO\_FORMAT\_SPECIFIC](usb__audio_8h.md#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a)

@ USB\_AUDIO\_FORMAT\_SPECIFIC

**Definition** usb\_audio.h:61

[usb\_audio\_send](usb__audio_8h.md#af1874c929638325e9e2a44da0e613041)

int usb\_audio\_send(const struct device \*dev, struct net\_buf \*buffer, size\_t len)

Send data using USB Audio device.

[usb\_audio\_get\_in\_frame\_size](usb__audio_8h.md#af314d5beb1d16377855313d46148a86c)

size\_t usb\_audio\_get\_in\_frame\_size(const struct device \*dev)

Get the frame size that is accepted by the Host.

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_audio.h](usb__audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
