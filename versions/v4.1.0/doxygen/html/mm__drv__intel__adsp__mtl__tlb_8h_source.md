---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html
original_path: doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm\_drv\_intel\_adsp\_mtl\_tlb.h

[Go to the documentation of this file.](mm__drv__intel__adsp__mtl__tlb_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (c) 2022 Intel Corporation.

4 \*

5 \* Author: Marcin Szkudlinski <marcin.szkudlinski@linux.intel.com>

6 \*

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_ADSP\_MTL\_TLB

10#define ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_ADSP\_MTL\_TLB

11

12

13/\*

14 \* This function will save contents of the physical memory banks into a provided storage buffer

15 \*

16 \* the system must be almost stopped. Operation is destructive - it will change physical to

17 \* virtual addresses mapping leaving the system not operational

18 \* Power states of memory banks will stay not touched

19 \* assuming

20 \* - the dcache memory had been invalidated before

21 \* - no remapping of addresses below unused\_l2\_sram\_start\_marker has been made

22 \* (this is ensured by the driver itself - it rejects such remapping request)

23 \*

24 \* at this point the memory is still up&running so its safe to use libraries like memcpy

25 \* and the procedure can be called in a zephyr driver model way

26 \*/

[ 27](mm__drv__intel__adsp__mtl__tlb_8h.md#aec3b78e74d53f6a9fe6ca029c7d776a5)typedef void (\*[mm\_save\_context](mm__drv__intel__adsp__mtl__tlb_8h.md#aec3b78e74d53f6a9fe6ca029c7d776a5))(void \*storage\_buffer);

28

29/\*

30 \* This function will return a required size of storage buffer needed to perform context save

31 \*

32 \*/

[ 33](mm__drv__intel__adsp__mtl__tlb_8h.md#a19135d221cf896eb1795c2f22f6679bc)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[mm\_get\_storage\_size](mm__drv__intel__adsp__mtl__tlb_8h.md#a19135d221cf896eb1795c2f22f6679bc))(void);

34

35/\*

36 \* This function will restore the contents and power state of the physical memory banks

37 \* and recreate physical to virtual mappings

38 \*

39 \* As the system memory is down at this point, the procedure

40 \* - MUST be located in IMR memory region

41 \* - MUST be called using a simple extern procedure call - API table is not yet loaded

42 \* - MUST NOT use libraries, like memcpy, use instead a special version bmemcpy located in IMR

43 \*

44 \*/

[ 45](mm__drv__intel__adsp__mtl__tlb_8h.md#aa98be3168d56e8fb7e183563eb64cbdb)void [adsp\_mm\_restore\_context](mm__drv__intel__adsp__mtl__tlb_8h.md#aa98be3168d56e8fb7e183563eb64cbdb)(void \*storage\_buffer);

46

[ 47](structintel__adsp__tlb__api.md)struct [intel\_adsp\_tlb\_api](structintel__adsp__tlb__api.md) {

[ 48](structintel__adsp__tlb__api.md#ad9788abb323e4c70c08178c9df98a62e) [mm\_save\_context](mm__drv__intel__adsp__mtl__tlb_8h.md#aec3b78e74d53f6a9fe6ca029c7d776a5) [save\_context](structintel__adsp__tlb__api.md#ad9788abb323e4c70c08178c9df98a62e);

[ 49](structintel__adsp__tlb__api.md#a49ce206e8ac75d0fad79af3bb5cd9447) [mm\_get\_storage\_size](mm__drv__intel__adsp__mtl__tlb_8h.md#a19135d221cf896eb1795c2f22f6679bc) [get\_storage\_size](structintel__adsp__tlb__api.md#a49ce206e8ac75d0fad79af3bb5cd9447);

50};

51

52#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_ADSP\_MTL\_TLB \*/

[mm\_get\_storage\_size](mm__drv__intel__adsp__mtl__tlb_8h.md#a19135d221cf896eb1795c2f22f6679bc)

uint32\_t(\* mm\_get\_storage\_size)(void)

**Definition** mm\_drv\_intel\_adsp\_mtl\_tlb.h:33

[adsp\_mm\_restore\_context](mm__drv__intel__adsp__mtl__tlb_8h.md#aa98be3168d56e8fb7e183563eb64cbdb)

void adsp\_mm\_restore\_context(void \*storage\_buffer)

[mm\_save\_context](mm__drv__intel__adsp__mtl__tlb_8h.md#aec3b78e74d53f6a9fe6ca029c7d776a5)

void(\* mm\_save\_context)(void \*storage\_buffer)

**Definition** mm\_drv\_intel\_adsp\_mtl\_tlb.h:27

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intel\_adsp\_tlb\_api](structintel__adsp__tlb__api.md)

**Definition** mm\_drv\_intel\_adsp\_mtl\_tlb.h:47

[intel\_adsp\_tlb\_api::get\_storage\_size](structintel__adsp__tlb__api.md#a49ce206e8ac75d0fad79af3bb5cd9447)

mm\_get\_storage\_size get\_storage\_size

**Definition** mm\_drv\_intel\_adsp\_mtl\_tlb.h:49

[intel\_adsp\_tlb\_api::save\_context](structintel__adsp__tlb__api.md#ad9788abb323e4c70c08178c9df98a62e)

mm\_save\_context save\_context

**Definition** mm\_drv\_intel\_adsp\_mtl\_tlb.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [mm\_drv\_intel\_adsp\_mtl\_tlb.h](mm__drv__intel__adsp__mtl__tlb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
