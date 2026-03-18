---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/chat_8h.html
original_path: doxygen/html/chat_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

chat.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`

[Go to the source code of this file.](chat_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [modem\_chat\_match](structmodem__chat__match.md) |
|  | Modem chat match. [More...](structmodem__chat__match.md#details) |
| struct | [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) |
|  | Modem chat script chat. [More...](structmodem__chat__script__chat.md#details) |
| struct | [modem\_chat\_script](structmodem__chat__script.md) |
|  | Modem chat script. [More...](structmodem__chat__script.md#details) |
| struct | [modem\_chat](structmodem__chat.md) |
|  | Chat instance internal context. [More...](structmodem__chat.md#details) |
| struct | [modem\_chat\_config](structmodem__chat__config.md) |
|  | Chat configuration. [More...](structmodem__chat__config.md#details) |

| Macros | |
| --- | --- |
| #define | [MODEM\_CHAT\_MATCH](#a078fd13acc9abcc0e0aa0304e6a8537a)(\_match, \_separators, \_callback) |
| #define | [MODEM\_CHAT\_MATCH\_WILDCARD](#a02b06e0d97df03b32eb6c40e91f91fd8)(\_match, \_separators, \_callback) |
| #define | [MODEM\_CHAT\_MATCH\_INITIALIZER](#aa62ca91615d0b93b0d2adbcf6c78e251)(\_match, \_separators, \_callback, \_wildcards, \_partial) |
| #define | [MODEM\_CHAT\_MATCH\_DEFINE](#a926b0d2993eb8158137e2caa7687abb8)(\_sym, \_match, \_separators, \_callback) |
| #define | [MODEM\_CHAT\_MATCHES\_DEFINE](#a216094ddd94351fadf0e84bacbadc84e)(\_sym, ...) |
| #define | [MODEM\_CHAT\_SCRIPT\_CMD\_RESP](#a01c94aa4a5881f2f4bdc004d08abaf0d)(\_request, \_response\_match) |
| #define | [MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_MULT](#add48fe039151f5596e5208cccd170746)(\_request, \_response\_matches) |
| #define | [MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE](#a13613a9df035c4ac55a730ca9d64fa36)(\_request, \_timeout) |
| #define | [MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE](#ab807fffae2007bc03a8e87ba73921888)(\_sym, ...) |
| #define | [MODEM\_CHAT\_SCRIPT\_DEFINE](#a20bd8d3dd49c813101c6f456351bc771)(\_sym, \_script\_chats, \_abort\_matches, \_callback, \_timeout) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_chat\_match\_callback](#ae689e92c91d414f968267e290e5246bd)) (struct [modem\_chat](structmodem__chat.md) \*chat, char \*\*argv, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) argc, void \*user\_data) |
|  | Callback called when matching chat is received. |
| typedef void(\* | [modem\_chat\_script\_callback](#a72ee94db5e79658fb71a65a3118d301e)) (struct [modem\_chat](structmodem__chat.md) \*chat, enum [modem\_chat\_script\_result](#a4035be227ddec8424311575305647d3e) result, void \*user\_data) |
|  | Callback called when script chat is received. |

| Enumerations | |
| --- | --- |
| enum | [modem\_chat\_script\_result](#a4035be227ddec8424311575305647d3e) { [MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS](#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee) , [MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT](#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b) , [MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT](#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e) } |
| enum | [modem\_chat\_script\_send\_state](#a734cb1bcbbbf5c87551b20038e0608ae) { [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE](#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974) , [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST](#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd) , [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER](#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf) } |

| Functions | |
| --- | --- |
| int | [modem\_chat\_init](#af79f3b0e67b5777876137b9e3e16d985) (struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_config](structmodem__chat__config.md) \*config) |
|  | Initialize modem pipe chat instance. |
| int | [modem\_chat\_attach](#af91ae4e64113188e7049a7568a086556) (struct [modem\_chat](structmodem__chat.md) \*chat, struct modem\_pipe \*pipe) |
|  | Attach modem chat instance to pipe. |
| int | [modem\_chat\_run\_script\_async](#a397d399703449498171ac898776fe791) (struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script) |
|  | Run script asynchronously. |
| int | [modem\_chat\_run\_script](#ae64d151a5f65bde1dd1973393acf3ff1) (struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script) |
|  | Run script. |
| static int | [modem\_chat\_script\_run](#aa92ffb91bab15c882cff7b13fca7eeb5) (struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script) |
|  | Run script asynchronously. |
| void | [modem\_chat\_script\_abort](#a5ec3918a4beb6b30deecedbd6f6382ee) (struct [modem\_chat](structmodem__chat.md) \*chat) |
|  | Abort script. |
| void | [modem\_chat\_release](#a62fa275cb9ce387b0bf5b384c9448c41) (struct [modem\_chat](structmodem__chat.md) \*chat) |
|  | Release pipe from chat instance. |

## Macro Definition Documentation

## [◆ ](#a078fd13acc9abcc0e0aa0304e6a8537a)MODEM\_CHAT\_MATCH

| #define MODEM\_CHAT\_MATCH | ( |  | *\_match*, |
| --- | --- | --- | --- |
|  |  |  | *\_separators*, |
|  |  |  | *\_callback* ) |

**Value:**

{ \

.match = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_match), .match\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_match) - 1), \

.separators = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_separators), \

.separators\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_separators) - 1), .wildcards = false, \

.callback = \_callback, \

}

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

## [◆ ](#a926b0d2993eb8158137e2caa7687abb8)MODEM\_CHAT\_MATCH\_DEFINE

| #define MODEM\_CHAT\_MATCH\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | *\_match*, |
|  |  |  | *\_separators*, |
|  |  |  | *\_callback* ) |

**Value:**

const static struct [modem\_chat\_match](structmodem__chat__match.md) \_sym = [MODEM\_CHAT\_MATCH](#a078fd13acc9abcc0e0aa0304e6a8537a)(\_match, \_separators, \_callback)

[MODEM\_CHAT\_MATCH](#a078fd13acc9abcc0e0aa0304e6a8537a)

#define MODEM\_CHAT\_MATCH(\_match, \_separators, \_callback)

**Definition** chat.h:54

[modem\_chat\_match](structmodem__chat__match.md)

Modem chat match.

**Definition** chat.h:37

## [◆ ](#aa62ca91615d0b93b0d2adbcf6c78e251)MODEM\_CHAT\_MATCH\_INITIALIZER

| #define MODEM\_CHAT\_MATCH\_INITIALIZER | ( |  | *\_match*, |
| --- | --- | --- | --- |
|  |  |  | *\_separators*, |
|  |  |  | *\_callback*, |
|  |  |  | *\_wildcards*, |
|  |  |  | *\_partial* ) |

**Value:**

{ \

.match = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_match), \

.match\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_match) - 1), \

.separators = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_separators), \

.separators\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_separators) - 1), \

.wildcards = \_wildcards, \

.partial = \_partial, \

.callback = \_callback, \

}

## [◆ ](#a02b06e0d97df03b32eb6c40e91f91fd8)MODEM\_CHAT\_MATCH\_WILDCARD

| #define MODEM\_CHAT\_MATCH\_WILDCARD | ( |  | *\_match*, |
| --- | --- | --- | --- |
|  |  |  | *\_separators*, |
|  |  |  | *\_callback* ) |

**Value:**

{ \

.match = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_match), .match\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_match) - 1), \

.separators = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_separators), \

.separators\_size = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(sizeof(\_separators) - 1), .wildcards = true, \

.callback = \_callback, \

}

## [◆ ](#a216094ddd94351fadf0e84bacbadc84e)MODEM\_CHAT\_MATCHES\_DEFINE

| #define MODEM\_CHAT\_MATCHES\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

const static struct [modem\_chat\_match](structmodem__chat__match.md) \_sym[] = {\_\_VA\_ARGS\_\_}

## [◆ ](#a01c94aa4a5881f2f4bdc004d08abaf0d)MODEM\_CHAT\_SCRIPT\_CMD\_RESP

| #define MODEM\_CHAT\_SCRIPT\_CMD\_RESP | ( |  | *\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_response\_match* ) |

**Value:**

{ \

.request = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_request), \

.request\_size = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(sizeof(\_request) - 1), \

.response\_matches = &\_response\_match, \

.response\_matches\_size = 1, \

.timeout = 0, \

}

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

## [◆ ](#add48fe039151f5596e5208cccd170746)MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_MULT

| #define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_MULT | ( |  | *\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_response\_matches* ) |

**Value:**

{ \

.request = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_request), \

.request\_size = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(sizeof(\_request) - 1), \

.response\_matches = \_response\_matches, \

.response\_matches\_size = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_response\_matches), \

.timeout = 0, \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

## [◆ ](#a13613a9df035c4ac55a730ca9d64fa36)MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE

| #define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE | ( |  | *\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_timeout* ) |

**Value:**

{ \

.request = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_request), \

.request\_size = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(sizeof(\_request) - 1), \

.response\_matches = NULL, \

.response\_matches\_size = 0, \

.timeout = \_timeout, \

}

## [◆ ](#ab807fffae2007bc03a8e87ba73921888)MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \_sym[] = {\_\_VA\_ARGS\_\_}

[modem\_chat\_script\_chat](structmodem__chat__script__chat.md)

Modem chat script chat.

**Definition** chat.h:90

## [◆ ](#a20bd8d3dd49c813101c6f456351bc771)MODEM\_CHAT\_SCRIPT\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | *\_script\_chats*, |
|  |  |  | *\_abort\_matches*, |
|  |  |  | *\_callback*, |
|  |  |  | *\_timeout* ) |

**Value:**

const static struct [modem\_chat\_script](structmodem__chat__script.md) \_sym = { \

.name = #\_sym, \

.[script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114) = \_script\_chats, \

.script\_chats\_size = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_script\_chats), \

.abort\_matches = \_abort\_matches, \

.abort\_matches\_size = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_abort\_matches), \

.callback = \_callback, \

.[timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268) = \_timeout, \

}

[modem\_chat\_script\_chat::timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268)

uint16\_t timeout

Timeout before chat script may continue to next step in milliseconds.

**Definition** chat.h:100

[modem\_chat\_script](structmodem__chat__script.md)

Modem chat script.

**Definition** chat.h:152

[modem\_chat\_script::script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114)

const struct modem\_chat\_script\_chat \* script\_chats

Array of script chats.

**Definition** chat.h:156

## Typedef Documentation

## [◆ ](#ae689e92c91d414f968267e290e5246bd)modem\_chat\_match\_callback

| typedef void(\* modem\_chat\_match\_callback) (struct [modem\_chat](structmodem__chat.md) \*chat, char \*\*argv, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) argc, void \*user\_data) |
| --- |

Callback called when matching chat is received.

Parameters
:   | chat | Pointer to chat instance instance |
    | --- | --- |
    | argv | Pointer to array of parsed arguments |
    | argc | Number of parsed arguments, arg 0 holds the exact match |
    | user\_data | Free to use user data set during [modem\_chat\_init()](#af79f3b0e67b5777876137b9e3e16d985) |

## [◆ ](#a72ee94db5e79658fb71a65a3118d301e)modem\_chat\_script\_callback

| typedef void(\* modem\_chat\_script\_callback) (struct [modem\_chat](structmodem__chat.md) \*chat, enum [modem\_chat\_script\_result](#a4035be227ddec8424311575305647d3e) result, void \*user\_data) |
| --- |

Callback called when script chat is received.

Parameters
:   | chat | Pointer to chat instance instance |
    | --- | --- |
    | result | Result of script execution |
    | user\_data | Free to use user data set during [modem\_chat\_init()](#af79f3b0e67b5777876137b9e3e16d985) |

## Enumeration Type Documentation

## [◆ ](#a4035be227ddec8424311575305647d3e)modem\_chat\_script\_result

| enum [modem\_chat\_script\_result](#a4035be227ddec8424311575305647d3e) |
| --- |

| Enumerator | |
| --- | --- |
| MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS |  |
| MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT |  |
| MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT |  |

## [◆ ](#a734cb1bcbbbf5c87551b20038e0608ae)modem\_chat\_script\_send\_state

| enum [modem\_chat\_script\_send\_state](#a734cb1bcbbbf5c87551b20038e0608ae) |
| --- |

| Enumerator | |
| --- | --- |
| MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE |  |
| MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST |  |
| MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER |  |

## Function Documentation

## [◆ ](#af91ae4e64113188e7049a7568a086556)modem\_chat\_attach()

| int modem\_chat\_attach | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat*, |
| --- | --- | --- | --- |
|  |  | struct modem\_pipe \* | *pipe* ) |

Attach modem chat instance to pipe.

Parameters
:   | chat | Chat instance |
    | --- | --- |
    | pipe | Pipe instance to attach Chat instance to |

Returns
:   0 if successful
:   negative errno code if failure

Note
:   Chat instance is enabled if successful

## [◆ ](#af79f3b0e67b5777876137b9e3e16d985)modem\_chat\_init()

| int modem\_chat\_init | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_config](structmodem__chat__config.md) \* | *config* ) |

Initialize modem pipe chat instance.

Parameters
:   | chat | Chat instance |
    | --- | --- |
    | config | Configuration which shall be applied to Chat instance |

Note
:   Chat instance must be attached to pipe

## [◆ ](#a62fa275cb9ce387b0bf5b384c9448c41)modem\_chat\_release()

| void modem\_chat\_release | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat* | ) |  |
| --- | --- | --- | --- | --- | --- |

Release pipe from chat instance.

Parameters
:   | chat | Chat instance |
    | --- | --- |

## [◆ ](#ae64d151a5f65bde1dd1973393acf3ff1)modem\_chat\_run\_script()

| int modem\_chat\_run\_script | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script* ) |

Run script.

Parameters
:   | chat | Chat instance |
    | --- | --- |
    | script | Script to run |

Returns
:   0 if successful
:   -EBUSY if a script is currently running
:   -EPERM if modem pipe is not attached
:   -EINVAL if arguments or script is invalid

Note
:   Script runs until complete or aborted.

## [◆ ](#a397d399703449498171ac898776fe791)modem\_chat\_run\_script\_async()

| int modem\_chat\_run\_script\_async | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script* ) |

Run script asynchronously.

Parameters
:   | chat | Chat instance |
    | --- | --- |
    | script | Script to run |

Returns
:   0 if script successfully started
:   -EBUSY if a script is currently running
:   -EPERM if modem pipe is not attached
:   -EINVAL if arguments or script is invalid

Note
:   Script runs asynchronously until complete or aborted.

## [◆ ](#a5ec3918a4beb6b30deecedbd6f6382ee)modem\_chat\_script\_abort()

| void modem\_chat\_script\_abort | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat* | ) |  |
| --- | --- | --- | --- | --- | --- |

Abort script.

Parameters
:   | chat | Chat instance |
    | --- | --- |

## [◆ ](#aa92ffb91bab15c882cff7b13fca7eeb5)modem\_chat\_script\_run()

| | int modem\_chat\_script\_run | ( | struct [modem\_chat](structmodem__chat.md) \* | *chat*, | | --- | --- | --- | --- | |  |  | const struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Run script asynchronously.

Note
:   Function exists for backwards compatibility and should be deprecated

Parameters
:   | chat | Chat instance |
    | --- | --- |
    | script | Script to run |

Returns
:   0 if script successfully started
:   -EBUSY if a script is currently running
:   -EPERM if modem pipe is not attached
:   -EINVAL if arguments or script is invalid

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [chat.h](chat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
