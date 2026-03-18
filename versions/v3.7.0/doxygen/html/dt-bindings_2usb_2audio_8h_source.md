---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2usb_2audio_8h_source.html
original_path: doxygen/html/dt-bindings_2usb_2audio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio.h

[Go to the documentation of this file.](dt-bindings_2usb_2audio_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_AUDIO\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_AUDIO\_H

9

10/\* USB Device Class Definition for Audio Devices Release 2.0 May 31, 2006

11 \* A.7 Audio Function Category Codes

12 \*/

[ 13](dt-bindings_2usb_2audio_8h.md#a473b6e15e022d8a22f9e1f41f7faeba2)#define AUDIO\_FUNCTION\_SUBCLASS\_UNDEFINED 0x00

[ 14](dt-bindings_2usb_2audio_8h.md#ad7607f93fa9510650051e3f28376a02a)#define AUDIO\_FUNCTION\_DESKTOP\_SPEAKER 0x01

[ 15](dt-bindings_2usb_2audio_8h.md#abe58fbbbb9797e1398692944877511a1)#define AUDIO\_FUNCTION\_HOME\_THEATER 0x02

[ 16](dt-bindings_2usb_2audio_8h.md#a3879fde1219c850f73722d36985960fb)#define AUDIO\_FUNCTION\_MICROPHONE 0x03

[ 17](dt-bindings_2usb_2audio_8h.md#a06d56e1c795164b50d5c8a6c230793d9)#define AUDIO\_FUNCTION\_HEADSET 0x04

[ 18](dt-bindings_2usb_2audio_8h.md#a4d9df2836001b65105cb9f9b5979e332)#define AUDIO\_FUNCTION\_TELEPHONE 0x05

[ 19](dt-bindings_2usb_2audio_8h.md#a3dbb5dfcdfc87881bf7d8948e9cd45c8)#define AUDIO\_FUNCTION\_CONVERTER 0x06

[ 20](dt-bindings_2usb_2audio_8h.md#a6900b280435b064f1f43bd0c83d79dc4)#define AUDIO\_FUNCTION\_VOICE\_SOUND\_RECORDER 0x07

[ 21](dt-bindings_2usb_2audio_8h.md#aa8b3e55c7e6dd610a354af04e9cf3462)#define AUDIO\_FUNCTION\_IO\_BOX 0x08

[ 22](dt-bindings_2usb_2audio_8h.md#ab252ed82b632209fce6f1e9602f73a39)#define AUDIO\_FUNCTION\_MUSICAL\_INSTRUMENT 0x09

[ 23](dt-bindings_2usb_2audio_8h.md#a18e9fa9324fe789c2e759eeed69282ba)#define AUDIO\_FUNCTION\_PRO\_AUDIO 0x0A

[ 24](dt-bindings_2usb_2audio_8h.md#a41078dde7492c94faccc78faef169aa4)#define AUDIO\_FUNCTION\_AUDIO\_VIDEO 0x0B

[ 25](dt-bindings_2usb_2audio_8h.md#af1af19c6180d3384df89c900499e34a2)#define AUDIO\_FUNCTION\_CONTROL\_PANEL 0x0C

[ 26](dt-bindings_2usb_2audio_8h.md#af2779ede0da5332a7a04f037c012d56c)#define AUDIO\_FUNCTION\_OTHER 0xFF

27

28

29/\* USB Device Class Definition for Terminal Types

30 \* Both "Universal Serial Bus Device Class Definition for Terminal Types"

31 \* Release 2.0 May 31, 2006 and Release 3.0 September 22, 2016 contain exactly

32 \* the same terminal types and values.

33 \*/

34

35/\* 2.1 USB Terminal Types \*/

[ 36](dt-bindings_2usb_2audio_8h.md#a292dc954e9120a122d56e9daf8b72f47)#define USB\_TERMINAL\_UNDEFINED 0x0100

[ 37](dt-bindings_2usb_2audio_8h.md#a7ab3eef75a6b2a3ab5c99a16bc93a439)#define USB\_TERMINAL\_STREAMING 0x0101

[ 38](dt-bindings_2usb_2audio_8h.md#a6ab66c693dde79afee1d102a121fcd4c)#define USB\_TERMINAL\_VENDOR\_SPECIFIC 0x01FF

39

40/\* 2.2 Input Terminal Types \*/

[ 41](dt-bindings_2usb_2audio_8h.md#a0a79431ecd6f9a7932233e01fd27dfa2)#define INPUT\_TERMINAL\_UNDEFINED 0x0200

[ 42](dt-bindings_2usb_2audio_8h.md#ac3b0d532ff97bd321b3a7c0399d3699f)#define INPUT\_TERMINAL\_MICROPHONE 0x0201

[ 43](dt-bindings_2usb_2audio_8h.md#a696fd2cc77c5ac64fae3c713df534189)#define INPUT\_TERMINAL\_DESKTOP\_MICROPHONE 0x0202

[ 44](dt-bindings_2usb_2audio_8h.md#a3dd70544ce70b832fc9012823ae08c3e)#define INPUT\_TERMINAL\_PERSONAL\_MICROPHONE 0x0203

[ 45](dt-bindings_2usb_2audio_8h.md#abe82d0c4e87a163628d2f708180ceab6)#define INPUT\_TERMINAL\_OMNI\_DIRECTIONAL\_MICROPHONE 0x0204

[ 46](dt-bindings_2usb_2audio_8h.md#aca8f01c471845eef0cd27b37550b2468)#define INPUT\_TERMINAL\_MICROPHONE\_ARRAY 0x0205

[ 47](dt-bindings_2usb_2audio_8h.md#a7d97cb05791741b50c86e07096dd761c)#define INPUT\_TERMINAL\_PROCESSING\_MICROPHONE\_ARRAY 0x0206

48

49/\* 2.3 Output Terminal Types \*/

[ 50](dt-bindings_2usb_2audio_8h.md#a394f4baecd7d0d7a1165746f81028369)#define OUTPUT\_TERMINAL\_UNDEFINED 0x0300

[ 51](dt-bindings_2usb_2audio_8h.md#a5b36095777c3220b1cc81759b8144381)#define OUTPUT\_TERMINAL\_SPEAKER 0x0301

[ 52](dt-bindings_2usb_2audio_8h.md#a4b9e4313786ee1d84902e6da1b05ace6)#define OUTPUT\_TERMINAL\_HEADPHONES 0x0302

[ 53](dt-bindings_2usb_2audio_8h.md#a6059461cfdd64db6201d1e0617376237)#define OUTPUT\_TERMINAL\_HEAD\_MOUNTED\_DISPLAY\_AUDIO 0x0303

[ 54](dt-bindings_2usb_2audio_8h.md#a49bc14fca4c3aff926a210807a114ae6)#define OUTPUT\_TERMINAL\_DESKTOP\_SPEAKER 0x0304

[ 55](dt-bindings_2usb_2audio_8h.md#acdd32fe2e04543413eaa35517027ff31)#define OUTPUT\_TERMINAL\_ROOM\_SPEAKER 0x0305

[ 56](dt-bindings_2usb_2audio_8h.md#ac34dbadad29f4bba29e3a214b2cb383d)#define OUTPUT\_TERMINAL\_COMMUNICATION\_SPEAKER 0x0306

[ 57](dt-bindings_2usb_2audio_8h.md#a2ad2ed54af2d6a50eaac80026a15e622)#define OUTPUT\_TERMINAL\_LOW\_FREQUENCY\_EFFECTS\_SPEAKER 0x0307

58

59/\* 2.4 Bi-directional Terminal Types \*/

[ 60](dt-bindings_2usb_2audio_8h.md#ac9658076027099652b708fd522054554)#define BIDIRECTIONAL\_TERMINAL\_UNDEFINED 0x0400

[ 61](dt-bindings_2usb_2audio_8h.md#a843c082b65c4ef3487fbb683fa82a037)#define BIDIRECTIONAL\_TERMINAL\_HANDSET 0x0401

[ 62](dt-bindings_2usb_2audio_8h.md#a3655df7f588b40b05d1e715069867c4b)#define BIDIRECTIONAL\_TERMINAL\_HEADSET 0x0402

[ 63](dt-bindings_2usb_2audio_8h.md#a788d71e702eef587faec88d2ea0b8b76)#define BIDIRECTIONAL\_TERMINAL\_SPEAKERPHONE\_NO\_ECHO\_REDUCTION 0x0403

[ 64](dt-bindings_2usb_2audio_8h.md#a45004711c44413429fdf876b4c6a2ca1)#define BIDIRECTIONAL\_TERMINAL\_ECHO\_SUPPRESSING\_SPEAKERPHONE 0x0404

[ 65](dt-bindings_2usb_2audio_8h.md#a72931fbd4dac3cdb6a031b1d1a578d59)#define BIDIRECTIONAL\_TERMINAL\_ECHO\_CANCELLING\_SPEAKERPHONE 0x0405

66

67/\* 2.5 Telephony Terminal Types \*/

[ 68](dt-bindings_2usb_2audio_8h.md#a58db26f7a557645eae30f99aa3081dd5)#define TELEPHONY\_TERMINAL\_UNDEFINED 0x0500

[ 69](dt-bindings_2usb_2audio_8h.md#aaa4bb6ff32f47c183aa8714b11b722fb)#define TELEPHONY\_TERMINAL\_PHONE\_LINE 0x0501

[ 70](dt-bindings_2usb_2audio_8h.md#adb21c5cb13cc4afa49800db476805777)#define TELEPHONY\_TERMINAL\_TELEPHONE 0x0502

[ 71](dt-bindings_2usb_2audio_8h.md#a9f3213426db15963247bcffa4edf9a65)#define TELEPHONY\_TERMINAL\_DOWN\_LINE\_PHONE 0x0503

72

73/\* 2.6 External Terminal Types \*/

[ 74](dt-bindings_2usb_2audio_8h.md#aca82b7803103175e741a2e4c66e1b2b9)#define EXTERNAL\_TERMINAL\_UNDEFINED 0x0600

[ 75](dt-bindings_2usb_2audio_8h.md#a2ac3d52e831e2d3f32a4ffb4d1970676)#define EXTERNAL\_TERMINAL\_ANALOG\_CONNECTOR 0x0601

[ 76](dt-bindings_2usb_2audio_8h.md#a761561fd620d5937940f787d7d5ff777)#define EXTERNAL\_TERMINAL\_DIGITAL\_AUDIO\_INTERFACE 0x0602

[ 77](dt-bindings_2usb_2audio_8h.md#a9aaf9f03bd7ebd6f2b5425b0141d13ad)#define EXTERNAL\_TERMINAL\_LINE\_CONNECTOR 0x0603

[ 78](dt-bindings_2usb_2audio_8h.md#a3c3b73374968ef6994b81fb939f68924)#define EXTERNAL\_TERMINAL\_LEGACY\_AUDIO\_CONNECTOR 0x0604

[ 79](dt-bindings_2usb_2audio_8h.md#a9889b2abdb8d02f349e9b3b9b308aa3d)#define EXTERNAL\_TERMINAL\_SPDIF\_INTERFACE 0x0605

[ 80](dt-bindings_2usb_2audio_8h.md#ab514248bb09e170be071a6fdc82226b3)#define EXTERNAL\_TERMINAL\_1394\_DA\_STREAM 0x0606

[ 81](dt-bindings_2usb_2audio_8h.md#a6fda0d595e79a61248700c3d994c2867)#define EXTERNAL\_TERMINAL\_1394\_DV\_STREAM\_SOUNDTRACK 0x0607

[ 82](dt-bindings_2usb_2audio_8h.md#aebc29b8cff2eeaea9a343a6089d4fc94)#define EXTERNAL\_TERMINAL\_ADAT\_LIGHTPIPE 0x0608

[ 83](dt-bindings_2usb_2audio_8h.md#a852053dd784cd847ed857557f3f0ca0c)#define EXTERNAL\_TERMINAL\_TDIF 0x0609

[ 84](dt-bindings_2usb_2audio_8h.md#a93a9007e85c6cecc42ba334ba6666ad4)#define EXTERNAL\_TERMINAL\_MADI 0x060A

85

86/\* 2.7 Embedded Function Terminal Types \*/

[ 87](dt-bindings_2usb_2audio_8h.md#aea3207bf2a12779afb215de3e4a5ed7d)#define EMBEDDED\_TERMINAL\_UNDEFINED 0x0700

[ 88](dt-bindings_2usb_2audio_8h.md#a335a5bc40cb97802ad0c68f9b29948fc)#define EMBEDDED\_TERMINAL\_LEVEL\_CALIBRATION\_NOISE\_SOURCE 0x0701

[ 89](dt-bindings_2usb_2audio_8h.md#ad8347c42b5eb3586c4d490370c21d194)#define EMBEDDED\_TERMINAL\_EQUALIZATION\_NOISE 0x0702

[ 90](dt-bindings_2usb_2audio_8h.md#a49f8a92d83dab3e8c53ef475ce4d805c)#define EMBEDDED\_TERMINAL\_CD\_PLAYER 0x0703

[ 91](dt-bindings_2usb_2audio_8h.md#ac39c605c34e0b6c7c679cd85730879a3)#define EMBEDDED\_TERMINAL\_DAT 0x0704

[ 92](dt-bindings_2usb_2audio_8h.md#aa2de301fc91b026cf5c6de850116e131)#define EMBEDDED\_TERMINAL\_DCC 0x0705

[ 93](dt-bindings_2usb_2audio_8h.md#aac3f961f58fd796c5c76fdc7db0acbeb)#define EMBEDDED\_TERMINAL\_COMPRESSED\_AUDIO\_PLAYER 0x0706

[ 94](dt-bindings_2usb_2audio_8h.md#a37d5a9d204ada550f4168bbecd60e8de)#define EMBEDDED\_TERMINAL\_ANALOG\_TAPE 0x0707

[ 95](dt-bindings_2usb_2audio_8h.md#a45ad40dab975eca3326272ce184bf61a)#define EMBEDDED\_TERMINAL\_PHONOGRAPH 0x0708

[ 96](dt-bindings_2usb_2audio_8h.md#a5c406d46612173bc1e9d4bd81c3f6232)#define EMBEDDED\_TERMINAL\_VCR\_AUDIO 0x0709

[ 97](dt-bindings_2usb_2audio_8h.md#a57508f7ea9a0c5c61e8c1fec241d023a)#define EMBEDDED\_TERMINAL\_VIDEO\_DISC\_AUDIO 0x070A

[ 98](dt-bindings_2usb_2audio_8h.md#a8fb4f904840989aec4defbd7d5fa065d)#define EMBEDDED\_TERMINAL\_DVD\_AUDIO 0x070B

[ 99](dt-bindings_2usb_2audio_8h.md#a755cf91bce7f116de2287816b24f1f79)#define EMBEDDED\_TERMINAL\_TV\_TUNER\_AUDIO 0x070C

[ 100](dt-bindings_2usb_2audio_8h.md#ab1a54f43c0525d4a8104bf950b140e21)#define EMBEDDED\_TERMINAL\_SATELLITE\_RECEIVER\_AUDIO 0x070D

[ 101](dt-bindings_2usb_2audio_8h.md#a294d562511a34e090e17ad6c1f081ff7)#define EMBEDDED\_TERMINAL\_CABLE\_TUNER\_AUDIO 0x070E

[ 102](dt-bindings_2usb_2audio_8h.md#aa36eb6cec461c9351ecdb757b6a139dd)#define EMBEDDED\_TERMINAL\_DSS\_AUDIO 0x070F

[ 103](dt-bindings_2usb_2audio_8h.md#aba5b429d0f4a72d68544c9708a47e55c)#define EMBEDDED\_TERMINAL\_RADIO\_RECEIVER 0x0710

[ 104](dt-bindings_2usb_2audio_8h.md#aafb83ecd011dccfbb7ed4d57045500d0)#define EMBEDDED\_TERMINAL\_RADIO\_TRANSMITTER 0x0711

[ 105](dt-bindings_2usb_2audio_8h.md#a58c881cc2bb8765cb3cb7ba35038b47b)#define EMBEDDED\_TERMINAL\_MULTI\_TRACK\_RECORDER 0x0712

[ 106](dt-bindings_2usb_2audio_8h.md#a83d800c8869f82cd9ebdde6f9173711b)#define EMBEDDED\_TERMINAL\_SYNTHESIZER 0x0713

[ 107](dt-bindings_2usb_2audio_8h.md#abc37aac5f2a4352a71d58d95722bab5b)#define EMBEDDED\_TERMINAL\_PIANO 0x0714

[ 108](dt-bindings_2usb_2audio_8h.md#af6fbfb745771e7fdabd5e6d8ac56404a)#define EMBEDDED\_TERMINAL\_GUITAR 0x0715

[ 109](dt-bindings_2usb_2audio_8h.md#a64305e1b4fa679a6b200c03942d084ca)#define EMBEDDED\_TERMINAL\_DRUMS\_RHYTHM 0x0716

[ 110](dt-bindings_2usb_2audio_8h.md#ac496de5b7b6bdd2d9d180f66b59c6ef3)#define EMBEDDED\_TERMINAL\_OTHER\_MUSICAL\_INSTRUMENT 0x0717

111

112#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_AUDIO\_H \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [usb](dir_b73aae62b1ec6442c36a8e8be819fb7c.md)
- [audio.h](dt-bindings_2usb_2audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
