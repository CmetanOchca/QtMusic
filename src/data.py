class Data:
    def __init__(self):
        self.current_song_data = {
            'title': '',
            'performer': '',
            'duration': '',
            'assessment': '',
            'preview': ''
        }

    def update_song_data(self, title: str, performer, duration, assessment, preview):
        """Обновление данных текущей песни"""
        self.current_song_data = {
            'title': title,
            'performer': performer,
            'duration': duration,
            'assessment': assessment,
            'preview': preview
        }
        print('Данные успешно записаны')

    def get_current_song_data(self):
        """Получение данных текущей песни"""
        return self.current_song_data


    def clear_current_song_data(self):
        """Очистка данных текущей песни"""
        self.current_song_data = {
            'title': '',
            'performer': '',
            'duration': '',
            'assessment': '',
            'preview': ''
        }