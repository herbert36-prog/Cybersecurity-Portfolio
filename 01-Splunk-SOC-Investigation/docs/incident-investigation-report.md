# Incident Investigation Report

## Incident Title
Potential Brute-Force Login Activity

## Investigation Overview

This investigation used Splunk Cloud Platform to analyse synthetic authentication logs and identify potentially suspicious login activity.

The objective was to identify repeated failed login attempts, investigate the source IP addresses involved, identify targeted accounts and analyse the activity over time.

## Tools Used

- Splunk Cloud Platform
- Search Processing Language (SPL)
- Synthetic CSV authentication logs

## Investigation Findings

### Authentication Activity

A total of 25 authentication events were analysed.

- Total events: 25
- Failed login attempts: 18
- Successful login attempts: 7

### Suspicious Source IP

The investigation identified `203.0.113.45` as the main source of suspicious activity.

This address was responsible for 16 failed login attempts, representing approximately 88.9% of all failed attempts.

### Targeted User Accounts

The suspicious IP attempted to access four different usernames:

| Username | Failed attempts |
|---|---:|
| admin | 8 |
| administrator | 3 |
| root | 3 |
| guest | 2 |

The targeting of multiple account names, including privileged account names, was consistent with potential automated password guessing.

### Timeline Analysis

The failed login attempts occurred in several bursts:

| Time | Failed attempts |
|---|---:|
| 09:05 | 5 |
| 09:06 | 3 |
| 09:10 | 3 |
| 09:13 | 3 |
| 09:20 | 2 |

This pattern provided further evidence of repeated suspicious authentication activity.

## Assessment

The activity was assessed as suspicious and consistent with a potential brute-force or password-guessing attempt.

However, the available synthetic logs do not establish whether any account was successfully compromised.

Further investigation would be required to determine whether any unauthorised access occurred.

## Recommended Actions

If this activity occurred in a real organisation, the following actions would be recommended:

1. Investigate the source IP and establish whether it is associated with legitimate activity.
2. Review successful authentication events involving the targeted accounts.
3. Check for unusual activity following the failed login attempts.
4. Apply appropriate account lockout and rate-limiting controls.
5. Review privileged account security and enforce multi-factor authentication.
6. Escalate the investigation if evidence of unauthorised access is discovered.

## Conclusion

This project demonstrated how Splunk Cloud can be used to search and analyse authentication logs, identify suspicious IP addresses, investigate targeted usernames and examine login activity over time.

The investigation provided practical experience with SIEM monitoring, SPL queries and SOC-style incident documentation.

## Disclaimer

This investigation used synthetic authentication data for educational purposes. No real attack or unauthorised access took place.
