+++
date = "24 Mar 2017"
author = "Team Mango"
draft = true
title = "TLS 1.3"
slug = "tls-13"
+++

## Faster Handshake

TLS 1.3 introduces a significantly slimmer Handshake Protocol than previous versions. In order to understand the implications of these changes, we first review the Handshake Protocol used in TLS 1.2. 
In TLS 1.2, the client begins the handshake with a Client Hello, followed by a Server Hello response from the server. The Client then proceeds with a Client Key Exchange and Client Finished; the server responds with its own versions. 
In contrast, TLS 1.3 incorporates the key share messages with the Client/Server Hello, meaning that each side of the connection has to send one less message (and only send one message total to initiate the connection).

<center><img src="/images/tls-13/handshake1.2.png" alt="TLS 1.2 Handshake" style="width:300px;"/><br>
<sup>TLS 1.2 Handshake</sup></center>

<center><img src="/images/tls-13/handshake1.3.png" alt="TLS 1.3 Handshake" style="width:300px;"/><br>
<sup>TLS 1.3 Handshake</sup></center>

###AuthLoop

AuthLoop is a TLS-style authentication protocol specifically designed to telephony networks. In this domain, the system must connect three different types of telephony networks: cellular, VoIP, and PSTN. However, the TLS Handshake transmission speeds for such a system were extremely slow - averaging 98 seconds per handshake - which is completely infeasible for most phone calls. AuthLoop keeps the authentication and shared secret elements of TLS and a freshness/liveness component analogous to the Heartbeat Protocol. On the other hand, AuthLoop removes RSA and the cipher agreement messages. Furthermore, AuthLoop does not encrypt messages and therefore has no Record Protocol. After slimming down, the average transmission time reduced drastically to 4.8 seconds.


## Anti-Downgrade Prevention and Detection

TLS 1.2 suffers from various downgrade and man-in-the-middle attacks like Logjam, FREAK and POODLE.
Logjam exploits the option of using legacy "export-grade" 512-bit Diffie–Hellman groups in TLS 1.2. It forces susceptible servers to downgrade to cryptographically weak 512 bit Diffie-Hellman groups, which could then be compromised.
FREAK is a man-in-the-middle attack that affects the OpenSSL stack, the default Android web browser, and some Safari browsers. It tricks servers into negotiating a TLS connection using cryptographically weak 512 bit encryption keys.
POODLE exploits vulnerability in SSL 3.0 but is applicable to TLS 1.2 after the attacker performs version rollback to SSL 3.0 through a man-in-the-middle attack.

### Downgrade Resilience in Key-Exchange Protocols

<center><img src="/images/timing-attacks/montgomery.png" alt="Montgomery ladder" style="width:300px;"/><br>
<sup>Montgomery's Ladder</sup><br><sup>Source: https://cr.yp.to/bib/2003/joye-ladder.pdf</sup></center>

## Removed
[An overview of TLS 1.3 and Q&A](https://blog.cloudflare.com/tls-1-3-overview-and-q-and-a/)  
In 1.3, everything was scrutinized for being really necessary and secure, and scrapped otherwise. The following things are removed:

* [static RSA handshake](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/)  
* the [CBC MAC-then-Encrypt](https://blog.cloudflare.com/padding-oracles-and-the-decline-of-cbc-mode-ciphersuites/) modes, which were responsible for Vaudenay, Lucky13, POODLE, LuckyMinus20  
* weak primitives like RC4, SHA1, MD5  
* compression  
* renegotiation  
* custom FFDHE groups  
* RSA PKCS#1v1.5  
* explicit nonces  
