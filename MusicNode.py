class MusicNode:
  def __init__(self, songName, artistName):
    self.songName = songName
    self.artistName = artistName
    self.next = None
  def __init__(self, songName, artistName, albumName):
    self.songName = songName
    self.artistName = artistName
    self.albumName = albumName
    self.next = None