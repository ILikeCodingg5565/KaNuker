import asyncio
import random
import time
import multiprocessing
from pyfiglet import figlet_format
from colorama import init, Fore, Back, Style
from kahoot import KahootClient
from kahoot.packets.server.game_start import GameStartPacket
from kahoot.packets.server.game_over import GameOverPacket

init(autoreset=False)

logo = "KaNuker V1"
font = "big"
ascii_logo = figlet_format(logo, font)
print(Fore.MAGENTA + Back.BLACK + Style.DIM + "Slither presents")
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + ascii_logo)

print(Fore.GREEN + Back.BLACK + Style.BRIGHT)
print("Shut terminal = Bots leave\n\n")

class BasicKahootBot:
    def __init__(self, game_pin: int, name: str, queue: multiprocessing.Queue):
        self.client = KahootClient()
        self.game_pin = game_pin
        self.name = name
        self.queue = queue

    async def on_game_start(self, packet: GameStartPacket):
        print(f"[+] {self.name} joined.")
        self.queue.put(self.name)

    async def on_game_over(self, packet: GameOverPacket):
        print(f"[!] {self.name}: Game over.")

    async def run(self):
        self.client.on("game_start", self.on_game_start)
        self.client.on("game_over", self.on_game_over)
        await self.client.join_game(self.game_pin, self.name)

def launch_bot(game_pin: int, name: str, delay: float, queue: multiprocessing.Queue):
    if delay > 0:
        time.sleep(random.uniform(0, delay))
    asyncio.run(BasicKahootBot(game_pin, name, queue).run())

def spawn_bots(game_pin: int, base_name: str, num_bots: int, delay: float):
    queue = multiprocessing.Queue()
    processes = []

    for _ in range(num_bots):
        random_suffix = random.randint(1000, 9999)
        name = f"{base_name}_{random_suffix}"
        p = multiprocessing.Process(target=launch_bot, args=(game_pin, name, delay, queue))
        p.start()
        processes.append(p)

    joined = 0
    while joined < num_bots:
        bot_name = queue.get()
        joined += 1

    print(f"\n✅ Success! {joined} bots have joined the Kahoot game.\n")

if __name__ == "__main__":
    game_pin = int(input("Enter game PIN: "))
    base_name = input("What name should the bot be? ")
    num_bots = int(input("How many should join? "))
    try:
        delay = float(input("Max random delay (in seconds) between joins (0 for none): "))
    except ValueError:
        delay = 0

    spawn_bots(game_pin, base_name, num_bots, delay)

print(Style.RESET_ALL)
