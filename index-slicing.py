#!/usr/bin/env python3

message = input("Enter a message: ")

print("First character:", message[0] )
print("Last character:", message[-1])
print("Middle character:", message[int(len(message) / 2)])

print("even index characters", message[0::2])
print("odd index characters", message[1::2])

print("Reversed message:", message[::-1])