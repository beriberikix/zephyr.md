---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/modules/thrift/hello/README.html
original_path: samples/modules/thrift/hello/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Thrift sample

![Thrift Layers](../../../../_images/thrift-layers.png)

## What is Thrift?

[Apache Thrift](https://github.com/apache/thrift) is an [IDL](https://en.wikipedia.org/wiki/Interface_description_language) specification, [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) framework, and
[code generator](https://en.wikipedia.org/wiki/Automatic_programming). It works across all major operating systems, supports over
27 programming languages, 7 protocols, and 6 low-level transports. Thrift was
originally developed at [Facebook in 2006](https://thrift.apache.org/static/files/thrift-20070401.pdf) and then shared with the
[Apache Software Foundation](https://www.apache.org). Thrift supports a rich set of types and data
structures, and abstracts away transport and protocol details, which lets
developers focus on application logic.

## Overview

This sample application includes a client and server implementing the RPC
interface described in [samples/modules/thrift/hello/hello.thrift](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/thrift/hello/hello.thrift).
The purpose of this example is to demonstrate how components at different
layers in thrift can be combined to build an application with desired features.

## Requirements

- Optional Modules

Download optional modules with west

```shell
west config manifest.group-filter -- +optional
west update
```

- QEMU Networking (described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu))
- Thrift dependencies installed for your host OS

UbuntumacOS

Install thrift dependencies in Ubuntu

```shell
 sudo apt install -y libboost-all-dev thrift-compiler libthrift-dev
```

Install thrift dependencies in macOS

```shell
 brew install boost openssl thrift
```

## Building and Running

This application can be run on a Linux host, with either the server or the
client in the QEMU environment, and the peer is built and run natively on
the host.

### Building the Native Client and Server

```shell
$ make -j -C samples/modules/thrift/hello/client/
$ make -j -C samples/modules/thrift/hello/server/
```

Under `client/`, 3 executables will be generated, and components
used in each layer of them are listed below:

| hello\_client | TSocket | TBufferedTransport | TBinaryProtocol |
| --- | --- | --- | --- |
| hello\_client\_compact | TSocket | TBufferedTransport | TCompactProtocol |
| hello\_client\_ssl | TSSLSocket | TBufferedTransport | TBinaryProtocol |

The same applies for the server. Only the client and the server with the
same set of stacks can communicate.

Additionally, there is a `hello_client.py` Python script that can be used
interchangeably with the `hello_client` C++ application to illustrate the
cross-language capabilities of Thrift.

| hello\_client.py | TSocket | TBufferedTransport | TBinaryProtocol |
| --- | --- | --- | --- |

### Running the Zephyr Server in QEMU

Build the Zephyr version of the `hello/server` sample application like this:

```shell
west build -b board_name samples/modules/thrift/hello/server
```

To enable advanced features, extra arguments should be passed accordingly:

- TCompactProtocol: `-DCONFIG_THRIFT_COMPACT_PROTOCOL=y`
- TSSLSocket: `-DCONF_FILE="prj.conf ../overlay-tls.conf"`

For example, to build for `qemu_x86_64` with TSSLSocket support:

```shell
west build -b qemu_x86_64 samples/modules/thrift/hello/server -- -DCONF_FILE="prj.conf ../overlay-tls.conf"
west build -t run
```

In another terminal, run the `hello_client` sample app compiled for the
host OS:

```shell
$ ./hello_client 192.0.2.1
$ ./hello_client_compact 192.0.2.1
$ ./hello_client_ssl 192.0.2.1 ../native-cert.pem ../native-key.pem ../qemu-cert.pem
```

You should observe the following in the original `hello/server` terminal:

```shell
ping
echo: Hello, world!
counter: 1
counter: 2
counter: 3
counter: 4
counter: 5
```

In the client terminal, run `hello_client.py` app under the host OS (not
described for compact or ssl variants for brevity):

```shell
$ ./hello_client.py
```

You should observe the following in the original `hello/server` terminal.
Note that the server’s state is not discarded (the counter continues to
increase).

```shell
ping
echo: Hello, world!
counter: 6
counter: 7
counter: 8
counter: 9
counter: 10
```

### Running the Zephyr Client in QEMU

In another terminal, run the `hello_server` sample app compiled for the
host OS:

```shell
$ ./hello_server 0.0.0.0
$ ./hello_server_compact 0.0.0.0
$ ./hello_server_ssl 0.0.0.0 ../native-cert.pem ../native-key.pem ../qemu-cert.pem
```

Then, in annother terminal, run the corresponding `hello/client` sample:

```shell
west build -b qemu_x86_64 samples/modules/thrift/hello/client
west build -t run
```

The additional arguments for advanced features are the same as
`hello/server`.

You should observe the following in the original `hello_server` terminal:

```shell
ping
echo: Hello, world!
counter: 1
counter: 2
counter: 3
counter: 4
counter: 5
```
