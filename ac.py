import pyautogui
import time

def auto_click(target_x, target_y, clicks=10, interval=0.1, button='left'):
    """
    Automatically click at (target_x, target_y) on the screen.

    :param target_x: X coordinate of the target position
    :param target_y: Y coordinate of the target position
    :param clicks: Number of clicks to perform
    :param interval: Time interval between clicks in seconds
    :param button: Mouse button to click ('left', 'right', 'middle')
    """
    # Move the mouse to the target position
    pyautogui.moveTo(target_x, target_y)
    
    # Perform the clicks
    for _ in range(clicks):
        pyautogui.click(button=button)
        time.sleep(interval)

if __name__ == "__main__":
    # Example target coordinates (change to your desired position)
    target_position = (500, 300)
    
    # Number of clicks and interval between clicks
    number_of_clicks = 20
    delay_between_clicks = 0.2  # seconds
    
    print(f"Starting auto clicker at position {target_position}...")
    auto_click(target_position[0], target_position[1], clicks=number_of_clicks, interval=delay_between_clicks)
    print("Done clicking.")
