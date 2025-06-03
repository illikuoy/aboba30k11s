# Мамедов Артур, 30-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_requests


def get_track_number_of_order():
    track_number = sender_requests.post_new_order()
    return track_number.json()["track"]


def test_get_order_by_track():
    track_number = get_track_number_of_order()
    get_response = sender_requests.get_order_info(track_number)
    assert get_response.status_code == 200