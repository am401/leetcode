### leetcode.com challenge
Link: https://leetcode.com/problems/defanging-an-ip-address

#### Problem
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period `"."` with `"[.]"`.

----

An interesting [resource](https://www.ibm.com/support/knowledgecenter/en/SSBRUQ_32.0.0/com.ibm.resilient.doc/install/resilient_install_defangURLs.htm)  on defanging IP addresses / protocols.

----

Defanging an IP address can be an advantage to improve security when sending links online. The solutions I have created in this case use either `replace()` or a combination of `split()` and `join()`.
