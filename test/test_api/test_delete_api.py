class TestDeleteApi:

    def test_delete_notes(self, delete_notes, get_notes, post_notes):
        # 1. Создаём заметку
        note = post_notes.creating_note()
        assert note.status_code == 201  # проверка успешного создания

        # 2. Получаем ID последней созданной заметки через GET
        notes_list = get_notes.get_notes()
        note_id = notes_list.json()[-1]["id"]

        # 3. Удаляем заметку
        delete_response = delete_notes.delete_notes(note_id)
        assert delete_response.status_code == 200
