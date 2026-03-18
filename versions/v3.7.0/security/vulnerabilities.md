---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/security/vulnerabilities.html
original_path: security/vulnerabilities.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Vulnerabilities

This page collects all of the vulnerabilities that are discovered and
fixed in each release. It will also often have more details than is
available in the releases. Some vulnerabilities are deemed to be
sensitive, and will not be publicly discussed until there is
sufficient time to fix them. Because the release notes are locked to
a version, the information here can be updated after the embargo is
lifted.

## CVE-2017

### CVE-2017-14199

Buffer overflow in `getaddrinfo()`.

- [CVE-2017-14199](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14199)
- [Zephyr project bug tracker ZEPSEC-12](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-12)
- [PR6158 fix for 1.11.0](https://github.com/zephyrproject-rtos/zephyr/pull/6158)

### CVE-2017-14201

The shell DNS command can cause unpredictable results due to misuse of
stack variables.

Use After Free vulnerability in the Zephyr shell allows a serial or
telnet connected user to cause denial of service, and possibly remote
code execution.

This has been fixed in release v1.14.0.

- [CVE-2017-14201](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14201)
- [Zephyr project bug tracker ZEPSEC-17](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-17)
- [PR13260 fix for v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/13260)

### CVE-2017-14202

The shell implementation does not protect against buffer overruns
resulting in unpredictable behavior.

Improper Restriction of Operations within the Bounds of a Memory
Buffer vulnerability in the shell component of Zephyr allows a serial
or telnet connected user to cause a crash, possibly with arbitrary
code execution.

This has been fixed in release v1.14.0.

- [CVE-2017-14202](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14202)
- [Zephyr project bug tracker ZEPSEC-18](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-18)
- [PR13048 fix for v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/13048)

## CVE-2019

### CVE-2019-9506

The Bluetooth BR/EDR specification up to and including version 5.1
permits sufficiently low encryption key length and does not prevent an
attacker from influencing the key length negotiation. This allows
practical brute-force attacks (aka “KNOB”) that can decrypt traffic
and inject arbitrary ciphertext without the victim noticing.

- [CVE-2019-9506](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9506)
- [Zephyr project bug tracker ZEPSEC-20](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-20)
- [PR18702 fix for v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/18702)
- [PR18659 fix for v2.0.0](https://github.com/zephyrproject-rtos/zephyr/pull/18659)

## CVE-2020

### CVE-2020-10019

Buffer Overflow vulnerability in USB DFU of zephyr allows a USB
connected host to cause possible remote code execution.

This has been fixed in releases v1.14.2, v2.2.0, and v2.1.1.

- [CVE-2020-10019](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10019)
- [Zephyr project bug tracker ZEPSEC-25](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-25)
- [PR23460 fix for 1.14.x](https://github.com/zephyrproject-rtos/zephyr/pull/23460)
- [PR23457 fix for 2.1.x](https://github.com/zephyrproject-rtos/zephyr/pull/23457)
- [PR23190 fix in 2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23190)

### CVE-2020-10021

Out-of-bounds write in USB Mass Storage with unaligned sizes

Out-of-bounds Write in the USB Mass Storage memoryWrite handler with
unaligned Sizes.

See NCC-ZEP-024, NCC-ZEP-025, NCC-ZEP-026

This has been fixed in releases v1.14.2, and v2.2.0.

- [CVE-2020-10021](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10021)
- [Zephyr project bug tracker ZEPSEC-26](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-26)
- [PR23455 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23455)
- [PR23456 fix for the v2.1 branch](https://github.com/zephyrproject-rtos/zephyr/pull/23456)
- [PR23240 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23240)

### CVE-2020-10022

UpdateHub Module Copies a Variable-Size Hash String Into a Fixed-Size Array

A malformed JSON payload that is received from an UpdateHub server may
trigger memory corruption in the Zephyr OS. This could result in a
denial of service in the best case, or code execution in the worst
case.

See NCC-ZEP-016

This has been fixed in the below pull requests for main, branch from
v2.1.0, and branch from v2.2.0.

- [CVE-2020-10022](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10022)
- [Zephyr project bug tracker ZEPSEC-28](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-28)
- [PR24154 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/24154)
- [PR24065 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/24065)
- [PR24066 fix for branch from v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/24066)

### CVE-2020-10023

Shell Subsystem Contains a Buffer Overflow Vulnerability In
shell\_spaces\_trim

The shell subsystem contains a buffer overflow, whereby an adversary
with physical access to the device is able to cause a memory
corruption, resulting in denial of service or possibly code execution
within the Zephyr kernel.

See NCC-ZEP-019

This has been fixed in releases v1.14.2, v2.2.0, and in a branch from
v2.1.0,

- [CVE-2020-10023](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10023)
- [Zephyr project bug tracker ZEPSEC-29](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-29)
- [PR23646 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23646)
- [PR23649 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/23649)
- [PR23304 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23304)

### CVE-2020-10024

ARM Platform Uses Signed Integer Comparison When Validating Syscall
Numbers

The arm platform-specific code uses a signed integer comparison when
validating system call numbers. An attacker who has obtained code
execution within a user thread is able to elevate privileges to that
of the kernel.

See NCC-ZEP-001

This has been fixed in releases v1.14.2, and v2.2.0, and in a branch
from v2.1.0,

- [CVE-2020-10024](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10024)
- [Zephyr project bug tracker ZEPSEC-30](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-30)
- [PR23535 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23535)
- [PR23498 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/23498)
- [PR23323 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23323)

### CVE-2020-10027

ARC Platform Uses Signed Integer Comparison When Validating Syscall
Numbers

An attacker who has obtained code execution within a user thread is
able to elevate privileges to that of the kernel.

See NCC-ZEP-001

This has been fixed in releases v1.14.2, and v2.2.0, and in a branch
from v2.1.0.

- [CVE-2020-10027](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10027)
- [Zephyr project bug tracker ZEPSEC-35](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-35)
- [PR23500 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23500)
- [PR23499 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/23499)
- [PR23328 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23328)

### CVE-2020-10028

Multiple Syscalls In GPIO Subsystem Performs No Argument Validation

Multiple syscalls with insufficient argument validation

See NCC-ZEP-006

This has been fixed in releases v1.14.2, and v2.2.0, and in a branch
from v2.1.0.

- [CVE-2020-10028](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10028)
- [Zephyr project bug tracker ZEPSEC-32](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-32)
- [PR23733 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23733)
- [PR23737 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/23737)
- [PR23308 fix for v2.2.0 (gpio patch)](https://github.com/zephyrproject-rtos/zephyr/pull/23308)

### CVE-2020-10058

Multiple Syscalls In kscan Subsystem Performs No Argument Validation

Multiple syscalls in the Kscan subsystem perform insufficient argument
validation, allowing code executing in userspace to potentially gain
elevated privileges.

See NCC-ZEP-006

This has been fixed in a branch from v2.1.0, and release v2.2.0.

- [CVE-2020-10058](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10058)
- [Zephyr project bug tracker ZEPSEC-34](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-34)
- [PR23748 fix for branch from v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/23748)
- [PR23308 fix for v2.2.0 (kscan patch)](https://github.com/zephyrproject-rtos/zephyr/pull/23308)

### CVE-2020-10059

UpdateHub Module Explicitly Disables TLS Verification

The UpdateHub module disables DTLS peer checking, which allows for a
man in the middle attack. This is mitigated by firmware images
requiring valid signatures. However, there is no benefit to using DTLS
without the peer checking.

See NCC-ZEP-018

This has been fixed in a PR against Zephyr main.

- [CVE-2020-10059](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10059)
- [Zephyr project bug tracker ZEPSEC-36](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-36)
- [PR24954 fix on main (to be fixed in v2.3.0)](https://github.com/zephyrproject-rtos/zephyr/pull/24954)
- [PR24954 fix v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/24999)
- [PR24954 fix v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/24997)

### CVE-2020-10060

UpdateHub Might Dereference An Uninitialized Pointer

In updatehub\_probe, right after JSON parsing is complete, objects[1]
is accessed from the output structure in two different places. If the
JSON contained less than two elements, this access would reference
uninitialized stack memory. This could result in a crash, denial of
service, or possibly an information leak.

Recommend disabling updatehub until such a time as a fix can be made
available.

See NCC-ZEP-030

This has been fixed in a PR against Zephyr main.

- [CVE-2020-10060](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10060)
- [Zephyr project bug tracker ZEPSEC-37](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-37)
- [PR27865 fix on main (to be fixed in v2.4.0)](https://github.com/zephyrproject-rtos/zephyr/pull/27865)
- [PR27865 fix for v2.3.0](https://github.com/zephyrproject-rtos/zephyr/pull/27889)
- [PR27865 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/27891)
- [PR27865 fix for v2.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/27893)

### CVE-2020-10061

Error handling invalid packet sequence

Improper handling of the full-buffer case in the Zephyr Bluetooth
implementation can result in memory corruption.

This has been fixed in branches for v1.14.0, v2.2.0, and will be
included in v2.3.0.

- [CVE-2020-10061](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10061)
- [Zephyr project bug tracker ZEPSEC-75](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-75)
- [PR23516 fix for v2.3 (split driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23516)
- [PR23517 fix for v2.3 (legacy driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23517)
- [PR23091 fix for branch from v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/23091)
- [PR23547 fix for branch from v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23547)

### CVE-2020-10062

Packet length decoding error in MQTT

CVE: An off-by-one error in the Zephyr project MQTT packet length
decoder can result in memory corruption and possible remote code
execution. NCC-ZEP-031

The MQTT packet header length can be 1 to 4 bytes. An off-by-one error
in the code can result in this being interpreted as 5 bytes, which can
cause an integer overflow, resulting in memory corruption.

This has been fixed in main for v2.3.

- [CVE-2020-10062](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10062)
- [Zephyr project bug tracker ZEPSEC-84](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-84)
- [commit 11b7a37d for v2.3](https://github.com/zephyrproject-rtos/zephyr/pull/23821/commits/11b7a37d9a0b438270421b224221d91929843de4)
- [NCC-ZEP report](https://research.nccgroup.com/2020/05/26/research-report-zephyr-and-mcuboot-security-assessment) (NCC-ZEP-031)

### CVE-2020-10063

Remote Denial of Service in CoAP Option Parsing Due To Integer
Overflow

A remote adversary with the ability to send arbitrary CoAP packets to
be parsed by Zephyr is able to cause a denial of service.

This has been fixed in main for v2.3.

- [CVE-2020-10063](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10063)
- [Zephyr project bug tracker ZEPSEC-55](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-55)
- [PR24435 fix in main for v2.3](https://github.com/zephyrproject-rtos/zephyr/pull/24435)
- [PR24531 fix for branch from v2.2](https://github.com/zephyrproject-rtos/zephyr/pull/24531)
- [PR24535 fix for branch from v2.1](https://github.com/zephyrproject-rtos/zephyr/pull/24535)
- [PR24530 fix for branch from v1.14](https://github.com/zephyrproject-rtos/zephyr/pull/24530)
- [NCC-ZEP report](https://research.nccgroup.com/2020/05/26/research-report-zephyr-and-mcuboot-security-assessment) (NCC-ZEP-032)

### CVE-2020-10064

Improper Input Frame Validation in ieee802154 Processing

- [CVE-2020-10064](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10064)
- [Zephyr project bug tracker ZEPSEC-65](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-65)
- [PR24971 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/24971)
- [PR33451 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/33451)

### CVE-2020-10065

OOB Write after not validating user-supplied length (<= 0xffff) and
copying to fixed-size buffer (default: 77 bytes) for HCI\_ACL packets in
bluetooth HCI over SPI driver.

- [CVE-2020-10065](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10065)
- [Zephyr project bug tracker ZEPSEC-66](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-66)
- This issue has not been fixed.

### CVE-2020-10066

Incorrect Error Handling in Bluetooth HCI core

In hci\_cmd\_done, the buf argument being passed as null causes
nullpointer dereference.

- [CVE-2020-10066](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10066)
- [Zephyr project bug tracker ZEPSEC-67](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-67)
- [PR24902 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/24902)
- [PR25089 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/25089)

### CVE-2020-10067

Integer Overflow In is\_in\_region Allows User Thread To Access Kernel Memory

A malicious userspace application can cause a integer overflow and
bypass security checks performed by system call handlers. The impact
would depend on the underlying system call and can range from denial
of service to information leak to memory corruption resulting in code
execution within the kernel.

See NCC-ZEP-005

This has been fixed in releases v1.14.2, and v2.2.0.

- [CVE-2020-10067](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10067)
- [Zephyr project bug tracker ZEPSEC-27](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-27)
- [PR23653 fix for v1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/23653)
- [PR23654 fix for the v2.1 branch](https://github.com/zephyrproject-rtos/zephyr/pull/23654)
- [PR23239 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23239)

### CVE-2020-10068

Zephyr Bluetooth DLE duplicate requests vulnerability

In the Zephyr project Bluetooth subsystem, certain duplicate and
back-to-back packets can cause incorrect behavior, resulting in a
denial of service.

This has been fixed in branches for v1.14.0, v2.2.0, and will be
included in v2.3.0.

- [CVE-2020-10068](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10068)
- [Zephyr project bug tracker ZEPSEC-78](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-78)
- [PR23707 fix for v2.3 (split driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23707)
- [PR23708 fix for v2.3 (legacy driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23708)
- [PR23091 fix for branch from v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/23091)
- [PR23964 fix for v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23964)

### CVE-2020-10069

Zephyr Bluetooth unchecked packet data results in denial of service

An unchecked parameter in bluetooth data can result in an assertion
failure, or division by zero, resulting in a denial of service attack.

This has been fixed in branches for v1.14.0, v2.2.0, and will be
included in v2.3.0.

- [CVE-2020-10069](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10069)
- [Zephyr project bug tracker ZEPSEC-81](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-81)
- [PR23705 fix for v2.3 (split driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23705)
- [PR23706 fix for v2.3 (legacy driver)](https://github.com/zephyrproject-rtos/zephyr/pull/23706)
- [PR23091 fix for branch from v1.14.0](https://github.com/zephyrproject-rtos/zephyr/pull/23091)
- [PR23963 fix for branch from v2.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/23963)

### CVE-2020-10070

MQTT buffer overflow on receive buffer

In the Zephyr Project MQTT code, improper bounds checking can result
in memory corruption and possibly remote code execution. NCC-ZEP-031

When calculating the packet length, arithmetic overflow can result in
accepting a receive buffer larger than the available buffer space,
resulting in user data being written beyond this buffer.

This has been fixed in main for v2.3.

- [CVE-2020-10070](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10070)
- [Zephyr project bug tracker ZEPSEC-85](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-85)
- [commit 0b39cbf3 for v2.3](https://github.com/zephyrproject-rtos/zephyr/pull/23821/commits/0b39cbf3c01d7feec9d0dd7cc7e0e374b6113542)
- [NCC-ZEP report](https://research.nccgroup.com/2020/05/26/research-report-zephyr-and-mcuboot-security-assessment) (NCC-ZEP-031)

### CVE-2020-10071

Insufficient publish message length validation in MQTT

The Zephyr MQTT parsing code performs insufficient checking of the
length field on publish messages, allowing a buffer overflow and
potentially remote code execution. NCC-ZEP-031

This has been fixed in main for v2.3.

- [CVE-2020-10071](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10071)
- [Zephyr project bug tracker ZEPSEC-86](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-86)
- [commit 989c4713 fix for v2.3](https://github.com/zephyrproject-rtos/zephyr/pull/23821/commits/989c4713ba429aa5105fe476b4d629718f3e6082)
- [NCC-ZEP report](https://research.nccgroup.com/2020/05/26/research-report-zephyr-and-mcuboot-security-assessment) (NCC-ZEP-031)

### CVE-2020-10072

All threads can access all socket file descriptors

There is no management of permissions to network socket API file
descriptors. Any thread running on the system may read/write a socket
file descriptor knowing only the numerical value of the file
descriptor.

- [CVE-2020-10072](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10072)
- [Zephyr project bug tracker ZEPSEC-87](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-87)
- [PR25804 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/25804)
- [PR27176 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/27176)

### CVE-2020-10136

IP-in-IP protocol routes arbitrary traffic by default zephyrproject

- [CVE-2020-10136](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10136)
- [Zephyr project bug tracker ZEPSEC-64](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-64)

### CVE-2020-13598

FS: Buffer Overflow when enabling Long File Names in FAT\_FS and calling fs\_stat

Performing fs\_stat on a file with a filename longer than 12
characters long will cause a buffer overflow.

- [CVE-2020-13598](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13598)
- [Zephyr project bug tracker ZEPSEC-88](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-88)
- [PR25852 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/25852)
- [PR28782 fix for v2.3](https://github.com/zephyrproject-rtos/zephyr/pull/28782)
- [PR33577 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/33577)

### CVE-2020-13599

Security problem with settings and littlefs

When settings is used in combination with littlefs all security
related information can be extracted from the device using MCUmgr and
this could be used e.g in bt-mesh to get the device key, network key,
app keys from the device.

- [CVE-2020-13599](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13599)
- [Zephyr project bug tracker ZEPSEC-57](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-57)
- [PR26083 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/26083)

### CVE-2020-13600

Malformed SPI in response for eswifi can corrupt kernel memory

- [CVE-2020-13600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13600)
- [Zephyr project bug tracker ZEPSEC-91](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-91)
- [PR26712 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/26712)

### CVE-2020-13601

Possible read out of bounds in dns read

- [CVE-2020-13601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13601)
- [Zephyr project bug tracker ZEPSEC-92](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-92)
- [PR27774 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/27774)
- [PR30503 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/30503)

### CVE-2020-13602

Remote Denial of Service in LwM2M do\_write\_op\_tlv

In the Zephyr LwM2M implementation, malformed input can result in an
infinite loop, resulting in a denial of service attack.

- [CVE-2020-13602](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13602)
- [Zephyr project bug tracker ZEPSEC-56](https://zephyrprojectsec.atlasssian.net/browse/ZEPSEC-56)
- [PR26571 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/26571)
- [PR33578 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/33578)

### CVE-2020-13603

Possible overflow in mempool

> - Zephyr offers pre-built ‘malloc’ wrapper function instead.
> - The ‘malloc’ function is wrapper for the ‘sys\_mem\_pool\_alloc’ function
> - sys\_mem\_pool\_alloc allocates ‘size + WB\_UP(sizeof(struct sys\_mem\_pool\_block))’ in an unsafe manner.
> - Asking for very large size values leads to internal integer wrap-around.
> - Integer wrap-around leads to successful allocation of very small memory.
> - For example: calling malloc(0xffffffff) leads to successful allocation of 7 bytes.
> - That leads to heap overflow.

- [CVE-2020-13603](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13603)
- [Zephyr project bug tracker ZEPSEC-111](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-111)
- [PR31796 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/31796)
- [PR32808 fix for v1.4](https://github.com/zephyrproject-rtos/zephyr/pull/26571)

## CVE-2021

### CVE-2021-3319

DOS: Incorrect 802154 Frame Validation for Omitted Source / Dest Addresses

Improper processing of omitted source and destination addresses in
ieee802154 frame validation (ieee802154\_validate\_frame)

This has been fixed in main for v2.5.0

- [CVE-2020-3319](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3319)
- [Zephyr project bug tracker GHSA-94jg-2p6q-5364](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-94jg-2p6q-5364)
- [PR31908 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/31908)

### CVE-2021-3320

Mismatch between validation and handling of 802154 ACK frames, where
ACK frames are considered during validation, but not during actual
processing, leading to a type confusion.

- [CVE-2020-3320](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3320)
- [PR31908 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/31908)

### CVE-2021-3321

Incomplete check of minimum IEEE 802154 fragment size leading to an
integer underflow.

- [CVE-2020-3321](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3321)
- [Zephyr project bug tracker ZEPSEC-114](https://zephyrprojectsec.atlassian.net/browse/ZEPSEC-114)
- [PR33453 fix for v2.4](https://github.com/zephyrproject-rtos/zephyr/pull/33453)

### CVE-2021-3323

Integer Underflow in 6LoWPAN IPHC Header Uncompression

This has been fixed in main for v2.5.0

- [CVE-2020-3323](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3323)
- [Zephyr project bug tracker GHSA-89j6-qpxf-pfpc](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-89j6-qpxf-pfpc)
- [PR 31971 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/31971)

### CVE-2021-3430

Assertion reachable with repeated LL\_CONNECTION\_PARAM\_REQ.

This has been fixed in main for v2.6.0

- [CVE-2021-3430](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3430)
- [Zephyr project bug tracker GHSA-46h3-hjcq-2jjr](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-46h3-hjcq-2jjr)
- [PR 33272 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33272)
- [PR 33369 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33369)
- [PR 33759 fix for 1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/33759)

### CVE-2021-3431

BT: Assertion failure on repeated LL\_FEATURE\_REQ

This has been fixed in main for v2.6.0

- [CVE-2021-3431](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3431)
- [Zephyr project bug tracker GHSA-7548-5m6f-mqv9](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-7548-5m6f-mqv9)
- [PR 33340 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33340)
- [PR 33369 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33369)

### CVE-2021-3432

Invalid interval in CONNECT\_IND leads to Division by Zero

This has been fixed in main for v2.6.0

- [CVE-2021-3432](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3432)
- [Zephyr project bug tracker GHSA-7364-p4wc-8mj4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-7364-p4wc-8mj4)
- [PR 33278 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33278)
- [PR 33369 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33369)

### CVE-2021-3433

BT: Invalid channel map in CONNECT\_IND results to Deadlock

This has been fixed in main for v2.6.0

- [CVE-2021-3433](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3433)
- [Zephyr project bug tracker GHSA-3c2f-w4v6-qxrp](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-3c2f-w4v6-qxrp)
- [PR 33278 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33278)
- [PR 33369 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33369)

### CVE-2021-3434

L2CAP: Stack based buffer overflow in le\_ecred\_conn\_req()

This has been fixed in main for v2.6.0

- [CVE-2021-3434](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3434)
- [Zephyr project bug tracker GHSA-8w87-6rfp-cfrm](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-8w87-6rfp-cfrm)
- [PR 33305 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33305)
- [PR 33419 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33419)
- [PR 33418 fix for 1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/33418)

### CVE-2021-3435

L2CAP: Information leakage in le\_ecred\_conn\_req()

This has been fixed in main for v2.6.0

- [CVE-2021-3435](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3435)
- [Zephyr project bug tracker GHSA-xhg3-gvj6-4rqh](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-xhg3-gvj6-4rqh)
- [PR 33305 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33305)
- [PR 33419 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33419)
- [PR 33418 fix for 1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/33418)

### CVE-2021-3436

Bluetooth: Possible to overwrite an existing bond during keys
distribution phase when the identity address of the bond is known

During the distribution of the identity address information we don’t
check for an existing bond with the same identity address.This means
that a duplicate entry will be created in RAM while the newest entry
will overwrite the existing one in persistent storage.

This has been fixed in main for v2.6.0

- [CVE-2021-3436](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3436)
- [Zephyr project bug tracker GHSA-j76f-35mc-4h63](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-j76f-35mc-4h63)
- [PR 33266 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/33266)
- [PR 33432 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33432)
- [PR 33433 fix for 2.4](https://github.com/zephyrproject-rtos/zephyr/pull/33433)
- [PR 33718 fix for 1.14.2](https://github.com/zephyrproject-rtos/zephyr/pull/33718)

### CVE-2021-3454

Truncated L2CAP K-frame causes assertion failure

For example, sending L2CAP K-frame where SDU length field is truncated
to only one byte, causes assertion failure in previous releases of
Zephyr. This has been fixed in master by commit 0ba9437 but has not
yet been backported to older release branches.

This has been fixed in main for v2.6.0

- [CVE-2021-3454](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3454)
- [Zephyr project bug tracker GHSA-fx88-6c29-vrp3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fx88-6c29-vrp3)
- [PR 32588 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/32588)
- [PR 33513 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/33513)
- [PR 33514 fix for 2.4](https://github.com/zephyrproject-rtos/zephyr/pull/33514)

### CVE-2021-3455

Disconnecting L2CAP channel right after invalid ATT request leads freeze

When Central device connects to peripheral and creates L2CAP
connection for Enhanced ATT, sending some invalid ATT request and
disconnecting immediately causes freeze.

This has been fixed in main for v2.6.0

- [CVE-2021-3455](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3455)
- [Zephyr project bug tracker GHSA-7g38-3x9v-v7vp](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-7g38-3x9v-v7vp)
- [PR 35597 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/35597)
- [PR 36104 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/36104)
- [PR 36105 fix for 2.4](https://github.com/zephyrproject-rtos/zephyr/pull/36105)

### CVE-2021-3510

Zephyr JSON decoder incorrectly decodes array of array

When using JSON\_OBJ\_DESCR\_ARRAY\_ARRAY, the subarray is has the token
type JSON\_TOK\_LIST\_START, but then assigns to the object part of the
union. arr\_parse then takes the offset of the array-object (which has
nothing todo with the list) treats it as relative to the parent
object, and stores the length of the subarray in there.

This has been fixed in main for v2.7.0

- [CVE-2021-3510](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3510)
- [Zephyr project bug tracker GHSA-289f-7mw3-2qf4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-289f-7mw3-2qf4)
- [PR 36340 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/36340)
- [PR 37816 fix for 2.6](https://github.com/zephyrproject-rtos/zephyr/pull/37816)

### CVE-2021-3581

HCI data not properly checked leads to memory overflow in the Bluetooth stack

In the process of setting SCAN\_RSP through the HCI command, the Zephyr
Bluetooth protocol stack did not effectively check the length of the
incoming HCI data. Causes memory overflow, and then the data in the
memory is overwritten, and may even cause arbitrary code execution.

This has been fixed in main for v2.6.0

- [CVE-2021-3581](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3581)
- [Zephyr project bug tracker GHSA-8q65-5gqf-fmw5](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-8q65-5gqf-fmw5)
- [PR 35935 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/35935)
- [PR 35984 fix for 2.5](https://github.com/zephyrproject-rtos/zephyr/pull/35984)
- [PR 35985 fix for 2.4](https://github.com/zephyrproject-rtos/zephyr/pull/35985)
- [PR 35985 fix for 1.14](https://github.com/zephyrproject-rtos/zephyr/pull/35985)

### CVE-2021-3625

Buffer overflow in Zephyr USB DFU DNLOAD

This has been fixed in main for v2.6.0

- [CVE-2021-3625](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3625)
- [Zephyr project bug tracker GHSA-c3gr-hgvr-f363](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-c3gr-hgvr-f363)
- [PR 36694 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/36694)

### CVE-2021-3835

Buffer overflow in Zephyr USB device class

This has been fixed in main for v3.0.0

- [CVE-2021-3835](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3835)
- [Zephyr project bug tracker GHSA-fm6v-8625-99jf](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fm6v-8625-99jf)
- [PR 42093 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/42093)
- [PR 42167 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/42167)

### CVE-2021-3861

Buffer overflow in the RNDIS USB device class

This has been fixed in main for v3.0.0

- [CVE-2021-3861](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3861)
- [Zephyr project bug tracker GHSA-hvfp-w4h8-gxvj](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hvfp-w4h8-gxvj)
- [PR 39725 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/39725)

### CVE-2021-3966

Usb bluetooth device ACL read cb buffer overflow

This has been fixed in main for v3.0.0

- [Zephyr project bug tracker GHSA-hfxq-3w6x-fv2m](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hfxq-3w6x-fv2m)
- [PR 42093 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/42093)
- [PR 42167 fix for v2.7.0](https://github.com/zephyrproject-rtos/zephyr/pull/42167)

## CVE-2022

### CVE-2022-0553

Possible to retrieve unencrypted firmware image

This has been fixed in main for v3.0.0

- [Zephyr project bug tracker GHSA-wrj2-9vj9-rrcp](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-wrj2-9vj9-rrcp)
- [PR 42424 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/42424)

### CVE-2022-1041

Out-of-bound write vulnerability in the Bluetooth Mesh core stack can be triggered during provisioning

This has been fixed in main for v3.1.0

- [Zephyr project bug tracker GHSA-p449-9hv9-pj38](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-p449-9hv9-pj38)
- [PR 45136 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/45136)
- [PR 45188 fix for v3.0.0](https://github.com/zephyrproject-rtos/zephyr/pull/45188)
- [PR 45187 fix for v2.7.0](https://github.com/zephyrproject-rtos/zephyr/pull/45187)

### CVE-2022-1042

Out-of-bound write vulnerability in the Bluetooth Mesh core stack can be triggered during provisioning

This has been fixed in main for v3.1.0

- [Zephyr project bug tracker GHSA-j7v7-w73r-mm5x](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-j7v7-w73r-mm5x)
- [PR 45066 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/45066)
- [PR 45135 fix for v3.0.0](https://github.com/zephyrproject-rtos/zephyr/pull/45135)
- [PR 45134 fix for v2.7.0](https://github.com/zephyrproject-rtos/zephyr/pull/45134)

### CVE-2022-1841

Out-of-Bound Write in tcp\_flags

This has been fixed in main for v3.1.0

- [Zephyr project bug tracker GHSA-5c3j-p8cr-2pgh](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-5c3j-p8cr-2pgh)
- [PR 45796 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/45796)

### CVE-2022-2741

can: denial-of-service can be triggered by a crafted CAN frame

This has been fixed in main for v3.2.0

- [Zephyr project bug tracker GHSA-hx5v-j59q-c3j8](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hx5v-j59q-c3j8)
- [PR 47903 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/47903)
- [PR 47957 fix for v3.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/47957)
- [PR 47958 fix for v3.0.0](https://github.com/zephyrproject-rtos/zephyr/pull/47958)
- [PR 47959 fix for v2.7.0](https://github.com/zephyrproject-rtos/zephyr/pull/47959)

### CVE-2022-2993

bt: host: Wrong key validation check

This has been fixed in main for v3.2.0

- [Zephyr project bug tracker GHSA-3286-jgjx-8cvr](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-3286-jgjx-8cvr)
- [PR 48733 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/48733)

### CVE-2022-3806

DoS: Invalid Initialization in le\_read\_buffer\_size\_complete()

- [Zephyr project bug tracker GHSA-w525-fm68-ppq3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-w525-fm68-ppq3)

## CVE-2023

### CVE-2023-0396

Buffer Overreads in Bluetooth HCI

- [Zephyr project bug tracker GHSA-8rpp-6vxq-pqg3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-8rpp-6vxq-pqg3)

### CVE-2023-0397

DoS: Invalid Initialization in le\_read\_buffer\_size\_complete()

- [Zephyr project bug tracker GHSA-wc2h-h868-q7hj](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-wc2h-h868-q7hj)

This has been fixed in main for v3.3.0

- [PR 54905 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/54905)
- [PR 47957 fix for v3.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/55024)
- [PR 47958 fix for v3.1.0](https://github.com/zephyrproject-rtos/zephyr/pull/55023)
- [PR 47959 fix for v2.7.4](https://github.com/zephyrproject-rtos/zephyr/pull/55022)

### CVE-2023-0779

net: shell: Improper input validation

- [Zephyr project bug tracker GHSA-9xj8-6989-r549](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-9xj8-6989-r549)

This has been fixed in main for v3.3.0

- [PR 54371 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/54371)
- [PR 54380 fix for v3.2.0](https://github.com/zephyrproject-rtos/zephyr/pull/54380)
- [PR 54381 fix for v2.7.4](https://github.com/zephyrproject-rtos/zephyr/pull/54381)

### CVE-2023-1901

HCI send\_sync Dangling Semaphore Reference Re-use

- [Zephyr project bug tracker GHSA-xvvm-8mcm-9cq3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-xvvm-8mcm-9cq3)

This has been fixed in main for v3.4.0

- [PR 56709 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/56709)

### CVE-2023-1902

HCI Connection Creation Dangling State Reference Re-use

- [Zephyr project bug tracker GHSA-fx9g-8fr2-q899](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fx9g-8fr2-q899)

This has been fixed in main for v3.4.0

- [PR 56709 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/56709)

### CVE-2023-3725

Potential buffer overflow vulnerability in the Zephyr CANbus subsystem.

- [Zephyr project bug tracker GHSA-2g3m-p6c7-8rr3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-2g3m-p6c7-8rr3)

This has been fixed in main for v3.5.0

- [PR 61502 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/61502)
- [PR 61518 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/61518)
- [PR 61517 fix for 3.3](https://github.com/zephyrproject-rtos/zephyr/pull/61517)
- [PR 61516 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/61516)

### CVE-2023-4257

Unchecked user input length in the Zephyr WiFi shell module can cause
buffer overflows.

- [Zephyr project bug tracker GHSA-853q-q69w-gf5j](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-853q-q69w-gf5j)

This has been fixed in main for v3.5.0

- [PR 605377 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/605377)
- [PR 61383 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/61383)

### CVE-2023-4258

bt: mesh: vulnerability in provisioning protocol implementation on provisionee side

- [Zephyr project bug tracker GHSA-m34c-cp63-rwh7](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-m34c-cp63-rwh7)

This has been fixed in main for v3.5.0

- [PR 59467 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/59467)
- [PR 60078 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/60078)
- [PR 60079 fix for 3.3](https://github.com/zephyrproject-rtos/zephyr/pull/60079)

### CVE-2023-4259

Buffer overflow vulnerabilities in the Zephyr eS-WiFi driver

- [Zephyr project bug tracker GHSA-gghm-c696-f4j4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-gghm-c696-f4j4)

This has been fixed in main for v3.5.0

- [PR 63074 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63074)
- [PR 63750 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63750)

### CVE-2023-4260

Off-by-one buffer overflow vulnerability in the Zephyr FS subsystem

- [Zephyr project bug tracker GHSA-gj27-862r-55wh](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-gj27-862r-55wh)

This has been fixed in main for v3.5.0

- [PR 63079 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63079)

### CVE-2023-4262

Potential buffer overflow vulnerabilities in the Zephyr Mgmt subsystem

- [Zephyr project bug tracker GHSA-56p9-5p3v-hhrc](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-56p9-5p3v-hhrc)
- This issue has not been fixed.

### CVE-2023-4263

Potential buffer overflow vulnerability in the Zephyr IEEE 802.15.4 nRF 15.4 driver.

- [Zephyr project bug tracker GHSA-rf6q-rhhp-pqhf](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-rf6q-rhhp-pqhf)

This has been fixed in main for v3.5.0

- [PR 60528 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/60528)
- [PR 61384 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/61384)
- [PR 61216 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/61216)

### CVE-2023-4264

Potential buffer overflow vulnerabilities in the Zephyr Bluetooth subsystem

- [Zephyr project bug tracker GHSA-rgx6-3w4j-gf5j](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-rgx6-3w4j-gf5j)

This has been fixed in main for v3.5.0

- [PR 58834 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/58834)
- [PR 60465 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/60465)
- [PR 61845 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/61845)
- [PR 61385 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/61385)

### CVE-2023-4265

Two potential buffer overflow vulnerabilities in Zephyr USB code

- [Zephyr project bug tracker GHSA-4vgv-5r6q-r6xh](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-4vgv-5r6q-r6xh)

This has been fixed in main for v3.4.0

- [PR 59157 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/59157)
- [PR 59018 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/59018)

### CVE-2023-4424

bt: hci: DoS and possible RCE

- [Zephyr project bug tracker GHSA-j4qm-xgpf-qjw3](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-j4qm-xgpf-qjw3)

This has been fixed in main for v3.5.0

- [PR 61651 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/61651)
- [PR 61696 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/61696)
- [PR 61695 fix for 3.3](https://github.com/zephyrproject-rtos/zephyr/pull/61695)
- [PR 61694 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/61694)

### CVE-2023-5055

L2CAP: Possible Stack based buffer overflow in le\_ecred\_reconf\_req()

- [Zephyr project bug tracker GHSA-wr8r-7f8x-24jj](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-wr8r-7f8x-24jj)

This has been fixed in main for v3.5.0

- [PR 62381 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/62381)

### CVE-2023-5139

Potential buffer overflow vulnerability in the Zephyr STM32 Crypto driver.

- [Zephyr project bug tracker GHSA-rhrc-pcxp-4453](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-rhrc-pcxp-4453)

This has been fixed in main for v3.5.0

- [PR 61839 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/61839)

### CVE-2023-5184

Potential signed to unsigned conversion errors and buffer overflow
vulnerabilities in the Zephyr IPM driver

- [Zephyr project bug tracker GHSA-8x3p-q3r5-xh9g](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-8x3p-q3r5-xh9g)

This has been fixed in main for v3.5.0

- [PR 63069 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63069)

### CVE-2023-5563

The SJA1000 CAN controller driver backend automatically attempts to recover
from a bus-off event when built with CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY=y. This
results in calling k\_sleep() in IRQ context, causing a fatal exception.

- [Zephyr project bug tracker GHSA-98mc-rj7w-7rpv](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-98mc-rj7w-7rpv)

This has been fixed in main for v3.5.0

- [PR 63713 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63713)
- [PR 63718 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/63718)
- [PR 63717 fix for 3.3](https://github.com/zephyrproject-rtos/zephyr/pull/63717)

### CVE-2023-5753

Potential buffer overflow vulnerabilities in the Zephyr Bluetooth
subsystem source code when asserts are disabled.

- [Zephyr project bug tracker GHSA-hmpr-px56-rvww](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-hmpr-px56-rvww)

This has been fixed in main for v3.5.0

- [PR 63605 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/63605)

### CVE-2023-5779

Out of bounds issue in remove\_rx\_filter in multiple can drivers.

- [Zephyr project bug tracker GHSA-7cmj-963q-jj47](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-7cmj-963q-jj47)

This has been fixed in main for v3.6.0

- [PR 64399 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/64399)
- [PR 64416 fix for 3.5](https://github.com/zephyrproject-rtos/zephyr/pull/64416)
- [PR 64415 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/64415)
- [PR 64427 fix for 3.3](https://github.com/zephyrproject-rtos/zephyr/pull/64427)
- [PR 64431 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/64431)

### CVE-2023-6249

Signed to unsigned conversion problem in esp32\_ipm\_send may lead to buffer overflow

- [Zephyr project bug tracker GHSA-32f5-3p9h-2rqc](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-32f5-3p9h-2rqc)

This has been fixed in main for v3.6.0

- [PR 65546 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/65546)

### CVE-2023-6749

Potential buffer overflow due unchecked data coming from user input in settings shell.

- [Zephyr project bug tracker GHSA-757h-rw37-66hw](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-757h-rw37-66hw)

This has been fixed in main for v3.6.0

- [PR 66451 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/66451)
- [PR 66584 fix for 3.5](https://github.com/zephyrproject-rtos/zephyr/pull/66584)

### CVE-2023-6881

Potential buffer overflow vulnerability in Zephyr fuse file system.

- [Zephyr project bug tracker GHSA-mh67-4h3q-p437](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-mh67-4h3q-p437)

This has been fixed in main for v3.6.0

- [PR 66592 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/66592)

### CVE-2023-7060

Missing Security Control in Zephyr OS IP Packet Handling

- [Zephyr project bug tracker GHSA-fjc8-223c-qgqr](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fjc8-223c-qgqr)

This has been fixed in main for v3.6.0

- [PR 66645 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/66645)
- [PR 66739 fix for 3.5](https://github.com/zephyrproject-rtos/zephyr/pull/66739)
- [PR 66738 fix for 3.4](https://github.com/zephyrproject-rtos/zephyr/pull/66738)
- [PR 66887 fix for 2.7](https://github.com/zephyrproject-rtos/zephyr/pull/66887)

## CVE-2024

### CVE-2024-1638

Bluetooth characteristic LESC security requirement not enforced without additional flags

- [Zephyr project bug tracker GHSA-p6f3-f63q-5mc2](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-p6f3-f63q-5mc2)

This has been fixed in main for v3.6.0

- [PR 69170 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/69170)

### CVE-2024-3077

Bluetooth: Integer underflow in gatt\_find\_info\_rsp. A malicious BLE
device can crash BLE victim device by sending malformed gatt packet.

- [Zephyr project bug tracker GHSA-gmfv-4vfh-2mh8](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-gmfv-4vfh-2mh8)

This has been fixed in main for v3.7.0

- [PR 69396 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/69396)

### CVE-2024-3332

Bluetooth: DoS caused by null pointer dereference.

A malicious BLE device can send a specific order of packet
sequence to cause a DoS attack on the victim BLE device.

- [Zephyr project bug tracker GHSA-jmr9-xw2v-5vf4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-jmr9-xw2v-5vf4)

This has been fixed in main for v3.7.0

- [PR 71030 fix for main](https://github.com/zephyrproject-rtos/zephyr/pull/71030)

### CVE-2024-4785

Under embargo until 2024-08-07

### CVE-2024-5754

Under embargo until 2024-09-04

### CVE-2024-5931

Under embargo until 2024-09-10

### CVE-2024-6135

Under embargo until 2024-09-11

### CVE-2024-6137

Under embargo until 2024-09-11

### CVE-2024-6258

Under embargo until 2024-09-05

### CVE-2024-6259

Under embargo until 2024-09-12

### CVE-2024-6442

Under embargo until 2024-09-22

### CVE-2024-6443

Under embargo until 2024-09-22

### CVE-2024-6444

Under embargo until 2024-09-22
