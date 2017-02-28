+++
title = "Timing Attacks"
author = "Team Cinnamon"
date = "24 Feb 2017"
draft = false
slug = "timing-attacks"
+++

# Digression: Notable News

Two newsworthy events occurred at the time of creating this blog post. While not strictly related to timing attacks, they are of high importance and relevant to TLS in general.

## The First SHA-1 Collision

On February 23rd, 2017, [Google announced](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html) (in collaboration with the [CWI Institute in Amsterdam](https://www.cwi.nl/)) that it had created the first SHA-1 collision.  As proof of this claim, two PDFs were published that yield the same SHA-1 hash despite containing different content ([PDF 1](https://shattered.it/static/shattered-1.pdf), [PDF 2](https://shattered.it/static/shattered-2.pdf)).

<center><img src="/images/timing-attacks/collision.png" alt="PDF Collision" style="width:600px;"/><br>
<sup>https://shattered.it/static/shattered.png</sup></center>

While not the first theoretical attack against SHA-1, Google's attack was the first succesful practical. While SHA-1 was deprecated by NIST in 2011, many systems still extensively use SHA-1 (git, SVN, even some [certificate authorities](https://www.riskiq.com/blog/labs/wosign-and-startcom-caught-red-handed/), etc.). Google argues that these findings should reinforce the need to more secure hashing algorithms:

> _We hope that our practical attack against SHA-1 will finally convince the industry that it is urgent to move to safer alternatives such as SHA-256._

### Attack Details

SHA-1 takes an arbitrary length message and computes a 160-bit hash. It divides the (padded) input into \\(k\\) blocks \\(M\_1, M\_2, ..., M\_k\\) of 512 bits. The 160-bit internal state \\(CV\_j\\), called the chaining value, is initialized to some initial value \\(CV\_0 = IV\\). Then, each block \\(M\_j\\) is fed to a compression function \\(h\\) that updates the chaining value, \\(CV\_{j+1} = h(CV\_j, M\_{j+1})\\). \\(CV\_k\\) Is the output of the hash.

Google's attack builds upon the best known theoretical collision attack outlined by [Stevens (2013)](https://marc-stevens.nl/research/papers/EC13-S.pdf). This attack is an _identical-prefix collision attack_, where a given prefix \\(P\\) is extended with two distinct _near collision block pairs_ such that they collide for any suffix \\(S\\):

$$ \text{SHA-1}(P||M\_1^{(1)}||M\_2^{(1)}||S) = \text{SHA-1}(P||M\_1^{(2)}||M\_2^{(2)}||S) $$

Finding both the first and second near collision block pairs, (\\(M\_1^{(1)}, M\_1^{(2)}\\)) and (\\(M\_2^{(1)}, M\_2^{(2)}\\)), respectively, was completed using slightly modified algorithms from Steven's work. Broadly speaking, differences in the first block pair cause a small difference in the output chaining value, which is "canceled" by the difference in the second block pair. The remaining identical suffixes ensure a collision. _Differential paths_ are leveraged as a precise description of the differences in block pairs and how these differences evolve through the hashing steps. This description is the foundation of a search over the possible block pairs.

The PDF format is exploited by packaging the differing collision blocks into an embedded JPEG image. In the example collision, the differing blocks are aligned such that the background of the PDFs are different.

<center><img src="/images/timing-attacks/pdf-enc.png" alt="PDF Encoding" style="width:600px;"/><br>
<sup>https://shattered.it/static/pdf\_format.png</sup></center>

A significant contribution of Google's work is the application of the above algorithms at a scale necessarily for practical execution. While the source code for these computations has not yet been released (the authors are allowing a grace period to move to modern hashing algorithms), the changes necessary to scale this attack are highly non-trivial. Combined, the computations required approximately 6500 CPU years and 100 GPU years. At the time of publishing, the authors estimate the total cost of their attack (via AWS) at $110,000, easily within the reach of criminals. This attack is estimated to be approximately 100,000 times faster than a brute force search.

Full technical details of the attack are outlined in the released [paper](https://shattered.it/static/shattered.pdf).

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


# Remote Timing Attacks are Still Practical
[Paper link](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf)

Timing attacks target at cryptosystems or protocols that donot run in constant time. [Elliptic curve](https://en.wikipedia.org/wiki/Elliptic_curve_cryptography) based [signature schemes](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) aim at providing side-channel resistance against timing attacks. For instance, scalar multiplication is achieved via [Montgomery's ladder](https://cr.yp.to/bib/2003/joye-ladder.pdf) which performs a sequence of input independent field operations on elliptic curve. [Brumley and Tuveri](https://gnunet.org/sites/default/files/Brumley%20%26%20Tuveri%20-%20Timing%20Attacks.pdf) reveal a timing attack vulnerability in OpenSSL's implementation of Montgomery's ladder and consequently reveal the private key of TLS server.
