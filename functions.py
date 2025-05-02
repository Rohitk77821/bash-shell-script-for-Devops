def check_memory(usage):
    if usage >75:
        return "memory is high!"
    return "memory is normal"
print(check_memory(99))
