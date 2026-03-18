---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/blob_8h_source.html
original_path: doxygen/html/blob_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob.h

[Go to the documentation of this file.](blob_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_H\_\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

23

24#ifndef CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX

[ 25](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e)#define CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX 0

26#endif

27

[ 29](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618)enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) {

[ 31](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6) [BT\_MESH\_BLOB\_XFER\_MODE\_NONE](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6),

[ 33](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b) [BT\_MESH\_BLOB\_XFER\_MODE\_PUSH](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b),

[ 35](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd) [BT\_MESH\_BLOB\_XFER\_MODE\_PULL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd),

[ 37](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089) [BT\_MESH\_BLOB\_XFER\_MODE\_ALL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089),

38};

39

[ 41](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81)enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) {

[ 43](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600) [BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600),

[ 45](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9) [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9),

[ 47](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1) [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1),

[ 49](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581) [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581),

[ 51](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd) [BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd),

[ 53](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf) [BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf),

54};

55

[ 57](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d)enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) {

[ 59](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d) [BT\_MESH\_BLOB\_SUCCESS](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d),

[ 63](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e) [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e),

[ 68](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a) [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a),

[ 73](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009) [BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009),

[ 77](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa) [BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa),

[ 79](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0) [BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0),

[ 81](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b) [BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b),

[ 84](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f) [BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f),

[ 88](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768) [BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768),

[ 90](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb) [BT\_MESH\_BLOB\_ERR\_INTERNAL](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb),

[ 94](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1) [BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1),

95};

96

[ 98](structbt__mesh__blob__block.md)struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) {

[ 100](structbt__mesh__blob__block.md#a67632460e4a37407074105f8ff3f97fd) size\_t [size](structbt__mesh__blob__block.md#a67632460e4a37407074105f8ff3f97fd);

[ 102](structbt__mesh__blob__block.md#a7521b8121a2a1f280d14e9e222b7d6cf) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structbt__mesh__blob__block.md#a7521b8121a2a1f280d14e9e222b7d6cf);

[ 104](structbt__mesh__blob__block.md#a57f92c3b0ef68128d44a90802788dfa3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [number](structbt__mesh__blob__block.md#a57f92c3b0ef68128d44a90802788dfa3);

[ 106](structbt__mesh__blob__block.md#a6bd9a432a789edeafc5d425232a32b4e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_count](structbt__mesh__blob__block.md#a6bd9a432a789edeafc5d425232a32b4e);

[ 108](structbt__mesh__blob__block.md#accf9cb6d7d838a45284b28268f6e83c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [missing](structbt__mesh__blob__block.md#accf9cb6d7d838a45284b28268f6e83c8)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e),

109 8)];

110};

111

[ 113](structbt__mesh__blob__chunk.md)struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) {

[ 115](structbt__mesh__blob__chunk.md#aabd55d7c8acf726cbc3470af55cb6bc5) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structbt__mesh__blob__chunk.md#aabd55d7c8acf726cbc3470af55cb6bc5);

[ 117](structbt__mesh__blob__chunk.md#afd2be87f4cd91f29eb24ebd0dfd9bccb) size\_t [size](structbt__mesh__blob__chunk.md#afd2be87f4cd91f29eb24ebd0dfd9bccb);

[ 119](structbt__mesh__blob__chunk.md#ad6f5ff266346af1ab0ba29f5339cb83f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__mesh__blob__chunk.md#ad6f5ff266346af1ab0ba29f5339cb83f);

120};

121

[ 123](structbt__mesh__blob__xfer.md)struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) {

[ 125](structbt__mesh__blob__xfer.md#a9b4f37addd1271e26ab90c6e63608867) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [id](structbt__mesh__blob__xfer.md#a9b4f37addd1271e26ab90c6e63608867);

[ 127](structbt__mesh__blob__xfer.md#a7a2ca36b08d1d55c2dfbca0120a5274d) size\_t [size](structbt__mesh__blob__xfer.md#a7a2ca36b08d1d55c2dfbca0120a5274d);

[ 129](structbt__mesh__blob__xfer.md#a2c3d9365b5cb6e569d147acae7a74ed6) enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) [mode](structbt__mesh__blob__xfer.md#a2c3d9365b5cb6e569d147acae7a74ed6);

130 /\* Logarithmic representation of the block size. \*/

[ 131](structbt__mesh__blob__xfer.md#aa971742f85ccd94bbdef6c61203caeba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [block\_size\_log](structbt__mesh__blob__xfer.md#aa971742f85ccd94bbdef6c61203caeba);

[ 133](structbt__mesh__blob__xfer.md#a646c5c56d5290f6c65e2b9fca89e9835) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_size](structbt__mesh__blob__xfer.md#a646c5c56d5290f6c65e2b9fca89e9835);

134};

135

[ 137](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962)enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) {

[ 139](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a) [BT\_MESH\_BLOB\_READ](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a),

[ 141](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab) [BT\_MESH\_BLOB\_WRITE](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab),

142};

143

[ 145](structbt__mesh__blob__io.md)struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) {

[ 156](structbt__mesh__blob__io.md#a4666a3fafde0ee9fdd51d27732bec6bc) int (\*[open](structbt__mesh__blob__io.md#a4666a3fafde0ee9fdd51d27732bec6bc))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

157 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

158 enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) mode);

159

[ 167](structbt__mesh__blob__io.md#aac42902d0bbbef10a5e9cc35e8a3ea64) void (\*[close](structbt__mesh__blob__io.md#aac42902d0bbbef10a5e9cc35e8a3ea64))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

168 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer);

169

[ 181](structbt__mesh__blob__io.md#a900f049b6a778d9e0973ee66b46dc046) int (\*[block\_start](structbt__mesh__blob__io.md#a900f049b6a778d9e0973ee66b46dc046))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

182 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

183 const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block);

184

[ 195](structbt__mesh__blob__io.md#a57381249bf63924b2345ece6e12909cb) void (\*[block\_end](structbt__mesh__blob__io.md#a57381249bf63924b2345ece6e12909cb))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

196 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

197 const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block);

198

[ 225](structbt__mesh__blob__io.md#ae0b27ea814e5c939d708ae20d452ca09) int (\*[wr](structbt__mesh__blob__io.md#ae0b27ea814e5c939d708ae20d452ca09))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

226 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

227 const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block,

228 const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk);

229

[ 250](structbt__mesh__blob__io.md#a330ec5dcc8d18b84e7fdab9ef6d75f49) int (\*[rd](structbt__mesh__blob__io.md#a330ec5dcc8d18b84e7fdab9ef6d75f49))(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

251 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

252 const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block,

253 const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk);

254};

255

257

258#ifdef \_\_cplusplus

259}

260#endif

261

262#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_H\_\_ \*/

[bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962)

bt\_mesh\_blob\_io\_mode

BLOB stream interaction mode.

**Definition** blob.h:137

[bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81)

bt\_mesh\_blob\_xfer\_phase

Transfer phase.

**Definition** blob.h:41

[CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e)

#define CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX

**Definition** blob.h:25

[bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d)

bt\_mesh\_blob\_status

BLOB model status codes.

**Definition** blob.h:57

[bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618)

bt\_mesh\_blob\_xfer\_mode

BLOB transfer mode.

**Definition** blob.h:29

[BT\_MESH\_BLOB\_WRITE](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab)

@ BT\_MESH\_BLOB\_WRITE

Write data to the stream.

**Definition** blob.h:141

[BT\_MESH\_BLOB\_READ](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a)

@ BT\_MESH\_BLOB\_READ

Read data from the stream.

**Definition** blob.h:139

[BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK

The BLOB Transfer Server is waiting for the next block of data.

**Definition** blob.h:47

[BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE

The BLOB Transfer Server is awaiting configuration.

**Definition** blob.h:43

[BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START

The BLOB Transfer Server is ready to receive a BLOB transfer.

**Definition** blob.h:45

[BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED

The BLOB transfer is paused.

**Definition** blob.h:53

[BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE

The BLOB was transferred successfully.

**Definition** blob.h:51

[BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581)

@ BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK

The BLOB Transfer Server is waiting for the next chunk of data.

**Definition** blob.h:49

[BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f)

@ BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE

There is not enough space available in memory to receive the BLOB.

**Definition** blob.h:84

[BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)

@ BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE

The requested information cannot be provided while the server is in the current phase.

**Definition** blob.h:94

[BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b)

@ BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID

The message contains a BLOB ID value that is not expected.

**Definition** blob.h:81

[BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e)

@ BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM

The Block Number field value is not within the range of blocks being transferred.

**Definition** blob.h:63

[BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa)

@ BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE

The operation cannot be performed while the server is in the current phase.

**Definition** blob.h:77

[BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768)

@ BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE

The transfer mode is not supported by the BLOB Transfer Server model.

**Definition** blob.h:88

[BT\_MESH\_BLOB\_ERR\_INTERNAL](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb)

@ BT\_MESH\_BLOB\_ERR\_INTERNAL

An internal error occurred on the node.

**Definition** blob.h:90

[BT\_MESH\_BLOB\_SUCCESS](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)

@ BT\_MESH\_BLOB\_SUCCESS

The message was processed successfully.

**Definition** blob.h:59

[BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a)

@ BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE

The block size is smaller than the size indicated by the Min Block Size Log state or is larger than t...

**Definition** blob.h:68

[BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0)

@ BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM

A parameter value in the message cannot be accepted.

**Definition** blob.h:79

[BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009)

@ BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE

The chunk size exceeds the size indicated by the Max Chunk Size state, or the number of chunks exceed...

**Definition** blob.h:73

[BT\_MESH\_BLOB\_XFER\_MODE\_PUSH](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b)

@ BT\_MESH\_BLOB\_XFER\_MODE\_PUSH

Push mode (Push BLOB Transfer Mode).

**Definition** blob.h:33

[BT\_MESH\_BLOB\_XFER\_MODE\_ALL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089)

@ BT\_MESH\_BLOB\_XFER\_MODE\_ALL

Both modes are valid.

**Definition** blob.h:37

[BT\_MESH\_BLOB\_XFER\_MODE\_NONE](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6)

@ BT\_MESH\_BLOB\_XFER\_MODE\_NONE

No valid transfer mode.

**Definition** blob.h:31

[BT\_MESH\_BLOB\_XFER\_MODE\_PULL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd)

@ BT\_MESH\_BLOB\_XFER\_MODE\_PULL

Pull mode (Pull BLOB Transfer Mode).

**Definition** blob.h:35

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:336

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_blob\_block](structbt__mesh__blob__block.md)

BLOB transfer data block.

**Definition** blob.h:98

[bt\_mesh\_blob\_block::number](structbt__mesh__blob__block.md#a57f92c3b0ef68128d44a90802788dfa3)

uint16\_t number

Block number.

**Definition** blob.h:104

[bt\_mesh\_blob\_block::size](structbt__mesh__blob__block.md#a67632460e4a37407074105f8ff3f97fd)

size\_t size

Block size in bytes.

**Definition** blob.h:100

[bt\_mesh\_blob\_block::chunk\_count](structbt__mesh__blob__block.md#a6bd9a432a789edeafc5d425232a32b4e)

uint16\_t chunk\_count

Number of chunks in block.

**Definition** blob.h:106

[bt\_mesh\_blob\_block::offset](structbt__mesh__blob__block.md#a7521b8121a2a1f280d14e9e222b7d6cf)

off\_t offset

Offset in bytes from the start of the BLOB.

**Definition** blob.h:102

[bt\_mesh\_blob\_block::missing](structbt__mesh__blob__block.md#accf9cb6d7d838a45284b28268f6e83c8)

uint8\_t missing[DIV\_ROUND\_UP(0, 8)]

Bitmap of missing chunks.

**Definition** blob.h:109

[bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md)

BLOB data chunk.

**Definition** blob.h:113

[bt\_mesh\_blob\_chunk::offset](structbt__mesh__blob__chunk.md#aabd55d7c8acf726cbc3470af55cb6bc5)

off\_t offset

Offset of the chunk data from the start of the block.

**Definition** blob.h:115

[bt\_mesh\_blob\_chunk::data](structbt__mesh__blob__chunk.md#ad6f5ff266346af1ab0ba29f5339cb83f)

uint8\_t \* data

Chunk data.

**Definition** blob.h:119

[bt\_mesh\_blob\_chunk::size](structbt__mesh__blob__chunk.md#afd2be87f4cd91f29eb24ebd0dfd9bccb)

size\_t size

Chunk data size.

**Definition** blob.h:117

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_io::rd](structbt__mesh__blob__io.md#a330ec5dcc8d18b84e7fdab9ef6d75f49)

int(\* rd)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_block \*block, const struct bt\_mesh\_blob\_chunk \*chunk)

Chunk data read callback.

**Definition** blob.h:250

[bt\_mesh\_blob\_io::open](structbt__mesh__blob__io.md#a4666a3fafde0ee9fdd51d27732bec6bc)

int(\* open)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer, enum bt\_mesh\_blob\_io\_mode mode)

Open callback.

**Definition** blob.h:156

[bt\_mesh\_blob\_io::block\_end](structbt__mesh__blob__io.md#a57381249bf63924b2345ece6e12909cb)

void(\* block\_end)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_block \*block)

Block end callback.

**Definition** blob.h:195

[bt\_mesh\_blob\_io::block\_start](structbt__mesh__blob__io.md#a900f049b6a778d9e0973ee66b46dc046)

int(\* block\_start)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_block \*block)

Block start callback.

**Definition** blob.h:181

[bt\_mesh\_blob\_io::close](structbt__mesh__blob__io.md#aac42902d0bbbef10a5e9cc35e8a3ea64)

void(\* close)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer)

Close callback.

**Definition** blob.h:167

[bt\_mesh\_blob\_io::wr](structbt__mesh__blob__io.md#ae0b27ea814e5c939d708ae20d452ca09)

int(\* wr)(const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_block \*block, const struct bt\_mesh\_blob\_chunk \*chunk)

Chunk data write callback.

**Definition** blob.h:225

[bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)

BLOB transfer.

**Definition** blob.h:123

[bt\_mesh\_blob\_xfer::mode](structbt__mesh__blob__xfer.md#a2c3d9365b5cb6e569d147acae7a74ed6)

enum bt\_mesh\_blob\_xfer\_mode mode

BLOB transfer mode.

**Definition** blob.h:129

[bt\_mesh\_blob\_xfer::chunk\_size](structbt__mesh__blob__xfer.md#a646c5c56d5290f6c65e2b9fca89e9835)

uint16\_t chunk\_size

Base chunk size.

**Definition** blob.h:133

[bt\_mesh\_blob\_xfer::size](structbt__mesh__blob__xfer.md#a7a2ca36b08d1d55c2dfbca0120a5274d)

size\_t size

Total BLOB size in bytes.

**Definition** blob.h:127

[bt\_mesh\_blob\_xfer::id](structbt__mesh__blob__xfer.md#a9b4f37addd1271e26ab90c6e63608867)

uint64\_t id

BLOB ID.

**Definition** blob.h:125

[bt\_mesh\_blob\_xfer::block\_size\_log](structbt__mesh__blob__xfer.md#aa971742f85ccd94bbdef6c61203caeba)

uint8\_t block\_size\_log

**Definition** blob.h:131

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob.h](blob_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
