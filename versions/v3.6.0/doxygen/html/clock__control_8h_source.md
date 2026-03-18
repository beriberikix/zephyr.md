---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/clock__control_8h_source.html
original_path: doxygen/html/clock__control_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control.h

[Go to the documentation of this file.](clock__control_8h.md)

1/\* clock\_control.h - public clock controller driver API \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_H\_

16

23

24#include <[errno.h](errno_8h.md)>

25#include <stddef.h>

26

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

30#include <[zephyr/sys/slist.h](slist_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36/\* Clock control API \*/

37

38/\* Used to select all subsystem of a clock controller \*/

[ 39](group__clock__control__interface.md#ga9aa9a4e00c1e7985a1fea6bed235003e)#define CLOCK\_CONTROL\_SUBSYS\_ALL NULL

40

[ 44](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09)enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) {

[ 45](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52) [CLOCK\_CONTROL\_STATUS\_STARTING](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52),

[ 46](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa) [CLOCK\_CONTROL\_STATUS\_OFF](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa),

[ 47](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db) [CLOCK\_CONTROL\_STATUS\_ON](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db),

[ 48](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc) [CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc)

49};

50

[ 56](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)typedef void \*[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db);

57

[ 64](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1)typedef void \*[clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1);

65

[ 72](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275)typedef void (\*[clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275))(const struct [device](structdevice.md) \*dev,

73 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) subsys,

74 void \*user\_data);

75

[ 76](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099)typedef int (\*[clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099))(const struct [device](structdevice.md) \*dev,

77 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

78

[ 79](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0)typedef int (\*[clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0))(const struct [device](structdevice.md) \*dev,

80 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

81 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

82

[ 83](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d)typedef int (\*[clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d))(const struct [device](structdevice.md) \*dev,

84 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

85 [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb,

86 void \*user\_data);

87

88typedef enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) (\*[clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a))(

89 const struct [device](structdevice.md) \*dev,

90 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

91

[ 92](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b)typedef int (\*[clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b))(const struct [device](structdevice.md) \*dev,

93 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

94 [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate);

95

[ 96](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0)typedef int (\*[clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0))(const struct [device](structdevice.md) \*dev,

97 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

98 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

99

[ 100](structclock__control__driver__api.md)struct [clock\_control\_driver\_api](structclock__control__driver__api.md) {

[ 101](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f) [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) [on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f);

[ 102](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3) [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) [off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3);

[ 103](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc) [clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d) [async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc);

[ 104](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332) [clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0) [get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332);

[ 105](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9) [clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a) [get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9);

[ 106](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c) [clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b) [set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c);

[ 107](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3) [clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0) [configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3);

108};

109

[ 123](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)static inline int [clock\_control\_on](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)(const struct [device](structdevice.md) \*dev,

124 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

125{

126 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

127 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

128

129 return api->[on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f)(dev, sys);

130}

131

[ 142](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)static inline int [clock\_control\_off](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)(const struct [device](structdevice.md) \*dev,

143 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

144{

145 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

146 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

147

148 return api->[off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3)(dev, sys);

149}

150

[ 168](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)static inline int [clock\_control\_async\_on](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)(const struct [device](structdevice.md) \*dev,

169 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

170 [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb,

171 void \*user\_data)

172{

173 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

174 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

175

176 if (api->[async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc) == NULL) {

177 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

178 }

179

180 return api->[async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc)(dev, sys, cb, user\_data);

181}

182

[ 191](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)static inline enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) [clock\_control\_get\_status](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)(const struct [device](structdevice.md) \*dev,

192 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

193{

194 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

195 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

196

197 if (!api->[get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)) {

198 return [CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc);

199 }

200

201 return api->[get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)(dev, sys);

202}

203

[ 216](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)static inline int [clock\_control\_get\_rate](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)(const struct [device](structdevice.md) \*dev,

217 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

218 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate)

219{

220 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

221 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

222

223 if (api->[get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332) == NULL) {

224 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

225 }

226

227 return api->[get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332)(dev, sys, rate);

228}

229

[ 246](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)static inline int [clock\_control\_set\_rate](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)(const struct [device](structdevice.md) \*dev,

247 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

248 [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate)

249{

250 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

251 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

252

253 if (api->[set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c) == NULL) {

254 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

255 }

256

257 return api->[set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c)(dev, sys, rate);

258}

259

[ 282](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)static inline int [clock\_control\_configure](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)(const struct [device](structdevice.md) \*dev,

283 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

284 void \*data)

285{

286 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

287 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

288

289 if (api->[configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3) == NULL) {

290 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

291 }

292

293 return api->[configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3)(dev, sys, data);

294}

295

296#ifdef \_\_cplusplus

297}

298#endif

299

303

304#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[clock\_control\_get\_rate](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)

static int clock\_control\_get\_rate(const struct device \*dev, clock\_control\_subsys\_t sys, uint32\_t \*rate)

Obtain the clock rate of given sub-system.

**Definition** clock\_control.h:216

[clock\_control\_async\_on](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)

static int clock\_control\_async\_on(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_cb\_t cb, void \*user\_data)

Request clock to start with notification when clock has been started.

**Definition** clock\_control.h:168

[clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1)

void \* clock\_control\_subsys\_rate\_t

clock\_control\_subsys\_rate\_t is a type to identify a clock controller sub-system rate.

**Definition** clock\_control.h:64

[clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a)

enum clock\_control\_status(\* clock\_control\_get\_status\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys)

**Definition** clock\_control.h:88

[clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d)

int(\* clock\_control\_async\_on\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_cb\_t cb, void \*user\_data)

**Definition** clock\_control.h:83

[clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275)

void(\* clock\_control\_cb\_t)(const struct device \*dev, clock\_control\_subsys\_t subsys, void \*user\_data)

Callback called on clock started.

**Definition** clock\_control.h:72

[clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0)

int(\* clock\_control\_configure\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys, void \*data)

**Definition** clock\_control.h:96

[clock\_control\_get\_status](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)

static enum clock\_control\_status clock\_control\_get\_status(const struct device \*dev, clock\_control\_subsys\_t sys)

Get clock status.

**Definition** clock\_control.h:191

[clock\_control\_set\_rate](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)

static int clock\_control\_set\_rate(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_subsys\_rate\_t rate)

Set the rate of the clock controlled by the device.

**Definition** clock\_control.h:246

[clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0)

int(\* clock\_control\_get)(const struct device \*dev, clock\_control\_subsys\_t sys, uint32\_t \*rate)

**Definition** clock\_control.h:79

[clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099)

int(\* clock\_control)(const struct device \*dev, clock\_control\_subsys\_t sys)

**Definition** clock\_control.h:76

[clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b)

int(\* clock\_control\_set)(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_subsys\_rate\_t rate)

**Definition** clock\_control.h:92

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:56

[clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09)

clock\_control\_status

Current clock status.

**Definition** clock\_control.h:44

[clock\_control\_off](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)

static int clock\_control\_off(const struct device \*dev, clock\_control\_subsys\_t sys)

Disable a clock controlled by the device.

**Definition** clock\_control.h:142

[clock\_control\_on](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)

static int clock\_control\_on(const struct device \*dev, clock\_control\_subsys\_t sys)

Enable a clock controlled by the device.

**Definition** clock\_control.h:123

[clock\_control\_configure](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)

static int clock\_control\_configure(const struct device \*dev, clock\_control\_subsys\_t sys, void \*data)

Configure a source clock.

**Definition** clock\_control.h:282

[CLOCK\_CONTROL\_STATUS\_ON](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db)

@ CLOCK\_CONTROL\_STATUS\_ON

**Definition** clock\_control.h:47

[CLOCK\_CONTROL\_STATUS\_OFF](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa)

@ CLOCK\_CONTROL\_STATUS\_OFF

**Definition** clock\_control.h:46

[CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc)

@ CLOCK\_CONTROL\_STATUS\_UNKNOWN

**Definition** clock\_control.h:48

[CLOCK\_CONTROL\_STATUS\_STARTING](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52)

@ CLOCK\_CONTROL\_STATUS\_STARTING

**Definition** clock\_control.h:45

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[clock\_control\_driver\_api](structclock__control__driver__api.md)

**Definition** clock\_control.h:100

[clock\_control\_driver\_api::set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c)

clock\_control\_set set\_rate

**Definition** clock\_control.h:106

[clock\_control\_driver\_api::on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f)

clock\_control on

**Definition** clock\_control.h:101

[clock\_control\_driver\_api::get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)

clock\_control\_get\_status\_fn get\_status

**Definition** clock\_control.h:105

[clock\_control\_driver\_api::off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3)

clock\_control off

**Definition** clock\_control.h:102

[clock\_control\_driver\_api::async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc)

clock\_control\_async\_on\_fn async\_on

**Definition** clock\_control.h:103

[clock\_control\_driver\_api::get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332)

clock\_control\_get get\_rate

**Definition** clock\_control.h:104

[clock\_control\_driver\_api::configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3)

clock\_control\_configure\_fn configure

**Definition** clock\_control.h:107

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control.h](clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
