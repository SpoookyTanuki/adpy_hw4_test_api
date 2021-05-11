from app import get_all_doc_owners_names as ap, get_doc_owner_name as p, show_all_docs_info as l
from app import get_doc_shelf as s, add_new_doc as a, delete_doc as d


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


class TestCommands():
    def setup(self):
        print('method setUp')

    def teardown(self):
        print('method tearDown')

    def test_ap(self):
        assert ap(), {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}

    def test_p(self):
        assert p("11-2"), "Геннадий Покемонов"

    def test_l(self):
        assert l(), f'passport "2207 876234" "Василий Гупкин" invoice "11-2" "Геннадий Покемонов" insurance "10006" "Аристарх Павлов"'
    #   не понимаю, почему не проходит тест, убирала f-строку, подставляла абзацы - не помогло

    def test_s(self):
        assert s("11-2"), "Документ находится на полке номер 1"

    def test_a(self):
        assert a("123", "passport", "Me Me", "4"), "4"
    #   не уверена, что сделала правильно, но не понимаю,
    #   как в assert запихать параметры других функций, которые не тестируются

    def test_d(self):
        assert d("11-2"), f'Документ с номером "11-2" был успешно удален'
    # но как проверить в реале, удалился он или нет?
    # вызывать внутри теста функцию show_all_docs_info и смотреть, удалилось ли что-то оттуда?






