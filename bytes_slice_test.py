def validateData(data: bytes, chunk_size: int) -> bytes:
        if len(data) % chunk_size:
            print(f"[ERROR | validateData] Data length is not {chunk_size} multiple")
            return data[:-(len(data) % chunk_size)]
        else:
            return data
        
a = b'ddd'
print(a)
a = validateData(a, 4)
print(a)
a = validateData(a, 4)
print(a)