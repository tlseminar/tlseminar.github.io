See [Teams](/teams) for the class teams and responsibilities.

<table>
<tr bgcolor="#CCC"><td style="text-align:center" width="22%"><b>Date</b></td><td style="text-align:center"><b>Topic</b></td><td style="text-align:center" width="14%"><b>Cinnamon</b></td><td style="text-align:center" width="14%"><b>Poppyseed</b></td><td style="text-align:center" width=12%><b>Sesame</b></td></tr>

<tr><td><a href="/class 1">Class 1</a> (20 Jan)</td><td>Intro</td><td>Plan</td><td bgcolor="#44AAEE">Blog</td><td>Plan</td></tr>

<tr><td><a href="/padding-oracle">Class 2</a> (27 Jan)</td><td>Padding Oracle Attacks</td><td bgcolor="#CCDD55">Lead</td><td>Food</td><td bgcolor="#44AAEE">Blog</td></tr>
<tr><td><a href="/downgrade-attacks">Class 3</a> (3 Feb)</td><td>Logjam/DROWN</td><td bgcolor="#44AAEE">Blog</td><td bgcolor="#CCDD55">Lead</td><td>Food</td></tr>
<tr><td><a href="/certificates">Class 4</a> (10 Feb)</td><td>Certificates</td><td>Food</td><td bgcolor="#44AAEE">Blog</td><td bgcolor="#CCDD55">Lead</td></tr>
<tr><td><a href="/verification">Class 5</a> (17 Feb)</td><td>Verification and Testing</td><td bgcolor="#CCDD55">Lead</td><td>Food</td><td bgcolor="#44AAEE">Blog</td></tr>
<tr><td><A href="/timing-attacks">Class 6</a> (24 Feb)</td><td>Side Channels</td><td bgcolor="#44AAEE">Blog</td><td bgcolor="#CCDD55">Lead</td><td>Food</td></tr>
<tr><td><a href="/tls-interception">Class 7</a> (3 Mar)</td><td>TLS Interception</td><td>Food</td><td bgcolor="#44AAEE">Blog</td><td bgcolor="#CCDD55">Lead</td></tr>
</table>

<table>
<tr><td bgcolor="#66EEAA" style="text-align:center" colspan=5>Spring Break</td></tr>
</table>

<table>
<tr bgcolor="#CCC"><td width="22%" style="text-align:center"><b>Date</b></td><td style="text-align:center"><b>Topic</b></td><td style="text-align:center" width=20%><b>Team Mango</b></td><td style="text-align:center" width=20%><b>Team Pineapple</b></td></tr>

<tr><td><a href="/usable-security">Class 8</a> (17 Mar)</td><td>Usable Security</td><td bgcolor="#CCDD55">Lead</td><td bgcolor="#44AAEE">Blog, Food</td></tr>
<tr><td><a href="/tls-13">Class 9</a> (24 Mar)</td><td>TLS 1.3</td><td bgcolor="#44AAEE">Blog, Food</td><td bgcolor="#CCDD55">Lead</td></tr>
<tr><td>Class 10 (31 Mar)</td><td colspan=3>Project Reviews</td></tr>
<tr><td><A href="/tls-outside-the-web/">Class 11</a> (7 Apr)</td><td>TLS Everywhere</td><td bgcolor="#CCDD55">Lead</td><td bgcolor="#44AAEE">Blog, Food</td></tr>
<tr><td>Class 12 (14 Apr)</td><td>Future of TLS</td><td bgcolor="#44AAEE">Blog, Food</td><td bgcolor="#CCDD55">Lead</td></tr>
<tr><td>Class 13 (21 Apr)</td><td colspan=3>Post-Quantum Crypto, Progress</td></tr>
<tr><td><a href="/presentations">Class 14</a> (28 Apr)</td><td colspan=3>Mini-Conference</td></tr>
</table>

**[Class 1](/class 1) - Introduction**  
   - [The First Few Milliseconds of an TLS 1.2 Connection](/first-few-milliseconds)

**[Class 2: Oracle Padding Attacks](/padding-oracle)**  

   - [Analysis of the SSL 3.0 Protocol](https://tlseminar.github.io/docs/analysisssl3.pdf)  
   - [Security Flaws Introduced by CBC Padding](http://www.iacr.org/cryptodb/archive/2002/EUROCRYPT/2850/2850.pdf)  
   - [Here Come The XOR Ninjas](https://tlseminar.github.io/docs/beast.pdf)  
   - [Lucky Thirteen: Breaking the TLS and DTLS Record Protocols](http://www.isg.rhul.ac.uk/tls/TLStiming.pdf)  

**[Class 3: Downgrade Attacks](/downgrade-attacks)**

   - [Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice](https://tlseminar.github.io/docs/logjam.pdf)
   - [DROWN: Breaking TLS using SSLv2](https://tlseminar.github.io/docs/drown.pdf)

**[Class 4: Certificates](/certificates)**

   - [SoK: SSL and HTTPS: Revisiting past challenges and evaluating certificate trust model enhancements](/docs/soktls.pdf)
   - [CONIKS: Bringing Key Transparency to End Users](https://eprint.iacr.org/2014/1004.pdf)
   - [Defeating SSL Using SSLstrip](https://www.youtube.com/watch?v=MFol6IMbZ7Y)

**[Class 5: Verification and Testing](/verification)**

   - [*Heartbleed*](http://heartbleed.com/), [*The CRIME Attack*](https://docs.google.com/presentation/d/11eBmGiHbYcHR9gL5nDyZChu_-lCa2GizeuOfaLU2HOU/edit#slide=id.g1e3070b2_0_10), [*Understanding Apple 'goto fail' Vulnerability*](https://www.cigital.com/blog/understanding-apple-goto-fail-vulnerability-2/)
   - Differential Testing: [*Using Frankencerts for Automated Adversarial Testing of Certificate Validation*](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.685.8677), [*An empirical study of goto in C code from GitHub repositories*](http://dl.acm.org/citation.cfm?doid=2786805.2786834)
   - Verification: [*Verifying s2n HMAC with SAW*](https://galois.com/blog/2016/09/verifying-s2n-hmac-with-saw/), [*Implementing TLS with Verified Cryptographic Security*](https://www.microsoft.com/en-us/research/publication/implementing-tls-with-verified-cryptographic-security/), [*Software Foundations*](http://www.cis.upenn.edu/~bcpierce/sf/current/Preface.html#lab2)

**[Class 6: Side Channels](/timing-attacks)**

   - Extra late-breaking news: [SHA-1 Collisions](/sha1-collisions), [Cloudflare Leak](/cloudflare-leak)
   - [Remote Timing Attacks are Practical](/docs/ssl-timing.pdf)
   - [Remote Timing Attacks are Still Practical](/docs/stillpractical.pdf)

