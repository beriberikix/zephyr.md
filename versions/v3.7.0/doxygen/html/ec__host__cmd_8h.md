---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ec__host__cmd_8h.html
original_path: doxygen/html/ec__host__cmd_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/mgmt/ec_host_cmd/backend.h](backend_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](ec__host__cmd_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ec\_host\_cmd](structec__host__cmd.md) |
| struct | [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) |
|  | Arguments passed into every installed host command handler. [More...](structec__host__cmd__handler__args.md#details) |
| struct | [ec\_host\_cmd\_handler](structec__host__cmd__handler.md) |
|  | Structure use for statically registering host command handlers. [More...](structec__host__cmd__handler.md#details) |
| struct | [ec\_host\_cmd\_request\_header](structec__host__cmd__request__header.md) |
|  | Header for requests from host to embedded controller. [More...](structec__host__cmd__request__header.md#details) |
| struct | [ec\_host\_cmd\_response\_header](structec__host__cmd__response__header.md) |
|  | Header for responses from embedded controller to host. [More...](structec__host__cmd__response__header.md#details) |

| Macros | |
| --- | --- |
| #define | [EC\_HOST\_CMD\_HANDLER](group__ec__host__cmd__interface.md#gaed5a8c4ba3648ae9e6284502f6a48dc7)(\_id, \_function, \_version\_mask, \_request\_type, \_response\_type) |
|  | Statically define and register a host command handler. |
| #define | [EC\_HOST\_CMD\_HANDLER\_UNBOUND](group__ec__host__cmd__interface.md#ga2dae15d1db72c7c9b5f879284a990e13)(\_id, \_function, \_version\_mask) |
|  | Statically define and register a host command handler without sizes. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573)) (const struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, void \*user\_data) |
| typedef enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* | [ec\_host\_cmd\_in\_progress\_cb\_t](group__ec__host__cmd__interface.md#gacf91301985634f9a12cd80db5e818821)) (void \*user\_data) |
| typedef enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* | [ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7)) (struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args) |

| Enumerations | |
| --- | --- |
| enum | [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) {     [EC\_HOST\_CMD\_SUCCESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e) = 0 , [EC\_HOST\_CMD\_INVALID\_COMMAND](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432) = 1 , [EC\_HOST\_CMD\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201) = 2 , [EC\_HOST\_CMD\_INVALID\_PARAM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d) = 3 ,     [EC\_HOST\_CMD\_ACCESS\_DENIED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c) = 4 , [EC\_HOST\_CMD\_INVALID\_RESPONSE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9) = 5 , [EC\_HOST\_CMD\_INVALID\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39) = 6 , [EC\_HOST\_CMD\_INVALID\_CHECKSUM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301) = 7 ,     [EC\_HOST\_CMD\_IN\_PROGRESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e) = 8 , [EC\_HOST\_CMD\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996) = 9 , [EC\_HOST\_CMD\_TIMEOUT](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26) = 10 , [EC\_HOST\_CMD\_OVERFLOW](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443) = 11 ,     [EC\_HOST\_CMD\_INVALID\_HEADER](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b) = 12 , [EC\_HOST\_CMD\_REQUEST\_TRUNCATED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00) = 13 , [EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5) = 14 , [EC\_HOST\_CMD\_BUS\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2) = 15 ,     [EC\_HOST\_CMD\_BUSY](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1) = 16 , [EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5) = 17 , [EC\_HOST\_CMD\_INVALID\_HEADER\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e) = 18 , [EC\_HOST\_CMD\_INVALID\_DATA\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985) = 19 ,     [EC\_HOST\_CMD\_DUP\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80) = 20 , [EC\_HOST\_CMD\_MAX](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad202e5ae4fac72a7fb3d1f4a7dff3ba9) = UINT16\_MAX   } |
|  | Host command response codes (16-bit). [More...](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) |
| enum | [ec\_host\_cmd\_log\_level](group__ec__host__cmd__interface.md#ga70cbd55129ef589688c6d2f5999337c9) {     [EC\_HOST\_CMD\_DEBUG\_OFF](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38) , [EC\_HOST\_CMD\_DEBUG\_NORMAL](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81) , [EC\_HOST\_CMD\_DEBUG\_EVERY](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6) , [EC\_HOST\_CMD\_DEBUG\_PARAMS](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1) ,     [EC\_HOST\_CMD\_DEBUG\_MODES](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)   } |
| enum | [ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec) { [EC\_HOST\_CMD\_STATE\_DISABLED](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af) = 0 , [EC\_HOST\_CMD\_STATE\_RECEIVING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20) , [EC\_HOST\_CMD\_STATE\_PROCESSING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8) , [EC\_HOST\_CMD\_STATE\_SENDING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46) } |

| Functions | |
| --- | --- |
| int | [ec\_host\_cmd\_init](group__ec__host__cmd__interface.md#gaab1fdcb0fd13a19447d262d496b8aed9) (struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend) |
|  | Initialize the host command subsystem. |
| int | [ec\_host\_cmd\_send\_response](group__ec__host__cmd__interface.md#ga95f36f8cf2d21ea73bd8a36f3f7303e8) (enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) status, const struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args) |
|  | Send the host command response. |
| void | [ec\_host\_cmd\_rx\_notify](group__ec__host__cmd__interface.md#gadbee4a2588abeb6db63f70a90b67a8fb) (void) |
|  | Signal a new host command. |
| void | [ec\_host\_cmd\_set\_user\_cb](group__ec__host__cmd__interface.md#gaaf267a44816e5f856db2092fca681d3e) ([ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573) cb, void \*user\_data) |
|  | Install a user callback for receiving a host command. |
| const struct [ec\_host\_cmd](structec__host__cmd.md) \* | [ec\_host\_cmd\_get\_hc](group__ec__host__cmd__interface.md#gaf3b87533037c4d865641643736904d02) (void) |
|  | Get the main ec host command structure. |
| FUNC\_NORETURN void | [ec\_host\_cmd\_task](group__ec__host__cmd__interface.md#gaaa3dc6c413b9637a3817cf82e138b27a) (void) |
|  | The thread function for Host Command subsystem. |
| int | [ec\_host\_cmd\_add\_suppressed](group__ec__host__cmd__interface.md#ga9f734642958684ca654a3c786b2ceb74) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cmd\_id) |
|  | Add a suppressed command. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [ec\_host\_cmd.h](ec__host__cmd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
