import threading
import time


def test_create_user(client):
    resp = client.post(
        "/users/register",
        json={
            "first_name": "Pavel",
            "last_name": "Durov",
            "nickname": "durov",
        },
    )

    assert resp.status_code == 201  # Created


def test_get_users(client):
    starting_time = time.time()
    st = set()

    def add_durov():
        st.add(client.get("/users/durov").json()["id"])

    threads = [threading.Thread(target=add_durov)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert len(set(st)) == 1

    assert starting_time - time.time() < 15  # Check time
