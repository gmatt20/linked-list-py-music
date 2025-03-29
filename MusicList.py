from MusicNode import MusicNode

class MusicList:
  def __init__(self):
    self.head = None
    self.tail = None

  def pushFront(self, songName, artistName, albumName):
    newNode = MusicNode(songName, artistName, albumName)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode

  def pushBack(self, songName, artistName, albumName):
    newNode = MusicNode(songName, artistName, albumName)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def PrintList(self):
      currNode = self.head
      while currNode != None:
        print(currNode.songName + " " + currNode.artistName + " " + currNode.albumName + " -> ")
        currNode = currNode.next

