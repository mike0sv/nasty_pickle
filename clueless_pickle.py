import pickle


def main():
    # unpickle bomb
    with open('bomb_virus_with_pic.pkl', 'rb') as f:
        payload = f.read()
        data = pickle.loads(payload)
        print(data)

    data2 = ['another', 'values']

    payload = pickle.dumps(data2)
    data3 = pickle.loads(payload)

    print(data3)


if __name__ == '__main__':
    main()
