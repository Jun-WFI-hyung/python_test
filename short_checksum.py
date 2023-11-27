from struct import unpack_from, pack
# checksum value = a2:bc:d6:74
test = "aa:aa:a3:a3:18:02:00:00:07:00:00:00:35:fc:37:00:a0:0d:45:03:63:49:c1:00:a7:ff:6e:00:79:00:18:05:00:00:00:00:00:00:00:00:6e:00:00:00:0e:06:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:14:ec:00:07:3c:03:32:04:07:00:00:00:00:dd:6d:00:08:00:00:00:08:00:00:00:63:45:00:00:2c:08:45:00:fa:63:16:00:00:00:00:00:82:cc:01:00:c4:ff:18:00:09:80:00:00:00:00:00:00:28:01:45:03:00:00:00:00:1f:3f:c1:00:2f:fa:6e:00:e1:0d:f5:0f:e5:00:cd:0b:19:00:00:00:19:00:00:00:3c:14:00:00:cf:0b:28:00:5b:be:06:00:00:00:00:00:05:4e:00:00:50:00:18:00:12:80:00:00:00:00:00:00:68:0c:45:03:00:00:00:00:bd:44:c1:00:85:00:6f:00:69:0e:00:00:20:00:51:0c:2d:00:00:00:2d:00:00:00:80:a0:00:00:52:0b:fe:00:54:e8:10:00:00:00:00:00:1a:fa:01:00:3b:ff:18:00:5b:40:00:00:00:00:00:00:c4:07:45:03:00:00:00:00:86:1b:c1:00:8a:04:6f:00:00:00:6f:10:f5:06:43:0c:2f:00:00:00:2f:00:00:00:e6:45:00:00:6e:0b:01:01:e3:c1:0b:00:00:00:00:00:99:a3:01:00:3b:ff:18:00:b7:71:00:00:00:00:00:00:f8:0b:45:03:00:00:00:00:36:34:c1:00:44:02:6f:00:5f:0e:00:00:57:03:00:00:4d:00:00:00:4d:00:00:00:38:30:00:00:d3:0a:3a:00:98:32:68:00:00:00:00:00:f1:2e:01:00:90:00:18:00:03:60:00:00:00:00:00:00:c8:06:45:03:00:00:00:00:d3:3a:c1:00:2f:00:6f:00:45:0e:59:10:7d:00:2d:0c:6e:00:00:00:6e:00:00:00:3b:1e:00:00:12:0b:49:00:ca:a5:02:00:00:00:00:00:e4:68:00:00:35:00:18:00:00:50:00:00:00:00:00:00:28:0b:45:03:00:00:00:00:dc:40:c1:00:40:00:6f:00:4d:0e:00:00:5e:00:39:0c:32:00:00:00:32:00:00:00:ed:22:00:00:53:0b:23:00:0d:e3:02:00:00:00:00:00:78:8a:00:00:2d:00:18:00:1f:00:01:00:00:00:00:00:10:9e:3c:03:00:00:00:80:bf:3f:c1:00:aa:00:6f:00:72:34:00:00:35:00:00:00:00:00:00:00:3a:3a:aa:aa"

mask_32bit = 2**32-1
fin = 0
parsed_test = bytes(list(map(lambda x: int(x, 16), test.split(':'))))
for i in range(0, len(parsed_test), 4):
    unpacked_data = unpack_from('<I', parsed_test, offset=i)
    fin += unpacked_data[0]
    fin = fin & mask_32bit
print(pack('<I', fin))

