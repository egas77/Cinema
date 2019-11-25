import sys
import sqlite3
import datetime
import numpy as np
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image, ImageQt, ImageDraw, ImageFont

from UI.ui_main import Ui_MainWindow
from UI.ui_add_session_dialog import Ui_AddSessionDialog
from UI.ui_add_cinema_dialog import Ui_AddCinemaDialog
from UI.ui_add_hall_dialog import Ui_AddHallDialog
from UI.ui_add_film_dialog import Ui_AdFilmDialog
from UI.ui_details_session_dialog import Ui_DetalisSessionDialog


class Cinema(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data_base()

        self.open_session_btn.clicked.connect(self.open_session)
        self.remove_session_btn.clicked.connect(self.remove_session)
        self.add_sesion_btn.clicked.connect(self.add_session)

        self.sessions_table.cellClicked.connect(self.cell_click)

    def load_data_base(self):
        con = sqlite3.connect(data_base_path)
        cur = con.cursor()

        sessions = cur.execute(
            '''SELECT film, date, time, hall FROM sessions'''
        ).fetchall()

        if sessions:
            self.sessions_table.clear()
            self.sessions_table.setRowCount(len(sessions))
            self.sessions_table.setColumnCount(5)

            head = ['Фильм', 'Кинотеатр', 'Зал', 'Дата', 'Время']
            self.sessions_table.setHorizontalHeaderLabels(head)
            for session_number in range(len(sessions)):
                film_id, date_iso, time_iso, hall_id = sessions[session_number]

                film_name = cur.execute(
                    '''SELECT name FROM films WHERE id = ?''', (film_id,)
                ).fetchall()[0][0]

                cinema_name = cur.execute(
                    '''SELECT name FROM cinemas WHERE
                     id = (SELECT cinema FROM halls WHERE id = ?)''', (hall_id,)
                ).fetchall()[0][0]

                hall_name = cur.execute(
                    '''SELECT name FROM halls WHERE id = ?''', (hall_id,)
                ).fetchall()[0][0]

                self.sessions_table.setItem(session_number, 0, QTableWidgetItem(film_name))
                self.sessions_table.setItem(session_number, 1, QTableWidgetItem(cinema_name))
                self.sessions_table.setItem(session_number, 2, QTableWidgetItem(hall_name))
                self.sessions_table.setItem(session_number, 3, QTableWidgetItem(date_iso))
                self.sessions_table.setItem(session_number, 4, QTableWidgetItem(time_iso))

            self.sessions_table.resizeColumnsToContents()

        cur.close()
        con.close()

    def open_session(self):
        row = self.sessions_table.currentRow()

        if row != -1:
            film_name = self.sessions_table.item(row, 0).text()
            cinema_name = self.sessions_table.item(row, 1).text()
            hall_name = self.sessions_table.item(row, 2).text()
            date = self.sessions_table.item(row, 3).text()
            time = self.sessions_table.item(row, 4).text()

            con = sqlite3.connect(data_base_path)
            cur = con.cursor()

            id_session = cur.execute(
                '''SELECT id FROM sessions WHERE
                film = (SELECT id FROM films WHERE name = ?) AND
                date = ? AND time = ? AND
                hall = (SELECT id FROM halls WHERE
                 cinema = (SELECT id FROM cinemas WHERE name = ?) AND
                 name = ?)''',
                (film_name, date, time, cinema_name, hall_name,)).fetchone()[0]

            cur.close()
            con.close()

            details_session_dialog = DetailsSessionDialog(id_session)
            # details_session_dialog.exec()

    def remove_session(self):
        pass

    def add_session(self):
        add_session_dialog = AddSessionDialog()
        add_session_dialog.accepted.connect(self.load_data_base)
        add_session_dialog.exec()

    def cell_click(self, row):
        self.sessions_table.selectRow(row)


class AddSessionDialog(QDialog, Ui_AddSessionDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('Добавить сеанс')

        self.button_box.clicked.connect(self.click_button_box)
        self.cinema_tool_btn.clicked.connect(self.add_cinema)
        self.hall_tool_btn.clicked.connect(self.add_hall)
        self.film_tool_btn.clicked.connect(self.add_film)

        self.init_cinemas()
        self.init_halls()
        self.init_films()

        self.cinema_combo_box.currentTextChanged.connect(self.init_halls)

    def init_cinemas(self):
        con = sqlite3.connect(data_base_path)
        cur = con.cursor()

        self.cinema_combo_box.clear()
        cinemas = cur.execute('SELECT name FROM cinemas').fetchall()
        if cinemas:
            cinemas = list(map(lambda data: data[0], cinemas))
            self.cinema_combo_box.addItems(cinemas)
            self.cinema_combo_box.setCurrentIndex(0)

        cur.close()
        con.close()

    def init_halls(self):
        self.hall_combo_box.clear()

        name_cinema = self.cinema_combo_box.currentText()
        if name_cinema:
            con = sqlite3.connect(data_base_path)
            cur = con.cursor()

            halls = cur.execute(
                'SELECT name FROM halls WHERE cinema = (SELECT id FROM cinemas WHERE name = ?)',
                (name_cinema,)
            ).fetchall()

            if halls:
                halls = list(map(lambda data: data[0], halls))
                self.hall_combo_box.addItems(halls)

            cur.close()
            con.close()

    def init_films(self):
        self.film_combo_box.clear()
        con = sqlite3.connect(data_base_path)
        cur = con.cursor()
        films = cur.execute('SELECT name FROM films').fetchall()
        if films:
            films = list(map(lambda data: data[0], films))
            self.film_combo_box.addItems(films)
        cur.close()
        con.close()

    def click_button_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            cinema_name = self.cinema_combo_box.currentText()
            hall_name = self.hall_combo_box.currentText()
            film_name = self.film_combo_box.currentText()
            date = self.data_edit.date().toPyDate().isoformat()
            time = self.time_edit.time().toPyTime().isoformat()

            if cinema_name and hall_name and film_name and date and time:
                con = sqlite3.connect(data_base_path)
                cur = con.cursor()

                hall_id = cur.execute(
                    '''SELECT id FROM halls WHERE
                     cinema = (SELECT id FROM cinemas WHERE name = ?) AND
                     name = ?''', (cinema_name, hall_name,)
                ).fetchall()[0][0]

                film_id = cur.execute(
                    '''SELECT id FROM films WHERE name = ?''', (film_name,)
                ).fetchall()[0][0]

                cur.execute(
                    '''INSERT INTO sessions(film, date, time, hall) VALUES (?, ?, ?, ?)''',
                    (film_id, date, time, hall_id)
                )

                con.commit()
                cur.close()
                con.close()

                self.accept()
        elif btn_text == 'Cancel':
            self.reject()

    def add_cinema(self):
        add_cinema_dialog = AddCinemaDialog()
        add_cinema_dialog.accepted.connect(self.init_cinemas)
        add_cinema_dialog.exec()

    def add_hall(self):
        current_cinema = self.cinema_combo_box.currentText()
        if current_cinema:
            add_hall_dialog = AddHallDialog(current_cinema)
        else:
            add_hall_dialog = AddHallDialog()
        add_hall_dialog.accepted.connect(self.init_halls)
        add_hall_dialog.exec()

    def add_film(self):
        add_film_dialog = AddFilmDialog()
        add_film_dialog.accepted.connect(self.init_films)
        add_film_dialog.exec()


class AddCinemaDialog(QDialog, Ui_AddCinemaDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_box.clicked.connect(self.click_button_box)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('Кинотеатр')

    def click_button_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            name = self.name_line_edit.text()
            address = self.address_line_edit.text()
            if name and address:
                con = sqlite3.connect(data_base_path)
                cur = con.cursor()
                cur.execute(
                    '''INSERT INTO cinemas(name, address) VALUES (?, ?)''', (name, address,)
                )
                con.commit()
                cur.close()
                con.close()
                self.accept()
        elif btn_text == 'Cancel':
            self.reject()


class AddHallDialog(QDialog, Ui_AddHallDialog):
    def __init__(self, cinema=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.cinema = cinema
        self.init_cinemas()
        self.button_box.clicked.connect(self.click_button_box)

    def click_button_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            cinema_name = self.cinema_combo_box.currentText()
            hall_name = self.name_line_edit.text()
            count_row = self.count_row_edit.value()
            count_col = self.count_col_elit.value()
            if cinema_name and hall_name and count_row and count_row:
                con = sqlite3.connect(data_base_path)
                cur = con.cursor()
                hall = np.full((count_row, count_col), 0, dtype=int)
                hall_bytes = hall.dumps()
                cur.execute(
                    '''INSERT INTO halls(cinema, hall, name) VALUES (
                    (SELECT id FROM cinemas WHERE name = ?), ?, ?)''',
                    (cinema_name, hall_bytes, hall_name)
                )
                con.commit()
                cur.close()
                con.close()
                self.accept()
        elif btn_text == 'Cancel':
            self.reject()

    def init_cinemas(self):
        con = sqlite3.connect(data_base_path)
        cur = con.cursor()

        self.cinema_combo_box.clear()
        cinemas = cur.execute('SELECT name FROM cinemas').fetchall()
        if cinemas:
            cinemas = list(map(lambda data: data[0], cinemas))
            self.cinema_combo_box.addItems(cinemas)
            if self.cinema:
                self.cinema_combo_box.setCurrentText(self.cinema)
            else:
                self.cinema_combo_box.setCurrentIndex(0)

        con.close()


class AddFilmDialog(QDialog, Ui_AdFilmDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Фильм')
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.button_box.clicked.connect(self.click_button_box)

    def click_button_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            name = self.name_line_edit.text()
            description = self.description_edit.toPlainText()
            if name and description:
                con = sqlite3.connect(data_base_path)
                cur = con.cursor()
                cur.execute(
                    '''INSERT INTO films(name, description) VALUES (?, ?)''',
                    (name, description,)
                )
                con.commit()
                cur.close()
                con.close()
                self.accept()
        elif btn_text == 'Cancel':
            self.reject()


class DetailsSessionDialog(QDialog, Ui_DetalisSessionDialog):
    def __init__(self, id_session):
        super().__init__()
        self.setupUi(self)
        self.id_session = id_session
        self.size_font = 25
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.initUI()

    def initUI(self):
        con = sqlite3.connect(data_base_path)
        cur = con.cursor()

        session_data = cur.execute('''SELECT id, film, date, time, hall FROM sessions WHERE
        id = ?''', (self.id_session,)).fetchall()[0]

        id_session = session_data[0]
        name_film = session_data[1]
        date = session_data[2]
        time = session_data[3]
        id_hall = session_data[4]

        hall_bytes = cur.execute(
            '''SELECT hall FROM halls WHERE id = ?''', (id_hall,)
        ).fetchone()[0]

        hall_array = pickle.loads(hall_bytes)
        font = ImageFont.truetype("arial.ttf", self.size_font)
        height_text = self.size_font
        max_width_text_row, max_width_text_col = 0, 0

        image = Image.new('RGB', (1000, 1000))
        draw = ImageDraw.Draw(image)

        shape = hall_array.shape

        for num in range(shape[0]):
            width_text, height_text = draw.textsize(str(num + 1), font=font)
            if width_text > max_width_text_row:
                max_width_text_row = width_text

        for num in range(shape[1]):
            width_text, height_text = draw.textsize(str(num + 1), font=font)
            if width_text > max_width_text_col:
                max_width_text_col = width_text

        size_item = (max(max_width_text_row, max_width_text_col), height_text)

        for row in range(1, shape[0] + 1):
            draw.text((0, row * height_text), str(row), font=font)

        for col in range(shape[1]):
            draw.text((col * max_width_text_col + max_width_text_row, 0),
                      str(col + 1), font=font)

        size_img = (shape[0] * size_item, shape[1] * size_item)

        # for x in range(self.size_font, size_img[0] + self.size_font, self.size_font):
        #     for y in range(self.size_font, size_img[1] + self.size_font, self.size_font):
        #         draw.rectangle([(x, y), (x + self.size_font - 1, y + self.size_font - 1)])

        image.show()


if __name__ == '__main__':
    data_base_path = 'data/cinema.db'
    app = QApplication(sys.argv)
    cinema = Cinema()
    cinema.show()
    sys.exit(app.exec())
