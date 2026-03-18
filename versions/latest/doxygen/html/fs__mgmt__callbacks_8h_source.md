---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fs__mgmt__callbacks_8h_source.html
original_path: doxygen/html/fs__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_callbacks.h

[Go to the documentation of this file.](fs__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2022 Laird Connectivity

3 \* Copyright (c) 2022 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_MCUMGR\_FS\_MGMT\_CALLBACKS\_

9#define H\_MCUMGR\_FS\_MGMT\_CALLBACKS\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

21

[ 23](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9)enum [fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) {

[ 25](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a) [FS\_MGMT\_FILE\_ACCESS\_READ](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a),

26

[ 28](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2) [FS\_MGMT\_FILE\_ACCESS\_WRITE](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2),

29

[ 31](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2) [FS\_MGMT\_FILE\_ACCESS\_STATUS](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2),

32

[ 34](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c) [FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c),

35};

36

[ 43](structfs__mgmt__file__access.md)struct [fs\_mgmt\_file\_access](structfs__mgmt__file__access.md) {

[ 45](structfs__mgmt__file__access.md#a3aeeaf6d4243c1aaa7d6129a2ef4a064) enum [fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) [access](structfs__mgmt__file__access.md#a3aeeaf6d4243c1aaa7d6129a2ef4a064);

46

[ 52](structfs__mgmt__file__access.md#a0155b69d23f3c5044e317eb236ff173c) char \*[filename](structfs__mgmt__file__access.md#a0155b69d23f3c5044e317eb236ff173c);

53};

54

58

59#ifdef \_\_cplusplus

60}

61#endif

62

63#endif

[fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9)

fs\_mgmt\_file\_access\_types

The type of operation that is being requested for a given file access callback.

**Definition** fs\_mgmt\_callbacks.h:23

[FS\_MGMT\_FILE\_ACCESS\_WRITE](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2)

@ FS\_MGMT\_FILE\_ACCESS\_WRITE

Access to write file (file download).

**Definition** fs\_mgmt\_callbacks.h:28

[FS\_MGMT\_FILE\_ACCESS\_READ](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a)

@ FS\_MGMT\_FILE\_ACCESS\_READ

Access to read file (file upload).

**Definition** fs\_mgmt\_callbacks.h:25

[FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c)

@ FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM

Access to calculate hash or checksum of file.

**Definition** fs\_mgmt\_callbacks.h:34

[FS\_MGMT\_FILE\_ACCESS\_STATUS](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2)

@ FS\_MGMT\_FILE\_ACCESS\_STATUS

Access to get status of file.

**Definition** fs\_mgmt\_callbacks.h:31

[fs\_mgmt\_file\_access](structfs__mgmt__file__access.md)

Structure provided in the MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS notification callback: This callback functi...

**Definition** fs\_mgmt\_callbacks.h:43

[fs\_mgmt\_file\_access::filename](structfs__mgmt__file__access.md#a0155b69d23f3c5044e317eb236ff173c)

char \* filename

Path and filename of file be accesses, note that this can be changed by handlers to redirect file acc...

**Definition** fs\_mgmt\_callbacks.h:52

[fs\_mgmt\_file\_access::access](structfs__mgmt__file__access.md#a3aeeaf6d4243c1aaa7d6129a2ef4a064)

enum fs\_mgmt\_file\_access\_types access

Specifies the type of the operation that is being requested.

**Definition** fs\_mgmt\_callbacks.h:45

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [fs\_mgmt](dir_c1d9e91ec7be14b6f800d54e568d432d.md)
- [fs\_mgmt\_callbacks.h](fs__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
