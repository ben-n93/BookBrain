# BookBrain

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, Qt, QObject

from datetime import date, datetime
from copy import deepcopy
import json

# List of generated IDs
entry_ids = list(range(1,10_001))

entries = {}

# JSON filenames.
entries_file = 'data/user_data.json'
ids_file = 'data/IDs.json'

genres = ['Biography', 'Comic', 'Crime', 'Detective', 'Fantasy',
'Graphic novel', 'Historical fiction', 'History', 'Horror',
'Literary fiction', 'Magic realism', 'Memoir', 'Mystery', 'Poetry', 'Romance',
'Science fiction', 'Self-help', 'Short stories', 'Thriller', 'True crime',
'Western']


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BookBrain')
        self.setMinimumHeight(450)
        self.setMinimumWidth(640)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        # Headers for QTableWidget
        self.header_one = QtWidgets.QTableWidgetItem('ID:')
        self.header_two = QtWidgets.QTableWidgetItem('Date started:')
        self.header_three = QtWidgets.QTableWidgetItem('Date finished:')
        self.header_four = QtWidgets.QTableWidgetItem('Book title:')
        self.header_five = QtWidgets.QTableWidgetItem('Author:')
        self.header_six = QtWidgets.QTableWidgetItem('Genre:')
        self.header_seven = QtWidgets.QTableWidgetItem('Comments:')
        # Table widget
        self.table = QtWidgets.QTableWidget(1, 7)
        # Sets headers.
        self.table.setHorizontalHeaderItem(0, self.header_one)
        self.table.setHorizontalHeaderItem(1, self.header_two)
        self.table.setHorizontalHeaderItem(2, self.header_three)
        self.table.setHorizontalHeaderItem(3, self.header_four)
        self.table.setHorizontalHeaderItem(4, self.header_five)
        self.table.setHorizontalHeaderItem(5, self.header_six)
        self.table.setHorizontalHeaderItem(6, self.header_seven)
        # Makes table uneditable.
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # When user clicks on cell, entire row selected.
        self.table.setSelectionBehavior(self.table.SelectRows)
        # Hides IDs column.
        self.table.setColumnHidden(0, True)
        # Entries buttons.
        self.add_book_button = QtWidgets.QPushButton('Add entry')
        self.edit_book_button = QtWidgets.QPushButton('Update entry')
        self.delete_book_button = QtWidgets.QPushButton('Delete entry')
        # Adds widgets to main window grid layout.
        self.layout.addWidget(self.table, 0, 0, 1, 0)
        self.layout.addWidget(self.add_book_button, 1, 0)
        self.layout.addWidget(self.edit_book_button, 1, 1)
        self.layout.addWidget(self.delete_book_button, 1, 2)
        # Sets default sorting to asending order of date finished.
        self.table.sortByColumn(2, Qt.AscendingOrder)
        # Sets column width of 'date finished column'. Needed to set because
        # values too small (due to date formatting default) to show column
        # header ('Date finished:') in full.
        self.table.setColumnWidth(2, 100)
        # Signals/slots.
        self.add_book_button.clicked.connect(self.show_input_window)
        self.delete_book_button.clicked.connect(self.delete_entry)
        self.edit_book_button.clicked.connect(self.show_edit_window)

        self.add_book_button.setFlat(True)


    def table_population(self):
        # Disabled table sorting, so as not to mess with table items order.
        self.table.setSortingEnabled(False)
        entries_row_count = 0
        for key in entries.keys():
            entries_row_count += 1
        self.table.setRowCount(entries_row_count)
        # Creates empty list.
        temp_list = []
        fields_list = ['ID', 'date_started', 'date_finished', 'book_title',
        'author_title', 'genre', 'comments']

        column_count = 0

        for field in fields_list:
            starting_row = 0
            temp_list = []
            for entry_dictionary in entries.values():
                temp_list.append(entry_dictionary[field])
            for item in temp_list:
                temp_item = QtWidgets.QTableWidgetItem(item)
                if column_count == 1 or column_count == 2:
                    # If column count equals 1 or 2, then it's either the date
                    # started or date ended column, in which case the value
                    # needs to be changed to a date so the columns can be
                    # sorted properly.
                    temp_item_text = temp_item.text()
                    # Attemps to changed value to date. If it fails, it's
                    # because the dictionary date value is empty, due to
                    # currently reading checkbox being toggled and empty string
                    # being added to dictionary.
                    try:
                        temp_date_item = datetime.strptime(temp_item_text,
                            "%d %b %Y")
                        temp_item.setData(0, QDate(temp_date_item))
                        # Centres date value horizontally and vertically.
                        temp_item.setTextAlignment(Qt.AlignVCenter |
                            Qt.AlignHCenter)
                    except ValueError:
                        pass
                self.table.setItem(starting_row, column_count, temp_item)
                starting_row += 1
            column_count += 1

        if len(entries) == 0:
            pass
        else:
            # Resizes all columns to fit contents, except for date finished and
            # Comments column.
            self.table.resizeColumnToContents(1)
            self.table.resizeColumnToContents(3)
            self.table.resizeColumnToContents(4)
            self.table.resizeColumnToContents(5)

        self.table.setSortingEnabled(True)


    def show_input_window(self):
        """ Displays the input window """
        input_window = InputWindow('add')
        input_window.exec()


    def show_edit_window(self):
        """Shows edit (input) window, if an entry/row is selected."""
        try:
            # Finds current row of user's current selection.
            self.current_row = self.table.currentRow()

            # Finds item (ID string) in ID column of current row.
            self.current_row_id = self.table.item(self.current_row, 0)

            # Finds ID of selected row/entry.
            self.current_row_id = self.current_row_id.text()

            input_window = InputWindow('edit', self.current_row_id)
            input_window.exec()

        except AttributeError:
            pass


    def delete_entry(self):
        """ Deletes book entry/dictionary from main window table and rewrites
        JSON file with revised entries dictionary"""

        # Checks to ensure there is actually an entry present to be deleted.
        if self.table.currentRow() < 0:
            pass
        else:
            self.delete_alert = QtWidgets.QMessageBox()
            self.delete_alert.setStandardButtons(QtWidgets.QMessageBox.Yes |
                                        QtWidgets.QMessageBox.Cancel)
            self.delete_alert.setIcon(QtWidgets.QMessageBox.Question)
            self.delete_alert.setText("Are you sure you want to delete this entry?")
            returnValue = self.delete_alert.exec()

            if returnValue == QtWidgets.QMessageBox.Yes:
                # Finds current row of current selection.
                self.current_row = self.table.currentRow()
                # Finds item in ID column of current row
                self.id_to_delete = self.table.item(self.current_row, 0)
                try:
                    # Finds ID of selected row/entry
                    self.id_to_delete = self.id_to_delete.text()

                    # Deletes entry that matches row ID.
                    del entries[self.id_to_delete]
                    # Converts ID to integer so it can be be readded to IDs list.
                    self.id_to_delete = int(self.id_to_delete)

                    # Adds deleted ID to IDs list, to be reused again.
                    entry_ids.insert(0, self.id_to_delete)

                    # Saves new entries file to JSON file.
                    with open(entries_file, 'w') as f:
                        json.dump(entries, f)

                    # Saves new entries file to JSON file.
                    with open(ids_file, 'w') as f:
                        json.dump(entry_ids, f)

                    # Removes currently selected entry from table.
                    self.table.removeRow(self.current_row)

                except AttributeError:
                    pass


class InputWindow(QtWidgets.QDialog):
    """ Input window for adding/editing book entries """
    def __init__(self, window_type, current_row_id=None):
        super().__init__()
        self.window_type = window_type
        self.current_row_id = current_row_id
        self.layout = QtWidgets.QFormLayout()
        # Sets input window layout
        self.setLayout(self.layout)
        # Sets input window title
        # QLineLabels
        self.book_label = QtWidgets.QLabel('Book title:')
        self.author_label = QtWidgets.QLabel('Author:')
        self.genre_label = QtWidgets.QLabel('Genre:')
        self.date_started_label = QtWidgets.QLabel('Date started:')
        self.date_finished_label = QtWidgets.QLabel('Date finished:')
        self.comments_label = QtWidgets.QLabel('Comments:')
        self.currently_reading_label = QtWidgets.QLabel('Currently reading:')
        self.want_to_read_label = QtWidgets.QLabel('Want to read:')
        # QCheckbox
        self.currently_reading_check_box = QtWidgets.QCheckBox('')
        self.want_to_read_check_box = QtWidgets.QCheckBox('')
        # QLineEdits
        self.book_line_edit = QtWidgets.QLineEdit()
        self.author_line_edit = QtWidgets.QLineEdit()
        # QComboBox
        self.genre_combo_box = QtWidgets.QComboBox()
        self.genre_combo_box.addItems(genres)
        # QPlainTextEdit
        self.comments_text_box = QtWidgets.QPlainTextEdit()
        self.confirm_button = QtWidgets.QPushButton('Confirm')
        # Date fields.
        self.today_date = date.today()
        self.date_object = QDate(self.today_date)
        # Finds current year, in order to set default Date started date as
        # start of year.
        self.current_year = self.today_date.year
        self.temp_current_year = QDate(self.current_year, 1, 1)
        # QDateEdit
        self.date_started_date_edit = QtWidgets.QDateEdit()
        self.date_finished_date_edit = QtWidgets.QDateEdit()
        self.date_finished_date_edit.setDate(self.date_object)
        self.date_started_date_edit.setDate(self.temp_current_year)
        # Enables calendar popup when selecting QDateEdits
        self.date_started_date_edit.setCalendarPopup(True)
        self.date_finished_date_edit.setCalendarPopup(True)
        # Sets date display format
        self.date_started_date_edit.setDisplayFormat('d MMMM yyyy')
        self.date_finished_date_edit.setDisplayFormat('d MMMM yyyy')

        self.test_min_date = QDate(2021,12,12)
        self.date_finished_date_edit.setMinimumDate(self.test_min_date)

        # Checks to see if editing existing entry.
        if self.window_type == 'edit':
            self.setWindowTitle('Edit entry')
            # Creates a copy of selected row's entry dictionary. It finds this
            # by matching the row's ID to key in entries dictionary.
            self.temp_edit_dictionary = deepcopy(entries[self.current_row_id])
            # Converts start dates' values to QDates, in order to set
            # entry window.
            self.temp_date_started = self.temp_edit_dictionary['date_started']
            self.temp_date_started = datetime.strptime(
                self.temp_date_started, "%d %b %Y")
            # Attempts to convert finished date value to QDate, in order to set
            # entry window. If it fails, it's because end date doesn't exist/
            # currently reading checkbox is toggled.
            try:
                self.temp_date_finished = \
                self.temp_edit_dictionary['date_finished']
                self.temp_date_finished = datetime.strptime(
                    self.temp_date_finished, "%d %b %Y")
                self.date_finished_date_edit.setDate(self.temp_date_finished)
            except ValueError:
                self.currently_reading_check_box.setChecked(True)

            # Sets (edit entry) input window fields with dictionary values.
            self.date_started_date_edit.setDate(self.temp_date_started)
            self.book_line_edit.setText(
                self.temp_edit_dictionary['book_title'])
            self.author_line_edit.setText(
                self.temp_edit_dictionary['author_title'])
            self.genre_combo_box.setCurrentText(
                self.temp_edit_dictionary['genre'])
            self.comments_text_box.setPlainText(
                self.temp_edit_dictionary['comments'])

            self.ID = self.temp_edit_dictionary['ID']

        else:
            self.setWindowTitle('Add entry')
            self.ID = ''

        # Adds labels and QWidgets to input window
        self.layout.addRow(self.book_label, self.book_line_edit)
        self.layout.addRow(self.author_label, self.author_line_edit)
        self.layout.addRow(self.genre_label, self.genre_combo_box)
        self.layout.addRow(self.currently_reading_label,
            self.currently_reading_check_box)
        self.layout.addRow(self.date_started_label,
            self.date_started_date_edit)
        # Because check box will be ticked if user is currently reading book,
        # the date finished field will not be added unless unchecked.
        if self.currently_reading_check_box.isChecked():
            pass
        else:
            self.layout.addRow(self.date_finished_label,
                self.date_finished_date_edit)
        self.layout.addRow(self.comments_label, self.comments_text_box)
        self.layout.addRow(self.confirm_button)

        # Signal/slots.
        self.date_started_date_edit.dateChanged.connect(self.date_change)
        self.date_finished_date_edit.dateChanged.connect(self.date_change)
        self.confirm_button.clicked.connect(self.confirm_entry)
        self.currently_reading_check_box.toggled.connect(self.toggle_box)


    def toggle_box(self):
        """ If toggle box is checked, date finished QEdit/field is removed
        from layout. If, AFTER being checked, toggle box is unchecked,
        date finished field is added to layout, in correct row position."""

        if self.currently_reading_check_box.isChecked():
                self.layout.removeRow(self.date_finished_date_edit)
        else:
            self.date_finished_label = QtWidgets.QLabel('Date finished:')
            self.date_finished_date_edit = QtWidgets.QDateEdit()
            self.date_finished_date_edit.setDisplayFormat('d MMMM yyyy')
            self.date_finished_date_edit.setCalendarPopup(True)
            self.date_finished_date_edit.setDate(self.date_object)
            self.layout.insertRow(5, self.date_finished_label,
                                  self.date_finished_date_edit)

    def date_change(self):
        """ Function that, when a date if changed, sets start and end date
        accordingly."""

        try:
            self.start_date = self.date_started_date_edit.date()
            self.end_date = self.date_finished_date_edit.date()

            self.date_started_date_edit.setMaximumDate(self.end_date)
            self.date_finished_date_edit.setMinimumDate(self.start_date)
        except RuntimeError:
            pass


    def confirm_entry(self):
        """Creates a book entry and saves to JSON file"""

        # If book or author fields empty, creates alert dialogue window and
        # stops entry from being saved.
        if  self.book_line_edit.text() == '' or self.author_line_edit.text() \
        == '':
            self.empty_alert = QtWidgets.QMessageBox()
            self.empty_alert.setIcon(QtWidgets.QMessageBox.Warning)
            self.empty_alert.setText("Book and author fields can't be empty.")
            self.empty_alert.exec()
        else:
            if self.ID != '':
                self.temp_id = self.ID
            else:
                # Pulls ID for entry.
                self.temp_id = entry_ids.pop(0)

            # Gets string from QPlainTextEdit.
            self.text = self.comments_text_box.toPlainText()

            # Date formatting for more readable/user-friendly value.
            self.date_format = Qt.RFC2822Date

            # Converts QDateEdit value to string.
            self.temp_QDate = self.date_started_date_edit.date()
            self.start_date_text = self.temp_QDate.toString(self.date_format)
            # Attemps to create a date from date finished field (user input).
            # If it fails, it's because there is no date finished field, due to
            # currently reading checkbox being toggled on.
            try:
                self.temp_QDate = self.date_finished_date_edit.date()
                self.finished_date_text = self.temp_QDate.toString(
                    self.date_format)
            except RuntimeError:
                self.finished_date_text = ''
            # Converts ID to string.
            self.temp_id = str(self.temp_id)

            # Creates dictionary with user input.
            self.temp_entry_dict = {
                'ID': self.temp_id,
                'date_started': self.start_date_text,
                'date_finished': self.finished_date_text,
                'book_title': self.book_line_edit.text(),
                'author_title': self.author_line_edit.text(),
                'genre': self.genre_combo_box.currentText(),
                'comments': self.text
            }

            # Adds ID and user input dictionary as key-value pair to entries
            # dictionary.
            entries[self.temp_id] = self.temp_entry_dict

            # Saves entered data to JSON file.
            with open(entries_file, 'w') as f:
                json.dump(entries, f)
            # Saves updated IDs list to JSON file.
            with open(ids_file, 'w') as f:
                json.dump(entry_ids, f)
            # Clears entries
            self.book_line_edit.setText('')
            self.author_line_edit.setText('')
            self.comments_text_box.setPlainText('')

            # Refreshs table in main window.
            main_window.table_population()

            # Closes input window.
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('BookBrain')
    main_window = MainWindow()
    #app.setStyle('Fusion')
    try:
        with open(entries_file) as f:
            entries = json.load(f)
    except FileNotFoundError:
        pass

    try:
        with open(ids_file) as f:
            entry_ids = json.load(f)
    except FileNotFoundError:
        pass

    main_window.table_population()
    main_window.show()

    app.exec()
