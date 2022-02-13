# BookBrain

A reading journal for keeping track of the books you've read:

<img width="779" alt="Screen Shot 2022-02-13 at 6 51 40 pm" src="https://user-images.githubusercontent.com/84557025/153744184-ddda6893-ae9a-4080-b93d-05c0c1c3ce96.png">

# Usage

BookBrain has all the features of a simple CRUD application.

Adding a book:

![add_book](https://user-images.githubusercontent.com/84557025/153744325-2a4c501d-2c65-4fa9-a1f4-ee05d477775b.gif)

Updating an entry:

![update_book](https://user-images.githubusercontent.com/84557025/153744380-027b3085-3444-4b0e-b32e-af59c33a85d8.gif)

Deleting an entry:

![delete_entry](https://user-images.githubusercontent.com/84557025/153744386-1356fe12-ce26-4d5b-9edf-8666005ecf8a.gif)

And you don't just have to just add _read_ books - you can add books you're currently reading:

![currently_reading](https://user-images.githubusercontent.com/84557025/153744393-1e0abe51-0695-4e87-9e73-b1f1b6e8f398.gif)

You can also filter by book title, author or genre:

![filter](https://user-images.githubusercontent.com/84557025/153744446-8fcf2f0a-f9ed-4d58-9a7a-c757d3906205.gif)

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

Style sheet: https://github.com/ColinDuquesnoy/QDarkStyleSheet

## Planned features
- [ ] Statistics on reading habits (e.g. pie chart of most read genres, average books read in a month, etc)
- [ ] Export book entries data as an Excel or PDF document
- [ ] UI refresh/update
- [ ] Release of stand-alone executable
