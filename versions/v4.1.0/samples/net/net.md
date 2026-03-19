---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/net.html
original_path: samples/net/net.html
---

# Networking

These samples demonstrate how to use the networking subsystem.

- [802.15.4 "serial-radio"](wpan_serial/README.md#wpan-serial "Implement a slip-radio device for Contiki-based border routers.")Implement a slip-radio device for Contiki-based border routers.
- [Cellular modem](cellular_modem/README.md#cellular-modem "Use a cellular modem to communicate with a UDP server.")Use a cellular modem to communicate with a UDP server.
- [DHCPv4 client](dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.
- [DNS resolve](dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")Resolve an IP address for a given hostname.
- [DSA (Distributed Switch Architecture)](dsa/README.md#dsa "Test and debug Distributed Switch Architecture")Test and debug Distributed Switch Architecture
- [gPTP](gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.")Enable gPTP support and monitor functionality using net-shell.
- [IPv4 autoconf client](ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")Perform IPv4 autoconfiguration and self-assign a random IPv4 address
- [Link Layer Discovery Protocol (LLDP)](lldp/README.md#lldp "Enable LLDP support and setup VLANs.")Enable LLDP support and setup VLANs.
- [LwM2M client](lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server.")Implement a LwM2M client that connects to a LwM2M server.
- [mDNS responder](mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")Listen and respond to mDNS queries.
- [MQTT publisher](mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.")Send MQTT PUBLISH messages to an MQTT server.
- [MQTT-SN publisher](mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.")Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.
- [Network packet capture](capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.")Capture network packets and send them to a remote host via IPIP tunnel.
- [Network statistics](stats/README.md#net-stats "Query and display network statistics from a user application.")Query and display network statistics from a user application.
- [Prometheus Sample](prometheus/README.md#prometheus "Implement a Prometheus Metric Server demonstrating various metric types.")Implement a Prometheus Metric Server demonstrating various metric types.
- [Promiscuous mode](promiscuous_mode/README.md#net-promiscuous-mode "Enable promiscuous mode on all interfaces and print information about incoming packets.")Enable promiscuous mode on all interfaces and print information about incoming packets.
- [PTP](ptp/README.md#ptp "Enable PTP support and monitor messages and events via logging.")Enable PTP support and monitor messages and events via logging.
- [Remote syslog](syslog_net/README.md#syslog-net "Enable a remote syslog service that sends syslog messages to a remote server")Enable a remote syslog service that sends syslog messages to a remote server
- [Secure MQTT Sensor/Actuator](secure_mqtt_sensor_actuator/README.md#secure-mqtt-sensor-actuator "Implement an MQTT-based IoT sensor/actuator device")Implement an MQTT-based IoT sensor/actuator device
- [Telnet console](telnet/README.md#telnet-console "Access Zephyr shell over telnet.")Access Zephyr shell over telnet.
- [TFTP client](tftp_client/README.md#tftp-client "Use the TFTP client library to get/put files from/to a TFTP server.")Use the TFTP client library to get/put files from/to a TFTP server.
- [Virtual LAN](vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")Setup two virtual LAN networks and use net-shell to view the networks' settings.
- [Virtual network interface](virtual/README.md#virtual-network-interface "Create a sample virtual network interface.")Create a sample virtual network interface.
- [zperf: Network Traffic Generator](zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.")Use the zperf shell utility to evaluate network bandwidth.

## [IoT Cloud](cloud/README.md)

- [AWS IoT Core MQTT](cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [Microsoft Azure IoT Hub MQTT](cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")Connect to Azure IoT Hub and publish messages using MQTT.
- [TagoIO HTTP Post](cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

## [OpenThread](openthread/README.md)

- [OpenThread co-processor](openthread/coprocessor/README.md#openthread-coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")Build a Thread border-router using OpenThread's co-processor designs.
- [OpenThread CoAP client and server application](openthread/coap/README.md#ot-coap "Build a Full Thread Device (FTD) CoAP server and client.")Build a Full Thread Device (FTD) CoAP server and client.
- [OpenThread shell](openthread/shell/README.md#openthread-shell "Test Thread and IEEE 802.15.4 using the OpenThread shell.")Test Thread and IEEE 802.15.4 using the OpenThread shell.

## [Sockets API](sockets/sockets.md)

- [Asynchronous echo server using poll()](sockets/echo_async/README.md#async-sockets-echo "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()
- [Asynchronous echo server using select()](sockets/echo_async_select/README.md#async-sockets-echo-select "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()
- [CoAP client](sockets/coap_client/README.md#coap-client "Use the CoAP library to implement a client that fetches a resource.")Use the CoAP library to implement a client that fetches a resource.
- [CoAP download](sockets/coap_download/README.md#coap-download "Use the CoAP client API to download data via a GET request")Use the CoAP client API to download data via a GET request
- [CoAP service](sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.")Use the CoAP server subsystem to register CoAP resources.
- [Dumb HTTP server](sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")Implement a simple, portable, HTTP server using BSD sockets.
- [Dumb HTTP server (multi-threaded)](sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")Implement a simple HTTP server supporting simultaneous connections using BSD sockets.
- [Echo client (advanced)](sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")Implement a client that sends IP packets, waits for data to be sent back, and verifies it.
- [Echo server (advanced)](sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")Implement a UDP/TCP server that sends received packets back to the sender.
- [Echo server (service)](sockets/echo_service/README.md#sockets-service-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.
- [Echo server (simple)](sockets/echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.
- [HTTP Client](sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [HTTP GET using plain sockets](sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")Implement an HTTP(S) client using plain BSD sockets.
- [HTTP Server](sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")Implement an HTTP(s) Server demonstrating various resource types.
- [Large HTTP download](sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")Download a large file from a web server using BSD sockets.
- [Network management socket](sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")Listen to network management events using a network management socket.
- [Packet socket](sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")Use raw packet sockets over Ethernet.
- [SNTP client](sockets/sntp_client/README.md#sntp-client "Use SNTP to get the current time from the host.")Use SNTP to get the current time from the host.
- [SocketCAN](sockets/can/README.md#socket-can "Send and receive raw CAN frames using BSD sockets API.")Send and receive raw CAN frames using BSD sockets API.
- [Socketpair](sockets/socketpair/README.md#sockets-socketpair "Implement communication between threads using socket pairs.")Implement communication between threads using socket pairs.
- [TCP sample for TTCN-3 based sanity check](sockets/tcp/README.md#sockets-tcp-sample "Use TTCN-3 to validate the functionality of the TCP stack.")Use TTCN-3 to validate the functionality of the TCP stack.
- [UDP sender using SO\_TXTIME](sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")Control the transmission time of a packet using SO\_TXTIME socket option.
- [WebSocket Client](sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")Implement a Websocket client that connects to a Websocket server.

## [Wi-Fi](wifi/README.md)

- [Wi-Fi AP-STA mode](wifi/apsta_mode/README.md#wifi-ap-sta-mode "Configure a Wi-Fi board to operate as both an Access Point (AP) and a Station (STA).")Configure a Wi-Fi board to operate as both an Access Point (AP) and a Station (STA).
- [Wi-Fi shell](wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")Test Wi-Fi functionality using the Wi-Fi shell module.
