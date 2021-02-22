import accounting


class TestAccounting:

    def setup(self):
        self.type = 'passport'
        self.number = '1111 111111'
        self.name = 'Name Name'
        self.shelf = '4'
        print('start')

    def test_add_shelf_passes(self):
        """ add_shelf() должен вернуть True если shelf нет в списке """
        assert accounting.add_shelf(self.shelf)

    def test_add_shelf_fails(self):
        """ add_shelf() должен вернуть False так как shelf есть в списке """
        assert not accounting.add_shelf(self.shelf)

    def test_add_document_passes(self):
        assert accounting.add_document(self.type, self.number, self.name, self.shelf)

    def test_add_documents_fails(self):
        assert not accounting.add_document(self.type, self.number, self.name, '5')

    def test_get_documents_passes(self):
        assert accounting.get_documents(self.number)

    def test_get_documents_fails(self):
        assert not accounting.get_documents('12')

    def test_print_people_passes(self):
        assert accounting.print_people(self.number)

    def test_print_people_fails(self):
        assert not accounting.print_people('12')

    def test_get_all_documents(self):
        assert accounting.get_all_documents()

    def test_get_shelfs_passes(self):
        assert accounting.get_shelfs(self.number)

    def test_get_shelfs_fails(self):
        assert not accounting.get_shelfs('5')

    def test_move_document_to_1_shelf(self):
        assert accounting.move_document(self.number, '1')

    def test_del_document(self):
        assert accounting.del_documents(self.number)
