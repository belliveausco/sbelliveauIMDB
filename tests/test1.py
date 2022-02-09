import imdb_setup_database


def test_data_size():
    result = imdb_setup_database.sample_data_top250_tv_shows()
    assert result == 250


test_data_size()
