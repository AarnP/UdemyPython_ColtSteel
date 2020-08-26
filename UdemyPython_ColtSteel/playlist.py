playlist = dict(
    title="Heaven on Earth",
    author="Aaron Phan",
    songs=[
        dict(title="damnation", artist=["blue"], duration=3.5),
        dict(title="rose", artist=["dragon, DJ Kunt"], duration=2.5),
        dict(title="guns", artist=["blue"], duration=4.5),
    ]
)

total_length = 0
for song in playlist['songs']:
    total_length += song["duration"]
print(total_length)
