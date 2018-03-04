from threading import Timer
print("in freer")
def timeout():
    print("Game over")

# duration is in seconds
t = Timer(2, timeout)
t.start()
print('entretemps')
# wait for time completion
t.join()