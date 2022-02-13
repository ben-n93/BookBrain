# Book Brain

A reading journal for keeping track of the books you've read:

<img width="774" alt="Screen Shot 2022-02-13 at 6 47 29 pm" src="https://user-images.githubusercontent.com/84557025/153744069-d32cd624-a6f6-4ca4-aa96-fb79ad917345.png">

# Usage

BookBrain has all the features of a simple CRUD application.

Adding a book:



Updating an entry:


Delete entries:

And you don't just have to just add _read_ books - you can add books you're currently reading:

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
