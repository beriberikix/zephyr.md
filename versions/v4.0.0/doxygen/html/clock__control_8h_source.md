---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clock__control_8h_source.html
original_path: doxygen/html/clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

25

26#include <[errno.h](errno_8h.md)>

27#include <stddef.h>

28

29#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

30#include <[zephyr/device.h](device_8h.md)>

31#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

32#include <[zephyr/sys/slist.h](slist_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

38/\* Clock control API \*/

39

40/\* Used to select all subsystem of a clock controller \*/

[ 41](group__clock__control__interface.md#ga9aa9a4e00c1e7985a1fea6bed235003e)#define CLOCK\_CONTROL\_SUBSYS\_ALL NULL

42

[ 46](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09)enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) {

[ 47](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52) [CLOCK\_CONTROL\_STATUS\_STARTING](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52),

[ 48](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa) [CLOCK\_CONTROL\_STATUS\_OFF](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa),

[ 49](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db) [CLOCK\_CONTROL\_STATUS\_ON](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db),

[ 50](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc) [CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc)

51};

52

[ 58](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)typedef void \*[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db);

59

[ 66](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1)typedef void \*[clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1);

67

[ 74](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275)typedef void (\*[clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275))(const struct [device](structdevice.md) \*dev,

75 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) subsys,

76 void \*user\_data);

77

[ 78](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099)typedef int (\*[clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099))(const struct [device](structdevice.md) \*dev,

79 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

80

[ 81](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0)typedef int (\*[clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0))(const struct [device](structdevice.md) \*dev,

82 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

83 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

84

[ 85](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d)typedef int (\*[clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d))(const struct [device](structdevice.md) \*dev,

86 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

87 [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb,

88 void \*user\_data);

89

90typedef enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) (\*[clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a))(

91 const struct [device](structdevice.md) \*dev,

92 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

93

[ 94](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b)typedef int (\*[clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b))(const struct [device](structdevice.md) \*dev,

95 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

96 [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate);

97

[ 98](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0)typedef int (\*[clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0))(const struct [device](structdevice.md) \*dev,

99 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

100 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

101

[ 102](structclock__control__driver__api.md)\_\_subsystem struct [clock\_control\_driver\_api](structclock__control__driver__api.md) {

[ 103](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f) [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) [on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f);

[ 104](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3) [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) [off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3);

[ 105](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc) [clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d) [async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc);

[ 106](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332) [clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0) [get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332);

[ 107](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9) [clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a) [get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9);

[ 108](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c) [clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b) [set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c);

[ 109](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3) [clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0) [configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3);

110};

111

[ 125](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)static inline int [clock\_control\_on](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)(const struct [device](structdevice.md) \*dev,

126 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

127{

128 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

129 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

130

131 return api->[on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f)(dev, sys);

132}

133

[ 144](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)static inline int [clock\_control\_off](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)(const struct [device](structdevice.md) \*dev,

145 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

146{

147 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

148 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

149

150 return api->[off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3)(dev, sys);

151}

152

[ 170](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)static inline int [clock\_control\_async\_on](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)(const struct [device](structdevice.md) \*dev,

171 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

172 [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb,

173 void \*user\_data)

174{

175 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

176 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

177

178 if (api->[async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc) == NULL) {

179 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

180 }

181

182 return api->[async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc)(dev, sys, cb, user\_data);

183}

184

[ 193](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)static inline enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) [clock\_control\_get\_status](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)(const struct [device](structdevice.md) \*dev,

194 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys)

195{

196 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

197 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

198

199 if (!api->[get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)) {

200 return [CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc);

201 }

202

203 return api->[get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)(dev, sys);

204}

205

[ 218](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)static inline int [clock\_control\_get\_rate](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)(const struct [device](structdevice.md) \*dev,

219 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

220 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate)

221{

222 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

223 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

224

225 if (api->[get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332) == NULL) {

226 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

227 }

228

229 return api->[get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332)(dev, sys, rate);

230}

231

[ 248](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)static inline int [clock\_control\_set\_rate](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)(const struct [device](structdevice.md) \*dev,

249 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

250 [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate)

251{

252 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

253 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

254

255 if (api->[set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c) == NULL) {

256 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

257 }

258

259 return api->[set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c)(dev, sys, rate);

260}

261

[ 284](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)static inline int [clock\_control\_configure](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)(const struct [device](structdevice.md) \*dev,

285 [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys,

286 void \*data)

287{

288 const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*api =

289 (const struct [clock\_control\_driver\_api](structclock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

290

291 if (api->[configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3) == NULL) {

292 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

293 }

294

295 return api->[configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3)(dev, sys, data);

296}

297

298#ifdef \_\_cplusplus

299}

300#endif

301

305

306#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[clock\_control\_get\_rate](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff)

static int clock\_control\_get\_rate(const struct device \*dev, clock\_control\_subsys\_t sys, uint32\_t \*rate)

Obtain the clock rate of given sub-system.

**Definition** clock\_control.h:218

[clock\_control\_async\_on](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf)

static int clock\_control\_async\_on(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_cb\_t cb, void \*user\_data)

Request clock to start with notification when clock has been started.

**Definition** clock\_control.h:170

[clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1)

void \* clock\_control\_subsys\_rate\_t

clock\_control\_subsys\_rate\_t is a type to identify a clock controller sub-system rate.

**Definition** clock\_control.h:66

[clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a)

enum clock\_control\_status(\* clock\_control\_get\_status\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys)

**Definition** clock\_control.h:90

[clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d)

int(\* clock\_control\_async\_on\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_cb\_t cb, void \*user\_data)

**Definition** clock\_control.h:85

[clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275)

void(\* clock\_control\_cb\_t)(const struct device \*dev, clock\_control\_subsys\_t subsys, void \*user\_data)

Callback called on clock started.

**Definition** clock\_control.h:74

[clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0)

int(\* clock\_control\_configure\_fn)(const struct device \*dev, clock\_control\_subsys\_t sys, void \*data)

**Definition** clock\_control.h:98

[clock\_control\_get\_status](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e)

static enum clock\_control\_status clock\_control\_get\_status(const struct device \*dev, clock\_control\_subsys\_t sys)

Get clock status.

**Definition** clock\_control.h:193

[clock\_control\_set\_rate](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614)

static int clock\_control\_set\_rate(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_subsys\_rate\_t rate)

Set the rate of the clock controlled by the device.

**Definition** clock\_control.h:248

[clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0)

int(\* clock\_control\_get)(const struct device \*dev, clock\_control\_subsys\_t sys, uint32\_t \*rate)

**Definition** clock\_control.h:81

[clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099)

int(\* clock\_control)(const struct device \*dev, clock\_control\_subsys\_t sys)

**Definition** clock\_control.h:78

[clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b)

int(\* clock\_control\_set)(const struct device \*dev, clock\_control\_subsys\_t sys, clock\_control\_subsys\_rate\_t rate)

**Definition** clock\_control.h:94

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:58

[clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09)

clock\_control\_status

Current clock status.

**Definition** clock\_control.h:46

[clock\_control\_off](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5)

static int clock\_control\_off(const struct device \*dev, clock\_control\_subsys\_t sys)

Disable a clock controlled by the device.

**Definition** clock\_control.h:144

[clock\_control\_on](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9)

static int clock\_control\_on(const struct device \*dev, clock\_control\_subsys\_t sys)

Enable a clock controlled by the device.

**Definition** clock\_control.h:125

[clock\_control\_configure](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06)

static int clock\_control\_configure(const struct device \*dev, clock\_control\_subsys\_t sys, void \*data)

Configure a source clock.

**Definition** clock\_control.h:284

[CLOCK\_CONTROL\_STATUS\_ON](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db)

@ CLOCK\_CONTROL\_STATUS\_ON

**Definition** clock\_control.h:49

[CLOCK\_CONTROL\_STATUS\_OFF](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa)

@ CLOCK\_CONTROL\_STATUS\_OFF

**Definition** clock\_control.h:48

[CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc)

@ CLOCK\_CONTROL\_STATUS\_UNKNOWN

**Definition** clock\_control.h:50

[CLOCK\_CONTROL\_STATUS\_STARTING](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52)

@ CLOCK\_CONTROL\_STATUS\_STARTING

**Definition** clock\_control.h:47

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[clock\_control\_driver\_api](structclock__control__driver__api.md)

**Definition** clock\_control.h:102

[clock\_control\_driver\_api::set\_rate](structclock__control__driver__api.md#a15e5eb98d0684a0afdb51f46d4e3fb5c)

clock\_control\_set set\_rate

**Definition** clock\_control.h:108

[clock\_control\_driver\_api::on](structclock__control__driver__api.md#a3b267856bdde2be0e679a9d1b16b3b4f)

clock\_control on

**Definition** clock\_control.h:103

[clock\_control\_driver\_api::get\_status](structclock__control__driver__api.md#a64461593304fad858b6d8f8292ef62f9)

clock\_control\_get\_status\_fn get\_status

**Definition** clock\_control.h:107

[clock\_control\_driver\_api::off](structclock__control__driver__api.md#a92385c0e0c7bbf8fe955ad2281b7ccc3)

clock\_control off

**Definition** clock\_control.h:104

[clock\_control\_driver\_api::async\_on](structclock__control__driver__api.md#a9a4a9a2ed1f0b80e48ee0f50469c72dc)

clock\_control\_async\_on\_fn async\_on

**Definition** clock\_control.h:105

[clock\_control\_driver\_api::get\_rate](structclock__control__driver__api.md#ab19c4aa8f48dfa33e8bce3189ea3c332)

clock\_control\_get get\_rate

**Definition** clock\_control.h:106

[clock\_control\_driver\_api::configure](structclock__control__driver__api.md#adfe1458a9b6fcca1c052ddfae1d311b3)

clock\_control\_configure\_fn configure

**Definition** clock\_control.h:109

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control.h](clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
