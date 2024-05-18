import jwt

# Received token
token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkFuYW50X0t1bWFyQDE3IiwidXNlcklEIjoxNzAxLCJleHAiOjE3MTYwMjI5ODV9.r3_arFmN6HEn8qaZxa66J6j_8zscHzLWszFomusPuAU4WCRn9p4px4QcueMCYan_"

# Secret key (same as used for generation)
secret = "Admin@17"

try:
    decoded = jwt.decode(token, secret, algorithms=['HS384'])
    print(decoded)
except jwt.exceptions.JWTError as e:
    print("Invalid JWT:", e)
