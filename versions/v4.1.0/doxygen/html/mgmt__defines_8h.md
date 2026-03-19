---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mgmt__defines_8h.html
original_path: doxygen/html/mgmt__defines_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_defines.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`

[Go to the source code of this file.](mgmt__defines_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MGMT\_RETURN\_CHECK](group__mcumgr__mgmt__api.md#gabdd715ff5b7efe040f205edf0b00bc43)(ok) |
|  | Used at end of MCUmgr handlers to return an error if the message size limit was reached, or OK if it was not. |
| #define | [MGMT\_HDR\_SIZE](group__mcumgr__mgmt__api.md#gabb62e7697ffb2a2f4e6d96abe28808a6)   8 |

| Enumerations | |
| --- | --- |
| enum | [mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd) { [MGMT\_OP\_READ](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4) = 0 , [MGMT\_OP\_READ\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7) , [MGMT\_OP\_WRITE](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9) , [MGMT\_OP\_WRITE\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543) } |
|  | Opcodes; encoded in first byte of header. [More...](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd) |
| enum | [mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) {     [MGMT\_GROUP\_ID\_OS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120) = 0 , [MGMT\_GROUP\_ID\_IMAGE](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c) , [MGMT\_GROUP\_ID\_STAT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc) , [MGMT\_GROUP\_ID\_SETTINGS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb) ,     [MGMT\_GROUP\_ID\_LOG](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309) , [MGMT\_GROUP\_ID\_CRASH](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204) , [MGMT\_GROUP\_ID\_SPLIT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527) , [MGMT\_GROUP\_ID\_RUN](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a) ,     [MGMT\_GROUP\_ID\_FS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5) , [MGMT\_GROUP\_ID\_SHELL](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85) , [MGMT\_GROUP\_ID\_ENUM](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c) , [MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726) = 64 ,     [ZEPHYR\_MGMT\_GRP\_BASIC](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68) = (MGMT\_GROUP\_ID\_PERUSER - 1)   } |
|  | MCUmgr groups. [More...](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) |
| enum | [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) {     [MGMT\_ERR\_EOK](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) = 0 , [MGMT\_ERR\_EUNKNOWN](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be) , [MGMT\_ERR\_ENOMEM](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe) , [MGMT\_ERR\_EINVAL](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7) ,     [MGMT\_ERR\_ETIMEOUT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55) , [MGMT\_ERR\_ENOENT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e) , [MGMT\_ERR\_EBADSTATE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787) , [MGMT\_ERR\_EMSGSIZE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd) ,     [MGMT\_ERR\_ENOTSUP](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758) , [MGMT\_ERR\_ECORRUPT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5) , [MGMT\_ERR\_EBUSY](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1) , [MGMT\_ERR\_EACCESSDENIED](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) ,     [MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054) , [MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00) , [MGMT\_ERR\_EPERUSER](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8) = 256   } |
|  | MCUmgr error codes. [More...](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [mgmt\_defines.h](mgmt__defines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
