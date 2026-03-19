---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/index.html
original_path: connectivity/networking/api/index.html
---

# Networking APIs

Zephyr provides support for the standard BSD socket APIs (defined in
[include/zephyr/net/socket.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socket.h)) for the applications to
use. See [BSD socket API](sockets.md#bsd-sockets-interface) for more details.

Apart of the standard API, Zephyr provides a set of custom networking APIs and
libraries for the application to use. See the list below for details.

Note

The legacy connectivity API in [include/zephyr/net/net\_context.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_context.h)
should not be used by applications.
