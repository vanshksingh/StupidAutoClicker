import time
import threading
from pynput import keyboard
from pynput.mouse import Controller, Button


class AutoClicker:
    def __init__(self, cps=10):
        self.cps = cps
        self.delay = 1.0 / cps
        self.running = False
        self.thread = None
        self.mouse = Controller()

    def click_loop(self):
        next_time = time.perf_counter()

        while self.running:
            self.mouse.click(Button.left, 1)

            next_time += self.delay
            sleep_time = next_time - time.perf_counter()

            if sleep_time > 0:
                time.sleep(sleep_time)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.click_loop, daemon=True)
            self.thread.start()
            print("[INFO] Started")

    def stop(self):
        if self.running:
            self.running = False
            print("[INFO] Stopped")

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()


class KeyHandler:
    def __init__(self, clicker):
        self.clicker = clicker
        self.space_pressed = False  # debounce flag

    def on_press(self, key):
        if key == keyboard.Key.space and not self.space_pressed:
            self.space_pressed = True
            self.clicker.toggle()

    def on_release(self, key):
        if key == keyboard.Key.space:
            self.space_pressed = False

        if key == keyboard.Key.esc:
            print("[INFO] Exiting...")
            return False


def listen_keyboard(clicker):
    handler = KeyHandler(clicker)

    with keyboard.Listener(
        on_press=handler.on_press,
        on_release=handler.on_release
    ) as listener:
        listener.join()


def main():
    cps = int(input("Enter CPS: "))
    clicker = AutoClicker(cps)

    print("SPACE → toggle | ESC → exit")

    listen_keyboard(clicker)


if __name__ == "__main__":
    main()
