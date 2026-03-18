---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/sockets/big_http_download/README.html
original_path: samples/net/sockets/big_http_download/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Large HTTP download

## Overview

The sockets/big\_http\_download sample application for Zephyr implements
a simple HTTP GET client using a BSD Sockets compatible API. Unlike
the [HTTP GET using plain sockets](../http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.") sample application, it downloads a file of
several megabytes in size, and verifies its integrity using hashing. It
also performs download repeatedly, tracking the total number of bytes
transferred. Thus, it can serve as a “load testing” application for
the Zephyr IP stack.

The source code for this sample application can be found at:
[samples/net/sockets/big\_http\_download](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking
- NAT/routing should be set up to allow connections to the Internet
- DNS server should be available on the host to resolve domain names

## Building and Running

Build the Zephyr version of the application like this:

```shell
west build -b <board_to_use> samples/net/sockets/big_http_download
```

After the sample starts, it issues an HTTP GET request for
[http://archive.ubuntu.com/ubuntu/dists/xenial/main/installer-amd64/current/images/hd-media/vmlinuz](http://archive.ubuntu.com/ubuntu/dists/xenial/main/installer-amd64/current/images/hd-media/vmlinuz)
This site was selected as providing files of variety of sizes, together
with various hashes for them, to ease external selection and verification.
The particular file selected is 6.7MB in size, so it can show how reliably
Zephyr streams non-trivial amounts of data, while still taking a
reasonable amount of time to complete. While the file is downloaded, its
hash is computed (SHA-256 is used in the source code), and an error
message is printed if it differs from the reference value, as specified
in the source code. After a short pause, the process repeats (in an
infinite loop), while the total counter of the bytes received is kept.
Thus the application can be used to test transfers of much larger amounts
of traffic over a longer time.

You can edit the source code to issue a request to any other site on
the Internet (or on the local network, in which case no NAT/routing
setup is needed).

Warning

If you are doing extensive testing with this sample, please reference
a file on a local server or a special-purpose testing server of your own
on the Internet. Using files on archive.ubuntu.com is not recommended for
large-scale testing.

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled, for example, using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/big_http_download -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The TLS version of this sample downloads a file from
[https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/git/1:2.34.1-1ubuntu1/git\_2.34.1.orig.tar.xz](https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/git/1:2.34.1-1ubuntu1/git_2.34.1.orig.tar.xz)
(6.6MB). The certificates used by the sample are in the sample’s `src`
directory and are used to access the default website configured in the sample
for TLS communication ([https://launchpad.net](https://launchpad.net)) and possible redirects. To access
a different web page over TLS, you’ll need to provide a different certificate
to authenticate to that server.

Note, that TLS support in the sample depends on non-posix, TLS socket
functionality. Therefore, it is only possible to run TLS in this sample
on Zephyr.

### Running application on POSIX Host

The same application source code can be built for a POSIX system, e.g.
Linux.

To build:

```shell
$ make -f Makefile.host
```

To run:

```shell
$ ./big_http_download
```

The behavior of the application is the same as the Zephyr version.
