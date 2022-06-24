import copy
import pytest
from accounting import name_by_doc, shelf_by_doc, add_doc, del_doc, add_shelf, move_doc, documents, directories

dirs = copy.deepcopy(directories)
docs = copy.deepcopy(documents)
FIXTURE_name_by_doc = [('1', 'Документа с таким номером у нас нет!')] \
          + [(doc['number'], doc['name']) for doc in documents]


@pytest.mark.parametrize('doc, result', FIXTURE_name_by_doc)
def test_name_by_doc(doc, result):
    assert name_by_doc(doc) == result


FIXTURE_shelf_by_doc = [('1', 'Документа с таким номером у нас нет!')] \
          + [(doc, shelf) for shelf, docs in directories.items() for doc in docs]


@pytest.mark.parametrize('doc, result', FIXTURE_shelf_by_doc)
def test_shelf_by_doc(doc, result):
    assert shelf_by_doc(doc) == result


FIXTURE_add_doc = [('11-2', '', '', '', 'Документ с таким номером уже существует'),
                   ('', '', '', '4670', 'Полки с таким номером у нас нет!'),
                   ('11-3', 'invoice', 'Аристарх Павлов', '3', 'Документ invoice с номером 11-3 добавлен на полку 3')]


@pytest.mark.parametrize('doc, type, owner, shelf, result', FIXTURE_add_doc)
def test_add_doc(doc, type, owner, shelf, result):
    assert add_doc(doc, type, owner, shelf) == result


documents = copy.deepcopy(docs)
FIXTURE_add_shelf = [('33', 'Полка 33 добавлена, теперь на неё можно что-нибудь положить')] \
                    + [(shelf, 'Полка с таким номером уже есть!') for shelf in directories]


@pytest.mark.parametrize('shelf, result', FIXTURE_add_shelf)
def test_add_shelf(shelf, result):
    assert add_shelf(shelf) == result


directories = copy.deepcopy(dirs)
documents = copy.deepcopy(docs)
FIXTURE_move_doc = [('33546s', '1', 'Документа с таким номером у нас нет!'),
                    ('', '5869', 'Полки с таким номером у нас нет!'),
                    ('11-2', '3', 'Документ 11-2 перемещён на полку 3')]


@pytest.mark.parametrize('doc, shelf, result', FIXTURE_move_doc)
def test_move_doc(doc, shelf, result):
    assert move_doc(doc, shelf) == result


documents = copy.deepcopy(docs)
directories = copy.deepcopy(dirs)
FIXTURE_del_doc = [('3345a', 'Документа с таким номером у нас нет!')] \
                        + [(doc['number'], 'Документ удалён!') for doc in documents]


@pytest.mark.parametrize('doc, result', FIXTURE_del_doc)
def test_del_doc(doc, result):
    assert del_doc(doc) == result

print(documents)
print(directories)