# Book Brain

A reading journal for keeping track of the books you've read:

![book_brain](https://user-images.githubusercontent.com/84557025/149754398-6dd0a2d0-8e29-4d69-b0db-81968c29f897.gif)

# Usage

BookBrain has all the features of a simple CRUD application.

You can update entries:

![edit_entry](https://user-images.githubusercontent.com/84557025/149754602-4e833b00-a935-47c0-882d-042edf3f85fa.gif)

Delete entries:

![delete](https://user-images.githubusercontent.com/84557025/149754582-a7af104e-1f24-4eee-b5b5-0c76fae131bc.gif)

And you don't just have to just add _read_ books - you can also specify if you're _currently_ reading a book:

![currently_reading](https://user-images.githubusercontent.com/84557025/149755872-9b689195-f17c-48c7-bfaf-ac349b1e82d0.gif)

## Installation

Clone the code to your virtual enviroment:

``` python
$ git clone https://github.com/ben-n93/BookBrain.git
```
Navigate into the BookBrain directory and install the required packages:

```python
$ cd BookBrain
$ pip3 install -r requirements.txt
```

Execute script:
```python
$ python3 book_brain.py
```

## Deleting user data

Book entries are saved into a JSON file ('user_data.json') in the data folder. If, for some reason, you need to wipe all the book entries (and you want to do so without manually deleting every row) you can simply delete this file (**_not_** the folder), as well as the 'IDs.json' file. The program will still work on restart.

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

## License

Distributed under the GPL-3.0 License. See LICENSE.txt for more information.

## Acknowledgement

I sourced the toolbar icons from [Google's Material Design](https://fonts.google.com/icons).

## Planned features
- [ ] Statistics on reading habits (e.g. pie chart of most read genres, average books read in a month, etc)
- [ ] Export book entries data as an Excel or PDF document
- [ ] UI refresh/update
- [ ] Delete all entries button
- [ ] Release of stand-alone executable
