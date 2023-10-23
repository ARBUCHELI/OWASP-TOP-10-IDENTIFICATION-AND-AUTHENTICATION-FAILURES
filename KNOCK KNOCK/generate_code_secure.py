import secrets

def generate_secure_code():
    code = (secrets.token_urlsafe())
    print(code)
    return code

def main():
    generate_secure_code()

if __name__ == '__main__':
    main()