---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/syslog_net/README.html
original_path: samples/net/syslog_net/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Remote syslog

## Overview

This sample application enables a remote syslog service that will
send syslog messages to a remote server, as configured in `prj.conf`.
See [https://tools.ietf.org/html/rfc5424](https://tools.ietf.org/html/rfc5424) and [https://tools.ietf.org/html/rfc5426](https://tools.ietf.org/html/rfc5426)
for more details about syslog protocol over UDP.

The source code for this sample application can be found at:
[samples/net/syslog\_net](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/syslog_net).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

For configuring the remote IPv6 syslog server, set the following
variables in prj.conf file:

```cfg
CONFIG_LOG_BACKEND_NET=y
CONFIG_LOG_BACKEND_NET_SERVER="[2001:db8::2]:514"
```

Default port number is 514 if user does not specify a value.
The following syntax is supported for the server address
and port:

```shell
192.0.2.1:514
192.0.2.42
[2001:db8::1]:514
[2001:db8::2]
2001:db::42
```

Build syslog\_net sample application like this:

```shell
west build -b <board to use> samples/net/syslog_net -- -DCONF_FILE=<config file to use>
```
