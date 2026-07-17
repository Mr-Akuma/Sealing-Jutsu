import os

# TM SAST broker check
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEKEY123456"

def run(cmd):
    os.system("bash -c " + cmd)
