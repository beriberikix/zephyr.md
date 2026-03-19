---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__dfu_8h_source.html
original_path: doxygen/html/usb__dfu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_dfu.h

[Go to the documentation of this file.](usb__dfu_8h.md)

1/\* SPDX-License-Identifier: BSD-3-Clause \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \*

5 \* Copyright(c) 2015,2016 Intel Corporation.

6 \* Copyright(c) 2017 PHYTEC Messtechnik GmbH

7 \*

8 \* Redistribution and use in source and binary forms, with or without

9 \* modification, are permitted provided that the following conditions

10 \* are met:

11 \*

12 \* \* Redistributions of source code must retain the above copyright

13 \* notice, this list of conditions and the following disclaimer.

14 \* \* Redistributions in binary form must reproduce the above copyright

15 \* notice, this list of conditions and the following disclaimer in

16 \* the documentation and/or other materials provided with the

17 \* distribution.

18 \* \* Neither the name of Intel Corporation nor the names of its

19 \* contributors may be used to endorse or promote products derived

20 \* from this software without specific prior written permission.

21 \*

22 \* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS

23 \* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT

24 \* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR

25 \* A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT

26 \* OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,

27 \* SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT

28 \* LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,

29 \* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY

30 \* THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT

31 \* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE

32 \* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

33 \*

34 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

35

43

44#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_DFU\_H\_

45#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_DFU\_H\_

46

47#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

48

[ 50](usb__dfu_8h.md#a86d100d1016e44b1a57d72f87394f49b)#define DFU\_SUBCLASS 0x01

51

[ 53](usb__dfu_8h.md#a6da8cdd5028653f5008ae62371d68049)#define DFU\_RT\_PROTOCOL 0x01

54

[ 56](usb__dfu_8h.md#ad44791964357de89e8f051a0eeff7b6c)#define DFU\_MODE\_PROTOCOL 0x02

57

[ 61](usb__dfu_8h.md#a1dbfcd9de4badc68f1a79720113dfa3d)#define DFU\_DETACH 0x00

[ 62](usb__dfu_8h.md#aaf8b2bc0fa447ec925a47cee00916e4a)#define DFU\_DNLOAD 0x01

[ 63](usb__dfu_8h.md#a9ec42539a3b1d7a1fcb47383e5ae73b7)#define DFU\_UPLOAD 0x02

[ 64](usb__dfu_8h.md#af45d9250c3e5dfb12a217bc08828cc06)#define DFU\_GETSTATUS 0x03

[ 65](usb__dfu_8h.md#aff6ab40ddfc07a8e873aa4c8dde99fc8)#define DFU\_CLRSTATUS 0x04

[ 66](usb__dfu_8h.md#a41912ad6c650bf2df2b730f3d6d07849)#define DFU\_GETSTATE 0x05

[ 67](usb__dfu_8h.md#a9f0bb6811ae976a2cd8a7b42c19a8390)#define DFU\_ABORT 0x06

68

[ 70](usb__dfu_8h.md#a2d6a59039cf1e8f97ba0443e7d20fd1c)#define DFU\_FUNC\_DESC 0x21

71

[ 73](usb__dfu_8h.md#a8f41515182d31b45f06523deb89a0b6d)#define DFU\_ATTR\_WILL\_DETACH 0x08

[ 74](usb__dfu_8h.md#a9426f19a5d9970da8b7479e6f341e26c)#define DFU\_ATTR\_MANIFESTATION\_TOLERANT 0x04

[ 75](usb__dfu_8h.md#a0fe01b636c7e5224a7cbd0ddcd3ac3e7)#define DFU\_ATTR\_CAN\_UPLOAD 0x02

[ 76](usb__dfu_8h.md#a07cbf2381d03bafb4d844cd00fd95079)#define DFU\_ATTR\_CAN\_DNLOAD 0x01

77

[ 79](usb__dfu_8h.md#a7f333dc5f69079381f912b9b3ab9d202)#define DFU\_VERSION 0x0110

80

[ 82](structdfu__runtime__descriptor.md)struct [dfu\_runtime\_descriptor](structdfu__runtime__descriptor.md) {

[ 83](structdfu__runtime__descriptor.md#a0eeecced453c285febca7a9d867c7241) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structdfu__runtime__descriptor.md#a0eeecced453c285febca7a9d867c7241);

[ 84](structdfu__runtime__descriptor.md#a5464341cf3c706af93de58c6db5edfb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structdfu__runtime__descriptor.md#a5464341cf3c706af93de58c6db5edfb9);

[ 85](structdfu__runtime__descriptor.md#aa8d5f353530adf846b14e88c97095a50) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmAttributes](structdfu__runtime__descriptor.md#aa8d5f353530adf846b14e88c97095a50);

[ 86](structdfu__runtime__descriptor.md#adaf32d218daf9fc74a6639845355cd9b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDetachTimeOut](structdfu__runtime__descriptor.md#adaf32d218daf9fc74a6639845355cd9b);

[ 87](structdfu__runtime__descriptor.md#a86312a99ed7c89eb027ca3e35b7b32e5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTransferSize](structdfu__runtime__descriptor.md#a86312a99ed7c89eb027ca3e35b7b32e5);

[ 88](structdfu__runtime__descriptor.md#a3dca4dc35930794eaa0ac03522949048) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdDFUVersion](structdfu__runtime__descriptor.md#a3dca4dc35930794eaa0ac03522949048);

89} \_\_packed;

90

[ 92](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31)enum [dfu\_status](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31) {

[ 93](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19) [statusOK](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19),

[ 94](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d) [errTARGET](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d),

[ 95](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e) [errFILE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e),

[ 96](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1) [errWRITE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1),

[ 97](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54) [errERASE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54),

[ 98](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be) [errCHECK\_ERASED](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be),

[ 99](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8) [errPROG](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8),

[ 100](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff) [errVERIFY](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff),

[ 101](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902) [errADDRESS](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902),

[ 102](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998) [errNOTDONE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998),

[ 103](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb) [errFIRMWARE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb),

[ 104](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210) [errVENDOR](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210),

[ 105](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947) [errUSB](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947),

[ 106](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb) [errPOR](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb),

[ 107](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471) [errUNKNOWN](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471),

[ 108](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788) [errSTALLEDPKT](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788)

109};

110

[ 112](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143)enum [dfu\_state](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143) {

[ 113](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa) [appIDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa),

[ 114](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1) [appDETACH](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1),

[ 115](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c) [dfuIDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c),

[ 116](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f) [dfuDNLOAD\_SYNC](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f),

[ 117](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e) [dfuDNBUSY](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e),

[ 118](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff) [dfuDNLOAD\_IDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff),

[ 119](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c) [dfuMANIFEST\_SYNC](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c),

[ 120](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6) [dfuMANIFEST](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6),

[ 121](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8) [dfuMANIFEST\_WAIT\_RST](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8),

[ 122](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2) [dfuUPLOAD\_IDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2),

[ 123](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd) [dfuERROR](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd),

124};

125

[ 126](usb__dfu_8h.md#a892959f521c403e4ec295c252e75e5dc)void [wait\_for\_usb\_dfu](usb__dfu_8h.md#a892959f521c403e4ec295c252e75e5dc)([k\_timeout\_t](structk__timeout__t.md) delay);

127

128#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_DFU\_H\_ \*/

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[dfu\_runtime\_descriptor](structdfu__runtime__descriptor.md)

Run-Time Functional Descriptor.

**Definition** usb\_dfu.h:82

[dfu\_runtime\_descriptor::bLength](structdfu__runtime__descriptor.md#a0eeecced453c285febca7a9d867c7241)

uint8\_t bLength

**Definition** usb\_dfu.h:83

[dfu\_runtime\_descriptor::bcdDFUVersion](structdfu__runtime__descriptor.md#a3dca4dc35930794eaa0ac03522949048)

uint16\_t bcdDFUVersion

**Definition** usb\_dfu.h:88

[dfu\_runtime\_descriptor::bDescriptorType](structdfu__runtime__descriptor.md#a5464341cf3c706af93de58c6db5edfb9)

uint8\_t bDescriptorType

**Definition** usb\_dfu.h:84

[dfu\_runtime\_descriptor::wTransferSize](structdfu__runtime__descriptor.md#a86312a99ed7c89eb027ca3e35b7b32e5)

uint16\_t wTransferSize

**Definition** usb\_dfu.h:87

[dfu\_runtime\_descriptor::bmAttributes](structdfu__runtime__descriptor.md#aa8d5f353530adf846b14e88c97095a50)

uint8\_t bmAttributes

**Definition** usb\_dfu.h:85

[dfu\_runtime\_descriptor::wDetachTimeOut](structdfu__runtime__descriptor.md#adaf32d218daf9fc74a6639845355cd9b)

uint16\_t wDetachTimeOut

**Definition** usb\_dfu.h:86

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

[dfu\_state](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143)

dfu\_state

bState values for the DFU\_GETSTATUS response

**Definition** usb\_dfu.h:112

[dfuMANIFEST\_SYNC](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c)

@ dfuMANIFEST\_SYNC

**Definition** usb\_dfu.h:119

[dfuERROR](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd)

@ dfuERROR

**Definition** usb\_dfu.h:123

[dfuUPLOAD\_IDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2)

@ dfuUPLOAD\_IDLE

**Definition** usb\_dfu.h:122

[dfuIDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c)

@ dfuIDLE

**Definition** usb\_dfu.h:115

[dfuDNLOAD\_IDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff)

@ dfuDNLOAD\_IDLE

**Definition** usb\_dfu.h:118

[appDETACH](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1)

@ appDETACH

**Definition** usb\_dfu.h:114

[dfuMANIFEST\_WAIT\_RST](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8)

@ dfuMANIFEST\_WAIT\_RST

**Definition** usb\_dfu.h:121

[appIDLE](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa)

@ appIDLE

**Definition** usb\_dfu.h:113

[dfuMANIFEST](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6)

@ dfuMANIFEST

**Definition** usb\_dfu.h:120

[dfuDNLOAD\_SYNC](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f)

@ dfuDNLOAD\_SYNC

**Definition** usb\_dfu.h:116

[dfuDNBUSY](usb__dfu_8h.md#a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e)

@ dfuDNBUSY

**Definition** usb\_dfu.h:117

[wait\_for\_usb\_dfu](usb__dfu_8h.md#a892959f521c403e4ec295c252e75e5dc)

void wait\_for\_usb\_dfu(k\_timeout\_t delay)

[dfu\_status](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31)

dfu\_status

bStatus values for the DFU\_GETSTATUS response

**Definition** usb\_dfu.h:92

[errSTALLEDPKT](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788)

@ errSTALLEDPKT

**Definition** usb\_dfu.h:108

[errVENDOR](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210)

@ errVENDOR

**Definition** usb\_dfu.h:104

[errVERIFY](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff)

@ errVERIFY

**Definition** usb\_dfu.h:100

[errTARGET](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d)

@ errTARGET

**Definition** usb\_dfu.h:94

[errFILE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e)

@ errFILE

**Definition** usb\_dfu.h:95

[errERASE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54)

@ errERASE

**Definition** usb\_dfu.h:97

[errWRITE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1)

@ errWRITE

**Definition** usb\_dfu.h:96

[errCHECK\_ERASED](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be)

@ errCHECK\_ERASED

**Definition** usb\_dfu.h:98

[errUSB](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947)

@ errUSB

**Definition** usb\_dfu.h:105

[errADDRESS](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902)

@ errADDRESS

**Definition** usb\_dfu.h:101

[errFIRMWARE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb)

@ errFIRMWARE

**Definition** usb\_dfu.h:103

[errPOR](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb)

@ errPOR

**Definition** usb\_dfu.h:106

[errUNKNOWN](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471)

@ errUNKNOWN

**Definition** usb\_dfu.h:107

[errPROG](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8)

@ errPROG

**Definition** usb\_dfu.h:99

[statusOK](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19)

@ statusOK

**Definition** usb\_dfu.h:93

[errNOTDONE](usb__dfu_8h.md#abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998)

@ errNOTDONE

**Definition** usb\_dfu.h:102

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_dfu.h](usb__dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
