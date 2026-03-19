---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/method_8h_source.html
original_path: doxygen/html/method_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

method.h

[Go to the documentation of this file.](method_8h.md)

1

4

5/\*

6 \* Copyright (c) 2022 Meta

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_METHOD\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_HTTP\_METHOD\_H\_

13

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) {

[ 29](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942) [HTTP\_DELETE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942) = 0,

[ 30](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166) [HTTP\_GET](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166) = 1,

[ 31](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442) [HTTP\_HEAD](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442) = 2,

[ 32](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf) [HTTP\_POST](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf) = 3,

[ 33](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512) [HTTP\_PUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512) = 4,

[ 34](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76) [HTTP\_CONNECT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76) = 5,

[ 35](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251) [HTTP\_OPTIONS](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251) = 6,

[ 36](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c) [HTTP\_TRACE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c) = 7,

[ 37](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c) [HTTP\_COPY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c) = 8,

[ 38](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf) [HTTP\_LOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf) = 9,

[ 39](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6) [HTTP\_MKCOL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6) = 10,

[ 40](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7) [HTTP\_MOVE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7) = 11,

[ 41](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d) [HTTP\_PROPFIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d) = 12,

[ 42](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92) [HTTP\_PROPPATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92) = 13,

[ 43](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac) [HTTP\_SEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac) = 14,

[ 44](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477) [HTTP\_UNLOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477) = 15,

[ 45](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b) [HTTP\_BIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b) = 16,

[ 46](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd) [HTTP\_REBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd) = 17,

[ 47](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a) [HTTP\_UNBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a) = 18,

[ 48](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c) [HTTP\_ACL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c) = 19,

[ 49](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd) [HTTP\_REPORT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd) = 20,

[ 50](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4) [HTTP\_MKACTIVITY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4) = 21,

[ 51](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e) [HTTP\_CHECKOUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e) = 22,

[ 52](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069) [HTTP\_MERGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069) = 23,

[ 53](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3) [HTTP\_MSEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3) = 24,

[ 54](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf) [HTTP\_NOTIFY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf) = 25,

[ 55](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf) [HTTP\_SUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf) = 26,

[ 56](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f) [HTTP\_UNSUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f) = 27,

[ 57](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc) [HTTP\_PATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc) = 28,

[ 58](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5) [HTTP\_PURGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5) = 29,

[ 59](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f) [HTTP\_MKCALENDAR](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f) = 30,

[ 60](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29) [HTTP\_LINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29) = 31,

[ 61](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4) [HTTP\_UNLINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4) = 32,

62

64 HTTP\_METHOD\_END\_VALUE /\* keep this the last value \*/

66};

67

68#ifdef \_\_cplusplus

69}

70#endif

71

75

76#endif

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:28

[HTTP\_PROPPATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92)

@ HTTP\_PROPPATCH

PROPPATCH.

**Definition** method.h:42

[HTTP\_MSEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3)

@ HTTP\_MSEARCH

MSEARCH.

**Definition** method.h:53

[HTTP\_PUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512)

@ HTTP\_PUT

PUT.

**Definition** method.h:33

[HTTP\_MKACTIVITY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4)

@ HTTP\_MKACTIVITY

MKACTIVITY.

**Definition** method.h:50

[HTTP\_MKCALENDAR](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f)

@ HTTP\_MKCALENDAR

MKCALENDAR.

**Definition** method.h:59

[HTTP\_BIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b)

@ HTTP\_BIND

BIND.

**Definition** method.h:45

[HTTP\_PURGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5)

@ HTTP\_PURGE

PURGE.

**Definition** method.h:58

[HTTP\_NOTIFY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf)

@ HTTP\_NOTIFY

NOTIFY.

**Definition** method.h:54

[HTTP\_PROPFIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d)

@ HTTP\_PROPFIND

PROPFIND.

**Definition** method.h:41

[HTTP\_DELETE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942)

@ HTTP\_DELETE

DELETE.

**Definition** method.h:29

[HTTP\_MERGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069)

@ HTTP\_MERGE

MERGE.

**Definition** method.h:52

[HTTP\_GET](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166)

@ HTTP\_GET

GET.

**Definition** method.h:30

[HTTP\_REPORT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd)

@ HTTP\_REPORT

REPORT.

**Definition** method.h:49

[HTTP\_SUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf)

@ HTTP\_SUBSCRIBE

SUBSCRIBE.

**Definition** method.h:55

[HTTP\_UNBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a)

@ HTTP\_UNBIND

UNBIND.

**Definition** method.h:47

[HTTP\_CONNECT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76)

@ HTTP\_CONNECT

CONNECT.

**Definition** method.h:34

[HTTP\_UNLOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477)

@ HTTP\_UNLOCK

UNLOCK.

**Definition** method.h:44

[HTTP\_MKCOL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6)

@ HTTP\_MKCOL

MKCOL.

**Definition** method.h:39

[HTTP\_OPTIONS](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251)

@ HTTP\_OPTIONS

OPTIONS.

**Definition** method.h:35

[HTTP\_LINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29)

@ HTTP\_LINK

LINK.

**Definition** method.h:60

[HTTP\_UNSUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f)

@ HTTP\_UNSUBSCRIBE

UNSUBSCRIBE.

**Definition** method.h:56

[HTTP\_REBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd)

@ HTTP\_REBIND

REBIND.

**Definition** method.h:46

[HTTP\_LOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf)

@ HTTP\_LOCK

LOCK.

**Definition** method.h:38

[HTTP\_POST](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf)

@ HTTP\_POST

POST.

**Definition** method.h:32

[HTTP\_HEAD](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442)

@ HTTP\_HEAD

HEAD.

**Definition** method.h:31

[HTTP\_SEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac)

@ HTTP\_SEARCH

SEARCH.

**Definition** method.h:43

[HTTP\_UNLINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4)

@ HTTP\_UNLINK

UNLINK.

**Definition** method.h:61

[HTTP\_ACL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c)

@ HTTP\_ACL

ACL.

**Definition** method.h:48

[HTTP\_CHECKOUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e)

@ HTTP\_CHECKOUT

CHECKOUT.

**Definition** method.h:51

[HTTP\_MOVE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7)

@ HTTP\_MOVE

MOVE.

**Definition** method.h:40

[HTTP\_COPY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c)

@ HTTP\_COPY

COPY.

**Definition** method.h:37

[HTTP\_PATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc)

@ HTTP\_PATCH

PATCH.

**Definition** method.h:57

[HTTP\_TRACE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c)

@ HTTP\_TRACE

TRACE.

**Definition** method.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [method.h](method_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
