
import muspy
import numpy as np
from pathlib import Path
import os

def evaluate(data):
    """Evaluate the results."""

    # Trim the music
    music = data
    #music = data.trim(data.resolution * 32)

    # Save as a MusPy JSON file
    music.save("eval/json/result.json")

    if not music.tracks:
        return {
            "pitch_class_entropy": np.nan,
            "scale_consistency": np.nan,
            "groove_consistency": np.nan,
        }

    return {
        "pitch_class_entropy": muspy.pitch_class_entropy(music),
        "scale_consistency": muspy.scale_consistency(music),
        "groove_consistency": muspy.groove_consistency(
            music, 4 * music.resolution
        ),
    }


if __name__ == "__main__":

    result = []

    file_path = '/home/kinnryuu/ダウンロード/GCCE_Model/exp'
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            music_object = muspy.read_midi(file)
            result_one = evaluate(music_object)
            result.append(result_one)

    for key in result[0]:
        output = np.nanmean([r[key] for r in result])
        print(f"{key}:{output:.4f}")
    print()
