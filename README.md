
# AutoClick

A simple Python auto clicker script that automatically clicks at a specified screen position. This tool is useful for automating repetitive mouse clicks on a target location.

---

## Features

- Move the mouse cursor to a target coordinate  
- Perform multiple automated mouse clicks with configurable intervals  
- Supports left, right, and middle mouse buttons  
- Easy to customize and extend  

---

## Requirements

- Python 3.6+  
- [`pyautogui`](https://pyautogui.readthedocs.io/en/latest/) library for mouse control  

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pook1337/AutoClick.git
   cd AutoClick
   ```

2. Install the required Python package:

   ```
   pip install pyautogui
   ```

---

## Usage

Edit the `ac.py` script to set your desired target position, number of clicks, click interval, and mouse button.

Example usage inside `ac.py`:

```
target_position = (500, 300)  # X, Y coordinates on the screen
number_of_clicks = 20
delay_between_clicks = 0.2  # seconds
button = 'left'  # 'left', 'right', or 'middle'
```

Run the script:

```
python ac.py
```

The script will move the mouse to the target position and perform the specified number of clicks with the given delay.

---

## How it works

- Uses `pyautogui.moveTo()` to position the mouse cursor.  
- Uses `pyautogui.click()` to perform mouse clicks.  
- Loops through the clicking process with a delay between clicks.

---

## Notes

- Make sure to run the script in an environment where mouse control is allowed.  
- Use responsibly and avoid violating terms of service of any software or platform.  
- You can extend this script to add features like image recognition, hotkeys to start/stop, or randomize click intervals.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

