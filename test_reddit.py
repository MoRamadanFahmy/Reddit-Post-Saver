import praw
import subprocess
import time
import pyautogui
import os


reddit = praw.Reddit(
    client_id="****",
    client_secret="****",
    user_agent="****"
)


subreddit = reddit.subreddit("learnmachinelearning")

r
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
save_dir = os.path.join(desktop, 'reddit-project')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)


for idx, post in enumerate(subreddit.hot(limit=5), start=1):
    title = post.title
    body = post.selftext

    if not body:
        body = "(No text content)"

    full_text = f"Title: {title}\n\n{body}"

    subprocess.Popen('notepad.exe')
    time.sleep(2)

    pyautogui.write(full_text, interval=0.02)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    file_path = os.path.join(save_dir, f'reddit_post_{idx}.txt')

    pyautogui.write(file_path)
    time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('left')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)

    print(f"✅ Saved reddit post {idx}")

print("\n✅ All reddit posts processed.")
