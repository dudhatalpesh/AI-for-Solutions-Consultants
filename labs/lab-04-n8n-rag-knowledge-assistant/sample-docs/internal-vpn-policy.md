# VPN and Remote Access Policy (internal)

*Synthetic demo content.*

## Scope
Applies to all employees and contractors accessing Northwind systems remotely.

## Requirements
1. Remote access to internal applications must use the Northwind VPN or the zero trust access portal.
2. Multi-factor authentication (MFA) is mandatory for every VPN session.
3. VPN sessions disconnect automatically after 12 hours, or after 30 minutes of inactivity.
4. Split tunnelling is disabled on corporate laptops.

## Logging and retention
VPN connection logs (user, device, source IP, timestamps) are retained for 90 days and then deleted. Security may extend retention for an active investigation.

## Exceptions
Exceptions require approval from the CISO office and are reviewed every 6 months.
