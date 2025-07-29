
liked_songs = {
  'Roots': 'Bintu Pabra',
  'Bapu':'Khasa Aala Chahar',
  'Manifest':'Filmy'
}


def display_songs(liked_songs, filename='liked_songs.txt'):
    with open('liked_songs.txt', 'w') as file:
      file.write('Liked songs:\n')
      for key,values in liked_songs.items():
        file.write(f"{key} by {values}\n")
           

display_songs(liked_songs)
with open('liked_songs.txt','r') as file1:
  content = file1.read()
  print(content)