import os
import subprocess

tracks: list[list[str]] = []

with open(r"time_points.txt", 'r') as tp:
    while True:
        track: list[str] = tp.readline().strip().split(';')
        if track != ['']:
            if track[2][:-1] == '\n':
                track[2] = track[2][:-1]
            tracks.append(track)
        else:
            break


def split_audio(input_path, tracks) -> str:

    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found!")
        return

    with open("already.txt", 'r') as ar:
        already: list[str] = ar.readlines()

    for start_time, end_time, filename in tracks:

        print(f"{start_time} - {end_time} Splite...")

        if filename+'\n' in already:
            print(f"{filename} already save")
            continue
        else:
            with open("already.txt", 'a') as ar:
                ar.write(filename+'\n')

        result: subprocess.CompletedProcess = subprocess.run(
            [
                "ffmpeg", "-i", input_path,
                "-ss", start_time, "-to", end_time,
                "-c:a", "libmp3lame", "-b:a", "129k",
                f"./Tracks/{filename}"
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )

        if result.returncode == 0:
            print(f"Save:      {filename}")
        else:
            print(f"Error {filename}: {result.stderr}")
            break


if __name__ == "__main__":
    split_audio("input.mp3", tracks)
