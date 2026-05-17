# Advanced Database Models Exercise 4

Author: Suvansh Shukla
Immatriculation Number: 256245

## Question 1 Conceptual Design

### Q1 (a)

![ER diagram](./ER-ADBM-Ex-4.png)

### Q1 (b)

![ER Model with Object Oriented Extensions](./ERD-Ex-4-Q1-B.png)

### Q1 (c)

![UML diagram](./ADMB-EX-4-Q1-C-UML.png)

## Question 2 Conceptual Design to Logical Design

### Q2 (a)

```RM
artist(ID, name, influenced_by, influences)
singer(s_id, artist_id, sex)
song_writer(sw_id, artist_id, genre)
singer_song_writer(s_id, sw_id)
songs(id, title, duration, s_id, sw_id)
```

### Q2 (b)

```java
import java.util.List;
import java.util.Set;

// Base Class
class Artist {
    private int id;
    private String name;
    
    // Unary/Recursive relationship: An artist can be influenced by many artists, 
    // and can influence many artists.
    private Set<Artist> influencedBy;
    private Set<Artist> influences; 
}

// Subclass of Artist
class Singer extends Artist {
    private String sex;
    
    // M:N Relationship represented via the association class/object "Song"
    private List<Song> performedSongs;
}

// Subclass of Artist
class SongWriter extends Artist {
    private String genre;
    
    // M:N Relationship represented via the association class/object "Song"
    private List<Song> writtenSongs;
}

class SingerSongWriter extends Artist {
    private String sex;
    private String genre;
}

// Association Class for the "performs songs" relationship
class Song {
    private int id;
    private String title;
    private double duration;
    
    // Links back to the entities involved in the relationship
    private Singer singer;
    private SongWriter songWriter;
}
```
