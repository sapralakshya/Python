def check_pattern(value,pattern):
    if pattern in value:
        return True
    else:
        return False
pat_tern="neu"
value="Ineuron"
print(check_pattern(value,pat_tern))
