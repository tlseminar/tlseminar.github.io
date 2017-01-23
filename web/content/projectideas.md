# Project Ideas

This page collects some ideas for projects.  It is meant as a starting
point to help you think of things that might be interesting to do, not
to limit your possibilities.  Any topic that is related to TLS and the
ecosystem around TLS is within scope for your project.

## Deployment in Practice

- Why do the servers running critical sensitive services for UVA
  appear to be so insecure?  What are the impediments in practice to
  making services like
  [collab](https://www.ssllabs.com/ssltest/analyze.html?d=collab.virginia.edu&latest)
  and
  [sis](https://www.ssllabs.com/ssltest/analyze.html?d=sis.virginia.edu&latest)
  more secure? 

## Proxy-Protected Server

- What can't we provide a simple proxy service in front of a web
  server that implements a simple, secure TLS endpoint?  What are the
  latency and overhead costs of implementing a server this way?

## Configuration

- Make it possible to configure a web server to use different
  certificates with different key pairs for different protocols and
  connection types.  (Motivated most immediately by the DROWN attack.)

- Contribute to tools automating use of ACME (e.g., for Let's Encrypt
  certificates).

## Client UI

- Most of the security indicators used by a browser can be spoofed,
  and few users understand what parts of the current UI can be
  "trusted" (controlled by the web browser core) and what parts are
  untrusted (controlled by the web page).  Reconsider the web client
  UI in a way that provides a stronger and clearer boundary between
  trustworthy and site-controlled content.  [[The Line of
  Death](https://textslashplain.com/2017/01/14/the-line-of-death/)]

- Why not put the favicon for a site in its SSL certificate?  How hard
  would it be to extend the current infrastructure to support this,
  and to provide a browser client that displays trusted favicon
  images.
  
## Protecting Resources
- [Heartbleed](http://heartbleed.com/) shocked the Internet for a while mainly because it allowed for remote attackers to access data in the server's memory, most importantly the server's private key. Heartbleed was a realization of an important concept: attacking a service and stealing data from the server's memory. There are numerous practical examples of web-based services that can become vulnerable to this type of attack. Can we mitigate this risk by using tools at the programming language level? A combination of Rust's language guarantees and a memory protection system might be the answer! Checkout [Rustls](https://github.com/ctz/rustls) and [fidelius charm](https://github.com/halmohri/fc).  
