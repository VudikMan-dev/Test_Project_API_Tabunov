import pytest

from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_authorization import PostAuthorization
from api.post_notes import PostNotes
from api.post_registration import PostRegistration
from test.data.json_for_post_autorization import DATA_POST_AUTHORIZATION
from test.data.json_for_post_notes import JsonForPostNotesTest


@pytest.fixture
def post_registration():
    """Инициализируем класс PostRegistration(), тем самым регистрируемся"""
    return PostRegistration()


@pytest.fixture
def post_authorization():
    """Инициализируем класс PostAuthorization(), тем самым авторизуемся"""
    return PostAuthorization()


@pytest.fixture
def post_notes(token):
    """Инициализируем класс PostNotes(token), тем самым создаём объект класса"""
    return PostNotes(token)


@pytest.fixture
def notes_client(token):
    """Инициализируем класс GetNotes(token), возвращаем экземпляр класса
       GetNotes с токеном, переиспользуем фикстуру token"""
    return GetNotes(token)


@pytest.fixture
def delete_client(token):
    """Инициализируем класс DeleteNotes(token), тем самым возвращаем экземпляр класса DeleteNotes"""
    return DeleteNotes(token)


@pytest.fixture
def token(post_authorization):
    """Фикстура на получение токена, переиспользуем фикстуру post_authorization() и метод get_token()"""
    return post_authorization.get_token(email=DATA_POST_AUTHORIZATION["email"],
                                        password=DATA_POST_AUTHORIZATION["password"])


@pytest.fixture
def setup_create_note(notes_client, post_notes):  # создаём заметку
    """Фикстура на создание заметки и возврат заметки по id, переиспользуем фикстуры notes_client, post_notes
    Актуально для DELETE удаление заметки - предусловия создание заметки и возвращение нашей созданной заметки"""
    post_notes.create_note(body=JsonForPostNotesTest.DATA_POST_NOTES)
    id_note = notes_client.get_note_by_title(
        JsonForPostNotesTest.DATA_POST_NOTES["title"])  # получаем id заметки
    return id_note  # возвращаем заметку


@pytest.fixture
def teardown_note_delete(notes_client, delete_client):  # ничего не делаем до конца теста
    """Фикстура на получение заметок и удаление заметки вконце теста, , переиспользуем фикстуры notes_client, delete_notes
    Актуально для POST создание заметки - предусловия не нужны, постусловия удалить заметку"""
    yield  # ничего не возвращаем
    id_note = notes_client.get_note_by_title(
        JsonForPostNotesTest.DATA_POST_NOTES["title"])  # получаем id заметки после теста
    delete_client.delete_notes(id_note)  # удаляем заметку вконце теста


@pytest.fixture
def setup_teardown_note(delete_client, setup_create_note):  # создаём заметку и возвращаем id
    """Фикстура на создание заметки и удаление вконце теста, переиспользуем фикстуры delete_notes, setup_create_note
    Актуально для GET - предусловия создание заметки и постусловия удаление заметки"""
    yield setup_create_note  # возвращаем заметку
    delete_client.delete_notes(setup_create_note)  # удаляем заметку вконце теста


@pytest.fixture
def second_user_token(post_authorization):
    """Получение токена второго пользователя"""
    token2 = post_authorization.get_token(email="second_user@test.com", password="123456")
    return token2
