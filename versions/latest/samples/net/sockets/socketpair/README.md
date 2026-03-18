---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/sockets/socketpair/README.html
original_path: samples/net/sockets/socketpair/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Socketpair

## Overview

The sockets/socketpair sample application for Zephyr demonstrates a
multi-threaded application communicating over pairs of unnamed,
connected UNIX-domain sockets. The pairs of sockets are created with
socketpair(2), as you might have guessed. Such sockets are compatible
with the BSD Sockets API, and therefore the purpose of this sample
is also to reinforce that it is possible to develop a sockets
application portable to both POSIX and Zephyr.

The source code for this sample application can be found at:
[samples/net/sockets/socketpair](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/socketpair).

## Requirements

None

## Building and Running

Build the Zephyr version of the sockets/echo application like this:

```shell
west build -b <board_to_use> samples/net/sockets/socketpair
```

After the sample starts, several client threads are spawned. Each client
thread sends a fixed number of messages to the server (main).

```shell
*** Booting Zephyr OS build v3.3.0-rc1-97-g432ff20a72e1 ***
setting-up
Alpha: socketpair: 4 <=> 3
Bravo: socketpair: 6 <=> 5
Charlie: socketpair: 8 <=> 7
main: read 'Alpha' on fd 4
main: read 'Bravo' on fd 6
main: read 'Charlie' on fd 8
main: read 'Alpha' on fd 4
main: read 'Bravo' on fd 6
main: read 'Charlie' on fd 8
main: read 'Alpha' on fd 4
main: read 'Bravo' on fd 6
main: read 'Charlie' on fd 8
tearing-down
SUCCESS
```

### Running application on POSIX Host

The same application source code can be built for a POSIX system, e.g.
Linux.

To build:

```shell
$ make -f Makefile.host
```

To run:

```shell
./socketpair_example
setting-up
Alpha: socketpair: 3 <=> 4
Bravo: socketpair: 5 <=> 6
Charlie: socketpair: 7 <=> 8
main: read 'Alpha' on fd 3
main: read 'Bravo' on fd 5
main: read 'Charlie' on fd 7
main: read 'Alpha' on fd 3
main: read 'Alpha' on fd 3
main: read 'Bravo' on fd 5
main: read 'Charlie' on fd 7
main: read 'Bravo' on fd 5
main: read 'Charlie' on fd 7
tearing-down
SUCCESS
```

As can be seen, the behavior of the application is approximately the same as
the Zephyr version.
