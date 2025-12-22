*This project has been created as part of the 42 curriculum by nel-ouad.*

# Born2BeRoot

## Description
Born2BeRoot is a system administration project focused on introducing virtualization and Linux server configuration.  
The objective is to create and secure a virtual machine by following strict rules related to partitioning, user management, security policies, services, and system monitoring.

The project aims to provide a solid foundation in server administration and security best practices.

---

## Project Description

### Choice of Operating System

For this project, **Debian** was chosen as the operating system.

**Debian – Pros:**
- Very stable and reliable
- Large community and extensive documentation
- Lightweight and well suited for servers
- Uses AppArmor by default, which is easier to understand and configure

**Debian – Cons:**
- Software versions may not be the most recent
- Less enterprise-oriented compared to Rocky Linux

**Rocky Linux – Comparison:**
- Enterprise-focused and binary compatible with Red Hat
- Uses SELinux, which is more powerful but more complex
- Harder to configure for beginners

Debian was chosen because it is **stable, beginner-friendly, and recommended for learning system administration**.

---

### Main Design Choices

**Partitioning**
- Logical Volume Manager (LVM) was used
- Encrypted partitions were created
- LVM allows flexible disk management and resizing

**Security Policies**
- Strong password policy enforced
- Password expiration and complexity rules applied
- SSH configured on a non-default port
- Root login via SSH disabled
- Firewall enabled and restricted to required ports only

**User Management**
- A main user `nel-ouad` was created
- User added to `sudo` and `user42` groups
- Root access restricted and controlled via sudo

**Services Installed**
- OpenSSH for remote access
- UFW for firewall management
- sudo for privilege escalation
- No graphical interface or unnecessary services installed

---

### Comparisons

#### Debian vs Rocky Linux
- Debian: stable, community-driven, beginner-friendly
- Rocky Linux: enterprise-oriented, SELinux-based, more complex
- Debian was chosen for simplicity and learning purposes

#### AppArmor vs SELinux
- AppArmor: profile-based, easier to configure, Debian default
- SELinux: label-based, more powerful, more complex
- AppArmor was chosen for clarity and ease of use

#### UFW vs firewalld
- UFW: simple and user-friendly, used on Debian
- firewalld: more advanced and dynamic, used on Rocky Linux
- UFW was chosen for simplicity

#### VirtualBox vs UTM
- VirtualBox: widely used, cross-platform, well documented
- UTM: mainly used on Apple Silicon (M1/M2)
- VirtualBox was chosen for compatibility and availability

---

## Environment
- Operating System: Debian
- Virtualization: VirtualBox
- Login user: `nel-ouad`
- Bonus part: ❌ Not implemented

---

## Instructions
The virtual machine starts normally after boot.  
A monitoring script displays system information periodically using `wall`.  
No manual execution is required.

---

## Resources
- https://noreply.gitbook.io/born2beroot  
- Google  
- ChatGPT (used for explanations and understanding concepts, not for direct answers)

---

## Notes
The bonus part of the project was not implemented.  
All mandatory requirements of the Born2BeRoot subject were completed.
