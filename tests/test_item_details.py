import pytest
from pages.item_details_page import ItemDetailsPage

def test_item_displaying(item_detail_page: ItemDetailsPage):
    item_detail_page.check_item_name()
    item_detail_page.check_item_desc()
    item_detail_page.check_price_format()

def test_add_item_to_cart(item_detail_page: ItemDetailsPage):
    item_detail_page.check_adding_item_to_cart()

def test_remove_item_from_cart(item_detail_page: ItemDetailsPage):
    item_detail_page.check_removing_item_from_cart()

def test_go_back_to_products(item_detail_page: ItemDetailsPage):
    item_detail_page.check_back_to_products_link()