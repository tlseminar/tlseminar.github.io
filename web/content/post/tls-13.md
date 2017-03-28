+++
date = "24 Mar 2017"
author = "Team Mango"
draft = true
title = "TLS 1.3"
slug = "tls-13"
+++

## TLS Evolves: Version 1.3

TLS v1.3 is a solid improvement. In order to get a good understanding of TLS v1.3 and where it is heading in the future, we will first look at where TLS has been:

### Looking Backward: Retro TLS

SSL/TLS has a storied past; SSL v1.0 was never released. Netscape, the company that originally developed SSL, circulated it internally but decided not to release it to the public because it had several flaws including a lack of data integrity protection.

After that non-starter, the timeline looks like this:
- 1994: Netscape develops SSL v2.0 which is shipped with the Netscape Navigator 1.1
- 1995: SSL v2.0 has serious security issues; Netscape releases SSL v3.
- 1999: TLS v1.0 released; standardizing and upgrading SSL v3.0 
- 2006: TLS v1.1 released; address the BEAST attack, which will come in 5 years
- 2008: TLS v1.2 released with Authenticated Encryption
- 2011: Google deploys public key pinning and forward secrecy
- 2013: Work on TLS v1.3 begins

A more thorough timeline can be found [here](https://www.feistyduck.com/ssl-tls-and-pki-history/).

So what does TLS v1.3 bring to the table? Let's take a look...

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

## 0-RTT Resumption

A major new feature in the TLS 1.3 draft is support for 0-RTT session resumption. In TLS 1.2, establishing a connection to a new server required at least 4 trips between the server and client to make an HTTP request and receive a response. With a session-ID or session ticket, that could be reduced to 3 trips per connection. TLS 1.3 by default reduces the number for new connections to only 3 trips per connection, but also adds support for a new mode termed *0-RTT*. In this mode, resumed HTTPS connections require only 2 trips, which is the bare minimum required for a full HTTP query and response. In this mode, TLS 1.3 adds no additional latency cost to the regular HTTP request!

![TLS 1.3 0-RTT](/images/tls-13/tls1_3_0rtt.png)
###### TLS 1.3 0-RTT (Source: https://blog.cloudflare.com/tls-1-3-overview-and-q-and-a/)

However, the addition of 0-RTT resumption to the protocol has an important implication for the security features provided by the protocol. Because TLS 1.3 session tickets, which enable 0-RTT resumption, are stateless on the server, such requests from the client are trivially vulnerable to **replay attacks**, which enable an attacker who can intercept an encrypted client message and re-send it to the server, without the server being able to differentiate the replayed blob.

To remedy this, the protocol authors recommend that initial requests from the client be *idempotent*, or non-state-changing. Servers should not allow the first request to be idempotent in 0-RTT mode. This has been arguably the most controversial part of the new standard, as it puts the onus on some higher level protocol to solve a problem that TLS has historically been responsible for. Even worse, it is not solved directly by HTTP but rather must be specifically kept in mind by web developers.

## Anti-Downgrade Prevention and Detection

[Downgrade resilience in key-exchange protocols](https://eprint.iacr.org/2016/072.pdf) by Karthikeyan Bhargavan et al. in IEEE Symposium on Security and Privacy (SP), 2016.

TLS 1.2 suffers from various downgrade and man-in-the-middle attacks like Logjam, FREAK and POODLE.
Logjam exploits the option of using legacy "export-grade" 512-bit Diffie–Hellman groups in TLS 1.2. It forces susceptible servers to downgrade to cryptographically weak 512 bit Diffie-Hellman groups, which could then be compromised.
FREAK is a man-in-the-middle attack that affects the OpenSSL stack, the default Android web browser, and some Safari browsers. It tricks servers into negotiating a TLS connection using cryptographically weak 512 bit encryption keys.
POODLE exploits vulnerability in SSL 3.0 but is applicable to TLS 1.2 once the attacker performs version rollback to SSL 3.0 through a man-in-the-middle attack.

The above problems can be countered using correct downgrade protection. While TLS 1.2 does implement downgrade protection, it fails to do so correctly.

### Downgrade Resilience in Key-Exchange Protocols

Downgrade protection primarily relies on the MACs in the finished messages, which in turn rely on the strength of the group and the negotiated algorithms and hash.
If a client and server support a weak group, then an attacker can downgrade the group and break the master secret to forget the MACs, as in Logjam.

<center><img src="/images/tls-13/tls1_2.png" alt="Downgrade Protection in TLS 1.2" style="width:800px;"/><br>
<sup>TLS 1.0 - 1.2 with (EC)DHE key exchange (a), where messages labeled with * occur only when client authentication is enabled, and (b) its downgrade protection sub-protocol</sup><br><sup>Source: https://eprint.iacr.org/2016/072.pdf</sup></center>

Draft 10 of TLS 1.3 implements the following downgrade protection mechanism.
<center><img src="/images/tls-13/tls1_3_draft10.png" alt="Downgrade Protection in TLS 1.3 Draft 10" style="width:800px;"/><br>
<sup>TLS 1.3 1-RTT mode with server-only authentication (a) and its downgrade protection sub-protocol (b) </sup><br><sup>Source: https://eprint.iacr.org/2016/072.pdf</sup></center>

There are three downgrade attacks possible on TLS 1.3 as described in Draft 10.
One, an attacker downgrades the connection to TLS 1.2 or lower and mounts any of the downgrade attacks mentioned before. This will succeed as long as the attacker can forge the finished MACs.
Second, an attacker uses the TLS fallback mechanism to stop TLS 1.3 connections and allows only TLS 1.2 connections to go through. Even if the end points implement the fallback protection mechanism, the attacker can use one of the downgrade attacks in TLS1.2 to break the connection.
Third, in Draft 10 of the TLS1.3 protocol, the handshake hashes restart upon receiving a Retry message and hence, the attacker can downgrade the Diffie-Hellman group for some classes of negotiation functions.

Recently, draft 11 of TLS 1.3 has [fixed](https://github.com/tlswg/tls13-spec/pull/284) the issue by requiring TLS 1.3 server to set top N bits of the ServerRandom to be a specific fixed value on receiving ClientHello message from a TLS 1.2 or below client. TLS 1.3 clients which receive a TLS 1.2 or below ServerHello check for this value and abort if they receive it.
This allows for detection of downgrade attacks over and above the Finished handshake as long as ephemeral cipher suites are used. This prevents attacks targeted at (EC)DHE.

Draft 11 of TLS 1.3 implements the following downgrade protection mechanism.
<center><img src="/images/tls-13/tls1_3_draft11.png" alt="Downgrade Protection in TLS 1.3 Draft 11" style="width:800px;"/><br>
<sup>TLS 1.3 Draft 11 Update on Downgrade Resilience in Key-Exchange Protocols</sup><br><sup>Source: https://eprint.iacr.org/2016/072.pdf</sup></center>

TLS 1.3 draft 11 counters all the attacks discussed by [Karthikeyan et al.](https://eprint.iacr.org/2016/072.pdf) by incorporating two countermeasures.
First, TLS 1.3 protocol continues the handshake hashes over retries.
Second, TLS 1.3 servers always include their highest supported version number in the server nonce, even when they choose a lower version such as TLS 1.0.
The TLS 1.3 server will send [ServerHello](https://tools.ietf.org/html/draft-ietf-tls-tls13-18#section-4.1.3) message in response to a ClientHello message when it is able to find an acceptable set of algorithms and the client's "key_share" extension is acceptable.  If it is not able to find an acceptable set of parameters, the server will respond with a "handshake_failure" fatal alert. The ServerHello message contains server's random value which incorporates downgrade protection mechanism. If a ClientHello indicates only support for TLS 1.2 or below, then the last eight bytes of server's random value MUST be set to: `44 4F 57 4E 47 52 44 01`.
If a ClientHello indicates only support for TLS 1.1 or below, then the last eight bytes of server's random value SHOULD be set to: `44 4F 57 4E 47 52 44 00`.
Likewise, the TLS 1.3 clients are required to check the above values in the server random.




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
