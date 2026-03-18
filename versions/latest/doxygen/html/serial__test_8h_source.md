---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/serial__test_8h_source.html
original_path: doxygen/html/serial__test_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

serial\_test.h

[Go to the documentation of this file.](serial__test_8h.md)

1/\*

2 \* Copyright 2022 The ChromiumOS Authors.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_SERIAL\_TEST\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_SERIAL\_TEST\_H\_

9

10#include <[errno.h](errno_8h.md)>

11

12#include <[zephyr/device.h](device_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif /\* \_\_cplusplus \*/

17

[ 32](serial__test_8h.md#a2b7d97302cb3546cfc8f384f4a7c1a4a)int [serial\_vnd\_queue\_in\_data](serial__test_8h.md#a2b7d97302cb3546cfc8f384f4a7c1a4a)(const struct [device](structdevice.md) \*dev, const unsigned char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

33

[ 41](serial__test_8h.md#a4275edbc443677d2c0f08100834977a7)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [serial\_vnd\_out\_data\_size\_get](serial__test_8h.md#a4275edbc443677d2c0f08100834977a7)(const struct [device](structdevice.md) \*dev);

42

[ 61](serial__test_8h.md#ab9b60bf8d62db2be3ad530cd0a78aedd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [serial\_vnd\_read\_out\_data](serial__test_8h.md#ab9b60bf8d62db2be3ad530cd0a78aedd)(const struct [device](structdevice.md) \*dev, unsigned char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

62

[ 81](serial__test_8h.md#a1e2a3d82504b34d5b4590afc67172c9e)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [serial\_vnd\_peek\_out\_data](serial__test_8h.md#a1e2a3d82504b34d5b4590afc67172c9e)(const struct [device](structdevice.md) \*dev, unsigned char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

82

[ 89](serial__test_8h.md#a04f02df85d720ccd5ce02ab9e217dba3)typedef void (\*[serial\_vnd\_write\_cb\_t](serial__test_8h.md#a04f02df85d720ccd5ce02ab9e217dba3))(const struct [device](structdevice.md) \*dev, void \*user\_data);

90

[ 99](serial__test_8h.md#a4908343c26e5846abf977befe2c5dbbe)void [serial\_vnd\_set\_callback](serial__test_8h.md#a4908343c26e5846abf977befe2c5dbbe)(const struct [device](structdevice.md) \*dev, [serial\_vnd\_write\_cb\_t](serial__test_8h.md#a04f02df85d720ccd5ce02ab9e217dba3) callback,

100 void \*user\_data);

101

102#ifdef \_\_cplusplus

103}

104#endif /\* \_\_cplusplus \*/

105

106#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_SERIAL\_TEST\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[serial\_vnd\_write\_cb\_t](serial__test_8h.md#a04f02df85d720ccd5ce02ab9e217dba3)

void(\* serial\_vnd\_write\_cb\_t)(const struct device \*dev, void \*user\_data)

Callback called after bytes written to the virtual serial port.

**Definition** serial\_test.h:89

[serial\_vnd\_peek\_out\_data](serial__test_8h.md#a1e2a3d82504b34d5b4590afc67172c9e)

uint32\_t serial\_vnd\_peek\_out\_data(const struct device \*dev, unsigned char \*data, uint32\_t size)

Peek at data written to virtual serial port.

[serial\_vnd\_queue\_in\_data](serial__test_8h.md#a2b7d97302cb3546cfc8f384f4a7c1a4a)

int serial\_vnd\_queue\_in\_data(const struct device \*dev, const unsigned char \*data, uint32\_t size)

Queues data to be read by the virtual serial port.

[serial\_vnd\_out\_data\_size\_get](serial__test_8h.md#a4275edbc443677d2c0f08100834977a7)

uint32\_t serial\_vnd\_out\_data\_size\_get(const struct device \*dev)

Returns size of unread written data.

[serial\_vnd\_set\_callback](serial__test_8h.md#a4908343c26e5846abf977befe2c5dbbe)

void serial\_vnd\_set\_callback(const struct device \*dev, serial\_vnd\_write\_cb\_t callback, void \*user\_data)

Sets the write callback on a virtual serial port.

[serial\_vnd\_read\_out\_data](serial__test_8h.md#ab9b60bf8d62db2be3ad530cd0a78aedd)

uint32\_t serial\_vnd\_read\_out\_data(const struct device \*dev, unsigned char \*data, uint32\_t size)

Read data written to virtual serial port.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [serial\_test.h](serial__test_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
