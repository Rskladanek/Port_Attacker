
# Port Attacker

**Port Attacker** is a work-in-progress (WIP) project designed to create an effective tool for network security testing through various port attack methods. The project aims to provide both a learning experience and a testing ground for experimenting with different techniques to challenge network defenses while considering advanced evasion strategies.

---

## Features

### Current Features
- **TCP SYN Flood**: Overload a target's network with SYN packets to exhaust resources.
- **HTTP GET Flood**: Send numerous HTTP GET requests to simulate a Distributed Denial of Service (DDoS) attack.
- **Slowloris Attack**: Keep many sockets open to exhaust a server's resources.
- **ICMP Flood**: Send a large number of ICMP Echo requests to a target.

### Planned Improvements
- **Multiprocessing Optimization**: Enhance attack efficiency using parallel processing.
- **Proxy Integration**: Support for routing traffic through proxies for anonymity and bypassing defenses.
- **Advanced Reporting**: Logs and analytics for attack results.
- **Customizable Attack Parameters**: Fine-tune attack strategies for specific targets.

---

## Project Structure

```
Port_Attacker/
├── modules/
│   ├── blitzsyn.py    # TCP SYN Flood implementation.
│   ├── webtsunami.py  # HTTP GET Flood implementation.
│   ├── crawlslow.py   # Slowloris attack module.
│   ├── pingstorm.py   # ICMP Flood implementation.
├── main.py            # Main entry point for the program.
├── menu.py            # Interactive menu interface.
├── README.md          # Project documentation.
├── requirements.txt   # List of required Python libraries.
```

---

## Requirements

- **Python**: >=3.9
- **Dependencies**: Install via `requirements.txt`
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Port_Attacker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Port_Attacker
   ```

3. Run the program:
   ```bash
   sudo python3 main.py
   ```

4. Follow the on-screen menu to choose an attack type.

---

## Fun Fact
The Slowloris attack, implemented here, was named after the slow loris, a small and slow-moving primate, symbolizing the deliberate and slow nature of the attack.

---

## Disclaimer

This project is for educational purposes only. Do not use it to target networks or systems you do not own or have explicit permission to test. Misuse of this tool may lead to severe legal consequences. Use responsibly.