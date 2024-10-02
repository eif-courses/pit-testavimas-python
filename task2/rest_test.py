import requests


def test_get_book_by_id():
    url = "https://run.mocky.io/v3/9b2fc100-4c56-473d-b488-323dfd26396c/books/1"  # Replace with your mock API URL
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

    # Verify response structure (Assuming a book object with 'id', 'title', and 'author')
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "author" in data