# Projects

(See [Project Ideas](/projectideas) page for some ideas for projects.)

### Minimal TLS

[**Project Site**](https://github.com/cmalekpour/minimal-tls)  
**Team members:** <a href="https://github.com/FreddieJin">Tianyi Jin</a>, <a href="https://github.com/cmalekpour">Cyrus Malekpour</a>, <a href="https://github.com/bhuvanesh8">Bhuvanesh Murali</a>, <a href="https://github.com/drs5ma">Daniel Saha</a>  

**Problem.** In recent years, TLS implementations have been targeted with memory corruption or leakage issues, which they are vulnerable. Since they are implemented in C/C++, it is difficult to make these implementations resistant to such attacks. Many implementations also attempt to include a wide variety of cipher suites, which drastically increases the amount of crypto code that needs to be audited and written securely.

**Goal.** We plan to create a "minimal" implementation of TLS with the goal of 95% support of browser clients. To accomplish this, we will identify the least possible set of server features and cipher suites we can support to meet this goal, with a strong focus on security. We will implement only a few key TLS extensions (ex: SNI, OCSP) with fail-safes for other features. The project will be written in the Rust programming language to provide good performance while removing the risk of memory corruption attacks.

### QuantumMenace

[**Project Site**](https://reidbix.github.io/QuantumMenace/): Analyzing postquantum applications for TLS and SSL  
**Team members:** Reid Bixler, Collin Berman  

In this blog we will be looking into various topics including post-quantum signatures, effects of quantum computing on TLS, benefits of switching to post-quantum algorithms, benefits of some post-quantum algorithms over others, and whatever other topics come up.

### DecentralizedCA

[**Project Site**](https://hainali.github.io/DecentralizedCA/)  
**Team members:** <a href="https://github.com/bargavjayaraman">Bargav Jayaraman</a>, <a href="https://github.com/HainaLi/">Hannah Li</a>

The project idea is to allow multiple CA servers to collaboratively
generate a certificate using multi-party computation protocols,
thereby acting like a "Decentralized CA".

### ssltimer

SSLTimer: Testing an SSL Implementation with respect to Timing Attack Vulnerability

[**Project Site**](https://github.com/yuchi1989/ssltimer/)  
**Yuchi Tian**  


### sok-tle-testing

SoK: Software Testing Methods Applied to SSL/TLS: Lessons in Discovering Implementation Bugs

[**Project Site**](https://darioncassel.github.io/sok-tls-testing/)  
**Darion Cassel**

There have been many attempts at discovering bugs in implementations
of SSL/TLS. We would like to present a taxonomy of these attempts in
order to better understand what their essential features are, what
classes of bugs these features are likely to capture, and what classes
of bugs are blind spots for this field.

### TIE: TLS Invariants Exploration

[**Project Site**](https://lowmanb94.github.io/tie/)  
**Ben Lowman**

Implementing TLS is hard. Given the wide range of cipher suites,
target platforms, and legacy code, it is unlikely that any TLS
implementations are free of bugs (see Heartbleed, Apple’s goto fail,
CCS injection, etc.). Rigorous testing is required in cases where
formal verification is not feasible. For most implementations,
traditional software engineering techniques are the primary means by
which confidence is gained in the correctness of the implementation.

My goal is to explore the use of program invariants in testing TLS
implementations. Inferred program invariants are a compressed
expression of program state, independent of control flow or
output. Dynamically inferred invariants (over test cases) could be
compared to ground truth invariants as a more robust method to verify
program correctness. It is also likely that different TLS
implementations exhibit similar invariants. I am interested in
exploring the possibility of employing Frankencerts-type differential
testing over dynamically inferred program invariants in addition to
expected output. This will require abstracting program invariants in a
meaningful way so that such “similar” invariants can be compared
directly.

### Line Of Trust

[**Project Site**](https://lineoftrust.github.io/)  
**Team members:** Anant Kharkar, Sam Havron, Bethlehem Naylor, Bill Young, Joshua Holtzman

Introducing the Line of Trust (LOTr): Erasing the line of death for fun and pleasure

### SSLskimmer

[**Project Site**](http://adamimeson.tech/sslskimmer/)  
**Adam Imeson**

In 2009, Moxie Marlinspike released an attack by the name of
SSLstrip. It allows man-in-the-middle attackers to strip the security
from HTTPS server responses, forwarding naked HTTP to the victim. If
the victim does not notice that they are no longer using a secure
connection they are likely to submit login details and other sensitive
information to stripped pages. The attacker reads the information
before forwarding it to the server.

I posit that the attack remains effective despite various
countermeasures implemented by browser vendors and web services. Given
the general availability of public wifi and its general vulnerability
to MITM attacks via ARP poisoning, it seems that it is only a matter
of time until the type of criminals to run credit card skimmers take
note of SSL skimming opportunities.

I intend to demonstrate susceptibility to this attack by conducting an
ethical study of user awareness. I also intend to build and test a
cheap battery-powered SSLskimmer as a proof of concept.