---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/zperf.html
original_path: connectivity/networking/api/zperf.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zperf: Network Traffic Generator

## [Overview](#id1)

zperf is a shell utility which allows to generate network traffic in Zephyr. The
tool may be used to evaluate network bandwidth.

zperf is compatible with iPerf\_2.0.5. Note that in newer iPerf versions,
an error message like this is printed and the server reported statistics
are missing.

```shell
LAST PACKET NOT RECEIVED!!!
```

zperf can be enabled in any application, a dedicated sample is also present
in Zephyr. See [zperf sample application](../../../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.") for details.

## [Sample Usage](#id2)

If Zephyr acts as a client, iPerf must be executed in server mode.
For example, the following command line must be used for UDP testing:

```shell
$ iperf -s -l 1K -u -V -B 2001:db8::2
```

For TCP testing, the command line would look like this:

```shell
$ iperf -s -l 1K -V -B 2001:db8::2
```

In the Zephyr console, zperf can be executed as follows:

```shell
zperf udp upload 2001:db8::2 5001 10 1K 1M
```

For TCP the zperf command would look like this:

```shell
zperf tcp upload 2001:db8::2 5001 10 1K 1M
```

If the IP addresses of Zephyr and the host machine are specified in the
config file, zperf can be started as follows:

```shell
zperf udp upload2 v6 10 1K 1M
```

or like this if you want to test TCP:

```shell
zperf tcp upload2 v6 10 1K 1M
```

If Zephyr is acting as a server, set the download mode as follows for UDP:

```shell
zperf udp download 5001
```

or like this for TCP:

```shell
zperf tcp download 5001
```

and in the host side, iPerf must be executed with the following
command line if you are testing UDP:

```shell
$ iperf -l 1K -u -V -c 2001:db8::1 -p 5001
```

and this if you are testing TCP:

```shell
$ iperf -l 1K -V -c 2001:db8::1 -p 5001
```

iPerf output can be limited by using the -b option if Zephyr is not
able to receive all the packets in orderly manner.
