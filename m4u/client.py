import requests


def upload():
    # create dummy data
    dummy_data = [
        {
            "log_contents": "Iguanas were falling out of the trees.",
        },
        {
            "log_contents": "Pandas were falling out of the trees.",
        },
        {
            "log_contents": "Dolphins were falling out of the trees.",
        },
        {
            "log_contents": "Sloths were falling out of the trees.",
        },
        {
            "log_contents": "Otters were falling out of the trees.",
        }
    ]

    for d in dummy_data:
        r = requests.post('http://127.0.0.1:8000/log', json=d)
        print(r)


def challenge():
    # dummy data
    dummy_data = [
        {
            "log_contents": "Iguanas were falling out of the trees.",
        },
        {
            "log_contents": "Pandas were falling out of the trees.",
        },
        {
            "log_contents": "Dolphins were falling out of the trees.",
        },
        {
            "log_contents": "Sloths were falling out of the trees.",
        },
        {
            "log_contents": "Otters were falling out of the trees.",
        }
    ]
    for d in dummy_data:
        r = requests.get(f'http://127.0.0.1:8000/challenge?data={str(d)}')
        print(r.text)


def get_state():
    r = requests.get(f'http://127.0.0.1:8000/state')
    print(r.text)

def proove(state):
    r = requests.get(f'http://127.0.0.1:8000/proove?state={state}')
    print(r.text)


def main():
    # upload()
    # challenge()
    get_state()
    # proove()


if __name__ == "__main__":
    main()
