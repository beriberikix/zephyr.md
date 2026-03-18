---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hci__raw__cmd__ext.html
original_path: doxygen/html/structbt__hci__raw__cmd__ext.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_raw\_cmd\_ext Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [HCI RAW channel](group__hci__raw.md)

`#include <[hci_raw.h](hci__raw_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [op](#a3b6fb18d5fabcc5f10265d9de3e46c48) |
|  | Opcode of the command. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [min\_len](#a04041d07145923ffb7116136e3c70ffa) |
|  | Minimal length of the command. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [func](#a364aa7239debd06655d7e51f2eb28ee5) )(struct [net\_buf](structnet__buf.md) \*buf) |
|  | Handler function. |

## Field Documentation

## [◆ ](#a364aa7239debd06655d7e51f2eb28ee5)func

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_hci\_raw\_cmd\_ext::func) (struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Handler function.

Handler function to be called when a command is intercepted.

Parameters
:   | buf | Buffer containing the command. |
    | --- | --- |

Returns
:   HCI Status code or BT\_HCI\_ERR\_EXT\_HANDLED if command has been handled already and a response has been sent as oppose to BT\_HCI\_ERR\_SUCCESS which just indicates that the command can be sent to the controller to be processed.

## [◆ ](#a04041d07145923ffb7116136e3c70ffa)min\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_hci\_raw\_cmd\_ext::min\_len |
| --- |

Minimal length of the command.

## [◆ ](#a3b6fb18d5fabcc5f10265d9de3e46c48)op

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_raw\_cmd\_ext::op |
| --- |

Opcode of the command.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_raw.h](hci__raw_8h_source.md)

- [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
