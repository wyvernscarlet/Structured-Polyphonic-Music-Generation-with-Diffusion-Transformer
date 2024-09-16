import mido
import matplotlib.pyplot as plt
import numpy as np


def midi_to_roll(mid):
    notes = []
    for i, track in enumerate(mid.tracks):
        time = 0
        for msg in track:
            time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                notes.append((msg.note, time))
    return notes


def add_noise_to_notes(notes, noise_level=5):
    noisy_notes = []
    for note, time in notes:
        noisy_time = time + np.random.randint(-noise_level, noise_level)
        noisy_notes.append((note, noisy_time))
    return noisy_notes


def plot_piano_roll(notes, filename):
    if not notes:
        print("No notes to plot.")
        return
    fig, ax = plt.subplots()

    # Sort notes by time
    notes.sort(key=lambda x: x[1])

    xs = [note[1] for note in notes]
    ys = [note[0] for note in notes]

    ax.scatter(xs, ys, marker='|')
    ax.set_xlabel('Time')
    ax.set_ylabel('Note')
    plt.title('Piano Roll with Noise')

    # Save as image
    plt.savefig(filename)
    plt.close(fig)


# 读取MIDI文件
midi_file = '/home/kinnryuu/ダウンロード/GCCE_Model/exp/sdf_chd8bar[scale=0.0]_24-05-23_223145.mid'
mid = mido.MidiFile(midi_file)

# 转换音符信息
notes = midi_to_roll(mid)

# 添加随机噪声
notes_with_noise = add_noise_to_notes(notes, noise_level=5)

# 绘制带有噪声的钢琴卷帘图并保存为图片
output_image_file = 'piano_roll_with_noise.png'
plot_piano_roll(notes_with_noise, output_image_file)

print(f"Piano roll with noise has been saved as {output_image_file}")