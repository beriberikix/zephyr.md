---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mgmt__defines_8h_source.html
original_path: doxygen/html/mgmt__defines_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_defines.h

[Go to the documentation of this file.](mgmt__defines_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2022-2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_MGMT\_MGMT\_DEFINES\_

9#define H\_MGMT\_MGMT\_DEFINES\_

10

11#include <[inttypes.h](inttypes_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 28](group__mcumgr__mgmt__api.md#gabdd715ff5b7efe040f205edf0b00bc43)#define MGMT\_RETURN\_CHECK(ok) ok ? MGMT\_ERR\_EOK : MGMT\_ERR\_EMSGSIZE

29

[ 31](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd)enum [mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd) {

[ 33](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4) [MGMT\_OP\_READ](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4) = 0,

34

[ 36](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7) [MGMT\_OP\_READ\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7),

37

[ 39](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9) [MGMT\_OP\_WRITE](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9),

40

[ 42](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543) [MGMT\_OP\_WRITE\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543),

43};

44

[ 49](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5)enum [mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) {

[ 51](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120) [MGMT\_GROUP\_ID\_OS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120) = 0,

52

[ 54](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c) [MGMT\_GROUP\_ID\_IMAGE](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c),

55

[ 57](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc) [MGMT\_GROUP\_ID\_STAT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc),

58

[ 60](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb) [MGMT\_GROUP\_ID\_SETTINGS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb),

61

[ 63](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309) [MGMT\_GROUP\_ID\_LOG](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309),

64

[ 66](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204) [MGMT\_GROUP\_ID\_CRASH](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204),

67

[ 69](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527) [MGMT\_GROUP\_ID\_SPLIT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527),

70

[ 72](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a) [MGMT\_GROUP\_ID\_RUN](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a),

73

[ 75](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5) [MGMT\_GROUP\_ID\_FS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5),

76

[ 78](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85) [MGMT\_GROUP\_ID\_SHELL](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85),

79

[ 81](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726) [MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726) = 64,

82

[ 87](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68) [ZEPHYR\_MGMT\_GRP\_BASIC](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68) = ([MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726) - 1),

88};

89

[ 93](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5)enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) {

[ 95](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) [MGMT\_ERR\_EOK](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) = 0,

96

[ 98](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be) [MGMT\_ERR\_EUNKNOWN](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be),

99

[ 101](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe) [MGMT\_ERR\_ENOMEM](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe),

102

[ 104](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7) [MGMT\_ERR\_EINVAL](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7),

105

[ 107](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55) [MGMT\_ERR\_ETIMEOUT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55),

108

[ 110](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e) [MGMT\_ERR\_ENOENT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e),

111

[ 113](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787) [MGMT\_ERR\_EBADSTATE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787),

114

[ 116](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd) [MGMT\_ERR\_EMSGSIZE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd),

117

[ 119](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758) [MGMT\_ERR\_ENOTSUP](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758),

120

[ 122](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5) [MGMT\_ERR\_ECORRUPT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5),

123

[ 125](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1) [MGMT\_ERR\_EBUSY](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1),

126

[ 128](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) [MGMT\_ERR\_EACCESSDENIED](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde),

129

[ 131](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054) [MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054),

132

[ 134](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00) [MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00),

135

[ 137](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8) [MGMT\_ERR\_EPERUSER](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8) = 256

138};

139

[ 140](group__mcumgr__mgmt__api.md#gabb62e7697ffb2a2f4e6d96abe28808a6)#define MGMT\_HDR\_SIZE 8

141

145

146#ifdef \_\_cplusplus

147}

148#endif

149

150#endif /\* MGMT\_MGMT\_DEFINES\_H\_ \*/

[mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5)

mcumgr\_group\_t

MCUmgr groups.

**Definition** mgmt\_defines.h:49

[mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5)

mcumgr\_err\_t

MCUmgr error codes.

**Definition** mgmt\_defines.h:93

[mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd)

mcumgr\_op\_t

Opcodes; encoded in first byte of header.

**Definition** mgmt\_defines.h:31

[MGMT\_GROUP\_ID\_SETTINGS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb)

@ MGMT\_GROUP\_ID\_SETTINGS

Settings management (config) group, used for reading/writing settings.

**Definition** mgmt\_defines.h:60

[MGMT\_GROUP\_ID\_SPLIT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527)

@ MGMT\_GROUP\_ID\_SPLIT

Split image management group (unused).

**Definition** mgmt\_defines.h:69

[MGMT\_GROUP\_ID\_IMAGE](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c)

@ MGMT\_GROUP\_ID\_IMAGE

Image management group, used for uploading firmware images.

**Definition** mgmt\_defines.h:54

[MGMT\_GROUP\_ID\_RUN](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a)

@ MGMT\_GROUP\_ID\_RUN

Run group (unused).

**Definition** mgmt\_defines.h:72

[MGMT\_GROUP\_ID\_OS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120)

@ MGMT\_GROUP\_ID\_OS

OS (operating system) group.

**Definition** mgmt\_defines.h:51

[MGMT\_GROUP\_ID\_SHELL](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85)

@ MGMT\_GROUP\_ID\_SHELL

Shell management group, used for executing shell commands.

**Definition** mgmt\_defines.h:78

[MGMT\_GROUP\_ID\_STAT](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc)

@ MGMT\_GROUP\_ID\_STAT

Statistic management group, used for retrieving statistics.

**Definition** mgmt\_defines.h:57

[ZEPHYR\_MGMT\_GRP\_BASIC](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68)

@ ZEPHYR\_MGMT\_GRP\_BASIC

Zephyr-specific groups decrease from PERUSER to avoid collision with upstream and user-defined groups...

**Definition** mgmt\_defines.h:87

[MGMT\_GROUP\_ID\_FS](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5)

@ MGMT\_GROUP\_ID\_FS

FS (file system) group, used for performing file IO operations.

**Definition** mgmt\_defines.h:75

[MGMT\_GROUP\_ID\_LOG](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309)

@ MGMT\_GROUP\_ID\_LOG

Log management group (unused).

**Definition** mgmt\_defines.h:63

[MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)

@ MGMT\_GROUP\_ID\_PERUSER

User groups defined from 64 onwards.

**Definition** mgmt\_defines.h:81

[MGMT\_GROUP\_ID\_CRASH](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204)

@ MGMT\_GROUP\_ID\_CRASH

Crash group (unused).

**Definition** mgmt\_defines.h:66

[MGMT\_ERR\_EPERUSER](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8)

@ MGMT\_ERR\_EPERUSER

User errors defined from 256 onwards.

**Definition** mgmt\_defines.h:137

[MGMT\_ERR\_EMSGSIZE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)

@ MGMT\_ERR\_EMSGSIZE

Response too large.

**Definition** mgmt\_defines.h:116

[MGMT\_ERR\_ENOTSUP](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758)

@ MGMT\_ERR\_ENOTSUP

Command not supported.

**Definition** mgmt\_defines.h:119

[MGMT\_ERR\_EINVAL](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7)

@ MGMT\_ERR\_EINVAL

Error in input value.

**Definition** mgmt\_defines.h:104

[MGMT\_ERR\_EOK](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)

@ MGMT\_ERR\_EOK

No error (success).

**Definition** mgmt\_defines.h:95

[MGMT\_ERR\_EBADSTATE](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787)

@ MGMT\_ERR\_EBADSTATE

Current state disallows command.

**Definition** mgmt\_defines.h:113

[MGMT\_ERR\_ENOENT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e)

@ MGMT\_ERR\_ENOENT

No such file/entry.

**Definition** mgmt\_defines.h:110

[MGMT\_ERR\_EUNKNOWN](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be)

@ MGMT\_ERR\_EUNKNOWN

Unknown error.

**Definition** mgmt\_defines.h:98

[MGMT\_ERR\_EBUSY](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1)

@ MGMT\_ERR\_EBUSY

Command blocked by processing of other command.

**Definition** mgmt\_defines.h:125

[MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054)

@ MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD

Requested SMP MCUmgr protocol version is not supported (too old).

**Definition** mgmt\_defines.h:131

[MGMT\_ERR\_EACCESSDENIED](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde)

@ MGMT\_ERR\_EACCESSDENIED

Access to specific function, command or resource denied.

**Definition** mgmt\_defines.h:128

[MGMT\_ERR\_ECORRUPT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5)

@ MGMT\_ERR\_ECORRUPT

Corrupt.

**Definition** mgmt\_defines.h:122

[MGMT\_ERR\_ETIMEOUT](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55)

@ MGMT\_ERR\_ETIMEOUT

Operation timed out.

**Definition** mgmt\_defines.h:107

[MGMT\_ERR\_ENOMEM](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe)

@ MGMT\_ERR\_ENOMEM

Insufficient memory (likely not enough space for CBOR object).

**Definition** mgmt\_defines.h:101

[MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00)

@ MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW

Requested SMP MCUmgr protocol version is not supported (too new).

**Definition** mgmt\_defines.h:134

[MGMT\_OP\_WRITE](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9)

@ MGMT\_OP\_WRITE

Write op-code.

**Definition** mgmt\_defines.h:39

[MGMT\_OP\_WRITE\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543)

@ MGMT\_OP\_WRITE\_RSP

Write response op-code.

**Definition** mgmt\_defines.h:42

[MGMT\_OP\_READ](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4)

@ MGMT\_OP\_READ

Read op-code.

**Definition** mgmt\_defines.h:33

[MGMT\_OP\_READ\_RSP](group__mcumgr__mgmt__api.md#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7)

@ MGMT\_OP\_READ\_RSP

Read response op-code.

**Definition** mgmt\_defines.h:36

[inttypes.h](inttypes_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [mgmt\_defines.h](mgmt__defines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
