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

## Attacks

RFC on known attacks: _Summarizing Known Attacks on Transport Layer Security (TLS) and Datagram TLS (DTLS)_. Y. Sheffer, et al. RFC 7457. February 2015. [[HTML](https://tools.ietf.org/html/rfc7457)] [[PDF](https://tools.ietf.org/pdf/rfc7457.pdf)]

Daniel Bleichenbacher. _Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS \#1_. CRYPTO 1998. [[PDF](http://archiv.infsec.ethz.ch/education/fs08/secsem/Bleichenbacher98.pdf)]

Serge Vaudenay. _Security Flaws Induced by CBC Padding Applications to
SSL, IPSEC, WTLS..._. EuroCRYPT
2002. [[PDF](http://www.iacr.org/cryptodb/archive/2002/EUROCRYPT/2850/2850.pdf)]

David Brumley and Daniel Boneh. _Remote Timing Attacks are Practical_.  USENIX Security Symposium 2003, and Computer Networks, August 2005. [[PDF](/docs/remotetiming.pdf)]  (Followed by: Billy Bob Brumley and Nicola Tuveri. _Remote Timing Attacks are Still Practical_. ESORICS 2011 [[PDF](https://eprint.iacr.org/2011/232.pdf)] [[ePrint](https://eprint.iacr.org/2011/232)])
 
Brice Canvel, Alain Hiltgen, Serge Vaudenay, and Martin Vuagnoux. _Password Interception in a SSL/TLS Channel_. CRYPTO 2003. [[PDF](http://www.iacr.org/cryptodb/archive/2003/CRYPTO/1069/1069.pdf)]

Thai Duong and Juliano Rizzo. _Here Come The &oplus; Ninjas_.  2011. [[PDF](/docs/beast.pdf)]

Nadhem AlFardan, Daniel J. Bernstein, Kenneth G. Paterson, Bertram Poettering, and Jacob C.N. Schuldt.
_On the Security of RC4 in TLS_. USENIX Security Symposium 2013. [[PDF](https://www.usenix.org/system/files/conference/usenixsecurity13/sec13-paper_alfardan.pdf)] [[Video](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/alFardan)]

Nadhem J. AlFardan and Kenneth G. Paterson. _Lucky Thirteen: Breaking the TLS and DTLS Record Protocols_. IEEE Symposium on Security and Privacy (Oakland) 2013. [[PDF](http://www.isg.rhul.ac.uk/tls/TLStiming.pdf)] [[Website](http://www.isg.rhul.ac.uk/tls/Lucky13.html)]

Nimrod Aviram, Sebastian Schinzel, Juraj Somorovsky, Nadia Heninger,
Maik Dankel, Jens Steube, Luke Valenta, David Adrian, J. Alex
Halderman, Viktor Dukhovni, Emilia Käsper, Shaanan Cohney, Susanne
Engels, Christof Paar, and Yuval Shavitt. _DROWN: Breaking TLS using
SSLv2_. 25th USENIX Security Symposium, Austin, TX, August 2016. [[PDF](/docs/drown.pdf)]

[[Website](https://drownattack.com/)]


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


Karthikeyan Bhargavan, Cédric Fournet, Markulf Kohlweiss, Alfredo Pironti, Pierre-Yves Strub. _Implementing TLS with Verified Cryptographic Security_
IEEE Symposium on Security and Privacy (Oakland), 2013. [[PDF](/docs/mitls.pdf)] [[Extended Tech Report, PDF](/docs/mitlstr.pdf)]

Karthikeyan Bhargavan1, Cedric Fournet, Markulf Kohlweiss, Alfredo Pironti, Pierre-Yves Strub, and Santiago Zanella-Beguelin. _Proving the TLS Handshake Secure (As It Is)_. CRYPTO 2014. [[PDF](/docs/provinghandshake.pdf)]

## Implementation Bugs

Martin Georgiev, Subodh Iyengar, Suman Jana, Rishita Anubhai, Dan
Boneh, Vitaly Shmatikov. _The Most Dangerous Code in the World:
Validating SSL Certificates in Non-Browser Software_.  ACM CCS 2012.
[[PDF](/docs/mostdangerouscode.pdf)]

David Kaloper-Mersinjak, Hannes Mehnert, Anil Madhavapeddy and Peter Sewell. _Not-quite-so-broken TLS: lessons in re-engineering a security protocol
specification and implementation_. USENIX Security 2015. [[PDF](/docs/nqsbtls.pdf)]

Benjamin Beurdouche, Karthikeyan Bhargavan, Antoine Delignat-Lavaud,
Cedric Fournet, Markulf Kohlweiss, Alfredo Pironti, Pierre-Yves Strub,
Jean Karim Zinzindohoue. _A Messy State of the Union: Taming the
Composite State Machines of TLS_.  IEEE Symposium on Security and
Privacy (Oakland) 2015. [[PDF](/docs/mitlsunion.pdf)] [[Talk Video](https://www.youtube.com/watch?v=rELp9-oFAw0)]

Suman Jana, Yuan Kang, Samuel Roth, and [Baishakhi Ray](http://rayb.info/). _Automatically Detecting Error Handling Bugs using Error Specifications_. USENIX Security 2016. [[PDF](/docs/epex.pdf)]

## Testing

Chad Brubaker, Suman Jana, [Baishakhi Ray](http://rayb.info/), Sarfraz Khurshid, Vitaly Shmatikov.
_Using Frankencerts for Automated Adversarial Testing of Certificate Validation in SSL/TLS Implementations_. IEEE Symposium on Security and Privacy (Oakland) 2014. [[PDF](/docs/frankencerts.pdf)]. 

Benjamin Beurdouche, Antoine Delignat-Lavaud, Nadim Kobeissi, Alfredo Pironti, Karthikeyan Bhargavan. _FLEXTLS: A Tool for Testing TLS Implementations_.
USENIX Workshop on Offensive Technologies, 2015. [[PDF](/docs/flextls.pdf)]

## Performance and Cost

Cristian Coarfa, Peter Druschel, and Dan S. Wallach. _Performance Analysis of TLS Web Servers_.  ACM Transactions on Computer Systems (earlier version in NDSS 2002), February 2006. [[PDF](/docs/performance.pdf)]

## Certificates


[Let's Encrypt](https://letsencrypt.org/)  
[ACMS](https://datatracker.ietf.org/doc/draft-ietf-acme-acme/?include_text=1)

## Post-Quantum

Joppe W. Bos, Craig Costello, Michael Naehrig, and Douglas
Stebila. _Post-quantum key exchange for the TLS protocol from the ring
learning with errors problem_.  IEEE Symposium on Security and Privacy (Oakland) 2016.
[[PDF](http://eprint.iacr.org/2014/599.pdf)] [[Talk Video](https://www.youtube.com/watch?v=BCmSzzQ2ges)]

Erdem Alkim, Léo Ducas, Thomas Pöppelmann, and Peter Schwabe.
_Post-quantum Key Exchange—A New Hope_.  USENIX Security Symposiumn 2016. [[PDF](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_alkim.pdf)] [[Talk Video](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/alkim)]
