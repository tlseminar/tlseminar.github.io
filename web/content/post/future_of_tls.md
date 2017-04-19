+++
date = "18 Apr 2017"
author = "Team Mango"
draft = true
title = "The Future of TLS"
slug = "tls-future"
+++


### More Traffic Analysis

TLS traffic analysis can be applied in the following scenarios,  

* Distinguishing between clients on the fly!
* Forensics!
* Intrusion detection!
* Malware detection!
* Homogeneous platform verification!
* Honeypots!

Techniques such as deep packet inspection and TLS flow fingerprinting can be used to distinguish clients, identify whether the encrypted connection is attributed to a Malware or not, and also be used for forensics, intrusion detection and homogeneous platform verification.

#### TLS fingerprinting
[Brotherston, L. (2015). Stealthier attacks and smarter defending with TLS fingerprinting.](https://blog.squarelemon.com/tls-fingerprinting/)  

During an TLS handshake, most clients initiate a TLS handshake request in a unique way. TLS fingerprinting is usually used to recognize a particular client. In TLS fingerprinting, some elements of the Client Hello Packet are filtered and collected to build a database of signatures. The collected elements are usually the combination of TLS version, record TLS version, ciphersuites, compression options, list of extensions, elliptic curves and signature algorithms. The use of this combined elements is not only reliable in terms of remaining static for any particular client, but offers greater granularity than assessing ciphersuites alone, which has a substantially larger quantity of fingerprint collisions. 

### QUIC (Quick UDP Internet Connections)
Internet today relies on TCP as a backbone for secure connections over the web. But TCP protocol introduces latency due to synchronization for channel setup, even before TLS handshake. The figure below shows that an average TCP connection takes 56 ms before the TLS handshake begins. This type of latency is not acceptable in mobile devices or in an area with poor internet reception.
<center><img src="images/future_of_tls/tls_handshake_time.png" alt="TLS Handshake Time" style="width:500px;"/><br>
<sup>TLS Handshake Time (Source: https://hpbn.co/transport-layer-security-tls/)</sup></center>

This motivates the need for faster secure networking by reducing the number of round trips required to establish secure connection. QUIC aims to achieve this by using UDP as backbone instead of TCP.

#### Implementing QUIC
[QUIC](https://www.chromium.org/quic) was introduced by Google and it relies on UDP for fast secure connection. UDP provides quick connection and can handle out of sequence packets but requires resending of failed packets to prevent packet loss. It is an excellent alternative for faster secure connection if security is taken care by the application and leaving UDP to take care of the packet transmission and recovery. This requires both server and client side change in application logic to ensure security. Google has already implemented its [crypto-layer](https://docs.google.com/document/d/1g5nIXAIkN_Y-7XJW5K45IblHd_L2f5LTaDUDwvZ5L6g/edit) and provides experimental libraries like [`libquic`](https://github.com/devsisters/libquic) and [`goquic`](https://github.com/devsisters/goquic), but currently this can only be tested on Google servers.
<center><img src="images/future_of_tls/QUIC.png" alt="QUIC protocol stack" style="width:500px;"/><br>
<sup>QUIC Protocol Stack (Source: https://ma.ttias.be/googles-quic-protocol-moving-web-tcp-udp/)</sup></center>

### InterPlanetary File System (IPFS)

Looking forward to the future of web, it is possible that new models of the Internet will come into play. One such candidate model that is being developed today is the InterPlanetary File System (IPFS). The goal of IPFS replace the Hypertext Transfer Protocol (HTTP) and treat the web as though it is a filesystem and to make the web distributed. Let's unpack what this means and what IPFS can potentially do for the web.

#### The Web, Distributed

A key distinction to make between models of the web are the way "nodes," or computers are linked together. On one end of the spectrum there is the centralized model where a single server contains all the content on the web and every computer must connect to it to retrieve a particular page. If this sounds dystopian and inefficient, it is. This single server would essentially have full say over what content gets to appear on the web and who gets access to it. Thankfully, that is not the model of the web we live under. 


<center><img src="https://www.researchgate.net/profile/Jason_Hoelscher/publication/260480880/figure/fig1/AS:297257619476480@1447883147178/Figure-1-Centralized-decentralized-and-distributed-network-models-by-Paul-Baran-1964.png" alt="Centralized, Decentralized, and Distributed Networks" style="width:500px;"/><br>
<sup>[On Distributed Communications - Baran](http://www.rand.org/content/dam/rand/pubs/research_memoranda/2006/RM3420.pdf)</sup></center>

Our web is better described as a decentralized network. There is no central authority in charge of all of the data on the web. Rather, there are millions of servers that host web pages that anyone can access (most of the time). Anyone can create a server and host whatever they want. As the web has evolved however, we see that this model is perhaps not as ideal as we might like; most of the servers that make up the web are controlled by a few server-providers such as Amazon, Google, and Microsoft. The servers of large corporations such as Facebook tend to function as content repositories for billions of people instead of each person controlling his or her identity on the web. As such, the network can be described with a long tail distribution: 

<center><img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Long_tail.svg" alt="Long Tail Distribution" style="width:500px;"/><br>
<sup>[Long Tail Distribution](https://upload.wikimedia.org/wikipedia/commons/8/8a/Long_tail.svg)</sup></center>

A few servers have the most traffic and the traffic of the remaining servers exponentially decreases and trails off to nil. 

What IPFS proposes to do is to create a distributed internet, where the actual distribution of content is done on a peer-to-peer basis. All of the nodes in the network host a nearly-equal amount of content. So why is this good? In both the centralized and decentralized case, a computer must download a file from a single server and deal with that servers busyness. With a distributed network, the computer can instead download content simultaneously from many of its peers. With video delivery for example, the P2P approach could save up to 60% in bandwidth costs [1].

#### The Web, Preserved

The second idea that makes IPFS different is that it has historic versioning built in. If you're familiar with git and the way each file has a history associated with it, then this concept should be right at home for you. If not, then imagine it this way: say you run a blog and one day you decide to add a new post to it. Both the way your blog was without the new post and the way it is now with the new post are saved within the network. So why is this a good thing? Take the case of Yahoo GeoCities. Back in the early 2000s Yahoo provided GeoCities as a place where people could set up small websites and publish content to them. However in 2009 Yahoo decided that GeoCities was no longer a profitable business for it and shut it down [2]. At the time there where about 38 million user-built pages on GeoCities [2]. Any content that was not preserved by the [Internet Archive](https://archive.org/web/geocities.php) was lost.

#### How It Works

When someone adds a file to the IPFS network, all of the blocks within the file are hashed. IPFS deduplicates files on entry so if any of the blocks are duplicates of some other block (as shown by comparing the hashes of the blocks), the duplicate block will not be re-added to the network. As mentioned, version history is tracked for every file so the blocks are given a version number (v1 in this example). The file is then distributed across the network to nodes that are "interested in it." This means that only nodes set to store a particular topic will store the file and its blocks. Indexing information is also stored with each node so that the network as a whole is aware of which node is storing what information. If a lookup is done on the file then the network is queried for nodes storing the content corresponding to the unique hash associated with the file. If you are more interested in how IPFS works, I recommending taking a look at the [IPFS whitepaper](https://github.com/ipfs/papers/raw/master/ipfs-cap2pfs/ipfs-p2p-file-system.pdf). 

#### Will it Work?

Technically, yes. The IPFS network is an actual thing that one can join and use now but it remains to be seen whether IPFS can gain widespread adoption. Currently, one of the major problems the network faces is that it is *slow* both for storing and querying content. This is partially due to the small size of the network, but also because of the overhead that comes from all of the necessary information, like the hashing of the files and their blocks, needed to support the network's functionality. Perhaps the largest problem is the deep entrenchment of the HTTP protocol. Nearly everything on the web uses HTTP for transporting content, and unless there is a clear and present need for a switch to a different architecture, IPFS may remain wishful thinking for a long while.


##### References

[1] : [ipfs.io](https://ipfs.io/)
[2] : [GeoCities](https://en.wikipedia.org/wiki/Yahoo!_GeoCities)