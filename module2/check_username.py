#!/usr/bin/python3 

def check_username(username):
    if len(username) < 8:
        print("Invalid username. Must be at least 8 characters long")
    else:
        if len(username) > 15:
            print("Username Must be 15 characters maximum")
        else:
            print("Username is valid")


check_username("Luqman")
check_username("Annabel4real")
