
# Port Attacker

**Port Attacker** is a work-in-progress (WIP) project designed to create an effective tool for network security testing through various port attack methods. The project aims to provide both a learning experience and a testing ground for experimenting with different techniques to challenge network defenses while considering advanced evasion strategies.

---

## Features

### Current Features
- **Basic Port Attacks** – The tool currently supports simple port-based attacks, such as:
  - TCP/UDP Flooding for resource exhaustion.
  - Scanning for open ports and service stability testing.
- **User-Friendly Menu** – A terminal-based menu interface for ease of use.

### Planned Improvements
- **Multiprocessing Support** – Enhancing attack efficiency by leveraging multiple processes.
- **Proxy Integration** – Allowing traffic to be routed through proxy servers to bypass firewall detection.
- **Advanced Attack Methods**:
  - Slowloris attack.
  - SYN Flooding.
  - DNS Amplification.
- **Evasion Techniques** – Implementing traffic masking and dynamic IP switching to circumvent network defenses.

---

## Project Structure

```
Port_Attacker/
├── modules/
│   ├── flooding.py    # Module for implementing flood-based attacks.
│   ├── main.py        # Main entry point for running the program.
│   ├── menu.py        # Menu interface for user interaction.
├── .gitignore         # Files/paths to be ignored by Git.
├── README.md          # Project documentation.
```

---

## Requirements
- **Python**: >=3.9
- **Libraries**:
  - `multiprocessing` (built-in)
  - `socket`
  - Future dependencies: `requests`, `scapy`

---

## Disclaimer
This project is intended for educational purposes and for testing the security of your own systems only. The author is not responsible for any misuse of this tool.

---