---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cellular_8h_source.html
original_path: doxygen/html/cellular_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cellular.h

[Go to the documentation of this file.](cellular_8h.md)

1/\*

2 \* Copyright (c) 2023 Bjarki Arge Andreasen

3 \* Copyright (c) 2023 Lucas Denefle

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CELLULAR\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_CELLULAR\_H\_

15

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25#include <[errno.h](errno_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e)enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) {

[ 33](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255) [CELLULAR\_ACCESS\_TECHNOLOGY\_GSM](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255) = 0,

[ 34](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea7c1911e14140b58340092891879d6048) [CELLULAR\_ACCESS\_TECHNOLOGY\_GPRS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea7c1911e14140b58340092891879d6048),

[ 35](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea3edbbd5543a26bb12a28ac131e97da0f) [CELLULAR\_ACCESS\_TECHNOLOGY\_UMTS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea3edbbd5543a26bb12a28ac131e97da0f),

[ 36](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eab205ca0387de08ea4b6f5612fcabbef4) [CELLULAR\_ACCESS\_TECHNOLOGY\_EDGE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eab205ca0387de08ea4b6f5612fcabbef4),

[ 37](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea0e441c38a4166e9ff807f809cee48ebc) [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea0e441c38a4166e9ff807f809cee48ebc),

[ 38](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eaf2844e36d3bcaf8adb67e153ee8203dc) [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M1](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eaf2844e36d3bcaf8adb67e153ee8203dc),

[ 39](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea89be8003f89a2079275b8ed95a68d7e1) [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M2](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea89be8003f89a2079275b8ed95a68d7e1),

[ 40](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea6f06e534f995b27f5856f57673890a3d) [CELLULAR\_ACCESS\_TECHNOLOGY\_NB\_IOT](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea6f06e534f995b27f5856f57673890a3d),

41};

42

[ 44](structcellular__network.md)struct [cellular\_network](structcellular__network.md) {

[ 46](structcellular__network.md#ad7afde61da3322e80f935c2b963eacf0) enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) [technology](structcellular__network.md#ad7afde61da3322e80f935c2b963eacf0);

[ 51](structcellular__network.md#a9313dcce10911b0febd56022c380f283) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[bands](structcellular__network.md#a9313dcce10911b0febd56022c380f283);

[ 53](structcellular__network.md#ab54057fc7cea1387c5ad3694103b0686) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structcellular__network.md#ab54057fc7cea1387c5ad3694103b0686);

54};

55

[ 57](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47)enum [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) {

[ 58](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a) [CELLULAR\_SIGNAL\_RSSI](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a),

[ 59](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a) [CELLULAR\_SIGNAL\_RSRP](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a),

[ 60](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338) [CELLULAR\_SIGNAL\_RSRQ](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338),

61};

62

[ 64](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30)enum [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) {

[ 66](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de) [CELLULAR\_MODEM\_INFO\_IMEI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de),

[ 68](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8) [CELLULAR\_MODEM\_INFO\_MODEL\_ID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8),

[ 70](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1) [CELLULAR\_MODEM\_INFO\_MANUFACTURER](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1),

[ 72](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027) [CELLULAR\_MODEM\_INFO\_FW\_VERSION](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027),

[ 74](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245) [CELLULAR\_MODEM\_INFO\_SIM\_IMSI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245),

[ 76](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d) [CELLULAR\_MODEM\_INFO\_SIM\_ICCID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d),

77};

78

[ 80](group__cellular__interface.md#ga71ddc5b9e09da398d02caadc91ef3cfc)typedef int (\*[cellular\_api\_configure\_networks](group__cellular__interface.md#ga71ddc5b9e09da398d02caadc91ef3cfc))(const struct [device](structdevice.md) \*dev,

81 const struct [cellular\_network](structcellular__network.md) \*networks,

82 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [size](structcellular__network.md#ab54057fc7cea1387c5ad3694103b0686));

83

[ 85](group__cellular__interface.md#ga6aa2c51fa80d5420593021c35444308a)typedef int (\*[cellular\_api\_get\_supported\_networks](group__cellular__interface.md#ga6aa2c51fa80d5420593021c35444308a))(const struct [device](structdevice.md) \*dev,

86 const struct [cellular\_network](structcellular__network.md) \*\*networks,

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[size](structcellular__network.md#ab54057fc7cea1387c5ad3694103b0686));

88

[ 90](group__cellular__interface.md#ga75cac77838970288d4d23647eaafd30b)typedef int (\*[cellular\_api\_get\_signal](group__cellular__interface.md#ga75cac77838970288d4d23647eaafd30b))(const struct [device](structdevice.md) \*dev,

91 const enum [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value);

92

[ 94](group__cellular__interface.md#ga03095206ae2b77ce232dd05b172bd56d)typedef int (\*[cellular\_api\_get\_modem\_info](group__cellular__interface.md#ga03095206ae2b77ce232dd05b172bd56d))(const struct [device](structdevice.md) \*dev,

95 const enum [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) type,

96 char \*info, size\_t size);

97

[ 99](structcellular__driver__api.md)\_\_subsystem struct [cellular\_driver\_api](structcellular__driver__api.md) {

[ 100](structcellular__driver__api.md#ac219c2c960f838bc8c0fd41307a3ff05) [cellular\_api\_configure\_networks](group__cellular__interface.md#ga71ddc5b9e09da398d02caadc91ef3cfc) [configure\_networks](structcellular__driver__api.md#ac219c2c960f838bc8c0fd41307a3ff05);

[ 101](structcellular__driver__api.md#a32ede01e742a2e7c18e9cb4f963b90fe) [cellular\_api\_get\_supported\_networks](group__cellular__interface.md#ga6aa2c51fa80d5420593021c35444308a) [get\_supported\_networks](structcellular__driver__api.md#a32ede01e742a2e7c18e9cb4f963b90fe);

[ 102](structcellular__driver__api.md#a7d64a630e4dafd57c00b04d3dfea1b79) [cellular\_api\_get\_signal](group__cellular__interface.md#ga75cac77838970288d4d23647eaafd30b) [get\_signal](structcellular__driver__api.md#a7d64a630e4dafd57c00b04d3dfea1b79);

[ 103](structcellular__driver__api.md#ab03cc8706fafd729c21cec9569eae8db) [cellular\_api\_get\_modem\_info](group__cellular__interface.md#ga03095206ae2b77ce232dd05b172bd56d) [get\_modem\_info](structcellular__driver__api.md#ab03cc8706fafd729c21cec9569eae8db);

104};

105

[ 127](group__cellular__interface.md#gaa53d52e58221c998eec272a4d063bdd4)static inline int [cellular\_configure\_networks](group__cellular__interface.md#gaa53d52e58221c998eec272a4d063bdd4)(const struct [device](structdevice.md) \*dev,

128 const struct [cellular\_network](structcellular__network.md) \*networks, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size)

129{

130 const struct [cellular\_driver\_api](structcellular__driver__api.md) \*api = (const struct [cellular\_driver\_api](structcellular__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

131

132 if (api->[configure\_networks](structcellular__driver__api.md#ac219c2c960f838bc8c0fd41307a3ff05) == NULL) {

133 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

134 }

135

136 return api->[configure\_networks](structcellular__driver__api.md#ac219c2c960f838bc8c0fd41307a3ff05)(dev, networks, size);

137}

138

[ 150](group__cellular__interface.md#ga70340d22df56665b1d113abc8b314a95)static inline int [cellular\_get\_supported\_networks](group__cellular__interface.md#ga70340d22df56665b1d113abc8b314a95)(const struct [device](structdevice.md) \*dev,

151 const struct [cellular\_network](structcellular__network.md) \*\*networks,

152 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size)

153{

154 const struct [cellular\_driver\_api](structcellular__driver__api.md) \*api = (const struct [cellular\_driver\_api](structcellular__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

155

156 if (api->[get\_supported\_networks](structcellular__driver__api.md#a32ede01e742a2e7c18e9cb4f963b90fe) == NULL) {

157 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

158 }

159

160 return api->[get\_supported\_networks](structcellular__driver__api.md#a32ede01e742a2e7c18e9cb4f963b90fe)(dev, networks, size);

161}

162

[ 175](group__cellular__interface.md#ga022eb4eecc300b14110107a46824cac0)static inline int [cellular\_get\_signal](group__cellular__interface.md#ga022eb4eecc300b14110107a46824cac0)(const struct [device](structdevice.md) \*dev,

176 const enum [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value)

177{

178 const struct [cellular\_driver\_api](structcellular__driver__api.md) \*api = (const struct [cellular\_driver\_api](structcellular__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

179

180 if (api->[get\_signal](structcellular__driver__api.md#a7d64a630e4dafd57c00b04d3dfea1b79) == NULL) {

181 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

182 }

183

184 return api->[get\_signal](structcellular__driver__api.md#a7d64a630e4dafd57c00b04d3dfea1b79)(dev, type, value);

185}

186

[ 200](group__cellular__interface.md#ga757f0802fd72d61d035a81057f23d5ca)static inline int [cellular\_get\_modem\_info](group__cellular__interface.md#ga757f0802fd72d61d035a81057f23d5ca)(const struct [device](structdevice.md) \*dev,

201 const enum [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) type, char \*info,

202 size\_t size)

203{

204 const struct [cellular\_driver\_api](structcellular__driver__api.md) \*api = (const struct [cellular\_driver\_api](structcellular__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

205

206 if (api->[get\_modem\_info](structcellular__driver__api.md#ab03cc8706fafd729c21cec9569eae8db) == NULL) {

207 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

208 }

209

210 return api->[get\_modem\_info](structcellular__driver__api.md#ab03cc8706fafd729c21cec9569eae8db)(dev, type, info, size);

211}

212

213#ifdef \_\_cplusplus

214}

215#endif

216

220

221#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CELLULAR\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cellular\_get\_signal](group__cellular__interface.md#ga022eb4eecc300b14110107a46824cac0)

static int cellular\_get\_signal(const struct device \*dev, const enum cellular\_signal\_type type, int16\_t \*value)

Get signal for the device.

**Definition** cellular.h:175

[cellular\_api\_get\_modem\_info](group__cellular__interface.md#ga03095206ae2b77ce232dd05b172bd56d)

int(\* cellular\_api\_get\_modem\_info)(const struct device \*dev, const enum cellular\_modem\_info\_type type, char \*info, size\_t size)

API for getting modem information.

**Definition** cellular.h:94

[cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e)

cellular\_access\_technology

Cellular access technologies.

**Definition** cellular.h:32

[cellular\_api\_get\_supported\_networks](group__cellular__interface.md#ga6aa2c51fa80d5420593021c35444308a)

int(\* cellular\_api\_get\_supported\_networks)(const struct device \*dev, const struct cellular\_network \*\*networks, uint8\_t \*size)

API for getting supported networks.

**Definition** cellular.h:85

[cellular\_get\_supported\_networks](group__cellular__interface.md#ga70340d22df56665b1d113abc8b314a95)

static int cellular\_get\_supported\_networks(const struct device \*dev, const struct cellular\_network \*\*networks, uint8\_t \*size)

Get supported cellular networks for the device.

**Definition** cellular.h:150

[cellular\_api\_configure\_networks](group__cellular__interface.md#ga71ddc5b9e09da398d02caadc91ef3cfc)

int(\* cellular\_api\_configure\_networks)(const struct device \*dev, const struct cellular\_network \*networks, uint8\_t size)

API for configuring networks.

**Definition** cellular.h:80

[cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47)

cellular\_signal\_type

Cellular signal type.

**Definition** cellular.h:57

[cellular\_get\_modem\_info](group__cellular__interface.md#ga757f0802fd72d61d035a81057f23d5ca)

static int cellular\_get\_modem\_info(const struct device \*dev, const enum cellular\_modem\_info\_type type, char \*info, size\_t size)

Get modem info for the device.

**Definition** cellular.h:200

[cellular\_api\_get\_signal](group__cellular__interface.md#ga75cac77838970288d4d23647eaafd30b)

int(\* cellular\_api\_get\_signal)(const struct device \*dev, const enum cellular\_signal\_type type, int16\_t \*value)

API for getting network signal strength.

**Definition** cellular.h:90

[cellular\_configure\_networks](group__cellular__interface.md#gaa53d52e58221c998eec272a4d063bdd4)

static int cellular\_configure\_networks(const struct device \*dev, const struct cellular\_network \*networks, uint8\_t size)

Configure cellular networks for the device.

**Definition** cellular.h:127

[cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30)

cellular\_modem\_info\_type

Cellular modem info type.

**Definition** cellular.h:64

[CELLULAR\_ACCESS\_TECHNOLOGY\_LTE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea0e441c38a4166e9ff807f809cee48ebc)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_LTE

**Definition** cellular.h:37

[CELLULAR\_ACCESS\_TECHNOLOGY\_UMTS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea3edbbd5543a26bb12a28ac131e97da0f)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_UMTS

**Definition** cellular.h:35

[CELLULAR\_ACCESS\_TECHNOLOGY\_NB\_IOT](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea6f06e534f995b27f5856f57673890a3d)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_NB\_IOT

**Definition** cellular.h:40

[CELLULAR\_ACCESS\_TECHNOLOGY\_GPRS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea7c1911e14140b58340092891879d6048)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_GPRS

**Definition** cellular.h:34

[CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M2](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea89be8003f89a2079275b8ed95a68d7e1)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M2

**Definition** cellular.h:39

[CELLULAR\_ACCESS\_TECHNOLOGY\_GSM](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_GSM

**Definition** cellular.h:33

[CELLULAR\_ACCESS\_TECHNOLOGY\_EDGE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eab205ca0387de08ea4b6f5612fcabbef4)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_EDGE

**Definition** cellular.h:36

[CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M1](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eaf2844e36d3bcaf8adb67e153ee8203dc)

@ CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M1

**Definition** cellular.h:38

[CELLULAR\_SIGNAL\_RSRQ](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338)

@ CELLULAR\_SIGNAL\_RSRQ

**Definition** cellular.h:60

[CELLULAR\_SIGNAL\_RSRP](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a)

@ CELLULAR\_SIGNAL\_RSRP

**Definition** cellular.h:59

[CELLULAR\_SIGNAL\_RSSI](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a)

@ CELLULAR\_SIGNAL\_RSSI

**Definition** cellular.h:58

[CELLULAR\_MODEM\_INFO\_SIM\_IMSI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245)

@ CELLULAR\_MODEM\_INFO\_SIM\_IMSI

International Mobile Subscriber Identity.

**Definition** cellular.h:74

[CELLULAR\_MODEM\_INFO\_MANUFACTURER](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1)

@ CELLULAR\_MODEM\_INFO\_MANUFACTURER

Modem manufacturer.

**Definition** cellular.h:70

[CELLULAR\_MODEM\_INFO\_MODEL\_ID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8)

@ CELLULAR\_MODEM\_INFO\_MODEL\_ID

Modem model ID.

**Definition** cellular.h:68

[CELLULAR\_MODEM\_INFO\_SIM\_ICCID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)

@ CELLULAR\_MODEM\_INFO\_SIM\_ICCID

Integrated Circuit Card Identification Number (SIM).

**Definition** cellular.h:76

[CELLULAR\_MODEM\_INFO\_FW\_VERSION](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027)

@ CELLULAR\_MODEM\_INFO\_FW\_VERSION

Modem fw version.

**Definition** cellular.h:72

[CELLULAR\_MODEM\_INFO\_IMEI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de)

@ CELLULAR\_MODEM\_INFO\_IMEI

International Mobile Equipment Identity.

**Definition** cellular.h:66

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[cellular\_driver\_api](structcellular__driver__api.md)

Cellular driver API.

**Definition** cellular.h:99

[cellular\_driver\_api::get\_supported\_networks](structcellular__driver__api.md#a32ede01e742a2e7c18e9cb4f963b90fe)

cellular\_api\_get\_supported\_networks get\_supported\_networks

**Definition** cellular.h:101

[cellular\_driver\_api::get\_signal](structcellular__driver__api.md#a7d64a630e4dafd57c00b04d3dfea1b79)

cellular\_api\_get\_signal get\_signal

**Definition** cellular.h:102

[cellular\_driver\_api::get\_modem\_info](structcellular__driver__api.md#ab03cc8706fafd729c21cec9569eae8db)

cellular\_api\_get\_modem\_info get\_modem\_info

**Definition** cellular.h:103

[cellular\_driver\_api::configure\_networks](structcellular__driver__api.md#ac219c2c960f838bc8c0fd41307a3ff05)

cellular\_api\_configure\_networks configure\_networks

**Definition** cellular.h:100

[cellular\_network](structcellular__network.md)

Cellular network structure.

**Definition** cellular.h:44

[cellular\_network::bands](structcellular__network.md#a9313dcce10911b0febd56022c380f283)

uint16\_t \* bands

List of bands, as defined by the specified cellular access technology, to enables.

**Definition** cellular.h:51

[cellular\_network::size](structcellular__network.md#ab54057fc7cea1387c5ad3694103b0686)

uint16\_t size

Size of bands.

**Definition** cellular.h:53

[cellular\_network::technology](structcellular__network.md#ad7afde61da3322e80f935c2b963eacf0)

enum cellular\_access\_technology technology

Cellular access technology.

**Definition** cellular.h:46

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [cellular.h](cellular_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
