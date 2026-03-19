---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mesh_8h_source.html
original_path: doxygen/html/mesh_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mesh.h

[Go to the documentation of this file.](mesh_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_H\_

12

13#include <stddef.h>

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[zephyr/net\_buf.h](net__buf_8h.md)>

17

18#include <[zephyr/bluetooth/mesh/keys.h](keys_8h.md)>

19#include <[zephyr/bluetooth/mesh/msg.h](msg_8h.md)>

20#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

21#include <[zephyr/bluetooth/mesh/main.h](main_8h.md)>

22#include <[zephyr/bluetooth/mesh/cfg.h](cfg_8h.md)>

23#include <[zephyr/bluetooth/mesh/cfg\_srv.h](cfg__srv_8h.md)>

24#include <[zephyr/bluetooth/mesh/health\_srv.h](health__srv_8h.md)>

25#include <[zephyr/bluetooth/mesh/blob\_srv.h](blob__srv_8h.md)>

26#include <[zephyr/bluetooth/mesh/cfg\_cli.h](cfg__cli_8h.md)>

27#include <[zephyr/bluetooth/mesh/health\_cli.h](health__cli_8h.md)>

28#include <[zephyr/bluetooth/mesh/blob\_cli.h](blob__cli_8h.md)>

29#include <[zephyr/bluetooth/mesh/blob\_io\_flash.h](blob__io__flash_8h.md)>

30#include <[zephyr/bluetooth/mesh/priv\_beacon\_srv.h](priv__beacon__srv_8h.md)>

31#include <[zephyr/bluetooth/mesh/priv\_beacon\_cli.h](priv__beacon__cli_8h.md)>

32#include <[zephyr/bluetooth/mesh/dfu\_srv.h](dfu__srv_8h.md)>

33#include <[zephyr/bluetooth/mesh/dfd\_srv.h](dfd__srv_8h.md)>

34#include <[zephyr/bluetooth/mesh/dfu\_cli.h](dfu__cli_8h.md)>

35#include <[zephyr/bluetooth/mesh/dfu\_metadata.h](dfu__metadata_8h.md)>

36#include <[zephyr/bluetooth/mesh/proxy.h](proxy_8h.md)>

37#include <[zephyr/bluetooth/mesh/heartbeat.h](heartbeat_8h.md)>

38#include <[zephyr/bluetooth/mesh/cdb.h](cdb_8h.md)>

39#include <[zephyr/bluetooth/mesh/rpr\_cli.h](rpr__cli_8h.md)>

40#include <[zephyr/bluetooth/mesh/rpr\_srv.h](rpr__srv_8h.md)>

41#include <[zephyr/bluetooth/mesh/sar\_cfg\_srv.h](sar__cfg__srv_8h.md)>

42#include <[zephyr/bluetooth/mesh/sar\_cfg\_cli.h](sar__cfg__cli_8h.md)>

43#include <[zephyr/bluetooth/mesh/op\_agg\_srv.h](op__agg__srv_8h.md)>

44#include <[zephyr/bluetooth/mesh/op\_agg\_cli.h](op__agg__cli_8h.md)>

45#include <[zephyr/bluetooth/mesh/large\_comp\_data\_srv.h](large__comp__data__srv_8h.md)>

46#include <[zephyr/bluetooth/mesh/large\_comp\_data\_cli.h](large__comp__data__cli_8h.md)>

47#include <[zephyr/bluetooth/mesh/od\_priv\_proxy\_srv.h](od__priv__proxy__srv_8h.md)>

48#include <[zephyr/bluetooth/mesh/od\_priv\_proxy\_cli.h](od__priv__proxy__cli_8h.md)>

49#include <[zephyr/bluetooth/mesh/sol\_pdu\_rpl\_srv.h](sol__pdu__rpl__srv_8h.md)>

50#include <[zephyr/bluetooth/mesh/sol\_pdu\_rpl\_cli.h](sol__pdu__rpl__cli_8h.md)>

51#include <[zephyr/bluetooth/mesh/brg\_cfg\_cli.h](brg__cfg__cli_8h.md)>

52#include <[zephyr/bluetooth/mesh/brg\_cfg\_srv.h](brg__cfg__srv_8h.md)>

53#include <[zephyr/bluetooth/mesh/statistic.h](statistic_8h.md)>

54

55#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_H\_ \*/

[access.h](access_8h.md)

Access layer APIs.

[blob\_cli.h](blob__cli_8h.md)

[blob\_io\_flash.h](blob__io__flash_8h.md)

[blob\_srv.h](blob__srv_8h.md)

[brg\_cfg\_cli.h](brg__cfg__cli_8h.md)

[brg\_cfg\_srv.h](brg__cfg__srv_8h.md)

Bluetooth Mesh Bridge Configuration Server Model APIs.

[cdb.h](cdb_8h.md)

[cfg.h](cfg_8h.md)

Runtime configuration APIs.

[cfg\_cli.h](cfg__cli_8h.md)

Configuration Client Model APIs.

[cfg\_srv.h](cfg__srv_8h.md)

Configuration Server Model APIs.

[dfd\_srv.h](dfd__srv_8h.md)

[dfu\_cli.h](dfu__cli_8h.md)

[dfu\_metadata.h](dfu__metadata_8h.md)

[dfu\_srv.h](dfu__srv_8h.md)

[health\_cli.h](health__cli_8h.md)

Health Client Model APIs.

[health\_srv.h](health__srv_8h.md)

Health Server Model APIs.

[heartbeat.h](heartbeat_8h.md)

Heartbeat APIs.

[types.h](include_2zephyr_2types_8h.md)

[keys.h](keys_8h.md)

Keys APIs.

[large\_comp\_data\_cli.h](large__comp__data__cli_8h.md)

[large\_comp\_data\_srv.h](large__comp__data__srv_8h.md)

[main.h](main_8h.md)

Bluetooth Mesh Protocol APIs.

[msg.h](msg_8h.md)

Message APIs.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[od\_priv\_proxy\_cli.h](od__priv__proxy__cli_8h.md)

[od\_priv\_proxy\_srv.h](od__priv__proxy__srv_8h.md)

[op\_agg\_cli.h](op__agg__cli_8h.md)

[op\_agg\_srv.h](op__agg__srv_8h.md)

[priv\_beacon\_cli.h](priv__beacon__cli_8h.md)

[priv\_beacon\_srv.h](priv__beacon__srv_8h.md)

[proxy.h](proxy_8h.md)

Proxy APIs.

[rpr\_cli.h](rpr__cli_8h.md)

[rpr\_srv.h](rpr__srv_8h.md)

[sar\_cfg\_cli.h](sar__cfg__cli_8h.md)

Bluetooth Mesh SAR Configuration Client Model APIs.

[sar\_cfg\_srv.h](sar__cfg__srv_8h.md)

Bluetooth Mesh SAR Configuration Server Model APIs.

[sol\_pdu\_rpl\_cli.h](sol__pdu__rpl__cli_8h.md)

[sol\_pdu\_rpl\_srv.h](sol__pdu__rpl__srv_8h.md)

[statistic.h](statistic_8h.md)

Bluetooth Mesh statistic APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh.h](mesh_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
