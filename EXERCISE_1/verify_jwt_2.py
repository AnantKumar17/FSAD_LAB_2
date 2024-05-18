import jwt

# Received token
token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkFuYW50X0t1bWFyQDE3IiwidXNlcklEIjoxNzE3LCJleHAiOjE3MTYwMjU1MDN9.G96iaODA0meN6R6X0NWPicEE2c13jmBWyUXQB80ZhR1wQHj1URTk1R9MzEFY6U9UXxqhjW7Z1SVG5D2buew2tg"

# Secret key (same as used for generation)
secret = "AdminNew@17"

try:
    decoded = jwt.decode(token, secret, algorithms=['HS512'])
    print(decoded)
except jwt.exceptions.JWTError as e:
    print("Invalid JWT:", e)
