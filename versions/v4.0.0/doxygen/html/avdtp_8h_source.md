---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/avdtp_8h_source.html
original_path: doxygen/html/avdtp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

avdtp.h

[Go to the documentation of this file.](avdtp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright 2024 NXP

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 21](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21)enum [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21) {

[ 23](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af) [BT\_AVDTP\_SUCCESS](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af) = 0x00,

[ 25](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a) [BT\_AVDTP\_TIME\_OUT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a) = 0xFF,

[ 27](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f) [BT\_AVDTP\_BAD\_HEADER\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f) = 0x01,

[ 29](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9) [BT\_AVDTP\_BAD\_LENGTH](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9) = 0x11,

[ 31](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064) [BT\_AVDTP\_BAD\_ACP\_SEID](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064) = 0x12,

[ 33](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8) [BT\_AVDTP\_SEP\_IN\_USE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8) = 0x13,

[ 35](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445) [BT\_AVDTP\_SEP\_NOT\_IN\_USE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445) = 0x14,

[ 37](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6) [BT\_AVDTP\_BAD\_SERV\_CATEGORY](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6) = 0x17,

[ 39](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0) [BT\_AVDTP\_BAD\_PAYLOAD\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0) = 0x18,

[ 41](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75) [BT\_AVDTP\_NOT\_SUPPORTED\_COMMAND](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75) = 0x19,

[ 45](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20) [BT\_AVDTP\_INVALID\_CAPABILITIES](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20) = 0x1A,

[ 47](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee) [BT\_AVDTP\_BAD\_RECOVERY\_TYPE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee) = 0x22,

[ 49](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35) [BT\_AVDTP\_BAD\_MEDIA\_TRANSPORT\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35) = 0x23,

[ 51](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099) [BT\_AVDTP\_BAD\_RECOVERY\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099) = 0x25,

[ 53](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7) [BT\_AVDTP\_BAD\_ROHC\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7) = 0x26,

[ 55](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da) [BT\_AVDTP\_BAD\_CP\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da) = 0x27,

[ 57](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14) [BT\_AVDTP\_BAD\_MULTIPLEXING\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14) = 0x28,

[ 59](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21af4849400efd124a97a5e6b797efa1a44) [BT\_AVDTP\_UNSUPPORTED\_CONFIGURAION](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21af4849400efd124a97a5e6b797efa1a44) = 0x29,

[ 64](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818) [BT\_AVDTP\_BAD\_STATE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818) = 0x31,

65};

66

[ 68](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757)enum [bt\_avdtp\_sep\_type](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757) {

[ 70](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f) [BT\_AVDTP\_SOURCE](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f) = 0,

[ 72](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9) [BT\_AVDTP\_SINK](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9) = 1

73};

74

[ 76](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f)enum [bt\_avdtp\_media\_type](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f) {

[ 78](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58) [BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58) = 0x00,

[ 80](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee) [BT\_AVDTP\_VIDEO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee) = 0x01,

[ 82](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4) [BT\_AVDTP\_MULTIMEDIA](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4) = 0x02

83};

84

[ 88](structbt__avdtp__sep__info.md)struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) {

[ 90](structbt__avdtp__sep__info.md#ab644a59a54d943e3d4729a198bda59cd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [inuse](structbt__avdtp__sep__info.md#ab644a59a54d943e3d4729a198bda59cd):1;

[ 92](structbt__avdtp__sep__info.md#a03bf1e8c29eaff7ef3b48f21dff7aa49) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__avdtp__sep__info.md#a03bf1e8c29eaff7ef3b48f21dff7aa49):6;

[ 94](structbt__avdtp__sep__info.md#a3d6c6832a40cdb31976a447459576e0f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__avdtp__sep__info.md#a3d6c6832a40cdb31976a447459576e0f):1;

[ 96](structbt__avdtp__sep__info.md#add86d89b0e062f034aa85bf7121313ee) enum [bt\_avdtp\_sep\_type](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757) [tsep](structbt__avdtp__sep__info.md#add86d89b0e062f034aa85bf7121313ee);

[ 100](structbt__avdtp__sep__info.md#a8cd4323a80ad4138095d5aceb08a64b6) enum [bt\_avdtp\_media\_type](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f) [media\_type](structbt__avdtp__sep__info.md#a8cd4323a80ad4138095d5aceb08a64b6);

101};

102

[ 104](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51)enum [bt\_avdtp\_service\_category](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51) {

[ 106](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c) [BT\_AVDTP\_SERVICE\_MEDIA\_TRANSPORT](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c) = 0x01,

[ 108](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37) [BT\_AVDTP\_SERVICE\_REPORTING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37) = 0x02,

[ 110](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902) [BT\_AVDTP\_SERVICE\_MEDIA\_RECOVERY](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902) = 0x03,

[ 112](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642) [BT\_AVDTP\_SERVICE\_CONTENT\_PROTECTION](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642) = 0x04,

[ 114](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73) [BT\_AVDTP\_SERVICE\_HEADER\_COMPRESSION](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73) = 0x05,

[ 116](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439) [BT\_AVDTP\_SERVICE\_MULTIPLEXING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439) = 0x06,

[ 118](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e) [BT\_AVDTP\_SERVICE\_MEDIA\_CODEC](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e) = 0x07,

[ 120](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0) [BT\_AVDTP\_SERVICE\_DELAY\_REPORTING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0) = 0x08,

121};

122

[ 124](structbt__avdtp__sep.md)struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) {

[ 126](structbt__avdtp__sep.md#a0258b35f0834479a2dccdcad9b3854b9) struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) [sep\_info](structbt__avdtp__sep.md#a0258b35f0834479a2dccdcad9b3854b9);

[ 128](structbt__avdtp__sep.md#a33e4959b5d7c5f53469ed59af4cae022) struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) [chan](structbt__avdtp__sep.md#a33e4959b5d7c5f53469ed59af4cae022);

[ 130](structbt__avdtp__sep.md#aeec9eb785451c8da65725603058a2a14) void (\*[media\_data\_cb](structbt__avdtp__sep.md#aeec9eb785451c8da65725603058a2a14))(struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) \*sep,

131 struct [net\_buf](structnet__buf.md) \*buf);

[ 133](structbt__avdtp__sep.md#a5c1afb8231c42d39156023939583681a) struct bt\_avdtp \*[session](structbt__avdtp__sep.md#a5c1afb8231c42d39156023939583681a);

[ 135](structbt__avdtp__sep.md#a2405b59cc7ed23c9cb221a9a684dc386) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__avdtp__sep.md#a2405b59cc7ed23c9cb221a9a684dc386);

136 /\* Internally used list node \*/

137 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

138};

139

140#ifdef \_\_cplusplus

141}

142#endif

143

144#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AVDTP\_H\_ \*/

[bt\_avdtp\_sep\_type](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757)

bt\_avdtp\_sep\_type

Stream End Point Type.

**Definition** avdtp.h:68

[BT\_AVDTP\_SINK](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9)

@ BT\_AVDTP\_SINK

Sink Role.

**Definition** avdtp.h:72

[BT\_AVDTP\_SOURCE](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f)

@ BT\_AVDTP\_SOURCE

Source Role.

**Definition** avdtp.h:70

[bt\_avdtp\_media\_type](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f)

bt\_avdtp\_media\_type

Stream End Point Media Type.

**Definition** avdtp.h:76

[BT\_AVDTP\_VIDEO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee)

@ BT\_AVDTP\_VIDEO

Video Media Type.

**Definition** avdtp.h:80

[BT\_AVDTP\_MULTIMEDIA](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4)

@ BT\_AVDTP\_MULTIMEDIA

Multimedia Media Type.

**Definition** avdtp.h:82

[BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)

@ BT\_AVDTP\_AUDIO

Audio Media Type.

**Definition** avdtp.h:78

[bt\_avdtp\_service\_category](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51)

bt\_avdtp\_service\_category

service category Type

**Definition** avdtp.h:104

[BT\_AVDTP\_SERVICE\_MEDIA\_RECOVERY](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902)

@ BT\_AVDTP\_SERVICE\_MEDIA\_RECOVERY

Recovery.

**Definition** avdtp.h:110

[BT\_AVDTP\_SERVICE\_HEADER\_COMPRESSION](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73)

@ BT\_AVDTP\_SERVICE\_HEADER\_COMPRESSION

Header Compression.

**Definition** avdtp.h:114

[BT\_AVDTP\_SERVICE\_CONTENT\_PROTECTION](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642)

@ BT\_AVDTP\_SERVICE\_CONTENT\_PROTECTION

Content Protection.

**Definition** avdtp.h:112

[BT\_AVDTP\_SERVICE\_MEDIA\_CODEC](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e)

@ BT\_AVDTP\_SERVICE\_MEDIA\_CODEC

Media Codec.

**Definition** avdtp.h:118

[BT\_AVDTP\_SERVICE\_REPORTING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37)

@ BT\_AVDTP\_SERVICE\_REPORTING

Reporting.

**Definition** avdtp.h:108

[BT\_AVDTP\_SERVICE\_MEDIA\_TRANSPORT](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c)

@ BT\_AVDTP\_SERVICE\_MEDIA\_TRANSPORT

Media Transport.

**Definition** avdtp.h:106

[BT\_AVDTP\_SERVICE\_MULTIPLEXING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439)

@ BT\_AVDTP\_SERVICE\_MULTIPLEXING

Multiplexing.

**Definition** avdtp.h:116

[BT\_AVDTP\_SERVICE\_DELAY\_REPORTING](avdtp_8h.md#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0)

@ BT\_AVDTP\_SERVICE\_DELAY\_REPORTING

Delay Reporting.

**Definition** avdtp.h:120

[bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21)

bt\_avdtp\_err\_code

AVDTP error code.

**Definition** avdtp.h:21

[BT\_AVDTP\_BAD\_STATE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818)

@ BT\_AVDTP\_BAD\_STATE

Indicates that the ACP state machine is in an invalid state in order to process the signal.

**Definition** avdtp.h:64

[BT\_AVDTP\_BAD\_RECOVERY\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099)

@ BT\_AVDTP\_BAD\_RECOVERY\_FORMAT

The format of Recovery Service Capability is not correct.

**Definition** avdtp.h:51

[BT\_AVDTP\_SUCCESS](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af)

@ BT\_AVDTP\_SUCCESS

The response is success, it is not from avdtp spec.

**Definition** avdtp.h:23

[BT\_AVDTP\_TIME\_OUT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a)

@ BT\_AVDTP\_TIME\_OUT

The request is time out without response, it is not from avdtp spec.

**Definition** avdtp.h:25

[BT\_AVDTP\_BAD\_SERV\_CATEGORY](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6)

@ BT\_AVDTP\_BAD\_SERV\_CATEGORY

The value of Service Category in the request packet is not defined in AVDTP.

**Definition** avdtp.h:37

[BT\_AVDTP\_NOT\_SUPPORTED\_COMMAND](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75)

@ BT\_AVDTP\_NOT\_SUPPORTED\_COMMAND

The requested command is not supported by the device.

**Definition** avdtp.h:41

[BT\_AVDTP\_INVALID\_CAPABILITIES](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20)

@ BT\_AVDTP\_INVALID\_CAPABILITIES

The reconfigure command is an attempt to reconfigure a transport service codec\_cap of the SEP.

**Definition** avdtp.h:45

[BT\_AVDTP\_BAD\_ROHC\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7)

@ BT\_AVDTP\_BAD\_ROHC\_FORMAT

The format of Header Compression Service Capability is not correct.

**Definition** avdtp.h:53

[BT\_AVDTP\_BAD\_HEADER\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f)

@ BT\_AVDTP\_BAD\_HEADER\_FORMAT

The request packet header format error.

**Definition** avdtp.h:27

[BT\_AVDTP\_SEP\_IN\_USE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8)

@ BT\_AVDTP\_SEP\_IN\_USE

The SEP is in use.

**Definition** avdtp.h:33

[BT\_AVDTP\_BAD\_PAYLOAD\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0)

@ BT\_AVDTP\_BAD\_PAYLOAD\_FORMAT

The requested command has an incorrect payload format.

**Definition** avdtp.h:39

[BT\_AVDTP\_BAD\_MULTIPLEXING\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14)

@ BT\_AVDTP\_BAD\_MULTIPLEXING\_FORMAT

The format of Multiplexing Service Capability is not correct.

**Definition** avdtp.h:57

[BT\_AVDTP\_BAD\_MEDIA\_TRANSPORT\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35)

@ BT\_AVDTP\_BAD\_MEDIA\_TRANSPORT\_FORMAT

The format of Media Transport Capability is not correct.

**Definition** avdtp.h:49

[BT\_AVDTP\_BAD\_LENGTH](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9)

@ BT\_AVDTP\_BAD\_LENGTH

The request packet length is not match the assumed length.

**Definition** avdtp.h:29

[BT\_AVDTP\_BAD\_CP\_FORMAT](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da)

@ BT\_AVDTP\_BAD\_CP\_FORMAT

The format of Content Protection Service Capability is not correct.

**Definition** avdtp.h:55

[BT\_AVDTP\_BAD\_ACP\_SEID](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064)

@ BT\_AVDTP\_BAD\_ACP\_SEID

The requested command indicates an invalid ACP SEID (not addressable).

**Definition** avdtp.h:31

[BT\_AVDTP\_BAD\_RECOVERY\_TYPE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee)

@ BT\_AVDTP\_BAD\_RECOVERY\_TYPE

The requested Recovery Type is not defined in AVDTP.

**Definition** avdtp.h:47

[BT\_AVDTP\_SEP\_NOT\_IN\_USE](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445)

@ BT\_AVDTP\_SEP\_NOT\_IN\_USE

The SEP is not in use.

**Definition** avdtp.h:35

[BT\_AVDTP\_UNSUPPORTED\_CONFIGURAION](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21af4849400efd124a97a5e6b797efa1a44)

@ BT\_AVDTP\_UNSUPPORTED\_CONFIGURAION

Configuration not supported.

**Definition** avdtp.h:59

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md)

AVDTP stream endpoint information.

**Definition** avdtp.h:88

[bt\_avdtp\_sep\_info::id](structbt__avdtp__sep__info.md#a03bf1e8c29eaff7ef3b48f21dff7aa49)

uint8\_t id

Stream End Point ID that is the identifier of the stream endpoint.

**Definition** avdtp.h:92

[bt\_avdtp\_sep\_info::reserved](structbt__avdtp__sep__info.md#a3d6c6832a40cdb31976a447459576e0f)

uint8\_t reserved

Reserved.

**Definition** avdtp.h:94

[bt\_avdtp\_sep\_info::media\_type](structbt__avdtp__sep__info.md#a8cd4323a80ad4138095d5aceb08a64b6)

enum bt\_avdtp\_media\_type media\_type

Media-type of the End Point Only BT\_AVDTP\_AUDIO is supported now.

**Definition** avdtp.h:100

[bt\_avdtp\_sep\_info::inuse](structbt__avdtp__sep__info.md#ab644a59a54d943e3d4729a198bda59cd)

uint8\_t inuse

End Point usage status.

**Definition** avdtp.h:90

[bt\_avdtp\_sep\_info::tsep](structbt__avdtp__sep__info.md#add86d89b0e062f034aa85bf7121313ee)

enum bt\_avdtp\_sep\_type tsep

Stream End-point Type that indicates if the stream end-point is SNK or SRC.

**Definition** avdtp.h:96

[bt\_avdtp\_sep](structbt__avdtp__sep.md)

AVDTP Stream End Point.

**Definition** avdtp.h:124

[bt\_avdtp\_sep::sep\_info](structbt__avdtp__sep.md#a0258b35f0834479a2dccdcad9b3854b9)

struct bt\_avdtp\_sep\_info sep\_info

Stream End Point information.

**Definition** avdtp.h:126

[bt\_avdtp\_sep::state](structbt__avdtp__sep.md#a2405b59cc7ed23c9cb221a9a684dc386)

uint8\_t state

SEP state.

**Definition** avdtp.h:135

[bt\_avdtp\_sep::chan](structbt__avdtp__sep.md#a33e4959b5d7c5f53469ed59af4cae022)

struct bt\_l2cap\_br\_chan chan

Media Transport Channel.

**Definition** avdtp.h:128

[bt\_avdtp\_sep::session](structbt__avdtp__sep.md#a5c1afb8231c42d39156023939583681a)

struct bt\_avdtp \* session

avdtp session

**Definition** avdtp.h:133

[bt\_avdtp\_sep::media\_data\_cb](structbt__avdtp__sep.md#aeec9eb785451c8da65725603058a2a14)

void(\* media\_data\_cb)(struct bt\_avdtp\_sep \*sep, struct net\_buf \*buf)

the endpoint media data

**Definition** avdtp.h:130

[bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md)

BREDR L2CAP Channel structure.

**Definition** l2cap.h:246

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [avdtp.h](avdtp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
