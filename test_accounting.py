import accounting


class TestAccounting:

    def setup(self):
        print("Start test")

    def teardown(self):
        print('Stop test')

    def test_add_document(self):
        assert accounting.add_document("insurance", "10006", "Аристарх Павлов", '4')

    def test_del_document(self):
        assert accounting.del_documents("10006")
