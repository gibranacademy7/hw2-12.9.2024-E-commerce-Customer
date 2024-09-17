import sqlite_lib
import pytest
import hw2

@pytest.fixture

def db_connection():
    sqlite_lib.connect('datab.db')
    yield
    sqlite_lib.close()


def test_members_count_Bronze(db_connection):
    expected = sqlite_lib.run_query_select('SELECT COUNT ("Customer ID")'
                                           'FROM "commerce-e"'
                                           'WHERE "Membership Type" = "Bronze"')
    assert expected[0][0] == hw2.members_count('Bronze')

def test_members_count_Silver(db_connection):
    expected = sqlite_lib.run_query_select('SELECT COUNT ("Customer ID")'
                                           'FROM "commerce-e"'
                                           'WHERE "Membership Type" = "Silver"')
    assert expected[0][0] == hw2.members_count('Silver')

def test_members_count_Gold(db_connection):
    expected = sqlite_lib.run_query_select('SELECT COUNT ("Customer ID")'
                                           'FROM "commerce-e"'
                                           'WHERE "Membership Type" = "Gold"')

    assert expected[0][0] == hw2.members_count('Gold')