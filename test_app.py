from app import get_all_doc_owners_names as ap, get_doc_owner_name as p, show_all_docs_info as l
from app import get_doc_shelf as s, add_new_doc as a, delete_doc as d

class TestCommands():

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('setup')

    def test_ap(self):
        assert ap() == {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}

    def test_p(self):
        assert p("11-2") == "Геннадий Покемонов"

    def test_l(self):
        all_docs = ['passport "2207 876234" "Василий Гупкин"',
                    'invoice "11-2" "Геннадий Покемонов"',
                    'insurance "10006" "Аристарх Павлов"']
        assert l() == all_docs

    def test_s(self):
        assert s("11-2") == "1"

    def test_a(self):
        assert a("123", "passport", "Me Me", "4") == "4"

    def test_d(self):
        assert d("11-2") == ('11-2', True)

    def teardown(self):
        print('teardown')

    def teardown_class(self):
        print('method teardown_class')