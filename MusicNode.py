class MusicNode:
  def __init__(self, songName, artistName, albumName):
    self.songName = songName
    self.artistName = artistName
    self.albumName = albumName
    self.next = None
  def Print(self):
    print("Song: ", self.songName)
    print("Artist: ", self.artistName)
    print("Album: ", self.albumName)