import pytest
from source.list.search_insert_position import Search

@pytest.fixture
def search_instance():
    return Search()


def test_existing_element_insertion(search_instance):
    nums = [1,2,3,4,5]
    target = 5
    insert_index = search_instance.searchInsert(nums, target)
    assert insert_index == 4


def test_new_element_insertion(search_instance):
    nums = [1, 3, 4, 5]
    target = 2
    insert_index = search_instance.searchInsert(nums, target)
    assert insert_index == 1
