---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/modem/index.html
original_path: services/modem/index.html
---

# Modem modules

This service provides modules necessary to communicate with modems.

Modems are self-contained devices that implement the hardware and
software necessary to perform RF (Radio-Frequency) communication,
including GNSS, Cellular, WiFi etc.

The modem modules are inter-connected dynamically using
data-in/data-out pipes making them independently testable and
highly flexible, ensuring stability and scalability.

## Modem pipe

This module is used to abstract data-in/data-out communication over
a variety of mechanisms, like UART and CMUX DLCI channels, in a
thread-safe manner.

A modem backend will internally contain an instance of a modem\_pipe
structure, alongside any buffers and additional structures required
to abstract away its underlying mechanism.

The modem backend will return a pointer to its internal modem\_pipe
structure when initialized, which will be used to interact with the
backend through the modem pipe API.

[Modem Pipe](../../doxygen/html/group__modem__pipe.md)

## Modem PPP

This module defines and binds a L2 PPP network interface, described in
[L2 Layer Management](../../connectivity/networking/api/net_l2.md#net-l2-interface), to a modem backend. The L2 PPP interface sends
and receives network packets. These network packets have to be wrapped
in PPP frames before being transported via a modem backend. This module
performs said wrapping.

[Modem PPP](../../doxygen/html/group__modem__ppp.md)

## Modem CMUX

This module is an implementation of CMUX following the 3GPP 27.010
specification. CMUX is a multiplexing protocol, allowing for multiple
bi-directional streams of data, called DLCI channels. The module
attaches to a single modem backend, exposing multiple modem backends,
each representing a DLCI channel.

[Modem CMUX](../../doxygen/html/group__modem__cmux.md)

## Modem pipelink

This module is used to share modem pipes globally. This module aims to
decouple the creation and setup of modem pipes in device drivers from
the users of said pipes. See
[drivers/modem/modem\_at\_shell.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/modem_at_shell.c) and
[drivers/modem/modem\_cellular.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/modem_cellular.c) for examples of how to
use the modem pipelink between device driver and application.

[Modem pipelink](../../doxygen/html/group__modem__pipelink.md)
