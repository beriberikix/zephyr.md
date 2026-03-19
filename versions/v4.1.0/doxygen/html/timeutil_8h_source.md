---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/timeutil_8h_source.html
original_path: doxygen/html/timeutil_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil.h

[Go to the documentation of this file.](timeutil_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

20

21#ifndef ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_

22#define ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_

23

24#include <time.h>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

39

40/\* Base Year value use in calculations in "timeutil\_timegm64" API \*/

[ 41](group__timeutil__repr__apis.md#gaa61359e3ffe7df1994a9265a66834385)#define TIME\_UTILS\_BASE\_YEAR 1900

42

[ 52](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [timeutil\_timegm64](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)(const struct [tm](structtm.md) \*[tm](structtm.md));

53

65[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) timeutil\_timegm(const struct [tm](structtm.md) \*[tm](structtm.md));

66

73

[ 86](structtimeutil__sync__config.md)struct [timeutil\_sync\_config](structtimeutil__sync__config.md) {

[ 94](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ref\_Hz](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7);

95

[ 107](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [local\_Hz](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f);

108};

109

[ 117](structtimeutil__sync__instant.md)struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) {

[ 123](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201);

124

[ 129](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337);

130};

131

[ 142](structtimeutil__sync__state.md)struct [timeutil\_sync\_state](structtimeutil__sync__state.md) {

[ 144](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96) const struct [timeutil\_sync\_config](structtimeutil__sync__config.md) \*[cfg](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96);

145

[ 147](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99) struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) [base](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99);

148

[ 153](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8) struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) [latest](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8);

154

[ 170](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3) float [skew](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3);

171};

172

[ 190](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)int [timeutil\_sync\_state\_update](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)(struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

191 const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*inst);

192

[ 217](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)int [timeutil\_sync\_state\_set\_skew](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)(struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, float skew,

218 const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*base);

219

[ 233](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)float [timeutil\_sync\_estimate\_skew](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp);

234

[ 257](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)int [timeutil\_sync\_ref\_from\_local](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

258 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*refp);

259

[ 281](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)int [timeutil\_sync\_local\_from\_ref](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

282 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201), [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*localp);

283

[ 302](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [timeutil\_sync\_skew\_to\_ppb](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)(float skew);

303

304#ifdef \_\_cplusplus

305}

306#endif

307

311

312#endif /\* ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[timeutil\_timegm64](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)

int64\_t timeutil\_timegm64(const struct tm \*tm)

Convert broken-down time to a POSIX epoch offset in seconds.

[timeutil\_sync\_state\_set\_skew](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)

int timeutil\_sync\_state\_set\_skew(struct timeutil\_sync\_state \*tsp, float skew, const struct timeutil\_sync\_instant \*base)

Update the state with a new skew and possibly base value.

[timeutil\_sync\_ref\_from\_local](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)

int timeutil\_sync\_ref\_from\_local(const struct timeutil\_sync\_state \*tsp, uint64\_t local, uint64\_t \*refp)

Interpolate a reference timescale instant from a local instant.

[timeutil\_sync\_state\_update](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)

int timeutil\_sync\_state\_update(struct timeutil\_sync\_state \*tsp, const struct timeutil\_sync\_instant \*inst)

Record a new instant in the time synchronization state.

[timeutil\_sync\_skew\_to\_ppb](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)

int32\_t timeutil\_sync\_skew\_to\_ppb(float skew)

Convert from a skew to an error in parts-per-billion.

[timeutil\_sync\_estimate\_skew](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)

float timeutil\_sync\_estimate\_skew(const struct timeutil\_sync\_state \*tsp)

Estimate the skew based on current state.

[timeutil\_sync\_local\_from\_ref](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)

int timeutil\_sync\_local\_from\_ref(const struct timeutil\_sync\_state \*tsp, uint64\_t ref, int64\_t \*localp)

Interpolate a local timescale instant from a reference instant.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[timeutil\_sync\_config](structtimeutil__sync__config.md)

Immutable state for synchronizing two clocks.

**Definition** timeutil.h:86

[timeutil\_sync\_config::ref\_Hz](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7)

uint32\_t ref\_Hz

The nominal instance counter rate in Hz.

**Definition** timeutil.h:94

[timeutil\_sync\_config::local\_Hz](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f)

uint32\_t local\_Hz

The nominal local counter rate in Hz.

**Definition** timeutil.h:107

[timeutil\_sync\_instant](structtimeutil__sync__instant.md)

Representation of an instant in two time scales.

**Definition** timeutil.h:117

[timeutil\_sync\_instant::ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201)

uint64\_t ref

An instant in the reference time scale.

**Definition** timeutil.h:123

[timeutil\_sync\_instant::local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337)

uint64\_t local

The corresponding instance in the local time scale.

**Definition** timeutil.h:129

[timeutil\_sync\_state](structtimeutil__sync__state.md)

State required to convert instants between time scales.

**Definition** timeutil.h:142

[timeutil\_sync\_state::cfg](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96)

const struct timeutil\_sync\_config \* cfg

Pointer to reference and local rate information.

**Definition** timeutil.h:144

[timeutil\_sync\_state::skew](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3)

float skew

The scale factor used to correct for clock skew.

**Definition** timeutil.h:170

[timeutil\_sync\_state::latest](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8)

struct timeutil\_sync\_instant latest

The most recent instant in both time scales.

**Definition** timeutil.h:153

[timeutil\_sync\_state::base](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99)

struct timeutil\_sync\_instant base

The base instant in both time scales.

**Definition** timeutil.h:147

[tm](structtm.md)

**Definition** time.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [timeutil.h](timeutil_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
