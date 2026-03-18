---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/mdns_responder/README.html
original_path: samples/net/mdns_responder/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# mDNS responder

## Overview

This application will wait mDNS queries for a pre-defined hostname and
respond to them. The default hostname is **zephyr** and it is set in the
`prj.conf` file.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)
- avahi or similar mDNS capable application that is able to query mDNS
  information.

## Building and Running

Build and run the mdns-responder sample application like this:

```shell
west build -b <board to use> samples/net/mdns_responder -- -DCONF_FILE=<config file to use>
```

After the mdns-responder sample application is started, it will await queries
from the network.

Open a terminal window in your host and type:

```shell
$ avahi-resolve -4 -n zephyr.local
```

If the query is successful, then following information is printed:

```shell
zephyr.local        192.0.2.1
```

For a IPv6 query, type this:

```shell
$ avahi-resolve -6 -n zephyr.local
```

If the query is successful, then following information is printed:

```shell
zephyr.local        2001:db8::1
```

Lastly, resolve services using DNS Service Discovery:

```shell
$ avahi-browse -t -r _zephyr._tcp
```

If the query is successful, then the following information is printed:

```shell
+   zeth IPv6 zephyr                                        _zephyr._tcp         local
=   zeth IPv6 zephyr                                        _zephyr._tcp         local
   hostname = [zephyr.local]
   address = [192.0.2.1]
   port = [4242]
   txt = []
```
