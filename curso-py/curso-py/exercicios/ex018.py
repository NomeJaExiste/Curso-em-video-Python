import math
an = math.radians(float(input('ângulo: ')))
print(f'Ângulo {math.ceil(math.degrees(an))}° com seno {math.sin(an):.2f}, cosseno {math.cos(an):.2f} e tangente {math.tan(an):.2f}')
