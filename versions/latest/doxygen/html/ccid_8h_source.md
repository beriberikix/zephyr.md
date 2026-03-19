---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ccid_8h_source.html
original_path: doxygen/html/ccid_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccid.h

[Go to the documentation of this file.](ccid_8h.md)

1

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCID\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCID\_H\_

13

26

27#include <[stdint.h](stdint_8h.md)>

28

29#include <[zephyr/bluetooth/gatt.h](gatt_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 36](group__bt__ccid.md#ga1be6ef63b32f44100a77e48c88a9c126)#define BT\_CCID\_MIN 0

[ 38](group__bt__ccid.md#gaae664247d3537ab473c2f533602b2afa)#define BT\_CCID\_MAX 255

39

[ 52](group__bt__ccid.md#gad621dd750e4b1c23791afc72785990fc)int [bt\_ccid\_alloc\_value](group__bt__ccid.md#gad621dd750e4b1c23791afc72785990fc)(void);

53

[ 66](group__bt__ccid.md#ga07845fe5cc445a35448881430f528609)const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[bt\_ccid\_find\_attr](group__bt__ccid.md#ga07845fe5cc445a35448881430f528609)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

67

69

70#ifdef \_\_cplusplus

71}

72#endif

73

74#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCID\_H\_ \*/

[gatt.h](gatt_8h.md)

Generic Attribute Profile handling.

[bt\_ccid\_find\_attr](group__bt__ccid.md#ga07845fe5cc445a35448881430f528609)

const struct bt\_gatt\_attr \* bt\_ccid\_find\_attr(uint8\_t ccid)

Get the GATT attribute of a CCID value.

[bt\_ccid\_alloc\_value](group__bt__ccid.md#gad621dd750e4b1c23791afc72785990fc)

int bt\_ccid\_alloc\_value(void)

Allocates a CCID value.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_gatt\_attr](structbt__gatt__attr.md)

GATT Attribute.

**Definition** gatt.h:227

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [ccid.h](ccid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
