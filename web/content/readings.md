# Readings

## Background

Wikipedia's [_Transport Layer
Security_](https://en.wikipedia.org/wiki/Transport_Layer_Security)
page includes a quite extensive summary of TLS vulnerabilities.

[_The First Few Milliseconds of an HTTPS Connection_](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html), Jeff Moser, 2009.

Jeremy Clark and Paul C. van Oorschot. _SoK: SSL and HTTPS: Revisiting
past challenges and evaluating certificate trust model
enhancements_. IEEE Symposium on Security and Privacy (Oakland) 2013.
[[PDF](/docs/soktls.pdf)]

## Protocol Specification

[The Transport Layer Security (TLS) Protocol Version
1.3](https://tlswg.github.io/tls13-spec/) (Internet Draft, 22 December
2016 is latest version as of today, 29 December 2016.)

Earlier versions:

- [The Transport Layer Security (TLS) Protocol Version 1.2](https://tools.ietf.org/html/rfc5246) [[PDF](https://tools.ietf.org/pdf/rfc5246.pdf)], August 2008.
- [Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc3268) [[PDF](https://tools.ietf.org/pdf/rfc3268.pdf)], June 2002.
- [The Secure Sockets Layer (SSL) Protocol Version 3.0](https://tools.ietf.org/html/rfc6101) [[PDF](https://tools.ietf.org/pdf/rfc6101.pdf)], August 2011.
- [The TLS Protocol Version 1.0](https://datatracker.ietf.org/doc/rfc2246/), January 1999.


## Protocol Analysis

David Wagner, Bruce Schneier. _Analysis of the SSL 3.0 Protocol_.  In
_Second USENIX Workshop on Electronic Commerce Proceedings_,
1996. [[PDF](/docs/analysisssl3.pdf)]

## Formal Methods

John C. Mitchell, Vitaly Shmatikov, and Ulrich Stern. _Finite-State Analysis of SSL 3.0_. USENIX Security Symposium, January 1998. [[PDF](/docs/finitestate.pdf)]

Lawrence C. Paulson. _Inductive Analysis of the Internet Protocol TLS_. ACM Transactions of Information and System Security, August 1999. [[PDF](/docs/inductiveanalysis.pdf)]

Karthikeyan Bhargavan, Ricardo Corin, Cédric Fournet, Eugen Zalinescu.
_Cryptographically Verified Implementations for TLS_. ACM CCS
2008. [[PDF](/docs/verifiedtls.pdf)]

Tibor Jager, Florian Kohlar, Sven Schäge, and Jörg Schwenk. _On the Security of TLS-DHE in the Standard Model_. May 2011. [[eprint](https://eprint.iacr.org/2011/219)] [[PDF](https://eprint.iacr.org/2011/219.pdf)]

Krawczyk, Hugo, Kenneth G. Paterson, and Hoeteck Wee. _On the Security of the TLS Protocol: A Systematic Analysis_. CRYPTO 2013. 
[[eprint](http://eprint.iacr.org/2013/339)]
[[PDF](http://eprint.iacr.org/2013/339.pdf)]

## Implementation Issues

Martin Georgiev, Subodh Iyengar, Suman Jana, Rishita Anubhai, Dan
Boneh, Vitaly Shmatikov. _The Most Dangerous Code in the World:
Validating SSL Certificates in Non-Browser Software_.  ACM CCS 2012.
[[PDF](/docs/mostdangerouscode.pdf)]

David Kaloper-Mersinjak, Hannes Mehnert, Anil Madhavapeddy and Peter Sewell. _Not-quite-so-broken TLS: lessons in re-engineering a security protocol
specification and implementation_. USENIX Security 2015. [[PDF](/docs/nqsbtls.pdf)]

Suman Jana, Yuan Kang, Samuel Roth, and [Baishakhi Ray](http://rayb.info/). _Automatically Detecting Error Handling Bugs using Error Specifications_. USENIX Security 2016. [[PDF](/docs/epex.pdf)]

## Testing

Chad Brubaker, Suman Jana, [Baishakhi Ray](http://rayb.info/), Sarfraz Khurshid, Vitaly Shmatikov.
_Using Frankencerts for Automated Adversarial Testing of Certificate Validation in SSL/TLS Implementations_. IEEE Symposium on Security and Privacy (Oakland) 2014. [[PDF](/docs/frankencerts.pdf)]. 

## Performance and Cost

Cristian Coarfa, Peter Druschel, and Dan S. Wallach. _Performance Analysis of TLS Web Servers_.  ACM Transactions on Computer Systems (earlier version in NDSS 2002), February 2006. [[PDF](/docs/performance.pdf)]

## Certificates


