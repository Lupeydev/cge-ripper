import valve.rcon
import socket
import random
import string

ALPHABET = string.ascii_letters + "_"
while True:
    def random_string_fixed(length):
        """Return a random string of exactly `length` characters."""
        return ''.join(random.choices(ALPHABET, k=length))

    def random_string_range(min_len, max_len):
        length = random.randint(min_len, max_len)  
        return ''.join(random.choices(ALPHABET, k=length))

    fixed_pw = random_string_fixed(20) 
    random_pw = random_string_range(1, 20)

    def run_rcon_command(host, port, password, command, timeout=5.0):
        try:
            with valve.rcon.RCON((host, port), password, timeout=timeout) as rcon:
                resp = rcon.execute(command)
                return resp
        except valve.rcon.RCONAuthenticationError:
            return "RCON authentication failed — check your password and permissions."
        except (socket.timeout, ConnectionRefusedError, OSError) as e:
            return f"Connection error — server not reachable or RCON not enabled: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

    if __name__ == "__main__":
        HOST = "169.150.249.133"  
        PORT = 22912
        RCON_PASSWORD = random_pw  
        print(run_rcon_command(HOST, PORT, RCON_PASSWORD, "status"))
        print(RCON_PASSWORD)
