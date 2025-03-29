from MusicNode import MusicNode

class MusicList:
  def __init__(self):
    self.head = None
    self.tail = None
  def pushFront(self, songName, artistName, albumName):
    if self.head == None:
      newNode = MusicNode(songName, artistName, albumName)
      self.head = newNode
      newNode.Print()
    else:
      
