+++
title = "Timing Attacks"
author = "Team Cinnamon"
date = "24 Feb 2017"
draft = false
slug = "timing-attacks"
+++

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
