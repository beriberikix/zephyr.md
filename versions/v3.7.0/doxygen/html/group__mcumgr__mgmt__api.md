---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mcumgr__mgmt__api.html
original_path: doxygen/html/group__mcumgr__mgmt__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr mgmt API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr mgmt API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mgmt\_handler](structmgmt__handler.md) |
|  | Read handler and write handler for a single command ID. [More...](structmgmt__handler.md#details) |
| struct | [mgmt\_group](structmgmt__group.md) |
|  | A collection of handlers for an entire command group. [More...](structmgmt__group.md#details) |

| Macros | |
| --- | --- |
| #define | [MGMT\_CTXT\_SET\_RC\_RSN](#ga8027c2a587a835d92450f2935e66eea0)(mc, rsn) |
| #define | [MGMT\_CTXT\_RC\_RSN](#ga4d22641395a665a911be715c2531fbd8)(mc) |
| #define | [MGMT\_RETURN\_CHECK](#gabdd715ff5b7efe040f205edf0b00bc43)(ok) |
|  | Used at end of MCUmgr handlers to return an error if the message size limit was reached, or OK if it was not. |
| #define | [MGMT\_HDR\_SIZE](#gabb62e7697ffb2a2f4e6d96abe28808a6)   8 |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [mgmt\_alloc\_rsp\_fn](#ga292686c742179758ca5b853fc21fe302)) (const void \*src\_buf, void \*arg) |
|  | Allocates a buffer suitable for holding a response. |
| typedef void(\* | [mgmt\_reset\_buf\_fn](#ga1346d5160823c5e43fce3e6cba9f8607)) (void \*buf, void \*arg) |
|  | Resets a buffer to a length of 0. |
| typedef int(\* | [mgmt\_handler\_fn](#gaaafc2c73e1616340e29df6a1ba94c241)) (struct [smp\_streamer](structsmp__streamer.md) \*ctxt) |
|  | Processes a request and writes the corresponding response. |

| Enumerations | |
| --- | --- |
| enum | [mcumgr\_op\_t](#gae06a618f492f18e856742b4affab80dd) { [MGMT\_OP\_READ](#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4) = 0 , [MGMT\_OP\_READ\_RSP](#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7) , [MGMT\_OP\_WRITE](#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9) , [MGMT\_OP\_WRITE\_RSP](#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543) } |
|  | Opcodes; encoded in first byte of header. [More...](#gae06a618f492f18e856742b4affab80dd) |
| enum | [mcumgr\_group\_t](#ga81f98b9a0c3810f7d607b783f8e259b5) {     [MGMT\_GROUP\_ID\_OS](#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120) = 0 , [MGMT\_GROUP\_ID\_IMAGE](#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c) , [MGMT\_GROUP\_ID\_STAT](#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc) , [MGMT\_GROUP\_ID\_SETTINGS](#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb) ,     [MGMT\_GROUP\_ID\_LOG](#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309) , [MGMT\_GROUP\_ID\_CRASH](#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204) , [MGMT\_GROUP\_ID\_SPLIT](#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527) , [MGMT\_GROUP\_ID\_RUN](#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a) ,     [MGMT\_GROUP\_ID\_FS](#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5) , [MGMT\_GROUP\_ID\_SHELL](#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85) , [MGMT\_GROUP\_ID\_PERUSER](#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726) = 64 , [ZEPHYR\_MGMT\_GRP\_BASIC](#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68) = (MGMT\_GROUP\_ID\_PERUSER - 1)   } |
|  | MCUmgr groups. [More...](#ga81f98b9a0c3810f7d607b783f8e259b5) |
| enum | [mcumgr\_err\_t](#gac5d8757a7ca945c77f405764b85ad5c5) {     [MGMT\_ERR\_EOK](#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) = 0 , [MGMT\_ERR\_EUNKNOWN](#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be) , [MGMT\_ERR\_ENOMEM](#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe) , [MGMT\_ERR\_EINVAL](#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7) ,     [MGMT\_ERR\_ETIMEOUT](#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55) , [MGMT\_ERR\_ENOENT](#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e) , [MGMT\_ERR\_EBADSTATE](#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787) , [MGMT\_ERR\_EMSGSIZE](#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd) ,     [MGMT\_ERR\_ENOTSUP](#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758) , [MGMT\_ERR\_ECORRUPT](#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5) , [MGMT\_ERR\_EBUSY](#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1) , [MGMT\_ERR\_EACCESSDENIED](#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) ,     [MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD](#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054) , [MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW](#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00) , [MGMT\_ERR\_EPERUSER](#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8) = 256   } |
|  | MCUmgr error codes. [More...](#gac5d8757a7ca945c77f405764b85ad5c5) |

| Functions | |
| --- | --- |
| void | [mgmt\_register\_group](#ga70379f21faacddb5cc4a66f37a576ea0) (struct [mgmt\_group](structmgmt__group.md) \*group) |
|  | Registers a full command group. |
| void | [mgmt\_unregister\_group](#ga87e98bdf47d1c7798098444f69ccf8b8) (struct [mgmt\_group](structmgmt__group.md) \*group) |
|  | Unregisters a full command group. |
| const struct [mgmt\_handler](structmgmt__handler.md) \* | [mgmt\_find\_handler](#ga620862436fad440b9d2b9d8112be4ad1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id) |
|  | Finds a registered command handler. |
| const struct [mgmt\_group](structmgmt__group.md) \* | [mgmt\_find\_group](#gae88bc30026fbff6530179a94ba8f11ae) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id) |
|  | Finds a registered command group. |
| const struct [mgmt\_handler](structmgmt__handler.md) \* | [mgmt\_get\_handler](#gaec6ccbcaf28404b4b3662d5059f0a32b) (const struct [mgmt\_group](structmgmt__group.md) \*group, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id) |
|  | Finds a registered command handler. |

## Detailed Description

MCUmgr mgmt API.

Since
:   1.11

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga4d22641395a665a911be715c2531fbd8)MGMT\_CTXT\_RC\_RSN

| #define MGMT\_CTXT\_RC\_RSN | ( |  | *mc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mgmt.h](mgmt_8h.md)>`

**Value:**

NULL

## [◆ ](#ga8027c2a587a835d92450f2935e66eea0)MGMT\_CTXT\_SET\_RC\_RSN

| #define MGMT\_CTXT\_SET\_RC\_RSN | ( |  | *mc*, |
| --- | --- | --- | --- |
|  |  |  | *rsn* ) |

`#include <[mgmt.h](mgmt_8h.md)>`

## [◆ ](#gabb62e7697ffb2a2f4e6d96abe28808a6)MGMT\_HDR\_SIZE

| #define MGMT\_HDR\_SIZE   8 |
| --- |

`#include <[mgmt_defines.h](mgmt__defines_8h.md)>`

## [◆ ](#gabdd715ff5b7efe040f205edf0b00bc43)MGMT\_RETURN\_CHECK

| #define MGMT\_RETURN\_CHECK | ( |  | *ok* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mgmt_defines.h](mgmt__defines_8h.md)>`

**Value:**

ok ? [MGMT\_ERR\_EOK](#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) : [MGMT\_ERR\_EMSGSIZE](#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)

[MGMT\_ERR\_EMSGSIZE](#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)

@ MGMT\_ERR\_EMSGSIZE

Response too large.

**Definition** mgmt\_defines.h:116

[MGMT\_ERR\_EOK](#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)

@ MGMT\_ERR\_EOK

No error (success).

**Definition** mgmt\_defines.h:95

Used at end of MCUmgr handlers to return an error if the message size limit was reached, or OK if it was not.

## Typedef Documentation

## [◆ ](#ga292686c742179758ca5b853fc21fe302)mgmt\_alloc\_rsp\_fn

| typedef void \*(\* mgmt\_alloc\_rsp\_fn) (const void \*src\_buf, void \*arg) |
| --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Allocates a buffer suitable for holding a response.

If a source buf is provided, its user data is copied into the new buffer.

Parameters
:   | src\_buf | An optional source buffer to copy user data from. |
    | --- | --- |
    | arg | Optional streamer argument. |

Returns
:   Newly-allocated buffer on success NULL on failure.

## [◆ ](#gaaafc2c73e1616340e29df6a1ba94c241)mgmt\_handler\_fn

| typedef int(\* mgmt\_handler\_fn) (struct [smp\_streamer](structsmp__streamer.md) \*ctxt) |
| --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Processes a request and writes the corresponding response.

A separate handler is required for each supported op-ID pair.

Parameters
:   | ctxt | The mcumgr context to use. |
    | --- | --- |

Returns
:   0 if a response was successfully encoded, [mcumgr\_err\_t](#gac5d8757a7ca945c77f405764b85ad5c5) code on failure.

## [◆ ](#ga1346d5160823c5e43fce3e6cba9f8607)mgmt\_reset\_buf\_fn

| typedef void(\* mgmt\_reset\_buf\_fn) (void \*buf, void \*arg) |
| --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Resets a buffer to a length of 0.

The buffer's user data remains, but its payload is cleared.

Parameters
:   | buf | The buffer to reset. |
    | --- | --- |
    | arg | Optional streamer argument. |

## Enumeration Type Documentation

## [◆ ](#gac5d8757a7ca945c77f405764b85ad5c5)mcumgr\_err\_t

| enum [mcumgr\_err\_t](#gac5d8757a7ca945c77f405764b85ad5c5) |
| --- |

`#include <[mgmt_defines.h](mgmt__defines_8h.md)>`

MCUmgr error codes.

| Enumerator | |
| --- | --- |
| MGMT\_ERR\_EOK | No error (success). |
| MGMT\_ERR\_EUNKNOWN | Unknown error. |
| MGMT\_ERR\_ENOMEM | Insufficient memory (likely not enough space for CBOR object). |
| MGMT\_ERR\_EINVAL | Error in input value. |
| MGMT\_ERR\_ETIMEOUT | Operation timed out. |
| MGMT\_ERR\_ENOENT | No such file/entry. |
| MGMT\_ERR\_EBADSTATE | Current state disallows command. |
| MGMT\_ERR\_EMSGSIZE | Response too large. |
| MGMT\_ERR\_ENOTSUP | Command not supported. |
| MGMT\_ERR\_ECORRUPT | Corrupt. |
| MGMT\_ERR\_EBUSY | Command blocked by processing of other command. |
| MGMT\_ERR\_EACCESSDENIED | Access to specific function, command or resource denied. |
| MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD | Requested SMP MCUmgr protocol version is not supported (too old). |
| MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW | Requested SMP MCUmgr protocol version is not supported (too new). |
| MGMT\_ERR\_EPERUSER | User errors defined from 256 onwards. |

## [◆ ](#ga81f98b9a0c3810f7d607b783f8e259b5)mcumgr\_group\_t

| enum [mcumgr\_group\_t](#ga81f98b9a0c3810f7d607b783f8e259b5) |
| --- |

`#include <[mgmt_defines.h](mgmt__defines_8h.md)>`

MCUmgr groups.

The first 64 groups are reserved for system level mcumgr commands. Per-user commands are then defined after group 64.

| Enumerator | |
| --- | --- |
| MGMT\_GROUP\_ID\_OS | OS (operating system) group. |
| MGMT\_GROUP\_ID\_IMAGE | Image management group, used for uploading firmware images. |
| MGMT\_GROUP\_ID\_STAT | Statistic management group, used for retrieving statistics. |
| MGMT\_GROUP\_ID\_SETTINGS | Settings management (config) group, used for reading/writing settings. |
| MGMT\_GROUP\_ID\_LOG | Log management group (unused). |
| MGMT\_GROUP\_ID\_CRASH | Crash group (unused). |
| MGMT\_GROUP\_ID\_SPLIT | Split image management group (unused). |
| MGMT\_GROUP\_ID\_RUN | Run group (unused). |
| MGMT\_GROUP\_ID\_FS | FS (file system) group, used for performing file IO operations. |
| MGMT\_GROUP\_ID\_SHELL | Shell management group, used for executing shell commands. |
| MGMT\_GROUP\_ID\_PERUSER | User groups defined from 64 onwards. |
| ZEPHYR\_MGMT\_GRP\_BASIC | Zephyr-specific groups decrease from PERUSER to avoid collision with upstream and user-defined groups.  Zephyr-specific: Basic group |

## [◆ ](#gae06a618f492f18e856742b4affab80dd)mcumgr\_op\_t

| enum [mcumgr\_op\_t](#gae06a618f492f18e856742b4affab80dd) |
| --- |

`#include <[mgmt_defines.h](mgmt__defines_8h.md)>`

Opcodes; encoded in first byte of header.

| Enumerator | |
| --- | --- |
| MGMT\_OP\_READ | Read op-code. |
| MGMT\_OP\_READ\_RSP | Read response op-code. |
| MGMT\_OP\_WRITE | Write op-code. |
| MGMT\_OP\_WRITE\_RSP | Write response op-code. |

## Function Documentation

## [◆ ](#gae88bc30026fbff6530179a94ba8f11ae)mgmt\_find\_group()

| const struct [mgmt\_group](structmgmt__group.md) \* mgmt\_find\_group | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *group\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Finds a registered command group.

Parameters
:   | group\_id | The group id of the command group to find. |
    | --- | --- |

Returns
:   The requested group on success; NULL on failure.

## [◆ ](#ga620862436fad440b9d2b9d8112be4ad1)mgmt\_find\_handler()

| const struct [mgmt\_handler](structmgmt__handler.md) \* mgmt\_find\_handler | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *group\_id*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *command\_id* ) |

`#include <[mgmt.h](mgmt_8h.md)>`

Finds a registered command handler.

Parameters
:   | group\_id | The group of the command to find. |
    | --- | --- |
    | command\_id | The ID of the command to find. |

Returns
:   The requested command handler on success; NULL on failure.

## [◆ ](#gaec6ccbcaf28404b4b3662d5059f0a32b)mgmt\_get\_handler()

| const struct [mgmt\_handler](structmgmt__handler.md) \* mgmt\_get\_handler | ( | const struct [mgmt\_group](structmgmt__group.md) \* | *group*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *command\_id* ) |

`#include <[mgmt.h](mgmt_8h.md)>`

Finds a registered command handler.

Parameters
:   | group | The group of the command to find. |
    | --- | --- |
    | command\_id | The ID of the command to find. |

Returns
:   The requested command handler on success; NULL on failure.

## [◆ ](#ga70379f21faacddb5cc4a66f37a576ea0)mgmt\_register\_group()

| void mgmt\_register\_group | ( | struct [mgmt\_group](structmgmt__group.md) \* | *group* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Registers a full command group.

Parameters
:   | group | The group to register. |
    | --- | --- |

## [◆ ](#ga87e98bdf47d1c7798098444f69ccf8b8)mgmt\_unregister\_group()

| void mgmt\_unregister\_group | ( | struct [mgmt\_group](structmgmt__group.md) \* | *group* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mgmt.h](mgmt_8h.md)>`

Unregisters a full command group.

Parameters
:   | group | The group to register. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
