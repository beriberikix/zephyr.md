---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cts_8h_source.html
original_path: doxygen/html/cts_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cts.h

[Go to the documentation of this file.](cts_8h.md)

1/\*

2 \* Copyright (c) 2024 Croxel Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_CTS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_CTS\_H\_

9

17

18#include <[stdint.h](stdint_8h.md)>

19#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 28](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7)enum [bt\_cts\_update\_reason](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7) {

29 /\* Unknown reason of update no bit is set \*/

[ 30](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309) [BT\_CTS\_UPDATE\_REASON\_UNKNOWN](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309) = 0,

31 /\* When time is changed manually e.g. through UI \*/

[ 32](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83) [BT\_CTS\_UPDATE\_REASON\_MANUAL](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

33 /\* If time is changed through external reference \*/

[ 34](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a) [BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

35 /\* time changed due to timezone adjust \*/

[ 36](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f) [BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

37 /\* time changed due to dst offset change \*/

[ 38](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c) [BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

39};

40

[ 45](structbt__cts__time__format.md)struct [bt\_cts\_time\_format](structbt__cts__time__format.md) {

[ 46](structbt__cts__time__format.md#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [year](structbt__cts__time__format.md#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e);

[ 47](structbt__cts__time__format.md#a079a1c49698b6e9cb84291acdd1cf687) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mon](structbt__cts__time__format.md#a079a1c49698b6e9cb84291acdd1cf687);

[ 48](structbt__cts__time__format.md#a408a2b777d10b536dbdfeca1b8335e6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mday](structbt__cts__time__format.md#a408a2b777d10b536dbdfeca1b8335e6b);

[ 49](structbt__cts__time__format.md#ab592c89e81e5cb43724affd3ce2b5768) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hours](structbt__cts__time__format.md#ab592c89e81e5cb43724affd3ce2b5768);

[ 50](structbt__cts__time__format.md#a299d6432d9b44b0de0be9c130733eb69) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min](structbt__cts__time__format.md#a299d6432d9b44b0de0be9c130733eb69);

[ 51](structbt__cts__time__format.md#ae0ccd07b2a280888f3881f0d2fc2add6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec](structbt__cts__time__format.md#ae0ccd07b2a280888f3881f0d2fc2add6);

[ 52](structbt__cts__time__format.md#ae696cbbd3a785c1df6d54ce771f1d7a2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wday](structbt__cts__time__format.md#ae696cbbd3a785c1df6d54ce771f1d7a2);

[ 53](structbt__cts__time__format.md#af601779a164440fe95c0dcbd7a3d7e60) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fractions256](structbt__cts__time__format.md#af601779a164440fe95c0dcbd7a3d7e60);

[ 54](structbt__cts__time__format.md#a3482e00650e9e9a63816709c82a1aa07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__cts__time__format.md#a3482e00650e9e9a63816709c82a1aa07);

55} \_\_packed;

56

[ 58](structbt__cts__cb.md)struct [bt\_cts\_cb](structbt__cts__cb.md) {

[ 63](structbt__cts__cb.md#accf7eb6620ae0f4b9693d238ecdde5b3) void (\*[notification\_changed](structbt__cts__cb.md#accf7eb6620ae0f4b9693d238ecdde5b3))(bool enabled);

64

[ 75](structbt__cts__cb.md#a1dd6b251b07537e81c010f654721cbf4) int (\*[cts\_time\_write](structbt__cts__cb.md#a1dd6b251b07537e81c010f654721cbf4))(struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time);

76

[ 89](structbt__cts__cb.md#ae4a374f95870bfa21b8c1d87e832fe48) int (\*[fill\_current\_cts\_time](structbt__cts__cb.md#ae4a374f95870bfa21b8c1d87e832fe48))(struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time);

90};

91

[ 101](group__bt__cts.md#ga26e1e7bb9fcd4d723cdc3458743da5a0)int [bt\_cts\_init](group__bt__cts.md#ga26e1e7bb9fcd4d723cdc3458743da5a0)(const struct [bt\_cts\_cb](structbt__cts__cb.md) \*cb);

102

[ 112](group__bt__cts.md#ga0a1eac245cf4b9d0dd07cfe45f133513)int [bt\_cts\_send\_notification](group__bt__cts.md#ga0a1eac245cf4b9d0dd07cfe45f133513)(enum [bt\_cts\_update\_reason](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7) [reason](structbt__cts__time__format.md#a3482e00650e9e9a63816709c82a1aa07));

113

[ 125](group__bt__cts.md#ga07893fdc07e448608cde663f3a54d587)int [bt\_cts\_time\_to\_unix\_ms](group__bt__cts.md#ga07893fdc07e448608cde663f3a54d587)(const struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*unix\_ms);

126

[ 138](group__bt__cts.md#ga90e1e2859695731b0213fe3dda4c5e52)int [bt\_cts\_time\_from\_unix\_ms](group__bt__cts.md#ga90e1e2859695731b0213fe3dda4c5e52)(struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) unix\_ms);

139

140#ifdef \_\_cplusplus

141}

142#endif

143

147

148#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_CTS\_H\_ \*/

[bt\_cts\_time\_to\_unix\_ms](group__bt__cts.md#ga07893fdc07e448608cde663f3a54d587)

int bt\_cts\_time\_to\_unix\_ms(const struct bt\_cts\_time\_format \*ct\_time, int64\_t \*unix\_ms)

Helper API to decode CTS formatted time into milliseconds since epoch.

[bt\_cts\_send\_notification](group__bt__cts.md#ga0a1eac245cf4b9d0dd07cfe45f133513)

int bt\_cts\_send\_notification(enum bt\_cts\_update\_reason reason)

Notify all connected clients that have enabled the current time update notification.

[bt\_cts\_init](group__bt__cts.md#ga26e1e7bb9fcd4d723cdc3458743da5a0)

int bt\_cts\_init(const struct bt\_cts\_cb \*cb)

This API should be called at application init.

[bt\_cts\_time\_from\_unix\_ms](group__bt__cts.md#ga90e1e2859695731b0213fe3dda4c5e52)

int bt\_cts\_time\_from\_unix\_ms(struct bt\_cts\_time\_format \*ct\_time, int64\_t unix\_ms)

Helper API to encode milliseconds since epoch to CTS formatted time.

[bt\_cts\_update\_reason](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7)

bt\_cts\_update\_reason

CTS time update reason bits as defined in the specification.

**Definition** cts.h:28

[BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f)

@ BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE

**Definition** cts.h:36

[BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a)

@ BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF

**Definition** cts.h:34

[BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c)

@ BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING

**Definition** cts.h:38

[BT\_CTS\_UPDATE\_REASON\_UNKNOWN](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309)

@ BT\_CTS\_UPDATE\_REASON\_UNKNOWN

**Definition** cts.h:30

[BT\_CTS\_UPDATE\_REASON\_MANUAL](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83)

@ BT\_CTS\_UPDATE\_REASON\_MANUAL

**Definition** cts.h:32

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[time.h](include_2zephyr_2posix_2time_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[bt\_cts\_cb](structbt__cts__cb.md)

Current Time Service callback structure.

**Definition** cts.h:58

[bt\_cts\_cb::cts\_time\_write](structbt__cts__cb.md#a1dd6b251b07537e81c010f654721cbf4)

int(\* cts\_time\_write)(struct bt\_cts\_time\_format \*cts\_time)

The Current Time has been updated by a peer.

**Definition** cts.h:75

[bt\_cts\_cb::notification\_changed](structbt__cts__cb.md#accf7eb6620ae0f4b9693d238ecdde5b3)

void(\* notification\_changed)(bool enabled)

Current Time Service notifications changed.

**Definition** cts.h:63

[bt\_cts\_cb::fill\_current\_cts\_time](structbt__cts__cb.md#ae4a374f95870bfa21b8c1d87e832fe48)

int(\* fill\_current\_cts\_time)(struct bt\_cts\_time\_format \*cts\_time)

When current time Read request or notification is triggered, CTS uses this callback to retrieve curre...

**Definition** cts.h:89

[bt\_cts\_time\_format](structbt__cts__time__format.md)

Current Time service data format, Please refer to specifications for more details.

**Definition** cts.h:45

[bt\_cts\_time\_format::mon](structbt__cts__time__format.md#a079a1c49698b6e9cb84291acdd1cf687)

uint8\_t mon

**Definition** cts.h:47

[bt\_cts\_time\_format::min](structbt__cts__time__format.md#a299d6432d9b44b0de0be9c130733eb69)

uint8\_t min

**Definition** cts.h:50

[bt\_cts\_time\_format::reason](structbt__cts__time__format.md#a3482e00650e9e9a63816709c82a1aa07)

uint8\_t reason

**Definition** cts.h:54

[bt\_cts\_time\_format::mday](structbt__cts__time__format.md#a408a2b777d10b536dbdfeca1b8335e6b)

uint8\_t mday

**Definition** cts.h:48

[bt\_cts\_time\_format::hours](structbt__cts__time__format.md#ab592c89e81e5cb43724affd3ce2b5768)

uint8\_t hours

**Definition** cts.h:49

[bt\_cts\_time\_format::year](structbt__cts__time__format.md#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e)

uint16\_t year

**Definition** cts.h:46

[bt\_cts\_time\_format::sec](structbt__cts__time__format.md#ae0ccd07b2a280888f3881f0d2fc2add6)

uint8\_t sec

**Definition** cts.h:51

[bt\_cts\_time\_format::wday](structbt__cts__time__format.md#ae696cbbd3a785c1df6d54ce771f1d7a2)

uint8\_t wday

**Definition** cts.h:52

[bt\_cts\_time\_format::fractions256](structbt__cts__time__format.md#af601779a164440fe95c0dcbd7a3d7e60)

uint8\_t fractions256

**Definition** cts.h:53

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [cts.h](cts_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
