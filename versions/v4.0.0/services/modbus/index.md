---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/modbus/index.html
original_path: services/modbus/index.html
---

# Modbus

Modbus is an industrial messaging protocol. The protocol is specified
for different types of networks or buses. Zephyr OS implementation
supports communication over serial line and may be used
with different physical interfaces, like RS485 or RS232.
TCP support is not implemented directly, but there are helper functions
to realize TCP support according to the application’s needs.

Modbus communication is based on client/server model.
Only one client may be present on the bus. Client can communicate with several
server devices. Server devices themselves are passive and must not send
requests or unsolicited responses.
Services requested by the client are specified by function codes (FCxx),
and can be found in the specification or documentation of the API below.

Zephyr RTOS implementation supports both client and server roles.

More information about Modbus and Modbus RTU can be found on the website
[MODBUS Protocol Specifications](https://www.modbus.org/specs.php).

## Samples

- [Modbus RTU server](../../samples/subsys/modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.") and [Modbus RTU client](../../samples/subsys/modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.") samples give
  the possibility to try out RTU server and RTU client implementation with an evaluation board.
- [Modbus TCP server](../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.") sample is a simple Modbus TCP server.
- [Modbus TCP-to-serial gateway](../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.") sample shows how to build a TCP to serial line
  gateway with Zephyr OS.

## API Reference

[MODBUS](../../doxygen/html/group__modbus.md)

Related code samples

- [Modbus RTU client](../../samples/subsys/modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.")Communicate with a Modbus RTU server.
- [Modbus RTU server](../../samples/subsys/modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.")Implement a Modbus RTU server exposing Modbus commands to control LEDs.
- [Modbus TCP server](../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")Implement a Modbus TCP server exposing Modbus commands to control LEDs.
- [Modbus TCP-to-serial gateway](../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.
