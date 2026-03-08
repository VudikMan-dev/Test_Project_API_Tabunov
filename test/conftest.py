import pytest

from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_authorization import PostAuthorization
from api.post_notes import PostNotes
from api.post_registration import PostRegistration
from test.data.json_for_post_notes import JsonForPostNotesTest

# Инициализируем класс PostRegistration(), тем самым регистрируемся
@pytest.fixture
def post_registration():
    return PostRegistration()

# Инициализируем класс PostAuthorization(), тем самым авторизуемся
@pytest.fixture
def post_authorization():
    return PostAuthorization()

# Инициализируем класс PostNotes(token), тем самым создаём заметку
@pytest.fixture
def post_notes(token):
    return PostNotes(token)

# Инициализируем класс GetNotes(token), тем самым возвращаем id заметки
@pytest.fixture
def get_notes(token):
    return GetNotes(token)

# Инициализируем класс DeleteNotes(token), тем самым удаляем заметку по id
@pytest.fixture
def delete_notes(token):
    return DeleteNotes(token)

# Фикстура на получение токена, переиспользуем фикстуру post_authorization()
@pytest.fixture
def token(post_authorization):
    return post_authorization.get_token()

# Фикстура на создание заметки и возврат заметки по id, переиспользуем фикстуры get_notes, post_notes
# Актуально для DELETE удаление заметки - предусловия создание заметки и возвращение нашей созданной заметки
@pytest.fixture
def setup_create_note_id(get_notes, post_notes): # создаём заметку
    post_notes.create_note()
    id_note = get_notes.get_note_by_title(
        JsonForPostNotesTest.DATA_POST_NOTES["title"]) # получаем id заметки
    return id_note # возвращаем заметку



# Фикстура на получение заметок и удаление заметки вконце теста, , переиспользуем фикстуры get_notes, delete_notes
# Актуально для POST создание заметки - предусловия не нужны, постусловия удалить заметку
@pytest.fixture
def teardown_note_delete(get_notes, delete_notes): # ничего не делаем до конца теста
    yield # ничего не возвращаем
    id_note = get_notes.get_note_by_title(JsonForPostNotesTest.DATA_POST_NOTES["title"]) # получаем id заметки после теста
    delete_notes.delete_notes(id_note) # удаляем заметку вконце теста

# Фикстура на создание заметки и удаление вконце теста, переиспользуем фикстуры delete_notes, setup_create_note
# Актуально для GET - предусловия создание заметки и постусловия удаление заметки
@pytest.fixture
def setup_teardown_note(delete_notes, setup_create_note): # создаём заметку и возвращаем id
    yield setup_create_note # возвращаем заметку
    delete_notes.delete_notes(setup_create_note) # удаляем заметку вконце теста
