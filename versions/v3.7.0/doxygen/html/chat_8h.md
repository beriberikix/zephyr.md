---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/chat_8h.html
original_path: doxygen/html/chat_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

chat.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/modem/stats.h](modem_2stats_8h_source.md)>`

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
| #define | [MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE](#a0a62af922c1ca5aed812ac634e490453)(\_request, \_timeout\_ms) |
| #define | [MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE](#ab807fffae2007bc03a8e87ba73921888)(\_sym, ...) |
| #define | [MODEM\_CHAT\_SCRIPT\_DEFINE](#ad15f82648a073883c5956d6b14f4e41a)(\_sym, \_script\_chats, \_abort\_matches, \_callback, \_timeout\_s) |
| #define | [MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE](#a7be78a33341512359a1857baaa4ac915)(\_sym, \_script\_chats, \_callback, \_timeout\_s) |
| #define | [MODEM\_CHAT\_SCRIPT\_EMPTY\_DEFINE](#a16441c0c385874a41b9ac071a67cea1c)(\_sym) |

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
| void | [modem\_chat\_match\_init](#a1f41fc90f5026dc688a90567278ac175) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match) |
|  | Initialize modem chat match. |
| int | [modem\_chat\_match\_set\_match](#ac9ed985688aeaee96adcb2b6c4285099) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, const char \*match) |
|  | Set match of modem chat match instance. |
| int | [modem\_chat\_match\_set\_separators](#a35c1a4f9ed2677fb747025f859eeae56) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, const char \*separators) |
|  | Set separators of modem chat match instance. |
| void | [modem\_chat\_match\_set\_callback](#afea28e13817e1daa6bb5c42514542e4e) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, [modem\_chat\_match\_callback](#ae689e92c91d414f968267e290e5246bd) callback) |
|  | Set modem chat match callback. |
| void | [modem\_chat\_match\_set\_partial](#a53cb148e665095d036edc266e778a8ce) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) partial) |
|  | Set modem chat match partial flag. |
| void | [modem\_chat\_match\_enable\_wildcards](#a3274b7ffcce059c4d0a5d2ccb3e0bcc6) (struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set modem chat match wildcards flag. |
| void | [modem\_chat\_script\_chat\_init](#af12d45cf404e85c94fc13252294c76ca) (struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat) |
|  | Initialize modem chat script chat. |
| int | [modem\_chat\_script\_chat\_set\_request](#adaed8cb3a0933fd15a46344ca0df9930) (struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat, const char \*request) |
|  | Set request of modem chat script chat instance. |
| int | [modem\_chat\_script\_chat\_set\_response\_matches](#a2aec485e298ebde8af0372deb9c4784f) (struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat, const struct [modem\_chat\_match](structmodem__chat__match.md) \*response\_matches, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) response\_matches\_size) |
|  | Set modem chat script chat matches. |
| void | [modem\_chat\_script\_chat\_set\_timeout](#ae52a949df85cbcb7729c88917f46ef8d) (struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout\_ms) |
|  | Set modem chat script chat timeout. |
| void | [modem\_chat\_script\_init](#afdca5529d3ae3c982f3577560216e309) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script) |
|  | Initialize modem chat script. |
| void | [modem\_chat\_script\_set\_name](#a9ab3fa018ee0b2ebaacb3d74ee7ce29a) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script, const char \*name) |
|  | Set modem chat script name. |
| int | [modem\_chat\_script\_set\_script\_chats](#ad6b669708d24a3d3d91d1c40c2c504c8) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script, const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chats, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) script\_chats\_size) |
|  | Set modem chat script chats. |
| int | [modem\_chat\_script\_set\_abort\_matches](#a9bff858315a05324ff9690bdbce7398f) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script, const struct [modem\_chat\_match](structmodem__chat__match.md) \*abort\_matches, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) abort\_matches\_size) |
|  | Set modem chat script abort matches. |
| void | [modem\_chat\_script\_set\_callback](#a4389d813db136c199c872f20a125eba2) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script, [modem\_chat\_script\_callback](#a72ee94db5e79658fb71a65a3118d301e) callback) |
|  | Set modem chat script callback. |
| void | [modem\_chat\_script\_set\_timeout](#a9180fa670c3b6e88fa6011fdce5fd909) (struct [modem\_chat\_script](structmodem__chat__script.md) \*script, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout\_s) |
|  | Set modem chat script timeout. |

| Variables | |
| --- | --- |
| const struct [modem\_chat\_match](structmodem__chat__match.md) | [modem\_chat\_any\_match](#ada2cd7e12d9a37af6f13ecfb6c182176) |
| const struct [modem\_chat\_match](structmodem__chat__match.md) | [modem\_chat\_empty\_matches](#ac94a45b118b155ca7de1a45d12297ae4) [0] |
| const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) | [modem\_chat\_empty\_script\_chats](#a19cd30454fb4eb9293e87b24a8cf0655) [0] |

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

**Definition** chat.h:55

[modem\_chat\_match](structmodem__chat__match.md)

Modem chat match.

**Definition** chat.h:38

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

**Definition** util.h:127

## [◆ ](#a0a62af922c1ca5aed812ac634e490453)MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE

| #define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE | ( |  | *\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_timeout\_ms* ) |

**Value:**

{ \

.request = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_request), \

.request\_size = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(sizeof(\_request) - 1), \

.response\_matches = NULL, \

.response\_matches\_size = 0, \

.timeout = \_timeout\_ms, \

}

## [◆ ](#ab807fffae2007bc03a8e87ba73921888)MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \_sym[] = {\_\_VA\_ARGS\_\_}

[modem\_chat\_script\_chat](structmodem__chat__script__chat.md)

Modem chat script chat.

**Definition** chat.h:97

## [◆ ](#ad15f82648a073883c5956d6b14f4e41a)MODEM\_CHAT\_SCRIPT\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | *\_script\_chats*, |
|  |  |  | *\_abort\_matches*, |
|  |  |  | *\_callback*, |
|  |  |  | *\_timeout\_s* ) |

**Value:**

const static struct [modem\_chat\_script](structmodem__chat__script.md) \_sym = { \

.name = #\_sym, \

.[script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114) = \_script\_chats, \

.script\_chats\_size = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_script\_chats), \

.abort\_matches = \_abort\_matches, \

.abort\_matches\_size = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_abort\_matches), \

.callback = \_callback, \

.[timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268) = \_timeout\_s, \

}

[modem\_chat\_script\_chat::timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268)

uint16\_t timeout

Timeout before chat script may continue to next step in milliseconds.

**Definition** chat.h:107

[modem\_chat\_script](structmodem__chat__script.md)

Modem chat script.

**Definition** chat.h:162

[modem\_chat\_script::script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114)

const struct modem\_chat\_script\_chat \* script\_chats

Array of script chats.

**Definition** chat.h:166

## [◆ ](#a16441c0c385874a41b9ac071a67cea1c)MODEM\_CHAT\_SCRIPT\_EMPTY\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_EMPTY\_DEFINE | ( |  | *\_sym* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE](#a7be78a33341512359a1857baaa4ac915)(\_sym, [modem\_chat\_empty\_script\_chats](#a19cd30454fb4eb9293e87b24a8cf0655), NULL, 0)

[modem\_chat\_empty\_script\_chats](#a19cd30454fb4eb9293e87b24a8cf0655)

const struct modem\_chat\_script\_chat modem\_chat\_empty\_script\_chats[0]

[MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE](#a7be78a33341512359a1857baaa4ac915)

#define MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE(\_sym, \_script\_chats, \_callback, \_timeout\_s)

**Definition** chat.h:190

## [◆ ](#a7be78a33341512359a1857baaa4ac915)MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE

| #define MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE | ( |  | *\_sym*, |
| --- | --- | --- | --- |
|  |  |  | *\_script\_chats*, |
|  |  |  | *\_callback*, |
|  |  |  | *\_timeout\_s* ) |

**Value:**

[MODEM\_CHAT\_SCRIPT\_DEFINE](#ad15f82648a073883c5956d6b14f4e41a)(\_sym, \_script\_chats, [modem\_chat\_empty\_matches](#ac94a45b118b155ca7de1a45d12297ae4), \

\_callback, \_timeout\_s)

[modem\_chat\_empty\_matches](#ac94a45b118b155ca7de1a45d12297ae4)

const struct modem\_chat\_match modem\_chat\_empty\_matches[0]

[MODEM\_CHAT\_SCRIPT\_DEFINE](#ad15f82648a073883c5956d6b14f4e41a)

#define MODEM\_CHAT\_SCRIPT\_DEFINE(\_sym, \_script\_chats, \_abort\_matches, \_callback, \_timeout\_s)

**Definition** chat.h:179

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

## [◆ ](#a3274b7ffcce059c4d0a5d2ccb3e0bcc6)modem\_chat\_match\_enable\_wildcards()

| void modem\_chat\_match\_enable\_wildcards | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Set modem chat match wildcards flag.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |
    | enable | Enable/disable Wildcards |

## [◆ ](#a1f41fc90f5026dc688a90567278ac175)modem\_chat\_match\_init()

| void modem\_chat\_match\_init | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize modem chat match.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |

## [◆ ](#afea28e13817e1daa6bb5c42514542e4e)modem\_chat\_match\_set\_callback()

| void modem\_chat\_match\_set\_callback | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match*, |
| --- | --- | --- | --- |
|  |  | [modem\_chat\_match\_callback](#ae689e92c91d414f968267e290e5246bd) | *callback* ) |

Set modem chat match callback.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |
    | callback | Callback to set |

## [◆ ](#ac9ed985688aeaee96adcb2b6c4285099)modem\_chat\_match\_set\_match()

| int modem\_chat\_match\_set\_match | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match*, |
| --- | --- | --- | --- |
|  |  | const char \* | *match* ) |

Set match of modem chat match instance.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |
    | match | Match to set |

Note
:   The lifetime of match must match or exceed the lifetime of chat\_match

Warning
:   Always call this API after match is modified

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

## [◆ ](#a53cb148e665095d036edc266e778a8ce)modem\_chat\_match\_set\_partial()

| void modem\_chat\_match\_set\_partial | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *partial* ) |

Set modem chat match partial flag.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |
    | partial | Partial flag to set |

## [◆ ](#a35c1a4f9ed2677fb747025f859eeae56)modem\_chat\_match\_set\_separators()

| int modem\_chat\_match\_set\_separators | ( | struct [modem\_chat\_match](structmodem__chat__match.md) \* | *chat\_match*, |
| --- | --- | --- | --- |
|  |  | const char \* | *separators* ) |

Set separators of modem chat match instance.

Parameters
:   | chat\_match | Modem chat match instance |
    | --- | --- |
    | separators | Separators to set |

Note
:   The lifetime of separators must match or exceed the lifetime of chat\_match

Warning
:   Always call this API after separators are modified

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

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

## [◆ ](#af12d45cf404e85c94fc13252294c76ca)modem\_chat\_script\_chat\_init()

| void modem\_chat\_script\_chat\_init | ( | struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | *script\_chat* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize modem chat script chat.

Parameters
:   | script\_chat | Modem chat script chat instance |
    | --- | --- |

## [◆ ](#adaed8cb3a0933fd15a46344ca0df9930)modem\_chat\_script\_chat\_set\_request()

| int modem\_chat\_script\_chat\_set\_request | ( | struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | *script\_chat*, |
| --- | --- | --- | --- |
|  |  | const char \* | *request* ) |

Set request of modem chat script chat instance.

Parameters
:   | script\_chat | Modem chat script chat instance |
    | --- | --- |
    | request | Request to set |

Note
:   The lifetime of request must match or exceed the lifetime of script\_chat

Warning
:   Always call this API after request is modified

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

## [◆ ](#a2aec485e298ebde8af0372deb9c4784f)modem\_chat\_script\_chat\_set\_response\_matches()

| int modem\_chat\_script\_chat\_set\_response\_matches | ( | struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | *script\_chat*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_match](structmodem__chat__match.md) \* | *response\_matches*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *response\_matches\_size* ) |

Set modem chat script chat matches.

Parameters
:   | script\_chat | Modem chat script chat instance |
    | --- | --- |
    | response\_matches | Response match array to set |
    | response\_matches\_size | Size of response match array |

Note
:   The lifetime of response\_matches must match or exceed the lifetime of script\_chat

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

## [◆ ](#ae52a949df85cbcb7729c88917f46ef8d)modem\_chat\_script\_chat\_set\_timeout()

| void modem\_chat\_script\_chat\_set\_timeout | ( | struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | *script\_chat*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *timeout\_ms* ) |

Set modem chat script chat timeout.

Parameters
:   | script\_chat | Modem chat script chat instance |
    | --- | --- |
    | timeout\_ms | Timeout in milliseconds |

## [◆ ](#afdca5529d3ae3c982f3577560216e309)modem\_chat\_script\_init()

| void modem\_chat\_script\_init | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize modem chat script.

Parameters
:   | script | Modem chat script instance |
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

## [◆ ](#a9bff858315a05324ff9690bdbce7398f)modem\_chat\_script\_set\_abort\_matches()

| int modem\_chat\_script\_set\_abort\_matches | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_match](structmodem__chat__match.md) \* | *abort\_matches*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *abort\_matches\_size* ) |

Set modem chat script abort matches.

Parameters
:   | script | Modem chat script instance |
    | --- | --- |
    | abort\_matches | Abort match array to set |
    | abort\_matches\_size | Size of abort match array |

Note
:   The lifetime of abort\_matches must match or exceed the lifetime of script

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

## [◆ ](#a4389d813db136c199c872f20a125eba2)modem\_chat\_script\_set\_callback()

| void modem\_chat\_script\_set\_callback | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script*, |
| --- | --- | --- | --- |
|  |  | [modem\_chat\_script\_callback](#a72ee94db5e79658fb71a65a3118d301e) | *callback* ) |

Set modem chat script callback.

Parameters
:   | script | Modem chat script instance |
    | --- | --- |
    | callback | Callback to set |

## [◆ ](#a9ab3fa018ee0b2ebaacb3d74ee7ce29a)modem\_chat\_script\_set\_name()

| void modem\_chat\_script\_set\_name | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

Set modem chat script name.

Parameters
:   | script | Modem chat script instance |
    | --- | --- |
    | name | Name to set |

Note
:   The lifetime of name must match or exceed the lifetime of script

## [◆ ](#ad6b669708d24a3d3d91d1c40c2c504c8)modem\_chat\_script\_set\_script\_chats()

| int modem\_chat\_script\_set\_script\_chats | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | *script\_chats*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *script\_chats\_size* ) |

Set modem chat script chats.

Parameters
:   | script | Modem chat script instance |
    | --- | --- |
    | script\_chats | Chat script array to set |
    | script\_chats\_size | Size of chat script array |

Note
:   The lifetime of script\_chats must match or exceed the lifetime of script

Return values
:   | 0 | if successful, negative errno code otherwise |
    | --- | --- |

## [◆ ](#a9180fa670c3b6e88fa6011fdce5fd909)modem\_chat\_script\_set\_timeout()

| void modem\_chat\_script\_set\_timeout | ( | struct [modem\_chat\_script](structmodem__chat__script.md) \* | *script*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout\_s* ) |

Set modem chat script timeout.

Parameters
:   | script | Modem chat script instance |
    | --- | --- |
    | timeout\_s | Timeout in seconds |

## Variable Documentation

## [◆ ](#ada2cd7e12d9a37af6f13ecfb6c182176)modem\_chat\_any\_match

| | const struct [modem\_chat\_match](structmodem__chat__match.md) modem\_chat\_any\_match | | --- | | extern |
| --- | --- | --- |

## [◆ ](#ac94a45b118b155ca7de1a45d12297ae4)modem\_chat\_empty\_matches

| | const struct [modem\_chat\_match](structmodem__chat__match.md) modem\_chat\_empty\_matches[0] | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a19cd30454fb4eb9293e87b24a8cf0655)modem\_chat\_empty\_script\_chats

| | const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) modem\_chat\_empty\_script\_chats[0] | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [chat.h](chat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
