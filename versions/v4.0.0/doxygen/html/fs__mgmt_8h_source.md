---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fs__mgmt_8h_source.html
original_path: doxygen/html/fs__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt.h

[Go to the documentation of this file.](fs__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2022 mcumgr authors

3 \* Copyright (c) 2022 Laird Connectivity

4 \* Copyright (c) 2022-2023 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef H\_FS\_MGMT\_

10#define H\_FS\_MGMT\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 19](fs__mgmt_8h.md#a17b142e59be58d1c83c9ce87f7d84b97)#define FS\_MGMT\_ID\_FILE 0

[ 20](fs__mgmt_8h.md#a89833eac462adda453375482691c9dfa)#define FS\_MGMT\_ID\_STAT 1

[ 21](fs__mgmt_8h.md#af8263e56dd044b2ed5f10ce57e6fe2a5)#define FS\_MGMT\_ID\_HASH\_CHECKSUM 2

[ 22](fs__mgmt_8h.md#a82aefe54b14e74127593f3b3c2e06955)#define FS\_MGMT\_ID\_SUPPORTED\_HASH\_CHECKSUM 3

[ 23](fs__mgmt_8h.md#aa5e765a2c844efb494648c8856b91d72)#define FS\_MGMT\_ID\_OPENED\_FILE 4

24

[ 28](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336)enum [fs\_mgmt\_err\_code\_t](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336) {

[ 30](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2) [FS\_MGMT\_ERR\_OK](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2) = 0,

31

[ 33](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6) [FS\_MGMT\_ERR\_UNKNOWN](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6),

34

[ 36](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d) [FS\_MGMT\_ERR\_FILE\_INVALID\_NAME](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d),

37

[ 39](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e) [FS\_MGMT\_ERR\_FILE\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e),

40

[ 42](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac) [FS\_MGMT\_ERR\_FILE\_IS\_DIRECTORY](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac),

43

[ 45](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591) [FS\_MGMT\_ERR\_FILE\_OPEN\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591),

46

[ 48](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045) [FS\_MGMT\_ERR\_FILE\_SEEK\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045),

49

[ 51](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06) [FS\_MGMT\_ERR\_FILE\_READ\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06),

52

[ 54](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f) [FS\_MGMT\_ERR\_FILE\_TRUNCATE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f),

55

[ 57](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85) [FS\_MGMT\_ERR\_FILE\_DELETE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85),

58

[ 60](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a) [FS\_MGMT\_ERR\_FILE\_WRITE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a),

61

[ 69](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a) [FS\_MGMT\_ERR\_FILE\_OFFSET\_NOT\_VALID](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a),

70

[ 72](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63) [FS\_MGMT\_ERR\_FILE\_OFFSET\_LARGER\_THAN\_FILE](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63),

73

[ 75](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884) [FS\_MGMT\_ERR\_CHECKSUM\_HASH\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884),

76

[ 78](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd) [FS\_MGMT\_ERR\_MOUNT\_POINT\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd),

79

[ 81](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271) [FS\_MGMT\_ERR\_READ\_ONLY\_FILESYSTEM](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271),

82

[ 84](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5) [FS\_MGMT\_ERR\_FILE\_EMPTY](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5),

85};

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91#endif

[fs\_mgmt\_err\_code\_t](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336)

fs\_mgmt\_err\_code\_t

Command result codes for file system management group.

**Definition** fs\_mgmt.h:28

[FS\_MGMT\_ERR\_FILE\_OPEN\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591)

@ FS\_MGMT\_ERR\_FILE\_OPEN\_FAILED

Error occurred whilst attempting to open a file.

**Definition** fs\_mgmt.h:45

[FS\_MGMT\_ERR\_FILE\_WRITE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a)

@ FS\_MGMT\_ERR\_FILE\_WRITE\_FAILED

Error occurred whilst attempting to write data to a file.

**Definition** fs\_mgmt.h:60

[FS\_MGMT\_ERR\_FILE\_EMPTY](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5)

@ FS\_MGMT\_ERR\_FILE\_EMPTY

The operation cannot be performed because the file is empty with no contents.

**Definition** fs\_mgmt.h:84

[FS\_MGMT\_ERR\_FILE\_IS\_DIRECTORY](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac)

@ FS\_MGMT\_ERR\_FILE\_IS\_DIRECTORY

The specified file is a directory, not a file.

**Definition** fs\_mgmt.h:42

[FS\_MGMT\_ERR\_FILE\_INVALID\_NAME](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d)

@ FS\_MGMT\_ERR\_FILE\_INVALID\_NAME

The specified file name is not valid.

**Definition** fs\_mgmt.h:36

[FS\_MGMT\_ERR\_FILE\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e)

@ FS\_MGMT\_ERR\_FILE\_NOT\_FOUND

The specified file does not exist.

**Definition** fs\_mgmt.h:39

[FS\_MGMT\_ERR\_OK](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2)

@ FS\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** fs\_mgmt.h:30

[FS\_MGMT\_ERR\_CHECKSUM\_HASH\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884)

@ FS\_MGMT\_ERR\_CHECKSUM\_HASH\_NOT\_FOUND

The requested checksum or hash type was not found or is not supported by this build.

**Definition** fs\_mgmt.h:75

[FS\_MGMT\_ERR\_FILE\_DELETE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85)

@ FS\_MGMT\_ERR\_FILE\_DELETE\_FAILED

Error occurred whilst trying to delete file.

**Definition** fs\_mgmt.h:57

[FS\_MGMT\_ERR\_FILE\_SEEK\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045)

@ FS\_MGMT\_ERR\_FILE\_SEEK\_FAILED

Error occurred whilst attempting to seek to an offset in a file.

**Definition** fs\_mgmt.h:48

[FS\_MGMT\_ERR\_FILE\_OFFSET\_LARGER\_THAN\_FILE](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63)

@ FS\_MGMT\_ERR\_FILE\_OFFSET\_LARGER\_THAN\_FILE

The requested offset is larger than the size of the file on the device.

**Definition** fs\_mgmt.h:72

[FS\_MGMT\_ERR\_READ\_ONLY\_FILESYSTEM](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271)

@ FS\_MGMT\_ERR\_READ\_ONLY\_FILESYSTEM

The specified mount point is that of a read-only filesystem.

**Definition** fs\_mgmt.h:81

[FS\_MGMT\_ERR\_MOUNT\_POINT\_NOT\_FOUND](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd)

@ FS\_MGMT\_ERR\_MOUNT\_POINT\_NOT\_FOUND

The specified mount point was not found or is not mounted.

**Definition** fs\_mgmt.h:78

[FS\_MGMT\_ERR\_FILE\_READ\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06)

@ FS\_MGMT\_ERR\_FILE\_READ\_FAILED

Error occurred whilst attempting to read data from a file.

**Definition** fs\_mgmt.h:51

[FS\_MGMT\_ERR\_FILE\_OFFSET\_NOT\_VALID](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a)

@ FS\_MGMT\_ERR\_FILE\_OFFSET\_NOT\_VALID

The specified data offset is not valid, this could indicate that the file on the device has changed s...

**Definition** fs\_mgmt.h:69

[FS\_MGMT\_ERR\_FILE\_TRUNCATE\_FAILED](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f)

@ FS\_MGMT\_ERR\_FILE\_TRUNCATE\_FAILED

Error occurred whilst trying to truncate file.

**Definition** fs\_mgmt.h:54

[FS\_MGMT\_ERR\_UNKNOWN](fs__mgmt_8h.md#a8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6)

@ FS\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** fs\_mgmt.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [fs\_mgmt](dir_c1d9e91ec7be14b6f800d54e568d432d.md)
- [fs\_mgmt.h](fs__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
