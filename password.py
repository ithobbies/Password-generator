import secrets


def create_new(length, characters):
    return "".join(secrets.choice(characters) for _ in range(length))
