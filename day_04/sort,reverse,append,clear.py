playlist = ["Yesterday", "Blinding Lights", "Starboy", "Bohemian Rhapsody", "Hello"]
playlist.sort()
print(playlist)
playlist.reverse()
print(playlist)

playlist_backup = playlist.copy
playlist.append("believer")
print(playlist_backup)

playlist.clear()
print(playlist)