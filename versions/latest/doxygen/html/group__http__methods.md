---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__http__methods.html
original_path: doxygen/html/group__http__methods.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HTTP request methods

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

HTTP request methods.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [http\_method](#gaacd5f203e33ac338ca5cb8f02a3ff3b8) {     [HTTP\_DELETE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942) = 0 , [HTTP\_GET](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166) = 1 , [HTTP\_HEAD](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442) = 2 , [HTTP\_POST](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf) = 3 ,     [HTTP\_PUT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512) = 4 , [HTTP\_CONNECT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76) = 5 , [HTTP\_OPTIONS](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251) = 6 , [HTTP\_TRACE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c) = 7 ,     [HTTP\_COPY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c) = 8 , [HTTP\_LOCK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf) = 9 , [HTTP\_MKCOL](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6) = 10 , [HTTP\_MOVE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7) = 11 ,     [HTTP\_PROPFIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d) = 12 , [HTTP\_PROPPATCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92) = 13 , [HTTP\_SEARCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac) = 14 , [HTTP\_UNLOCK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477) = 15 ,     [HTTP\_BIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b) = 16 , [HTTP\_REBIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd) = 17 , [HTTP\_UNBIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a) = 18 , [HTTP\_ACL](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c) = 19 ,     [HTTP\_REPORT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd) = 20 , [HTTP\_MKACTIVITY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4) = 21 , [HTTP\_CHECKOUT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e) = 22 , [HTTP\_MERGE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069) = 23 ,     [HTTP\_MSEARCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3) = 24 , [HTTP\_NOTIFY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf) = 25 , [HTTP\_SUBSCRIBE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf) = 26 , [HTTP\_UNSUBSCRIBE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f) = 27 ,     [HTTP\_PATCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc) = 28 , [HTTP\_PURGE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5) = 29 , [HTTP\_MKCALENDAR](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f) = 30 , [HTTP\_LINK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29) = 31 ,     [HTTP\_UNLINK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4) = 32   } |
|  | HTTP Request Methods. [More...](#gaacd5f203e33ac338ca5cb8f02a3ff3b8) |

## Detailed Description

HTTP request methods.

## Enumeration Type Documentation

## [◆ ](#gaacd5f203e33ac338ca5cb8f02a3ff3b8)http\_method

| enum [http\_method](#gaacd5f203e33ac338ca5cb8f02a3ff3b8) |
| --- |

`#include <[method.h](method_8h.md)>`

HTTP Request Methods.

| Enumerator | |
| --- | --- |
| HTTP\_DELETE | DELETE. |
| HTTP\_GET | GET. |
| HTTP\_HEAD | HEAD. |
| HTTP\_POST | POST. |
| HTTP\_PUT | PUT. |
| HTTP\_CONNECT | CONNECT. |
| HTTP\_OPTIONS | OPTIONS. |
| HTTP\_TRACE | TRACE. |
| HTTP\_COPY | COPY. |
| HTTP\_LOCK | LOCK. |
| HTTP\_MKCOL | MKCOL. |
| HTTP\_MOVE | MOVE. |
| HTTP\_PROPFIND | PROPFIND. |
| HTTP\_PROPPATCH | PROPPATCH. |
| HTTP\_SEARCH | SEARCH. |
| HTTP\_UNLOCK | UNLOCK. |
| HTTP\_BIND | BIND. |
| HTTP\_REBIND | REBIND. |
| HTTP\_UNBIND | UNBIND. |
| HTTP\_ACL | ACL. |
| HTTP\_REPORT | REPORT. |
| HTTP\_MKACTIVITY | MKACTIVITY. |
| HTTP\_CHECKOUT | CHECKOUT. |
| HTTP\_MERGE | MERGE. |
| HTTP\_MSEARCH | MSEARCH. |
| HTTP\_NOTIFY | NOTIFY. |
| HTTP\_SUBSCRIBE | SUBSCRIBE. |
| HTTP\_UNSUBSCRIBE | UNSUBSCRIBE. |
| HTTP\_PATCH | PATCH. |
| HTTP\_PURGE | PURGE. |
| HTTP\_MKCALENDAR | MKCALENDAR. |
| HTTP\_LINK | LINK. |
| HTTP\_UNLINK | UNLINK. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
