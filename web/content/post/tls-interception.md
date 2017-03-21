+++
date = "20 Mar 2017"
author = "Team Poppyseed"
draft = false
title = "TLS Interception and SSL Inspection"
slug = "tls-interception"
+++

> The fact that "SSL inspection" is a phrase that exists, should be a blazing red flag that what you think SSL is doing for you is fundamentally broken. **Compounding the problem are the mistakes that SSL inspection software authors are making**.
> 
> -- *[Will Dormann](https://insights.sei.cmu.edu/cert/2015/03/the-risks-of-ssl-inspection.html "The Risks of SSL Inspection") (2015), Carnegie Melon Software Engineering Institute CERT/CC Blog*

### Recent History

TLS Interception, also referred to as SSL Inspection, is a topic that has been in the news in recent years and months. Back in 2014, researchers from Brigham Young University published a paper titled [TLS Proxies: Friend or Foe?](https://arxiv.org/pdf/1407.7146.pdf "TLS Proxies: Friend or Foe?") where they deployed a Flash application via Google Adwords campaign to identify client-server certificate mismatches across the web. They discovered a wide prevalence of adware, malware and TLS proxy products presenting certificates trusted by the client but not issued by the server -- and in most instances acting in a negligant manner by introducing security vulnerabilities. One parental filter they tested replaced untrusted certificates with trusted ones, bypassing browser warning screens. *This is exactly the type of passive attack HTTPS aims to prevent*. 

Vulnerabilities involving two advertisement injectors, one of which was preinstalled on [Lenovo PCs](https://nakedsecurity.sophos.com/2015/02/20/the-lenovo-superfish-controversy-what-you-need-to-know), were found to severely compromise the security of end users in February of 2015. Later that same year, German journalist [Hanno Böck](https://blog.hboeck.de/archives/869-How-Kaspersky-makes-you-vulnerable-to-the-FREAK-attack-and-other-ways-Antivirus-software-lowers-your-HTTPS-security.html) looked at three popular antivirus suites and found that all lowered security by either exposing end users to vulnerabilities like FREAK and CRIME or supporting less secure encrpytion algorithms.

In early 2017 researchers teamed up with Google, Mozilla, and Cloudflare for an internet-wide survey - [The Security Impact of HTTPS Interception](https://jhalderm.com/pub/papers/interception-ndss17.pdf). TLS interception software was assessed based on how the TLS connection observed from the client differed from the TLS parameters advertised by the client. In all but two of the tested products, security was reduced, and in some cases serious vulnerabilities were introduced. Most recently in February of 2017, a Chrome 56 update took down almost a third of Montgomery County Public School's 50,000 fleet of Chromebooks offline, because the school systems web filter, BlueCoat Proxy, [did not properly handle TLS 1.3](https://bugs.chromium.org/p/chromium/issues/detail?id=694593). When Chrome attempted to connect via TLS 1.3, the Bluecoat software abruptly terminated the connection, rather than negotiating for TLS 1.2.
 
### How SSL/TLS interception works

SSL/TLS interception is performed by software on "middleboxes" located in between the client and HTTPS website or on the client’s machine, in the case of malware, anti-virus software, and ad injectors.  Middlebox software has both legitimate and illegitimate use cases and often belongs to one of the following categories:
* proxies or content filters
* antivirus suites
* content cachers
* advertisement injectors
* malware

![Middlebox framework](/images/tls-interception/middlebox_proxy_setup.png)

###### Source: [The Security Impact of HTTPS Interception (2017)](https://zakird.com/papers/https_interception.pdf)

Middlebox proxy software relies on the client having previously installed a root certificate onto their operating system. Any outgoing SSL/TLS connections from the client are terminated and re-established by the proxy to the server, which acts as a man-in-the-middle. In an ideal situation, the proxy's ClientHello mirrors the TLS parameters expressed in client's ClientHello, to avoid modifying the client request. The proxy can then inspect plaintext and establish a TLS connection back to the client using the installed certificate to circumvent browser warnings and silently man-in-the-middle the connection between client and server.

### 2015: Lenovo / Superfish

In 2015, there was in an incident involving Lenovo PC's shipped with a preinstalled image advertisement optimizer developed by Superfish. Superfish used Komodia's tool "SSL hijacker" to intercept HTTPS connections in order to gather image data for its ad optimization engine. Komodia's tool is similar to to all SSL inspectors - it first installs root certificates on the client machine and then MITMs all TLS connections to HTTPs websites, issuing the  preinstalled Komodia certificate to the client instead of the target HTTPS server's certificate to bypass browser warnings.

Unfortunately, the private key for the certificate was hardcoded into the software and could be trivially extracted by the end user. In addition, Komodia used the same private key for every machine running Superfish. It didn't take long for security researcher [Robert Grahm](http://blog.erratasec.com/2015/02/extracting-superfish-certificate.html) to crack the password for the private key. (it was 'komodia'). With this key, an adversary could MITM any client running Superfish on their laptop by using using a copy of this hardcoded certificate. To compound on this, users were not alerted to the presence of Superfish software on their new Lenovo laptops.

[Komodia released a security notice](http://www.komodia.com/security-notice) saying they fixed the issue by updating the software to create **unique** certificates per installation and **randomly** generated passwords. They also addressed other potential vulnerabilities such as updating their list of supported cipher suites and verifying certificate revocation statuses (they support OCSP). The countermeasures outlined in their security notice serve as a starting point for all HTTPS interception software developers.

### Later in 2015: PrivDog & Atrustmedia

Shortly after the Superfish incident, another piece of TLS interception software named PrivDog made by Adtrustmedia was also [found to be vulnerable](https://www.kb.cert.org/vuls/id/366544). PrivDog is an advertisement program which intercepts HTTPS connections and replaces "bad" advertisements with advertisements approved by Adtrustmedia. 

Privdog, like the aforementioned Superfish, simply replaced certificates for a HTTPS server with new certificates signed by the root certificate they installed on the affected machine. However, the Privdog software performed no validation of the original certificate presented by the target server. Not only did it make untrusted certificates seem trusted, but legitimite websites with [EV Certificates](https://en.wikipedia.org/wiki/Extended_Validation_Certificate) were replaced with PrivDog's self signed certificate removing the green browser indication. Any website an affected user visited with an invalid certificate would appear valid, without browser warnings. An adversary could easily MITM a client running PrivDog by simply advertising a self-signed certificate!

### 2017: "The Security Impact of HTTPS Interception"

###### [The Security Impact of HTTPS Interception (2017)](https://zakird.com/papers/https_interception.pdf) by Durumeric et al.

![Grades for middlebox interception](/images/tls-interception/middlebox_interception.png)

In early 2017, researchers teamed up with Google, Mozilla and Cloudflare in efforts to measure TLS interception in an internet wide [study](https://zakird.com/papers/https_interception.pdf). They noted that TLS interception software can be detected from the server's point of view by identifying a mismatch between popular browsers TLS handshakes and the observed handshake. Going one step further, by observing the TLS handshakes of popular interception software they were able to construct fingerprints for some of the most widely used interception products. 

The study measured interception from the vantage point of the Cloudflare CDN, Firefox Update servers, and popular e-commerce sites. Important results from the study found that about 5-10% of measured HTTPS connections were intercepted, and much of the software reduced the security of the end user in one way or another, with 97%, 54%, and 32% of connections to Firefox, Cloudflare, and e-commerce sites becoming less secure respectively. Interestingly, the only middlebox software to earn a grade of ‘A’ was BlueCoat Proxy.

### 2017: Chrome 56 update breaks Bluecoat Proxy v6.5

> **Note these issues are always bugs in the middlebox products.** TLS version negotiation is backwards compatible, so a correctly-implemented TLS-terminating proxy should not require changes to work in a TLS-1.3-capable ecosystem [...] That these products broke is an indication of defects in their TLS implementations
> 
> -- *[David Benjamin](https://bugs.chromium.org/p/chromium/issues/detail?id=694593#c26), (2017), Chromium Bug Tracker*

On February 21 2017, a few weeks after the above paper was published, mishandling of TLS 1.3 connections by BlueCoat Proxy left thousands of clients without internet connection after an automatic Chrome 56 update. The problem wasn’t that BlueCoat Proxy didn’t implement TLS 1.3, but that it didn’t gracefully renegotiate down to TLS 1.2 which it does support. Instead, the software simply terminated the incoming connection. This left tens of thousands of Chromebooks used by Montgomery County Public Schools students temporarily unable to connect to the internet. The temporary solution was for individual users to alter Chrome's internal settings to disable TLS 1.3 [chrome://flags/#ssl-version-max](chrome://flags/#ssl-version-max) until a more general solution was delivered by [the following day](https://bugs.chromium.org/p/chromium/issues/detail?id=694593#c12) by Chromium, which rolled-back TLS 1.3 support by default.

## Going Forward

Whether it be at the cost of availability or end user security, these incidents expose the fragility of TLS interception software. Google has reached out to middlebox vendors in efforts to help them resolve the issues, but vendors should independently strive to fix their products for the security of their users at the same time. Organizations who deploy TLS interception software should choose products in an informed manner, including by consulting resources like the results of the ["The Security Impact of HTTPS Interception"](https://zakird.com/papers/https_interception.pdf) to decide whether a product's treatment of TLS connections reflects their security needs. 

![Grades for various clientside interception](/images/tls-interception/clientside_interception.png)

###### Source: [The Security Impact of HTTPS Interception (2017)](https://zakird.com/papers/https_interception.pdf)
