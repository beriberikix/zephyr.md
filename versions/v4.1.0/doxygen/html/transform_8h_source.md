---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/transform_8h_source.html
original_path: doxygen/html/transform_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

transform.h

[Go to the documentation of this file.](transform_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_TRANSFORM\_H

5#define SECURE\_STORAGE\_ITS\_TRANSFORM\_H

6

14#include <[zephyr/secure\_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)>

15

[ 17](transform_8h.md#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)enum { [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](transform_8h.md#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)

18 = CONFIG\_SECURE\_STORAGE\_ITS\_MAX\_DATA\_SIZE

19 + sizeof([secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd))

20 + CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_OUTPUT\_OVERHEAD };

21

[ 22](transform_8h.md#a88f73da6f6fa94b828c589c5669164aa)#define SECURE\_STORAGE\_ITS\_TRANSFORM\_DATA\_SIZE(stored\_data\_len) \

23 (stored\_data\_len - (SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE \

24 - CONFIG\_SECURE\_STORAGE\_ITS\_MAX\_DATA\_SIZE))

25

[ 38](transform_8h.md#ac976a23f8049c4e2e5b95bf867b9ea24)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_transform\_to\_store](transform_8h.md#ac976a23f8049c4e2e5b95bf867b9ea24)(

39 [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, size\_t data\_len, const void \*data,

40 [secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd) create\_flags,

41 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stored\_data[static [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](transform_8h.md#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)],

42 size\_t \*stored\_data\_len);

43

[ 56](transform_8h.md#a25353d53a0bce5dea8fc4d42bba8988e)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_transform\_from\_store](transform_8h.md#a25353d53a0bce5dea8fc4d42bba8988e)(

57 [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, size\_t stored\_data\_len,

58 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stored\_data[static [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](transform_8h.md#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)],

59 size\_t data\_size, void \*data, size\_t \*data\_len,

60 [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) \*create\_flags);

61

62#endif

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211)

uint32\_t psa\_storage\_create\_flags\_t

Flags used when creating an entry.

**Definition** storage\_common.h:26

[secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md)

The UID (caller + entry IDs) of an ITS entry.

**Definition** common.h:26

[secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd)

uint8\_t secure\_storage\_packed\_create\_flags\_t

**Definition** common.h:11

[common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)

Common definitions of the secure storage subsystem's ITS APIs.

[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)

int32\_t psa\_status\_t

**Definition** error.h:13

[secure\_storage\_its\_transform\_from\_store](transform_8h.md#a25353d53a0bce5dea8fc4d42bba8988e)

psa\_status\_t secure\_storage\_its\_transform\_from\_store(secure\_storage\_its\_uid\_t uid, size\_t stored\_data\_len, const uint8\_t stored\_data[static SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE], size\_t data\_size, void \*data, size\_t \*data\_len, psa\_storage\_create\_flags\_t \*create\_flags)

Transforms and validates the stored data of an ITS entry for use.

[secure\_storage\_its\_transform\_to\_store](transform_8h.md#ac976a23f8049c4e2e5b95bf867b9ea24)

psa\_status\_t secure\_storage\_its\_transform\_to\_store(secure\_storage\_its\_uid\_t uid, size\_t data\_len, const void \*data, secure\_storage\_packed\_create\_flags\_t create\_flags, uint8\_t stored\_data[static SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE], size\_t \*stored\_data\_len)

Transforms the data of an ITS entry for storage.

[SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](transform_8h.md#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)

@ SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE

**Definition** transform.h:17

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [transform.h](transform_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
