---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/method_8h.html
original_path: doxygen/html/method_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

method.h File Reference

HTTP request methods.
[More...](#details)

[Go to the source code of this file.](method_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) {     [HTTP\_DELETE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942) = 0 , [HTTP\_GET](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166) = 1 , [HTTP\_HEAD](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442) = 2 , [HTTP\_POST](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf) = 3 ,     [HTTP\_PUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512) = 4 , [HTTP\_CONNECT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76) = 5 , [HTTP\_OPTIONS](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251) = 6 , [HTTP\_TRACE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c) = 7 ,     [HTTP\_COPY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c) = 8 , [HTTP\_LOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf) = 9 , [HTTP\_MKCOL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6) = 10 , [HTTP\_MOVE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7) = 11 ,     [HTTP\_PROPFIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d) = 12 , [HTTP\_PROPPATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92) = 13 , [HTTP\_SEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac) = 14 , [HTTP\_UNLOCK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477) = 15 ,     [HTTP\_BIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b) = 16 , [HTTP\_REBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd) = 17 , [HTTP\_UNBIND](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a) = 18 , [HTTP\_ACL](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c) = 19 ,     [HTTP\_REPORT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd) = 20 , [HTTP\_MKACTIVITY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4) = 21 , [HTTP\_CHECKOUT](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e) = 22 , [HTTP\_MERGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069) = 23 ,     [HTTP\_MSEARCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3) = 24 , [HTTP\_NOTIFY](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf) = 25 , [HTTP\_SUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf) = 26 , [HTTP\_UNSUBSCRIBE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f) = 27 ,     [HTTP\_PATCH](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc) = 28 , [HTTP\_PURGE](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5) = 29 , [HTTP\_MKCALENDAR](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f) = 30 , [HTTP\_LINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29) = 31 ,     [HTTP\_UNLINK](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4) = 32   } |
|  | HTTP Request Methods. [More...](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) |

## Detailed Description

HTTP request methods.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [method.h](method_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
