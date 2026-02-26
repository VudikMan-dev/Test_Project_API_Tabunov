import pytest

from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_authorization import PostAuthorization
from api.post_notes import PostNotes
from api.post_registration import PostRegistration
from test.data.json_for_post_notes import JsonForPostNotesTest


@pytest.fixture
def post_registration():
    return PostRegistration()

@pytest.fixture
def post_authorization():
    return PostAuthorization()



@pytest.fixture
def get_notes(token):
    return GetNotes(token)

@pytest.fixture
def post_notes(token):
    return PostNotes(token)

@pytest.fixture
def delete_notes(token):
    return DeleteNotes(token)

@pytest.fixture
def token(post_authorization):
    return post_authorization.get_token()



@pytest.fixture
def setup_create_note(get_notes, post_notes): # создаём заметку
    id_note = get_notes.get_note_by_title(JsonForPostNotesTest.DATA_POST_NOTES["title"]) # получаем id заметки
    return id_note # возвращаем заметку

@pytest.fixture
def teardown_note(get_notes, delete_notes): # ничего не делаем до конца теста
    yield # ничего не возвращаем
    id_note = get_notes.get_note_by_title(JsonForPostNotesTest.DATA_POST_NOTES["title"]) # получаем id заметки после теста
    delete_notes.delete_notes(id_note) # удаляем заметку вконце теста

@pytest.fixture
def setup_teardown_note(delete_notes, setup_create_note): # создаём заметку и возвращаем id
    yield setup_create_note # возвращаем заметку
    delete_notes.delete_notes(setup_create_note) # удаляем заметку вконце теста