import os
import subprocess

INPUT_FILE = "input.mp3"
TRACKS = [
    ('00:00:00', '00:02:15', 'SWZ - Black Star.mp3'),
    ('00:02:15', '00:04:23', 'SWZ - Dark Dreamer.mp3'),
    ('00:04:23', '00:06:27', 'SWZ - Core Breach.mp3'),
    ('00:06:27', '00:08:28', 'SWZ - Last Light.mp3'),
    ('00:08:28', '00:10:21', 'SWZ - Black Horizon.mp3'),
    ('00:10:21', '00:12:54', 'SWZ - Cosmic Grave.mp3'),
    ('00:12:54', '00:15:02', 'SWZ - Fading Pulsar.mp3'),
    ('00:15:02', '00:17:14', 'SWZ - Silent Explosion.mp3'),
    ('00:17:14', '00:19:03', 'SWZ - Stellar Ruin.mp3'),
    ('00:19:03', '00:21:10', 'SWZ - Red Star Wave.mp3'),
    ('00:21:10', '00:23:22', 'SWZ - Burning Blue.mp3'),
    ('00:23:22', '00:25:17', 'SWZ - Shattered Orbit.mp3'),
    ('00:25:17', '00:27:03', 'SWZ - Ash Horizon.mp3'),
    ('00:27:03', '00:28:46', 'SWZ - Sunset Burn.mp3'),
    ('00:28:46', '00:30:42', 'SWZ - Void Pulse.mp3'),
    ('00:30:42', '00:32:54', 'SWZ - Final Flare.mp3'),
    ('00:32:54', '00:34:42', 'SWZ - Burning Silence.mp3'),
    ('00:34:42', '00:36:44', 'SWZ - Collapse Sequence.mp3'),
    ('00:36:44', '00:38:36', 'SWZ - World Eater.mp3'),
    ('00:38:36', '00:40:28', 'SWZ - Radiation Dawn.mp3'),
    ('00:40:28', '00:42:07', 'SWZ - Fallen Sky.mp3'),
    ('00:42:07', '00:44:06', 'SWZ - Eternal Fallout.mp3'),
    ('00:44:06', '00:45:56', 'SWZ - Gravity Scar.mp3'),
    ('00:45:56', '00:47:52', 'SWZ - Ember Reign.mp3'),
    ('00:47:52', '00:50:13', 'SWZ - Oblivion Drift.mp3'),
    ('00:50:13', '00:52:49', 'SWZ - Supernova Wake.mp3'),
    ('00:52:49', '00:55:18', 'SWZ - Planetary Ash.mp3'),
    ('00:55:18', '00:57:45', 'SWZ - Darkened Code.mp3'),
    ('00:57:45', '00:59:59', 'SWZ - Star Fire.mp3')
]


def split_audio(input_path, tracks):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found!")
        return
    already = []
    for start_time, end_time, filename in tracks:
        print(f"Splite: ({start_time} -> {end_time})...")
        if filename in already:
            print(f"File '{filename}' already exists!")
            continue
        if filename in already:
            continue
        already.append(filename)

        command = [
            "ffmpeg",
            "-i",
            input_path,
            "-ss",
            start_time,
            "-to",
            end_time,
            "-c:a", "libmp3lame", "-b:a", "129k",
            filename,
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )

        if result.returncode == 0:
            print(f"Save: {filename}")
        else:
            print(f"Error {filename}:")
            print(result.stderr)
            break


if __name__ == "__main__":
    split_audio(INPUT_FILE, TRACKS)
