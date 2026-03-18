---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/uart__mux_8h_source.html
original_path: doxygen/html/uart__mux_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mux.h

[Go to the documentation of this file.](uart__mux_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_MUX\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_MUX\_H\_

14

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29struct gsm\_dlci;

30

[ 42](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3)typedef void (\*[uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3))(const struct [device](structdevice.md) \*mux,

43 int dlci\_address,

44 bool connected, void \*user\_data);

45

[ 47](structuart__mux__driver__api.md)\_\_subsystem struct [uart\_mux\_driver\_api](structuart__mux__driver__api.md) {

[ 53](structuart__mux__driver__api.md#a600ea39ef3bcfcd8949ab3f38c8a454c) struct uart\_driver\_api [uart\_api](structuart__mux__driver__api.md#a600ea39ef3bcfcd8949ab3f38c8a454c);

54

[ 59](structuart__mux__driver__api.md#a312a7c8724c885d9f8fdcd9434ce44c2) int (\*[attach](structuart__mux__driver__api.md#a312a7c8724c885d9f8fdcd9434ce44c2))(const struct [device](structdevice.md) \*mux, const struct [device](structdevice.md) \*uart,

60 int dlci\_address, [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3) cb,

61 void \*user\_data);

62};

63

[ 76](group__uart__mux__interface.md#gaae2cc4e03f5e4536b945746cf689fe56)static inline int [uart\_mux\_attach](group__uart__mux__interface.md#gaae2cc4e03f5e4536b945746cf689fe56)(const struct [device](structdevice.md) \*mux,

77 const struct [device](structdevice.md) \*uart,

78 int dlci\_address, [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3) cb,

79 void \*user\_data)

80{

81 const struct [uart\_mux\_driver\_api](structuart__mux__driver__api.md) \*api =

82 (const struct [uart\_mux\_driver\_api](structuart__mux__driver__api.md) \*)mux->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

83

84 return api->[attach](structuart__mux__driver__api.md#a312a7c8724c885d9f8fdcd9434ce44c2)(mux, uart, dlci\_address, cb, user\_data);

85}

86

[ 94](group__uart__mux__interface.md#ga551b58a43626981af2be757f44206ccc)\_\_syscall const struct [device](structdevice.md) \*[uart\_mux\_find](group__uart__mux__interface.md#ga551b58a43626981af2be757f44206ccc)(int dlci\_address);

95

[ 107](group__uart__mux__interface.md#gaac6d68c5f53f60b5dfb1191a85429144)const struct [device](structdevice.md) \*[uart\_mux\_alloc](group__uart__mux__interface.md#gaac6d68c5f53f60b5dfb1191a85429144)(void);

108

[ 118](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d)typedef void (\*[uart\_mux\_cb\_t](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d))(const struct [device](structdevice.md) \*uart,

119 const struct [device](structdevice.md) \*dev,

120 int dlci\_address, void \*user\_data);

121

[ 129](group__uart__mux__interface.md#gae7f1271a6fac1edd388bd8add3b01614)void [uart\_mux\_foreach](group__uart__mux__interface.md#gae7f1271a6fac1edd388bd8add3b01614)([uart\_mux\_cb\_t](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d) cb, void \*user\_data);

130

[ 139](group__uart__mux__interface.md#ga3e9871415092eba11a7be262ae4da0a2)void [uart\_mux\_disable](group__uart__mux__interface.md#ga3e9871415092eba11a7be262ae4da0a2)(const struct [device](structdevice.md) \*dev);

140

[ 148](group__uart__mux__interface.md#gad832440ec0f4157fc895a1ec05081337)void [uart\_mux\_enable](group__uart__mux__interface.md#gad832440ec0f4157fc895a1ec05081337)(const struct [device](structdevice.md) \*dev);

149

150#ifdef \_\_cplusplus

151}

152#endif

153

154#include <syscalls/uart\_mux.h>

155

159

160#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_MUX\_H\_ \*/

[device.h](device_8h.md)

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[uart\_mux\_cb\_t](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d)

void(\* uart\_mux\_cb\_t)(const struct device \*uart, const struct device \*dev, int dlci\_address, void \*user\_data)

Callback used while iterating over UART muxes.

**Definition** uart\_mux.h:118

[uart\_mux\_disable](group__uart__mux__interface.md#ga3e9871415092eba11a7be262ae4da0a2)

void uart\_mux\_disable(const struct device \*dev)

Disable the mux.

[uart\_mux\_find](group__uart__mux__interface.md#ga551b58a43626981af2be757f44206ccc)

const struct device \* uart\_mux\_find(int dlci\_address)

Get UART related to a specific DLCI channel.

[uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3)

void(\* uart\_mux\_attach\_cb\_t)(const struct device \*mux, int dlci\_address, bool connected, void \*user\_data)

Define the user callback function which is called when the UART mux is attached properly.

**Definition** uart\_mux.h:42

[uart\_mux\_alloc](group__uart__mux__interface.md#gaac6d68c5f53f60b5dfb1191a85429144)

const struct device \* uart\_mux\_alloc(void)

Allocate muxing UART device.

[uart\_mux\_attach](group__uart__mux__interface.md#gaae2cc4e03f5e4536b945746cf689fe56)

static int uart\_mux\_attach(const struct device \*mux, const struct device \*uart, int dlci\_address, uart\_mux\_attach\_cb\_t cb, void \*user\_data)

Attach physical/real UART to UART muxing device.

**Definition** uart\_mux.h:76

[uart\_mux\_enable](group__uart__mux__interface.md#gad832440ec0f4157fc895a1ec05081337)

void uart\_mux\_enable(const struct device \*dev)

Enable the mux.

[uart\_mux\_foreach](group__uart__mux__interface.md#gae7f1271a6fac1edd388bd8add3b01614)

void uart\_mux\_foreach(uart\_mux\_cb\_t cb, void \*user\_data)

Go through all the UART muxes and call callback for each of them.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[uart\_mux\_driver\_api](structuart__mux__driver__api.md)

UART mux driver API structure.

**Definition** uart\_mux.h:47

[uart\_mux\_driver\_api::attach](structuart__mux__driver__api.md#a312a7c8724c885d9f8fdcd9434ce44c2)

int(\* attach)(const struct device \*mux, const struct device \*uart, int dlci\_address, uart\_mux\_attach\_cb\_t cb, void \*user\_data)

Attach the mux to this UART.

**Definition** uart\_mux.h:59

[uart\_mux\_driver\_api::uart\_api](structuart__mux__driver__api.md#a600ea39ef3bcfcd8949ab3f38c8a454c)

struct uart\_driver\_api uart\_api

The uart\_driver\_api must be placed in first position in this struct so that we are compatible with ua...

**Definition** uart\_mux.h:53

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_mux.h](uart__mux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
