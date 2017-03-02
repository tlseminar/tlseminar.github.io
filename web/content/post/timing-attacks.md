+++
title = "Timing Attacks"
author = "Team Cinnamon"
date = "24 Feb 2017"
draft = false
slug = "timing-attacks"
+++

# Digression: Notable News

Two newsworthy events occurred at the time of this post's creation. While not strictly related to timing attacks, they are of high importance and relevant to TLS in general.

### The First SHA-1 Collision

On February 23rd, 2017, [Google announced](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html) (in collaboration with the [CWI Institute in Amsterdam](https://www.cwi.nl/)) that it had created the first SHA-1 collision.  As proof of this claim, two PDFs were published that yield the same SHA-1 hash despite containing different content ([PDF 1](https://shattered.it/static/shattered-1.pdf), [PDF 2](https://shattered.it/static/shattered-2.pdf)).

<center><img src="/images/timing-attacks/collision.png" alt="PDF Collision" style="width:600px;"/><br>
<sup>https://shattered.it/static/shattered.png</sup></center>

While not the first theoretical attack against SHA-1, Google's attack was the first succesful practical attack. While SHA-1 was deprecated by NIST in 2011, many systems still extensively use SHA-1 (git, SVN, even some [certificate authorities](https://www.riskiq.com/blog/labs/wosign-and-startcom-caught-red-handed/), etc.). Google argues that these findings should reinforce the need to more secure hashing algorithms:

> _We hope that our practical attack against SHA-1 will finally convince the industry that it is urgent to move to safer alternatives such as SHA-256._

### Attack Details

SHA-1 takes an arbitrary length message and computes a 160-bit hash. It divides the (padded) input into \\(k\\) blocks \\(M\_1, M\_2, ..., M\_k\\) of 512 bits. The 160-bit internal state \\(CV\_j\\), called the chaining value, is initialized to some initial value \\(CV\_0 = IV\\). Then, each block \\(M\_j\\) is fed to a compression function \\(h\\) that updates the chaining value, \\(CV\_{j+1} = h(CV\_j, M\_{j+1})\\). \\(CV\_k\\) Is the output of the hash.

Google's attack builds upon the best known theoretical collision attack outlined by [Stevens (2013)](https://marc-stevens.nl/research/papers/EC13-S.pdf). This attack is an _identical-prefix collision attack_, where a given prefix \\(P\\) is extended with two distinct _near collision block pairs_ such that they collide for any suffix \\(S\\):

$$ \text{SHA-1}(P||M\_1^{(1)}||M\_2^{(1)}||S) = \text{SHA-1}(P||M\_1^{(2)}||M\_2^{(2)}||S) $$

Finding both the first and second near collision block pairs, (\\(M\_1^{(1)}, M\_1^{(2)}\\)) and (\\(M\_2^{(1)}, M\_2^{(2)}\\)), respectively, was completed using slightly modified algorithms from Steven's work. Broadly speaking, differences in the first block pair cause a small difference in the output chaining value, which is "canceled" by the difference in the second block pair. The remaining identical suffixes ensure a collision. _Differential paths_ are leveraged as a precise description of the differences in block pairs and how these differences evolve through the hashing steps. This description is the foundation of a search over the possible block pairs.

The PDF format is exploited by packaging the differing collision blocks into an embedded JPEG image. In the example collision, the differing blocks are aligned such that the background of the PDFs are different.

<center><img src="/images/timing-attacks/pdf-enc.png" alt="PDF Encoding" style="width:600px;"/><br>
<sup>https://shattered.it/static/pdf\_format.png</sup></center>

A significant contribution of Google's work is the application of the above algorithms at a scale necessary for practical execution. While the source code for these computations has not yet been released (the authors are allowing a grace period to move to modern hashing algorithms), the changes required to scale this attack are highly non-trivial. Combined, the computations required approximately 6500 CPU years and 100 GPU years. At the time of publishing, the authors estimate the total cost of their attack (via AWS) at $110,000, easily within the reach of criminals. This attack is estimated to be approximately 100,000 times faster than a brute force search.

Full technical details of the attack are outlined in the released [paper](https://shattered.it/static/shattered.pdf).

# The Cloudflare Leak

### How the Incident Developed

Cloudflare is an Internet infrastructure company that provides security and performance services to millions of websites.  On February 17th, 2017, a security researcher from [Google's Project Zero](https://googleprojectzero.blogspot.com/), Travis Ormandy, noticed that some HTTP requests running through Cloudflare were returning corrupted web pages. 

<center><img src="/images/timing-attacks/cloudflare/tweet.png" alt="Travis Ormandy's Tweet" style="width:500px;"/>
<sup>[https://twitter.com/taviso/status/832744397800214528](https://twitter.com/taviso/status/832744397800214528)</sup></center>

The problem that Travis noticed was that under certain circumstances, when the Cloudflare "edge servers" returned a web page, they were going past the end of a buffer and adding to the HTML dumps of memory that contained information such as auth tokens, HTTP POST bodies, HTTP cookies, and other private information [1]. To make matters worse, search engines both indexed and cached this data such that it was for a while searchable [1]. 

<center><img src="/images/timing-attacks/cloudflare/leak.png" alt="Example Leaked Data" style="width:500px;"/>
<sup>[http://pastebin.com/AKEFci31](http://pastebin.com/AKEFci31)</sup></center>

Since the discovery of the bug, Cloudflare worked with Google and other search engines to remove affected the cached pages.

### The Impact

Data could have been leaking at early as September 22nd [2], but Cloudflare reported that the period of highest impact was from February 13th through February 18th with around 1 in every 3,300,000 HTTP requests have a potential memory leakage [1]. It is difficult to assess how much data was leaked, especially since the corrupted results and their cached versions were quickly removed from search engines, but Wired reports that data from large companies such as Fitbit, Uber, and OKCupid was found in the corrupted pages of a set of affected web pages [2].

Cloudflare asserts that the leak did not reveal any private keys, and even though other sensitive information was leaked, it did not appear in the HTML content of particularly high-traffic sites, so the damage was mitigated. 

Overall, about 3000 customer's sites triggered the bug [2], but, as previously noted, the data leaked could have come from any other Cloudflare customer. Cloudflare is aware of about 150 customers who were affected in that way.

### The Bug Itself

As mentioned earlier, the problem resulted from a buffer being overrun and thus additional data from memory being written to the HTML of web pages. But how did this happen, and why did it happen now?

Some of Cloudflare's services rely on modifying, or "rewriting," HTML pages as they are routed through the edge servers. In order to do this rewriting, Cloudflare reads and parses the HTML to find elements that require changing. Cloudflare used to use a HTML parser written using a project called [Ragel](https://www.colm.net/open-source/ragel/) that converts a description of a regular language into a finite state machine. However, about a year ago they decided that the Ragel-based parser was a source of technical debt and wrote a new parser called cf-html to replace it [1].

Cloudflare first rolled this new parser our for their [Automatic HTTP Rewrites](https://blog.cloudflare.com/how-we-brought-https-everywhere-to-the-cloud-part-1/) service and have since been slowly migrating other services away from the Ragel-based parser. In order to use these parsers, Cloudflare adds them as a module to [NGINX](https://www.nginx.com/resources/wiki/), a load-balancer [1].

As it turned out, the parser that was written with Ragel actually had a bug in it for several years [1], but there was no memory leak because of a certain configuration fo the internal NGINX buffers. When cf-html was adopted, the buffers slightly changed, enabling the leakage.

The actual bug was caused by what you might expect: a pointer error in the C code generated by Ragel (but the bug was not the fault of Ragel). 

<center><img src="/images/timing-attacks/cloudflare/bug.png" alt="C Code Bug" style="width:500px;"/>
<sup>[https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)</sup></center>

As can be guessed from this snippit, the cause of the bug was that the check for the end of the bugger was done using the equality operator, ```==```, instead of ```>=```, which would have caught the bug. That snippit is the generated code. Let's look at the code that generated that.

In order to check for a the end of the buffer when parsing a ```<script>``` tag, this piece of code was used:

<center><img src="/images/timing-attacks/cloudflare/bug2.png" alt="Ragel Bug Code" style="width:500px;"/>
<sup>[https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)</sup></center>

What it means is that in order to parse the end of the tag, zero or more ```unquoted_attr_char``` are parsed followed by whitespace, ```/```, or ```>``` signifying the end of the tag. If there is nothing wrong with the script tag, the parser will move to the code in the ```@{ }```. If there is a problem, the parser will move to the ```$lerr{ }``` section.

The bug was caused if a web page **ended** with a malformed HTML tag such as ```<script type=```. The parser would transition to ```dd("script consume_attr failed")``` which is just print debug output, but then **instead of failing, it transitions to ```fgoto script_consume_attr;```**, which means it tries to parse another attribute.

Notice that the ```@{ }``` block has a ```fhold``` while the ```$lerr{ }``` block does not. It was the lack of the ```fhold``` in the second block that caused the leak. In the generated code, ```fhold``` is equivalent to ```p--``` and thus if the malformed tag error happens at the end of the buffer, then ```p``` will actually be after the end of the document and the check for the end of the buffer will fail, causing ```p``` to overrun the buffer.

### The Response From Cloudflare

Cloudflare seems to have responded relatively well to this bug. After the bug was brought to their attention they performed an initial mitigation, which meant disabling all of the sevices that used cf_html, in 47 minutes. Luckily, Cloudlfare uses a 'global kill' [1] feature to enable the global disabling of any service. Since the Email Obfuscation was the main cause of the leak, it was disabled first, and then Automatic HTTPS rewrites were killed about 3 hours later [1]. About 7 hours after the bug was detected, a fix was deployed globablly. As mentioned previously, Cloudflare also contacted search engines to get the affected pages and their cached versions removed from the web.

What was not as good about Cloudflare's response were the lessons they said they learned in their incident report. Essentially, their lessons learned amounted to saying the bug was a corner case in an "ancient piece of software" and that they will be looking to "fuzz older software" to look for other potential problems [1].

### Further Thoughts

Bugs like this expose the difficulty of ensuring software correctness. It is quite unlikely that a corner case like this would have been caught by human eyes, and even a fuzzer would have had to have triggered some exceptional conditions in order to 
exposed the bug. It seems like this could have possibly been avoided if a formally verified implementation of the parser was made and then used to generate safer code.

### References

[1] [https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)
[2] [https://www.wired.com/2017/02/crazy-cloudflare-bug-jeopardized-millions-sites/](https://www.wired.com/2017/02/crazy-cloudflare-bug-jeopardized-millions-sites/)

# Introduction 

Timing attacks are a type of vulnerability exploited through information leaked from timing side-channels. In this threat model, an attacker is able to observe the time required for certain parts of a program at runtime and gain information about the execution path followed. 

We examine the following snippet of Python code as an example:

```python
def comp(a,b):
if len(a) != len(b):
return False
for c1, c2 in zip (a,b):
if c1 != c2:
return False
return True
```

We see that the `comp()` function performs string comparison, returning True if the strings are character-wise equal and false otherwise. Let us assume for the sake of simplicity that the lengths of the strings are public (i.e. we are not concerned with timing leaks from the initial length comparison). Let us first look at a comparison of the words “hello” and “catch”. These words fail the string comparison immediately, since `“h” != “c”`. Thus, the function returns False after a single iteration of the loop. In contrast, comparing “hello” to “hella” will require 5 iterations before returning False. An attacker can use the resulting timing delay to determine that “hello” and “hella” share beginning characters, whereas “hello” and “catch” do not. If “hello” was a secret word, the attacker would gain knowledge about the secret. 

One solution to this problem would be to use a boolean flag initialized to True. If the words have mismatched characters, the flag will be set to False, and the flag will be returned after comparing all characters. In theory, this masks the timing leak; in practice, a compiler may optimize such code to return early, reinstating the timing leak. Furthermore, there may still be timing leaks in the execution of the code, such as variation in the instruction cache depending on which statements are entered. 

Thus, we see from this simple example that verifying constant-time implementation of code has many challenges, which we further discuss below.

# Remote Timing Attacks are Practical
[Paper link](docs/ssl-timing.pdf)

At the heart of RSA decription is a modular exponentiation \\( m = c^d mod~N\\) where \\(N = pq\\) is the RSA modulus, d is the private decryption exponent, and c is the ciphertext being decrypted. OpenSSL uses the Chinese Remainder Theorem (CRT) to perform this exponentiation. With Chinese remaindering, the function \\( m = c^d mod~N\\) is computed in two steps.

First, evaluate \\( m_1 = c^{d_1} mod~p\\) and \\( m_2 = c^{d_2} mod~q\\) (\\(d_1\\) and \\(d_2\\) are precomputed from \\(d\\)).

Then, combine \\(m_1\\) and \\(m_2\\) using CRT to yield m.

### Chinese Remainder Theorem
Suppose that \\(n_1,n_2,...,n_r\\) are pairwise relatively prime positive integers, and let \\(c_1,c_2,...,c_r\\) be integers.

Then the system of congruences,

\\(X \equiv c_1 (mod~n_1)\\) 

\\(X \equiv c_2 (mod~n_2)\\)

... 

\\(X \equiv c_r (mod~n_r)\\)

has a unique solution modulo \\(N = n_1n_2...n_r\\)
### Gauss’s Algorithm
\\(X \equiv c_1N_1{N_1}^{-1} + c_2N_2{N_2}^{-1} + ... + c_rN_r{N_r}^{-1}(mod~N)\\), where

\\(N_i = N/n_i \\)

\\(N_i{N_1}^{-1} \equiv 1 (mod~n_i)\\)

### Hasted’s Broadcast Attack (add with Chinese Remainder Theorem)
Hasted's Broadcast Attack relies on cases when the public exponent \\(e\\) is small or when partial knowledge of the
secret key is available.
If \\(e\\) (public) is the same across different sites, the attacker can use Chinese Remainder Theorem and decrypt messages!

Hasted’s Broadcast Attack works as follows:

Alice encrypts the same message \\(M\\) with three different public keys \\(n_1\\) \\(n_2\\) and \\(n_3\\)
, all with public exponent \\(e=3\\), The resulting \\(C_1C_2\\) and \\(C_3\\) are known.

\\(M^3 \equiv c_1 (mod~n_1)\\) 

\\(M^3 \equiv c_2 (mod~n_2)\\)

\\(M^3 \equiv c_3 (mod~n_3)\\)

An attack can then recover \\(M\\) as follows:

\\(x = C_1N_1N_1^{-1} + C_2N_2N_2^{-1} + C_3N_3N_3^{-1}~mod~n_1n_2n_3 \\)

\\(M = \sqrt[3]{x}\\)

### Montgomery Reduction
The Montgomery Reduction is an algorithm  that allows modular arithmetic to be performed 
efficiently when the modulus is large.

The reduction takes advantage of the fact that \\(x~mod~2^n\\) 
is easier to compute than \\(x~mod~q\\); the reduction simply strips off all but the \\(n\\) least significant bytes.

Steps needed for the reduction:

- The Montgomery Form of \\(a\\) is \\(aR~mod~q\\), where \\(R\\) is some public \\(2n , n\\) chosen based on underlying hardware.

- Multiplication of \\(ab\\) in Montgomery Form: \\(aRbR = cR2\\).

- Pre-compute \\(RR^{-1}~mod~q\\).

- Reduce: \\(cR^{2}R^{-1}~mod~q = cR~mod~q\\).

- \\(c\\) can be kept in form and reused for additional multiplications during sliding windows.

- To escape Montgomery space and return to \\(q\\) space: multiply again by \\(R^{-1}\\) to arrive at solution \\(c\\). 

- \\(c = ab~mod~q\\) (performing \\(mod\\) by \\(q\\) causes successive subtractions of \\(ab\\) by \\(q\\) till result \\(c\\) in range \\([0,q)\\).
The paper identifies these "extra reductions")

### Protections against timing attacks:
There are numerous defenses against timing attacks! For instance:

A decryption routine with the number of operations being independent of input: 

- This is akin to Montgomery's Latter, as described above. Simply carry out the Montgomery extra reduction, 
even if it's not necessary. This might be hard to mend to existing systems without replacing their entire decryption algorithm
(What if the compiler optimizes this away?).

By quantizing all RSA computations: 

- This decreases performance because "all decryptions must take the maximum time of
any decryption".

By blinding, which works as follows:

- Calculate \\(x = reg~mod~N\\) before actual decryption for random \\(r\\) chosen each time

- Decrypt as normal.

- Unblind: divide by \\(r~mod~N\\) to obtain the decryption of the ciphertext
\\(g\\).

- Since \\(r\\) is random, \\(x\\) is also random -- and input \\(g\\) should have minimal
correlation with total decryption time.

<center><img src="/images/timing-attacks/gap.jpg" alt="PDF Collision" style="width:500px;"/><br>
([Image credit]
(http://slideplayer.com/slide/4519452/))</center>


# Remote Timing Attacks are Still Practical
[Billy Bob Brumley and Nicola Tuveri. "Remote timing attacks are still practical." European Symposium on Research in Computer Security. Springer Berlin Heidelberg, 2011.](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf)

Timing attacks target cryptosystems and protocols that do not run in constant time. [Elliptic curve](https://en.wikipedia.org/wiki/Elliptic_curve_cryptography) based [signature schemes](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) aim at providing side-channel resistance against timing attacks. For instance, scalar multiplication is achieved via [Montgomery's ladder](https://cr.yp.to/bib/2003/joye-ladder.pdf) which performs a sequence of independent field operations on elliptic curves. [Brumley and Tuveri](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf) reveal a timing attack vulnerability in OpenSSL's implementation of Montgomery's ladder that consequently leaks the server's private key.

### What is Montgomery's Ladder?
Consider the right-to-left square-and-multiply algorithm to compute an exponentiation operation:
<center><img src="/images/timing-attacks/right-to-left.png" alt="Montgomery ladder" style="width:500px;"/><br>
<sup>Right-to-Left Square-and-Multiply Algorithm</sup><br><sup>Source: https://cr.yp.to/bib/2003/joye-ladder.pdf</sup></center>

The above algorithm performs more operations when the bit is set, thereby leading to a possible timing attack. Montgomery's power ladder method, on the other hand, performs the same number of operations in both the cases. This prevents timing based side-channel attacks as well as makes the algorithm more efficient by making it parallelizable. The algorithm is as below:
<center><img src="/images/timing-attacks/montgomery.png" alt="Montgomery ladder" style="width:500px;"/><br>
<sup>Montgomery's Ladder</sup><br><sup>Source: https://cr.yp.to/bib/2003/joye-ladder.pdf</sup></center>

### OpenSSL's implementation of Montgomery's Ladder
OpenSSL uses Elliptic Curve Cryptography for generating Digital Signatures to sign a TLS server's RSA key.
Elliptic Curve Cryptography for Digital Signature uses the following curve for binary fields:
<center><img src="/images/timing-attacks/curve.png" alt="ECC" style="width:400px;"/></center>
NIST recommends two standard curves: 1. Set a2 = 1 and choose a6 pseudo-randomly, or 2. Choose a2 from {0,1} and set a6 = 1.
Either of the two curves can be used for digital signatures. Parties select private key as 0 < d < n and public key as [d]G and then proceed to generate digital signatures using elliptic curves as:
<center><img src="/images/timing-attacks/digital_signatures.png" alt="digital" style="width:300px;"/></center>
OpenSSL uses Montogmery's ladder to compute the above digital signatures since it requires multiple exponentiation operations. However, OpenSSL's implementation has a flaw that leads to timing attack. Below is OpenSSL's implementation:
<center><img src="/images/timing-attacks/OpenSSL_montgomery.png" alt="OpenSSL" style="width:700px;"/><br>
<sup>OpenSSL's implementation of Montgomery's Ladder</sup><br>
<sup>Source: https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf</sup></center>
As indicated in the third line of code, OpenSSL optimizes the number of ladder steps and therefore leaks information about the MSB of k. Since the time taken to compute the scalar multiplications is proportional to the logarithm of k, which is revealed by the MSB of k, this leads to a timing attack. The attacker collects multiple digital signatures such that the signatures are generated by random nonce k with leading zero bits; this information is revealed by the above timing attack. The attacker then launches a [lattice attack](http://www.hpl.hp.com/techreports/1999/HPL-1999-90.pdf) using the collected digital signatures to reveal the RSA key of the TLS server.

### Countermeasure
A possible countermeasure as proposed by [Brumley and Tuveri](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf) is to pad the scalar k as follows:
<center><img src="/images/timing-attacks/countermeasure.png" alt="counter" style="width:400px;"/><br>
<sup>Countermeasure to OpenSSL's flaw</sup><br>
<sup>Source: https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf</sup></center>
This ensures that the logarithm is constant and hence leaks no side-channel information. Moreover, the above modification does not cause extra computation overhead.

### Sources

[Marc Joye and Sung-Ming Yen. "The Montgomery powering ladder." International Workshop on Cryptographic Hardware and Embedded Systems. Springer Berlin Heidelberg, 2002.](https://cr.yp.to/bib/2003/joye-ladder.pdf)

[Billy Bob Brumley and Nicola Tuveri. "Remote timing attacks are still practical." European Symposium on Research in Computer Security. Springer Berlin Heidelberg, 2011.](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf)

[Howgrave-Graham, Nick A., and Nigel P. Smart. "Lattice attacks on digital signature schemes." Designs, Codes and Cryptography 23.3 (2001): 283-290.](http://www.hpl.hp.com/techreports/1999/HPL-1999-90.pdf)

# Cache Timing Attacks

At this point, it seems as though we've seen everything—there couldn't possibly be another side-channel attack, right?

Wrong. 

Timing attacks are capable of leveraging the <strong>CPU cache</strong> as a side-channel in order to perform attacks.  Since the issue results from hardware design, it's difficult for application designers to address; the behaviors that influence cache patterns are proprietary features hidden away into today's processors.

### Intel CPU Cache
In cache terminology, <strong>hits</strong> occur when queried data is present in the cache and <strong>misses</strong> occur when data must be fetched from main memory.  Consider the L1 and L2 caches of the Intel Sandy Bridge processor.  Both are <strong>8-way set associative caches</strong> consisting of sets with 64-byte lines (64 sets in L1, 512 sets in L2, for a total of 32KB and 256KB in storage, respectively).  

For those unfamiliar with computer architecture, addresses of information in the cache are split into three components:  tag, set, and offset.  An address looks something like this:
```
1111 0000 1111 0000 1111        000011       110000
Tag                              Set         Offset
```

Now that we've reviewed the memory hierarchy, let's take a look at some attacks that use variations in cache timing and operation to their advantage.

### PRIME+PROBE
The PRIME+PROBE attack is carried out by <strong>filling the victim's cache with controlled data</strong>.  As the victim carries out normal tasks in their machine, some of the attack data is evicted from the cache.  All the while, the attacker monitors the cache contents, keeping careful track of which cache lines were evicted.  In doing so, this provides the attacker with intimate knowledge of the operation and nature of the victim's activities as well as the contents replaced by the victim.

### EVICT+TIME

The EVICT+TIME attack is carried out by evicting a line of an AES lookup table from the cache such that all AES lookup tables are in the cache save for one.  The attacker then runs the encryption process.  As you might imagine, <strong>if the encryption process accesses the partially evicted lookup table, encryption will take longer to complete</strong>.  By timing exactly how long encryption takes, the attackers are able to determine which indices of which tables were accessed.  Because table lookups depend on the AES encryption key, the attacker thus gains knowledge about the key.

### Cache Games

The Cache Games attack targets AES-128 in OpenSSL v0.9.8 and is capable of recovering the full secret key.  In the attack, a non-privileged spy process conducts a 2.8 second observation of approximately 100 AES encryptions (1.56KB of data) and then performs 3 minutes of computation on a separate machine.  The spy process is able to abuse the default Linux scheduler, unfortunately named the <em>Completely Fair Scheduler</em>, to monitor cache offset accesses with extremely accurate precision, thus gaining information about the key.  

In order to abuse the CFS, the spy process creates hundreds of threads that immediately block.  After a few cycles, the first thread awakens, checks for memory accesses by the target code, and then signals for the next thread to awaken.  This continues for all threads.  To filter-out noise, Cache Games uses an ANN that takes bitmaps of activations and outputs points with high probability of access.

<center><img src="/images/timing-attacks/cachegames.png" alt="Cache Games ANN" style="width:300px;"/><br /><sup>An ANN takes bitmaps of activations and outputs <br />points with high probability of access</sup></center>

The nature of the AES encryption process—consisting of 10 rounds of 16 memory accesses—allows the spy process to construct a list of partial-key candidates that is continually refined as more encryptions are repeated.  The CFS maintains processes in a red-black tree and associates with each process a total runtime.  The scheduler calculates a "max execution time" for each process by dividing the total time it has been waiting by the number of processes in the tree.  Whichever process minimizes this value is selected to run next.

#### Mitigation

* Remove or restrict access to high-resolution timers such as ```rdtsc``` (unlikely; necessary to benchmark various hardware properties)
* Allow certain memory to be marked as <em>uncacheable</em> (hardware challenge!)
* Use AES-NI instructions in Intel chips to compute AES (but what about other encryption algorithms?)
* Scatter-gather:  secret data should not be allowed to influence memory access at coarser-than-cache-line granularity.

### Cachebleed

In keeping with the trend of affixing "-bleed" to various information security leakage vulnerabilities, CacheBleed is a very recent (c. 2016) attack on RSA decryptions as implemented in OpenSSL v1.0.2 on Intel Sandy Bridge processors.  In the attack, the timing of operations in <strong>cache banks</strong> is taken advantage of in order to glean information about the RSA decryption multiplier.

Cache banks were a new feature in Sandy Bridge processors, designed to accommodate accessing multiple instructions in the same cache line in the same cycle.  As it turns out, cache banks can only serve one operation at a time, so if a <em>cache bank conflict</em> is encountered, one request will be delayed!

In order to carry-out the attack, the attacker and victim start out running on the same hyperthreaded core, thus sharing the L1 cache.  The attacker then issues a huge number of requests to a single cache bank.  By carefully measuring how many cycles passed in completion of the request, the attacker can discern whether the victim accessed that cache bank at some point.  After many queries, the attack is successful at extracting both 2048-bit and 4096-bit secret keys.  

#### Mitigation

The upside to CacheBleed is that it's highly complicated, requiring shared access to a hyperthreaded core on which RSA decryption is taking place—certainly not a predictable scenario.  In any case, there are other pieces of "low-hanging fruit" in computer systems that attackers are more likely to target.  Nonetheless, Haswell processors implement cache banks differently such that conflicts are handled more carefully.  The only other mitigation technique is to disable hyperthreading entirely.

