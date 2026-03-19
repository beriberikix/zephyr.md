---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__key.html
original_path: doxygen/html/structieee802154__key.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_key Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Key configuration for transmit security offloading, see [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0 "IEEE802154_CONFIG_MAC_KEYS").
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [key\_value](#a01b760f3e622ad0a60888170e5688b9d) |
|  | Key material. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [key\_frame\_counter](#a357419c2d16a527a2417f4eded566aac) |
|  | Initial value of frame counter associated with the key, see section 9.4.3. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [frame\_counter\_per\_key](#a5ca5258422db14b99fd37e7126cfc85d) |
|  | Indicates if per-key frame counter should be used, see section 9.4.3. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_id\_mode](#a732a2a89e74139bd1d8e9b358c0306c7) |
|  | Key Identifier Mode, see section 9.4.2.3, Table 9-7. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [key\_id](#ae0a1e354b5718e8135fb6198ea12276a) |
|  | Key Identifier, see section 9.4.4. |

## Detailed Description

Key configuration for transmit security offloading, see [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0 "IEEE802154_CONFIG_MAC_KEYS").

## Field Documentation

## [◆ ](#a5ca5258422db14b99fd37e7126cfc85d)frame\_counter\_per\_key

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_key::frame\_counter\_per\_key |
| --- |

Indicates if per-key frame counter should be used, see section 9.4.3.

## [◆ ](#a357419c2d16a527a2417f4eded566aac)key\_frame\_counter

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_key::key\_frame\_counter |
| --- |

Initial value of frame counter associated with the key, see section 9.4.3.

## [◆ ](#ae0a1e354b5718e8135fb6198ea12276a)key\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_key::key\_id |
| --- |

Key Identifier, see section 9.4.4.

## [◆ ](#a732a2a89e74139bd1d8e9b358c0306c7)key\_id\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_key::key\_id\_mode |
| --- |

Key Identifier Mode, see section 9.4.2.3, Table 9-7.

## [◆ ](#a01b760f3e622ad0a60888170e5688b9d)key\_value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_key::key\_value |
| --- |

Key material.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_key](structieee802154__key.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
