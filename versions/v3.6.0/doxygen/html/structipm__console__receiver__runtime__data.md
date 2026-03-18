---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipm__console__receiver__runtime__data.html
original_path: doxygen/html/structipm__console__receiver__runtime__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm\_console\_receiver\_runtime\_data Struct Reference

`#include <[ipm_console.h](ipm__console_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ring\_buf](structring__buf.md) | [rb](#ae80a0417e9367be13b1882700da1787e) |
|  | Buffer for received bytes from the low-level IPM device. |
| struct k\_sem | [sem](#a533b6ede3eb1d26ee435b3d8c060ef5a) |
|  | Semaphore to wake up the thread to print out messages. |
| const struct [device](structdevice.md) \* | [ipm\_device](#a18851d2abe3e8fc6b0baf65ad95785c8) |
|  | pointer to the bound low-level IPM device |
| int | [channel\_disabled](#a52e52921cb31c30ef78e27c7359855e9) |
|  | Indicator that the channel is temporarily disabled due to full buffer. |
| struct [k\_thread](structk__thread.md) | [rx\_thread](#a614fc792b330f4145bd149f2a968681d) |
|  | Receiver worker thread. |

## Field Documentation

## [◆ ](#a52e52921cb31c30ef78e27c7359855e9)channel\_disabled

| int ipm\_console\_receiver\_runtime\_data::channel\_disabled |
| --- |

Indicator that the channel is temporarily disabled due to full buffer.

## [◆ ](#a18851d2abe3e8fc6b0baf65ad95785c8)ipm\_device

| const struct [device](structdevice.md)\* ipm\_console\_receiver\_runtime\_data::ipm\_device |
| --- |

pointer to the bound low-level IPM device

## [◆ ](#ae80a0417e9367be13b1882700da1787e)rb

| struct [ring\_buf](structring__buf.md) ipm\_console\_receiver\_runtime\_data::rb |
| --- |

Buffer for received bytes from the low-level IPM device.

## [◆ ](#a614fc792b330f4145bd149f2a968681d)rx\_thread

| struct [k\_thread](structk__thread.md) ipm\_console\_receiver\_runtime\_data::rx\_thread |
| --- |

Receiver worker thread.

## [◆ ](#a533b6ede3eb1d26ee435b3d8c060ef5a)sem

| struct k\_sem ipm\_console\_receiver\_runtime\_data::sem |
| --- |

Semaphore to wake up the thread to print out messages.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[ipm\_console.h](ipm__console_8h_source.md)

- [ipm\_console\_receiver\_runtime\_data](structipm__console__receiver__runtime__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
