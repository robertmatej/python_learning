import struct

file = "obrazy\_bus.png"
file2 = "obrazy\pb95.jpg"
ihdr_signature = []
#checkong IHDR signature
try:
    with open(file, 'rb') as reader:
        for i in range(0, 8):
            #print(reader.read(1))
            byte = reader.read(1)
            unpacked = struct.unpack('B', byte)
            print(unpacked)
            ihdr_signature.append(unpacked[0])


    if ihdr_signature == [137, 80, 78, 71, 13, 10, 26, 10]:
        print(f'Loaded file is PNG, IHDR signature: {ihdr_signature}')
    else:
        print(f'Loaded file is not PNG, IHDR signature: {ihdr_signature}')

except FileNotFoundError:
    print('Wrong filename')

# getting IHDR header witch file information
def ihdr_header():
    try:
        with open(file, 'rb') as reader2:
            # getting information from IHDR
            reader2.read(16)
            width = struct.unpack('!I', reader2.read(4))
            print(f'width: {width[0]}')
            height = struct.unpack('!I', reader2.read(4))
            print(f'height: {height[0]}')
            b_depth = struct.unpack('B', reader2.read(1))
            print(f'bit depth: {b_depth[0]}')
            color_type = struct.unpack('B', reader2.read(1))
            print(f'color type: {color_type[0]}')
            compr_meth = struct.unpack('B', reader2.read(1))
            print(f'compression method: {compr_meth[0]}')
            filter_meth = struct.unpack('B', reader2.read(1))
            print(f'filter method: {filter_meth[0]}')
            interlace_meth = struct.unpack('B', reader2.read(1))
            print(f'interlace method: {interlace_meth[0]}')


    except FileNotFoundError:
        print('Wrong filename')


ihdr_header()