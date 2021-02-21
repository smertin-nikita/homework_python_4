import accounting


class TestAccounting:

    def setup(self):
        self.type = 'passport'
        self.number = '1111 111111'
        self.name = 'Name Name'
        self.shelf = '4'
        print('start')

    def test_add_shelf_passes(self):
        """ add_shelf() должен вернуть True если s """
        assert accounting.add_shelf(self.shelf)

    def test_add_shelf_fails(self):
        assert not accounting.add_shelf(self.shelf)

    def test_add_document_passes(self):
        assert accounting.add_document(self.type, self.number, self.name, self.shelf)

    def test_add_documents_fails(self):
        assert not accounting.add_document(self.type, self.number, self.name, self.shelf)

    def test_get_documents(self):
        assert accounting.get_documents(self.number)

    def test_print_people(self):
        assert accounting.print_people(self.number)

    def test_get_all_documents(self):
        assert accounting.get_all_documents()

    def test_get_shelfs(self):
        assert accounting.get_shelfs(self.number)

    def test_move_document_to_1_shelf(self):
        assert accounting.move_document(self.number, '1')

    def test_del_document(self):
        assert accounting.del_documents(self.number)
