# rcon_example_safe.py
import valve.rcon
import socket
import random
import string

ALPHABET = string.ascii_letters + "_"
while True:
# --- two helpers: fixed-length and random-length ----------------
    def random_string_fixed(length):
        """Return a random string of exactly `length` characters."""
        return ''.join(random.choices(ALPHABET, k=length))

    def random_string_range(min_len, max_len):
        """Return a random string whose length is chosen uniformly between min_len and max_len."""
        length = random.randint(min_len, max_len)   # fixed typo: randint
        return ''.join(random.choices(ALPHABET, k=length))

# Example usage (locally):
    fixed_pw = random_string_fixed(20)   # 20-char password
    random_pw = random_string_range(1, 20)

# --- rcon wrapper (use only with servers you own / have permission to access) ---
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
    # DO NOT use this to brute-force. Only run with a password you legitimately have.
        HOST = "169.150.249.133"   # change to the server you own for testing
        PORT = 22912
        RCON_PASSWORD = random_pw   # set to the password you own/control
        print(run_rcon_command(HOST, PORT, RCON_PASSWORD, "status"))
        print(RCON_PASSWORD)
