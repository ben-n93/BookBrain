# Book Brain

> A reading journal for keeping track of the books you've read.

<img width="752" alt="Screen Shot 2022-01-16 at 11 28 11 am" src="https://user-images.githubusercontent.com/84557025/149656277-8c7eaa63-6461-43ba-b7ec-3e259c0c2685.png">

## Installation

Clone the code to your virtual enviroment:

``` python
$ git clone https://github.com/ben-n93/BookBrain.git
```
Install the required packages:

```python
$ pip3 install -r requirements.txt
```

Navigate into the BookBrain directory and execute script:
```python
$ cd BookBrain
$ python3 book_brain.py
```

## Deleting user data

Book entries are saved into a JSON file ('user_data.json') in the data folder. If, for some reason, you need to wipe all the book entries you can simply delete this file (**_not_** the folder), as well as the 'IDs.json' file. The program will still work on restart.

You can delete all entries from the command line by issuing the following from the root directory of BookBrain:

### Mac:
```
$ cd data
$ rm IDS.json user_data.json
```
### Windows:
```
$ cd data
$ del IDS.json, user_data.json
```
## Planned features
- [ ] Statistics on reading habits (e.g. pie chart of most read genres, etc)
- [ ] Export data as an Excel or PDF document
- [ ] UI refresh/update
- [ ] Delete all entries
