---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mipi__stp__decoder_8h_source.html
original_path: doxygen/html/mipi__stp__decoder_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_stp\_decoder.h

[Go to the documentation of this file.](mipi__stp__decoder_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_MIPI\_STP\_DECODER\_H\_\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_MIPI\_STP\_DECODER\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d)enum [mipi\_stp\_decoder\_ctrl\_type](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d) {

[ 24](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5) [STP\_DATA4](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5) = 1,

[ 25](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100) [STP\_DATA8](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100) = 2,

[ 26](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184) [STP\_DATA16](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184) = 4,

[ 27](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e) [STP\_DATA32](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e) = 8,

[ 28](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a) [STP\_DATA64](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a) = 16,

[ 29](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e) [STP\_DECODER\_NULL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e) = 128,

[ 30](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daaac471f0ecdd67e4b4838cf57ff0f4a1) [STP\_DECODER\_MASTER](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daaac471f0ecdd67e4b4838cf57ff0f4a1),

[ 31](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a) [STP\_DECODER\_MERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a),

[ 32](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360) [STP\_DECODER\_CHANNEL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360),

[ 33](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f) [STP\_DECODER\_VERSION](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f),

[ 34](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37) [STP\_DECODER\_FREQ](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37),

[ 35](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7) [STP\_DECODER\_GERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7),

[ 36](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5) [STP\_DECODER\_FLAG](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5),

[ 37](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef) [STP\_DECODER\_ASYNC](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef),

[ 38](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4) [STP\_DECODER\_NOT\_SUPPORTED](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4),

39};

40

[ 46](group__mipi__stp__decoder__apis.md#gae19e768343e0543260752ec2876d1faa)#define STP\_DECODER\_TYPE2STR(\_type) \

47 \_type == STP\_DATA4 ? "DATA4" : (\

48 \_type == STP\_DATA8 ? "DATA8" : (\

49 \_type == STP\_DATA16 ? "DATA16" : (\

50 \_type == STP\_DATA32 ? "DATA32" : (\

51 \_type == STP\_DATA64 ? "DATA64" : (\

52 \_type == STP\_DECODER\_NULL ? "NULL" : (\

53 \_type == STP\_DECODER\_MASTER ? "MASTER" : (\

54 \_type == STP\_DECODER\_MERROR ? "MERROR" : (\

55 \_type == STP\_DECODER\_CHANNEL ? "CHANNEL" : (\

56 \_type == STP\_DECODER\_VERSION ? "VERSION" : (\

57 \_type == STP\_DECODER\_FREQ ? "FREQ" : (\

58 \_type == STP\_DECODER\_GERROR ? "GERROR" : (\

59 \_type == STP\_DECODER\_FLAG ? "FLAG" : (\

60 \_type == STP\_DECODER\_ASYNC ? "ASYNC" : (\

61 "Unknown"))))))))))))))

62

[ 64](unionmipi__stp__decoder__data.md)union [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) {

[ 66](unionmipi__stp__decoder__data.md#a3c7d85bc475b27f570b9059745d7d11f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](unionmipi__stp__decoder__data.md#a3c7d85bc475b27f570b9059745d7d11f);

67

[ 69](unionmipi__stp__decoder__data.md#a3b3cae98d63ceda950e88690da282966) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [freq](unionmipi__stp__decoder__data.md#a3b3cae98d63ceda950e88690da282966);

70

[ 72](unionmipi__stp__decoder__data.md#a3dc68ca2196c807965071d754c139655) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ver](unionmipi__stp__decoder__data.md#a3dc68ca2196c807965071d754c139655);

73

[ 75](unionmipi__stp__decoder__data.md#ace873d9e7d38a5f39338618b4d74cdf4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [err](unionmipi__stp__decoder__data.md#ace873d9e7d38a5f39338618b4d74cdf4);

76

[ 78](unionmipi__stp__decoder__data.md#a70db937ada38cb0f97cd45fa78bd9466) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dummy](unionmipi__stp__decoder__data.md#a70db937ada38cb0f97cd45fa78bd9466);

79

[ 81](unionmipi__stp__decoder__data.md#a1cb5f92d1d0976f1ec047e7398e6d95d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [data](unionmipi__stp__decoder__data.md#a1cb5f92d1d0976f1ec047e7398e6d95d);

82};

83

[ 95](group__mipi__stp__decoder__apis.md#gad3456ba4b000dd1a77c4dc85428bd7d8)typedef void (\*[mipi\_stp\_decoder\_cb](group__mipi__stp__decoder__apis.md#gad3456ba4b000dd1a77c4dc85428bd7d8))(enum [mipi\_stp\_decoder\_ctrl\_type](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d) type,

96 union [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) [data](unionmipi__stp__decoder__data.md#a1cb5f92d1d0976f1ec047e7398e6d95d),

97 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts, bool marked);

98

[ 100](structmipi__stp__decoder__config.md)struct [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) {

[ 102](structmipi__stp__decoder__config.md#abf1a03280ec82f3a2db7aef25c6522ac) bool [start\_out\_of\_sync](structmipi__stp__decoder__config.md#abf1a03280ec82f3a2db7aef25c6522ac);

103

[ 105](structmipi__stp__decoder__config.md#a519473c106e406e453c104790045d404) [mipi\_stp\_decoder\_cb](group__mipi__stp__decoder__apis.md#gad3456ba4b000dd1a77c4dc85428bd7d8) [cb](structmipi__stp__decoder__config.md#a519473c106e406e453c104790045d404);

106};

107

[ 115](group__mipi__stp__decoder__apis.md#ga4a67705c849793f02c7ae409434b4e79)int [mipi\_stp\_decoder\_init](group__mipi__stp__decoder__apis.md#ga4a67705c849793f02c7ae409434b4e79)(const struct [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) \*config);

116

[ 127](group__mipi__stp__decoder__apis.md#ga520104e814b15cce22ec74a4e827a5b9)int [mipi\_stp\_decoder\_decode](group__mipi__stp__decoder__apis.md#ga520104e814b15cce22ec74a4e827a5b9)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

128

[ 135](group__mipi__stp__decoder__apis.md#ga0e1be10f234d72e81b48d21bfe8a42f8)void [mipi\_stp\_decoder\_sync\_loss](group__mipi__stp__decoder__apis.md#ga0e1be10f234d72e81b48d21bfe8a42f8)(void);

136

140

141#ifdef \_\_cplusplus

142}

143#endif

144

145#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_MIPI\_STP\_DECODER\_H\_\_ \*/

[mipi\_stp\_decoder\_sync\_loss](group__mipi__stp__decoder__apis.md#ga0e1be10f234d72e81b48d21bfe8a42f8)

void mipi\_stp\_decoder\_sync\_loss(void)

Indicate synchronization loss.

[mipi\_stp\_decoder\_init](group__mipi__stp__decoder__apis.md#ga4a67705c849793f02c7ae409434b4e79)

int mipi\_stp\_decoder\_init(const struct mipi\_stp\_decoder\_config \*config)

Initialize the decoder.

[mipi\_stp\_decoder\_decode](group__mipi__stp__decoder__apis.md#ga520104e814b15cce22ec74a4e827a5b9)

int mipi\_stp\_decoder\_decode(const uint8\_t \*data, size\_t len)

Decode STPv2 stream.

[mipi\_stp\_decoder\_ctrl\_type](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d)

mipi\_stp\_decoder\_ctrl\_type

STPv2 opcodes.

**Definition** mipi\_stp\_decoder.h:23

[mipi\_stp\_decoder\_cb](group__mipi__stp__decoder__apis.md#gad3456ba4b000dd1a77c4dc85428bd7d8)

void(\* mipi\_stp\_decoder\_cb)(enum mipi\_stp\_decoder\_ctrl\_type type, union mipi\_stp\_decoder\_data data, uint64\_t \*ts, bool marked)

Callback signature.

**Definition** mipi\_stp\_decoder.h:95

[STP\_DECODER\_NULL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e)

@ STP\_DECODER\_NULL

**Definition** mipi\_stp\_decoder.h:29

[STP\_DATA4](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5)

@ STP\_DATA4

**Definition** mipi\_stp\_decoder.h:24

[STP\_DECODER\_FLAG](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5)

@ STP\_DECODER\_FLAG

**Definition** mipi\_stp\_decoder.h:36

[STP\_DECODER\_FREQ](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37)

@ STP\_DECODER\_FREQ

**Definition** mipi\_stp\_decoder.h:34

[STP\_DATA16](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184)

@ STP\_DATA16

**Definition** mipi\_stp\_decoder.h:26

[STP\_DATA32](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e)

@ STP\_DATA32

**Definition** mipi\_stp\_decoder.h:27

[STP\_DATA8](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100)

@ STP\_DATA8

**Definition** mipi\_stp\_decoder.h:25

[STP\_DECODER\_CHANNEL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360)

@ STP\_DECODER\_CHANNEL

**Definition** mipi\_stp\_decoder.h:32

[STP\_DATA64](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a)

@ STP\_DATA64

**Definition** mipi\_stp\_decoder.h:28

[STP\_DECODER\_ASYNC](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef)

@ STP\_DECODER\_ASYNC

**Definition** mipi\_stp\_decoder.h:37

[STP\_DECODER\_NOT\_SUPPORTED](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4)

@ STP\_DECODER\_NOT\_SUPPORTED

**Definition** mipi\_stp\_decoder.h:38

[STP\_DECODER\_GERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7)

@ STP\_DECODER\_GERROR

**Definition** mipi\_stp\_decoder.h:35

[STP\_DECODER\_MERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a)

@ STP\_DECODER\_MERROR

**Definition** mipi\_stp\_decoder.h:31

[STP\_DECODER\_MASTER](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daaac471f0ecdd67e4b4838cf57ff0f4a1)

@ STP\_DECODER\_MASTER

**Definition** mipi\_stp\_decoder.h:30

[STP\_DECODER\_VERSION](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f)

@ STP\_DECODER\_VERSION

**Definition** mipi\_stp\_decoder.h:33

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md)

Decoder configuration.

**Definition** mipi\_stp\_decoder.h:100

[mipi\_stp\_decoder\_config::cb](structmipi__stp__decoder__config.md#a519473c106e406e453c104790045d404)

mipi\_stp\_decoder\_cb cb

Callback.

**Definition** mipi\_stp\_decoder.h:105

[mipi\_stp\_decoder\_config::start\_out\_of\_sync](structmipi__stp__decoder__config.md#abf1a03280ec82f3a2db7aef25c6522ac)

bool start\_out\_of\_sync

Indicates that decoder start in out of sync state.

**Definition** mipi\_stp\_decoder.h:102

[mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md)

Union with data associated with a given STP opcode.

**Definition** mipi\_stp\_decoder.h:64

[mipi\_stp\_decoder\_data::data](unionmipi__stp__decoder__data.md#a1cb5f92d1d0976f1ec047e7398e6d95d)

uint64\_t data

Data.

**Definition** mipi\_stp\_decoder.h:81

[mipi\_stp\_decoder\_data::freq](unionmipi__stp__decoder__data.md#a3b3cae98d63ceda950e88690da282966)

uint64\_t freq

Frequency.

**Definition** mipi\_stp\_decoder.h:69

[mipi\_stp\_decoder\_data::id](unionmipi__stp__decoder__data.md#a3c7d85bc475b27f570b9059745d7d11f)

uint16\_t id

ID - used for master and channel.

**Definition** mipi\_stp\_decoder.h:66

[mipi\_stp\_decoder\_data::ver](unionmipi__stp__decoder__data.md#a3dc68ca2196c807965071d754c139655)

uint32\_t ver

Version.

**Definition** mipi\_stp\_decoder.h:72

[mipi\_stp\_decoder\_data::dummy](unionmipi__stp__decoder__data.md#a70db937ada38cb0f97cd45fa78bd9466)

uint32\_t dummy

Dummy.

**Definition** mipi\_stp\_decoder.h:78

[mipi\_stp\_decoder\_data::err](unionmipi__stp__decoder__data.md#ace873d9e7d38a5f39338618b4d74cdf4)

uint32\_t err

Error code.

**Definition** mipi\_stp\_decoder.h:75

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [mipi\_stp\_decoder.h](mipi__stp__decoder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
