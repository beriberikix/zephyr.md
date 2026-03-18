---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/img__mgmt__client_8h_source.html
original_path: doxygen/html/img__mgmt__client_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_client.h

[Go to the documentation of this file.](img__mgmt__client_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_IMG\_MGMT\_CLIENT\_

8#define H\_IMG\_MGMT\_CLIENT\_

9

10#include <[inttypes.h](inttypes_8h.md)>

11#include <[zephyr/mgmt/mcumgr/grp/img\_mgmt/img\_mgmt.h](img__mgmt_8h.md)>

12#include <[zephyr/mgmt/mcumgr/smp/smp\_client.h](smp__client_8h.md)>

13

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 28](structmcumgr__image__list__flags.md)struct [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md) {

[ 30](structmcumgr__image__list__flags.md#acb12d5ae0c75e9dac48874e542784bd3) bool [bootable](structmcumgr__image__list__flags.md#acb12d5ae0c75e9dac48874e542784bd3): 1;

[ 32](structmcumgr__image__list__flags.md#a744597f98d3092de161512d0817bb1a2) bool [pending](structmcumgr__image__list__flags.md#a744597f98d3092de161512d0817bb1a2): 1;

[ 34](structmcumgr__image__list__flags.md#ad3ff9c0acbcf2ebbb5f6820b38705bff) bool [confirmed](structmcumgr__image__list__flags.md#ad3ff9c0acbcf2ebbb5f6820b38705bff): 1;

[ 36](structmcumgr__image__list__flags.md#ade2a01aeeede96070bcdf33ce2d949fb) bool [active](structmcumgr__image__list__flags.md#ade2a01aeeede96070bcdf33ce2d949fb): 1;

[ 38](structmcumgr__image__list__flags.md#af7c7b565ef02ea95c7486949a29164c1) bool [permanent](structmcumgr__image__list__flags.md#af7c7b565ef02ea95c7486949a29164c1): 1;

39};

40

[ 44](structmcumgr__image__data.md)struct [mcumgr\_image\_data](structmcumgr__image__data.md) {

[ 46](structmcumgr__image__data.md#a713cff86339e08b2f74b564dca4c521e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [slot\_num](structmcumgr__image__data.md#a713cff86339e08b2f74b564dca4c521e);

[ 48](structmcumgr__image__data.md#ac394e1e5a0e0425b27926a3405d8bb2d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [img\_num](structmcumgr__image__data.md#ac394e1e5a0e0425b27926a3405d8bb2d);

[ 50](structmcumgr__image__data.md#a96a8216a5faa7095cec5907ef2117a41) char [hash](structmcumgr__image__data.md#a96a8216a5faa7095cec5907ef2117a41)[[IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)];

[ 52](structmcumgr__image__data.md#aa75e38d37c9b12a2ccf32af6a47df814) char [version](structmcumgr__image__data.md#aa75e38d37c9b12a2ccf32af6a47df814)[[IMG\_MGMT\_VER\_MAX\_STR\_LEN](group__mcumgr__img__mgmt.md#ga57a5c429be5a3860981007e9728db181) + 1];

[ 54](structmcumgr__image__data.md#a24f83149d88a3709b4f58bc72ee932be) struct [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md) [flags](structmcumgr__image__data.md#a24f83149d88a3709b4f58bc72ee932be);

55};

56

[ 60](structmcumgr__image__state.md)struct [mcumgr\_image\_state](structmcumgr__image__state.md) {

[ 62](structmcumgr__image__state.md#a4ec39c59f3cfe789dabf7fc361ff86ac) enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) [status](structmcumgr__image__state.md#a4ec39c59f3cfe789dabf7fc361ff86ac);

[ 64](structmcumgr__image__state.md#afd36103c373d709733ee928326c50343) int [image\_list\_length](structmcumgr__image__state.md#afd36103c373d709733ee928326c50343);

[ 66](structmcumgr__image__state.md#af7bd52b3a18ad190e0159c5e928b857e) struct [mcumgr\_image\_data](structmcumgr__image__data.md) \*[image\_list](structmcumgr__image__state.md#af7bd52b3a18ad190e0159c5e928b857e);

67};

68

[ 72](structmcumgr__image__upload.md)struct [mcumgr\_image\_upload](structmcumgr__image__upload.md) {

[ 74](structmcumgr__image__upload.md#a5522d2958df295c72fd00212155c7eee) enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) [status](structmcumgr__image__upload.md#a5522d2958df295c72fd00212155c7eee);

[ 76](structmcumgr__image__upload.md#ade29d2b559d9709b7372874e993e267c) size\_t [image\_upload\_offset](structmcumgr__image__upload.md#ade29d2b559d9709b7372874e993e267c);

77};

78

[ 84](structimg__gr__upload.md)struct [img\_gr\_upload](structimg__gr__upload.md) {

[ 86](structimg__gr__upload.md#a773dfcf2f4ceccb771020f29f2e44c92) char [sha256](structimg__gr__upload.md#a773dfcf2f4ceccb771020f29f2e44c92)[[IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)];

[ 88](structimg__gr__upload.md#af71ec58c3a2c39e1549c41f7692b1319) bool [hash\_initialized](structimg__gr__upload.md#af71ec58c3a2c39e1549c41f7692b1319);

[ 90](structimg__gr__upload.md#a093b1897e492545ab5b92d91bde727fb) size\_t [image\_size](structimg__gr__upload.md#a093b1897e492545ab5b92d91bde727fb);

[ 92](structimg__gr__upload.md#a71736f17ef73d50d0e61049d356e2ce2) size\_t [offset](structimg__gr__upload.md#a71736f17ef73d50d0e61049d356e2ce2);

[ 94](structimg__gr__upload.md#ae5245e6622c991cbd207b3f69f7548f3) size\_t [upload\_header\_size](structimg__gr__upload.md#ae5245e6622c991cbd207b3f69f7548f3);

[ 96](structimg__gr__upload.md#a457e54010e9980b96bc970f6d43bd127) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [image\_num](structimg__gr__upload.md#a457e54010e9980b96bc970f6d43bd127);

97};

98

[ 102](structimg__mgmt__client.md)struct [img\_mgmt\_client](structimg__mgmt__client.md) {

[ 104](structimg__mgmt__client.md#a36abd266bbd1ea35849423708f9e816d) struct [smp\_client\_object](structsmp__client__object.md) \*[smp\_client](structimg__mgmt__client.md#a36abd266bbd1ea35849423708f9e816d);

[ 106](structimg__mgmt__client.md#a77559218adc5f7873366c56f9a02750e) struct [img\_gr\_upload](structimg__gr__upload.md) [upload](structimg__mgmt__client.md#a77559218adc5f7873366c56f9a02750e);

[ 108](structimg__mgmt__client.md#a2a2097f05111d6242d623a68959ecca9) int [image\_list\_length](structimg__mgmt__client.md#a2a2097f05111d6242d623a68959ecca9);

[ 110](structimg__mgmt__client.md#a654c94fafac9cd72465a413de8266005) struct [mcumgr\_image\_data](structmcumgr__image__data.md) \*[image\_list](structimg__mgmt__client.md#a654c94fafac9cd72465a413de8266005);

[ 112](structimg__mgmt__client.md#a4fb8d168a6faf48c32903b71fc8c8097) int [status](structimg__mgmt__client.md#a4fb8d168a6faf48c32903b71fc8c8097);

113};

114

[ 126](group__mcumgr__img__mgmt__client.md#ga1c21618818b5b058e28bdd32360e3838)void [img\_mgmt\_client\_init](group__mcumgr__img__mgmt__client.md#ga1c21618818b5b058e28bdd32360e3838)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client,

127 int image\_list\_size, struct [mcumgr\_image\_data](structmcumgr__image__data.md) \*image\_list);

128

[ 141](group__mcumgr__img__mgmt__client.md#ga99dccccacad33c5e7f91043b483a3884)int [img\_mgmt\_client\_upload\_init](group__mcumgr__img__mgmt__client.md#ga99dccccacad33c5e7f91043b483a3884)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, size\_t image\_size,

142 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) image\_num, const char \*image\_hash);

143

[ 155](group__mcumgr__img__mgmt__client.md#ga55fddd1f53765ce25e4285e45714ebc1)int [img\_mgmt\_client\_upload](group__mcumgr__img__mgmt__client.md#ga55fddd1f53765ce25e4285e45714ebc1)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t length,

156 struct [mcumgr\_image\_upload](structmcumgr__image__upload.md) \*res\_buf);

157

169

[ 170](group__mcumgr__img__mgmt__client.md#gabb1cbc805d8f7e2d8ab94f063f29f9ac)int [img\_mgmt\_client\_state\_write](group__mcumgr__img__mgmt__client.md#gabb1cbc805d8f7e2d8ab94f063f29f9ac)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, char \*[hash](structmcumgr__image__data.md#a96a8216a5faa7095cec5907ef2117a41), bool confirm,

171 struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf);

172

[ 182](group__mcumgr__img__mgmt__client.md#gad1937b33597ddd012fc7d1fd04cf17f8)int [img\_mgmt\_client\_state\_read](group__mcumgr__img__mgmt__client.md#gad1937b33597ddd012fc7d1fd04cf17f8)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf);

183

193

[ 194](group__mcumgr__img__mgmt__client.md#ga27ca742a8fc5fc3a96510d73fa85a7a3)int [img\_mgmt\_client\_erase](group__mcumgr__img__mgmt__client.md#ga27ca742a8fc5fc3a96510d73fa85a7a3)(struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) slot);

195

199

200#ifdef \_\_cplusplus

201}

202#endif

203

204#endif /\* H\_IMG\_MGMT\_CLIENT\_ \*/

[img\_mgmt\_client\_init](group__mcumgr__img__mgmt__client.md#ga1c21618818b5b058e28bdd32360e3838)

void img\_mgmt\_client\_init(struct img\_mgmt\_client \*client, struct smp\_client\_object \*smp\_client, int image\_list\_size, struct mcumgr\_image\_data \*image\_list)

Inilialize image group client.

[img\_mgmt\_client\_erase](group__mcumgr__img__mgmt__client.md#ga27ca742a8fc5fc3a96510d73fa85a7a3)

int img\_mgmt\_client\_erase(struct img\_mgmt\_client \*client, uint32\_t slot)

Erase selected Image Slot.

[img\_mgmt\_client\_upload](group__mcumgr__img__mgmt__client.md#ga55fddd1f53765ce25e4285e45714ebc1)

int img\_mgmt\_client\_upload(struct img\_mgmt\_client \*client, const uint8\_t \*data, size\_t length, struct mcumgr\_image\_upload \*res\_buf)

Upload part of image.

[img\_mgmt\_client\_upload\_init](group__mcumgr__img__mgmt__client.md#ga99dccccacad33c5e7f91043b483a3884)

int img\_mgmt\_client\_upload\_init(struct img\_mgmt\_client \*client, size\_t image\_size, uint32\_t image\_num, const char \*image\_hash)

Initialize image upload.

[img\_mgmt\_client\_state\_write](group__mcumgr__img__mgmt__client.md#gabb1cbc805d8f7e2d8ab94f063f29f9ac)

int img\_mgmt\_client\_state\_write(struct img\_mgmt\_client \*client, char \*hash, bool confirm, struct mcumgr\_image\_state \*res\_buf)

Write image state.

[img\_mgmt\_client\_state\_read](group__mcumgr__img__mgmt__client.md#gad1937b33597ddd012fc7d1fd04cf17f8)

int img\_mgmt\_client\_state\_read(struct img\_mgmt\_client \*client, struct mcumgr\_image\_state \*res\_buf)

Read image state.

[IMG\_MGMT\_VER\_MAX\_STR\_LEN](group__mcumgr__img__mgmt.md#ga57a5c429be5a3860981007e9728db181)

#define IMG\_MGMT\_VER\_MAX\_STR\_LEN

**Definition** img\_mgmt.h:39

[IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)

#define IMG\_MGMT\_DATA\_SHA\_LEN

**Definition** img\_mgmt.h:28

[mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5)

mcumgr\_err\_t

MCUmgr error codes.

**Definition** mgmt\_defines.h:93

[img\_mgmt.h](img__mgmt_8h.md)

[inttypes.h](inttypes_8h.md)

[smp\_client.h](smp__client_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[img\_gr\_upload](structimg__gr__upload.md)

IMG mgmt client upload structure.

**Definition** img\_mgmt\_client.h:84

[img\_gr\_upload::image\_size](structimg__gr__upload.md#a093b1897e492545ab5b92d91bde727fb)

size\_t image\_size

Image size.

**Definition** img\_mgmt\_client.h:90

[img\_gr\_upload::image\_num](structimg__gr__upload.md#a457e54010e9980b96bc970f6d43bd127)

uint32\_t image\_num

Image slot num.

**Definition** img\_mgmt\_client.h:96

[img\_gr\_upload::offset](structimg__gr__upload.md#a71736f17ef73d50d0e61049d356e2ce2)

size\_t offset

Image upload offset state.

**Definition** img\_mgmt\_client.h:92

[img\_gr\_upload::sha256](structimg__gr__upload.md#a773dfcf2f4ceccb771020f29f2e44c92)

char sha256[32]

Image 256-bit hash.

**Definition** img\_mgmt\_client.h:86

[img\_gr\_upload::upload\_header\_size](structimg__gr__upload.md#ae5245e6622c991cbd207b3f69f7548f3)

size\_t upload\_header\_size

Worst case init upload message size.

**Definition** img\_mgmt\_client.h:94

[img\_gr\_upload::hash\_initialized](structimg__gr__upload.md#af71ec58c3a2c39e1549c41f7692b1319)

bool hash\_initialized

True when Hash is configured, false when not.

**Definition** img\_mgmt\_client.h:88

[img\_mgmt\_client](structimg__mgmt__client.md)

IMG mgmt client object.

**Definition** img\_mgmt\_client.h:102

[img\_mgmt\_client::image\_list\_length](structimg__mgmt__client.md#a2a2097f05111d6242d623a68959ecca9)

int image\_list\_length

Client image list buffer size.

**Definition** img\_mgmt\_client.h:108

[img\_mgmt\_client::smp\_client](structimg__mgmt__client.md#a36abd266bbd1ea35849423708f9e816d)

struct smp\_client\_object \* smp\_client

SMP client object.

**Definition** img\_mgmt\_client.h:104

[img\_mgmt\_client::status](structimg__mgmt__client.md#a4fb8d168a6faf48c32903b71fc8c8097)

int status

Command status.

**Definition** img\_mgmt\_client.h:112

[img\_mgmt\_client::image\_list](structimg__mgmt__client.md#a654c94fafac9cd72465a413de8266005)

struct mcumgr\_image\_data \* image\_list

Image list buffer.

**Definition** img\_mgmt\_client.h:110

[img\_mgmt\_client::upload](structimg__mgmt__client.md#a77559218adc5f7873366c56f9a02750e)

struct img\_gr\_upload upload

Image Upload state data for client internal use.

**Definition** img\_mgmt\_client.h:106

[mcumgr\_image\_data](structmcumgr__image__data.md)

Image list data.

**Definition** img\_mgmt\_client.h:44

[mcumgr\_image\_data::flags](structmcumgr__image__data.md#a24f83149d88a3709b4f58bc72ee932be)

struct mcumgr\_image\_list\_flags flags

Image Flags.

**Definition** img\_mgmt\_client.h:54

[mcumgr\_image\_data::slot\_num](structmcumgr__image__data.md#a713cff86339e08b2f74b564dca4c521e)

uint32\_t slot\_num

Image slot num.

**Definition** img\_mgmt\_client.h:46

[mcumgr\_image\_data::hash](structmcumgr__image__data.md#a96a8216a5faa7095cec5907ef2117a41)

char hash[32]

Image SHA256 checksum.

**Definition** img\_mgmt\_client.h:50

[mcumgr\_image\_data::version](structmcumgr__image__data.md#aa75e38d37c9b12a2ccf32af6a47df814)

char version[(sizeof("255.255.65535.4294967295"))+1]

Image Version.

**Definition** img\_mgmt\_client.h:52

[mcumgr\_image\_data::img\_num](structmcumgr__image__data.md#ac394e1e5a0e0425b27926a3405d8bb2d)

uint32\_t img\_num

Image number.

**Definition** img\_mgmt\_client.h:48

[mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md)

Image list flags.

**Definition** img\_mgmt\_client.h:28

[mcumgr\_image\_list\_flags::pending](structmcumgr__image__list__flags.md#a744597f98d3092de161512d0817bb1a2)

bool pending

Pending update state.

**Definition** img\_mgmt\_client.h:32

[mcumgr\_image\_list\_flags::bootable](structmcumgr__image__list__flags.md#acb12d5ae0c75e9dac48874e542784bd3)

bool bootable

Bootable image.

**Definition** img\_mgmt\_client.h:30

[mcumgr\_image\_list\_flags::confirmed](structmcumgr__image__list__flags.md#ad3ff9c0acbcf2ebbb5f6820b38705bff)

bool confirmed

Confirmed image.

**Definition** img\_mgmt\_client.h:34

[mcumgr\_image\_list\_flags::active](structmcumgr__image__list__flags.md#ade2a01aeeede96070bcdf33ce2d949fb)

bool active

Active image.

**Definition** img\_mgmt\_client.h:36

[mcumgr\_image\_list\_flags::permanent](structmcumgr__image__list__flags.md#af7c7b565ef02ea95c7486949a29164c1)

bool permanent

Permanent image state.

**Definition** img\_mgmt\_client.h:38

[mcumgr\_image\_state](structmcumgr__image__state.md)

MCUmgr Image list response.

**Definition** img\_mgmt\_client.h:60

[mcumgr\_image\_state::status](structmcumgr__image__state.md#a4ec39c59f3cfe789dabf7fc361ff86ac)

enum mcumgr\_err\_t status

Status.

**Definition** img\_mgmt\_client.h:62

[mcumgr\_image\_state::image\_list](structmcumgr__image__state.md#af7bd52b3a18ad190e0159c5e928b857e)

struct mcumgr\_image\_data \* image\_list

Image list pointer.

**Definition** img\_mgmt\_client.h:66

[mcumgr\_image\_state::image\_list\_length](structmcumgr__image__state.md#afd36103c373d709733ee928326c50343)

int image\_list\_length

Length of image\_list.

**Definition** img\_mgmt\_client.h:64

[mcumgr\_image\_upload](structmcumgr__image__upload.md)

MCUmgr Image upload response.

**Definition** img\_mgmt\_client.h:72

[mcumgr\_image\_upload::status](structmcumgr__image__upload.md#a5522d2958df295c72fd00212155c7eee)

enum mcumgr\_err\_t status

Status.

**Definition** img\_mgmt\_client.h:74

[mcumgr\_image\_upload::image\_upload\_offset](structmcumgr__image__upload.md#ade29d2b559d9709b7372874e993e267c)

size\_t image\_upload\_offset

Reported image offset.

**Definition** img\_mgmt\_client.h:76

[smp\_client\_object](structsmp__client__object.md)

SMP client object.

**Definition** smp\_client.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt\_client.h](img__mgmt__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
