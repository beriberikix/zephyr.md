---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/os__mgmt__callbacks_8h_source.html
original_path: doxygen/html/os__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_callbacks.h

[Go to the documentation of this file.](os__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_OS\_MGMT\_CALLBACKS\_

8#define H\_MCUMGR\_OS\_MGMT\_CALLBACKS\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

20

[ 26](structos__mgmt__reset__data.md)struct [os\_mgmt\_reset\_data](structos__mgmt__reset__data.md) {

[ 28](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01) bool [force](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01);

29};

30

[ 35](structos__mgmt__bootloader__info__data.md)struct [os\_mgmt\_bootloader\_info\_data](structos__mgmt__bootloader__info__data.md) {

[ 40](structos__mgmt__bootloader__info__data.md#a0509ede3b6d0b40c0b93700a738f54cf) zcbor\_state\_t \*[zse](structos__mgmt__bootloader__info__data.md#a0509ede3b6d0b40c0b93700a738f54cf);

41

[ 43](structos__mgmt__bootloader__info__data.md#a19db05235f5b818dfc7e479265beee71) const size\_t \*[decoded](structos__mgmt__bootloader__info__data.md#a19db05235f5b818dfc7e479265beee71);

44

[ 46](structos__mgmt__bootloader__info__data.md#add73c66753d7b66713e9fdac8a1f951f) struct zcbor\_string \*[query](structos__mgmt__bootloader__info__data.md#add73c66753d7b66713e9fdac8a1f951f);

47

[ 52](structos__mgmt__bootloader__info__data.md#a2629ccb5b8ecc9da25bed2d0ec695938) bool \*[has\_output](structos__mgmt__bootloader__info__data.md#a2629ccb5b8ecc9da25bed2d0ec695938);

53};

54

58

59#ifdef \_\_cplusplus

60}

61#endif

62

63#endif

[os\_mgmt\_bootloader\_info\_data](structos__mgmt__bootloader__info__data.md)

Structure provided in the MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO notification callback: This callback fu...

**Definition** os\_mgmt\_callbacks.h:35

[os\_mgmt\_bootloader\_info\_data::zse](structos__mgmt__bootloader__info__data.md#a0509ede3b6d0b40c0b93700a738f54cf)

zcbor\_state\_t \* zse

The zcbor encoder which is currently being used to output group information, additional fields to the...

**Definition** os\_mgmt\_callbacks.h:40

[os\_mgmt\_bootloader\_info\_data::decoded](structos__mgmt__bootloader__info__data.md#a19db05235f5b818dfc7e479265beee71)

const size\_t \* decoded

Contains the number of decoded parameters.

**Definition** os\_mgmt\_callbacks.h:43

[os\_mgmt\_bootloader\_info\_data::has\_output](structos__mgmt__bootloader__info__data.md#a2629ccb5b8ecc9da25bed2d0ec695938)

bool \* has\_output

Must be set to true to indicate a response has been added, otherwise will return the OS\_MGMT\_ERR\_QUER...

**Definition** os\_mgmt\_callbacks.h:52

[os\_mgmt\_bootloader\_info\_data::query](structos__mgmt__bootloader__info__data.md#add73c66753d7b66713e9fdac8a1f951f)

struct zcbor\_string \* query

Contains the value of the query parameter.

**Definition** os\_mgmt\_callbacks.h:46

[os\_mgmt\_reset\_data](structos__mgmt__reset__data.md)

Structure provided in the MGMT\_EVT\_OP\_OS\_MGMT\_RESET notification callback: This callback function is ...

**Definition** os\_mgmt\_callbacks.h:26

[os\_mgmt\_reset\_data::force](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01)

bool force

Contains the value of the force parameter.

**Definition** os\_mgmt\_callbacks.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
