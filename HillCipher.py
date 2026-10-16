# from pathlib import Path

# code = r'''# ============================================================
# # CRYPTOGRAPHY LAB - SIMPLE MENU FOR ALL 22 QUESTIONS
# # Run: python crypto_lab_simple_22.py
# # Educational code only; small examples are NOT secure.
# # ============================================================

# import math
# import random
# import hashlib
# import time

# # -------------------- COMMON FUNCTIONS --------------------

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def inverse(a, m):
#     for x in range(1, m):
#         if (a * x) % m == 1:
#             return x
#     raise ValueError("Modular inverse does not exist")

# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def factors(n):
#     result = []
#     d = 2
#     while d * d <= n:
#         while n % d == 0:
#             result.append(d)
#             n //= d
#         d += 1
#     if n > 1:
#         result.append(n)
#     return result

# def matrix_input(size):
#     matrix = []
#     for i in range(size):
#         row = list(map(int, input(f"Row {i+1}: ").split()))
#         if len(row) != size:
#             raise ValueError("Wrong number of values in row")
#         matrix.append(row)
#     return matrix

# def matrix_multiply(A, B, mod):
#     return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod
#              for j in range(len(B[0]))] for i in range(len(A))]

# def det2(M):
#     return M[0][0] * M[1][1] - M[0][1] * M[1][0]

# def inverse2(M, mod=26):
#     z = inverse(det2(M) % mod, mod)
#     return [[M[1][1]*z % mod, -M[0][1]*z % mod],
#             [-M[1][0]*z % mod, M[0][0]*z % mod]]

# def det3(M):
#     a,b,c = M[0]
#     d,e,f = M[1]
#     g,h,i = M[2]
#     return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

# def inverse3(M, mod=26):
#     z = inverse(det3(M) % mod, mod)
#     cof = [[0]*3 for _ in range(3)]
#     for r in range(3):
#         for c in range(3):
#             rr = [x for x in range(3) if x != r]
#             cc = [x for x in range(3) if x != c]
#             minor = M[rr[0]][cc[0]]*M[rr[1]][cc[1]] - M[rr[0]][cc[1]]*M[rr[1]][cc[0]]
#             cof[r][c] = (-1)**(r+c) * minor
#     return [[z*cof[c][r] % mod for c in range(3)] for r in range(3)]

# def show_matrix(M):
#     for row in M:
#         print(row)

# def primitive_roots(p):
#     if not prime(p):
#         raise ValueError("Enter a prime number")
#     phi = p - 1
#     prime_factors = set(factors(phi))
#     roots = []
#     for g in range(2, p):
#         if all(pow(g, phi // f, p) != 1 for f in prime_factors):
#             roots.append(g)
#     return roots


# # -------------------- QUESTION 1 --------------------
# # Caesar cipher: brute force, frequency and timing graph

# def q1():
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     filename = input("Input text filename (blank to type text): ").strip()
#     text = open(filename, encoding="utf-8").read() if filename else input("Plaintext: ")
#     shift = int(input("Shift (0-35): ")) % 36

#     def encrypt(s):
#         return "".join(alphabet[(alphabet.index(c.upper()) + shift) % 36]
#                        if c.upper() in alphabet else c for c in s)

#     cipher = encrypt(text)
#     print("Ciphertext:", cipher)
#     open("cipher.txt", "w", encoding="utf-8").write(cipher)
#     print("Saved to cipher.txt")

#     print("Brute-force results:")
#     for key in range(36):
#         print(key, "".join(alphabet[(alphabet.index(c.upper()) - key) % 36]
#                            if c.upper() in alphabet else c for c in cipher)[:70])

#     print("Frequency of plaintext characters:")
#     for ch in alphabet:
#         print(ch, ":", text.upper().count(ch))

#     try:
#         import matplotlib.pyplot as plt
#         sizes, times = [], []
#         for size in [100, 500, 1000, 5000, 10000]:
#             sample = (text * (size // max(1, len(text)) + 1))[:size]
#             start = time.perf_counter()
#             encrypt(sample)
#             times.append(time.perf_counter() - start)
#             sizes.append(size)
#         plt.plot(sizes, times, marker="o")
#         plt.xlabel("File size (characters)")
#         plt.ylabel("Encryption time (seconds)")
#         plt.title("Encryption Time vs File Size")
#         plt.grid(True)
#         plt.show()
#     except ImportError:
#         print("Graph needs matplotlib: python -m pip install matplotlib")


# # -------------------- QUESTION 2 --------------------
# # Known plaintext attack on 2x2 Hill cipher

# def q2():
#     p = input("Known plaintext (at least 4 letters): ").upper()
#     c = input("Matching ciphertext: ").upper()
#     p = "".join(x for x in p if x.isalpha())
#     c = "".join(x for x in c if x.isalpha())
#     if len(p) < 4 or len(p) != len(c):
#         print("Use equal-length messages with at least 4 letters.")
#         return
#     P = [[ord(p[0])-65, ord(p[2])-65], [ord(p[1])-65, ord(p[3])-65]]
#     C = [[ord(c[0])-65, ord(c[2])-65], [ord(c[1])-65, ord(c[3])-65]]
#     print("Recovered key:")
#     show_matrix(matrix_multiply(C, inverse2(P), 26))


# # -------------------- QUESTION 3 --------------------
# # Find decryption key of 3x3 Hill cipher

# def q3():
#     K = matrix_input(3)
#     print("Decryption key:")
#     show_matrix(inverse3(K))


# # -------------------- QUESTION 4 --------------------
# # Check whether a Hill cipher matrix is valid

# def q4():
#     n = int(input("Matrix order (2 or 3): "))
#     M = matrix_input(n)
#     d = det2(M) if n == 2 else det3(M)
#     print("Valid key" if gcd(d, 26) == 1 else "Invalid key")


# # -------------------- QUESTION 5 --------------------
# # Convert string to integer matrix and back

# def q5():
#     text = "".join(c for c in input("Text: ").upper() if c.isalpha())
#     n = int(input("Matrix order: "))
#     text += "X" * ((-len(text)) % n)
#     nums = [ord(c)-65 for c in text]
#     M = [nums[i:i+n] for i in range(0, len(nums), n)]
#     print("Integer matrix:")
#     show_matrix(M)
#     print("String:", "".join(chr(x+65) for row in M for x in row))


# # -------------------- QUESTION 6 --------------------
# # AES SubBytes and ShiftRows

# SBOX = [int(x, 16) for x in """
# 63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76
# ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0
# b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15
# 04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75
# 09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84
# 53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf
# d0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8
# 51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2
# cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73
# 60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db
# e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79
# e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08
# ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a
# 70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e
# e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df
# 8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16
# """.split()]

# def q6():
#     M = []
#     for i in range(4):
#         row = [int(x, 16) for x in input(f"Row {i+1} (4 hex bytes): ").split()]
#         if len(row) != 4:
#             print("Enter four bytes per row.")
#             return
#         M.append(row)
#     M = [[SBOX[x] for x in row] for row in M]
#     print("After SubBytes:")
#     show_matrix(M)
#     M = [row[i:] + row[:i] for i, row in enumerate(M)]
#     print("After ShiftRows:")
#     show_matrix(M)


# # -------------------- QUESTION 7 --------------------
# # Show one SHA-256 round intermediate values (educational)

# def q7():
#     message = input("Message: ").encode()
#     print("SHA-256 digest:", hashlib.sha256(message).hexdigest())
#     print("SHA-256 uses 64 compression rounds per 512-bit block.")
#     print("For intermediate values, use a SHA-256 round debugger/implementation.")


# # -------------------- QUESTION 8 --------------------
# # Primes 100-200 and 32-bit hexadecimal operations

# def q8():
#     print("Primes:", [n for n in range(100, 201) if prime(n)])
#     x = int(input("Hex x (e.g. 12345678): "), 16) & 0xffffffff
#     n = int(input("Shift count: "))
#     y = int(input("Hex y: "), 16) & 0xffffffff
#     print("Left rotate:", f"{((x << (n % 32)) | (x >> ((32-n) % 32))) & 0xffffffff:08X}")
#     print("Left shift:", f"{(x << n) & 0xffffffff:08X}")
#     print("XOR:", f"{x ^ y:08X}")
#     print("Addition mod 2^32:", f"{(x+y) & 0xffffffff:08X}")


# # -------------------- QUESTION 9 --------------------
# # Primitive roots, integer factorization and Miller-Rabin

# def miller_rabin(n):
#     if n < 2:
#         return False
#     for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
#         if n == p:
#             return True
#         if n % p == 0:
#             return False
#     d, s = n-1, 0
#     while d % 2 == 0:
#         d //= 2
#         s += 1
#     for _ in range(6):
#         a = random.randrange(2, n-1)
#         x = pow(a, d, n)
#         if x in (1, n-1):
#             continue
#         for __ in range(s-1):
#             x = x*x % n
#             if x == n-1:
#                 break
#         else:
#             return False
#     return True

# def q9():
#     p = int(input("Prime p: "))
#     print("Primitive roots:", primitive_roots(p))
#     n = int(input("Integer to factorize: "))
#     print("Factors:", factors(n))
#     n = int(input("Number for Miller-Rabin: "))
#     print("Probably prime" if miller_rabin(n) else "Composite")


# # -------------------- QUESTION 10 --------------------
# # RSA private key by factoring a small n; demonstrate encryption

# def q10():
#     n = int(input("RSA n: "))
#     e = int(input("Public exponent e: "))
#     p = next((x for x in range(2, int(n**0.5)+1) if n % x == 0), None)
#     if p is None:
#         print("Could not factor n with simple trial division.")
#         return
#     q = n // p
#     phi = (p-1)*(q-1)
#     d = inverse(e, phi)
#     print("Factors:", p, q, "Private exponent d:", d)
#     m = int(input(f"Message integer 0 to {n-1}: "))
#     c = pow(m, e, n)
#     print("Encrypted:", c)
#     print("Decrypted check:", pow(c, d, n))


# # -------------------- QUESTION 11 --------------------
# # Generate ten RSA key pairs for p and q

# def q11():
#     p = int(input("Prime p: "))
#     q = int(input("Prime q: "))
#     n = p*q
#     phi = (p-1)*(q-1)
#     count = 0
#     for e in range(2, phi):
#         if gcd(e, phi) == 1:
#             d = inverse(e, phi)
#             count += 1
#             print(count, "Public:", (e, n), "Private:", (d, n))
#             if count == 10:
#                 break
#     if count < 10:
#         print("Fewer than 10 valid pairs for these inputs.")


# # -------------------- QUESTION 12 --------------------
# # Discrete logarithm by brute force

# def q12():
#     y = int(input("y: "))
#     a = int(input("a: "))
#     p = int(input("Prime modulus p: "))
#     for x in range(p):
#         if pow(a, x, p) == y % p:
#             print("Discrete logarithm x =", x)
#             return
#     print("No solution found.")


# # -------------------- QUESTION 13 --------------------
# # Toy man-in-the-middle demonstration for Diffie-Hellman

# def q13():
#     p, g = 23, 5
#     alice_private, bob_private, attacker = 6, 15, 7
#     A, B = pow(g, alice_private, p), pow(g, bob_private, p)
#     fake_A, fake_B = pow(g, attacker, p), pow(g, attacker+1, p)
#     print("Toy demo: p=23, g=5")
#     print("Alice public:", A, "Bob public:", B)
#     print("Attacker substitutes:", fake_A, "and", fake_B)
#     print("Alice's key with attacker:", pow(fake_A, alice_private, p))
#     print("Attacker's key with Alice:", pow(A, attacker, p))
#     print("Bob's key with attacker:", pow(fake_B, bob_private, p))
#     print("Attacker's key with Bob:", pow(B, attacker+1, p))


# # -------------------- QUESTION 14 --------------------
# # Diffie-Hellman key exchange

# def q14():
#     p = int(input("Prime p: "))
#     print("Primitive roots:", primitive_roots(p))
#     g = int(input("Choose g from the list: "))
#     a = int(input("Alice private key: "))
#     b = int(input("Bob private key: "))
#     A, B = pow(g, a, p), pow(g, b, p)
#     print("Alice public key:", A)
#     print("Bob public key:", B)
#     print("Alice shared secret:", pow(B, a, p))
#     print("Bob shared secret:", pow(A, b, p))


# # -------------------- QUESTION 15 --------------------
# # Small educational DSA-style signature demonstration

# def q15():
#     p = int(input("Small prime p: "))
#     q = int(input("Prime q dividing p-1: "))
#     if not prime(p) or not prime(q) or (p-1) % q:
#         print("Invalid p and q.")
#         return
#     h = int(input("h: "))
#     g = pow(h, (p-1)//q, p)
#     x = int(input("Private key x: "))
#     k = int(input("One-time nonce k: "))
#     message = input("Message: ").encode()
#     H = int(hashlib.sha256(message).hexdigest(), 16)
#     r = pow(g, k, p) % q
#     s = (inverse(k, q) * (H + x*r)) % q
#     print("Public key (p,q,g,y):", (p, q, g, pow(g, x, p)))
#     print("Signature (r,s):", (r, s))
#     print("Toy demonstration only, not production DSS.")


# # -------------------- ELLIPTIC CURVE COMMON FUNCTIONS --------------------

# def ec_add(P, Q, a, p):
#     if P is None:
#         return Q
#     if Q is None:
#         return P
#     x, y = P
#     X, Y = Q
#     if x == X and (y+Y) % p == 0:
#         return None
#     if P != Q:
#         slope = ((Y-y) * inverse((X-x) % p, p)) % p
#     else:
#         if y == 0:
#             return None
#         slope = ((3*x*x+a) * inverse((2*y) % p, p)) % p
#     xx = (slope*slope-x-X) % p
#     yy = (slope*(x-xx)-y) % p
#     return xx, yy

# def ec_multiply(k, P, a, p):
#     result = None
#     while k:
#         if k & 1:
#             result = ec_add(result, P, a, p)
#         P = ec_add(P, P, a, p)
#         k >>= 1
#     return result

# def ec_setup():
#     a = int(input("Curve a: "))
#     b = int(input("Curve b: "))
#     p = int(input("Prime p: "))
#     if not prime(p) or (4*a**3 + 27*b**2) % p == 0:
#         raise ValueError("Need prime p and a valid curve.")
#     return a % p, b % p, p

# def ec_point(a, b, p, name="P"):
#     P = (int(input(name+" x: ")) % p, int(input(name+" y: ")) % p)
#     if (P[1]**2 - P[0]**3 - a*P[0] - b) % p:
#         raise ValueError("Point is not on the curve.")
#     return P

# def all_ec_points(a, b, p):
#     return [(x,y) for x in range(p) for y in range(p)
#             if (y*y-x*x*x-a*x-b) % p == 0]


# # -------------------- QUESTION 16 --------------------
# # Generate elliptic curve points and add two points

# def q16():
#     a,b,p = ec_setup()
#     print("Affine points:", all_ec_points(a,b,p), "and point at infinity O")
#     P = ec_point(a,b,p,"P")
#     Q = ec_point(a,b,p,"Q")
#     print("P + Q =", ec_add(P,Q,a,p))


# # -------------------- QUESTION 17 --------------------
# # Generate points and scalar multiplication

# def q17():
#     a,b,p = ec_setup()
#     print("Affine points:", all_ec_points(a,b,p))
#     P = ec_point(a,b,p)
#     k = int(input("Scalar k: "))
#     print("kP =", ec_multiply(k,P,a,p))


# # -------------------- QUESTION 18 --------------------
# # Solve small elliptic curve discrete logarithm

# def q18():
#     a,b,p = ec_setup()
#     P = ec_point(a,b,p,"Base P")
#     Q = ec_point(a,b,p,"Target Q")
#     R = None
#     for k in range(p*p+2*p+5):
#         if R == Q:
#             print("Scalar k =", k)
#             return
#         R = ec_add(R,P,a,p)
#     print("No scalar found in search range.")


# # -------------------- QUESTION 19 --------------------
# # Elliptic curve key exchange

# def q19():
#     a,b,p = ec_setup()
#     P = ec_point(a,b,p,"Base point")
#     x = int(input("Alice private scalar: "))
#     y = int(input("Bob private scalar: "))
#     A, B = ec_multiply(x,P,a,p), ec_multiply(y,P,a,p)
#     print("Alice public point:", A)
#     print("Bob public point:", B)
#     print("Alice shared point:", ec_multiply(x,B,a,p))
#     print("Bob shared point:", ec_multiply(y,A,a,p))


# # -------------------- QUESTION 20 --------------------
# # Elliptic curve ElGamal encryption and list all affine points

# def q20():
#     a,b,p = ec_setup()
#     print("All affine points:", all_ec_points(a,b,p), "and O")
#     G = ec_point(a,b,p,"Base G")
#     private = int(input("Receiver private key: "))
#     M = ec_point(a,b,p,"Message point")
#     k = int(input("Ephemeral key k: "))
#     public = ec_multiply(private,G,a,p)
#     C1 = ec_multiply(k,G,a,p)
#     C2 = ec_add(M,ec_multiply(k,public,a,p),a,p)
#     shared = ec_multiply(private,C1,a,p)
#     negative = None if shared is None else (shared[0],(-shared[1]) % p)
#     print("Public key:", public)
#     print("Ciphertext:", C1, C2)
#     print("Decrypted point:", ec_add(C2,negative,a,p))


# # -------------------- QUESTION 21 --------------------
# # ECC one-way function demonstration

# def q21():
#     a,b,p = ec_setup()
#     P = ec_point(a,b,p,"Base point")
#     k = int(input("Scalar k: "))
#     print("Input scalar:", k)
#     print("Output point kP:", ec_multiply(k,P,a,p))
#     print("Finding k from P and kP is the elliptic curve discrete logarithm problem.")


# # -------------------- QUESTION 22 --------------------
# # Logistic regression intrusion detection (small synthetic example)

# def q22():
#     try:
#         from sklearn.linear_model import LogisticRegression
#     except ImportError:
#         print("Install scikit-learn: python -m pip install scikit-learn")
#         return
#     X = [[10,0],[12,0],[15,1],[8,0],[100,8],[120,12],[90,7],[150,15],
#          [20,0],[18,1],[110,10],[130,9],[9,0],[140,14],[25,1],[105,8]]
#     y = [0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1]
#     model = LogisticRegression().fit(X,y)
#     packets = int(input("Packet count: "))
#     failed = int(input("Failed logins: "))
#     result = model.predict([[packets,failed]])[0]
#     print("Prediction:", "Possible intrusion" if result else "Normal")
#     print("Probability:", round(model.predict_proba([[packets,failed]])[0][1],3))


# # -------------------- MENU --------------------
# # QUESTION 1 code ends above; QUESTION 2 code begins above, etc.
# # Each function is separated by a question-name comment for easy identification.

# QUESTIONS = [
#     ("Caesar brute force, frequency, timing graph", q1),
#     ("Known plaintext Hill cipher attack", q2),
#     ("3x3 Hill decryption key", q3),
#     ("Check Hill key validity", q4),
#     ("String to integer matrix and back", q5),
#     ("AES SubBytes and ShiftRows", q6),
#     ("One SHA-256 round demonstration", q7),
#     ("Primes and hexadecimal bit operations", q8),
#     ("Primitive roots, factorization, Miller-Rabin", q9),
#     ("RSA factorization and encryption", q10),
#     ("Ten RSA public/private key pairs", q11),
#     ("Discrete logarithm", q12),
#     ("Diffie-Hellman MITM demonstration", q13),
#     ("Diffie-Hellman key exchange", q14),
#     ("DSS-style signature", q15),
#     ("Elliptic curve points and addition", q16),
#     ("Elliptic curve scalar multiplication", q17),
#     ("Elliptic curve discrete logarithm", q18),
#     ("Elliptic curve key exchange", q19),
#     ("Elliptic curve encryption", q20),
#     ("ECC one-way function", q21),
#     ("Logistic regression intrusion detection", q22)
# ]

# def main():
#     while True:
#         print("\\n========== CRYPTOGRAPHY LAB ==========")
#         for number, (name, _) in enumerate(QUESTIONS, 1):
#             print(f"{number}. {name}")
#         print("0. Exit")
#         choice = input("Enter question number: ")
#         if choice == "0":
#             break
#         try:
#             number = int(choice)
#             if 1 <= number <= 22:
#                 print("\\nQUESTION", number, "-", QUESTIONS[number-1][0])
#                 QUESTIONS[number-1][1]()
#             else:
#                 print("Choose a number from 1 to 22.")
#         except Exception as error:
#             print("Error:", error)

# if __name__ == "__main__":
#     main()
# '''
# p = Path("/mnt/data/crypto_lab_simple_22.py")
# p.write_text(code, encoding="utf-8")
# compile(code, str(p), "exec")
# print(f"Created and syntax-checked {p.name}: {len(code.splitlines())} lines")
