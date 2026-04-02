# 🖱️ Python Auto Clicker (High-Speed, Toggle-Based)

A fast and lightweight auto-clicker built in Python using `pynput`, designed for high performance and precise timing. Toggle clicking using the **SPACE bar**, and exit cleanly with **ESC**.

---

## 🚀 Features

* ⚡ High-speed clicking (100–200 CPS depending on system)
* 🎯 Precise timing using `time.perf_counter`
* 🔁 Toggle start/stop with **SPACE**
* 🛑 Exit anytime with **ESC**
* 🧠 Debounced key handling (no accidental double toggles)
* 🧵 Multi-threaded (non-blocking execution)
* 🖥️ Cross-platform (macOS, Windows, Linux)

---

## 📦 Installation

Install required dependencies:

```bash
pip install pynput
```

---

## ▶️ Usage

Run the script:

```bash
python clicker.py
```

Then:

* Enter desired **Clicks Per Second (CPS)**
* Press **SPACE** → Start/Stop clicking
* Press **ESC** → Exit program

---

## ⚠️ macOS Permissions (IMPORTANT)

If you're on macOS, you must enable permissions:

### 1. Go to:

**System Settings → Privacy & Security**

### 2. Enable:

* ✅ Accessibility
* ✅ Input Monitoring

### 3. Add:

* Terminal **OR**
* PyCharm **OR**
* Your Python binary (`.venv/bin/python`)

Without this, keyboard/mouse control will NOT work.

---

## 🧠 How It Works

* Uses `pynput.mouse.Controller` for faster clicking than `pyautogui`
* Uses a **precision loop** with `perf_counter()` to maintain consistent CPS
* Runs clicking in a **daemon thread**
* Uses a **debounce mechanism** to prevent multiple toggles from one key press

---

## 📈 Performance Notes

| Method        | Speed        |
| ------------- | ------------ |
| pyautogui     | ~20–50 CPS   |
| pynput (this) | ~100–200 CPS |

> Actual performance depends on your OS and hardware.

---

## ⚙️ Customization Ideas

* 🎲 Randomized CPS (human-like clicking)
* 🖱️ Right-click or middle-click support
* 🎯 Click at fixed screen coordinates
* 🪟 Target specific application window
* 🎛️ GUI (Tkinter / PyQt slider)

---

## ⚠️ Disclaimer

This tool is intended for:

* Automation
* Testing
* Personal productivity

Do **not** use in ways that violate terms of service of games or applications.

---

## 🧑‍💻 Author

Built with focus on performance, simplicity, and clean architecture.
