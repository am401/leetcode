### Unique Email Addresses
Link: https://leetcode.com/problems/unique-email-addresses/

### Problem
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

----

The solution feels a bit hacked together and there are certainly some improvements to be had for error handling and such however at this time the solution works. We are given a list of email addresses that may contain *locals*. Anything following a `+` in the *local*  will be ignored when you actually send emails. The same went for periods (`.`) within the local name, these would be ignored.

The challenge was that ignoring the periods and plus signs within the local, how many unique emails were being sent. This provided the challenge that really we were concentraing on the first half of an email address since the domain name will have periods in it. I experimented with a couple of versions but eventually found the best way to handle things is to remove the string between the `+` and the `@`. This would leave just periods within the *local*.

Once the `+` signs were removed, I split the email address up at the `@` and removed the periods from the *local*, ealving the domain intact. The email address was then put back together with the cleaned up *local* and the domain and added back to a list. This then allowed me to use `set()` to identify the number of unique email addresses and return the value as an integer.
