# Python_1
-list 중복 제거 - set()
```python
def unique_names(names1, names2):
    a = list(set(names1 + names2))
    return a 

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
```

# Python_2
```python
def group_by_owners(files):
    f = files.values()
    s = set(f)
    newdict = {}
    fileowners = list(s)
    for owner in fileowners:
        l = []
        for file in files:
            if owner == files[file]:
                l.append(file)
            newdict[owner] = l  
    return newdict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
```

# Python and SQL_1
```python
def group_by_owners(files):
    values = files.values()
    s = set(values)
    li = list(s)
    newdict = {}
    for i in li:
        l = []
        for file in files:
            if i == files[file]:
                l.append(file)
            newdict[i] = l
    return newdict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
```

# Python and SQL_2
```python
def unique_names(names1, names2):
    a = list(set(names1 + names2))
    return a

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
```

# Python and SQL_3
```sql
update enrollments 
set year = 2015 
where id >= 20 and id <= 100;
```

# Python and SQL_4
```sql
select userID,avg(duration) as AverageDuration
from Sessions
group by UserID
limit 1;

select userID,avg(duration) as AverageDuration
from Sessions
group by UserID
having count(UserID) > 1;
```

# Python Algorithms 1
```python
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = {self}
        song = self.next
        while song:
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
```
# Python Algorithms 2
```python
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    taken = {}
    for i,num in enumerate(numbers):
        diff = target_sum - num
        if diff in taken:
            return i, taken[diff]
        taken[num] = i 
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
```    

# Python Algorithms and SQL 1
```python
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.value >= value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
```

# Python Algorithms and SQL 2
```python
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = {self}
        song = self.next
        while song:
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
```

# Python Algorithms and SQL 3
```sql
UPDATE enrollments
SET year = 2015
WHERE id between 20 and 100; 
```

# Python Algorithms and SQL 4
```sql
select userId, avg(duration)
from sessions
group by userID having count(userId) > 1;
```
