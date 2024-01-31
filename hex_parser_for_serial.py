from struct import pack

form = '>dd'
pos = [37.395742368912465, 126.97559883391028]
parser = lambda y, z: ' '.join(list(map(lambda x: f'{hex(x)[2:]:0>2}', list(pack(y, *z)))))

print(parser(form, pos))